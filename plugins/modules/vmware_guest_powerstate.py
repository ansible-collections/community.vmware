#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r"""
---
module: vmware_guest_powerstate
deprecated:
  removed_in: 7.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.vm_powerstate) instead.
short_description: Manages power states of virtual machines in vCenter
description:
- Power on / Power off / Restart a virtual machine.
author:
- Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>
options:
  datacenter:
    description:
      - The datacenter where the VM you'd like to operate the power.
    default: ha-datacenter
    type: str
  state:
    description:
    - Set the state of the virtual machine.
    choices: [ powered-off, powered-on, reboot-guest, restarted, shutdown-guest, suspended, present]
    default: present
    type: str
  name:
    description:
    - Name of the virtual machine to work with.
    - Virtual machine names in vCenter are not necessarily unique, which may be problematic, see O(name_match).
    type: str
  name_match:
    description:
    - If multiple virtual machines matching the name, use the first or last found.
    default: first
    choices: [ first, last ]
    type: str
  uuid:
    description:
    - UUID of the instance to manage if known, this is VMware's unique identifier.
    - This is required if O(name) or O(moid) is not supplied.
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
  folder:
    description:
    - Destination folder, absolute or relative path to find an existing guest.
    - The folder should include the datacenter. ESX's datacenter is ha-datacenter
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
  scheduled_at:
    description:
    - Date and time in string format at which specified task needs to be performed.
    - "The required format for date and time - 'dd/mm/yyyy hh:mm'."
    - Scheduling task requires vCenter server. A standalone ESXi server does not support this option.
    type: str
  schedule_task_name:
    description:
    - Name of schedule task.
    - Valid only if O(scheduled_at) is specified.
    type: str
    required: false
  schedule_task_description:
    description:
    - Description of schedule task.
    - Valid only if O(scheduled_at) is specified.
    type: str
    required: false
  schedule_task_enabled:
    description:
    - Flag to indicate whether the scheduled task is enabled or disabled.
    type: bool
    required: false
    default: true
  force:
    description:
    - Ignore warnings and complete the actions.
    - This parameter is useful while forcing virtual machine state.
    default: false
    type: bool
  state_change_timeout:
    description:
    - If the O(state=shutdown-guest), by default the module will return immediately after sending the shutdown signal.
    - If this argument is set to a positive integer, the module will instead wait for the VM to reach the poweredoff state.
    - The value sets a timeout in seconds for the module to wait for the state change.
    default: 0
    type: int
  answer:
    description:
    - A list of questions to answer, should one or more arise while waiting for the task to complete.
    - Some common uses are to allow a cdrom to be changed even if locked, or to answer the question as to whether a VM was copied or moved.
    - Can be used if O(state=powered-on).
    suboptions:
      question:
        description:
        - The message id, for example C(msg.uuid.altered).
        type: str
        required: true
      response:
        description:
        - The choice key, for example C(button.uuid.copiedTheVM).
        type: str
        required: true
    type: list
    elements: dict
extends_documentation_fragment:
- vmware.vmware.base_options
"""

EXAMPLES = r"""
- name: Set the state of a virtual machine to poweroff
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: "/{{ datacenter_name }}/vm/my_folder"
    name: "{{ guest_name }}"
    state: powered-off
  delegate_to: localhost
  register: deploy

- name: Set the state of a virtual machine to poweron using MoID
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: "/{{ datacenter_name }}/vm/my_folder"
    moid: vm-42
    state: powered-on
  delegate_to: localhost
  register: deploy

- name: Set the state of a virtual machine to poweroff at given scheduled time
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    folder: "/{{ datacenter_name }}/vm/my_folder"
    name: "{{ guest_name }}"
    state: powered-off
    scheduled_at: "09/01/2018 10:18"
    schedule_task_name: "task_00001"
    schedule_task_description: "Sample task to poweroff VM"
    schedule_task_enabled: true
  delegate_to: localhost
  register: deploy_at_schedule_datetime

- name: Wait for the virtual machine to shutdown
  community.vmware.vmware_guest_powerstate:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "{{ guest_name }}"
    state: shutdown-guest
    state_change_timeout: 200
  delegate_to: localhost
  register: deploy

- name: Automatically answer if a question locked a virtual machine
  block:
    - name: Power on a virtual machine without the answer param
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        validate_certs: false
        folder: "{{ f1 }}"
        name: "{{ vm_name }}"
        state: powered-on
  rescue:
    - name: Power on a virtual machine with the answer param
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        validate_certs: false
        folder: "{{ f1 }}"
        name: "{{ vm_name }}"
        answer:
          - question: "msg.uuid.altered"
            response: "button.uuid.copiedTheVM"
        state: powered-on
"""

RETURN = r""" # """

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from random import randint
from datetime import datetime
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, set_vm_power_state, \
    check_answer_question_status, make_answer_response, answer_question, gather_vm_facts
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.common.text.converters import to_native


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str', default='ha-datacenter'),
        state=dict(type='str', default='present',
                   choices=['present', 'powered-off', 'powered-on', 'reboot-guest', 'restarted', 'shutdown-guest', 'suspended']),
        name=dict(type='str'),
        name_match=dict(type='str', choices=['first', 'last'], default='first'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
        folder=dict(type='str'),
        force=dict(type='bool', default=False),
        scheduled_at=dict(type='str'),
        schedule_task_name=dict(),
        schedule_task_description=dict(),
        schedule_task_enabled=dict(type='bool', default=True),
        state_change_timeout=dict(type='int', default=0),
        answer=dict(type='list',
                    elements='dict',
                    options=dict(
                        question=dict(type='str', required=True),
                        response=dict(type='str', required=True)
                    ))
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
        mutually_exclusive=[
            ['name', 'uuid', 'moid'],
            ['scheduled_at', 'answer']
        ],
    )

    result = dict(changed=False,)

    if module.params['folder']:
        module.params['folder'] = module.params['folder'].rstrip('/')

    pyv = PyVmomi(module)

    # Check if the VM exists before continuing
    vm = pyv.get_vm()

    if vm:
        # VM already exists, so set power state
        scheduled_at = module.params.get('scheduled_at', None)
        if scheduled_at:
            if not pyv.is_vcenter():
                module.fail_json(msg="Scheduling task requires vCenter, hostname %s "
                                     "is an ESXi server." % module.params.get('hostname'))
            powerstate = {
                'present': vim.VirtualMachine.PowerOn,
                'powered-off': vim.VirtualMachine.PowerOff,
                'powered-on': vim.VirtualMachine.PowerOn,
                'reboot-guest': vim.VirtualMachine.RebootGuest,
                'restarted': vim.VirtualMachine.Reset,
                'shutdown-guest': vim.VirtualMachine.ShutdownGuest,
                'suspended': vim.VirtualMachine.Suspend,
            }
            dt = ''
            try:
                dt = datetime.strptime(scheduled_at, '%d/%m/%Y %H:%M')
            except ValueError as e:
                module.fail_json(msg="Failed to convert given date and time string to Python datetime object,"
                                     "please specify string in 'dd/mm/yyyy hh:mm' format: %s" % to_native(e))
            schedule_task_spec = vim.scheduler.ScheduledTaskSpec()
            schedule_task_name = module.params['schedule_task_name'] or 'task_%s' % str(randint(10000, 99999))
            schedule_task_desc = module.params['schedule_task_description']
            if schedule_task_desc is None:
                schedule_task_desc = 'Schedule task for vm %s for ' \
                                     'operation %s at %s' % (vm.name, module.params['state'], scheduled_at)
            schedule_task_spec.name = schedule_task_name
            schedule_task_spec.description = schedule_task_desc
            schedule_task_spec.scheduler = vim.scheduler.OnceTaskScheduler()
            schedule_task_spec.scheduler.runAt = dt
            schedule_task_spec.action = vim.action.MethodAction()
            schedule_task_spec.action.name = powerstate[module.params['state']]
            schedule_task_spec.enabled = module.params['schedule_task_enabled']

            try:
                pyv.content.scheduledTaskManager.CreateScheduledTask(vm, schedule_task_spec)
                # As this is async task, we create scheduled task and mark state to changed.
                module.exit_json(changed=True)
            except vim.fault.InvalidName as e:
                module.fail_json(msg="Failed to create scheduled task %s for %s : %s" % (module.params.get('state'),
                                                                                         vm.name,
                                                                                         to_native(e.msg)))
            except vim.fault.DuplicateName as e:
                module.exit_json(changed=False, details=to_native(e.msg))
            except vmodl.fault.InvalidArgument as e:
                module.fail_json(msg="Failed to create scheduled task %s as specifications "
                                     "given are invalid: %s" % (module.params.get('state'),
                                                                to_native(e.msg)))
        else:
            # Check if a virtual machine is locked by a question
            if check_answer_question_status(vm) and module.params['answer']:
                try:
                    responses = make_answer_response(vm, module.params['answer'])
                    answer_question(vm, responses)
                except Exception as e:
                    module.fail_json(msg="%s" % e)

                # Wait until a virtual machine is unlocked
                while True:
                    if check_answer_question_status(vm) is False:
                        break

                result['changed'] = True
                result['instance'] = gather_vm_facts(pyv.content, vm)
            else:
                result = set_vm_power_state(pyv.content, vm, module.params['state'], module.params['force'], module.params['state_change_timeout'],
                                            module.params['answer'])
            result['answer'] = module.params['answer']
    else:
        id = module.params.get('uuid') or module.params.get('moid') or module.params.get('name')
        module.fail_json(msg="Unable to set power state for non-existing virtual machine : '%s'" % id)

    if result.get('failed') is True:
        module.fail_json(**result)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
