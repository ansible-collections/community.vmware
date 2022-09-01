#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Ansible Project
# Copyright: (c) 2019, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_object_rename
short_description: Renames VMware objects
description:
- This module can be used to rename VMware objects.
- All variables and VMware object names are case sensitive.
- Renaming Host and Network is not supported by VMware APIs.
author:
- Abhijeet Kasurde (@Akasurde)
requirements:
- vSphere Automation SDK
options:
    object_type:
      description:
      - Type of object to work with.
      - Valid options are Cluster, ClusterComputeResource, Datacenter, Datastore, Folder, ResourcePool, VM or VirtualMachine.
      required: True
      type: str
      choices:
        - 'ClusterComputeResource'
        - 'Cluster'
        - 'Datacenter'
        - 'Datastore'
        - 'Folder'
        - 'Network'
        - 'ResourcePool'
        - 'VM'
        - 'VirtualMachine'
    object_name:
      description:
      - Name of the object to work with.
      - Mutually exclusive with C(object_moid).
      type: str
    object_moid:
      description:
      - Managed object id of the VMware object to work with.
      - Mutually exclusive with C(object_name).
      type: str
    new_name:
      description:
      - New name for VMware object.
      required: True
      aliases: ['object_new_name']
      type: str
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation
'''

EXAMPLES = r'''
- name: Rename a virtual machine
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: Fedora_31
    object_name: Fedora_VM
    object_type: VirtualMachine
  delegate_to: localhost

- name: Rename a virtual machine using moid
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: Fedora_31
    object_moid: vm-14
    object_type: VirtualMachine
  delegate_to: localhost

- name: Rename a datacenter
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: Asia_Datacenter
    object_name: dc1
    object_type: Datacenter
  delegate_to: localhost

- name: Rename a folder with moid
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: backup
    object_moid: group-v46
    object_type: Folder
  delegate_to: localhost

- name: Rename a cluster with moid
  community.vmware.vmware_object_rename:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    new_name: CCR_1
    object_moid: domain-c33
    object_type: Cluster
  delegate_to: localhost
'''

RETURN = r'''
rename_status:
    description: metadata about VMware object rename operation
    returned: on success
    type: dict
    sample: {
        "current_name": "Fedora_31",
        "desired_name": "Fedora_31",
        "previous_name": "Fedora_VM",
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, wait_for_task
try:
    from pyVmomi import vim
except ImportError:
    pass


class VmwareObjectRename(VmwareRestClient):
    def __init__(self, module):
        """
        Constructor
        """
        super(VmwareObjectRename, self).__init__(module)
        self.pyv = PyVmomi(module=module)
        self.soap_stub = self.pyv.si._stub

        self.object_type = self.params.get('object_type')
        self.object_name = self.params.get('object_name')
        self.object_new_name = self.params.get('new_name')
        self.object_moid = self.params.get('object_moid')

        self.managed_object = None

    def ensure_state(self):
        """
        Manage the internal state of object rename operation

        """
        results = dict(
            changed=False,
            rename_status=dict(),
        )

        results['rename_status']['desired_name'] = self.object_new_name
        changed = False

        vcenter_obj = self.api_client.vcenter
        available_object_types = [i for i in dir(vcenter_obj) if hasattr(getattr(vcenter_obj, i), 'list') and i != 'Host']
        available_object_types += ['ClusterComputeResource', 'VirtualMachine']

        if self.object_type not in available_object_types:
            self.module.fail_json(msg="Object type can be any"
                                  " one of [%s]" % ", ".join(available_object_types))

        valid_object_types = {
            'ClusterComputeResource': [
                vcenter_obj.Cluster,
                vim.ClusterComputeResource,
                'cluster',
            ],
            'Cluster': [
                vcenter_obj.Cluster,
                vim.ClusterComputeResource,
                'cluster',
            ],
            'Datacenter': [
                vcenter_obj.Datacenter,
                vim.Datacenter,
                'datacenter',
            ],
            'Datastore': [
                vcenter_obj.Datastore,
                vim.Datastore,
                'datastore',
            ],
            'Folder': [
                vcenter_obj.Folder,
                vim.Folder,
                'folder',
            ],
            'Network': [
                vcenter_obj.Network,
                vim.ClusterComputeResource,
                'network',
            ],
            'ResourcePool': [
                vcenter_obj.ResourcePool,
                vim.ResourcePool,
                'resource_pool'
            ],
            'VM': [
                vcenter_obj.VM,
                vim.VirtualMachine,
                'vm',
            ],
            'VirtualMachine': [
                vcenter_obj.VM,
                vim.VirtualMachine,
                'vm',
            ],
        }

        target_object = valid_object_types[self.object_type][0]

        # Generate filter spec.
        # List method will be used in getting objects.
        # List method can get only up to a max of 1,000 objects.
        # If VCSA has than 1,000 objects with the specified object_type, the following error will occur.
        # Error: Too many virtual machines. Add more filter criteria to reduce the number.
        # To resolve the error, the list method should use the filter spec, to be less than 1,000 objects.
        filter_spec = target_object.FilterSpec()
        if self.object_moid:
            # Make a filter for moid if you specify object_moid.
            # The moid is a unique id, so get one object if target moid object exists in the vSphere environment.
            if target_object is vcenter_obj.Datacenter:
                filter_spec.datacenters = set([self.object_moid])

            if target_object is vcenter_obj.Cluster:
                filter_spec.clusters = set([self.object_moid])

            if target_object is vcenter_obj.ResourcePool:
                filter_spec.resource_pools = set([self.object_moid])

            if target_object is vcenter_obj.Folder:
                filter_spec.folders = set([self.object_moid])

            if target_object is vcenter_obj.VM:
                filter_spec.vms = set([self.object_moid])

            if target_object is vcenter_obj.Network:
                filter_spec.networks = set([self.object_moid])

            if target_object is vcenter_obj.Datastore:
                filter_spec.datastores = set([self.object_moid])
        else:
            # If you use object_name parameter, an object will filter with names.
            filter_spec.names = set([self.object_name])

        # Get an object for changing the object name.
        all_vmware_objs = target_object.list(filter_spec)

        # Ensure whether already exists an object in the same object_new_name name.
        existing_obj_moid = None
        if self.object_moid:
            if all_vmware_objs:
                # Ensure whether the same object name as object_new_name.
                if all_vmware_objs[0].name == self.object_new_name:
                    existing_obj_moid = all_vmware_objs
        else:
            existing_obj_moid = target_object.list(target_object.FilterSpec(names=set([self.object_new_name])))
        if existing_obj_moid:
            # Object with same name already exists
            results['rename_status']['current_name'] = results['rename_status']['previous_name'] = self.object_new_name
            results['changed'] = False
            self.module.exit_json(**results)

        if not all_vmware_objs:
            msg = "Failed to find object with %s '%s' and %s' object type"
            if self.object_name:
                msg = msg % ('name', self.object_name, self.object_type)
            elif self.object_moid:
                msg = msg % ('moid', self.object_moid, self.object_type)
            self.module.fail_json(msg=msg)

        obj_moid = getattr(all_vmware_objs[0], valid_object_types[self.object_type][2])
        vmware_obj = valid_object_types[self.object_type][1](obj_moid, self.soap_stub)

        if not vmware_obj:
            msg = "Failed to create VMware object with object %s %s"
            if self.object_name:
                msg = msg % ('name', self.object_name)
            elif self.object_moid:
                msg = msg % ('moid', self.object_moid)
            self.module.fail_json(msg=msg)

        try:
            results['rename_status']['previous_name'] = vmware_obj.name
            if not self.module.check_mode:
                task = vmware_obj.Rename_Task(self.object_new_name)
                wait_for_task(task)
            changed = True
            results['rename_status']['current_name'] = vmware_obj.name
        except Exception as e:
            msg = to_native(e)
            if hasattr(e, 'msg'):
                msg = to_native(e.msg)
            self.module.fail_json(msg=msg)

        results['changed'] = changed
        self.module.exit_json(**results)


def main():
    argument_spec = VmwareRestClient.vmware_client_argument_spec()
    argument_spec.update(
        object_name=dict(),
        object_moid=dict(),
        new_name=dict(aliases=['object_new_name'], required=True),
        object_type=dict(type='str', required=True, choices=['ClusterComputeResource', 'Cluster', 'Datacenter',
                                                             'Datastore', 'Folder', 'Network', 'ResourcePool', 'VM',
                                                             'VirtualMachine'])
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=[
            ['object_name', 'object_moid'],
        ]
    )

    vmware_object_rename = VmwareObjectRename(module)
    vmware_object_rename.ensure_state()


if __name__ == '__main__':
    main()
