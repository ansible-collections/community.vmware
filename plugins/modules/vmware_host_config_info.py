#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_config_info
short_description: Gathers info about an ESXi host's advance configuration information
description:
- This module can be used to gather information about an ESXi host's advance configuration information when ESXi hostname or Cluster name is given.
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
- name: Gather info about all ESXi Host in given Cluster
  community.vmware.vmware_host_config_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
  delegate_to: localhost

- name: Gather info about ESXi Host
  community.vmware.vmware_host_config_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
'''

RETURN = r'''
hosts_info:
    description:
    - dict with hostname as key and dict with host config information
    returned: always
    type: dict
    sample: {
        "10.76.33.226": {
            "Annotations.WelcomeMessage": "",
            "BufferCache.FlushInterval": 30000,
            "BufferCache.HardMaxDirty": 95,
            "BufferCache.PerFileHardMaxDirty": 50,
            "BufferCache.SoftMaxDirty": 15,
        }
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VmwareConfigInfoManager(PyVmomi):
    def __init__(self, module):
        super(VmwareConfigInfoManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)

    def gather_host_info(self):
        hosts_info = {}
        for host in self.hosts:
            host_info = {}
            for option in host.configManager.advancedOption.QueryOptions():
                host_info[option.key] = option.value
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

    vmware_host_config = VmwareConfigInfoManager(module)
    module.exit_json(changed=False, hosts_info=vmware_host_config.gather_host_info())


if __name__ == "__main__":
    main()
