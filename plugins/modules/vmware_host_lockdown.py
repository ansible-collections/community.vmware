#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_lockdown
short_description: Manage administrator permission for the local administrative account for the ESXi host
description:
- This module can be used to manage administrator permission for the local administrative account for the host when ESXi hostname is given.
- This module is destructive as administrator permission are managed using APIs used, please read options carefully and proceed.
- Please specify O(hostname) as vCenter IP or hostname only, as lockdown operations are not possible from standalone ESXi server.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  cluster_name:
    description:
    - Name of cluster.
    - All host systems from given cluster used to manage lockdown.
    - Required parameter, if O(esxi_hostname) is not set.
    type: str
  esxi_hostname:
    description:
    - List of ESXi hostname to manage lockdown.
    - Required parameter, if O(cluster_name) is not set.
    - See examples for specifications.
    type: list
    elements: str
  state:
    description:
    - State of hosts system
    - If set to V(disabled), all host systems will be removed from lockdown mode.
    - If host system is already out of lockdown mode and set to V(disabled), no action will be taken.
    - If set to V(normal), all host systems will be set in lockdown mode.
    - If host system is already in lockdown mode and set to V(normal), no action will be taken.
    - If set to V(strict), all host systems will be set in strict lockdown mode.
    - If host system is already in strict lockdown mode and set to V(strict), no action will be taken.
    default: normal
    choices: [ disabled, normal, strict ]
    type: str
extends_documentation_fragment:
- vmware.vmware.base_options

'''

EXAMPLES = r'''
- name: Enter host system into lockdown mode
  community.vmware.vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: normal
  delegate_to: localhost

- name: Exit host systems from lockdown mode
  community.vmware.vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: disabled
  delegate_to: localhost

- name: Enter host systems into lockdown mode
  community.vmware.vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname:
        - '{{ esxi_hostname_1 }}'
        - '{{ esxi_hostname_2 }}'
    state: normal
  delegate_to: localhost

- name: Exit host systems from lockdown mode
  community.vmware.vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname:
        - '{{ esxi_hostname_1 }}'
        - '{{ esxi_hostname_2 }}'
    state: disabled
  delegate_to: localhost

- name: Enter all host system from cluster into lockdown mode
  community.vmware.vmware_host_lockdown:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    state: normal
  delegate_to: localhost
'''

RETURN = r'''
results:
    description: metadata about state of Host system lock down
    returned: always
    type: dict
    sample: {
                "host_lockdown_state": {
                    "DC0_C0": {
                        "current_state": "normal",
                        "previous_state": "disabled",
                        "desired_state": "normal",
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
        results = dict(changed=False, host_lockdown_state=dict())
        change_list = []
        desired_state = self.params.get('state')

        for host in self.hosts:
            current_state_api = host.configManager.hostAccessManager.lockdownMode
            current_state = current_state_api[8:].lower()
            results['host_lockdown_state'][host.name] = dict(current_state=desired_state,
                                                             desired_state=desired_state,
                                                             previous_state=current_state
                                                             )
            changed = False
            if current_state != desired_state:
                changed = True
                if not self.module.check_mode:
                    try:
                        desired_state_api = 'lockdown' + desired_state.capitalize()
                        host.configManager.hostAccessManager.ChangeLockdownMode(desired_state_api)
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
        state=dict(type='str', default='normal', choices=['disabled', 'normal', 'strict'], required=False),
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
