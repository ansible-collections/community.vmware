#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, sky-joker
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: vmware_host_datastore_resize
short_description: Resize the vmfs datastore capacity
author:
  - sky-joker (@sky-joker)
description:
  - This module can be resized the vmfs datastore capacity.
notes:
  - Supports C(check_mode).
  - In VCSA and ESXi will be displayed slightly smaller capacity size than you specified the size.
    For example, if you specified 5GB to resize_gb, the capacity will be expanded 4.75GB in VCSA and ESXi host.
    This module can't compare correctly between to be expanded block size and the now capacity block size
    because a method doesn't find to get the accurate block size to expand.
    So, please cautions, If already expanded 4.75GB, an error will happen if you specified 5GB to resize
    because VCSA and ESXi recognize 5GB is 4.75GB.
requirements:
  - python >= 3.6
  - PyVmomi
version_added: '1.12.0'
options:
  esxi_hostname:
    description:
      - Name of the host system to work with.
    type: str
    required: True
  datastore:
    description:
      - Name of the datastore to resize a capacity.
    type: str
    required: True
  expand:
    description:
      - Expand the capacity base on existing datastore free capacity.
      - If not free capacity, the datastore capacity can't be expanded.
    suboptions:
      partition_number:
        description:
          - A partition number you'd like to expand the partition.
        type: int
        default: 1
        aliases:
          - partition
      resize_gb:
        description:
          - The resize size of the datastore capacity.
          - If you'd like to specify capacity size to expand, should be specified the integer in gigabyte size.
          - If you'd like to expand using all free capacity, resize_gb set to C(all).
          - The I(resize_gb) can be specified only the value either C(all) or integer.
        type: str
        required: True
    type: dict
    required: True
extends_documentation_fragment:
  - community.vmware.vmware.documentation
"""

EXAMPLES = r"""
- name: Expand the partition number 1 in the datastore capacity up to 20GB
  community.vmware.vmware_host_datastore_resize:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    datastore: "{{ datastore }}"
    expand:
      partition_number: 1
      resize_gb: 20

- name: Expand the partition number 1 in the datastore capacity using free all capacity up to
  community.vmware.vmware_host_datastore_resize:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    esxi_hostname: "{{ esxi1 }}"
    datastore: "{{ datastore }}"
    expand:
      partition_number: 1
      resize_gb: all
"""

RETURN = r"""
resized_datastore_info:
  description:
    - dict of the resized datastore capacity information.
  returned: changed
  type: dict
  sample: >-
    {
        "changed": true,
        "failed": false,
        "resized_datastore_info": {
            "capacity": 31943819264,
            "free_space": 30434918400,
            "name": "DS1"
        }
    }
"""

try:
    from pyVmomi import vim
except ImportError:
    pass

import math
import re
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec
from ansible.module_utils.basic import AnsibleModule


class VMwareHostDatastoreResize(PyVmomi):
    def __init__(self, module):
        super(VMwareHostDatastoreResize, self).__init__(module)
        self.esxi_hostname = self.params['esxi_hostname']
        self.datastore = self.params['datastore']
        self.expand = self.params['expand']

        if not re.match(r'all|[0-9]+', self.expand["resize_gb"]):
            self.module.fail_json(msg="resize_gb can be specified only the value either all or int.")
        if re.match(r'[0-9]+', self.expand["resize_gb"]):
            self.expand["resize_gb"] = int(self.expand["resize_gb"])

        self.host_obj = self.find_hostsystem_by_name(self.esxi_hostname)
        if not self.host_obj:
            self.module.fail_json(msg="Failed to find host system: %s" % self.esxi_hostname)

        # Find attached datastore at host.
        self.datastore_obj = None
        for datastore in self.host_obj.datastore:
            if datastore.name == self.datastore:
                self.datastore_obj = datastore
                break
        if not self.datastore_obj:
            self.module.fail_json(msg="Failed to find datastore: %s" % self.datastore)

        if not hasattr(self.datastore_obj.info, "vmfs"):
            self.module.fail_json(msg="The datastore isn't vmfs. this module can resize vmfs only.")

        # Config Manager of hostsystem
        self.cnf_mng = self.host_obj.configManager
        self.result = dict(changed=False)

    def get_expand_partition(self, vmfs_ds_options):
        """
        Get information that to expand the datastore capacity.

        Args:
            vmfs_ds_options (list): list of datastore partition.

        Returns:
            - expand_disk_info (dict): information to expand the datastore capacity.
        """
        expand_disk_info = {}
        for vmfs_ds_option in vmfs_ds_options:
            for partition in vmfs_ds_option.info.layout.partition:
                if partition.partition == self.expand["partition_number"]:
                    expand_disk_info.update({
                        "vmfs_datastore_expand_spec": vmfs_ds_option.spec,
                        "scsi_disk_partition": vmfs_ds_option.spec.extent,
                        "disk_partition_block_range": partition
                    })
                    return expand_disk_info

        return expand_disk_info

    def expand_datastore(self, vmfs_datastore_expand_spec):
        """
        A datastore will be expanded.

        Args:
            vmfs_datastore_expand_spec (vim.host.VmfsDatastoreExpandSpec): data object to expand the datastore capacity.

        Returns:
            - resized_datastore (vim.Datastore): datastore managed object.
        """
        resized_datastore = None
        try:
            resized_datastore = self.cnf_mng.datastoreSystem.ExpandVmfsDatastore(datastore=self.datastore_obj,
                                                                                 spec=vmfs_datastore_expand_spec)
        except Exception as e:
            # It seems that the resize_block_size changes to suitable value by internal processing in the ExpandVmfsDatastore.
            # For example, if you specified 5GB to resize_gb, will be expanded 4.75GB in VCSA and ESXi host.
            # This module can't compare correctly the datastore size(block size) before and after because I don't find a method
            # to get the accurate block size to expand.
            # So, if you specified the same value the existing datastore, I implemented this error will happen.
            self.module.fail_json(msg="%s Maybe you specified the same capacity the existing datastore." % to_native(e.msg))

        return resized_datastore

    def generate_return_value(self, resized_datastore):
        """
        Generate information of the resized datastore capacity.

        Args:
            resized_datastore (vim.Datastore): resized datastore managed object.

        Returns:
            - resized_datastore_info (dict): summarized the resized datastore information.
        """
        resized_datastore_info = {
            "name": resized_datastore.summary.name,
            "capacity": resized_datastore.summary.capacity,
            "free_space": resized_datastore.summary.freeSpace
        }

        return resized_datastore_info

    def execute(self):
        if self.module.check_mode:
            self.result["changed"] = True
            self.module.exit_json(**self.result)

        if self.expand:
            vmfs_ds_options = self.cnf_mng.datastoreSystem.QueryVmfsDatastoreExpandOptions(self.datastore_obj)

            # If not found vmfs_ds_options, the partition doesn't exist that can expand.
            if not vmfs_ds_options and self.expand["resize_gb"] == "all":
                # If resize_gb is all, it will normal termination when already expanded the datastore to full.
                self.module.exit_json(**self.result)
            elif not vmfs_ds_options and self.expand["resize_gb"] != "all":
                self.module.fail_json(msg="Failed to find the partition can expand.")

            expand_disk_info = self.get_expand_partition(vmfs_ds_options)
            if not expand_disk_info:
                self.module.fail_json(msg="Failed to find the partition number: %s" % self.expand["partition_number"])

            if self.expand['resize_gb'] != "all":
                block_size = expand_disk_info["disk_partition_block_range"].end.blockSize
                total_block_size = expand_disk_info["disk_partition_block_range"].end.block
                capacity_block_size = math.floor(self.datastore_obj.info.vmfs.capacity / block_size)
                resize_block_size = math.floor(self.expand["resize_gb"] * block_size / 1024)

                if total_block_size > resize_block_size and capacity_block_size < resize_block_size:
                    disk_partition_block_range = expand_disk_info["disk_partition_block_range"]
                    disk_partition_block_range.end.block = resize_block_size
                    host_disk_partition_info = self.cnf_mng.storageSystem.ComputeDiskPartitionInfoForResize(expand_disk_info["scsi_disk_partition"],
                                                                                                            disk_partition_block_range)

                    vmfs_datastore_expand_spec = expand_disk_info["vmfs_datastore_expand_spec"]
                    vmfs_datastore_expand_spec.partition = host_disk_partition_info.spec
                    resized_datastore = self.expand_datastore(vmfs_datastore_expand_spec)
                else:
                    self.module.fail_json(msg="The specified the value can't expand in existing datastore: %s" % self.expand["resize_gb"])
            else:
                vmfs_datastore_expand_spec = expand_disk_info["vmfs_datastore_expand_spec"]
                resized_datastore = self.expand_datastore(vmfs_datastore_expand_spec)

            if resized_datastore:
                self.result["changed"] = True
                self.result["resized_datastore_info"] = self.generate_return_value(resized_datastore)

            self.module.exit_json(**self.result)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=True),
        datastore=dict(type='str', required=True),
        expand=dict(type='dict',
                    required=True,
                    options=dict(
                        partition_number=dict(type='int', default=1, aliases=['partition']),
                        resize_gb=dict(type='str', required=True)
                    )),
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_host_datastore_resize = VMwareHostDatastoreResize(module)
    vmware_host_datastore_resize.execute()


if __name__ == "__main__":
    main()
