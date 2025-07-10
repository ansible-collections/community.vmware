#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2024, Fernando Mendieta <fernandomendietaovejero@gmail.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_all_snapshots_info
short_description: Gathers information about all snapshots across virtual machines in a specified vmware datacenter
description:
- This module collects detailed information of all the snapshots of the datacenter, can be used with filter options
author:
- Fernando Mendieta (@valkiriaaquatica)
options:
  datacenter:
    description:
      - The name of the datacenter to gather snapshot information from. You can get it in the vmware UI.
    required: true
    type: str
  filters:
    description:
      - Optional filters to apply to the snapshot data being gathered, you can apply one or more.
      - Filters are applied based on the variable match_type specified. If match_type exact, filters require exact matches.
      - On the other hand when match_type includes it gets the values that contain that value.
      - Available filter options creation_time, description, folder, id, name, quiesced, state, vm_name.
      - Multiple filters can be applied the snapshot must meet all filter criteria to be included in the results.
    required: false
    type: dict
    default: {}
  match_type:
    description:
      - Indicates whether the filter match should be exact or includes.
      - For example when you want to get all the snapshots that contain in their name the word test you place the filter name test and the match_type includes.
      - For example when you want to get all snapshots that are in state poweredOn you skip the match_type default is exact  or you write match_type exact.
    required: false
    type: str
    choices: ['exact', 'includes']
    default: exact
extends_documentation_fragment:
- vmware.vmware.base_options
'''

EXAMPLES = r'''
  - name: Gather information about all snapshots in VMware vCenter
    vmware_all_snapshots_info:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      validate_certs: no
      datacenter: '{{ datacenter_name }}'
    delegate_to: localhost
  - name: Gather information of a snapshot with filters applied and match_type in exacts.
    vmware_all_snapshots_info:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      validate_certs: yes
      datacenter: '{{ datacenter_name }}'
      filters:
        state: "poweredOn"
        vm_name: "you_marchine_name"
    delegate_to: localhost
  - name: Gather information of snapshots that in their name contain the "test" in their name.
    vmware_all_snapshots_info:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      validate_certs: yes
      datacenter: '{{ datacenter_name }}'
      match_type: "includes"
      filters:
        name: "test"
    delegate_to: localhost
'''

RETURN = r'''
vmware_all_snapshots_info:
  description: A list of all snapshots information across all virtual machines in the specified datacenter
  returned: always
  type: list
  elements: dict
  contains:
    vm_name:
      description: The name of the virtual machine that appears in the iu.
      type: str
      returned: always
    folder:
      description: The folder path of the virtual machine in the datacenter, normally is vm
      type: str
      returned: always
    name:
      description: The name of the snapshot
      type: str
      returned: always
    description:
      description: The description of the snapshot.
      type: str
      returned: when it exists because depends if it has or not
    creation_time:
      description: The time the snapshot was created
      type: str
      returned: always
    state:
      description: The state of the virtual machine at the snapshot (powered on/off)
      type: str
      returned: always
    id:
      description: The unique identifier of the snapshot
      type: int
      returned: always
    quiesced:
      description: Indicates if the snapshot was created with the virtual machines file system quiesced
      type: bool
      returned: always
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, list_snapshots_recursively
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec

try:
    from pyVmomi import vim
except ImportError:
    pass


class VMwareSnapshotInfo(PyVmomi):
    def __init__(self, module):
        super(VMwareSnapshotInfo, self).__init__(module)

    def list_snapshots(self, vm):
        return (
            list_snapshots_recursively(vm.snapshot.rootSnapshotList)
            if vm.snapshot
            else []
        )

    def get_all_vms(self, datacenter):
        content = self.content

        datacenter_obj = self.find_datacenter_by_name(datacenter)
        container = content.viewManager.CreateContainerView(
            datacenter_obj, [vim.VirtualMachine], True
        )
        vms = container.view
        container.Destroy()
        return vms

    def gather_snapshots_info(self, filters, match_type, datacenter=None):
        snapshot_data = []
        for vm in self.get_all_vms(datacenter):
            for snapshot in self.list_snapshots(vm):
                snapshot_info = {
                    "vm_name": vm.name,
                    "folder": vm.parent.name,
                    **snapshot,
                }
                if self.passes_filters(snapshot_info, filters, match_type):
                    snapshot_data.append(snapshot_info)
        return snapshot_data

    def passes_filters(self, snapshot_info, filters, match_type):
        for key, value in filters.items():
            if key not in snapshot_info:
                continue
            actual_value = str(snapshot_info[key]).lower()
            desired_value = str(value).lower()

            if match_type == "exact" and actual_value != desired_value:
                return False
            elif match_type == "includes" and desired_value not in actual_value:
                return False
        return True


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(required=True, type="str"),
        filters=dict(required=False, type="dict", default={}),
        match_type=dict(
            required=False, type="str", choices=["exact", "includes"], default="exact"
        ),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    vmware_snapshot_info = VMwareSnapshotInfo(module)
    datacenter = module.params.get("datacenter")
    filters = module.params.get("filters")
    match_type = module.params.get("match_type")
    all_snapshots = vmware_snapshot_info.gather_snapshots_info(filters, match_type, datacenter)
    module.exit_json(changed=False, vmware_all_snapshots_info=all_snapshots)


if __name__ == "__main__":
    main()
