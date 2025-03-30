#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2023, Pure Storage, Inc.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_disk
short_description: Attach or detach disks from an esxi host
description:
- This module can be used to attach / detach disks on an ESXi host.
author:
- Ryan BADAÏ (@ryanb74) <ryan.badai@dbi-services.com>
options:
  uuid:
    description:
    - uuid of the disk to attach / detach.
    - Can be obtained using community.vmware.vmware_host_scsidisk_info module.
    required: true
    type: str
  esxi_hostname:
    description:
    - Name of the ESXi host on which the operation is performed.
    - Required when used with a vcenter
    type: str
    required: false
  state:
    description:
    - "attached: Attach disk on esxi host if it is not attached, else do nothing."
    - "detached: Detach disk on esxi host if it is attached, else do nothing."
    default: attached
    choices: [ attached, detached ]
    type: str
seealso:
- VMware vSphere API Reference Documentation : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/right-pane.html
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Attach disk on esxi host
  vmware_host_disk:
    hostname: "{{ vcenter_hostname }}"
    esxi_hostname: "{{ esxi_hostname }}"
    uuid: "{{ disk_uuid }}"
    state: attached
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
'''

RETURN = r'''
result:
  description: A string that describes whether the mount/unmount was successfully performed.
  returned: success or changed
  type: str
  sample:
    - Disk with uuid 020001000060060e8008783a000050783a000000164f50454e2d56 is already attached.
    - Disk with uuid 020001000060060e8008783a000050783a000000164f50454e2d56 was successfully detached.
    - Disk with uuid 020001000060060e8008783a000050783a000000164f50454e2d56 is already detached.
    - Disk with uuid 020001000060060e8008783a000050783a000000164f50454e2d56 was successfully attached.
    - Disk with uuid FAKE_UUID was not found !
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import vmware_argument_spec, find_obj
from ansible_collections.community.vmware.plugins.module_utils.vmware_sms import SMS
from ansible.module_utils._text import to_native


class VMwareHostDisk(SMS):
    def __init__(self, module):
        super(VMwareHostDisk, self).__init__(module)

        self.uuid = module.params['uuid']
        self.esxi_hostname = module.params['esxi_hostname']
        self.state = module.params['state']

        if self.is_vcenter():
            if not self.esxi_hostname:
                self.module.fail_json(msg="esxi_hostname is mandatory with a vcenter")
            self.esxi = self.find_hostsystem_by_name(self.esxi_hostname)
            if self.esxi is None:
                self.module.fail_json(msg="Failed to find ESXi hostname %s" % self.esxi_hostname)
        else:
            self.esxi = find_obj(self.content, [vim.HostSystem], None)

    def process_state(self):
        """Evaluates what must be done based on current state"""
        ds_states = {
            'detached': {
                'attached': self.detach_disk_from_host,
                'detached': lambda: self.module.exit_json(changed=False, result="Disk with uuid %s is already detached." % self.uuid)
            },
            'attached': {
                'attached': lambda: self.module.exit_json(changed=False, result="Disk with uuid %s is already attached." % self.uuid),
                'detached': self.attach_disk_to_host
            }
        }
        try:
            ds_states[self.state][self.get_disk_attachment_state()]()
        except (vmodl.RuntimeFault, vmodl.MethodFault) as vmodl_fault:
            self.module.fail_json(msg=to_native(vmodl_fault.msg))
        except Exception as e:
            self.module.fail_json(msg=to_native(e))

    def get_disk_attachment_state(self):
        """Checks whether the disk is attached or not.
          :return: Current attachment state of the disk: "attached" or "detached"
          :rtype: string
        """
        storage_system = self.esxi.configManager.storageSystem # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html 

        for disk in storage_system.storageDeviceInfo.scsiLun: # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.ScsiLun.html 
            if disk.uuid == self.uuid:
                if "ok" in disk.operationalState: # https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.ScsiLun.State.html 
                    return "attached"
                elif "off" in disk.operationalState:
                    return "detached"
                self.module.fail_json(msg='Disk is in an unexpected state !{} ' % disk.operationalState)
                
        self.module.fail_json(msg='Disk with uuid %s was not found !' % self.uuid)
    

    def detach_disk_from_host(self):
        if self.module.check_mode is False:       
            try:
                self.esxi.configManager.storageSystem.DetachScsiLun(self.uuid)
                self.module.exit_json(changed=True, result="Disk with uuid %s was successfully detached." % self.uuid)

            except vim.fault.ResourceInUse as e:
                self.module.fail_json(msg='Disk with uuid {}  is currently used and can\'t be detached ! {}' % self.uuid % e)
            except vim.fault.VimFault as e:
                self.module.fail_json(msg='Disk with uuid {} can\'t be detached because of an unexpected error ! {}' % self.uuid % e)
        self.module.exit_json(changed=True, result="CHECK MODE: Disk with uuid %s would be successfully detached." % self.uuid)


    def attach_disk_to_host(self):
        if self.module.check_mode is False:
            try:
                self.esxi.configManager.storageSystem.AttachScsiLun(self.uuid) 
                self.module.exit_json(changed=True, result="Disk with uuid %s was successfully attached." % self.uuid)
            except vim.fault.VimFault as e:
                self.module.fail_json(msg='Disk with uuid {} can\'t be attached because of an unexpected error ! {}' % self.uuid % e)
        self.module.exit_json(changed=True, result="CHECK MODE: disk with uuid %s would be successfully attached." % self.uuid)

def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        uuid=dict(type='str', required=True),
        esxi_hostname=dict(type='str', required=False),
        state=dict(type='str', default='attached', choices=['detached', 'attached'])
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    vmware_host_datastore = VMwareHostDisk(module)
    vmware_host_datastore.process_state()


if __name__ == '__main__':
    main()