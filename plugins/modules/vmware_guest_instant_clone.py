#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# Copyright: (c) 2021, Anant Chopra <chopraan@vmware.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_instant_clone
short_description: Instant Clone VM

description:
- This module can be used for Creating a powered-on Instant Clone of a virtual machine.
- All variables and VMware object names are case sensitive.
- M(community.vmware.vmware_guest) module is needed for creating a VM with poweredon state which would be used as a parent VM.
- M(community.vmware.vmware_guest_powerstate) module is also needed to poweroff the instant cloned module.
- The powered off VM would in turn be deleted by again using M(community.vmware.vmware_guest) module.
- Thus M(community.vmware.vmware_guest) module is necessary for removing Instant Cloned VM when VMs being created in testing environment.

options:
  name:
    description:
      - Name of the Cloned virtual machine.
    type: str
    aliases: ['vm_name']
    required: True
  parent_vm:
    description:
      - Name of the parent virtual machine.
      - This is a required parameter, if parameter C(uuid) or C(moid) is not supplied.
    type: str
  uuid:
    description:
      - UUID of the vm instance to clone from, this is VMware's unique identifier.
      - This is a required parameter, if parameter C(parent_vm) or C(moid) is not supplied.
    type: str
  moid:
    description:
      - Managed Object ID of the vm instance to manage if known, this is a unique identifier only within a single vCenter instance.
      - This is required if C(parent_vm) or C(uuid) is not supplied.
    type: str
  use_instance_uuid:
    description:
      - Whether to use the VMware instance UUID rather than the BIOS UUID.
    default: false
    type: bool
  host:
    description:
      - Name of the ESX Host in datacenter in which to place cloned VM.
      - The host has to be a member of the cluster that contains the resource pool.
      - Required with I(resource_pool) to find resource pool details. This will be used as additional information when there are resource pools with same name.
    type: str
    aliases: ['esxi_hostname']
    required: True
  datastore:
    description:
      - The name of the datastore or the datastore cluster.
      - If datastore cluster name is specified, module will find the Storage DRS recommended datastore in that cluster.
    type: str
    required: True
  datacenter:
    description:
      - Name of the datacenter, where VM to be deployed.
    type: str
    required: True
  folder:
    description:
      - Destination folder, absolute path to deploy the cloned vm.
      - This parameter is case sensitive.
      - 'Examples:'
      - 'folder: ha-datacenter/vm'
      - 'folder: /datacenter1/vm'
    type: str
  resource_pool:
    description:
      - Name of the resource pool in datacenter in which to place deployed VM.
      - Required if I(cluster) is not specified.
      - For default or non-unique resource pool names, specify I(host) and I(cluster).
      - C(Resources) is the default name of resource pool.
    type: str
    required: False

extends_documentation_fragment:
- community.vmware.vmware.documentation

version_added: '1.9.0'
author:
- Anant Chopra (@Anant99-sys)

'''

EXAMPLES = r'''
- name: Instant Clone a VM
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: False
    folder: "{{ f0 }}"
    datastore: "{{ rw_datastore }}"
    datacenter: "{{ dc1 }}"
    host: "{{ esxi1 }}"
    name: "{{ Clone_vm }}"
    parent_vm: "{{ testvm_1 }}"
    resource_pool: "{{ test_resource_001 }}"
  register: vm_clone
  delegate_to: localhost

- name: set state to poweroff the Cloned VM
  community.vmware.vmware_guest_powerstate:
    validate_certs: false
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "cloned_vm_from_vm_cluster"
    folder: "{{ f0 }}"
    state: powered-off
  register: poweroff_instant_clone_from_vm_when_cluster
  delegate_to: localhost

- name: Clean VM
  community.vmware.vmware_guest:
    validate_certs: false
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "cloned_vm_from_vm_cluster"
    datacenter: "{{ dc1 }}"
    state: absent
  register: delete_instant_clone_from_vm_when_cluster
  ignore_errors: true
  delegate_to: localhost

- name: Instant Clone a VM when skipping optional params
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: False
    name: "{{ Clone_vm }}"
    parent_vm: "{{ testvm_1 }}"
    datacenter: "{{ dc1 }}"
    datastore: "{{ rw_datastore }}"
    host: "{{ esxi1 }}"
  register: VM_clone_optional_arguments
  delegate_to: localhost

- name: Instant clone in check mode
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: False
    folder: "{{ f0 }}"
    datastore: "{{ rw_datastore }}"
    datacenter: "{{ dc1 }}"
    host: "{{ esx1 }}"
    name: "{{ Clone_vm }}"
    parent_vm: "{{ testvm_2 }}"
    resource_pool: "{{ test_resource_001 }}"
  check_mode: true
  register: check_mode_clone
  delegate_to: localhost
- debug:
    var: check_mode_clone

'''

RETURN = r'''
vm_info:
    description: metadata about the virtual machine
    returned: always
    type: dict
    sample: {
        "vm_name": "",
        "vcenter": "",
        "host": "",
        "datastore": "",
        "vm_folder": ""
    }
'''
from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    TaskError,
    find_vm_by_name,
    find_vm_by_id,
    connect_to_api,
    vmware_argument_spec,
    find_obj,
    wait_for_task,
)

try:
    from pyVmomi import vim
except ImportError:
    pass


class VmwareGuestInstantClone(PyVmomi):
    def __init__(self, module):
        """Constructor."""
        super().__init__(module)
        self.instant_clone_spec = vim.vm.InstantCloneSpec()
        self.relocate_spec = vim.vm.RelocateSpec()
        self.vm_name = self.params.get('name')
        self.parent_vm = self.params.get('parent_vm')
        self.datacenter = self.params.get('datacenter')
        self.datastore = self.params.get('datastore')
        self.hostname = self.params.get('hostname')
        self.folder = self.params.get('folder')
        self.resource_pool = self.params.get('resource_pool')
        self.host = self.params.get('host')
        self.username = self.params.get('username')
        self.password = self.params.get('password')
        self.validate_certs = self.params.get('validate_certs')
        self.moid = self.params.get('moid')
        self.uuid = self.params.get('uuid')
        self.port = self.params.get('port')
        self.use_instance_uuid = self.params.get('use_instance_uuid')

    def get_new_vm_info(self, vm):
        # to check if vm has been cloned in the destination vc
        # query for the vm in destination vc
        # get the host and datastore info
        info = {}
        vm_obj = find_vm_by_name(content=self.destination_content, vm_name=vm)
        if vm_obj is None:
            self.module.fail_json(msg="Newly Instant cloned VM is not found in the VCenter")

        vm_facts = self.gather_facts(vm_obj)
        info['vm_name'] = vm
        info['vcenter'] = self.hostname
        info['host'] = vm_facts['hw_esxi_host']
        info['datastore'] = vm_facts['hw_datastores']
        info['vm_folder'] = vm_facts['hw_folder']
        return info

    def Instant_clone(self):
        # clone the vm on  VC
        if self.vm_obj is None:
            vm_id = self.parent_vm or self.uuid or self.moid
            self.module.fail_json(msg="Failed to find the VM/template with %s" % vm_id)
        task = self.vm_obj.InstantClone_Task(spec=self.instant_clone_spec)
        try:
            wait_for_task(task)
            vm_info = self.get_new_vm_info(self.vm_name)
            result = {'changed': True, 'failed': False, 'vm_info': vm_info}
        except TaskError as task_e:
            self.module.fail_json(msg=to_native(task_e))
        return result

    def sanitize_params(self):
        '''
        Verify user-provided parameters
        '''
        # connect to host/VC
        self.destination_content = connect_to_api(
            self.module,
            hostname=self.hostname,
            username=self.username,
            password=self.password,
            port=self.port,
            validate_certs=self.validate_certs)

        use_instance_uuid = self.params.get('use_instance_uuid') or False

        if 'parent_vm' in self.params and self.params['parent_vm']:
            self.vm_obj = find_vm_by_name(content=self.destination_content, vm_name=self.parent_vm)

        elif 'uuid' in self.params and self.params['uuid']:
            if not use_instance_uuid:
                self.vm_obj = find_vm_by_id(content=self.destination_content, vm_id=self.params['uuid'], vm_id_type="uuid")
            elif use_instance_uuid:
                self.vm_obj = find_vm_by_id(content=self.destination_content,
                                            vm_id=self.params['uuid'],
                                            vm_id_type="instance_uuid")

        elif 'moid' in self.params and self.params['moid']:
            self.vm_obj = vim.VirtualMachine(self.params['moid'], self.si._stub)

        if self.vm_obj is None:
            vm_id = self.parent_vm or self.uuid or self.moid
            self.module.fail_json(msg="Failed to find the VM/template with %s" % vm_id)

        vm = find_vm_by_name(content=self.destination_content, vm_name=self.params['name'])
        if vm:
            self.module.exit_json(changed=False, msg="A VM with the given name already exists")

        self.datacenter = self.find_datacenter_by_name(self.params['datacenter'])

        # datacentre check
        if self.datacenter is None:
            self.module.fail_json(msg="Datacenter not found.")

        datastore_name = self.params['datastore']
        datastore_cluster = find_obj(self.destination_content, [vim.StoragePod], datastore_name)

        if datastore_cluster:
            # If user specified datastore cluster so get recommended datastore
            datastore_name = self.get_recommended_datastore(datastore_cluster_obj=datastore_cluster)
            # Check if get_recommended_datastore or user specified datastore exists or not
        # datastore check
        self.datastore = self.find_datastore_by_name(datastore_name=datastore_name)

        if self.datastore is None:
            self.module.fail_json(msg="Datastore not found.")

        if self.params['folder']:
            self.folder = self.find_folder_by_name(folder_name=self.params['folder'])
            if self.folder is None:
                self.module.fail_json(msg="Folder not found.")
        else:
            self.folder = self.datacenter.vmFolder

        self.host = self.find_hostsystem_by_name(host_name=self.params['host'])
        if self.host is None:
            self.module.fail_json(msg="Host not found.")

        if self.params['resource_pool']:
            self.resource_pool = self.find_resource_pool_by_name(resource_pool_name=self.params['resource_pool'])
            if self.resource_pool is None:
                self.module.fail_json(msg="Resource Pool not found.")
        else:
            self.resource_pool = self.host.parent.resourcePool

    def populate_specs(self):

        # populate relocate spec
        self.relocate_spec.datastore = self.datastore
        self.relocate_spec.pool = self.resource_pool
        self.relocate_spec.folder = self.folder
        # populate Instant clone spec
        self.instant_clone_spec.name = self.vm_name
        self.instant_clone_spec.location = self.relocate_spec


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        name=dict(type='str', required=True, aliases=['vm_name']),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        datacenter=dict(type='str', required=True),
        datastore=dict(type='str', required=True),
        use_instance_uuid=dict(type='bool', default=False),
        host=dict(type='str', required=True, aliases=['esxi_hostname']),
        folder=dict(type='str', required=False),
        resource_pool=dict(type='str', required=False),
        parent_vm=dict(type='str')
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['uuid', 'parent_vm', 'moid'],
        ],
        mutually_exclusive=[
            ['uuid', 'parent_vm', 'moid'],
        ],
    )
    result = {'failed': False, 'changed': False}

    if module.check_mode:
        result.update(
            vm_name=module.params['name'],
            host=module.params['hostname'],
            datastore=module.params['datastore'],
            vm_folder=module.params['folder'],
            changed=True,
            desired_operation='Create VM with check mode'
        )
        module.exit_json(**result)

    clone_manager = VmwareGuestInstantClone(module)
    clone_manager.sanitize_params()
    clone_manager.populate_specs()
    result = clone_manager.Instant_clone()

    if result['failed']:
        module.fail_json(**result)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
