#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Wei Gao <gaowei3@qq.com>
# Copyright: (c) 2018, Ansible Project
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: vmware_host_connection_info
short_description: Gathers connection state about remote ESXi hostsystem
description: This module can be used to check on the connection state of a ESXi host in vcenter
version_added: 2.10
author:
    - Christian Neugum (@digifuchsi)
    - Valentin Yonev (@valentinJonev)
requirements:
    - python >= 2.6
    - PyVmomi
options:
  esxi_hostname:
    description:
    - ESXi hostname.
    type: str
extends_documentation_fragment: vmware.documentation
'''

EXAMPLES = r'''
- name: Gather vmware host facts from vCenter
  vmware_host_connection_info:
    hostname: "{{ vcenter_server }}"
    username: "{{ vcenter_user }}"
    password: "{{ vcenter_pass }}"
    esxi_hostname: "{{ esxi_hostname }}"
  register: host_facts
  delegate_to: localhost
'''

RETURN = r'''
ansible_facts:
  description: system info about the host machine
  returned: always
  type: dict
  sample:
    {
        "connectionState": "connected"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec


class VMwareHostFactManager(PyVmomi):
    def __init__(self, module):
        super(VMwareHostFactManager, self).__init__(module)
        self.esxi_host_name = self.params.get('esxi_hostname', None)

    def get_connection_info(self):
        if self.is_vcenter():
            if self.esxi_host_name is None:
                self.module.fail_json(msg="Connected to a vCenter system without specifying esxi_hostname")
            self.host = self.get_all_host_objs(esxi_host_name=self.esxi_host_name)
            if len(self.host) > 1:
                self.module.fail_json(msg="esxi_hostname matched multiple hosts")
            self.host = self.host[0]
        else:
            self.module.fail_json(msg="Not connected to a vCenter system")

        if self.host is None:
            self.module.fail_json(msg="Failed to find host system.")

        self.module.exit_json(changed=False, connectionState=self.host.runtime.connectionState)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=False),
    )
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    vm_host_manager = VMwareHostFactManager(module)
    vm_host_manager.get_connection_info()


if __name__ == '__main__':
    main()
