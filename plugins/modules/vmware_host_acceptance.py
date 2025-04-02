#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_acceptance
short_description: Manage the host acceptance level of an ESXi host
description:
- This module can be used to manage the host acceptance level of an ESXi host.
- The host acceptance level controls the acceptance level of each VIB on a ESXi host.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  cluster_name:
    description:
    - Name of the cluster.
    - Acceptance level of all ESXi host system in the given cluster will be managed.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname.
    - Acceptance level of this ESXi host system will be managed.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
  state:
    description:
    - If set to V(partner), then accept only partner and VMware signed and certified VIBs.
    - If set to V(vmware_certified), then accept only VIBs that are signed and certified by VMware.
    - If set to V(vmware_accepted), then accept VIBs that have been accepted by VMware.
    - If set to V(community), then accept all VIBs, even those that are not signed.
    choices: [ community, partner, vmware_accepted, vmware_certified ]
    required: true
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Set acceptance level to community for all ESXi Host in given Cluster
  community.vmware.vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
    state: 'community'
  delegate_to: localhost
  register: cluster_acceptance_level

- name: Set acceptance level to vmware_accepted for the given ESXi Host
  community.vmware.vmware_host_acceptance:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: 'vmware_accepted'
  delegate_to: localhost
  register: host_acceptance_level
'''

RETURN = r'''
facts:
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
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VMwareAccpetanceManager(PyVmomi):
    def __init__(self, module):
        super(VMwareAccpetanceManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        self.desired_state = self.params.get('state')
        self.hosts_facts = {}

    def set_acceptance_level(self):
        change = []
        for host in self.hosts:
            self.hosts_facts[host.name] = dict(level='', error='NA')
            host_image_config_mgr = host.configManager.imageConfigManager
            if host_image_config_mgr:
                try:
                    self.hosts_facts[host.name]['level'] = host_image_config_mgr.HostImageConfigGetAcceptance()
                except vim.fault.HostConfigFault as e:
                    self.hosts_facts[host.name]['error'] = to_native(e.msg)
            host_changed = False
            if self.hosts_facts[host.name]['level'] != self.desired_state:
                try:
                    if self.module.check_mode:
                        self.hosts_facts[host.name]['level'] = self.desired_state
                    else:
                        host_image_config_mgr.UpdateHostImageAcceptanceLevel(newAcceptanceLevel=self.desired_state)
                        self.hosts_facts[host.name]['level'] = host_image_config_mgr.HostImageConfigGetAcceptance()
                    host_changed = True
                except vim.fault.HostConfigFault as e:
                    self.hosts_facts[host.name]['error'] = to_native(e.msg)

            change.append(host_changed)
        self.module.exit_json(changed=any(change), facts=self.hosts_facts)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str', required=False),
        esxi_hostname=dict(type='str', required=False),
        state=dict(type='str',
                   choices=['community', 'partner', 'vmware_accepted', 'vmware_certified'],
                   required=True
                   ),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True
    )

    vmware_host_accept_config = VMwareAccpetanceManager(module)
    vmware_host_accept_config.set_acceptance_level()


if __name__ == "__main__":
    main()
