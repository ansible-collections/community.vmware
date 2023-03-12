#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: vmware_object_custom_attributes_info
short_description: Gather custom attributes of an object
author:
  - sky-joker (@sky-joker)
description:
  - This module can be gathered custom attributes of an object.
notes:
  - Supports C(check_mode).
options:
  object_type:
    description:
      - Type of an object to work with.
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
    required: true
  object_name:
    description:
      - Name of the object to work with.
    type: str
    aliases:
      - name
  moid:
    description:
      - Managed Object ID of the instance to get if known, this is a unique identifier only within a single vCenter instance.
      - This is required if C(object_name) is not supplied.
    type: str
extends_documentation_fragment:
  - community.vmware.vmware.documentation
"""

EXAMPLES = r"""
- name: Gather custom attributes of a virtual machine
  community.vmware.vmware_object_custom_attributes_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    object_type: VirtualMachine
    object_name: "{{ object_name }}"
  register: vm_attributes

- name: Gather custom attributes of a virtual machine with moid
  community.vmware.vmware_object_custom_attributes_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    object_type: VirtualMachine
    moid: "{{ moid }}"
  register: vm_attributes
"""

RETURN = r"""
custom_attributes:
  description: list of custom attributes of an object.
  returned: always
  type: list
  sample: >-
    [
        {
            "attribute": "example01",
            "key": 132,
            "type": "VirtualMachine",
            "value": "10"
        },
        {
            "attribute": "example02",
            "key": 131,
            "type": "VirtualMachine",
            "value": "20"
        },
        {
            "attribute": "example03",
            "key": 130,
            "type": "VirtualMachine",
            "value": null
        }
    ]
"""

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec, find_obj


class VmwareCustomAttributesInfo(PyVmomi):
    def __init__(self, module):
        super(VmwareCustomAttributesInfo, self).__init__(module)

        if not self.is_vcenter():
            self.module.fail_json(msg="You have to connect to a vCenter server!")

        self.object_type = self.params['object_type']
        self.object_name = self.params['object_name']
        self.moid = self.params['moid']

        self.valid_object_types = {
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

    def execute(self):
        result = {'changed': False}

        if self.object_name:
            obj = find_obj(self.content, [self.valid_object_types[self.object_type]], self.object_name)
        elif self.moid:
            obj = self.find_obj_by_moid(self.object_type, self.moid)
        if not obj:
            self.module.fail_json(msg="can't find the object: %s" % self.object_name if self.object_name else self.moid)

        custom_attributes = []
        available_fields = {}
        for available_custom_attribute in obj.availableField:
            available_fields.update({
                available_custom_attribute.key: {
                    'name': available_custom_attribute.name,
                    'type': available_custom_attribute.managedObjectType
                }
            })

        custom_values = {}
        for custom_value in obj.customValue:
            custom_values.update({
                custom_value.key: custom_value.value
            })

        for key, value in available_fields.items():
            attribute_result = {
                'attribute': value['name'],
                'type': self.to_json(value['type']).replace('vim.', '') if value['type'] is not None else 'Global',
                'key': key,
                'value': None
            }

            if key in custom_values:
                attribute_result['value'] = custom_values[key]

            custom_attributes.append(attribute_result)

        result['custom_attributes'] = custom_attributes
        self.module.exit_json(**result)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
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
        object_name=dict(type='str', aliases=['name']),
        moid=dict(type='str')
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           mutually_exclusive=[
                               ['object_name', 'moid']
                           ],
                           required_one_of=[
                               ['object_name', 'moid']
                           ],
                           supports_check_mode=True)

    vmware_custom_attributes_info = VmwareCustomAttributesInfo(module)
    vmware_custom_attributes_info.execute()


if __name__ == "__main__":
    main()
