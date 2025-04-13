#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Christian Kotte <christian.kotte@gmx.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_vmhba_info
short_description: Gathers info about vmhbas available on the given ESXi host
description:
- This module can be used to gather information about vmhbas available on the given ESXi host.
- If O(cluster_name) is provided, then vmhba information about all hosts from given cluster will be returned.
- If O(esxi_hostname) is provided, then vmhba information about given host system will be returned.
author:
- Christian Kotte (@ckotte)
options:
  esxi_hostname:
    description:
    - Name of the host system to work with.
    - Vmhba information about this ESXi server will be returned.
    - This parameter is required if O(cluster_name) is not specified.
    type: str
  cluster_name:
    description:
    - Name of the cluster from which all host systems will be used.
    - Vmhba information about each ESXi server will be returned for the given cluster.
    - This parameter is required if O(esxi_hostname) is not specified.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather info about vmhbas of all ESXi Host in the given Cluster
  community.vmware.vmware_host_vmhba_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_host_vmhbas

- name: Gather info about vmhbas of an ESXi Host
  community.vmware.vmware_host_vmhba_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_vmhbas
'''

RETURN = r'''
hosts_vmhbas_info:
    description:
    - dict with hostname as key and dict with vmhbas information as value.
    returned: hosts_vmhbas_info
    type: dict
    sample:
        {
            "10.76.33.204": {
                "vmhba_details": [
                    {
                        "adapter": "HPE Smart Array P440ar",
                        "bus": 3,
                        "device": "vmhba0",
                        "driver": "nhpsa",
                        "location": "0000:03:00.0",
                        "model": "Smart Array P440ar",
                        "node_wwn": "50:01:43:80:37:18:9e:a0",
                        "status": "unknown",
                        "type": "SAS"
                    },
                    {
                        "adapter": "QLogic Corp ISP2532-based 8Gb Fibre Channel to PCI Express HBA",
                        "bus": 5,
                        "device": "vmhba1",
                        "driver": "qlnativefc",
                        "location": "0000:05:00.0",
                        "model": "ISP2532-based 8Gb Fibre Channel to PCI Express HBA",
                        "node_wwn": "57:64:96:32:15:90:23:95:82",
                        "port_type": "unknown",
                        "port_wwn": "57:64:96:32:15:90:23:95:82",
                        "speed": 8,
                        "status": "online",
                        "type": "Fibre Channel"
                    },
                    {
                        "adapter": "QLogic Corp ISP2532-based 8Gb Fibre Channel to PCI Express HBA",
                        "bus": 8,
                        "device": "vmhba2",
                        "driver": "qlnativefc",
                        "location": "0000:08:00.0",
                        "model": "ISP2532-based 8Gb Fibre Channel to PCI Express HBA",
                        "node_wwn": "57:64:96:32:15:90:23:95:21",
                        "port_type": "unknown",
                        "port_wwn": "57:64:96:32:15:90:23:95:21",
                        "speed": 8,
                        "status": "online",
                        "type": "Fibre Channel"
                    }
                ],
            }
        }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class HostVmhbaMgr(PyVmomi):
    """Class to manage vmhba info"""

    def __init__(self, module):
        super(HostVmhbaMgr, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system.")

    def gather_host_vmhba_info(self):
        """Gather vmhba info"""
        hosts_vmhba_info = {}
        for host in self.hosts:
            host_vmhba_info = dict()
            host_st_system = host.configManager.storageSystem
            if host_st_system:
                device_info = host_st_system.storageDeviceInfo
                host_vmhba_info['vmhba_details'] = []
                for hba in device_info.hostBusAdapter:
                    hba_info = dict()
                    if hba.pci:
                        hba_info['location'] = hba.pci
                        for pci_device in host.hardware.pciDevice:
                            if pci_device.id == hba.pci:
                                hba_info['adapter'] = pci_device.vendorName + ' ' + pci_device.deviceName
                                break
                    else:
                        hba_info['location'] = 'PCI'
                    hba_info['device'] = hba.device
                    # contains type as string in format of 'key-vim.host.FibreChannelHba-vmhba1'
                    hba_type = hba.key.split(".")[-1].split("-")[0]
                    if hba_type == 'SerialAttachedHba':
                        hba_info['type'] = 'SAS'
                    elif hba_type == 'FibreChannelHba':
                        hba_info['type'] = 'Fibre Channel'
                    else:
                        hba_info['type'] = hba_type
                    hba_info['bus'] = hba.bus
                    hba_info['status'] = hba.status
                    hba_info['model'] = hba.model
                    hba_info['driver'] = hba.driver
                    try:
                        if isinstance(hba, (vim.host.FibreChannelHba, vim.host.FibreChannelOverEthernetHba)):
                            hba_info['node_wwn'] = self.format_number('%X' % hba.nodeWorldWideName)
                        else:
                            hba_info['node_wwn'] = self.format_number(hba.nodeWorldWideName)
                    except AttributeError:
                        pass
                    try:
                        if isinstance(hba, (vim.host.FibreChannelHba, vim.host.FibreChannelOverEthernetHba)):
                            hba_info['port_wwn'] = self.format_number('%X' % hba.portWorldWideName)
                        else:
                            hba_info['port_wwn'] = self.format_number(hba.portWorldWideName)
                    except AttributeError:
                        pass
                    try:
                        hba_info['port_type'] = hba.portType
                    except AttributeError:
                        pass
                    try:
                        hba_info['speed'] = hba.speed
                    except AttributeError:
                        pass
                    host_vmhba_info['vmhba_details'].append(hba_info)

            hosts_vmhba_info[host.name] = host_vmhba_info
        return hosts_vmhba_info

    @staticmethod
    def format_number(number):
        """Format number"""
        string = str(number)
        return ':'.join(a + b for a, b in zip(string[::2], string[1::2]))


def main():
    """Main"""
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str', required=False),
        esxi_hostname=dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True,
    )

    host_vmhba_mgr = HostVmhbaMgr(module)
    module.exit_json(changed=False, hosts_vmhbas_info=host_vmhba_mgr.gather_host_vmhba_info())


if __name__ == "__main__":
    main()
