#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright, (c) 2022, Mario Lenz <m@riolenz.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# flake8: noqa: E402
#
"""Module: vmware_custom_attribute_manager

This module manages custom attributes on vCenter/vSphere objects.
It supports creating/updating custom attributes (state=present) and clearing them (state=absent).
"""

from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    find_obj,
    vmware_argument_spec,
)
from pyVmomi import vim, vmodl

if hasattr(vmodl.fault, "MethodFault"):
    MethodFault = vmodl.fault.MethodFault  # type: ignore
else:

    class _MethodFault(Exception):
        """Fallback exception for vmodl.fault.MethodFault when it is not available."""

    MethodFault = _MethodFault

DOCUMENTATION = r"""
---
module: vmware_custom_attribute_manager
version_added: "3.2.0"
short_description: "Manage custom attributes on VMware vSphere objects"
description:
  - "This module allows you to add, update, or clear custom attributes on VMware vSphere objects. When state is set to C(present), custom attributes are created or updated. When state is set to C(absent), custom attributes are cleared. The provided value is ignored in that case."
author:
  - "Mario Lenz (@mariolenz)"
  - "Simon Bärlocher (@sbaerlocher)"
  - "whatwedo GmbH (@whatwedo)"
options:
  custom_attributes:
    description:
      - "A list of dictionaries, each containing the name and value of a custom attribute to be managed. When state is C(absent), the value provided is ignored."
    required: true
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - "Name of the custom attribute."
        type: str
        required: true
      value:
        description:
          - "Value to assign to the custom attribute."
        type: str
        default: ""
  object_name:
    description:
      - "Name of the vSphere object to manage."
    required: true
    type: str
  object_type:
    description:
      - "Type of the vSphere object to which the custom attribute is associated."
    required: true
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
      - Network
      - VirtualApp
  state:
    description:
      - If set to V(present), the custom attribute is set to the given value.
      - If set to V(absent), the custom attribute is cleared. The given value is ignored in this case.
    default: 'present'
    choices: ['present', 'absent']
    type: str
extends_documentation_fragment:
- vmware.vmware.base_options

EXAMPLES = r"""

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
"""

RETURN = r"""
changed:
  description: "Indicates if any change was made."
  type: bool
  returned: always
msg:
  description: "A summary message."
  type: str
  returned: always
details:
  description: "List of messages for each custom attribute."
  type: list
  returned: always
  sample: [
      {"name": "Environment", "msg": "Custom field 'Environment' set to 'Production'."},
      {"name": "Owner", "msg": "Custom field 'Owner' is already set to 'Ops'."}
  ]
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, find_obj
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec

    def __init__(self, module):
        super().__init__(module)
        self.module = module
        custom_attributes = module.params["custom_attributes"]
        self.custom_attributes = custom_attributes
        self.object_name = module.params["object_name"]
        obj_type = module.params["object_type"]
        if not isinstance(self.object_name, str) or not self.object_name.strip():
            self.module.fail_json(msg="'object_name' must be a non-empty string")
        if not isinstance(obj_type, str) or not obj_type.strip():
            self.module.fail_json(msg="'object_type' must be a non-empty string")
        if not isinstance(custom_attributes, list) or not custom_attributes:
            self.module.fail_json(msg="'attributes' must be a non-empty list")
        object_types_map = {
            "Cluster": vim.ClusterComputeResource,
            "Datacenter": vim.Datacenter,
            "Datastore": vim.Datastore,
            "DistributedVirtualPortgroup": vim.dvs.DistributedVirtualPortgroup,
            "DistributedVirtualSwitch": vim.DistributedVirtualSwitch,
            "Folder": vim.Folder,
            "HostSystem": vim.HostSystem,
            "ResourcePool": vim.ResourcePool,
            "VirtualMachine": vim.VirtualMachine,
            "Network": vim.Network,
            "VirtualApp": vim.VirtualApp,
        }
        if obj_type not in object_types_map:
            self.module.fail_json(msg=f"Unsupported object_type '{obj_type}'.")
        self.object_type = object_types_map[obj_type]
        self.managed_object = find_obj(
            self.content, [self.object_type], self.object_name
        )
        if self.managed_object is None:
            self.module.fail_json(
                msg=f"Object '{self.object_name}' of type '{obj_type}' not found."
            )
        self.custom_field_cache = {}
        custom_fields_manager = self.content.customFieldsManager
        if hasattr(custom_fields_manager, "field"):
            for field in custom_fields_manager.field:
                self.custom_field_cache[field.name] = field.key
        self.custom_value_cache = {}
        for custom_value in getattr(self.managed_object, "customValue", []):
            self.custom_value_cache[custom_value.key] = custom_value.value

    def _find_current_custom_field_value(self, field_key):
        return self.custom_value_cache.get(field_key)

    def _process_custom_attribute(self, attribute_name, attribute_value, clear=False):
        custom_fields_manager = self.content.customFieldsManager
        field_key = self.custom_field_cache.get(attribute_name)
        if field_key is None:
            if clear:
                return (
                    False,
                    f"Custom field '{attribute_name}' does not exist, nothing to clear.",
                )
            try:
                field_definition = custom_fields_manager.AddCustomFieldDef(
                    name=attribute_name,
                    moType=type(self.managed_object),
                    fieldDefPolicy=None,
                    fieldPolicy=None,
                )
                field_key = field_definition.key
                self.custom_field_cache[attribute_name] = field_key
            except MethodFault as error:
                self.module.fail_json(
                    msg=f"Failed to create custom field '{attribute_name}': {to_native(error)}"
                )
        current_value = self._find_current_custom_field_value(field_key)
        if clear:
            if current_value in [None, ""]:
                result = (False, f"Custom field '{attribute_name}' is already empty.")
            elif self.module.check_mode:
                result = (True, f"Custom field '{attribute_name}' would be cleared.")
            else:
                try:
                    custom_fields_manager.SetField(
                        entity=self.managed_object, key=field_key, value=""
                    )
                    self.custom_value_cache[field_key] = ""
                    result = (
                        True,
                        f"Custom field '{attribute_name}' has been cleared.",
                    )
                except MethodFault as error:
                    self.module.fail_json(
                        msg=f"Failed to clear custom field '{attribute_name}': {to_native(error)}"
                    )
        else:
            if current_value == attribute_value:
                result = (
                    False,
                    f"Custom field '{attribute_name}' already has value '{attribute_value}'.",
                )
            elif self.module.check_mode:
                result = (
                    True,
                    f"Custom field '{attribute_name}' would be set to '{attribute_value}'.",
                )
            else:
                try:
                    custom_fields_manager.SetField(
                        entity=self.managed_object, key=field_key, value=attribute_value
                    )
                    self.custom_value_cache[field_key] = attribute_value
                    result = (
                        True,
                        f"Custom field '{attribute_name}' set to '{attribute_value}'.",
                    )
                except MethodFault as error:
                    self.module.fail_json(
                        msg=f"Failed to set custom field '{attribute_name}': {to_native(error)}"
                    )
        return result

    def process_custom_attributes(self):
        """Processes all provided custom attributes and returns change status, summary, and details."""
        overall_changed = False
        detailed_messages = []
        state = self.module.params.get("state", "present")
        clear = state == "absent"
        for attribute in self.custom_attributes:
            attribute_name = attribute.get("name")
            attribute_value = attribute.get("value", "")
            if not isinstance(attribute_name, str) or not attribute_name.strip():
                self.module.fail_json(
                    msg="Each attribute must include a non-empty 'name' field."
                )
            change_occurred, message = self._process_custom_attribute(
                attribute_name, attribute_value, clear=clear
            )
            overall_changed = overall_changed or change_occurred
            detailed_messages.append({"name": attribute_name, "msg": message})
        summary_message = f"Processed {len(self.custom_attributes)} attribute(s)."
        return overall_changed, summary_message, detailed_messages

    def update(self):
        """Alias for process_custom_attributes to provide an additional public method."""
        return self.process_custom_attributes()


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        {
            "object_name": {"type": "str", "required": True},
            "object_type": {
                "type": "str",
                "default": "VirtualMachine",
                "choices": [
                    "Cluster",
                    "Datacenter",
                    "Datastore",
                    "DistributedVirtualPortgroup",
                    "DistributedVirtualSwitch",
                    "Folder",
                    "HostSystem",
                    "ResourcePool",
                    "VirtualMachine",
                    "Network",
                    "VirtualApp",
                ],
            },
            "custom_attributes": {"type": "list", "required": True, "elements": "dict"},
            "state": {
                "type": "str",
                "default": "present",
                "choices": ["present", "absent"],
            },
        }
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    manager = CustomAttributeManager(module)
    try:
        changed, summary_message, details = manager.process_custom_attributes()
    except (ValueError, KeyError, MethodFault, TypeError) as error:
        module.fail_json(msg=f"An unexpected error occurred: {to_native(error)}")
    module.exit_json(changed=changed, msg=summary_message, details=details)


if __name__ == "__main__":
    main()
