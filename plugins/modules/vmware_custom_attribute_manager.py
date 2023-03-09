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
version_added: '3.2.0'
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
        required: true
      value:
        description:
          - Value of the attribute.
        type: str
        default: ''
    required: true
    type: list
    elements: dict
  object_name:
    description:
      - Name of the vSphere object to work with.
    type: str
    required: true
  object_type:
    description:
      - Type of the object the custom attribute is associated with.
    type: str
    choices:
      - Cluster
      - Datacenter
      - Datastore
      - DistributedVirtualPortgroup
      - DistributedVirtualSwitch
      - Folder
      - HostSystem
      - ResourcePool
      - VirtualMachine
    required: true
  state:
    description:
      - If set to C(present), the custom attribute is set to the given value.
      - If set to C(absent), the custom attribute is cleared. The given value is ignored in this case.
    default: 'present'
    choices: ['present', 'absent']
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Add virtual machine custom attributes
  community.vmware.vmware_custom_attribute_manager:
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
  community.vmware.vmware_custom_attribute_manager:
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
  community.vmware.vmware_custom_attribute_manager:
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
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec, find_obj


class CustomAttributeManager(PyVmomi):
    def __init__(self, module):
        super(CustomAttributeManager, self).__init__(module)

        if not self.is_vcenter():
            self.module.fail_json(msg="You have to connect to a vCenter server!")

        object_types_map = {
            'Cluster': vim.ClusterComputeResource,
            'Datacenter': vim.Datacenter,
            'Datastore': vim.Datastore,
            'DistributedVirtualPortgroup': vim.DistributedVirtualPortgroup,
            'DistributedVirtualSwitch': vim.DistributedVirtualSwitch,
            'Folder': vim.Folder,
            'HostSystem': vim.HostSystem,
            'ResourcePool': vim.ResourcePool,
            'VirtualMachine': vim.VirtualMachine
        }

        self.object_type = object_types_map[self.params['object_type']]

        self.object_name = self.params['object_name']
        self.obj = find_obj(self.content, [self.object_type], self.params['object_name'])
        if self.obj is None:
            module.fail_json(msg="Unable to manage custom attributes for non-existing"
                                 " object %s." % self.object_name)

        self.ca_list = self.params['custom_attributes'].copy()

        for ca in self.ca_list:
            for av_field in self.obj.availableField:
                if av_field.name == ca['name']:
                    ca['key'] = av_field.key
                    break

        for ca in self.ca_list:
            if 'key' not in ca:
                self.module.fail_json(msg="Custom attribute %s does not exist for object type %s." % (ca['name'], self.params['object_type']))

    def set_custom_attributes(self):
        changed = False
        obj_cas_set = [x.key for x in self.obj.value]

        for ca in self.ca_list:
            if ca['key'] not in obj_cas_set:
                changed = True
                if not self.module.check_mode:
                    self.content.customFieldsManager.SetField(entity=self.obj, key=ca['key'], value=ca['value'])
                continue
            for x in self.obj.customValue:
                if ca['key'] == x.key and ca['value'] != x.value:
                    changed = True
                    if not self.module.check_mode:
                        self.content.customFieldsManager.SetField(entity=self.obj, key=ca['key'], value=ca['value'])

        return {'changed': changed, 'failed': False}

    def remove_custom_attributes(self):
        changed = False

        for ca in self.ca_list:
            for x in self.obj.customValue:
                if ca['key'] == x.key and x.value != '':
                    changed = True
                    if not self.module.check_mode:
                        self.content.customFieldsManager.SetField(entity=self.obj, key=ca['key'], value='')

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
            'Cluster',
            'Datacenter',
            'Datastore',
            'DistributedVirtualPortgroup',
            'DistributedVirtualSwitch',
            'Folder',
            'HostSystem',
            'ResourcePool',
            'VirtualMachine'
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
