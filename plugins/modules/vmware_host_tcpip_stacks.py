#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_host_tcpip_stacks
short_description: Manage the TCP/IP Stacks configuration of ESXi host
author:
  - sky-joker (@sky-joker)
description:
  - This module can be used to modify the TCP/IP stacks configuration.
options:
  esxi_hostname:
    description:
      - Name of the ESXi host.
    type: str
    required: true
  default:
    description:
      - The TCP/IP stacks configuration of the I(default).
    suboptions:
      hostname:
        description:
          - The host name of the ESXi host.
        type: str
        required: true
      domain:
        description:
          - The domain name portion of the DNS name.
        type: str
        required: true
      preferred_dns:
        description:
          - The IP address of the preferred dns server.
        type: str
      alternate_dns:
        description:
          - The IP address of the alternate dns server.
        type: str
      search_domains:
        description:
          - The domain in which to search for hosts, placed in order of preference.
        default: []
        elements: str
        type: list
      gateway:
        description:
          - The ipv4 gateway address.
        type: str
      ipv6_gateway:
        description:
          - The ipv6 gateway address.
        type: str
      congestion_algorithm:
        description:
          - The TCP congest control algorithm.
        choices:
          - newreno
          - cubic
        default: newreno
        type: str
      max_num_connections:
        description:
          - The maximum number of socket connection that are requested.
        default: 11000
        type: int
    type: dict
  provisioning:
    description:
      - The TCP/IP stacks configuration of the I(provisioning).
    suboptions:
      gateway:
        description:
          - The ipv4 gateway address.
        type: str
      ipv6_gateway:
        description:
          - The ipv6 gateway address.
        type: str
      congestion_algorithm:
        description:
          - The TCP congest control algorithm.
        choices:
          - newreno
          - cubic
        default: newreno
        type: str
      max_num_connections:
        description:
          - The maximum number of socket connection that are requested.
        default: 11000
        type: int
    type: dict
  vmotion:
    description:
      - The TCP/IP stacks configuration of the I(vmotion).
    suboptions:
      gateway:
        description:
          - The ipv4 gateway address.
        type: str
      ipv6_gateway:
        description:
          - The ipv6 gateway address.
        type: str
      congestion_algorithm:
        description:
          - The TCP congest control algorithm.
        choices:
          - newreno
          - cubic
        default: newreno
        type: str
      max_num_connections:
        description:
          - The maximum number of socket connection that are requested.
        default: 11000
        type: int
    type: dict
  vxlan:
    description:
      - The TCP/IP stacks configuration of the I(vxlan).
    suboptions:
      gateway:
        description:
          - The ipv4 gateway address.
        type: str
      ipv6_gateway:
        description:
          - The ipv6 gateway address.
        type: str
      congestion_algorithm:
        description:
          - The TCP congest control algorithm.
        choices:
          - newreno
          - cubic
        default: newreno
        type: str
      max_num_connections:
        description:
          - The maximum number of socket connection that are requested.
        default: 11000
        type: int
    type: dict
    aliases:
      - nsx_overlay
extends_documentation_fragment:
  - vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Update the TCP/IP stack configuration of the default
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    default:
      hostname: "{{ esxi_hostname }}"
      domain: example.com
      preferred_dns: 192.168.10.1
      alternate_dns: 192.168.20.1
      search_domains:
        - hoge.com
        - fuga.com
      gateway: 192.168.10.1
      congestion_algorithm: cubic
      max_num_connections: 12000

- name: Update the TCP/IP stack configuration of the provisioning
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    provisioning:
      congestion_algorithm: newreno
      max_num_connections: 12000
      gateway: 10.10.10.254

- name: Update the TCP/IP stack configuration of the default and provisioning
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    default:
      hostname: "{{ esxi_hostname }}"
      domain: example.com
      preferred_dns: 192.168.10.1
      alternate_dns: 192.168.20.1
      search_domains:
        - hoge.com
        - fuga.com
      gateway: 192.168.10.1
      congestion_algorithm: cubic
      max_num_connections: 12000
    provisioning:
      congestion_algorithm: newreno
      max_num_connections: 12000
      gateway: 10.10.10.254

- name: Update the ipv6 gateway of the provisioning TCP/IP stack
  community.vmware.vmware_host_tcpip_stacks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi_hostname }}"
    provisioning:
      ipv6_gateway: ::ffff:6440:301
'''

RETURN = r'''
default:
  description: dict of the TCP/IP stack configuration of the default.
  returned: always
  type: dict
  sample: >-
    {
        "alternate_dns": "192.168.20.1",
        "congestion_algorithm": "cubic",
        "domain": "example.com",
        "gateway": "192.168.10.1",
        "ipv6_gateway", null,
        "hostname": "esxi-test03",
        "max_num_connections": 12000,
        "preferred_dns": "192.168.10.1",
        "search_domains": [
            "hoge.com",
            "fuga.com"
        ]
    }
provisioning:
  description: dict of the TCP/IP stack configuration of the provisioning.
  returned: always
  type: dict
  sample: >-
    {
        "congestion_algorithm": "newreno",
        "gateway": "10.10.10.254",
        "ipv6_gateway": null,
        "max_num_connections": 12000
    }
vmotion:
  description: dict of the TCP/IP stack configuration of the vmotion.
  returned: always
  type: dict
  sample: >-
    {
        "congestion_algorithm": "newreno",
        "gateway": null,
        "ipv6_gateway": null,
        "max_num_connections": 11000
    }
vxlan:
  description: dict of the TCP/IP stack configuration of the vxlan.
  returned: always
  type: dict
  sample: >-
    {
        "congestion_algorithm": "newreno",
        "gateway": null,
        "ipv6_gateway": null,
        "max_num_connections": 11000
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

try:
    from collections import OrderedDict
except ImportError:
    try:
        from ordereddict import OrderedDict
    except ImportError:
        pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_text
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class VmwareHostTcpipStack(PyVmomi):
    def __init__(self, module):
        super(VmwareHostTcpipStack, self).__init__(module)
        self.esxi_hostname = self.params['esxi_hostname']
        self.default = self.params['default']
        self.provisioning = self.params['provisioning']
        self.vmotion = self.params['vmotion']
        self.vxlan = self.params['vxlan']

        self.net_stack_instance_keys = {
            "default": "defaultTcpipStack",
            "vmotion": "vmotion",
            "provisioning": "vSphereProvisioning",
            "vxlan": "vxlan"
        }

    def check_enabled_net_stack_instance(self):
        """
        Make sure if enabled each the tcpip stack item in ESXi host.
        """
        self.enabled_net_stack_instance = {
            "default": False,
            "vmotion": False,
            "provisioning": False,
            "vxlan": False
        }
        for net_stack_instance in self.host_obj.runtime.networkRuntimeInfo.netStackInstanceRuntimeInfo:
            if net_stack_instance.netStackInstanceKey == self.net_stack_instance_keys['default']:
                self.enabled_net_stack_instance['default'] = True

            if net_stack_instance.netStackInstanceKey == self.net_stack_instance_keys['provisioning']:
                self.enabled_net_stack_instance['provisioning'] = True

            if net_stack_instance.netStackInstanceKey == self.net_stack_instance_keys['vmotion']:
                self.enabled_net_stack_instance['vmotion'] = True

            if net_stack_instance.netStackInstanceKey == self.net_stack_instance_keys['vxlan']:
                self.enabled_net_stack_instance['vxlan'] = True

    def get_net_stack_instance_config(self):
        """
        Get a configuration of tcpip stack item if it is enabled.
        """
        self.exist_net_stack_instance_config = {}
        for key, value in self.enabled_net_stack_instance.items():
            if value is True:
                for net_stack_instance in self.host_obj.config.network.netStackInstance:
                    if net_stack_instance.key == self.net_stack_instance_keys[key]:
                        self.exist_net_stack_instance_config[key] = net_stack_instance

    def diff_net_stack_instance_config(self):
        """
        Check the difference between a new and existing config.
        """
        self.change_flag = False

        # Make the diff_config variable to check the difference between a new and existing config.
        self.diff_config = dict(before={}, after={})
        for key, value in self.enabled_net_stack_instance.items():
            if value is True:
                self.diff_config['before'][key] = {}
                self.diff_config['after'][key] = {}

        if self.enabled_net_stack_instance['default']:
            exist_dns_servers = self.exist_net_stack_instance_config['default'].dnsConfig.address
            for key in 'before', 'after':
                self.diff_config[key]['default'] = dict(
                    hostname=self.exist_net_stack_instance_config['default'].dnsConfig.hostName,
                    domain=self.exist_net_stack_instance_config['default'].dnsConfig.domainName,
                    preferred_dns=exist_dns_servers[0] if [dns for dns in exist_dns_servers if exist_dns_servers.index(dns) == 0] else None,
                    alternate_dns=exist_dns_servers[1] if [dns for dns in exist_dns_servers if exist_dns_servers.index(dns) == 1] else None,
                    search_domains=self.exist_net_stack_instance_config['default'].dnsConfig.searchDomain,
                    gateway=self.exist_net_stack_instance_config['default'].ipRouteConfig.defaultGateway,
                    ipv6_gateway=self.exist_net_stack_instance_config['default'].ipRouteConfig.ipV6DefaultGateway,
                    congestion_algorithm=self.exist_net_stack_instance_config['default'].congestionControlAlgorithm,
                    max_num_connections=self.exist_net_stack_instance_config['default'].requestedMaxNumberOfConnections
                )
                if self.default:
                    if self.diff_config['before']['default']['hostname'] != self.default['hostname']:
                        self.change_flag = True
                        self.diff_config['after']['default']['hostname'] = self.default['hostname']
                    if self.diff_config['before']['default']['domain'] != self.default['domain']:
                        self.change_flag = True
                        self.diff_config['after']['default']['domain'] = self.default['domain']
                    if self.diff_config['before']['default']['preferred_dns'] != self.default['preferred_dns']:
                        self.change_flag = True
                        self.diff_config['after']['default']['preferred_dns'] = self.default['preferred_dns']
                    if self.diff_config['before']['default']['alternate_dns'] != self.default['alternate_dns']:
                        self.change_flag = True
                        self.diff_config['after']['default']['alternate_dns'] = self.default['alternate_dns']
                    if self.diff_config['before']['default']['search_domains'] != self.default['search_domains']:
                        self.change_flag = True
                        self.diff_config['after']['default']['search_domains'] = self.default['search_domains']
                    if self.diff_config['before']['default']['gateway'] != self.default['gateway']:
                        self.change_flag = True
                        self.diff_config['after']['default']['gateway'] = self.default['gateway']
                    if self.diff_config['before']['default']['ipv6_gateway'] != self.default['ipv6_gateway']:
                        self.change_flag = True
                        self.diff_config['after']['default']['ipv6_gateway'] = self.default['ipv6_gateway']
                    if self.diff_config['before']['default']['congestion_algorithm'] != self.default['congestion_algorithm']:
                        self.change_flag = True
                        self.diff_config['after']['default']['congestion_algorithm'] = self.default['congestion_algorithm']
                    if self.diff_config['before']['default']['max_num_connections'] != self.default['max_num_connections']:
                        self.change_flag = True
                        self.diff_config['after']['default']['max_num_connections'] = self.default['max_num_connections']

        if self.enabled_net_stack_instance['provisioning']:
            for key in 'before', 'after':
                self.diff_config[key]['provisioning'] = dict(
                    gateway=self.exist_net_stack_instance_config['provisioning'].ipRouteConfig.defaultGateway,
                    ipv6_gateway=self.exist_net_stack_instance_config['provisioning'].ipRouteConfig.ipV6DefaultGateway,
                    congestion_algorithm=self.exist_net_stack_instance_config['provisioning'].congestionControlAlgorithm,
                    max_num_connections=self.exist_net_stack_instance_config['provisioning'].requestedMaxNumberOfConnections
                )
            if self.provisioning:
                if self.diff_config['before']['provisioning']['gateway'] != self.provisioning['gateway']:
                    self.change_flag = True
                    self.diff_config['after']['provisioning']['gateway'] = self.provisioning['gateway']
                if self.diff_config['before']['provisioning']['ipv6_gateway'] != self.provisioning['ipv6_gateway']:
                    self.change_flag = True
                    self.diff_config['after']['provisioning']['ipv6_gateway'] = self.provisioning['ipv6_gateway']
                if self.diff_config['before']['provisioning']['max_num_connections'] != self.provisioning['max_num_connections']:
                    self.change_flag = True
                    self.diff_config['after']['provisioning']['max_num_connections'] = self.provisioning['max_num_connections']
                if self.diff_config['before']['provisioning']['congestion_algorithm'] != self.provisioning['congestion_algorithm']:
                    self.change_flag = True
                    self.diff_config['after']['provisioning']['congestion_algorithm'] = self.provisioning['congestion_algorithm']

        if self.enabled_net_stack_instance['vmotion']:
            for key in 'before', 'after':
                self.diff_config[key]['vmotion'] = dict(
                    gateway=self.exist_net_stack_instance_config['vmotion'].ipRouteConfig.defaultGateway,
                    ipv6_gateway=self.exist_net_stack_instance_config['vmotion'].ipRouteConfig.ipV6DefaultGateway,
                    congestion_algorithm=self.exist_net_stack_instance_config['vmotion'].congestionControlAlgorithm,
                    max_num_connections=self.exist_net_stack_instance_config['vmotion'].requestedMaxNumberOfConnections
                )
            if self.vmotion:
                if self.diff_config['before']['vmotion']['gateway'] != self.vmotion['gateway']:
                    self.change_flag = True
                    self.diff_config['after']['vmotion']['gateway'] = self.vmotion['gateway']
                if self.diff_config['before']['vmotion']['ipv6_gateway'] != self.vmotion['ipv6_gateway']:
                    self.change_flag = True
                    self.diff_config['after']['vmotion']['ipv6_gateway'] = self.vmotion['ipv6_gateway']
                if self.diff_config['before']['vmotion']['max_num_connections'] != self.vmotion['max_num_connections']:
                    self.change_flag = True
                    self.diff_config['after']['vmotion']['max_num_connections'] = self.vmotion['max_num_connections']
                if self.diff_config['before']['vmotion']['congestion_algorithm'] != self.vmotion['congestion_algorithm']:
                    self.change_flag = True
                    self.diff_config['after']['vmotion']['congestion_algorithm'] = self.vmotion['congestion_algorithm']

        if self.enabled_net_stack_instance['vxlan']:
            for key in 'before', 'after':
                self.diff_config[key]['vxlan'] = dict(
                    gateway=self.exist_net_stack_instance_config['vxlan'].ipRouteConfig.defaultGateway,
                    ipv6_gateway=self.exist_net_stack_instance_config['vxlan'].ipRouteConfig.ipV6DefaultGateway,
                    congestion_algorithm=self.exist_net_stack_instance_config['vxlan'].congestionControlAlgorithm,
                    max_num_connections=self.exist_net_stack_instance_config['vxlan'].requestedMaxNumberOfConnections
                )
            if self.vxlan:
                if self.diff_config['before']['vxlan']['gateway'] != self.vxlan['gateway']:
                    self.change_flag = True
                    self.diff_config['after']['vxlan']['gateway'] = self.vxlan['gateway']
                if self.diff_config['before']['vxlan']['ipv6_gateway'] != self.vxlan['ipv6_gateway']:
                    self.change_flag = True
                    self.diff_config['after']['vxlan']['ipv6_gateway'] = self.vxlan['ipv6_gateway']
                if self.diff_config['before']['vxlan']['max_num_connections'] != self.vxlan['max_num_connections']:
                    self.change_flag = True
                    self.diff_config['after']['vxlan']['max_num_connections'] = self.vxlan['max_num_connections']
                if self.diff_config['before']['vxlan']['congestion_algorithm'] != self.vxlan['congestion_algorithm']:
                    self.change_flag = True
                    self.diff_config['after']['vxlan']['congestion_algorithm'] = self.vxlan['congestion_algorithm']

    def generate_net_stack_instance_config(self):
        """
        Generate a new configuration for tcpip stack to modify the configuration.
        """
        self.new_net_stack_instance_configs = vim.host.NetworkConfig()
        self.new_net_stack_instance_configs.netStackSpec = []

        if self.default and self.enabled_net_stack_instance['default']:
            default_config = vim.host.NetworkConfig.NetStackSpec()
            default_config.operation = 'edit'
            default_config.netStackInstance = vim.host.NetStackInstance()
            default_config.netStackInstance.key = self.net_stack_instance_keys['default']
            default_config.netStackInstance.ipRouteConfig = vim.host.IpRouteConfig()
            default_config.netStackInstance.ipRouteConfig.defaultGateway = self.default['gateway']
            default_config.netStackInstance.ipRouteConfig.ipV6DefaultGateway = self.default['ipv6_gateway']
            default_config.netStackInstance.dnsConfig = vim.host.DnsConfig()
            default_config.netStackInstance.dnsConfig.hostName = self.default['hostname']
            default_config.netStackInstance.dnsConfig.domainName = self.default['domain']
            dns_servers = []
            if self.default['preferred_dns']:
                dns_servers.append(self.default['preferred_dns'])
            if self.default['alternate_dns']:
                dns_servers.append(self.default['alternate_dns'])
            default_config.netStackInstance.dnsConfig.address = dns_servers
            default_config.netStackInstance.dnsConfig.searchDomain = self.default['search_domains']
            default_config.netStackInstance.congestionControlAlgorithm = self.default['congestion_algorithm']
            default_config.netStackInstance.requestedMaxNumberOfConnections = self.default['max_num_connections']
            self.new_net_stack_instance_configs.netStackSpec.append(default_config)

        if self.provisioning and self.enabled_net_stack_instance['provisioning']:
            provisioning_config = vim.host.NetworkConfig.NetStackSpec()
            provisioning_config.operation = 'edit'
            provisioning_config.netStackInstance = vim.host.NetStackInstance()
            provisioning_config.netStackInstance.key = self.net_stack_instance_keys['provisioning']
            provisioning_config.netStackInstance.ipRouteConfig = vim.host.IpRouteConfig()
            provisioning_config.netStackInstance.ipRouteConfig.defaultGateway = self.provisioning['gateway']
            provisioning_config.netStackInstance.ipRouteConfig.ipV6DefaultGateway = self.provisioning['ipv6_gateway']
            provisioning_config.netStackInstance.congestionControlAlgorithm = self.provisioning['congestion_algorithm']
            provisioning_config.netStackInstance.requestedMaxNumberOfConnections = self.provisioning['max_num_connections']
            self.new_net_stack_instance_configs.netStackSpec.append(provisioning_config)

        if self.vmotion and self.enabled_net_stack_instance['vmotion']:
            vmotion_config = vim.host.NetworkConfig.NetStackSpec()
            vmotion_config.operation = 'edit'
            vmotion_config.netStackInstance = vim.host.NetStackInstance()
            vmotion_config.netStackInstance.key = self.net_stack_instance_keys['vmotion']
            vmotion_config.netStackInstance.ipRouteConfig = vim.host.IpRouteConfig()
            vmotion_config.netStackInstance.ipRouteConfig.defaultGateway = self.vmotion['gateway']
            vmotion_config.netStackInstance.ipRouteConfig.ipV6DefaultGateway = self.vmotion['ipv6_gateway']
            vmotion_config.netStackInstance.congestionControlAlgorithm = self.vmotion['congestion_algorithm']
            vmotion_config.netStackInstance.requestedMaxNumberOfConnections = self.vmotion['max_num_connections']
            self.new_net_stack_instance_configs.netStackSpec.append(vmotion_config)

        if self.vxlan and self.enabled_net_stack_instance['vxlan']:
            vxlan_config = vim.host.NetworkConfig.NetStackSpec()
            vxlan_config.operation = 'edit'
            vxlan_config.netStackInstance = vim.host.NetStackInstance()
            vxlan_config.netStackInstance.key = self.net_stack_instance_keys['vxlan']
            vxlan_config.netStackInstance.ipRouteConfig = vim.host.IpRouteConfig()
            vxlan_config.netStackInstance.ipRouteConfig.defaultGateway = self.vxlan['gateway']
            vxlan_config.netStackInstance.ipRouteConfig.ipV6DefaultGateway = self.vxlan['ipv6_gateway']
            vxlan_config.netStackInstance.congestionControlAlgorithm = self.vxlan['congestion_algorithm']
            vxlan_config.netStackInstance.requestedMaxNumberOfConnections = self.vxlan['max_num_connections']
            self.new_net_stack_instance_configs.netStackSpec.append(vxlan_config)

    def execute(self):
        # The host name is unique in vCenter, so find the host from the whole.
        self.host_obj = self.find_hostsystem_by_name(self.esxi_hostname)
        if self.host_obj is None:
            self.module.fail_json(msg="Cannot find the specified ESXi host: %s" % self.params['esxi_hostname'])

        self.check_enabled_net_stack_instance()
        self.get_net_stack_instance_config()
        self.diff_net_stack_instance_config()
        if self.change_flag:
            if self.module.check_mode is False:
                self.generate_net_stack_instance_config()
                try:
                    self.host_obj.configManager.networkSystem.UpdateNetworkConfig(self.new_net_stack_instance_configs, 'modify')
                except vim.fault.PlatformConfigFault as e:
                    self.module.fail_json(msg="cannot modify tcpip stack config: %s" % to_text(e.faultMessage[0].message))
                except Exception as e:
                    self.module.fail_json(msg="cannot modify tcpip stack config: %s" % to_text(e.msg))

        # Make a warning for the item if it isn't supported by ESXi when specified item.
        for key, value in self.enabled_net_stack_instance.items():
            if self.params[key] and value is False:
                self.module.warn("%s isn't supported in %s" % (key, self.params['esxi_hostname']))

        # Make the return value for the result.
        result = dict(
            changed=self.change_flag,
            diff=dict(
                before=OrderedDict(sorted(self.diff_config['before'].items())),
                after=OrderedDict(sorted(self.diff_config['after'].items()))
            )
        )
        for key, value in self.enabled_net_stack_instance.items():
            if value:
                result[key] = self.diff_config['after'][key]
            else:
                result[key] = {}
        self.module.exit_json(**result)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=True),
        default=dict(type='dict',
                     options=dict(
                         hostname=dict(type='str', required=True),
                         domain=dict(type='str', required=True),
                         preferred_dns=dict(type='str'),
                         alternate_dns=dict(type='str'),
                         search_domains=dict(type='list', elements='str', default=[]),
                         gateway=dict(type='str'),
                         ipv6_gateway=dict(type='str'),
                         congestion_algorithm=dict(type='str', choices=['newreno', 'cubic'], default='newreno'),
                         max_num_connections=dict(type='int', default=11000)

                     )),
        provisioning=dict(type='dict',
                          options=dict(
                              gateway=dict(type='str'),
                              ipv6_gateway=dict(type='str'),
                              congestion_algorithm=dict(type='str', choices=['newreno', 'cubic'], default='newreno'),
                              max_num_connections=dict(type='int', default=11000)
                          )),
        vmotion=dict(type='dict',
                     options=dict(
                         gateway=dict(type='str'),
                         ipv6_gateway=dict(type='str'),
                         congestion_algorithm=dict(type='str', choices=['newreno', 'cubic'], default='newreno'),
                         max_num_connections=dict(type='int', default=11000)
                     )),
        vxlan=dict(type='dict',
                   aliases=['nsx_overlay'],
                   options=dict(
                       gateway=dict(type='str'),
                       ipv6_gateway=dict(type='str'),
                       congestion_algorithm=dict(type='str', choices=['newreno', 'cubic'], default='newreno'),
                       max_num_connections=dict(type='int', default=11000)
                   ))
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_host_tcpip_stack = VmwareHostTcpipStack(module)
    vmware_host_tcpip_stack.execute()


if __name__ == "__main__":
    main()
