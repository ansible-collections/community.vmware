#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_find
short_description: Find the folder path(s) for a virtual machine by name or UUID
description:
    - Find the folder path(s) for a virtual machine by name or UUID
author:
    - Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>
options:
   name:
     description:
     - Name of the VM to work with.
     - This is required if O(uuid) parameter is not supplied.
     type: str
   uuid:
     description:
     - UUID of the instance to manage if known, this is VMware's BIOS UUID by default.
     - This is required if O(name) parameter is not supplied.
     type: str
   use_instance_uuid:
     description:
     - Whether to use the VMware instance UUID rather than the BIOS UUID.
     default: false
     type: bool
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Find Guest's Folder using name
  community.vmware.vmware_guest_find:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: testvm
  delegate_to: localhost
  register: vm_folder

- name: Find Guest's Folder using UUID
  community.vmware.vmware_guest_find:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    uuid: 38c4c89c-b3d7-4ae6-ae4e-43c5118eae49
  delegate_to: localhost
  register: vm_folder
'''

RETURN = r'''
folders:
    description: List of folders for user specified virtual machine
    returned: on success
    type: list
    sample: [
        '/DC0/vm',
    ]
'''


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, find_vm_by_id
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec

try:
    from pyVmomi import vim
except ImportError:
    pass


class PyVmomiHelper(PyVmomi):
    def __init__(self, module):
        super(PyVmomiHelper, self).__init__(module)
        self.name = self.params['name']
        self.uuid = self.params['uuid']
        self.use_instance_uuid = self.params['use_instance_uuid']

    def getvm_folder_paths(self):
        results = []
        vms = []

        if self.uuid:
            if self.use_instance_uuid:
                vm_obj = find_vm_by_id(self.content, vm_id=self.uuid, vm_id_type="instance_uuid")
            else:
                vm_obj = find_vm_by_id(self.content, vm_id=self.uuid, vm_id_type="uuid")
            if vm_obj is None:
                self.module.fail_json(msg="Failed to find the virtual machine with UUID : %s" % self.uuid)
            vms = [vm_obj]

        elif self.name:
            objects = self.get_managed_objects_properties(vim_type=vim.VirtualMachine, properties=['name'])
            for temp_vm_object in objects:
                if temp_vm_object.obj.name == self.name:
                    vms.append(temp_vm_object.obj)

        for vm in vms:
            folder_path = self.get_vm_path(self.content, vm)
            results.append(folder_path)

        return results


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        uuid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           required_one_of=[['name', 'uuid']],
                           mutually_exclusive=[['name', 'uuid']],
                           )

    pyv = PyVmomiHelper(module)
    # Check if the VM exists before continuing
    folders = pyv.getvm_folder_paths()

    # VM already exists
    if folders:
        try:
            module.exit_json(folders=folders)
        except Exception as exc:
            module.fail_json(msg="Folder enumeration failed with exception %s" % to_native(exc))
    else:
        module.fail_json(msg="Unable to find folders for virtual machine %s" % (
            module.params.get('name')
            or module.params.get('uuid')))


if __name__ == '__main__':
    main()
