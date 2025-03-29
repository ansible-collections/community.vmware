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
module: vmware_tag
short_description: Manage VMware tags
description:
- This module can be used to create / delete / update VMware tags.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
author:
- Abhijeet Kasurde (@Akasurde)
requirements:
- vSphere Automation SDK
options:
    tag_name:
      description:
      - The name of tag to manage.
      required: true
      aliases: [ 'tag', 'name' ]
      type: str
    tag_description:
      description:
      - The tag description.
      - This is required only if O(state=present).
      - This parameter is ignored, when O(state=absent).
      - Process of updating tag only allows description change.
      required: false
      default: ''
      aliases: [ 'description' ]
      type: str
    category_id:
      description:
      - The unique ID generated by vCenter should be used to.
      - User can get this unique ID from facts module.
      - Required if O(category_name) is not set.
      required: false
      type: str
    category_name:
      description:
      - The name of category.
      - Required if O(category_id) is not set.
      required: false
      aliases: [ 'category' ]
      type: str
      version_added: '3.5.0'
    state:
      description:
      - The state of tag.
      - If set to V(present) and tag does not exists, then tag is created.
      - If set to V(present) and tag exists, then tag is updated.
      - If set to V(absent) and tag exists, then tag is deleted.
      - If set to V(absent) and tag does not exists, no action is taken.
      required: false
      default: 'present'
      choices: [ 'present', 'absent' ]
      type: str
extends_documentation_fragment:
- vmware.vmware.base_options
- vmware.vmware.additional_rest_options

'''

EXAMPLES = r'''
- name: Create a tag
  community.vmware.vmware_tag:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    category_id: 'urn:vmomi:InventoryServiceCategory:e785088d-6981-4b1c-9fb8-1100c3e1f742:GLOBAL'
    tag_name: Sample_Tag_0002
    tag_description: Sample Description
    state: present
  delegate_to: localhost

- name: Update tag description
  community.vmware.vmware_tag:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_name: Sample_Tag_0002
    tag_description: Some fancy description
    state: present
  delegate_to: localhost

- name: Delete tag
  community.vmware.vmware_tag:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_name: Sample_Tag_0002
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
tag_status:
  description: dictionary of tag metadata
  returned: on success
  type: dict
  sample: {
        "msg": "Tag 'Sample_Tag_0002' created.",
        "tag_id": "urn:vmomi:InventoryServiceTag:bff91819-f529-43c9-80ca-1c9dfda09441:GLOBAL"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
try:
    from com.vmware.vapi.std.errors_client import Error
except ImportError:
    pass


class VmwareTag(VmwareRestClient):
    def __init__(self, module):
        super(VmwareTag, self).__init__(module)
        self.tag_service = self.api_client.tagging.Tag
        self.tag_name = self.params.get('tag_name')
        self.category_service = self.api_client.tagging.Category
        self.category_id = self.params.get('category_id')

        if self.category_id is None:
            category_name = self.params.get('category_name')
            category_obj = self.search_svc_object_by_name(service=self.category_service, svc_obj_name=category_name)
            if category_obj is None:
                self.module.fail_json(msg="Unable to find the category %s" % category_name)

            self.category_id = category_obj.id

        self.tag_obj = self.get_tag_by_category_id(tag_name=self.tag_name, category_id=self.category_id)

    def ensure_state(self):
        """
        Manage internal states of tags

        """
        desired_state = self.params.get('state')
        states = {
            'present': {
                'present': self.state_update_tag,
                'absent': self.state_create_tag,
            },
            'absent': {
                'present': self.state_delete_tag,
                'absent': self.state_unchanged,
            }
        }
        states[desired_state][self.check_tag_status()]()

    def state_create_tag(self):
        """
        Create tag

        """
        tag_spec = self.tag_service.CreateSpec()
        tag_spec.name = self.tag_name
        tag_spec.description = self.params.get('tag_description')

        """
        There is no need to check if a category with the specified category_id
        exists. The tag service will do the corresponding checks and will fail
        if someone tries to create a tag for a category id that does not exist.

        """
        tag_spec.category_id = self.category_id
        tag_id = ''
        try:
            tag_id = self.tag_service.create(tag_spec)
        except Error as error:
            self.module.fail_json(msg="%s" % self.get_error_message(error))

        if tag_id is not None:
            self.module.exit_json(changed=True,
                                  tag_status=dict(msg="Tag '%s' created." % tag_spec.name, tag_id=tag_id))
        self.module.exit_json(changed=False,
                              tag_status=dict(msg="No tag created", tag_id=tag_id))

    def state_unchanged(self):
        """
        Return unchanged state

        """
        self.module.exit_json(changed=False)

    def state_update_tag(self):
        """
        Update tag

        """
        changed = False
        tag_id = self.tag_obj.id
        results = dict(msg="Tag %s is unchanged." % self.tag_name,
                       tag_id=tag_id)
        tag_desc = self.tag_obj.description
        desired_tag_desc = self.params.get('tag_description')
        if tag_desc != desired_tag_desc:
            tag_update_spec = self.tag_service.UpdateSpec()
            tag_update_spec.description = desired_tag_desc
            try:
                self.tag_service.update(tag_id, tag_update_spec)
            except Error as error:
                self.module.fail_json(msg="%s" % self.get_error_message(error))

            results['msg'] = 'Tag %s updated.' % self.tag_name
            changed = True

        self.module.exit_json(changed=changed, tag_status=results)

    def state_delete_tag(self):
        """
        Delete tag

        """
        tag_id = self.tag_obj.id
        try:
            self.tag_service.delete(tag_id=tag_id)
        except Error as error:
            self.module.fail_json(msg="%s" % self.get_error_message(error))

        self.module.exit_json(changed=True,
                              tag_status=dict(msg="Tag '%s' deleted." % self.tag_name, tag_id=tag_id))

    def check_tag_status(self):
        """
        Check if tag exists or not
        Returns: 'present' if tag found, else 'absent'

        """
        return 'present' if self.tag_obj is not None else 'absent'


def main():
    argument_spec = VmwareRestClient.vmware_client_argument_spec()
    argument_spec.update(
        tag_name=dict(type='str', aliases=['tag', 'name'], required=True),
        tag_description=dict(type='str', aliases=['description'], default='', required=False),
        category_id=dict(type='str'),
        category_name=dict(type='str', aliases=['category']),
        state=dict(type='str', choices=['present', 'absent'], default='present', required=False),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=[
            ('category_id', 'category_name'),
        ],
        required_one_of=[
            ['category_id', 'category_name'],
        ]
    )

    vmware_tag = VmwareTag(module)
    vmware_tag.ensure_state()


if __name__ == '__main__':
    main()
