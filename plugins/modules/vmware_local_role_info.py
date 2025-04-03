#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_local_role_info
short_description: Gather info about local roles on an ESXi host or vCenter
description:
    - This module can be used to gather information about local role info on an ESXi host or vCenter
author:
- Abhijeet Kasurde (@Akasurde)
notes:
    - Be sure that the user used for login, has the appropriate rights to view roles
    - The module returns a list of dict in version 2.8 and above.
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather info about local role from an ESXi (or vCenter)
  community.vmware.vmware_local_role_info:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
  register: fact_details
  delegate_to: localhost
- name: Get Admin privileges
  set_fact:
    admin_priv: "{{ fact_details.local_role_info | selectattr('role_name', 'equalto', 'Admin') | map(attribute='privileges') | first  }}"
- debug:
    msg: "{{ admin_priv }}"
'''

RETURN = r'''
local_role_info:
    description: A list of dict about role information present on ESXi host
    returned: always
    type: list
    sample: [
        {
            "privileges": [
                "Alarm.Acknowledge",
                "Alarm.Create",
                "Alarm.Delete",
                "Alarm.DisableActions",
            ],
            "role_id": -12,
            "role_info_label": "Ansible User",
            "role_info_summary": "Ansible Automation user",
            "role_name": "AnsiUser1",
            "role_system": true
        },
        {
            "privileges": [],
            "role_id": -5,
            "role_info_label": "No access",
            "role_info_summary": "Used for restricting granted access",
            "role_name": "NoAccess",
            "role_system": true
        },
        {
            "privileges": [
                "System.Anonymous",
                "System.View"
            ],
            "role_id": -3,
            "role_info_label": "View",
            "role_info_summary": "Visibility access (cannot be granted)",
            "role_name": "View",
            "role_system": true
        }
    ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VMwareLocalRoleInfo(PyVmomi):
    """Class to manage local role info"""

    def __init__(self, module):
        super(VMwareLocalRoleInfo, self).__init__(module)
        self.module = module
        self.params = module.params

        if self.content.authorizationManager is None:
            self.module.fail_json(
                msg="Failed to get local authorization manager settings.",
                details="It seems that '%s' does not support this functionality" % self.params['hostname']
            )

    def gather_local_role_info(self):
        """Gather info about local roles"""
        results = list()
        for role in self.content.authorizationManager.roleList:
            results.append(
                dict(
                    role_name=role.name,
                    role_id=role.roleId,
                    privileges=list(role.privilege),
                    role_system=role.system,
                    role_info_label=role.info.label,
                    role_info_summary=role.info.summary,
                )
            )

        self.module.exit_json(changed=False, local_role_info=results)


def main():
    """Main"""
    argument_spec = base_argument_spec()
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    vmware_local_role_info = VMwareLocalRoleInfo(module)
    vmware_local_role_info.gather_local_role_info()


if __name__ == '__main__':
    main()
