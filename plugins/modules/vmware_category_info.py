#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_category_info
short_description: Gather info about VMware tag categories
description:
- This module can be used to gather information about VMware tag categories.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in earlier versions of vSphere.
author:
- Abhijeet Kasurde (@Akasurde)
requirements:
- vSphere Automation SDK
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation

'''

EXAMPLES = r'''
- name: Gather info about tag categories
  community.vmware.vmware_category_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: all_tag_category_info

- name: Gather category id from given tag category
  community.vmware.vmware_category_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: tag_category_results

- set_fact:
    category_id: "{{ item.category_id }}"
  loop: "{{ tag_category_results.tag_category_info|json_query(query) }}"
  vars:
    query: "[?category_name==`Category0001`]"
- debug: var=category_id

'''

RETURN = r'''
tag_category_info:
  description: metadata of tag categories
  returned: always
  type: list
  sample: [
    {
       "category_associable_types": [],
       "category_cardinality": "MULTIPLE",
       "category_description": "awesome description",
       "category_id": "urn:vmomi:InventoryServiceCategory:e785088d-6981-4b1c-9fb8-1100c3e1f742:GLOBAL",
       "category_name": "Category0001",
       "category_used_by": []
    },
    {
       "category_associable_types": [
            "VirtualMachine"
       ],
       "category_cardinality": "SINGLE",
       "category_description": "another awesome description",
       "category_id": "urn:vmomi:InventoryServiceCategory:ae5b7c6c-e622-4671-9b96-76e93adb70f2:GLOBAL",
       "category_name": "template_tag",
       "category_used_by": []
    }
  ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import rest_compatible_argument_spec


class VmwareCategoryInfoManager(VmwareRestClient):
    def __init__(self, module):
        super(VmwareCategoryInfoManager, self).__init__(module)
        self.category_service = self.api_client.tagging.Category

    def get_all_tag_categories(self):
        """Retrieve all tag category information."""
        global_tag_categories = []
        for category in self.category_service.list():
            category_obj = self.category_service.get(category)
            global_tag_categories.append(
                dict(
                    category_description=category_obj.description,
                    category_used_by=category_obj.used_by,
                    category_cardinality=str(category_obj.cardinality),
                    category_associable_types=category_obj.associable_types,
                    category_id=category_obj.id,
                    category_name=category_obj.name,
                )
            )

        self.module.exit_json(changed=False, tag_category_info=global_tag_categories)


def main():
    argument_spec = rest_compatible_argument_spec()
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_category_info = VmwareCategoryInfoManager(module)
    vmware_category_info.get_all_tag_categories()


if __name__ == '__main__':
    main()
