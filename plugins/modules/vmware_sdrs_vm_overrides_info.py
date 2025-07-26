#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Lionel Sutcliffe <sutcliffe.lionel@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: vmware_sdrs_vm_overrides_info
short_description: Check for VM overrides in a SDRS datastore cluster
description:
    - This module can be used to check if VM overrides exist in a SDRS enabled datastore cluster in a given VMware environment.
    - All parameters and VMware object values are case sensitive.
author:
-  Lionel Sutcliffe (@sudo-lupus)
options:
    datastore_cluster_name:
      description:
      - The name of the datastore cluster.
      required: true
      type: str
extends_documentation_fragment:
- vmware.vmware.base_options

"""

EXAMPLES = r"""
- name: Check if SDRS Overrides exist in datastore cluster
  community.vmware.vmware_sdrs_vm_overrides_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_cluster_name: '{{ datastore_cluster_name }}'
  delegate_to: localhost
"""

RETURN = r"""
result:
    description: information about datastore clusters with VMs with SDRS enabled
    returned: always
    type: dict
    sample: {
        "changed": false,
        "result": {
            "vm_overrides": {
                "VM_1": {
                    "sdrs_enabled_status": false, "vm_behavior": null
                    },
                 "VM_2": {
                    "sdrs_enabled_status": false, "vm_behavior": null
                    }
                }
            }
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class VMwareDatastoreClusterManager(PyVmomi):
    def __init__(self, module):
        super(VMwareDatastoreClusterManager, self).__init__(module)
        self.datastore_cluster_name = self.params.get("datastore_cluster_name")
        self.datastore_cluster_obj = self.find_datastore_cluster_by_name(
            self.datastore_cluster_name
        )

    def check_vm_overrides(self):
        """
        Check SDRS status of VMs in datastore cluster
        """
        results = dict(changed=False, result={})

        vm_configs = list(self.datastore_cluster_obj.podStorageDrsEntry.storageDrsConfig.vmConfig)
        vm_overrides = dict()

        for vm in vm_configs:
            if vm.enabled is not None or vm.behavior is not None:
                vm_overrides[vm.vm.name] = {}
                vm_overrides[vm.vm.name]["sdrs_enabled_status"] = vm.enabled
                vm_overrides[vm.vm.name]["vm_behavior"] = vm.behavior

        if vm_overrides.keys():
            results["result"] = dict(vm_overrides=vm_overrides)
        else:
            results["result"] = ""

        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        dict(
            datastore_cluster_name=dict(type="str", required=True),
        )
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    datastore_cluster_mgr = VMwareDatastoreClusterManager(module)
    datastore_cluster_mgr.check_vm_overrides()


if __name__ == "__main__":
    main()
