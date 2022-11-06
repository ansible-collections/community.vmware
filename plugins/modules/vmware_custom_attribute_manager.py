#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright, (c) 2022, Mario Lenz <m@riolenz.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_custom_attribute_manager
short_description: Manage custom attributes from VMware for the given vSphere object
description:
  - This module can be used to add, remove and update custom attributes for the given vSphere object.
author:
  - Mario Lenz (@mariolenz)
options:
  custom_attributes:
    description:
      - A list of name and value of custom attributes that needs to be manage.
      - Value of custom attribute is not required and will be ignored, if C(state) is set to C(absent).
    suboptions:
      name:
        description:
          - Name of the attribute.
        type: str
        required: True
      value:
        description:
          - Value of the attribute.
        type: str
        default: ''
    required: True
    type: list
    elements: dict
  object_name:
    description:
      - Name of the vSphere object to work with.
    type: str
    required: True
  object_type:
    description:
      - Type of the object the custom attribute is associated with.
    type: str
    choices:
      - Datacenter
      - Cluster
      - HostSystem
      - ResourcePool
      - Folder
      - VirtualMachine
      - DistributedVirtualSwitch
      - DistributedVirtualPortgroup
      - Datastore
    required: True
  state:
    description:
      - The action to take.
      - If set to C(present), then custom attribute is added or updated.
      - If set to C(absent), then custom attribute is removed.
    default: 'present'
    choices: ['present', 'absent']
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Add virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    object_name: vm1
    object_type: VirtualMachine
    state: present
    custom_attributes:
      - name: MyAttribute
        value: MyValue
  delegate_to: localhost

- name: Add multiple virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    object_name: vm1
    object_type: VirtualMachine
    state: present
    custom_attributes:
      - name: MyAttribute
        value: MyValue
      - name: MyAttribute2
        value: MyValue2
  delegate_to: localhost

- name: Remove virtual machine Attribute
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    object_name: vm1
    object_type: VirtualMachine
    state: absent
    custom_attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes
'''

RETURN = r'''
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec


class CustomAttributeManager(PyVmomi):
    def __init__(self, module):
        super(CustomAttributeManager, self).__init__(module)

        self.custom_attributes = self.params['custom_attributes']

        object_types_map = {
            'Datacenter': vim.Datacenter,
            'Cluster': vim.ClusterComputeResource,
            'HostSystem': vim.HostSystem,
            'ResourcePool': vim.ResourcePool,
            'Folder': vim.Folder,
            'VirtualMachine': vim.VirtualMachine,
            'DistributedVirtualSwitch': vim.DistributedVirtualSwitch,
            'DistributedVirtualPortgroup': vim.DistributedVirtualPortgroup,
            'Datastore': vim.Datastore
        }

        self.object_type = object_types_map[self.params['object_type']]

        self.object_name = self.params['object_name']
        self.obj = self.find_object_by_name(self.params['object_name'], self.object_type)
        if self.obj is None:
            module.fail_json(msg="Unable to manage custom attributes for non-existing"
                                 " object %s." % self.object_name)

        for ca in self.custom_attributes:
            for x in self.custom_field_mgr:
                if x.name == ca.name and x.managedObjectType == self.object_type:
                    ca['key'] = x.key
                    break

        for ca in self.custom_attributes:
            if 'key' not in ca:
                self.module.fail_json(msg="Custom attribute %s does not exist for object type %s." % (ca.name, self.params['object_type']))

    def set_custom_attribute(self):
        changed = False

        for ca in self.custom_attributes:
            for x in self.obj.customValue:
                if ca.key == x.key and ca.value != x.value:
                    changed = True
                    if not self.module.check_mode:
                        self.content.customFieldsManager.SetField(entity=self.obj, key=ca.key, value=ca.value)

        return {'changed': changed, 'failed': False}

    def remove_custom_attribute(self):
        changed = False

        for ca in self.custom_attributes:
            for x in self.obj.customValue:
                if ca.key == x.key and x.value is not None:
                    changed = True
                    if not self.module.check_mode:
                        self.content.customFieldsManager.SetField(entity=self.obj, key=ca.key, value=None)

        return {'changed': changed, 'failed': False}


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        custom_attributes=dict(
            type='list',
            required=True,
            elements='dict',
            options=dict(
                name=dict(type='str', required=True),
                value=dict(type='str', default=''),
            )
        ),
        object_name=dict(type='str', required=True),
        object_type=dict(type='str', required=True, choices=[
            'Datacenter',
            'Cluster',
            'HostSystem',
            'ResourcePool',
            'Folder',
            'VirtualMachine',
            'DistributedVirtualSwitch',
            'DistributedVirtualPortgroup',
            'Datastore'
        ]),
        state=dict(type='str', default='present',
                   choices=['absent', 'present']),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    pyv = CustomAttributeManager(module)
    results = {'changed': False, 'failed': False}

    if module.params['state'] == "present":
        results = pyv.set_custom_attributes()
    elif module.params['state'] == "absent":
        results = pyv.remove_custom_attributes()

    module.exit_json(**results)


if __name__ == '__main__':
    main()
