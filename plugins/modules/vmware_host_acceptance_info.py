#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# Copyright: (c) 2023, Mario Lenz <m@riolenz.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_acceptance_info
short_description: Gather host acceptance level of ESXi hosts
description:
- This module can be used to gather the host acceptance level of ESXi hosts.
- The host acceptance level controls the acceptance level of each VIB on a ESXi host.
author:
- Abhijeet Kasurde (@Akasurde)
- Mario Lenz (@mariolenz)
options:
  cluster_name:
    description:
    - Name of the cluster.
    - Acceptance level of all ESXi host system in the given cluster will be gathered.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname.
    - Acceptance level of this ESXi host system will be gathered.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
extends_documentation_fragment:
- vmware.vmware.base_options

'''

EXAMPLES = r'''
- name: Get acceptance level from the given ESXi Host
  community.vmware.vmware_host_acceptance_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_acceptance_level
'''

RETURN = r'''
host_acceptance_info:
    description:
    - dict with hostname as key and dict with acceptance level facts, error as value
    returned: facts
    type: dict
    sample: { "facts": { "localhost.localdomain": { "error": "NA", "level": "vmware_certified" }}}
'''

try:
    from pyVmomi import vim
except ImportError:
    pass
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.common.text.converters import to_native


class VMwareAccpetanceManager(PyVmomi):
    def __init__(self, module):
        super(VMwareAccpetanceManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        self.hosts_facts = {}

    def gather_acceptance_info(self):
        for host in self.hosts:
            self.hosts_facts[host.name] = dict(level='', error='NA')
            host_image_config_mgr = host.configManager.imageConfigManager
            if host_image_config_mgr:
                try:
                    self.hosts_facts[host.name]['level'] = host_image_config_mgr.HostImageConfigGetAcceptance()
                except vim.fault.HostConfigFault as e:
                    self.hosts_facts[host.name]['error'] = to_native(e.msg)
        self.module.exit_json(changed=False, host_acceptance_info=self.hosts_facts)


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

    vmware_host_accept_config = VMwareAccpetanceManager(module)
    vmware_host_accept_config.gather_acceptance_info()


if __name__ == "__main__":
    main()
