#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vmkernel_info
short_description: Gathers VMKernel info about an ESXi host
description:
- This module can be used to gather VMKernel information about an ESXi host from given ESXi hostname or cluster name.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  cluster_name:
    description:
    - Name of the cluster.
    - VMKernel information about each ESXi server will be returned for the given cluster.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname.
    - VMKernel information about this ESXi server will be returned.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather VMKernel info about all ESXi Host in given Cluster
  community.vmware.vmware_vmkernel_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
  delegate_to: localhost
  register: cluster_host_vmks

- name: Gather VMKernel info about ESXi Host
  community.vmware.vmware_vmkernel_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_vmks
'''

RETURN = r'''
host_vmk_info:
    description: metadata about VMKernel present on given host system
    returned: success
    type: dict
    sample:
        {
            "10.76.33.208": [
                {
                    "device": "vmk0",
                    "dhcp": true,
                    "enable_ft": false,
                    "enable_management": true,
                    "enable_vmotion": false,
                    "enable_vsan": false,
                    "ipv4_address": "10.76.33.28",
                    "ipv4_subnet_mask": "255.255.255.0",
                    "key": "key-vim.host.VirtualNic-vmk0",
                    "mac": "52:54:00:12:50:ce",
                    "mtu": 1500,
                    "portgroup": "Management Network",
                    "stack": "defaultTcpipStack"
                },
            ]
        }

'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VmkernelInfoManager(PyVmomi):
    def __init__(self, module):
        super(VmkernelInfoManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        self.service_type_vmks = dict()
        self.get_all_vmks_by_service_type()

    def get_all_vmks_by_service_type(self):
        """
        Function to return information about service types and VMKernel

        """
        for host in self.hosts:
            self.service_type_vmks[host.name] = dict(vmotion=[], vsan=[], management=[], faultToleranceLogging=[])
            for service_type in self.service_type_vmks[host.name].keys():
                vmks_list = self.query_service_type_for_vmks(host, service_type)
                self.service_type_vmks[host.name][service_type] = vmks_list

    def query_service_type_for_vmks(self, host_system, service_type):
        """
        Function to return list of VMKernels
        Args:
            host_system: Host system managed object
            service_type: Name of service type

        Returns: List of VMKernel which belongs to that service type

        """
        vmks_list = []
        query = None
        try:
            query = host_system.configManager.virtualNicManager.QueryNetConfig(service_type)
        except vim.fault.HostConfigFault as config_fault:
            self.module.fail_json(msg="Failed to get all VMKs for service type %s due to"
                                      " host config fault : %s" % (service_type, to_native(config_fault.msg)))
        except vmodl.fault.InvalidArgument as invalid_argument:
            self.module.fail_json(msg="Failed to get all VMKs for service type %s due to"
                                      " invalid arguments : %s" % (service_type, to_native(invalid_argument.msg)))
        except Exception as e:
            self.module.fail_json(msg="Failed to get all VMKs for service type %s due to"
                                      "%s" % (service_type, to_native(e)))

        if not query or not query.selectedVnic:
            return vmks_list
        selected_vnics = list(query.selectedVnic)
        vnics_with_service_type = [vnic.device for vnic in query.candidateVnic if vnic.key in selected_vnics]
        return vnics_with_service_type

    def gather_host_vmk_info(self):
        hosts_info = {}

        for host in self.hosts:
            host_vmk_info = []
            host_network_system = host.config.network
            if host_network_system:
                vmks_config = host.config.network.vnic
                for vmk in vmks_config:
                    host_vmk_info.append(dict(
                        device=vmk.device,
                        key=vmk.key,
                        portgroup=vmk.portgroup,
                        ipv4_address=vmk.spec.ip.ipAddress,
                        ipv4_subnet_mask=vmk.spec.ip.subnetMask,
                        dhcp=vmk.spec.ip.dhcp,
                        mac=vmk.spec.mac,
                        mtu=vmk.spec.mtu,
                        stack=vmk.spec.netStackInstanceKey,
                        enable_vsan=vmk.device in self.service_type_vmks[host.name]['vsan'],
                        enable_vmotion=vmk.device in self.service_type_vmks[host.name]['vmotion'],
                        enable_management=vmk.device in self.service_type_vmks[host.name]['management'],
                        enable_ft=vmk.device in self.service_type_vmks[host.name]['faultToleranceLogging'],
                    )
                    )
            hosts_info[host.name] = host_vmk_info
        return hosts_info


def main():
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
        supports_check_mode=True
    )

    vmware_vmk_config = VmkernelInfoManager(module)
    module.exit_json(changed=False, host_vmk_info=vmware_vmk_config.gather_host_vmk_info())


if __name__ == "__main__":
    main()
