#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Module for managing VMware custom attribute definitions.
"""

from types import ModuleType
from typing import Any, Dict, Optional

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec

try:
    from pyVmomi import vim as _vim  # type: ignore
except ImportError:
    _vim = None  # type: ignore

vim: Optional[ModuleType] = _vim

DOCUMENTATION = r"""
---
module: vmware_custom_attribute
version_added: "3.2.0"
short_description: Manage custom attribute definitions for vSphere objects.
description:
  - This module adds or removes custom attribute definitions for various vSphere objects.
  - It supports all object types provided by VMware (e.g. Cluster, Datacenter, VirtualMachine, etc.).
author:
  - Mario Lenz (@mariolenz)
  - Simon Bärlocher (@sbaerlocher)
  - whatwedo GmbH (@whatwedo)
options:
  custom_attribute:
    description:
      - Name of the custom attribute.
    required: true
    type: str
  object_type:
    description:
      - Type of the object the custom attribute is associated with.
      - All supported types are listed here.
    required: true
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
      - Network
      - VirtualApp
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
  - vmware.vmware.base_options
"""

EXAMPLES = r"""
- name: Add VM Custom Attribute Definition
  community.vmware.vmware_custom_attribute:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: present
    object_type: VirtualMachine
    custom_attribute: custom_attr_def_1
  delegate_to: localhost
  register: definitions

- name: Remove VM Custom Attribute Definition
  community.vmware.vmware_custom_attribute:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: absent
    object_type: VirtualMachine
    custom_attribute: custom_attr_def_1
  delegate_to: localhost
  register: definitions

- name: Add Network Custom Attribute Definition
  community.vmware.vmware_custom_attribute:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    state: present
    object_type: Network
    custom_attribute: custom_attr_network
  delegate_to: localhost
  register: definitions
"""

RETURN = r"""
changed:
    description: Indicates if any change was made.
    type: bool
failed:
    description: Indicates if the operation failed.
    type: bool
"""


def get_object_type_mapping() -> Dict[str, Any]:
    """Returns a mapping from object type names to the corresponding pyVmomi classes."""
    return {
        "Cluster": vim.ClusterComputeResource if vim else None,
        "Datacenter": vim.Datacenter if vim else None,
        "Datastore": vim.Datastore if vim else None,
        "DistributedVirtualPortgroup": (
            vim.dvs.DistributedVirtualPortgroup if vim else None
        ),
        "DistributedVirtualSwitch": vim.DistributedVirtualSwitch if vim else None,
        "Folder": vim.Folder if vim else None,
        "Global": None,
        "HostSystem": vim.HostSystem if vim else None,
        "ResourcePool": vim.ResourcePool if vim else None,
        "VirtualMachine": vim.VirtualMachine if vim else None,
        "Network": vim.Network if vim else None,
        "VirtualApp": getattr(vim, "VirtualApp", None) if vim else None,
    }


class CustomAttributeManager(PyVmomi):
    """Class responsible for managing custom attribute definitions."""

    def __init__(self, module: AnsibleModule) -> None:
        super().__init__(module)
        self.module = module

        if not isinstance(module.params, dict):
            self.module.fail_json(msg="module.params is not a dict")
        self.parameters: Dict[str, Any] = module.params

        custom_attribute_value = self.parameters.get("custom_attribute", "")
        if (
            not isinstance(custom_attribute_value, str)
            or not custom_attribute_value.strip()
        ):
            self.module.fail_json(msg="'custom_attribute' must be a non-empty string")

        if vim is None:
            self.module.fail_json(msg="pyVmomi is required for this module")

        if not self.is_vcenter():
            self.module.fail_json(msg="A connection to a vCenter server is required!")

        object_type_value = self.parameters.get("object_type", "")
        if not isinstance(object_type_value, str) or not object_type_value.strip():
            self.module.fail_json(msg="'object_type' must be a non-empty string")

        object_type_mapping = get_object_type_mapping()
        self.object_type = object_type_mapping.get(object_type_value)
        if self.object_type is None and object_type_value != "Global":
            self.module.fail_json(msg=f"Unsupported object type: {object_type_value}")

        try:
            self.custom_field_definitions = self.content.customFieldsManager.field
        except AttributeError:
            self.module.fail_json(
                msg="Failed to access customFieldsManager in vCenter content"
            )

    def find_custom_attribute_definition(
        self, custom_attribute_name: str
    ) -> Optional[Any]:
        """Searches for a custom attribute definition and returns it if found."""
        for custom_field_definition in self.custom_field_definitions:
            if (
                custom_field_definition.name == custom_attribute_name
                and custom_field_definition.managedObjectType == self.object_type
            ):
                return custom_field_definition
        return None

    def remove_custom_definition(self, custom_attribute_name: str) -> Dict[str, Any]:
        """Removes the custom attribute definition if it exists."""
        state_changed = False
        custom_field_definition = self.find_custom_attribute_definition(
            custom_attribute_name
        )
        if custom_field_definition:
            state_changed = True
            if not self.module.check_mode:
                self.content.customFieldsManager.RemoveCustomFieldDef(
                    key=custom_field_definition.key
                )
        return {"changed": state_changed, "failed": False}

    def add_custom_definition(self, custom_attribute_name: str) -> Dict[str, Any]:
        """Adds the custom attribute definition if it does not exist."""
        state_changed = False
        if not self.find_custom_attribute_definition(custom_attribute_name):
            state_changed = True
            if not self.module.check_mode:
                self.content.customFieldsManager.AddFieldDefinition(
                    name=custom_attribute_name, moType=self.object_type
                )
        return {"changed": state_changed, "failed": False}


def manage_custom_attribute_definition(module: AnsibleModule) -> None:
    """Determines whether to add or remove the custom attribute definition based on the 'state' parameter."""
    if not isinstance(module.params, dict):
        module.fail_json(msg="module.params is not a dict")
    parameters: Dict[str, Any] = module.params
    custom_attribute_name = parameters["custom_attribute"]
    desired_state = parameters["state"]
    custom_attribute_manager = CustomAttributeManager(module)
    if desired_state == "present":
        result = custom_attribute_manager.add_custom_definition(custom_attribute_name)
    else:
        result = custom_attribute_manager.remove_custom_definition(
            custom_attribute_name
        )
    module.exit_json(**result)


def main() -> None:
    """Main entry point for the module."""
    argument_specification = base_argument_spec()
    argument_specification.update(
        custom_attribute={"type": "str", "no_log": False, "required": True},
        object_type={
            "type": "str",
            "required": True,
            "choices": [
                "Cluster",
                "Datacenter",
                "Datastore",
                "DistributedVirtualPortgroup",
                "DistributedVirtualSwitch",
                "Folder",
                "Global",
                "HostSystem",
                "ResourcePool",
                "VirtualMachine",
                "Network",
                "VirtualApp",
            ],
        },
        state={"type": "str", "default": "present", "choices": ["absent", "present"]},
    )
    module = AnsibleModule(
        argument_spec=argument_specification,
        supports_check_mode=True,
    )

    try:
        manage_custom_attribute_definition(module)
    except ValueError as error:
        module.fail_json(msg=f"ValueError: {error}")
    except KeyError as error:
        module.fail_json(msg=f"KeyError: {error}")


if __name__ == "__main__":
    main()
