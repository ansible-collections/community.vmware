#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_boot_manager
short_description: Manage boot options for the given virtual machine
description:
    - This module can be used to manage boot options for the given virtual machine.
author:
    - Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>
options:
   name:
     description:
     - Name of the VM to work with.
     - This is required if O(uuid) or O(moid) parameter is not supplied.
     type: str
   uuid:
     description:
     - UUID of the instance to manage if known, this is VMware's BIOS UUID by default.
     - This is required if O(name) or O(moid) parameter is not supplied.
     type: str
   moid:
     description:
     - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
     - This is required if O(name) or O(uuid) is not supplied.
     type: str
   use_instance_uuid:
     description:
     - Whether to use the VMware instance UUID rather than the BIOS UUID.
     default: false
     type: bool
   name_match:
     description:
     - If multiple virtual machines matching the name, use the first or last found.
     default: 'first'
     choices: ['first', 'last']
     type: str
   boot_order:
     description:
     - List of the boot devices.
     default: []
     type: list
     elements: str
   boot_hdd_name:
     description:
     - This parameter is optional, if not set, will use the first virtual disk found in VM device list.
     type: str
     version_added: '3.2.0'
   boot_delay:
     description:
     - Delay in milliseconds before starting the boot sequence.
     type: int
   enter_bios_setup:
     description:
     - If set to V(true), the virtual machine automatically enters BIOS setup the next time it boots.
     - The virtual machine resets this flag, so that the machine boots proceeds normally.
     type: 'bool'
   boot_retry_enabled:
     description:
     - If set to V(true), the virtual machine that fails to boot, will try to boot again after O(boot_retry_delay) is expired.
     - If set to V(false), the virtual machine waits indefinitely for user intervention.
     type: 'bool'
   boot_retry_delay:
     description:
     - Specify the time in milliseconds between virtual machine boot failure and subsequent attempt to boot again.
     - If set, will automatically set O(boot_retry_enabled=true) as this parameter is required.
     type: int
   boot_firmware:
     description:
     - Choose which firmware should be used to boot the virtual machine.
     choices: ["bios", "efi"]
     type: str
   secure_boot_enabled:
     description:
     - Choose if EFI secure boot should be enabled.  EFI secure boot can only be enabled with boot_firmware = efi
     type: 'bool'
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Change virtual machine's boot order and related parameters
  community.vmware.vmware_guest_boot_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: testvm
    boot_delay: 2000
    enter_bios_setup: true
    boot_retry_enabled: true
    boot_retry_delay: 22300
    boot_firmware: bios
    secure_boot_enabled: false
    boot_order:
      - floppy
      - cdrom
      - ethernet
      - disk
  delegate_to: localhost
  register: vm_boot_order

- name: Change virtual machine's boot order using Virtual Machine MoID
  community.vmware.vmware_guest_boot_manager:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    moid: vm-42
    boot_delay: 2000
    enter_bios_setup: true
    boot_retry_enabled: true
    boot_retry_delay: 22300
    boot_firmware: bios
    secure_boot_enabled: false
    boot_order:
      - floppy
      - cdrom
      - ethernet
      - disk
  delegate_to: localhost
  register: vm_boot_order
'''

RETURN = r'''
vm_boot_status:
    description: metadata about boot order of virtual machine
    returned: always
    type: dict
    sample: {
        "current_boot_order": [
            "floppy",
            "disk",
            "ethernet",
            "cdrom"
        ],
        "current_boot_delay": 2000,
        "current_boot_retry_delay": 22300,
        "current_boot_retry_enabled": true,
        "current_enter_bios_setup": true,
        "current_boot_firmware": "bios",
        "current_secure_boot_enabled": false,
        "previous_boot_delay": 10,
        "previous_boot_retry_delay": 10000,
        "previous_boot_retry_enabled": true,
        "previous_enter_bios_setup": false,
        "previous_boot_firmware": "efi",
        "previous_secure_boot_enabled": true,
        "previous_boot_order": [
            "ethernet",
            "cdrom",
            "floppy",
            "disk"
        ],
    }
'''


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, find_vm_by_id, wait_for_task, TaskError
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec

try:
    from pyVmomi import vim, VmomiJSONEncoder
except ImportError:
    pass


class VmBootManager(PyVmomi):
    def __init__(self, module):
        super(VmBootManager, self).__init__(module)
        self.name = self.params['name']
        self.uuid = self.params['uuid']
        self.moid = self.params['moid']
        self.use_instance_uuid = self.params['use_instance_uuid']
        self.vm = None

    def _get_vm(self):
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

        elif self.moid:
            vm_obj = VmomiJSONEncoder.templateOf('VirtualMachine')(self.module.params['moid'], self.si._stub)
            if vm_obj:
                vms.append(vm_obj)

        if vms:
            if self.params.get('name_match') == 'first':
                self.vm = vms[0]
            elif self.params.get('name_match') == 'last':
                self.vm = vms[-1]
        else:
            self.module.fail_json(msg="Failed to find virtual machine using %s" % (self.name or self.uuid))

    @staticmethod
    def humanize_boot_order(boot_order):
        results = []
        for device in boot_order:
            if isinstance(device, vim.vm.BootOptions.BootableCdromDevice):
                results.append('cdrom')
            elif isinstance(device, vim.vm.BootOptions.BootableDiskDevice):
                results.append('disk')
            elif isinstance(device, vim.vm.BootOptions.BootableEthernetDevice):
                results.append('ethernet')
            elif isinstance(device, vim.vm.BootOptions.BootableFloppyDevice):
                results.append('floppy')
        return results

    def ensure(self):
        boot_order_list = []
        change_needed = False
        kwargs = dict()
        previous_boot_disk = None
        valid_device_strings = ['cdrom', 'disk', 'ethernet', 'floppy']

        self._get_vm()

        for device_order in self.params.get('boot_order'):
            if device_order not in valid_device_strings:
                self.module.fail_json(msg="Invalid device found [%s], please specify device from ['%s']" % (device_order,
                                                                                                            "', '".join(valid_device_strings)))
            if device_order == 'cdrom':
                first_cdrom = [device for device in self.vm.config.hardware.device if isinstance(device, vim.vm.device.VirtualCdrom)]
                if first_cdrom:
                    boot_order_list.append(vim.vm.BootOptions.BootableCdromDevice())
            elif device_order == 'disk':
                if not self.params.get('boot_hdd_name'):
                    first_hdd = [device for device in self.vm.config.hardware.device if isinstance(device, vim.vm.device.VirtualDisk)]
                else:
                    first_hdd = [device for device in self.vm.config.hardware.device if isinstance(device, vim.vm.device.VirtualDisk)
                                 and device.deviceInfo.label == self.params.get('boot_hdd_name')]
                    if not first_hdd:
                        self.module.fail_json(msg="Not found virtual disk with disk label '%s'" % (self.params.get('boot_hdd_name')))
                if first_hdd:
                    boot_order_list.append(vim.vm.BootOptions.BootableDiskDevice(deviceKey=first_hdd[0].key))
            elif device_order == 'ethernet':
                first_ether = [device for device in self.vm.config.hardware.device if isinstance(device, vim.vm.device.VirtualEthernetCard)]
                if first_ether:
                    boot_order_list.append(vim.vm.BootOptions.BootableEthernetDevice(deviceKey=first_ether[0].key))
            elif device_order == 'floppy':
                first_floppy = [device for device in self.vm.config.hardware.device if isinstance(device, vim.vm.device.VirtualFloppy)]
                if first_floppy:
                    boot_order_list.append(vim.vm.BootOptions.BootableFloppyDevice())

        # Get previous boot disk name when boot_hdd_name is set
        if self.params.get('boot_hdd_name'):
            for i in range(0, len(self.vm.config.bootOptions.bootOrder)):
                if isinstance(self.vm.config.bootOptions.bootOrder[i], vim.vm.BootOptions.BootableDiskDevice):
                    if self.vm.config.bootOptions.bootOrder[i].deviceKey:
                        for dev in self.vm.config.hardware.device:
                            if isinstance(dev, vim.vm.device.VirtualDisk) and \
                                    dev.key == self.vm.config.bootOptions.bootOrder[i].deviceKey:
                                previous_boot_disk = dev.deviceInfo.label

        if len(boot_order_list) != len(self.vm.config.bootOptions.bootOrder):
            kwargs.update({'bootOrder': boot_order_list})
            change_needed = True
        else:
            for i in range(0, len(boot_order_list)):
                boot_device_type = type(boot_order_list[i])
                vm_boot_device_type = type(self.vm.config.bootOptions.bootOrder[i])
                if boot_device_type != vm_boot_device_type:
                    kwargs.update({'bootOrder': boot_order_list})
                    change_needed = True
                else:
                    if vm_boot_device_type is vim.vm.BootOptions.BootableDiskDevice and \
                            boot_order_list[i].deviceKey != self.vm.config.bootOptions.bootOrder[i].deviceKey:
                        kwargs.update({'bootOrder': boot_order_list})
                        change_needed = True

        if self.params.get('boot_delay') is not None and \
                self.vm.config.bootOptions.bootDelay != self.params.get('boot_delay'):
            kwargs.update({'bootDelay': self.params.get('boot_delay')})
            change_needed = True

        if self.params.get('enter_bios_setup') is not None and \
                self.vm.config.bootOptions.enterBIOSSetup != self.params.get('enter_bios_setup'):
            kwargs.update({'enterBIOSSetup': self.params.get('enter_bios_setup')})
            change_needed = True

        if self.params.get('boot_retry_enabled') is not None and \
                self.vm.config.bootOptions.bootRetryEnabled != self.params.get('boot_retry_enabled'):
            kwargs.update({'bootRetryEnabled': self.params.get('boot_retry_enabled')})
            change_needed = True

        if self.params.get('boot_retry_delay') is not None and \
                self.vm.config.bootOptions.bootRetryDelay != self.params.get('boot_retry_delay'):
            if not self.vm.config.bootOptions.bootRetryEnabled:
                kwargs.update({'bootRetryEnabled': True})
            kwargs.update({'bootRetryDelay': self.params.get('boot_retry_delay')})
            change_needed = True

        boot_firmware_required = False
        if self.params.get('boot_firmware') is not None and self.vm.config.firmware != self.params.get('boot_firmware'):
            change_needed = True
            boot_firmware_required = True

        if self.params.get('secure_boot_enabled') is not None:
            if self.params.get('secure_boot_enabled') and self.params.get('boot_firmware') == "bios":
                self.module.fail_json(msg="Secure boot cannot be enabled when boot_firmware = bios")
            elif self.params.get('secure_boot_enabled') and \
                    self.params.get('boot_firmware') != 'efi' and \
                    self.vm.config.firmware == 'bios':
                self.module.fail_json(msg="Secure boot cannot be enabled since the VM's boot firmware is currently set to bios")
            elif self.vm.config.bootOptions.efiSecureBootEnabled != self.params.get('secure_boot_enabled'):
                kwargs.update({'efiSecureBootEnabled': self.params.get('secure_boot_enabled')})
                change_needed = True

        changed = False
        results = dict(
            previous_boot_order=self.humanize_boot_order(self.vm.config.bootOptions.bootOrder),
            previous_boot_delay=self.vm.config.bootOptions.bootDelay,
            previous_enter_bios_setup=self.vm.config.bootOptions.enterBIOSSetup,
            previous_boot_retry_enabled=self.vm.config.bootOptions.bootRetryEnabled,
            previous_boot_retry_delay=self.vm.config.bootOptions.bootRetryDelay,
            previous_boot_firmware=self.vm.config.firmware,
            previous_secure_boot_enabled=self.vm.config.bootOptions.efiSecureBootEnabled,
            current_boot_order=[]
        )
        if previous_boot_disk:
            results.update({'previous_boot_disk': previous_boot_disk})

        if change_needed:
            vm_conf = vim.vm.ConfigSpec()
            vm_conf.bootOptions = vim.vm.BootOptions(**kwargs)
            if boot_firmware_required:
                vm_conf.firmware = self.params.get('boot_firmware')
            task = self.vm.ReconfigVM_Task(vm_conf)

            try:
                changed, result = wait_for_task(task)
            except TaskError as e:
                self.module.fail_json(msg="Failed to perform reconfigure virtual"
                                          " machine %s for boot order due to: %s" % (self.name or self.uuid,
                                                                                     to_native(e)))

        results.update(
            {
                'current_boot_order': self.humanize_boot_order(self.vm.config.bootOptions.bootOrder),
                'current_boot_delay': self.vm.config.bootOptions.bootDelay,
                'current_enter_bios_setup': self.vm.config.bootOptions.enterBIOSSetup,
                'current_boot_retry_enabled': self.vm.config.bootOptions.bootRetryEnabled,
                'current_boot_retry_delay': self.vm.config.bootOptions.bootRetryDelay,
                'current_boot_firmware': self.vm.config.firmware,
                'current_secure_boot_enabled': self.vm.config.bootOptions.efiSecureBootEnabled
            }
        )
        if self.params.get('boot_hdd_name'):
            results.update({'current_boot_disk': self.params.get('boot_hdd_name')})

        self.module.exit_json(changed=changed, vm_boot_status=results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
        name_match=dict(
            choices=['first', 'last'],
            default='first'
        ),
        boot_order=dict(
            type='list',
            default=[],
            elements='str'
        ),
        boot_hdd_name=dict(type='str'),
        boot_delay=dict(type='int'),
        enter_bios_setup=dict(type='bool'),
        boot_retry_enabled=dict(type='bool'),
        boot_retry_delay=dict(type='int'),
        secure_boot_enabled=dict(type='bool'),
        boot_firmware=dict(
            type='str',
            choices=['efi', 'bios']
        )
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['name', 'uuid', 'moid']
        ],
        mutually_exclusive=[
            ['name', 'uuid', 'moid']
        ],
    )

    pyv = VmBootManager(module)
    pyv.ensure()


if __name__ == '__main__':
    main()
