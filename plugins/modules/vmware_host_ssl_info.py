#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_ssl_info
short_description: Gather info of ESXi host system about SSL
description:
- This module can be used to gather information of the SSL thumbprint information for a host.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  cluster_name:
    description:
    - Name of the cluster.
    - SSL thumbprint information about all ESXi host system in the given cluster will be reported.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname.
    - SSL thumbprint information of this ESXi host system will be reported.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather SSL thumbprint information about all ESXi Hosts in given Cluster
  community.vmware.vmware_host_ssl_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: all_host_ssl_info

- name: Get SSL Thumbprint info about "{{ esxi_hostname }}"
  community.vmware.vmware_host_ssl_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: '{{ esxi_hostname }}'
  register: ssl_info
- set_fact:
    ssl_thumbprint: "{{ ssl_info['host_ssl_info'][esxi_hostname]['ssl_thumbprints'][0] }}"
- debug:
    msg: "{{ ssl_thumbprint }}"
- name: Add ESXi Host to vCenter
  vmware_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    cluster_name: '{{ cluster_name }}'
    esxi_hostname: '{{ esxi_hostname }}'
    esxi_username: '{{ esxi_username }}'
    esxi_password: '{{ esxi_password }}'
    esxi_ssl_thumbprint: '{{ ssl_thumbprint }}'
    state: present
'''

RETURN = r'''
host_ssl_info:
    description:
    - dict with hostname as key and dict with SSL thumbprint related info
    returned: info
    type: dict
    sample:
        {
            "10.76.33.215": {
                "owner_tag": "",
                "principal": "vpxuser",
                "ssl_thumbprints": [
                    "E3:E8:A9:20:8D:32:AE:59:C6:8D:A5:91:B0:20:EF:00:A2:7C:27:EE",
                    "F1:AC:DA:6E:D8:1E:37:36:4A:5C:07:E5:04:0B:87:C8:75:FB:42:01"
                ]
            }
        }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VMwareHostSslManager(PyVmomi):
    def __init__(self, module):
        super(VMwareHostSslManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        self.hosts_info = {}

    def gather_ssl_info(self):
        for host in self.hosts:
            self.hosts_info[host.name] = dict(
                principal='',
                owner_tag='',
                ssl_thumbprints=[])

            host_ssl_info_mgr = host.config.sslThumbprintInfo
            if host_ssl_info_mgr:
                self.hosts_info[host.name]['principal'] = host_ssl_info_mgr.principal
                self.hosts_info[host.name]['owner_tag'] = host_ssl_info_mgr.ownerTag
                self.hosts_info[host.name]['ssl_thumbprints'] = list(host_ssl_info_mgr.sslThumbprints)

        self.module.exit_json(changed=False, host_ssl_info=self.hosts_info)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str'),
        esxi_hostname=dict(type='str'),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True,
    )

    vmware_host_accept_config = VMwareHostSslManager(module)
    vmware_host_accept_config.gather_ssl_info()


if __name__ == "__main__":
    main()
