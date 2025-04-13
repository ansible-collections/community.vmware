#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2022, Swisscom (Schweiz) AG
# Author(s): Olivia Luetolf <olivia.luetolf@swisscom.com>
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_cluster_dpm
short_description: Manage Distributed Power Management (DPM) on VMware vSphere clusters
description:
    - Manages DPM on VMware vSphere clusters.
author:
- Olivia Luetolf (@olilu)
deprecated:
  removed_in: 6.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880).
  alternative: Use M(vmware.vmware.cluster_dpm) instead.
options:
    cluster_name:
      description:
      - The name of the cluster to be managed.
      type: str
      required: true
    datacenter:
      description:
      - The name of the datacenter.
      type: str
      required: true
      aliases: [ datacenter_name ]
    enable_dpm:
      description:
      - Whether to enable DPM.
      type: bool
      default: false
    default_dpm_behaviour:
      description:
      - Whether dpm should be automated or manual
      type: str
      default: automated
      choices: [ automated, manual ]
    host_power_action_rate:
      description:
      - specify host power action rate
      - V(1) is the lowest and V(5) the highest
      type: int
      default: 3
      choices: [1, 2, 3, 4, 5]
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Enable DPM
  community.vmware.vmware_cluster_dpm:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable_dpm: true
    default_dpm_behaviour: automated
    host_power_action_rate: 2
  delegate_to: localhost

'''

RETURN = r'''
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    TaskError,
    find_datacenter_by_name,
    wait_for_task
)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VMwareCluster(PyVmomi):
    def __init__(self, module):
        super(VMwareCluster, self).__init__(module)
        self.cluster_name = module.params['cluster_name']
        self.datacenter_name = module.params['datacenter']
        self.enable_dpm = module.params['enable_dpm']
        self.default_dpm_behaviour = module.params['default_dpm_behaviour']
        self.host_power_action_rate = [5, 4, 3, 2, 1][module.params['host_power_action_rate'] - 1]
        self.datacenter = None
        self.cluster = None

        self.datacenter = find_datacenter_by_name(self.content, self.datacenter_name)
        if self.datacenter is None:
            self.module.fail_json(msg="Datacenter %s does not exist." % self.datacenter_name)

        self.cluster = self.find_cluster_by_name(cluster_name=self.cluster_name, datacenter_name=self.datacenter)
        if self.cluster is None:
            self.module.fail_json(msg="Cluster %s does not exist." % self.cluster_name)

    def check_dpm_config_diff(self):
        """
        Check DRS configuration diff
        Returns: True if there is diff, else False

        """
        dpm_config = self.cluster.configurationEx.dpmConfigInfo
        change_message = None
        changes = False

        if dpm_config is None or dpm_config.enabled != self.enable_dpm:
            change_message = 'DPM enabled status changes'
            changes = True
            return changes, change_message
        elif self.enable_dpm:
            if dpm_config.hostPowerActionRate != self.host_power_action_rate or dpm_config.defaultDpmBehavior != self.default_dpm_behaviour:
                change_message = 'DPM Host Power Action Rate and/or default DPM behaviour change.'
                changes = True
                return changes, change_message

        return changes, change_message

    def configure_dpm(self):
        """
        Manage DRS configuration

        """
        changed, result = self.check_dpm_config_diff()

        if changed:
            if not self.module.check_mode:
                cluster_config_spec = vim.cluster.ConfigSpecEx()
                cluster_config_spec.dpmConfig = vim.cluster.DpmConfigInfo()
                cluster_config_spec.dpmConfig.enabled = self.enable_dpm
                cluster_config_spec.dpmConfig.defaultDpmBehavior = self.default_dpm_behaviour
                cluster_config_spec.dpmConfig.hostPowerActionRate = self.host_power_action_rate

                try:
                    task = self.cluster.ReconfigureComputeResource_Task(cluster_config_spec, True)
                    changed = wait_for_task(task)[0]
                except vmodl.RuntimeFault as runtime_fault:
                    self.module.fail_json(msg=to_native(runtime_fault.msg))
                except vmodl.MethodFault as method_fault:
                    self.module.fail_json(msg=to_native(method_fault.msg))
                except TaskError as task_e:
                    self.module.fail_json(msg=to_native(task_e))
                except Exception as generic_exc:
                    self.module.fail_json(msg="Failed to update cluster"
                                              " due to generic exception %s" % to_native(generic_exc))
            else:
                changed = True

        self.module.exit_json(changed=changed, result=result)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        cluster_name=dict(type='str', required=True),
        datacenter=dict(type='str', required=True, aliases=['datacenter_name']),
        enable_dpm=dict(type='bool', default=False),
        default_dpm_behaviour=dict(type='str', choices=['automated', 'manual'], default='automated'),
        host_power_action_rate=dict(type='int', choices=[1, 2, 3, 4, 5], default=3)
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    vmware_cluster_dpm = VMwareCluster(module)
    vmware_cluster_dpm.configure_dpm()


if __name__ == '__main__':
    main()
