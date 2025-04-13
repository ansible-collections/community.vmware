#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: vmware_host_user_manager
short_description: Manage users of ESXi
author:
  - sky-joker (@sky-joker)
description:
  - This module can add, update or delete local users on ESXi host.
options:
  esxi_hostname:
    description:
      - Name of the ESXi host that is managing the local user.
    type: str
    required: true
  user_name:
    description:
      - Name of the local user.
    aliases:
      - local_user_name
    type: str
    required: true
  user_password:
    description:
      - The local user password.
      - If you'd like to update the password, requires O(override_user_password=true).
    aliases:
      - local_user_password
    type: str
  user_description:
    description:
      - The local user description.
    aliases:
      - local_user_description
    type: str
  override_user_password:
    description:
      - If the local user exists and updates the password, change this parameter value is true.
    default: false
    type: bool
  state:
    description:
      - If set to V(present), add a new local user or update information.
      - If set to V(absent), delete the local user.
    default: present
    type: str
    choices:
      - present
      - absent
extends_documentation_fragment:
  - community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Add new local user to ESXi host
  community.vmware.vmware_host_user_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    user_name: example
    user_description: "example user"
    user_password: "{{ local_user_password }}"
    state: present

- name: Update the local user password in ESXi host
  community.vmware.vmware_host_user_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    user_name: example
    user_description: "example user"
    user_password: "{{ local_user_password }}"
    override_user_password: true
    state: present

- name: Delete the local user in ESXi host
  community.vmware.vmware_host_user_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    user_name: example
    state: absent
'''

RETURN = r'''
msg:
  description: The executed result for the module.
  returned: always
  type: str
  sample: >-
    {
        "msg": "Added the new user.
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VmwareHostUserManager(PyVmomi):
    def __init__(self, module):
        super(VmwareHostUserManager, self).__init__(module)
        self.esxi_hostname = module.params["esxi_hostname"]
        self.user_name = module.params["user_name"]
        self.user_password = module.params["user_password"]
        self.user_description = module.params["user_description"]
        self.override_user_password = module.params["override_user_password"]
        self.state = module.params["state"]

    def search_user(self):
        """
        Search the specified user from ESXi

        Returns: searched user
        """
        searchStr = self.user_name
        exactMatch = True
        findUsers = True
        findGroups = False
        user_account = self.host_obj.configManager.userDirectory.RetrieveUserGroups(None, searchStr, None, None, exactMatch, findUsers, findGroups)
        return user_account

    def ensure_user_info_diff(self, user_account):
        """
        Ensure a user information difference.
        The method can check a user description difference only.
        Also, it can't get the set password via vSphere API.

        Returns: bool
        """
        if user_account.fullName != self.user_description and self.user_description is not None:
            return True

        return False

    def add_user(self):
        """
        Add a new user
        """
        user_spec = vim.host.LocalAccountManager.AccountSpecification(
            id=self.user_name,
            description=self.user_description,
            password=self.user_password
        )
        try:
            self.host_obj.configManager.accountManager.CreateUser(user_spec)
        except Exception as e:
            self.module.fail_json(msg="Failed to add a new user: %s" % to_text(e.msg))

    def update_user(self):
        """
        Update a user information
        """
        user_spec = vim.host.LocalAccountManager.AccountSpecification(
            id=self.user_name,
            description=self.user_description
        )

        if self.user_password and self.override_user_password:
            user_spec.password = self.user_password

        try:
            self.host_obj.configManager.accountManager.UpdateUser(user_spec)
        except Exception as e:
            self.module.fail_json(msg="Failed to update a new password: %s" % to_text(e))

    def remove_user(self):
        """
        Remove a user
        """
        try:
            self.host_obj.configManager.accountManager.RemoveUser(self.user_name)
        except Exception as e:
            self.module.fail_json(msg="Failed to remove a user: %s" % to_text(e.msg))

    def execute(self):
        # The host name is unique in vCenter, so find the host from the whole.
        self.host_obj = self.find_hostsystem_by_name(self.esxi_hostname)
        if self.host_obj is None:
            self.module.fail_json(msg="Cannot find the specified ESXi host: %s" % self.params['esxi_hostname'])

        # Search the specified user
        user_account = self.search_user()

        changed = False
        msg = "The change will not occur for the user information."
        if self.state == "present":
            if user_account:
                user_diff = self.ensure_user_info_diff(user_account[0])
                # If you want to update a user password, require the override_user_passwd is true.
                if user_diff or self.override_user_password:
                    changed = True
                    if self.module.check_mode:
                        msg = "The user information will be updated."
                    else:
                        msg = "Updated the user information."
                        self.update_user()
            else:
                changed = True
                if self.module.check_mode:
                    msg = "The new user will be added."
                else:
                    msg = "Added the new user."
                    self.add_user()

        if self.state == "absent":
            if user_account:
                changed = True
                if self.module.check_mode:
                    msg = "The user will be removed."
                else:
                    msg = "Removed the user."
                    self.remove_user()

        self.module.exit_json(changed=changed, msg=msg)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type="str", required=True),
        user_name=dict(type="str", required=True, aliases=["local_user_name"]),
        user_password=dict(type="str", aliases=["local_user_password"], no_log=True),
        user_description=dict(type="str", aliases=["local_user_description"]),
        override_user_password=dict(type="bool", default=False, no_log=False),
        state=dict(type="str", default="present", choices=["present", "absent"])
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ('override_user_password', True, ['user_password']),
        ]
    )
    vmware_host_user_manager = VmwareHostUserManager(module)
    vmware_host_user_manager.execute()


if __name__ == "__main__":
    main()
