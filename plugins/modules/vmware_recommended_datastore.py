#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_recommended_datastore
short_description: Returns the recommended datastore from a SDRS-enabled datastore cluster
description:
- This module provides the recommended datastores from a datastore cluster only if the SDRS is enabled for the specified datastore cluster
author:
- @MalfuncEddie - original code of Abhijeet Kasurde (@Akasurde)
notes:
- Tested on vSphere 6.7
requirements:
- python >= 2.6
- PyVmomi
options:
  datastore_cluster_name:
    description:
    - Name of the datastore cluster
    - This is required
    type: str
    required: True
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''


EXAMPLES = r'''
- name: Get recommended datastore from a Storage DRS-enabled datastore cluster
  community.vmware.vmware_recommended_datastore:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_cluster_name: "{{ datastore_cluster_name }}"
  delegate_to: localhost
  register: recommended_ds
'''


RETURN = r'''
vmware_recommended_datastore:
  description: metadata about the recommended datastore
  returned: always
  type: dict
  sample: {
    'changed': False,
    'recommended_datastore': 'datastorecluster-01',
    'failed': False
  }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec, find_obj


class VmwareDatastoreClusterInfo(PyVmomi):
    def __init__(self, module):
        super(VmwareDatastoreClusterInfo, self).__init__(module)
        datastore_cluster_name = self.params.get('datastore_cluster')
        datastore_cluster = find_obj(self.content, [vim.StoragePod], datastore_cluster_name)
        datastore_name = self.get_recommended_datastore(datastore_cluster_obj=datastore_cluster)
        result = dict(
          changed=False,
          recommended_datastore=datastore_name
        )
        self.module.exit_json(**result)


    def get_recommended_datastore(self, datastore_cluster_obj=None):
        """
        Function to return Storage DRS recommended datastore from datastore cluster
        Args:
            datastore_cluster_obj: datastore cluster managed object
        Returns: Name of recommended datastore from the given datastore cluster
        """

        if datastore_cluster_obj is None:
            return None

        # Check if Datastore Cluster provided by user is SDRS ready
        sdrs_status = datastore_cluster_obj.podStorageDrsEntry.storageDrsConfig.podConfig.enabled

        if sdrs_status:
            # We can get storage recommendation only if SDRS is enabled on given datastorage cluster
            pod_sel_spec = vim.storageDrs.PodSelectionSpec()
            pod_sel_spec.storagePod = datastore_cluster_obj
            storage_spec = vim.storageDrs.StoragePlacementSpec()
            storage_spec.podSelectionSpec = pod_sel_spec
            storage_spec.type = 'create'
            try:
                rec = self.content.storageResourceManager.RecommendDatastores(storageSpec=storage_spec)
                rec_action = rec.recommendations[0].action[0]
                return rec_action.destination.name
            except Exception:
                # There is some error so we fall back to general workflow
                pass

        datastore = None
        datastore_freespace = 0
        for ds_elem in datastore_cluster_obj.childEntity:
            if isinstance(ds_elem, vim.Datastore) and ds_elem.summary.freeSpace > datastore_freespace:
                # If datastore field is provided, filter destination datastores
                if not self.is_datastore_valid(datastore_obj=ds_elem):
                    continue

                datastore = ds_elem
                datastore_freespace = ds_elem.summary.freeSpace

        if datastore:
            return datastore.name
        return None


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        datastore_cluster_name=dict(type='str', required=True)
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    VmwareDatastoreClusterInfo(module)


if __name__ == '__main__':
    main()
