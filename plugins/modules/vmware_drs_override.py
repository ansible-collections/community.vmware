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
    name:
      description:
      - Name of the VM for which the DRS override is set.
      - This is required if O(uuid) or O(moid) is not supplied.
      type: str
      aliases: [ vm_name ]
    uuid:
      description:
      - UUID of the instance to manage if known, this is VMware's unique identifier.
      - This is required if O(name) or O(moid) is not supplied.
      type: str
    use_instance_uuid:
      description:
      - Whether to use the VMware instance UUID rather than the BIOS UUID.
      default: false
      type: bool
    moid:
      description:
      - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
      - This is required if O(name) or O(uuid) is not supplied.
      type: str
    folder:
      description:
      - Destination folder, absolute or relative path to find an existing guest.
      - The folder should include the datacenter. ESXi server's datacenter is ha-datacenter.
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
      - The datacenter name to which virtual machine belongs to.
     type: str
    drs_behavior:
        description:
            - Desired DRS behavior for the VM.
            - Use 'absent' to remove the DRS override.
        choices: ['absent', 'manual', 'partiallyAutomated', 'fullyAutomated']
        default: 'manual'
        type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation
author:
    - Sergey Goncharov (@svg1007)
    - Michał Gąsior (@Rogacz)
'''

EXAMPLES = '''
- name: Set DRS behavior for a VM
  community.vmware.vmware_drs_override:
    hostname: "vcenter.example.com"
    username: "administrator@vsphere.local"
    password: "yourpassword"
    port: 443
    validate_certs: False
    name: "my_vm_name"
    drs_behavior: "manual"
  delegate_to: localhost

- name: Remove DRS override for a VM
  community.vmware.vmware_drs_override:
    hostname: "vcenter.example.com"
    username: "administrator@vsphere.local"
    password: "yourpassword"
    moid: vm-42
    drs_behavior: "absent"
  delegate_to: localhost
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
        self.drs_behavior = module.params['drs_behavior']
        self.vm = self.get_vm()
        if not self.vm:
            self.module.fail_json(msg=f"VM '{self.params['name']}' not found.")
        if not self.is_vcenter():
            self.module.fail_json(msg="DRS configuration is only supported in vCenter environments.")

    def set_drs_override(self):
        cluster = self.vm.runtime.host.parent
        if not cluster:
            self.module.fail_json(msg="VM is not in a Cluster.")

        # Check current DRS settings
        existing_config = next((config for config in cluster.configuration.drsVmConfig if config.key == self.vm), None)
        if existing_config:
            if existing_config.behavior == self.drs_behavior:
                # Nothing to do
                self.module.exit_json(changed=False, msg="DRS behavior is already set to the desired state.")
            if self.drs_behavior == 'absent':
                # Remove the DRS override
                drs_vm_config_spec = vim.cluster.DrsVmConfigSpec(
                    operation=vim.option.ArrayUpdateSpec.Operation.remove,
                    removeKey=self.vm,
                )
                msg = "DRS override removed successfully."
            else:
                # Update the DRS override
                drs_vm_config_spec = vim.cluster.DrsVmConfigSpec(
                    operation=vim.option.ArrayUpdateSpec.Operation.edit,
                    info=vim.cluster.DrsVmConfigInfo(
                        key=self.vm,
                        enabled=True,
                        behavior=self.drs_behavior,
                    ),
                )
                msg = "DRS override updated successfully."
        else:
            if self.drs_behavior == 'absent':
                # Nothing to do
                self.module.exit_json(changed=False, msg="DRS override is already absent.")
            # Define the DRS override as it does not exist
            drs_vm_config_spec = vim.cluster.DrsVmConfigSpec(
                operation=vim.option.ArrayUpdateSpec.Operation.add,
                info=vim.cluster.DrsVmConfigInfo(
                    key=self.vm,
                    enabled=True,
                    behavior=self.drs_behavior,
                ),
            )
            msg = "DRS override applied successfully."

        if not self.module.check_mode:
            # Apply the cluster reconfiguration if not in check mode
            cluster_config_spec = vim.cluster.ConfigSpec()
            cluster_config_spec.drsVmConfigSpec = [drs_vm_config_spec]
            try:
                task = cluster.ReconfigureCluster_Task(spec=cluster_config_spec, modify=True)
                wait_for_task(task)
            except vmodl.MethodFault as error:
                self.module.fail_json(msg=f"Failed to set DRS override: {error.msg}")

        self.module.exit_json(changed=True, msg=msg)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update({
        'name': {'type': 'str', 'aliases': ['vm_name']},
        'uuid': {'type': 'str'},
        'moid': {'type': 'str'},
        'use_instance_uuid': {'type': 'bool', 'default': False},
        'folder': {'type': 'str'},
        'datacenter': {'type': 'str'},
        'drs_behavior': {'type': 'str', 'choices': ['absent', 'manual', 'partiallyAutomated', 'fullyAutomated'], 'default': 'manual'},
    })

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['name', 'uuid', 'moid'],
        ],
    )

    if module.params['folder']:
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    drs_override = VmwareDrsOverride(module)
    drs_override.set_drs_override()


if __name__ == '__main__':
    main()
