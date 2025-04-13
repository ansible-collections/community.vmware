#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

DOCUMENTATION = '''
---
module: vmware_drs_override
version_added: '5.2.0'
short_description: Configure DRS behavior for a specific VM in vSphere
description:
    - This module allows setting a DRS behavior override for individual VMs within a DRS-enabled VMware vSphere cluster.
options:
    vm_name:
        description:
            - Name of the VM for which the DRS override is set.
        required: true
        type: str
    drs_behavior:
        description:
            - Desired DRS behavior for the VM.
        choices: ['manual', 'partiallyAutomated', 'fullyAutomated']
        default: 'manual'
        type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation
author:
    - Sergey Goncharov (@svg1007)
'''

EXAMPLES = '''
- name: Set DRS behavior for a VM
  vmware_drs_override:
    hostname: "vcenter.example.com"
    username: "administrator@vsphere.local"
    password: "yourpassword"
    port: 443
    validate_certs: False
    vm_name: "my_vm_name"
    drs_behavior: "manual"
'''

RETURN = '''
changed:
    description: Whether the DRS behavior was changed.
    type: bool
    returned: always
msg:
    description: A message describing the outcome of the task.
    type: str
    returned: always
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import wait_for_task, PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VmwareDrsOverride(PyVmomi):
    def __init__(self, module):
        super(VmwareDrsOverride, self).__init__(module)
        self.vm_name = self.params.get('vm_name', None)
        self.drs_behavior = module.params['drs_behavior']
        self.params['name'] = self.vm_name
        self.vm = self.get_vm()
        if not self.vm:
            self.module.fail_json(msg="VM '%s' not found." % self.vm_name)

        if not self.is_vcenter():
            self.module.fail_json(msg="DRS configuration is only supported in vCenter environments.")

    def set_drs_override(self):
        cluster = self.vm.runtime.host.parent

        # Check current DRS settings
        existing_config = next((config for config in cluster.configuration.drsVmConfig if config.key == self.vm), None)
        if existing_config and existing_config.behavior == self.drs_behavior:
            self.module.exit_json(changed=False, msg="DRS behavior is already set to the desired state.")

        # Create DRS VM config spec
        drs_vm_config_spec = vim.cluster.DrsVmConfigSpec(
            operation='add',
            info=vim.cluster.DrsVmConfigInfo(
                key=self.vm,
                enabled=True,
                behavior=self.drs_behavior
            )
        )

        # Apply the cluster reconfiguration
        cluster_config_spec = vim.cluster.ConfigSpec()
        cluster_config_spec.drsVmConfigSpec = [drs_vm_config_spec]
        try:
            task = cluster.ReconfigureCluster_Task(spec=cluster_config_spec, modify=True)
            wait_for_task(task)
            self.module.exit_json(changed=True, msg="DRS override applied successfully.")
        except vmodl.MethodFault as error:
            self.module.fail_json(msg="Failed to set DRS override: %s" % error.msg)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        vm_name=dict(type='str', required=True),
        drs_behavior=dict(type='str', choices=['manual', 'partiallyAutomated', 'fullyAutomated'], default='manual')
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    drs_override = VmwareDrsOverride(module)
    drs_override.set_drs_override()


if __name__ == '__main__':
    main()
