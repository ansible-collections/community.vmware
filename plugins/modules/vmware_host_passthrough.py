#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: vmware_host_passthrough
short_description: Manage PCI device passthrough settings on host
author:
  - sky-joker (@sky-joker)
description:
  - This module can be managed PCI device passthrough settings on host.
options:
  cluster:
    description:
      - Name of the cluster from which all host systems will be used.
      - This parameter is required if O(esxi_hostname) is not specified.
    aliases:
      - cluster_name
    type: str
  esxi_hostname:
    description:
      - Name of the host system to work with.
      - This parameter is required if O(cluster_name) is not specified.
      - User can specify specific host from the cluster.
    type: str
  devices:
    description:
      - List of PCI device name or id.
    suboptions:
      device:
        description:
          - Name of PCI device to enable passthrough.
        aliases:
          - name
          - device_name
        type: str
    elements: dict
    required: true
    type: list
  state:
    description:
      - If V(state=present), passthrough of PCI device will be enabled.
      - If V(state=absent), passthrough of PCI device will be disabled.
    choices:
      - present
      - absent
    default: present
    type: str
extends_documentation_fragment:
  - vmware.vmware.base_options
"""

EXAMPLES = r"""
- name: Enable PCI device passthrough against the whole ESXi in a cluster
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    cluster: "{{ ccr1 }}"
    devices:
      - device_name: "Dual Band Wireless AC 3165"
    state: present

- name: Enable PCI device passthrough against one ESXi
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    devices:
      - device_name: "Dual Band Wireless AC 3165"
    state: present

- name: Enable PCI device passthrough with PCI ids
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    devices:
      - device: '0000:03:00.0'
      - device: '0000:00:02.0'
    state: present

- name: Disable PCI device passthrough against the whole ESXi in a cluster
  community.vmware.vmware_host_passthrough:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    cluster: "{{ ccr1 }}"
    devices:
      - device_name: "Dual Band Wireless AC 3165"
    state: absent
"""

RETURN = r"""
passthrough_configs:
  description:
    - list of that PCI devices have been enabled passthrough for each host system.
  returned: changed
  type: list
  elements: dict
  sample: >-
    [
        {
            "esxi-01.example.com": [
                {
                    "device_id": "0000:03:00.0",
                    "device_name": "Dual Band Wireless AC 3165",
                    "passthruEnabled": true
                }
            ]
        },
        {
            "esxi-02.example.com": [
                {
                    "device_id": "0000:03:00.0",
                    "device_name": "Dual Band Wireless AC 3165",
                    "passthruEnabled": true
                }
            ]
        }
    ]
"""

try:
    from pyVmomi import vim
except ImportError:
    pass

import copy
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.basic import AnsibleModule


class VMwareHostPassthrough(PyVmomi):
    def __init__(self, module):
        super(VMwareHostPassthrough, self).__init__(module)
        self.cluster = self.params['cluster']
        self.esxi_hostname = self.params['esxi_hostname']
        self.devices = self.params['devices']
        self.state = self.params['state']

        self.hosts = self.get_all_host_objs(cluster_name=self.cluster, esxi_host_name=self.esxi_hostname)
        # Looks for a specified ESXi host from a cluster if specified cluster and ESXi host.
        if self.cluster and self.esxi_hostname:
            self.hosts = [host_obj for host_obj in self.hosts if host_obj.name == self.esxi_hostname]
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system: %s" % self.esxi_hostname)

        self.result = dict(changed=False, passthrough_configs=[], diff={})

    def collect_pci_device_ids_for_supported_passthrough(self):
        """
        Collect device ids for supported passthrough from pciPassthruInfo.
        The condition for whether support passthrough is that passthruCapable property has True.
        """
        self.hosts_passthrough_pci_device_id = {}
        for host_obj in self.hosts:
            esxi_hostname = host_obj.name
            self.hosts_passthrough_pci_device_id[esxi_hostname] = {
                'host_obj': host_obj,
                'pci_device_ids': []
            }
            for pci_device in host_obj.config.pciPassthruInfo:
                if pci_device.passthruCapable:
                    self.hosts_passthrough_pci_device_id[esxi_hostname]['pci_device_ids'].append(pci_device)

    def collect_pci_devices_able_to_enable_passthrough(self):
        """
        Collect devices able to enable passthrough based on device id.
        """
        self.hosts_passthrough_pci_devices = []
        for esxi_hostname, value in self.hosts_passthrough_pci_device_id.items():
            pci_devices = []
            for device_id in value['pci_device_ids']:
                for device in value['host_obj'].hardware.pciDevice:
                    if device.id == device_id.id:
                        pci_devices.append({
                            'device_name': device.deviceName,
                            'device_id': device.id,
                            'passthruEnabled': device_id.passthruEnabled,
                        })
            self.hosts_passthrough_pci_devices.append({
                esxi_hostname: {
                    'host_obj': value['host_obj'],
                    'pci_devices': pci_devices
                }
            })

    def check_whether_devices_exist(self):
        """
        Check specified pci devices are exists.
        """
        self.existent_devices = []
        self.non_existent_devices = []

        # The keys use in checking pci devices existing.
        keys = ['device_name', 'device_id']

        for host_pci_device in self.hosts_passthrough_pci_devices:
            pci_devices = []
            for esxi_hostname, value in host_pci_device.items():
                for target_device in self.devices:
                    device = target_device['device']
                    if device in [pci_device.get(key) for key in keys for pci_device in value['pci_devices']]:
                        pci_devices.append(
                            [
                                pci_device for pci_device in value['pci_devices']
                                if device == pci_device['device_name'] or device == pci_device['device_id']
                            ]
                        )
                    else:
                        self.non_existent_devices.append(device)
                self.existent_devices.append({
                    esxi_hostname: {
                        'host_obj': value['host_obj'],
                        'checked_pci_devices': self.de_duplication(sum(pci_devices, []))
                    }
                })

    def diff_passthrough_config(self):
        """
        Check there are differences between a new and existing config each ESXi host.
        """
        # Make the diff_config variable to check the difference between a new and existing config.
        self.diff_config = dict(before={}, after={})

        self.change_flag = False
        self.host_target_device_to_change_configuration = {}
        state = True if self.state == "present" else False
        for host_has_checked_pci_devices in self.existent_devices:
            for esxi_hostname, value in host_has_checked_pci_devices.items():
                for key in 'before', 'after':
                    self.diff_config[key][esxi_hostname] = []
                self.host_target_device_to_change_configuration[esxi_hostname] = {
                    'host_obj': None,
                    'new_configs': []
                }
                for target_device in self.devices:
                    device = target_device['device']
                    for checked_pci_device in value['checked_pci_devices']:
                        if device == checked_pci_device['device_name'] or device == checked_pci_device['device_id']:
                            before = dict(checked_pci_device)
                            after = dict(copy.deepcopy(checked_pci_device))

                            if state != checked_pci_device['passthruEnabled']:
                                self.change_flag = True
                                after['passthruEnabled'] = state

                                self.host_target_device_to_change_configuration[esxi_hostname]['new_configs'].append(after)
                            self.host_target_device_to_change_configuration[esxi_hostname]['host_obj'] = value['host_obj']
                            self.diff_config['before'][esxi_hostname].append(before)
                            self.diff_config['after'][esxi_hostname].append(after)

                # De-duplicate pci device data and sort.
                self.diff_config['before'][esxi_hostname] = sorted(
                    self.de_duplication(self.diff_config['before'][esxi_hostname]),
                    key=lambda d: d['device_name']
                )
                self.diff_config['after'][esxi_hostname] = sorted(
                    self.de_duplication(self.diff_config['after'][esxi_hostname]),
                    key=lambda d: d['device_name']
                )

    def generate_passthrough_configurations_to_be_applied(self):
        """
        Generate configs to enable or disable PCI device passthrough.
        The configs are generated against only ESXi host has PCI device to be changed.
        """
        self.host_passthrough_configs = {}
        for esxi_hostname, value in self.host_target_device_to_change_configuration.items():
            self.host_passthrough_configs[esxi_hostname] = {
                'host_obj': value['host_obj'],
                'generated_new_configs': []
            }
            if value['new_configs']:
                state = True if self.state == "present" else False
                for new_config in value['new_configs']:
                    config = vim.host.PciPassthruConfig()
                    config.passthruEnabled = state
                    config.id = new_config['device_id']
                    self.host_passthrough_configs[esxi_hostname]['generated_new_configs'].append(config)

    def de_duplication(self, data):
        """
        De-duplicate dictionaries in a list.
        """
        return [
            dict(s) for s in set(frozenset(d.items()) for d in data)
        ]

    def execute(self):
        self.collect_pci_device_ids_for_supported_passthrough()
        self.collect_pci_devices_able_to_enable_passthrough()

        self.check_whether_devices_exist()
        if self.non_existent_devices:
            self.module.fail_json(msg="Failed to fined device: %s" % list(set(self.non_existent_devices)))

        self.diff_passthrough_config()
        if self.change_flag and self.module.check_mode is False:
            self.generate_passthrough_configurations_to_be_applied()
            for value in self.host_passthrough_configs.values():
                try:
                    host_obj = value['host_obj']
                    config = value['generated_new_configs']
                    host_obj.configManager.pciPassthruSystem.UpdatePassthruConfig(config)
                except Exception as e:
                    self.module.fail_json(msg="Failed to operate PCI device passthrough: %s" % e)

        # ESXi host configuration will be included in the result if it will be changed.
        self.result['passthrough_configs'] = [
            {
                esxi_hostname: value['new_configs']
            } for esxi_hostname, value in self.host_target_device_to_change_configuration.items() if value['new_configs']
        ]
        self.result['changed'] = self.change_flag
        self.result['diff'] = self.diff_config
        self.module.exit_json(**self.result)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster=dict(type='str', aliases=['cluster_name']),
        esxi_hostname=dict(type='str'),
        devices=dict(type='list', elements='dict', required=True,
                     options=dict(
                         device=dict(type='str', aliases=['name', 'device_name'])
                     )),
        state=dict(type='str', default='present', choices=['present', 'absent'])
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           required_one_of=[
                               ['cluster', 'esxi_hostname']
                           ],
                           supports_check_mode=True)

    vmware_host_passthrough = VMwareHostPassthrough(module)
    vmware_host_passthrough.execute()


if __name__ == "__main__":
    main()
