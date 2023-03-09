#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_custom_attribute
version_added: '3.2.0'
short_description: Manage custom attributes definitions
description:
  - This module can be used to add and remove custom attributes definitions for various vSphere objects.
author:
  - Mario Lenz (@mariolenz)
options:
  custom_attribute:
    description:
      - Name of the custom attribute.
    required: true
    type: str
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
      - Global
      - HostSystem
      - ResourcePool
      - VirtualMachine
    required: true
  state:
    description:
      - Manage definition of custom attributes.
      - If set to C(present) and definition not present, then custom attribute definition is created.
      - If set to C(present) and definition is present, then no action taken.
      - If set to C(absent) and definition is present, then custom attribute definition is removed.
      - If set to C(absent) and definition is absent, then no action taken.
    default: 'present'
    choices: ['present', 'absent']
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Add VM Custom Attribute Definition
  community.vmware.vmware_custom_attribute:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: present
    object_type: VirtualMachine
    custom_attribute: custom_attr_def_1
  delegate_to: localhost
  register: defs

- name: Remove VM Custom Attribute Definition
  community.vmware.vmware_custom_attribute:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: absent
    object_type: VirtualMachine
    custom_attribute: custom_attr_def_1
  delegate_to: localhost
  register: defs
'''

RETURN = r'''
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec

try:
    from pyVmomi import vim
except ImportError:
    pass


class CustomAttribute(PyVmomi):
    def __init__(self, module):
        super(CustomAttribute, self).__init__(module)

        if not self.is_vcenter():
            self.module.fail_json(msg="You have to connect to a vCenter server!")

        object_types_map = {
            'Cluster': vim.ClusterComputeResource,
            'Datacenter': vim.Datacenter,
            'Datastore': vim.Datastore,
            'DistributedVirtualPortgroup': vim.DistributedVirtualPortgroup,
            'DistributedVirtualSwitch': vim.DistributedVirtualSwitch,
            'Folder': vim.Folder,
            'Global': None,
            'HostSystem': vim.HostSystem,
            'ResourcePool': vim.ResourcePool,
            'VirtualMachine': vim.VirtualMachine
        }

        self.object_type = object_types_map[self.params['object_type']]

    def remove_custom_def(self, field):
        changed = False
        for x in self.custom_field_mgr:
            if x.name == field and x.managedObjectType == self.object_type:
                changed = True
                if not self.module.check_mode:
                    self.content.customFieldsManager.RemoveCustomFieldDef(key=x.key)
                break
        return {'changed': changed, 'failed': False}

    def add_custom_def(self, field):
        changed = False
        found = False
        for x in self.custom_field_mgr:
            if x.name == field and x.managedObjectType == self.object_type:
                found = True
                break

        if not found:
            changed = True
            if not self.module.check_mode:
                self.content.customFieldsManager.AddFieldDefinition(name=field, moType=self.object_type)
        return {'changed': changed, 'failed': False}


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        custom_attribute=dict(type='str', no_log=False, required=True),
        object_type=dict(type='str', required=True, choices=[
            'Cluster',
            'Datacenter',
            'Datastore',
            'DistributedVirtualPortgroup',
            'DistributedVirtualSwitch',
            'Folder',
            'Global',
            'HostSystem',
            'ResourcePool',
            'VirtualMachine'
        ]),
        state=dict(type='str', default='present', choices=['absent', 'present']),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    pyv = CustomAttribute(module)
    results = dict(changed=False, custom_attribute_defs=list())
    if module.params['state'] == "present":
        results = pyv.add_custom_def(module.params['custom_attribute'])
    elif module.params['state'] == "absent":
        results = pyv.remove_custom_def(module.params['custom_attribute'])

    module.exit_json(**results)


if __name__ == '__main__':
    main()
