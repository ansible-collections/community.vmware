#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_scanhba
short_description: Rescan host HBA's and optionally refresh the storage system
description:
- This module can force a rescan of the hosts HBA subsystem which is needed when wanting to mount a new datastore.
- You could use this before using M(community.vmware.vmware_host_datastore) to mount a new datastore to ensure your device/volume is ready.
- You can also optionally force a Refresh of the Storage System in vCenter/ESXi Web Client.
- You can supply an esxi_hostname or a cluster_name
author:
- Michael Eaton (@michaeldeaton)
options:
  esxi_hostname:
    description:
    - ESXi hostname to Rescan the storage subsystem on.
    required: false
    type: str
  cluster_name:
    description:
    - Cluster name to Rescan the storage subsystem on (this will run the rescan task on each host in the cluster).
    required: false
    type: str
  rescan_hba:
    description:
    - Rescan all host bus adapters for new storage devices. Rescanning all adapters can be slow.
    required: false
    default: true
    type: bool
  refresh_storage:
    description:
    - Refresh the storage system in vCenter/ESXi Web Client for each host found
    required: false
    default: false
    type: bool
  rescan_vmfs:
    description:
    - Rescan all known storage devices for new VMFS volumes.
    required: false
    default: false
    type: bool
extends_documentation_fragment:
- vmware.vmware.base_options

'''

EXAMPLES = r'''
- name: Rescan HBA's for a given ESXi host and refresh storage system objects
  community.vmware.vmware_host_scanhba:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      esxi_hostname: '{{ inventory_hostname }}'
      refresh_storage: true
  delegate_to: localhost

- name: Rescan HBA's for a given cluster - all found hosts will be scanned
  community.vmware.vmware_host_scanhba:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      esxi_hostname: '{{ inventory_hostname }}'
      refresh_storage: true
  delegate_to: localhost

- name: Rescan for new VMFS Volumes in a given cluster, but do not scan for new Devices - all found hosts will be scanned
  community.vmware.vmware_host_scanhba:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      esxi_hostname: '{{ inventory_hostname }}'
      rescan_vmfs: true
      rescan_hba: false
  delegate_to: localhost

- name: Rescan HBA's for a given ESXi host and don't refresh storage system objects
  community.vmware.vmware_host_scanhba:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      esxi_hostname: '{{ inventory_hostname }}'
  delegate_to: localhost
'''

RETURN = r'''
result:
    description: return confirmation of requested host and updated / refreshed storage system
    returned: always
    type: dict
    sample: {
        "esxi01.example.com": {
            "rescaned_hba": "true",
            "refreshed_storage": "true",
            "rescaned_vmfs": "true"
        }
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class VmwareHbaScan(PyVmomi):
    def __init__(self, module):
        super(VmwareHbaScan, self).__init__(module)

    def scan(self):
        esxi_host_name = self.params.get('esxi_hostname', None)
        cluster_name = self.params.get('cluster_name', None)
        rescan_hba = self.params.get('rescan_hba', bool)
        refresh_storage = self.params.get('refresh_storage', bool)
        rescan_vmfs = self.params.get('rescan_vmfs', bool)
        hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        results = dict(changed=True, result=dict())

        if not hosts:
            self.module.fail_json(msg="Failed to find any hosts.")

        for host in hosts:
            results['result'][host.name] = dict()
            if rescan_hba is True:
                host.configManager.storageSystem.RescanAllHba()

            if refresh_storage is True:
                host.configManager.storageSystem.RefreshStorageSystem()

            if rescan_vmfs is True:
                host.configManager.storageSystem.RescanVmfs()

            results['result'][host.name]['rescaned_hba'] = rescan_hba
            results['result'][host.name]['refreshed_storage'] = refresh_storage
            results['result'][host.name]['rescaned_vmfs'] = rescan_vmfs

        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=False),
        cluster_name=dict(type='str', required=False),
        rescan_hba=dict(type='bool', default=True, required=False),
        refresh_storage=dict(type='bool', default=False, required=False),
        rescan_vmfs=dict(type='bool', default=False, required=False)
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=False
    )

    hbascan = VmwareHbaScan(module)
    hbascan.scan()


if __name__ == '__main__':
    main()
