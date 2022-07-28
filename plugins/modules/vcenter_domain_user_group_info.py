#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: vcenter_domain_user_group_info
short_description: Gather user or group information of a domain
author:
  - sky-joker (@sky-joker)
description:
  - This module can be used to gather information about user or group of a domain.
options:
  domain:
    description:
      - The I(domain) to be specified searching.
    type: str
    default: vsphere.local
  search_string:
    description:
      - The I(search_string) is a string to be specified searching.
      - Specify the domain user or group name to be searched.
    type: str
    required: True
  belongs_to_group:
    description:
      -  If a group existing, returned contains only users or groups that directly belong to the specified group.
    type: str
  belongs_to_user:
    description:
      - If a user existing, returned contains only groups that directly contain the specified user.
    type: str
  exact_match:
    description:
      - If I(exact_match) is C(True), it indicates the I(search_string) passed should match a user or group name exactly.
    type: bool
    default: False
  find_users:
    description:
      - If I(find_users) is C(True), domain users will be included in the result.
    type: bool
    default: True
  find_groups:
    description:
      - If I(find_groups) is C(True), domain groups will be included in the result.
    type: bool
    default: True
version_added: '1.6.0'
extends_documentation_fragment:
  - community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Gather all domain user and group of vsphere.local
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: ''
  register: gather_all_domain_user_group_result

- name: Gather all domain user and group included the administrator string
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: administrator
  register: gather_domain_user_group_result

- name: Gather all domain user of vsphere.local
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: ''
    find_users: true
    find_groups: false
  register: gather_all_domain_user_result

- name: Gather administrator user by exact match condition
  community.vmware.vcenter_domain_user_group_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    domain: vsphere.local
    search_string: "vsphere.local\\administrator"
    exact_match: true
  register: gather_administrator_user_exact_match_result
'''

RETURN = r'''
domain_user_groups:
  description: list of domain user and group information
  returned: success
  type: list
  sample: >-
    [
        {
            "fullName": "Administrator vsphere.local",
            "group": false,
            "principal": "Administrator"
        }
    ]
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec


class VcenterDomainUserGroupInfo(PyVmomi):
    def __init__(self, module):
        super(VcenterDomainUserGroupInfo, self).__init__(module)
        self.domain = self.params['domain']
        self.search_string = self.params['search_string']
        self.belongs_to_group = self.params['belongs_to_group']
        self.belongs_to_user = self.params['belongs_to_user']
        self.exact_match = self.params['exact_match']
        self.find_users = self.params['find_users']
        self.find_groups = self.params['find_groups']

    def execute(self):
        user_directory_manager = self.content.userDirectory

        if not self.domain.upper() in user_directory_manager.domainList:
            self.module.fail_json(msg="domain not found: %s" % self.domain)

        try:
            user_search_result = user_directory_manager.RetrieveUserGroups(
                domain=self.domain,
                searchStr=self.search_string,
                belongsToGroup=self.belongs_to_group,
                belongsToUser=self.belongs_to_user,
                exactMatch=self.exact_match,
                findUsers=self.find_users,
                findGroups=self.find_groups
            )
        except vim.fault.NotFound as e:
            self.module.fail_json(msg="%s" % to_native(e.msg))
        except Exception as e:
            self.module.fail_json(msg="Couldn't gather domain user or group information: %s" % to_native(e))

        user_search_result_normalization = []
        if user_search_result:
            for object in user_search_result:
                user_search_result_normalization.append({
                    'fullName': object.fullName,
                    'principal': object.principal,
                    'group': object.group
                })

        self.module.exit_json(changed=False, domain_user_groups=user_search_result_normalization)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        domain=dict(type='str', default='vsphere.local'),
        search_string=dict(type='str', required=True),
        belongs_to_group=dict(type='str', default=None),
        belongs_to_user=dict(type='str', default=None),
        exact_match=dict(type='bool', default=False),
        find_users=dict(type='bool', default=True),
        find_groups=dict(type='bool', default=True)
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vcenter_domain_user_info = VcenterDomainUserGroupInfo(module)
    vcenter_domain_user_info.execute()


if __name__ == "__main__":
    main()
