#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright, (c) 2018, Ansible Project
# Copyright, (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_custom_attributes
short_description: Manage custom attributes from VMware for the given virtual machine
description:
    - This module can be used to add, remove and update custom attributes for the given virtual machine.
author:
    - Jimmy Conner (@cigamit)
    - Abhijeet Kasurde (@Akasurde)
options:
   name:
     description:
     - Name of the virtual machine to work with.
     - This is required parameter, if C(uuid) or C(moid) is not supplied.
     type: str
   state:
     description:
     - The action to take.
     - If set to C(present), then custom attribute is added or updated.
     - If set to C(absent), then custom attribute value is removed.
     default: 'present'
     choices: ['present', 'absent']
     type: str
   uuid:
     description:
     - UUID of the virtual machine to manage if known. This is VMware's unique identifier.
     - This is required parameter, if C(name) or C(moid) is not supplied.
     type: str
   moid:
     description:
     - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
     - This is required if C(name) or C(uuid) is not supplied.
     type: str
   use_instance_uuid:
     description:
     - Whether to use the VMware instance UUID rather than the BIOS UUID.
     default: false
     type: bool
   folder:
     description:
     - Absolute path to find an existing guest.
     - This is required parameter, if C(name) is supplied and multiple virtual machines with same name are found.
     type: str
   datacenter:
     description:
     - Datacenter name where the virtual machine is located in.
     type: str
   attributes:
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
     default: []
     type: list
     elements: dict
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Add virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: present
    attributes:
      - name: MyAttribute
        value: MyValue
  delegate_to: localhost
  register: attributes

- name: Add multiple virtual machine custom attributes
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: present
    attributes:
      - name: MyAttribute
        value: MyValue
      - name: MyAttribute2
        value: MyValue2
  delegate_to: localhost
  register: attributes

- name: Remove virtual machine Attribute
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
    state: absent
    attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes

- name: Remove virtual machine Attribute using Virtual Machine MoID
  community.vmware.vmware_guest_custom_attributes:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    moid: vm-42
    state: absent
    attributes:
      - name: MyAttribute
  delegate_to: localhost
  register: attributes
'''

RETURN = r'''
custom_attributes:
    description: metadata about the virtual machine attributes
    returned: always
    type: dict
    sample: {
        "mycustom": "my_custom_value",
        "mycustom_2": "my_custom_value_2",
        "sample_1": "sample_1_value",
        "sample_2": "sample_2_value",
        "sample_3": "sample_3_value"
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec


class VmAttributeManager(PyVmomi):
    def __init__(self, module):
        super(VmAttributeManager, self).__init__(module)

        # Initialize the variables.
        # Make the diff_config variable to check the difference between a new and existing config.
        # https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#diff
        self.diff_config = dict(before={}, after={})

        # reuslt_fields is the variable for the return value after the job finish.
        self.result_fields = {}

        # update_custom_attributes is the variable for storing the custom attributes to update.
        self.update_custom_attributes = []

        # changed variable is the flag of whether the target changed.
        # https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#changed
        self.changed = False

    def set_custom_field(self, vm, user_fields):
        """Add or update the custom attribute and value.

        Args:
            vm (vim.VirtualMachine): The managed object of a virtual machine.
            user_fields (list): list of the specified custom attributes by user.

        Returns:
            The dictionary for the ansible return value.
        """
        self.check_exists(vm, user_fields)
        if self.module.check_mode is True:
            self.module.exit_json(changed=self.changed, diff=self.diff_config)

        # If update_custom_attributes variable has elements, add or update the custom attributes and values.
        for field in self.update_custom_attributes:
            if 'key' in field:
                self.content.customFieldsManager.SetField(entity=vm, key=field['key'], value=field['value'])
            else:
                field_key = self.content.customFieldsManager.AddFieldDefinition(name=field['name'],
                                                                                moType=vim.VirtualMachine)
                self.content.customFieldsManager.SetField(entity=vm, key=field_key.key, value=field['value'])

            # Set result_fields for the return value.
            self.result_fields[field['name']] = field['value']

        return {'changed': self.changed, 'failed': False, 'custom_attributes': self.result_fields}

    def remove_custom_field(self, vm, user_fields):
        """Remove the value from the existing custom attribute.

        Args:
            vm (vim.VirtualMachine): The managed object of a virtual machine.
            user_fields (list): list of the specified custom attributes by user.

        Returns:
            The dictionary for the ansible return value.
        """
        # All custom attribute values will set blank to remove the value.
        for v in user_fields:
            v['value'] = ''

        self.check_exists(vm, user_fields)
        if self.module.check_mode is True:
            self.module.exit_json(changed=self.changed, diff=self.diff_config)

        # If update_custom_attributes variable has elements, remove the custom attribute values.
        for field in self.update_custom_attributes:
            self.content.customFieldsManager.SetField(entity=vm, key=field['key'], value=field['value'])

            # Set result_fields for the return value.
            self.result_fields[field['name']] = field['value']

        return {'changed': self.changed, 'failed': False, 'custom_attributes': self.result_fields}

    def check_exists(self, vm, user_fields):
        """Check the existing custom attributes and values.

        In the function, the below processing is executed.

        Gather the existing custom attributes from the virtual machine and make update_custom_attributes for updating
        if it has differences between the existing configuration and the user_fields.

        And set diff key for checking between before and after configuration to self.diff_config.

        Args:
            vm (vim.VirtualMachine): The managed object of a virtual machine.
            user_fields (list): list of the specified custom attributes by user.
        """
        # Gather the available existing custom attributes based on user_fields
        existing_custom_attributes = []
        for k, n in [(x.key, x.name) for x in self.custom_field_mgr for v in user_fields if x.name == v['name']]:
            existing_custom_attributes.append({
                "key": k,
                "name": n
            })

        # Gather the values of set the custom attribute.
        for e in existing_custom_attributes:
            for v in vm.customValue:
                if e['key'] == v.key:
                    e['value'] = v.value

            # When add custom attribute as a new one, it has not the value key.
            # Add the value key to avoid unintended behavior in the difference check.
            if 'value' not in e:
                e['value'] = ''

        # Select the custom attribute and value to update the configuration.
        _user_fields_for_diff = []
        for v in user_fields:
            for e in existing_custom_attributes:
                if v['name'] == e['name'] and v['value'] != e['value']:
                    self.update_custom_attributes.append({
                        "name": v['name'],
                        "value": v['value'],
                        "key": e['key']
                    })

                if v['name'] == e['name']:
                    _user_fields_for_diff.append({
                        "name": v['name'],
                        "value": v['value']
                    })
            # Add the custom attribute as a new one if the state is present and existing_custom_attribute has not the custom attribute name.
            if v['name'] not in [x['name'] for x in existing_custom_attributes] and self.params['state'] == "present":
                self.update_custom_attributes.append(v)
                _user_fields_for_diff.append({
                    "name": v['name'],
                    "value": v['value']
                })

        # If the custom attribute exists to update, the changed is set to True.
        if self.update_custom_attributes:
            self.changed = True

        # Add custom_attributes key for the difference between before and after configuration to check.
        self.diff_config['before']['custom_attributes'] = sorted(
            [x for x in existing_custom_attributes if x.pop('key', None)], key=lambda k: k['name']
        )
        self.diff_config['after']['custom_attributes'] = sorted(_user_fields_for_diff, key=lambda k: k['name'])


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str'),
        name=dict(type='str'),
        folder=dict(type='str'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
        state=dict(type='str', default='present',
                   choices=['absent', 'present']),
        attributes=dict(
            type='list',
            default=[],
            elements='dict',
            options=dict(
                name=dict(type='str', required=True),
                value=dict(type='str', default=''),
            )
        ),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['name', 'uuid', 'moid']
        ],
    )

    if module.params.get('folder'):
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    pyv = VmAttributeManager(module)
    results = {'changed': False, 'failed': False, 'instance': dict()}

    # Check if the virtual machine exists before continuing
    vm = pyv.get_vm()

    if vm:
        # virtual machine already exists
        if module.params['state'] == "present":
            results = pyv.set_custom_field(vm, module.params['attributes'])
        elif module.params['state'] == "absent":
            results = pyv.remove_custom_field(vm, module.params['attributes'])
        module.exit_json(**results)
    else:
        # virtual machine does not exists
        vm_id = (module.params.get('name') or module.params.get('uuid') or module.params.get('moid'))
        module.fail_json(msg="Unable to manage custom attributes for non-existing"
                             " virtual machine %s" % vm_id)


if __name__ == '__main__':
    main()
