#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Mario Lenz <m@riolenz.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_lockdown_exceptions
version_added: '3.1.0'
short_description: Manage Lockdown Mode Exception Users
description:
- This module can be used to manage Lockdown Mode Exception Users.
- Please specify O(hostname) as vCenter IP or hostname only, as lockdown operations are not possible from standalone ESXi server.
author:
- Mario Lenz (@mariolenz)
options:
  cluster_name:
    description:
    - Name of cluster.
    - All host systems from given cluster used to manage exception users.
    - Required parameter, if O(esxi_hostname) is not set.
    type: str
  esxi_hostname:
    description:
    - List of ESXi hostname to manage exception users.
    - Required parameter, if O(cluster_name) is not set.
    type: list
    elements: str
  state:
    description:
    - If V(present), make sure the given users are defined as Lockdown Mode Exception Users.
    - If V(absent), make sure the given users are NO Lockdown Mode Exception Users.
    - If V(set), will replace Lockdown Mode Exception Users defined list of users.
    default: present
    choices: [ present, absent , set ]
    type: str
  exception_users:
    description:
    - List of Lockdown Mode Exception Users.
    - To remove all Exception Users, O(state=set) the empty list.
    type: list
    elements: str
    required: true
extends_documentation_fragment:
- vmware.vmware.base_options

'''

EXAMPLES = r'''
- name: Remove all Lockdown Mode Exception Users on a host
  community.vmware.vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    exception_users: []
    state: set
  delegate_to: localhost
'''

RETURN = r'''
results:
    description: metadata about exception users of Host systems
    returned: always
    type: dict
    sample: {
                "host_lockdown_exceptions": {
                    "DC0_C0": {
                        "current_exception_users": [],
                        "desired_exception_users": [],
                        "previous_exception_users": [
                            "root"
                        ]
                    },
                }
            }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.common.text.converters import to_native


class VmwareLockdownManager(PyVmomi):
    def __init__(self, module):
        super(VmwareLockdownManager, self).__init__(module)
        if not self.is_vcenter():
            self.module.fail_json(msg="Lockdown operations are performed from vCenter only. "
                                      "hostname %s is an ESXi server. Please specify hostname "
                                      "as vCenter server." % self.module.params['hostname'])
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)

    def ensure(self):
        """
        Function to manage internal state management
        """
        results = dict(changed=False, host_lockdown_exceptions=dict())
        change_list = []
        desired_state = self.params.get('state')
        exception_users = self.params.get('exception_users')
        for host in self.hosts:
            current_exception_users = host.configManager.hostAccessManager.QueryLockdownExceptions()
            current_exception_users.sort()
            new_exception_users = current_exception_users.copy()
            results['host_lockdown_exceptions'][host.name] = dict(previous_exception_users=current_exception_users)
            changed = False

            if desired_state == 'present':
                for user in exception_users:
                    if user not in current_exception_users:
                        new_exception_users.append(user)
                        changed = True
            elif desired_state == 'absent':
                for user in exception_users:
                    if user in current_exception_users:
                        new_exception_users.remove(user)
                        changed = True
            elif desired_state == 'set':
                if set(current_exception_users) != set(exception_users):
                    new_exception_users = exception_users
                    changed = True

            new_exception_users.sort()
            results['host_lockdown_exceptions'][host.name]['desired_exception_users'] = new_exception_users
            results['host_lockdown_exceptions'][host.name]['current_exception_users'] = new_exception_users

            if changed and not self.module.check_mode:
                try:
                    host.configManager.hostAccessManager.UpdateLockdownExceptions(new_exception_users)

                except vim.fault.HostConfigFault as host_config_fault:
                    self.module.fail_json(msg="Failed to manage lockdown mode for esxi"
                                              " hostname %s : %s" % (host.name, to_native(host_config_fault.msg)))
                except vim.fault.AdminDisabled as admin_disabled:
                    self.module.fail_json(msg="Failed to manage lockdown mode as administrator "
                                              "permission has been disabled for "
                                              "esxi hostname %s : %s" % (host.name, to_native(admin_disabled.msg)))
                except Exception as generic_exception:
                    self.module.fail_json(msg="Failed to manage lockdown mode due to generic exception for esxi "
                                              "hostname %s : %s" % (host.name, to_native(generic_exception)))
            change_list.append(changed)

        if any(change_list):
            results['changed'] = True

        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str', required=False),
        esxi_hostname=dict(type='list', required=False, elements='str'),
        exception_users=dict(type='list', required=True, elements='str'),
        state=dict(type='str', default='present', choices=['present', 'absent', 'set'], required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ]
    )

    vmware_lockdown_mgr = VmwareLockdownManager(module)
    vmware_lockdown_mgr.ensure()


if __name__ == "__main__":
    main()
