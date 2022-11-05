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
module: vmware_tag_manager
short_description: Manage association of VMware tags with VMware objects
description:
- This module can be used to assign / remove VMware tags from the given VMware objects.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.
author:
- Abhijeet Kasurde (@Akasurde)
- Frederic Van Reet (@GBrawl)
requirements:
- vSphere Automation SDK
options:
    tag_names:
      description:
      - List of tag(s) to be managed.
      - User can also specify category name by specifying colon separated value. For example, "category_name:tag_name".
      - User can also specify tag and category as dict, when tag or category contains colon.
        See example for more information. Added in version 2.10.
      - User can skip category name if you have unique tag names.
      required: True
      type: list
      elements: raw
    state:
      description:
      - If C(state) is set to C(add) or C(present) will add the tags to the existing tag list of the given object.
      - If C(state) is set to C(remove) or C(absent) will remove the tags from the existing tag list of the given object.
      - If C(state) is set to C(set) will replace the tags of the given objects with the user defined list of tags.
      default: add
      choices: [ present, absent, add, remove, set ]
      type: str
    object_type:
      description:
      - Type of object to work with.
      required: True
      choices:
        - VirtualMachine
        - Datacenter
        - ClusterComputeResource
        - HostSystem
        - DistributedVirtualSwitch
        - DistributedVirtualPortgroup
        - Datastore
        - DatastoreCluster
        - ResourcePool
        - Folder
      type: str
    object_name:
      description:
      - Name of the object to work with.
      - For DistributedVirtualPortgroups the format should be "switch_name:portgroup_name"
      - Required if C(moid) is not set.
      required: False
      type: str
    moid:
      description:
      - Managed object ID for the given object.
      - Required if C(object_name) is not set.
      required: False
      type: str
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation

'''

EXAMPLES = r'''
- name: Add tags to a virtual machine
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0002
      - Category_0001:Sample_Tag_0003
    object_name: Fedora_VM
    object_type: VirtualMachine
    state: add
  delegate_to: localhost

- name: Specify tag and category as dict
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - tag: tag_0001
        category: cat_0001
      - tag: tag_0002
        category: cat_0002
    object_name: Fedora_VM
    object_type: VirtualMachine
    state: add
  delegate_to: localhost

- name: Remove a tag from a virtual machine
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0002
    object_name: Fedora_VM
    object_type: VirtualMachine
    state: remove
  delegate_to: localhost

- name: Add tags to a distributed virtual switch
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0003
    object_name: Switch_0001
    object_type: DistributedVirtualSwitch
    state: add
  delegate_to: localhost

- name: Add tags to a distributed virtual portgroup
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Tag_0004
    object_name: Switch_0001:Portgroup_0001
    object_type: DistributedVirtualPortgroup
    state: add
  delegate_to: localhost


- name: Get information about folders
  community.vmware.vmware_folder_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: 'Asia-Datacenter1'
  delegate_to: localhost
  register: r
- name: Set Managed object ID for the given folder
  ansible.builtin.set_fact:
    folder_mo_id: "{{ (r.flat_folder_info | selectattr('path', 'equalto', '/Asia-Datacenter1/vm/tier1/tier2') | map(attribute='moid'))[0] }}"
- name: Add tags to a Folder using managed object id
  community.vmware.vmware_tag_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    tag_names:
      - Sample_Cat_0004:Sample_Tag_0004
    object_type: Folder
    moid: "{{ folder_mo_id }}"
    state: add
  delegate_to: localhost

'''

RETURN = r'''
tag_status:
    description: metadata about tags related to object configuration
    returned: on success
    type: list
    sample: {
        "current_tags": [
            "backup",
            "security"
        ],
        "desired_tags": [
            "security"
        ],
        "previous_tags": [
            "backup",
            "security"
        ]
    }
'''
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils.vmware import (PyVmomi, find_dvs_by_name, find_dvspg_by_name)
try:
    from com.vmware.vapi.std_client import DynamicID
    from com.vmware.vapi.std.errors_client import Error
except ImportError:
    pass


class VmwareTagManager(VmwareRestClient):
    def __init__(self, module):
        """
        Constructor
        """
        super(VmwareTagManager, self).__init__(module)
        self.pyv = PyVmomi(module=module)

        moid = self.params.get('moid')
        self.object_type = self.params.get('object_type')
        managed_object_id = None

        if moid:
            managed_object_id = moid
        else:
            object_name = self.params.get('object_name')
            managed_object = self.get_managed_object(object_name, self.object_type)

            if managed_object is None:
                self.module.fail_json(msg="Failed to find the managed object for %s with type %s" % (object_name, self.object_type))

            if not hasattr(managed_object, '_moId'):
                self.module.fail_json(msg="Unable to find managed object id for %s managed object" % object_name)

            managed_object_id = managed_object._moId

        self.dynamic_managed_object = DynamicID(type=self.object_type, id=managed_object_id)

        self.tag_service = self.api_client.tagging.Tag
        self.category_service = self.api_client.tagging.Category
        self.tag_association_svc = self.api_client.tagging.TagAssociation

        self.tag_names = self.params.get('tag_names')

    def get_managed_object(self, object_name=None, object_type=None):
        managed_object = None
        if not all([object_type, object_name]):
            return managed_object

        if object_type == 'VirtualMachine':
            managed_object = self.pyv.get_vm_or_template(object_name)

        if object_type == 'Folder':
            managed_object = self.pyv.find_folder_by_name(object_name)

        if object_type == 'Datacenter':
            managed_object = self.pyv.find_datacenter_by_name(object_name)

        if object_type == 'Datastore':
            managed_object = self.pyv.find_datastore_by_name(object_name)

        if object_type == 'DatastoreCluster':
            managed_object = self.pyv.find_datastore_cluster_by_name(object_name)
            self.object_type = 'StoragePod'

        if object_type == 'ClusterComputeResource':
            managed_object = self.pyv.find_cluster_by_name(object_name)

        if object_type == 'ResourcePool':
            managed_object = self.pyv.find_resource_pool_by_name(object_name)

        if object_type == 'HostSystem':
            managed_object = self.pyv.find_hostsystem_by_name(object_name)

        if object_type == 'DistributedVirtualSwitch':
            managed_object = find_dvs_by_name(self.pyv.content, object_name)
            self.object_type = 'VmwareDistributedVirtualSwitch'

        if object_type == 'DistributedVirtualPortgroup':
            dvs_name, pg_name = object_name.split(":", 1)
            dv_switch = find_dvs_by_name(self.pyv.content, dvs_name)
            if dv_switch is None:
                self.module.fail_json(msg="A distributed virtual switch with name %s does not exist" % dvs_name)
            managed_object = find_dvspg_by_name(dv_switch, pg_name)

        return managed_object

    def ensure_state(self):
        """
        Manage the internal state of tags

        """
        results = dict(
            changed=False,
            tag_status=dict(),
        )
        tag_objs = []
        changed = False
        action = self.params.get('state')
        try:
            available_tag_obj = self.get_tags_for_object(tag_service=self.tag_service,
                                                         tag_assoc_svc=self.tag_association_svc,
                                                         dobj=self.dynamic_managed_object)
        except Error as error:
            self.module.fail_json(msg="%s" % self.get_error_message(error))

        _temp_prev_tags = ["%s:%s" % (tag['category_name'], tag['name']) for tag in self.get_tags_for_dynamic_obj(self.dynamic_managed_object)]
        results['tag_status']['previous_tags'] = _temp_prev_tags
        results['tag_status']['desired_tags'] = self.tag_names

        # Check if category and tag combination exists as per user request
        for tag in self.tag_names:
            category_obj, category_name, tag_name = None, None, None
            if isinstance(tag, dict):
                tag_name = tag.get('tag')
                category_name = tag.get('category')
                if category_name:
                    # User specified category
                    category_obj = self.search_svc_object_by_name(self.category_service, category_name)
                    if not category_obj:
                        self.module.fail_json(msg="Unable to find the category %s" % category_name)
            elif isinstance(tag, str):
                if ":" in tag:
                    # User specified category
                    category_name, tag_name = tag.split(":", 1)
                    category_obj = self.search_svc_object_by_name(self.category_service, category_name)
                    if not category_obj:
                        self.module.fail_json(msg="Unable to find the category %s" % category_name)
                else:
                    # User specified only tag
                    tag_name = tag

            if category_obj:
                tag_obj = self.get_tag_by_category(tag_name=tag_name, category_id=category_obj.id)
            elif category_name:
                tag_obj = self.get_tag_by_category(tag_name=tag_name, category_name=category_name)
            else:
                tag_obj = self.get_tag_by_name(tag_name=tag_name)

            if not tag_obj:
                self.module.fail_json(msg="Unable to find the tag %s" % tag_name)

            tag_objs.append(tag_obj)

        if action in ('add', 'present'):
            for tag_obj in tag_objs:
                if tag_obj not in available_tag_obj:
                    # Tag is not already applied
                    try:
                        self.tag_association_svc.attach(tag_id=tag_obj.id, object_id=self.dynamic_managed_object)
                        changed = True
                    except Error as error:
                        self.module.fail_json(msg="%s" % self.get_error_message(error))

        elif action == 'set':
            for av_tag in available_tag_obj:
                if av_tag not in tag_objs:
                    # Tag not in the defined list
                    try:
                        self.tag_association_svc.detach(tag_id=av_tag.id, object_id=self.dynamic_managed_object)
                        changed = True
                    except Error as error:
                        self.module.fail_json(msg="%s" % self.get_error_message(error))

            for tag_obj in tag_objs:
                if tag_obj not in available_tag_obj:
                    # Tag is not already applied
                    try:
                        self.tag_association_svc.attach(tag_id=tag_obj.id, object_id=self.dynamic_managed_object)
                        changed = True
                    except Error as error:
                        self.module.fail_json(msg="%s" % self.get_error_message(error))

        elif action in ('remove', 'absent'):
            for tag_obj in tag_objs:
                if tag_obj in available_tag_obj:
                    try:
                        self.tag_association_svc.detach(tag_id=tag_obj.id, object_id=self.dynamic_managed_object)
                        changed = True
                    except Error as error:
                        self.module.fail_json(msg="%s" % self.get_error_message(error))

        _temp_curr_tags = ["%s:%s" % (tag['category_name'], tag['name']) for tag in self.get_tags_for_dynamic_obj(self.dynamic_managed_object)]
        results['tag_status']['current_tags'] = _temp_curr_tags
        results['changed'] = changed
        self.module.exit_json(**results)


def main():
    argument_spec = VmwareRestClient.vmware_client_argument_spec()
    argument_spec.update(
        tag_names=dict(type='list', required=True, elements='raw'),
        state=dict(type='str', choices=['absent', 'add', 'present', 'remove', 'set'], default='add'),
        moid=dict(type='str'),
        object_name=dict(type='str'),
        object_type=dict(type='str', required=True, choices=['VirtualMachine', 'Datacenter', 'ClusterComputeResource',
                                                             'HostSystem', 'DistributedVirtualSwitch',
                                                             'DistributedVirtualPortgroup', 'Datastore', 'ResourcePool',
                                                             'Folder', 'DatastoreCluster']),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=[
            ('moid', 'object_name'),
        ],
        required_one_of=[
            ['moid', 'object_name'],
        ]
    )

    vmware_tag_manager = VmwareTagManager(module)
    vmware_tag_manager.ensure_state()


if __name__ == '__main__':
    main()
