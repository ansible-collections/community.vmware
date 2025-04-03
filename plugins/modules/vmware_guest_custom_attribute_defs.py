#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_custom_attribute_defs
short_description: Manage custom attributes definitions for virtual machine from VMware
description:
    - This module can be used to add and remove custom attributes definitions for the given virtual machine from VMware.
author:
    - Jimmy Conner (@cigamit)
    - Abhijeet Kasurde (@Akasurde)
options:
   attribute_key:
     description:
     - Name of the custom attribute definition.
     - This is required parameter, if O(state=present) or O(state=absent).
     required: false
     type: str
   state:
     description:
     - Manage definition of custom attributes.
     - If set to V(present) and definition not present, then custom attribute definition is created.
     - If set to V(present) and definition is present, then no action taken.
     - If set to V(absent) and definition is present, then custom attribute definition is removed.
     - If set to V(absent) and definition is absent, then no action taken.
     default: 'present'
     choices: ['present', 'absent']
     type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Add VMware Attribute Definition
  community.vmware.vmware_guest_custom_attribute_defs:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: present
    attribute_key: custom_attr_def_1
  delegate_to: localhost
  register: defs

- name: Remove VMware Attribute Definition
  community.vmware.vmware_guest_custom_attribute_defs:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: absent
    attribute_key: custom_attr_def_1
  delegate_to: localhost
  register: defs
'''

RETURN = r'''
custom_attribute_defs:
    description: list of all current attribute definitions
    returned: always
    type: list
    sample: ["sample_5", "sample_4"]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec

try:
    from pyVmomi import vim
except ImportError:
    pass


class VmAttributeDefManager(PyVmomi):
    def __init__(self, module):
        super(VmAttributeDefManager, self).__init__(module)

    def remove_custom_def(self, field):
        changed = False
        f = dict()
        for x in self.custom_field_mgr:
            if x.name == field and x.managedObjectType == vim.VirtualMachine:
                changed = True
                if not self.module.check_mode:
                    self.content.customFieldsManager.RemoveCustomFieldDef(key=x.key)
                    break
            f[x.name] = (x.key, x.managedObjectType)
        return {'changed': changed, 'failed': False, 'custom_attribute_defs': list(f.keys())}

    def add_custom_def(self, field):
        changed = False
        found = False
        f = dict()
        for x in self.custom_field_mgr:
            if x.name == field:
                found = True
            f[x.name] = (x.key, x.managedObjectType)

        if not found:
            changed = True
            if not self.module.check_mode:
                new_field = self.content.customFieldsManager.AddFieldDefinition(name=field, moType=vim.VirtualMachine)
                f[new_field.name] = (new_field.key, new_field.type)
        return {'changed': changed, 'failed': False, 'custom_attribute_defs': list(f.keys())}


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        attribute_key=dict(type='str', no_log=False),
        state=dict(type='str', default='present', choices=['absent', 'present']),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ['state', 'present', ['attribute_key']],
            ['state', 'absent', ['attribute_key']],
        ]
    )

    pyv = VmAttributeDefManager(module)
    results = dict(changed=False, custom_attribute_defs=list())
    if module.params['state'] == "present":
        results = pyv.add_custom_def(module.params['attribute_key'])
    elif module.params['state'] == "absent":
        results = pyv.remove_custom_def(module.params['attribute_key'])

    module.exit_json(**results)


if __name__ == '__main__':
    main()
