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
module: vmware_host_powerstate
short_description: Manages power states of host systems in vCenter
description:
- This module can be used to manage power states of host systems in given vCenter infrastructure.
- User can set power state to 'power-down-to-standby', 'power-up-from-standby', 'shutdown-host' and 'reboot-host'.
- State 'reboot-host', 'shutdown-host' and 'power-down-to-standby' are not supported by all the host systems.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  state:
    description:
    - Set the state of the host system.
    choices: [ 'power-down-to-standby', 'power-up-from-standby', 'shutdown-host', 'reboot-host' ]
    default: 'shutdown-host'
    type: str
  esxi_hostname:
    description:
    - Name of the host system to work with.
    - This is required parameter if O(cluster_name) is not specified.
    type: str
  cluster_name:
    description:
    - Name of the cluster from which all host systems will be used.
    - This is required parameter if O(esxi_hostname) is not specified.
    type: str
  force:
    description:
    - 'This parameter specify if the host should be proceeding with user defined powerstate
      regardless of whether it is in maintenance mode.'
    - 'If O(state=reboot-host) and O(force=true), then host system is rebooted regardless of whether it is in maintenance mode.'
    - 'If O(state=shutdown-host) and O(force=true), then host system is shutdown regardless of whether it is in maintenance mode.'
    - 'If O(state=power-down-to-standby) and O(force=true), then all powered off VMs will evacuated.'
    - 'Not applicable if O(state=power-up-from-standby).'
    type: bool
    default: false
  timeout:
    description:
    - 'This parameter defines timeout for O(state=power-down-to-standby) or O(state=power-up-from-standby).'
    - 'Ignored if O(state=reboot-host) or O(state=shutdown-host).'
    - 'This parameter is defined in seconds.'
    default: 600
    type: int
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Set the state of a host system to reboot
  community.vmware.vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: reboot-host
  delegate_to: localhost
  register: reboot_host

- name: Set the state of a host system to power down to standby
  community.vmware.vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    state: power-down-to-standby
  delegate_to: localhost
  register: power_down

- name: Set the state of all host systems from cluster to reboot
  community.vmware.vmware_host_powerstate:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    state: reboot-host
  delegate_to: localhost
  register: reboot_host
'''

RETURN = r'''
result:
    description: metadata about host system's state
    returned: always
    type: dict
    sample: {
        "esxi01": {
            "msg": "power down 'esxi01' to standby",
            "error": "",
        },
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, wait_for_task, TaskError
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VmwareHostPowerManager(PyVmomi):
    def __init__(self, module):
        super(VmwareHostPowerManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name')
        esxi_host_name = self.params.get('esxi_hostname')
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system with given configuration.")

    def ensure(self):
        """
        Function to manage internal state of host system

        """
        results = dict(changed=False, result=dict())
        state = self.params.get('state')
        force = self.params.get('force')
        timeout = self.params.get('timeout')
        host_change_list = []
        for host in self.hosts:
            changed = False
            task = None
            if not host.runtime.inMaintenanceMode and not force:
                self.module.fail_json(msg="Current host system '%s' is not in maintenance mode,"
                                          " please specify 'force' as True to proceed." % host.name)
            if host.runtime.connectionState == 'notResponding':
                self.module.fail_json(msg="Current host system '%s' can not be set in '%s'"
                                          " mode as the host system is not responding." % (host.name, state))

            results['result'][host.name] = dict(msg='', error='')
            if state == 'reboot-host' and not host.capability.rebootSupported:
                self.module.fail_json(msg="Current host '%s' can not be rebooted as the host system"
                                          " does not have capability to reboot." % host.name)
            elif state == 'shutdown-host' and not host.capability.shutdownSupported:
                self.module.fail_json(msg="Current host '%s' can not be shut down as the host system"
                                          " does not have capability to shut down." % host.name)
            elif state in ['power-down-to-standby', 'power-up-from-standby'] and not host.capability.standbySupported:
                self.module.fail_json(msg="Current host '%s' can not be '%s' as the host system"
                                          " does not have capability to standby supported." % (host.name, state))

            if state == 'reboot-host':
                if not self.module.check_mode:
                    task = host.RebootHost_Task(force)
                verb = "reboot '%s'" % host.name
            elif state == 'shutdown-host':
                if not self.module.check_mode:
                    task = host.ShutdownHost_Task(force)
                verb = "shutdown '%s'" % host.name
            elif state == 'power-down-to-standby':
                if not self.module.check_mode:
                    task = host.PowerDownHostToStandBy_Task(timeout, force)
                verb = "power down '%s' to standby" % host.name
            elif state == 'power-up-from-standby':
                if not self.module.check_mode:
                    task = host.PowerUpHostFromStandBy_Task(timeout)
                verb = "power up '%s' from standby" % host.name

            if not self.module.check_mode:
                try:
                    success, result = wait_for_task(task)
                    if success:
                        changed = True
                        results['result'][host.name]['msg'] = verb
                    else:
                        results['result'][host.name]['error'] = result
                except TaskError as task_error:
                    self.module.fail_json(msg="Failed to %s as host system due to : %s" % (verb,
                                                                                           str(task_error)))
                except Exception as generic_exc:
                    self.module.fail_json(msg="Failed to %s due to generic exception : %s" % (host.name,
                                                                                              to_native(generic_exc)))
            else:
                # Check mode
                changed = True
                results['result'][host.name]['msg'] = verb

            host_change_list.append(changed)

        if any(host_change_list):
            results['changed'] = True
        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        state=dict(type='str', default='shutdown-host',
                   choices=['power-down-to-standby', 'power-up-from-standby', 'shutdown-host', 'reboot-host']),
        esxi_hostname=dict(type='str', required=False),
        cluster_name=dict(type='str', required=False),
        force=dict(type='bool', default=False),
        timeout=dict(type='int', default=600),

    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True,
                           required_one_of=[
                               ['cluster_name', 'esxi_hostname'],
                           ]
                           )

    host_power_manager = VmwareHostPowerManager(module)
    host_power_manager.ensure()


if __name__ == '__main__':
    main()
