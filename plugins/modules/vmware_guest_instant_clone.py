#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ansible Project
# Copyright: (c) 2021, Anant Chopra <chopraan@vmware.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_instant_clone
short_description: Instant Clone VM

description:
- This module can be used for Creating a powered-on Instant Clone of a virtual machine.
- M(community.vmware.vmware_guest) module is needed for creating a VM with poweredon state which would be used as a parent VM.
- M(community.vmware.vmware_guest_powerstate) module is also needed to poweroff the instant cloned module.
- The powered off VM would in turn be deleted by again using M(community.vmware.vmware_guest) module.
- Thus M(community.vmware.vmware_guest) module is necessary for removing Instant Cloned VM when VMs being created in testing environment.
- Also GuestOS Customization has now been added with guestinfo_vars parameter.
- The Parent VM must have The Guest customization Engine for instant Clone to customize Guest OS.
- Only Linux Os in Parent VM enable support for native vSphere Guest Customization for Instant Clone in vSphere 7.
options:
  name:
    description:
      - Name of the Cloned virtual machine.
    type: str
    aliases: ['vm_name']
    required: true
  parent_vm:
    description:
      - Name of the parent virtual machine.
      - This is a required parameter, if parameter O(uuid) or O(moid) is not supplied.
    type: str
  uuid:
    description:
      - UUID of the vm instance to clone from, this is VMware's unique identifier.
      - This is a required parameter, if parameter O(parent_vm) or O(moid) is not supplied.
    type: str
  moid:
    description:
      - Managed Object ID of the vm instance to manage if known, this is a unique identifier only within a single vCenter instance.
      - This is required if O(parent_vm) or O(uuid) is not supplied.
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
      - Required with O(resource_pool) to find resource pool details. This will be used as additional information when there are resource pools with same name.
    type: str
    aliases: ['esxi_hostname']
    required: true
  datastore:
    description:
      - The name of the datastore or the datastore cluster.
      - If datastore cluster name is specified, module will find the Storage DRS recommended datastore in that cluster.
    type: str
    required: true
  datacenter:
    description:
      - Name of the datacenter, where VM to be deployed.
    type: str
    required: true
  folder:
    description:
      - Destination folder, absolute path to deploy the cloned vm.
      - 'Examples:'
      - 'folder: ha-datacenter/vm'
      - 'folder: /datacenter1/vm'
    type: str
  resource_pool:
    description:
      - Name of the resource pool in datacenter in which to place deployed VM.
      - C(Resources) is the default name of resource pool.
    type: str
    required: false
  vm_username:
    description:
      - The user to login-in to the virtual machine.
      - Only required when using guest customization feature.
    required: false
    type: str
  vm_password:
    description:
      - The password used to login-in to the virtual machine.
      - Only required when using guest customization feature.
    required: false
    type: str
  guestinfo_vars:
    description:
      - Provides GuestOS Customization functionality in instant cloned VM.
      - A list of key value pairs that will be passed to the destination VM.
      - These pairs should be used to provide user-defined customization to differentiate the destination VM from the source VM.
    suboptions:
      hostname:
        description:
          - hostname is used to obtain the DNS(Domain Name System) name and set the Guest system's hostname.
        type: str
      ipaddress:
        description:
          - ipaddress is used to set the ipaddress in Instant Cloned Guest Operating System.
        type: str
      netmask:
        description:
          - netmask is used to set the netmask in Instant Cloned Guest Operating System.
        type: str
      gateway:
        description:
          - netmask is used to set the netmask in Instant Cloned Guest Operating System.
        type: str
      dns:
        description:
          - dns is used to set the dns in Instant Cloned Guest Operating System..
        type: str
      domain:
        description:
          - domain is used to set A fully qualified domain name (FQDN) or complete domain name for Instant Cloned Guest operating System.
        type: str
    type: list
    elements: dict
  wait_vm_tools:
    description:
      - Whether waiting until vm tools start after rebooting an instant clone vm.
    type: bool
    default: true
  wait_vm_tools_timeout:
    description:
      - Define a timeout (in seconds) for the O(wait_vm_tools) parameter.
    type: int
    default: 300
extends_documentation_fragment:
- vmware.vmware.base_options

author:
- Anant Chopra (@Anant99-sys)

'''

EXAMPLES = r'''
- name: Instant Clone a VM
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
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

- name: Instant Clone a VM with guest_customization
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    vm_username: "root"
    vm_password: "SuperSecret"
    validate_certs: false
    folder: "{{ f0 }}"
    datastore: "{{ rw_datastore }}"
    datacenter: "{{ dc1 }}"
    host: "{{ esxi1 }}"
    guestinfo_vars:
      - hostname: "{{ guestinfo.ic.hostname }}"
        ipaddress: "{{ guestinfo.ic.ipaddress }}"
        netmask: "{{ guestinfo.ic.netmask }}"
        gateway: "{{ guestinfo.ic.gateway }}"
        dns: "{{ guestinfo.ic.dns }}"
        domain: "{{ guestinfo.ic.domain }}"
    name: "Instant_clone_guest_customize"
    parent_vm: "test_vm1"
    resource_pool: DC0_C0_RP1
  register: Instant_cloned_guest_customize
  delegate_to: localhost

- name: Instant Clone a VM when skipping optional params
  community.vmware.vmware_guest_instant_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
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
    validate_certs: false
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
    description:
      - metadata about the virtual machine
    returned: always
    type: dict
    sample: {
        "vm_name": "",
        "vcenter": "",
        "host": "",
        "datastore": "",
        "vm_folder": "",
        "instance_uuid": ""
    }
'''

import time
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    TaskError,
    find_vm_by_name,
    find_vm_by_id,
    find_obj,
    wait_for_task,
    set_vm_power_state
)
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible_collections.vmware.vmware.plugins.module_utils.clients.pyvmomi import PyvmomiClient

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
        self.wait_vm_tools = self.params.get('wait_vm_tools')
        self.wait_vm_tools_timeout = self.params.get('wait_vm_tools_timeout')
        self.guestinfo_vars = self.params.get('guestinfo_vars')

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
        info['instance_uuid'] = vm_facts['instance_uuid']
        return info

    def Instant_clone(self):
        # clone the vm on VC
        if self.vm_obj is None:
            vm_id = self.parent_vm or self.uuid or self.moid
            self.module.fail_json(msg="Failed to find the VM/template with %s" % vm_id)
        try:
            task = self.vm_obj.InstantClone_Task(spec=self.instant_clone_spec)
            wait_for_task(task)
            vm_info = self.get_new_vm_info(self.vm_name)
            result = {'changed': True, 'failed': False, 'vm_info': vm_info}
        except TaskError as task_e:
            self.module.fail_json(msg=to_native(task_e))

        pyvmomi_client = PyvmomiClient(
            hostname=self.hostname,
            username=self.username,
            password=self.password,
            port=self.port,
            validate_certs=self.validate_certs)

        self.destination_content = pyvmomi_client.content

        vm_IC = find_vm_by_name(content=self.destination_content, vm_name=self.params['name'])
        if vm_IC and self.params.get('guestinfo_vars'):
            guest_custom_mng = self.destination_content.guestCustomizationManager
            # Make an object for authentication in a guest OS
            auth_obj = vim.vm.guest.NamePasswordAuthentication()

            guest_user = self.params.get('vm_username')
            guest_password = self.params.get('vm_password')
            auth_obj.username = guest_user
            auth_obj.password = guest_password

            guestinfo_vars = self.params.get('guestinfo_vars')
            # Make a spec object to customize Guest OS
            customization_spec = vim.vm.customization.Specification()
            customization_spec.globalIPSettings = vim.vm.customization.GlobalIPSettings()
            customization_spec.globalIPSettings.dnsServerList = [guestinfo_vars[0]['dns']]
            # Make an identity object to do linux prep
            # The params are reflected the specified following after rebooting OS
            customization_spec.identity = vim.vm.customization.LinuxPrep()
            customization_spec.identity.domain = guestinfo_vars[0]['domain']
            customization_spec.identity.hostName = vim.vm.customization.FixedName()
            customization_spec.identity.hostName.name = guestinfo_vars[0]['hostname']

            customization_spec.nicSettingMap = []
            adapter_mapping_obj = vim.vm.customization.AdapterMapping()
            adapter_mapping_obj.adapter = vim.vm.customization.IPSettings()
            adapter_mapping_obj.adapter.ip = vim.vm.customization.FixedIp()
            adapter_mapping_obj.adapter.ip.ipAddress = guestinfo_vars[0]['ipaddress']
            adapter_mapping_obj.adapter.subnetMask = guestinfo_vars[0]['netmask']
            adapter_mapping_obj.adapter.gateway = [guestinfo_vars[0]['gateway']]

            customization_spec.nicSettingMap.append(adapter_mapping_obj)

            try:
                task_guest = guest_custom_mng.CustomizeGuest_Task(vm_IC, auth_obj, customization_spec)
                wait_for_task(task_guest)
                vm_info = self.get_new_vm_info(self.vm_name)
                result = {'changed': True, 'failed': False, 'vm_info': vm_info}
            except TaskError as task_e:
                self.module.fail_json(msg=to_native(task_e))

            # Should require rebooting to reflect customization parameters to instant clone vm.
            instant_vm_obj = find_vm_by_id(content=self.content, vm_id=vm_info['instance_uuid'], vm_id_type='instance_uuid')
            set_vm_power_state(content=self.content, vm=instant_vm_obj, state='rebootguest', force=False)

            if self.wait_vm_tools:
                interval = 15
                # Wait vm tools is started after rebooting.
                while self.wait_vm_tools_timeout > 0:
                    if instant_vm_obj.guest.toolsRunningStatus != 'guestToolsRunning':
                        break
                    self.wait_vm_tools_timeout -= interval
                    time.sleep(interval)

                while self.wait_vm_tools_timeout > 0:
                    if instant_vm_obj.guest.toolsRunningStatus == 'guestToolsRunning':
                        break
                    self.wait_vm_tools_timeout -= interval
                    time.sleep(interval)

                if self.wait_vm_tools_timeout <= 0:
                    self.module.fail_json(msg="Timeout has been reached for waiting to start the vm tools.")

        return result

    def sanitize_params(self):
        '''
        Verify user-provided parameters
        '''
        # connect to host/VC
        pyvmomi_client = PyvmomiClient(
            hostname=self.hostname,
            username=self.username,
            password=self.password,
            port=self.port,
            validate_certs=self.validate_certs)

        self.destination_content = pyvmomi_client.content

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
            self.folder = self.find_folder_by_fqpn(folder_name=self.params['folder'], datacenter_name=self.params['datacenter'], folder_type='vm')
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

        if self.params['guestinfo_vars']:
            self.guestinfo_vars = self.dict_to_optionvalues()
        else:
            self.guestinfo_vars = None

    def dict_to_optionvalues(self):
        optionvalues = []
        for dictionary in self.params['guestinfo_vars']:
            for key, value in dictionary.items():
                opt = vim.option.OptionValue()
                (opt.key, opt.value) = ("guestinfo.ic." + key, value)
                optionvalues.append(opt)

        return optionvalues

    def populate_specs(self):

        # populate relocate spec
        self.relocate_spec.datastore = self.datastore
        self.relocate_spec.pool = self.resource_pool
        self.relocate_spec.folder = self.folder
        # populate Instant clone spec
        self.instant_clone_spec.name = self.vm_name
        self.instant_clone_spec.location = self.relocate_spec
        self.instant_clone_spec.config = self.guestinfo_vars


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type='str', required=True, aliases=['vm_name']),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        vm_username=dict(type='str', required=False),
        vm_password=dict(type='str', no_log=True, required=False),
        datacenter=dict(type='str', required=True),
        datastore=dict(type='str', required=True),
        use_instance_uuid=dict(type='bool', default=False),
        host=dict(type='str', required=True, aliases=['esxi_hostname']),
        folder=dict(type='str', required=False),
        resource_pool=dict(type='str', required=False),
        parent_vm=dict(type='str'),
        wait_vm_tools=dict(type='bool', default=True),
        wait_vm_tools_timeout=dict(type='int', default=300),
        guestinfo_vars=dict(
            type='list',
            elements='dict',
            options=dict(
                ipaddress=dict(type='str'),
                netmask=dict(type='str'),
                gateway=dict(type='str'),
                dns=dict(type='str'),
                domain=dict(type='str'),
                hostname=dict(type='str'),
            ),
        ),
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
        required_together=[
            ['vm_username', 'vm_password', 'guestinfo_vars']
        ]
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
