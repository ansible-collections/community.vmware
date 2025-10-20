#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ansible Project
# Copyright: (c) 2021, VMware, Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_guest_tpm
short_description: Add or remove vTPM device for specified VM.
description: >
   This module is used for adding or removing Virtual Trusted Platform Module(vTPM) device for an existing
   Virtual Machine. You must create a key provider on vCenter before you can add a vTPM. The ESXi hosts
   running in your environment must be ESXi 6.7 or later (Windows guest OS), or 7.0 Update 2 (Linux guest OS).
author:
- Diane Wang (@Tomorrow9) <dianew@vmware.com>
options:
  name:
    description:
    - Name of the virtual machine.
    - This is required if parameter O(uuid) or O(moid) is not supplied.
    type: str
  uuid:
    description:
    - UUID of the instance to manage if known, this is VMware's unique identifier.
    - This is required if parameter O(name) or O(moid) is not supplied.
    type: str
  moid:
    description:
    - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
    - This is required if O(name) or O(uuid) is not supplied.
    type: str
  folder:
    description:
    - VM folder, absolute or relative path to find an existing VM.
    - This parameter is not required, only when multiple VMs are found with the same name.
    - The folder should include the datacenter name.
    - 'Examples:'
    - '   folder: /datacenter1/vm'
    - '   folder: datacenter1/vm'
    - '   folder: /datacenter1/vm/folder1'
    - '   folder: datacenter1/vm/folder1'
    - '   folder: /folder1/datacenter1/vm'
    - '   folder: folder1/datacenter1/vm'
    - '   folder: /folder1/datacenter1/vm/folder2'
    type: str
  datacenter:
    description:
    - The vCenter datacenter name used to get specified cluster or host.
    type: str
    required: true
  state:
    description:
    - State of vTPM device.
    - If set to 'absent', vTPM device will be removed from VM.
    - If set to 'present', vTPM device will be added if not present.
    - Virtual machine should be turned off before add or remove vTPM device.
    - Virtual machine should not contain snapshots before add vTPM device.
    type: str
    choices: ['present', 'absent']
    default: 'present'
extends_documentation_fragment:
- vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Add vTPM to specified VM
  community.vmware.vmware_guest_tpm:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    name: "Test_VM"
    state: present
  delegate_to: localhost

- name: Remove vTPM from specified VM
  community.vmware.vmware_guest_tpm:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    name: "Test_VM"
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
instance:
    description: metadata about the VM vTPM device
    returned: always
    type: dict
    sample: None
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, wait_for_task
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vm_device_helper import PyVmomiDeviceHelper


class PyVmomiHelper(PyVmomi):
    def __init__(self, module):
        super(PyVmomiHelper, self).__init__(module)
        self.device_helper = PyVmomiDeviceHelper(self.module)
        self.config_spec = vim.vm.ConfigSpec()
        self.config_spec.deviceChange = []
        self.vm = None
        self.vtpm_device = None

    def get_vtpm_info(self, vm_obj=None, vtpm_device=None):
        vtpm_info = dict()
        if vm_obj:
            for device in vm_obj.config.hardware.device:
                if self.device_helper.is_tpm_device(device):
                    vtpm_device = device
        if vtpm_device:
            vtpm_info = dict(
                key=vtpm_device.key,
                label=vtpm_device.deviceInfo.label,
                summary=vtpm_device.deviceInfo.summary,
            )

        return vtpm_info

    def vtpm_operation(self, vm_obj=None):
        vtpm_device_spec = None
        results = {'failed': False, 'changed': False}
        if not self.is_vcenter():
            self.module.fail_json(msg="Please connect to vCenter Server to configure vTPM device of virtual machine.")

        self.vm = vm_obj
        if self.vm.runtime.powerState != vim.VirtualMachinePowerState.poweredOff:
            self.module.fail_json(msg="Please make sure VM is powered off before configuring vTPM device,"
                                      " current state is '%s'" % self.vm.runtime.powerState)

        for device in self.vm.config.hardware.device:
            if self.device_helper.is_tpm_device(device):
                self.vtpm_device = device

        if self.module.params['state'] == 'present':
            if self.module.check_mode:
                results['desired_operation'] = "add vTPM"
            else:
                results['vtpm_operation'] = "add vTPM"
            if self.vtpm_device:
                results['vtpm_info'] = self.get_vtpm_info(vtpm_device=self.vtpm_device)
                results['msg'] = "vTPM device already exist on VM"
                self.module.exit_json(**results)
            else:
                if self.module.check_mode:
                    results['changed'] = True
                    self.module.exit_json(**results)
                vtpm_device_spec = self.device_helper.create_tpm()
        if self.module.params['state'] == 'absent':
            if self.module.check_mode:
                results['desired_operation'] = "remove vTPM"
            else:
                results['vtpm_operation'] = "remove vTPM"
            if self.vtpm_device is None:
                results['msg'] = "No vTPM device found on VM"
                self.module.exit_json(**results)
            else:
                if self.module.check_mode:
                    results['changed'] = True
                    self.module.exit_json(**results)
                vtpm_device_spec = self.device_helper.remove_tpm(self.vtpm_device)
        self.config_spec.deviceChange.append(vtpm_device_spec)

        try:
            task = self.vm.ReconfigVM_Task(spec=self.config_spec)
            wait_for_task(task)
        except Exception as e:
            self.module.fail_json(msg="Failed to configure vTPM device on virtual machine due to '%s'" % to_native(e))
        if task.info.state == 'error':
            self.module.fail_json(msg='Failed to reconfigure VM with vTPM device', detail=task.info.error.msg)
        results['changed'] = True
        results['vtpm_info'] = self.get_vtpm_info(vm_obj=self.vm)
        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        folder=dict(type='str'),
        datacenter=dict(type='str', required=True),
        state=dict(type='str', default='present', choices=['present', 'absent']),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[['name', 'uuid', 'moid']],
    )
    if module.params['folder']:
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    vm_config_vtpm = PyVmomiHelper(module)
    vm = vm_config_vtpm.get_vm()
    if not vm:
        vm_id = (module.params.get('name') or module.params.get('uuid') or module.params.get('moid'))
        module.fail_json(msg="Unable to configure vTPM device for non-existing virtual machine '%s'." % vm_id)
    try:
        vm_config_vtpm.vtpm_operation(vm_obj=vm)
    except Exception as e:
        module.fail_json(msg="Failed to configure vTPM device of virtual machine '%s' with exception : %s"
                             % (vm.name, to_native(e)))


if __name__ == "__main__":
    main()
