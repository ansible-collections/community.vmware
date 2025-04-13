#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_dns_info
short_description: Gathers info about an ESXi host's DNS configuration information
description:
- This module can be used to gather information about an ESXi host's DNS configuration information when ESXi hostname or Cluster name is given.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  cluster_name:
    description:
    - Name of the cluster from which the ESXi host belong to.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname to gather information from.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather DNS info about all ESXi Hosts in given Cluster
  community.vmware.vmware_host_dns_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
  delegate_to: localhost

- name: Gather DNS info about ESXi Host
  community.vmware.vmware_host_dns_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
'''

RETURN = r'''
hosts_dns_info:
    description: metadata about DNS config from given cluster / host system
    returned: always
    type: dict
    sample: {
                "DC0_C0_H0": {
                    "dhcp": true,
                    "domain_name": "localdomain",
                    "host_name": "localhost",
                    "ip_address": [
                        "8.8.8.8"
                    ],
                    "search_domain": [
                        "localdomain"
                    ],
                    "virtual_nic_device": "vmk0"
                }
            }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VmwareDnsInfoManager(PyVmomi):
    def __init__(self, module):
        super(VmwareDnsInfoManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)

    def gather_dns_info(self):
        hosts_info = {}
        for host in self.hosts:
            host_info = {}
            dns_config = host.config.network.dnsConfig
            host_info['dhcp'] = dns_config.dhcp
            host_info['virtual_nic_device'] = dns_config.virtualNicDevice
            host_info['host_name'] = dns_config.hostName
            host_info['domain_name'] = dns_config.domainName
            host_info['ip_address'] = list(dns_config.address)
            host_info['search_domain'] = list(dns_config.searchDomain)
            hosts_info[host.name] = host_info
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

    vmware_dns_config = VmwareDnsInfoManager(module)
    module.exit_json(changed=False, hosts_dns_info=vmware_dns_config.gather_dns_info())


if __name__ == "__main__":
    main()
