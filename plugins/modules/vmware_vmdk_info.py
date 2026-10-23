#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, Everpure Inc.
# Copyright: (c) 2026, Eugenio Grosso <eugenio.grosso@everpuredata.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vmdk_info
short_description: Gather information about a virtual disk file
description:
    - Gather information about a virtual disk (VMDK) file on a datastore, whether or not a VM uses it.
    - Reports the size, the provisioning type, the disk UUID and geometry, and the VMs that use the disk.
      This is the information that C(vmkfstools -q), C(-g) and C(-J getuuid) show on an ESXi host.
    - Works with a vCenter or directly with an ESXi host.
author:
    - Eugenio Grosso (@genegr)

version_added: 7.1.0

options:
    path:
        description:
            - Path of the virtual disk descriptor.
            - Either a datastore path such as V([datastore1] vm1/vm1.vmdk) or a path such as
              V(/vmfs/volumes/datastore1/vm1/vm1.vmdk). The datastore can be given by name or, in the second form, by VMFS UUID.
        type: str
        required: true
    datacenter:
        description:
            - Name or MOID of the datacenter that holds the datastore.
            - Only needed when several datacenters have a datastore with the same name.
            - Ignored when connected to an ESXi host.
        type: str

notes:
    - When the disk is not used by a VM, the API does not report whether a thick disk is eager zeroed,
      nor which LUN an RDM descriptor maps. In this case the provisioning reported in RV(vmdk) is V(thick) for thick disks,
      and the RDM compatibility mode comes from the name of the mapping file.

extends_documentation_fragment:
    - vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Gather information about a virtual disk
  community.vmware.vmware_vmdk_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    path: "[datastore1] vm1/vm1.vmdk"
  register: _disk

- name: Check that a disk exists, using an ESXi style path
  community.vmware.vmware_vmdk_info:
    path: /vmfs/volumes/datastore1/vm1/vm1_1.vmdk
  register: _disk
  failed_when: not _disk.vmdk.exists
'''

RETURN = r'''
vmdk:
    description:
        - Information about the virtual disk. If the disk does not exist, only C(path), C(exists) and C(datastore) are returned.
        - C(provisioning) is one of V(thin), V(zeroedthick), V(eagerzeroedthick), V(thick), V(sparse), V(rdm) or V(rdmp).
        - C(attached_to) lists the VMs that use the disk, directly or as the base of a snapshot.
    returned: always
    type: dict
    sample:
        path: "[datastore1] vm1/vm1.vmdk"
        exists: true
        datastore:
            name: datastore1
            moid: datastore-1001
        backing_type: FlatVer2BackingInfo
        provisioning: thin
        capacity_bytes: 42949672960
        file_size_bytes: 1073741824
        thin: true
        controller_type: VirtualLsiLogicController
        hardware_version: 14
        extents:
            - "[datastore1] vm1/vm1-flat.vmdk"
        modification_time: "2026-10-22T07:02:19+00:00"
        uuid: "60 00 C2 9a 4c 6e 1b 1f-1c 5a 7c 0f 1d 62 23 a5"
        geometry:
            cylinders: 5221
            heads: 255
            sectors: 63
        attached_to:
            - vm:
                name: vm1
                moid: vm-1002
              label: Hard disk 1
              disk_mode: persistent
              snapshot_base: false
'''

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    vmware_argument_spec
)
from ansible_collections.community.vmware.plugins.module_utils.vmware_vmdk import (
    VmdkFiles
)


class VmdkInfoModule(PyVmomi):
    def __init__(self, module):
        super().__init__(module)
        self.files = VmdkFiles(self)
        self.path = self.files.resolve(self.params['path'], 'path')

    def gather_info(self):
        """
        Returns:
            dict, the description of the disk
        """
        return self.files.describe(self.path)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        path=dict(type='str', required=True),
        datacenter=dict(type='str', required=False),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    vmdk_info = VmdkInfoModule(module)
    module.exit_json(changed=False, vmdk=vmdk_info.gather_info())


if __name__ == '__main__':
    main()
