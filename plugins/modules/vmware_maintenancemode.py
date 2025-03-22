#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, VMware, Inc.
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_maintenancemode
deprecated:
  removed_in: 7.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.esxi_maintenance_mode) instead.
short_description: Place a host into maintenance mode
description:
    - This module can be used for placing a ESXi host into maintenance mode.
    - Support for VSAN compliant maintenance mode when selected.
author:
- Jay Jahns (@jjahns) <jjahns@vmware.com>
- Abhijeet Kasurde (@Akasurde)
options:
    esxi_hostname:
        description:
            - Name of the host as defined in vCenter.
        required: true
        type: str
    vsan:
        description:
            - Specify which VSAN compliant mode to enter.
        choices:
            - 'ensureObjectAccessibility'
            - 'evacuateAllData'
            - 'noAction'
        required: false
        aliases: [ 'vsan_mode' ]
        type: str
    evacuate:
        description:
            - If set to V(true), evacuate all powered off VMs.
        default: false
        required: false
        type: bool
    timeout:
        description:
            - Specify a timeout for the operation.
        required: false
        default: 0
        type: int
    state:
        description:
            - Enter or exit maintenance mode.
        choices:
            - present
            - absent
        default: present
        required: false
        type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Enter VSAN-Compliant Maintenance Mode
  community.vmware.vmware_maintenancemode:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    vsan: ensureObjectAccessibility
    evacuate: true
    timeout: 3600
    state: present
  delegate_to: localhost
'''

RETURN = r'''
hostsystem:
    description: Name of vim reference
    returned: always
    type: str
    sample: "'vim.HostSystem:host-236'"
hostname:
    description: Name of host in vCenter
    returned: always
    type: str
    sample: "esxi.local.domain"
status:
    description: Action taken
    returned: always
    type: str
    sample: "ENTER"
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, TaskError, vmware_argument_spec, wait_for_task
from ansible.module_utils._text import to_native


class VmwareMaintenanceMgr(PyVmomi):
    def __init__(self, module):
        super(VmwareMaintenanceMgr, self).__init__(module)
        self.esxi_hostname = self.module.params.get('esxi_hostname')
        self.vsan = self.module.params.get('vsan', None)
        self.host = self.find_hostsystem_by_name(host_name=self.esxi_hostname)
        if not self.host:
            self.module.fail_json(msg='Host %s not found in vCenter' % self.esxi_hostname)

    def EnterMaintenanceMode(self):
        if self.host.runtime.inMaintenanceMode:
            self.module.exit_json(changed=False,
                                  hostsystem=str(self.host),
                                  hostname=self.esxi_hostname,
                                  status='NO_ACTION',
                                  msg='Host %s already in maintenance mode' % self.esxi_hostname)

        spec = vim.host.MaintenanceSpec()

        if self.vsan:
            spec.vsanMode = vim.vsan.host.DecommissionMode()
            spec.vsanMode.objectAction = self.vsan

        try:
            if not self.module.check_mode:
                task = self.host.EnterMaintenanceMode_Task(self.module.params['timeout'],
                                                           self.module.params['evacuate'],
                                                           spec)

                success, result = wait_for_task(task)
            else:
                success = True

            self.module.exit_json(changed=success,
                                  hostsystem=str(self.host),
                                  hostname=self.esxi_hostname,
                                  status='ENTER',
                                  msg='Host %s entered maintenance mode' % self.esxi_hostname)

        except TaskError as e:
            self.module.fail_json(msg='Host %s failed to enter maintenance mode due to %s' % (self.esxi_hostname, to_native(e)))

    def ExitMaintenanceMode(self):
        if not self.host.runtime.inMaintenanceMode:
            self.module.exit_json(changed=False,
                                  hostsystem=str(self.host),
                                  hostname=self.esxi_hostname,
                                  status='NO_ACTION',
                                  msg='Host %s not in maintenance mode' % self.esxi_hostname)

        try:
            if not self.module.check_mode:
                task = self.host.ExitMaintenanceMode_Task(self.module.params['timeout'])

                success, result = wait_for_task(task)
            else:
                success = True

            self.module.exit_json(changed=success,
                                  hostsystem=str(self.host),
                                  hostname=self.esxi_hostname,
                                  status='EXIT',
                                  msg='Host %s exited maintenance mode' % self.esxi_hostname)
        except TaskError as e:
            self.module.fail_json(msg='Host %s failed to exit maintenance mode due to %s' % (self.esxi_hostname, to_native(e)))


def main():
    spec = vmware_argument_spec()
    spec.update(dict(esxi_hostname=dict(type='str', required=True),
                     vsan=dict(type='str',
                               choices=['ensureObjectAccessibility',
                                        'evacuateAllData',
                                        'noAction'],
                               aliases=['vsan_mode'],
                               ),
                     evacuate=dict(type='bool', default=False),
                     timeout=dict(default=0, type='int'),
                     state=dict(required=False, default='present', choices=['present', 'absent'])
                     )
                )

    module = AnsibleModule(argument_spec=spec,
                           supports_check_mode=True)

    host_maintenance_mgr = VmwareMaintenanceMgr(module=module)

    if module.params['state'] == 'present':
        host_maintenance_mgr.EnterMaintenanceMode()
    elif module.params['state'] == 'absent':
        host_maintenance_mgr.ExitMaintenanceMode()


if __name__ == '__main__':
    main()
