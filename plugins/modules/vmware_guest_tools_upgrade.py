#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Mike Klebolt  <michael.klebolt@centurylink.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_tools_upgrade
short_description: Module to upgrade VMTools
description:
    - This module upgrades the VMware Tools on Windows and Linux guests and reboots them.
notes:
    - "In order to upgrade VMTools, please power on virtual machine before hand - either 'manually' or
      using module M(community.vmware.vmware_guest_powerstate)."
options:
   name:
        description:
            - Name of the virtual machine to work with.
            - 'This is required if O(uuid) or O(moid) is not supplied.'
        type: str
   name_match:
        description:
            - If multiple virtual machines matching the name, use the first or last found.
        default: 'first'
        choices: ['first', 'last']
        type: str
   uuid:
        description:
            - "UUID of the instance to manage if known, this is VMware's unique identifier."
            - This is required if O(name) or O(moid) is not supplied.
        type: str
   moid:
        description:
            - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
            - This is required if O(name) or O(uuid) is not supplied.
        type: str
   folder:
        description:
            - Destination folder, absolute or relative path to find an existing guest.
            - This is required, if O(name) is supplied.
            - "The folder should include the datacenter. ESX's datacenter is ha-datacenter"
            - 'Examples:'
            - '   folder: /ha-datacenter/vm'
            - '   folder: ha-datacenter/vm'
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
            - Destination datacenter where the virtual machine exists.
        required: true
        type: str
   force_upgrade:
        description:
            - This flag overrides the guest operating system detection and forcibly upgrade VMware tools or open-vm-tools.
            - "This is useful when VMware tools is too old and unable to detect the 'guestFamily' value."
            - 'Using this flag may sometime give unexpected results since module will override the default'
            - "behaviour of 'guestFamily' detection."
        default: false
        type: bool
        required: false
   installer_options:
        version_added: '4.1.0'
        description:
            - Command line options passed to the installer to modify the installation procedure for tools.
        type: str
        required: false
extends_documentation_fragment:
- community.vmware.vmware.documentation

author:
    - Mike Klebolt (@MikeKlebolt) <michael.klebolt@centurylink.com>
'''

EXAMPLES = r'''
- name: Get VM UUID
  vmware_guest_facts:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter }}"
    folder: "/{{datacenter}}/vm"
    name: "{{ vm_name }}"
  delegate_to: localhost
  register: vm_facts

- name: Upgrade VMware Tools using uuid
  community.vmware.vmware_guest_tools_upgrade:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    uuid: "{{ vm_facts.instance.hw_product_uuid }}"
  delegate_to: localhost

- name: Upgrade VMware Tools using MoID
  community.vmware.vmware_guest_tools_upgrade:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
  delegate_to: localhost
'''

RETURN = r''' # '''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, wait_for_task
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class PyVmomiHelper(PyVmomi):
    def __init__(self, module):
        super(PyVmomiHelper, self).__init__(module)

    def upgrade_tools(self, vm):
        result = {'failed': False, 'changed': False, 'msg': ''}

        # Exit if VMware tools is already up to date
        if vm.guest.toolsVersionStatus2 == "guestToolsCurrent":
            result.update(
                msg="VMwareTools are already up to date",
            )
            return result
        elif vm.guest.toolsVersionStatus2 == "guestToolsSupportedNew" or vm.guest.toolsVersionStatus2 == "guestToolsTooNew":
            result.update(
                msg="VMwareTools are already newer than the version available on the host",
            )
            return result

        # Fail if VM is not powered on
        elif vm.summary.runtime.powerState != "poweredOn":
            result.update(
                failed=True,
                msg="VM must be powered on to upgrade tools",
            )
            return result

        # Fail if VMware tools is either not installed or not running
        elif vm.guest.toolsVersionStatus2 == 'guestToolsNotInstalled':
            result.update(
                failed=True,
                msg="VMwareTools are not installed."
            )
            return result
        elif vm.guest.toolsRunningStatus != 'guestToolsRunning':
            result.update(
                failed=True,
                msg="VMwareTools are not running."
            )
            return result

        # Fail if VMware tools are unmanaged
        elif vm.guest.toolsVersionStatus2 == "guestToolsUnmanaged":
            result.update(
                failed=True,
                msg="VMwareTools not managed by VMware",
            )
            return result

        # If vmware tools is out of date, check major OS family
        # Upgrade tools on Linux and Windows guests
        elif vm.guest.toolsVersionStatus2 in ["guestToolsBlacklisted", "guestToolsNeedUpgrade", "guestToolsSupportedOld", "guestToolsTooOld"]:
            try:
                force = self.module.params.get('force_upgrade')
                installer_options = self.module.params.get('installer_options')
                if force or vm.guest.guestFamily in ["linuxGuest", "windowsGuest"]:
                    if installer_options is not None:
                        task = vm.UpgradeTools(installer_options)
                    else:
                        task = vm.UpgradeTools()
                    changed, err_msg = wait_for_task(task)
                    result.update(changed=changed, msg=to_native(err_msg))
                else:
                    result.update(msg='Guest Operating System is other than Linux and Windows.')
                return result
            except Exception as exc:
                result.update(
                    failed=True,
                    msg='Error while upgrading VMwareTools %s' % to_native(exc),
                )
                return result
        else:
            result.update(
                failed=True,
                msg="This shouldn't happen, looks like a problem in the module",
            )
            return result


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        name_match=dict(type='str', choices=['first', 'last'], default='first'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        folder=dict(type='str'),
        datacenter=dict(type='str', required=True),
        force_upgrade=dict(type='bool', default=False),
        installer_options=dict(type='str'),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['name', 'uuid', 'moid']
        ]
    )

    if module.params['folder']:
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    pyv = PyVmomiHelper(module)
    # Check if the VM exists before continuing
    vm = pyv.get_vm()

    # VM already exists
    if vm:
        try:
            result = pyv.upgrade_tools(vm)
            if result['changed']:
                module.exit_json(changed=result['changed'])
            elif result['failed']:
                module.fail_json(msg=result['msg'])
            else:
                module.exit_json(msg=result['msg'], changed=result['changed'])
        except Exception as exc:
            module.fail_json(msg='Unknown error: %s' % to_native(exc))
    else:
        vm_id = module.params.get('uuid') or module.params.get('name') or module.params.get('moid')
        module.fail_json(msg='Unable to find VM %s' % vm_id)


if __name__ == '__main__':
    main()
