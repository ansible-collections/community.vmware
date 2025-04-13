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
module: vmware_tag_info
short_description: Manage VMware tag info
description:
- This module can be used to collect information about VMware tags.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
author:
- Abhijeet Kasurde (@Akasurde)
requirements:
- vSphere Automation SDK
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation

'''

EXAMPLES = r'''
- name: Get info about tag
  community.vmware.vmware_tag_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: Get category id from the given tag
  community.vmware.vmware_tag_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost
  register: tag_details
- debug:
    msg: "{{ tag_details.tag_facts['fedora_machines']['tag_category_id'] }}"

- name: Gather tag id from the given tag
  community.vmware.vmware_tag_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
  delegate_to: localhost
  register: tag_results
- set_fact:
    tag_id: "{{ item.tag_id }}"
  loop: "{{ tag_results.tag_info|json_query(query) }}"
  vars:
    query: "[?tag_name==`tag0001`]"
- debug: var=tag_id
'''

RETURN = r'''
tag_facts:
  description: dictionary of tag metadata
  returned: on success
  type: dict
  sample: {
        "Sample_Tag_0002": {
            "tag_category_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL",
            "tag_description": "Sample Description",
            "tag_id": "urn:vmomi:InventoryServiceTag:a141f212-0f82-4f05-8eb3-c49647c904c5:GLOBAL",
            "tag_used_by": []
        },
        "fedora_machines": {
            "tag_category_id": "urn:vmomi:InventoryServiceCategory:baa90bae-951b-4e87-af8c-be681a1ba30c:GLOBAL",
            "tag_description": "",
            "tag_id": "urn:vmomi:InventoryServiceTag:7d27d182-3ecd-4200-9d72-410cc6398a8a:GLOBAL",
            "tag_used_by": []
        },
        "ubuntu_machines": {
            "tag_category_id": "urn:vmomi:InventoryServiceCategory:89573410-29b4-4cac-87a4-127c084f3d50:GLOBAL",
            "tag_description": "",
            "tag_id": "urn:vmomi:InventoryServiceTag:7f3516d5-a750-4cb9-8610-6747eb39965d:GLOBAL",
            "tag_used_by": []
        }
    }

tag_info:
    description: list of tag metadata
    returned: on success
    type: list
    sample: [
        {   "tag_name": "Sample_Tag_0002",
            "tag_category_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL",
            "tag_description": "Sample Description",
            "tag_id": "urn:vmomi:InventoryServiceTag:a141f212-0f82-4f05-8eb3-c49647c904c5:GLOBAL",
            "tag_used_by": []
        },
        {   "tag_name": "Sample_Tag_0002",
            "tag_category_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL",
            "tag_description": "",
            "tag_id": "urn:vmomi:InventoryServiceTag:7d27d182-3ecd-4200-9d72-410cc6398a8a:GLOBAL",
            "tag_used_by": []
        },
        {   "tag_name": "ubuntu_machines",
            "tag_category_id": "urn:vmomi:InventoryServiceCategory:89573410-29b4-4cac-87a4-127c084f3d50:GLOBAL",
            "tag_description": "",
            "tag_id": "urn:vmomi:InventoryServiceTag:7f3516d5-a750-4cb9-8610-6747eb39965d:GLOBAL",
            "tag_used_by": []
        }
    ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import rest_compatible_argument_spec


class VmTagInfoManager(VmwareRestClient):
    def __init__(self, module):
        """Constructor."""
        super(VmTagInfoManager, self).__init__(module)

    def get_all_tags(self):
        """
        Retrieve all tag information.
        """
        global_tag_info = list()
        # Backward compatability
        global_tags = dict()
        tag_service = self.api_client.tagging.Tag
        for tag in tag_service.list():
            tag_obj = tag_service.get(tag)
            global_tags[tag_obj.name] = dict(
                tag_description=tag_obj.description,
                tag_used_by=tag_obj.used_by,
                tag_category_id=tag_obj.category_id,
                tag_id=tag_obj.id
            )
            global_tag_info.append(dict(
                tag_name=tag_obj.name,
                tag_description=tag_obj.description,
                tag_used_by=tag_obj.used_by,
                tag_category_id=tag_obj.category_id,
                tag_id=tag_obj.id
            ))

        self.module.exit_json(
            changed=False,
            tag_facts=global_tags,
            tag_info=global_tag_info
        )


def main():
    argument_spec = rest_compatible_argument_spec()
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    vmware_tag_info = VmTagInfoManager(module)
    vmware_tag_info.get_all_tags()


if __name__ == '__main__':
    main()
