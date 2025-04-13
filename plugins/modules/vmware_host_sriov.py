#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (C) 2020, Viktor Tsymbalyuk
# Copyright: (C) 2020, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_sriov
short_description: Manage SR-IOV settings on host
description:
- This module can be used to configure, enable or disable SR-IOV functions on ESXi host.
- Module does not reboot the host after changes, but puts it in output "rebootRequired" state.
- User can specify an ESXi hostname or Cluster name. In case of cluster name, all ESXi hosts are updated.
author:
- Viktor Tsymbalyuk (@victron)
options:
  esxi_hostname:
    description:
    - Name of the host system to work with.
    - This parameter is required if O(cluster_name) is not specified.
    - User can specify specific host from the cluster.
    type: str
  cluster_name:
    description:
    - Name of the cluster from which all host systems will be used.
    - This parameter is required if O(esxi_hostname) is not specified.
    type: str
  vmnic:
    description:
    - Interface name, like vmnic0.
    type: str
    required: true
  num_virt_func:
    description:
    - number of functions to activate on interface.
    - 0 means SR-IOV disabled.
    - number greater than 0 means SR-IOV enabled.
    type: int
    required: true
  sriov_on:
    description:
    - optional parameter, related to O(num_virt_func).
    - SR-IOV can be enabled only if O(num_virt_func) > 0.
    type: bool
    required: false
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: enable SR-IOV on vmnic0 with 8 functions
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: true
    num_virt_func: 8

- name: enable SR-IOV on already enabled interface vmnic0
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: true
    num_virt_func: 8

- name: enable SR-IOV on vmnic0 with big number of functions
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: true
    num_virt_func: 100
  ignore_errors: true

- name: disable SR-IOV on vmnic0
  community.vmware.vmware_host_sriov:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi1 }}"
    vmnic: vmnic0
    sriov_on: false
    num_virt_func: 0
'''

RETURN = r'''
host_sriov_diff:
    description:
    - contains info about SR-IOV status on vmnic before, after and requested changes
    - sometimes vCenter slowly update info, as result "after" contains same info as "before"
      need to run again in check_mode or reboot host, as ESXi requested
    returned: always
    type: dict
    "sample": {
        "changed": true,
        "diff": {
            "after": {
                "host_test": {
                    "sriovActive": false,
                    "sriovEnabled": true,
                    "maxVirtualFunctionSupported": 63,
                    "numVirtualFunction": 0,
                    "numVirtualFunctionRequested": 8,
                    "rebootRequired": true,
                    "sriovCapable": true
                }
            },
            "before": {
                "host_test": {
                    "sriovActive": false,
                    "sriovEnabled": false,
                    "maxVirtualFunctionSupported": 63,
                    "numVirtualFunction": 0,
                    "numVirtualFunctionRequested": 0,
                    "rebootRequired": false,
                    "sriovCapable": true
                }
            },
            "changes": {
                "host_test": {
                    "numVirtualFunction": 8,
                    "rebootRequired": true,
                    "sriovEnabled": true
                }
            }
        }
    }
'''


try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from time import sleep


class VmwareAdapterConfigManager(PyVmomi):
    """Class to configure SR-IOV settings"""

    def __init__(self, module):
        super(VmwareAdapterConfigManager, self).__init__(module)
        cluster_name = self.params.get("cluster_name", None)
        esxi_host_name = self.params.get("esxi_hostname", None)

        self.vmnic = self.params.get("vmnic", None)
        self.num_virt_func = self.params.get("num_virt_func", None)
        self.sriov_on = self.params.get("sriov_on", None)

        #  prepare list of hosts to work with them
        self.hosts = self.get_all_host_objs(
            cluster_name=cluster_name, esxi_host_name=esxi_host_name
        )
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system.")
        self.results = {"before": {}, "after": {}, "changes": {}}

    def sanitize_params(self):
        """checks user input, raise error if input incompatible
        :return : None
        """

        if self.num_virt_func < 0:
            self.module.fail_json(msg="allowed value for num_virt_func >= 0")
        if self.num_virt_func == 0:
            if self.sriov_on is True:
                self.module.fail_json(
                    msg="with sriov_on == true, allowed value for num_virt_func > 0"
                )
            self.sriov_on = False  # fill value, if user not provided

        if self.num_virt_func > 0:
            if self.sriov_on is False:
                self.module.fail_json(
                    msg="with sriov_on == false, allowed value for num_virt_func is 0"
                )
            self.sriov_on = True  # fill value, if user not provided

    def check_compatibility(self, before, hostname):
        """
        checks hardware compatibility with user input, raise error if input incompatible
        :before     : dict, of params on target interface before changing
        :hostname   : str, hosthame
        :return     : None
        """
        if self.num_virt_func > 0:
            if not before["sriovCapable"]:
                self.module.fail_json(
                    msg="sriov not supported on host= %s, nic= %s" % (hostname, self.vmnic)
                )

        if before["maxVirtualFunctionSupported"] < self.num_virt_func:
            self.module.fail_json(
                msg="maxVirtualFunctionSupported= %d on %s" % (before["maxVirtualFunctionSupported"], self.vmnic)
            )

    def make_diff(self, before, hostname):
        """
        preparing diff - changes which will be applied
        :before     : dict, of params on target interface before changing
        :hostname   : str, hosthame
        :return     : dict, of changes which is going to apply
        """
        diff = {}
        change = False
        change_msg = ""

        if before["sriovEnabled"] != self.sriov_on:
            diff["sriovEnabled"] = self.sriov_on
            change = True

        if before["numVirtualFunction"] != self.num_virt_func:
            if before["numVirtualFunctionRequested"] != self.num_virt_func:
                diff["numVirtualFunction"] = self.num_virt_func
                change = True
            else:
                change_msg = "Not active (looks like not rebooted) "

        if not change:
            change_msg += "No any changes, already configured "
        diff["msg"] = change_msg
        diff["change"] = change

        return diff

    def set_host_state(self):
        """Checking and applying ESXi host configuration one by one,
        from prepared list of hosts in `self.hosts`.
        For every host applied:
        - user input checking done via calling `sanitize_params` method
        - checks hardware compatibility with user input `check_compatibility`
        - conf changes created via `make_diff`
        - changes applied via calling `_update_sriov` method
        - host state before and after via calling `_check_sriov`
        """
        self.sanitize_params()
        change_list = []
        changed = False
        for host in self.hosts:
            self.results["before"][host.name] = {}
            self.results["after"][host.name] = {}
            self.results["changes"][host.name] = {}
            self.results["before"][host.name] = self._check_sriov(host)

            self.check_compatibility(self.results["before"][host.name], host.name)
            diff = self.make_diff(self.results["before"][host.name], host.name)
            self.results["changes"][host.name] = diff

            if not diff["change"]:
                change_list.append(False)
                self.results["after"][host.name] = self._check_sriov(host)
                if (self.results["before"][host.name]["rebootRequired"] != self.results["after"][host.name]["rebootRequired"]):
                    self.results["changes"][host.name]["rebootRequired"] = self.results["after"][host.name]["rebootRequired"]
                continue

            success = self._update_sriov(host, self.sriov_on, self.num_virt_func)
            if success:
                change_list.append(True)
            else:
                change_list.append(False)

            self.results["after"][host.name] = self._check_sriov(host)
            self.results["changes"][host.name].update(
                {
                    "rebootRequired": self.results["after"][host.name]["rebootRequired"]
                }
            )

        if any(change_list):
            changed = True
        self.module.exit_json(changed=changed, diff=self.results)

    def _check_sriov(self, host):
        pnic_info = {}
        pnic_info["rebootRequired"] = host.summary.rebootRequired
        for pci_device in host.configManager.pciPassthruSystem.pciPassthruInfo:
            if pci_device.id == self._getPciId(host):
                try:
                    if pci_device.sriovCapable:
                        pnic_info["sriovCapable"] = True
                        pnic_info["sriovEnabled"] = pci_device.sriovEnabled
                        pnic_info["sriovActive"] = pci_device.sriovActive
                        pnic_info["numVirtualFunction"] = pci_device.numVirtualFunction
                        pnic_info[
                            "numVirtualFunctionRequested"
                        ] = pci_device.numVirtualFunctionRequested
                        pnic_info[
                            "maxVirtualFunctionSupported"
                        ] = pci_device.maxVirtualFunctionSupported
                    else:
                        pnic_info["sriovCapable"] = False
                except AttributeError:
                    pnic_info["sriovCapable"] = False
                break
        return pnic_info

    def _getPciId(self, host):
        for pnic in host.config.network.pnic:
            if pnic.device == self.vmnic:
                return pnic.pci
        self.module.fail_json(msg="No nic= %s on host= %s" % (self.vmnic, host.name))

    def _update_sriov(self, host, sriovEnabled, numVirtualFunction):
        nic_sriov = vim.host.SriovConfig()
        nic_sriov.id = self._getPciId(host)
        nic_sriov.sriovEnabled = sriovEnabled
        nic_sriov.numVirtualFunction = numVirtualFunction

        try:
            if not self.module.check_mode:
                host.configManager.pciPassthruSystem.UpdatePassthruConfig([nic_sriov])
                # looks only for refresh info
                host.configManager.pciPassthruSystem.Refresh()
                sleep(2)  # TODO: needed method to know that host updated info
                return True
            return False
        except vim.fault.HostConfigFault as config_fault:
            self.module.fail_json(
                msg="Failed to configure SR-IOV for host= %s due to : %s"
                % (host.name, to_native(config_fault.msg))
            )
            return False


def main():
    """Main"""
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type="str", required=False),
        esxi_hostname=dict(type="str", required=False),
        vmnic=dict(type="str", required=True),
        num_virt_func=dict(type="int", required=True),
        sriov_on=dict(type="bool", required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ["cluster_name", "esxi_hostname"],
        ],
        supports_check_mode=True,
    )

    vmware_host_adapter_config = VmwareAdapterConfigManager(module)
    vmware_host_adapter_config.set_host_state()


if __name__ == "__main__":
    main()
