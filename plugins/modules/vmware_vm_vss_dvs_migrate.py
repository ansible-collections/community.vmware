#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vm_vss_dvs_migrate
short_description: Migrates a virtual machine from a standard vswitch to distributed
description:
    - Migrates a virtual machine from a standard vswitch to distributed
author:
- Joseph Callen (@jcpowermac)
options:
    vm_name:
        description:
            - Name of the virtual machine to migrate to a dvSwitch
        required: true
        type: str
    dvportgroup_name:
        description:
            - Name of the portgroup to migrate to the virtual machine to
        required: true
        type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Migrate VCSA to vDS
  community.vmware.vmware_vm_vss_dvs_migrate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    vm_name: '{{ vm_name }}'
    dvportgroup_name: '{{ distributed_portgroup_name }}'
  delegate_to: localhost
'''

try:
    from pyVmomi import vim, vmodl
    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import HAS_PYVMOMI, \
    connect_to_api, get_all_objs, vmware_argument_spec, wait_for_task, find_vm_by_name


class VMwareVmVssDvsMigrate(object):
    def __init__(self, module):
        self.module = module
        self.content = connect_to_api(module)
        self.vm = None
        self.vm_name = module.params['vm_name']
        self.dvportgroup_name = module.params['dvportgroup_name']

    def process_state(self):
        vm_nic_states = {
            'absent': self.migrate_network_adapter_vds,
            'present': self.state_exit_unchanged,
        }

        vm_nic_states[self.check_vm_network_state()]()

    def find_dvspg_by_name(self):
        vmware_distributed_port_group = get_all_objs(self.content, [vim.dvs.DistributedVirtualPortgroup])
        for dvspg in vmware_distributed_port_group:
            if dvspg.name == self.dvportgroup_name:
                return dvspg
        return None

    def migrate_network_adapter_vds(self):
        vm_configspec = vim.vm.ConfigSpec()
        nic = vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo()
        port = vim.dvs.PortConnection()
        devicespec = vim.vm.device.VirtualDeviceSpec()

        pg = self.find_dvspg_by_name()

        if pg is None:
            self.module.fail_json(msg="The standard portgroup was not found")

        dvswitch = pg.config.distributedVirtualSwitch
        port.switchUuid = dvswitch.uuid
        port.portgroupKey = pg.key
        nic.port = port

        for device in self.vm.config.hardware.device:
            if isinstance(device, vim.vm.device.VirtualEthernetCard):
                devicespec.device = device
                devicespec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
                devicespec.device.backing = nic
                vm_configspec.deviceChange.append(devicespec)

        task = self.vm.ReconfigVM_Task(vm_configspec)
        changed, result = wait_for_task(task)
        self.module.exit_json(changed=changed, result=result)

    def state_exit_unchanged(self):
        self.module.exit_json(changed=False)

    def check_vm_network_state(self):
        try:
            self.vm = find_vm_by_name(self.content, vm_name=self.vm_name)

            if self.vm is None:
                self.module.fail_json(msg="A virtual machine with name %s does not exist" % self.vm_name)
            for device in self.vm.config.hardware.device:
                if isinstance(device, vim.vm.device.VirtualEthernetCard):
                    if isinstance(device.backing, vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo):
                        return 'present'
            return 'absent'
        except vmodl.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=runtime_fault.msg)
        except vmodl.MethodFault as method_fault:
            self.module.fail_json(msg=method_fault.msg)


def main():

    argument_spec = vmware_argument_spec()
    argument_spec.update(dict(vm_name=dict(required=True, type='str'),
                              dvportgroup_name=dict(required=True, type='str')))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)
    if not HAS_PYVMOMI:
        module.fail_json(msg='pyvmomi is required for this module')

    vmware_vmnic_migrate = VMwareVmVssDvsMigrate(module)
    vmware_vmnic_migrate.process_state()


if __name__ == '__main__':
    main()
