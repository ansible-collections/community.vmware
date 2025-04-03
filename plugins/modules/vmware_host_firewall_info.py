#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_firewall_info
short_description: Gathers info about an ESXi host's firewall configuration information
description:
- This module can be used to gather information about an ESXi host's firewall configuration information when ESXi hostname or Cluster name is given.
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
- name: Gather firewall info about all ESXi Host in given Cluster
  community.vmware.vmware_host_firewall_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
  delegate_to: localhost

- name: Gather firewall info about ESXi Host
  community.vmware.vmware_host_firewall_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
'''

RETURN = r'''
hosts_firewall_info:
    description: metadata about host's firewall configuration
    returned: on success
    type: dict
    sample: {
            "esxi_hostname_0001": [
                {
                    "allowed_hosts": {
                        "all_ip": true,
                        "ip_address": [
                            "10.10.10.1",
                        ],
                        "ip_network": [
                            "11.111.112.0/22",
                            "192.168.10.1/24"
                        ],
                    },
                    "enabled": true,
                    "key": "CIMHttpServer",
                    "rule": [
                        {
                            "direction": "inbound",
                            "end_port": null,
                            "port": 5988,
                            "port_type": "dst",
                            "protocol": "tcp"
                        }
                    ],
                    "service": "sfcbd-watchdog"
                },
            ]
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class FirewallInfoManager(PyVmomi):
    def __init__(self, module):
        super(FirewallInfoManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)

    @staticmethod
    def normalize_rule_set(rule_obj):
        rule_dict = dict()
        rule_dict['key'] = rule_obj.key
        rule_dict['service'] = rule_obj.service
        rule_dict['enabled'] = rule_obj.enabled
        rule_dict['rule'] = []

        for rule in rule_obj.rule:
            rule_set_dict = dict()
            rule_set_dict['port'] = rule.port
            rule_set_dict['end_port'] = rule.endPort
            rule_set_dict['direction'] = rule.direction
            rule_set_dict['port_type'] = rule.portType
            rule_set_dict['protocol'] = rule.protocol
            rule_dict['rule'].append(rule_set_dict)

        allowed_host = rule_obj.allowedHosts
        rule_allow_host = dict()
        rule_allow_host['ip_address'] = list(allowed_host.ipAddress)
        rule_allow_host['ip_network'] = [ip.network + "/" + str(ip.prefixLength) for ip in allowed_host.ipNetwork]
        rule_allow_host['all_ip'] = allowed_host.allIp
        rule_dict['allowed_hosts'] = rule_allow_host
        return rule_dict

    def gather_host_firewall_info(self):
        hosts_firewall_info = dict()
        for host in self.hosts:
            firewall_system = host.configManager.firewallSystem
            if firewall_system:
                hosts_firewall_info[host.name] = []
                for rule_set_obj in firewall_system.firewallInfo.ruleset:
                    hosts_firewall_info[host.name].append(self.normalize_rule_set(rule_obj=rule_set_obj))
        return hosts_firewall_info


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

    vmware_host_firewall = FirewallInfoManager(module)
    module.exit_json(changed=False, hosts_firewall_info=vmware_host_firewall.gather_host_firewall_info())


if __name__ == "__main__":
    main()
