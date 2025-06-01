#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2025, Simon Bärlocher (@sbaerlocher) <s.baerlocher@sbaerlocher.ch>
# Copyright: (c) 2025, whatwedo GmbH (https://whatwedo.ch)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

"""
This module implements the Ansible module 'vcenter_object_move', which moves a vCenter
inventory object (e.g. a VirtualMachine, Host, Datastore, Network, or Folder) to a specified
destination folder within the appropriate inventory branch.
"""

from typing import cast

from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    find_datacenter_by_name,
    vmware_argument_spec,
    wait_for_task,
)
from pyVmomi import vim

DOCUMENTATION = r"""
---
module: vcenter_object_move
short_description: Moves an inventory object to a specified destination folder in vCenter
description:
  - Moves an inventory object (e.g. a VirtualMachine, Host, Datastore, Network or Folder) to a specified destination folder within the appropriate inventory branch.
  - The destination folder is specified as a slash-separated path relative to the datacenter's base folder.
  - Supported object types:
      - C(vm): Virtual Machines, vApps and Folders under the VM folder.
      - C(host): Hosts and Folders under the Host folder.
      - C(datastore): Datastores and Folders under the Datastore folder.
      - C(network): Networks and Folders under the Network folder.
  - If the object is already located in the target folder, no action is taken (idempotence).
author:
  - Simon Bärlocher (@sbaerlocher)
  - whatwedo GmbH (@whatwedo)
options:
  datacenter:
    description:
      - Name of the datacenter.
    required: true
    aliases: [ datacenter_name ]
    type: str
  object_name:
    description:
      - Name of the inventory object to move.
    required: true
    type: str
  object_type:
    description:
      - Inventory branch where the object resides.
      - Determines the base folder for both object lookup and destination folder traversal.
    required: false
    type: str
    default: vm
    choices: [ vm, host, datastore, network ]
  destination_folder:
    description:
      - Destination folder path relative to the base folder of the chosen object_type.
      - Example: C(NewFolder) or C(folder1/subfolder2)
    required: true
    type: str
  state:
    description:
      - Desired state.
      - Only C(present) is supported.
    required: false
    type: str
    default: present
    choices: [ present ]
extends_documentation_fragment:
  - community.vmware.vmware.documentation
"""

EXAMPLES = r"""
- name: Move a VM to a new folder
  vcenter_object_move:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "DC0"
    object_name: "MyVM"
    object_type: "vm"
    destination_folder: "NewFolder/SubFolder"
  delegate_to: localhost

- name: Move a Host to a different folder
  vcenter_object_move:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "DC0"
    object_name: "esxi-01"
    object_type: "host"
    destination_folder: "Maintenance"
  delegate_to: localhost
"""

RETURN = r"""
changed:
  description: Indicates if the object was moved.
  type: bool
  returned: always
msg:
  description: A message describing the result.
  type: str
  returned: always
"""

BASE_FOLDER_MAPPING = {
    "vm": {
        "base_folder_attr": "vmFolder",
        "search_types": [vim.VirtualMachine, vim.Folder, vim.VirtualApp],
    },
    "host": {
        "base_folder_attr": "hostFolder",
        "search_types": [vim.HostSystem, vim.Folder],
    },
    "datastore": {
        "base_folder_attr": "datastoreFolder",
        "search_types": [vim.Datastore, vim.Folder],
    },
    "network": {
        "base_folder_attr": "networkFolder",
        "search_types": [vim.Network, vim.Folder],
    },
}


# pylint: disable=too-many-instance-attributes
class ObjectMover(PyVmomi):
    """
    Helper class to move vCenter inventory objects to a specified destination folder.
    """

    def __init__(self, module):
        """
        Initialize the ObjectMover, validate parameters,
        and check for the existence of the datacenter,
        the inventory object, and the destination folder.

        :param module: The AnsibleModule instance containing parameters.
        """
        super().__init__(module)
        self.module = module
        self._vim = vim
        self.datacenter_name = module.params["datacenter"]
        self.inventory_object_name = module.params["object_name"]
        self.inventory_object_type = module.params.get("object_type", "vm")
        self.destination_folder_path = module.params["destination_folder"]
        self.desired_state = module.params.get("state", "present")
        self.vcenter_datacenter_object = find_datacenter_by_name(
            self.content, datacenter_name=self.datacenter_name
        )
        if not self.vcenter_datacenter_object:
            self.module.fail_json(msg=f"Datacenter '{self.datacenter_name}' not found.")
        if self.inventory_object_type not in BASE_FOLDER_MAPPING:
            self.module.fail_json(
                msg=f"Unsupported object_type '{self.inventory_object_type}'."
            )
        mapping = BASE_FOLDER_MAPPING[self.inventory_object_type]
        self.inventory_base_folder = getattr(
            self.vcenter_datacenter_object, mapping["base_folder_attr"]
        )
        self.inventory_search_types = mapping["search_types"]
        self.inventory_object = self._find_object_by_name(
            self.inventory_object_name,
            self.inventory_search_types,
            self.inventory_base_folder,
        )
        if not self.inventory_object:
            self.module.fail_json(
                msg=(
                    f"Object '{self.inventory_object_name}' not found in datacenter "
                    f"'{self.datacenter_name}' under branch "
                    f"'{self.inventory_object_type}'."
                )
            )
        self.destination_folder_object = self._find_destination_folder(
            self.destination_folder_path
        )
        if not self.destination_folder_object:
            self.module.fail_json(
                msg=(
                    f"Destination folder '{self.destination_folder_path}' not found under "
                    f"branch '{self.inventory_object_type}' in datacenter "
                    f"'{self.datacenter_name}'."
                )
            )

    def _find_object_by_name(self, name, vim_types, base_folder):
        """
        Search for an inventory object by its name within the given base folder.

        :param name: Name of the inventory object.
        :param vim_types: List of vSphere types to filter the search.
        :param base_folder: The folder where the search should be performed.
        :return: The inventory object if found, else None.
        """
        container_view = self.content.viewManager.CreateContainerView(
            base_folder, vim_types, True
        )
        try:
            for inventory_object in container_view.view:
                if inventory_object.name == name:
                    return inventory_object
            return None
        finally:
            container_view.Destroy()

    def _find_destination_folder(self, path):
        """
        Traverse the base folder to locate the destination folder specified by the path.

        :param path: Slash-separated path to the destination folder.
        :return: The destination folder object if found, else None.
        """
        folder_parts = [part for part in path.strip("/").split("/") if part]
        current_folder = self.inventory_base_folder
        for folder_name in folder_parts:
            child_entities = getattr(current_folder, "childEntity", [])
            if child_entities is None:
                child_entities = []
            child_folders = {
                child.name: child
                for child in child_entities
                if isinstance(child, vim.Folder)
            }
            if folder_name in child_folders:
                current_folder = child_folders[folder_name]
            else:
                return None
        return current_folder

    def move_inventory_object(self):
        """
        Move the inventory object to the destination folder if it is not already there.

        :return: A tuple with a boolean indicating if a change occurred and a message.
        """
        parent_obj = getattr(self.inventory_object, "parent", None)
        if parent_obj and getattr(parent_obj, "_moId", None) == getattr(
            self.destination_folder_object, "_moId", None
        ):
            return (
                False,
                f"Object '{self.inventory_object_name}' is already in the destination folder.",
            )
        if self.module.check_mode:
            return (
                True,
                f"Object '{self.inventory_object_name}' would be moved to folder "
                f"'{self.destination_folder_path}'.",
            )
        try:
            if not isinstance(self.destination_folder_object, vim.Folder):
                self.module.fail_json(
                    msg="Destination folder object is not an instance of vim.Folder."
                )
                return (False, None)
            destination_folder: vim.Folder = cast(
                vim.Folder, self.destination_folder_object
            )
            move_task = destination_folder.MoveIntoFolder_Task([self.inventory_object])
            wait_for_task(move_task)
            return (
                True,
                f"Object '{self.inventory_object_name}' was successfully moved to folder "
                f"'{self.destination_folder_path}'.",
            )
        except Exception as error:  # pylint: disable=broad-exception-caught
            self.module.fail_json(
                msg=(
                    f"Failed to move object '{self.inventory_object_name}': "
                    f"{to_native(error)}"
                )
            )
            return (False, None)

    @property
    def vim(self):
        """
        Property to access the vim module.

        :return: The vim module.
        """
        return self._vim


def main():
    """
    Main entry point for the module. Validates parameters,
    performs the move operation, and exits with the result.
    """
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        {
            "datacenter": {
                "type": "str",
                "required": True,
                "aliases": ["datacenter_name"],
            },
            "object_name": {"type": "str", "required": True},
            "object_type": {
                "type": "str",
                "default": "vm",
                "choices": ["vm", "host", "datastore", "network"],
            },
            "destination_folder": {"type": "str", "required": True},
            "state": {"type": "str", "default": "present", "choices": ["present"]},
        }
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    object_mover = ObjectMover(module)
    result = object_mover.move_inventory_object()
    if result is None:
        module.exit_json(changed=False, msg="Unexpected error: No result returned.")
    changed, result_message = result
    module.exit_json(changed=changed, msg=result_message)


if __name__ == "__main__":
    main()
