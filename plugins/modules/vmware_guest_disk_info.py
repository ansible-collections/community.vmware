#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, NAER William Leemans (@bushvin) <willie@elaba.net>
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_disk_info
short_description: Gather info about disks of given virtual machine
description:
    - This module can be used to gather information about disks belonging to given virtual machine.
    - All parameters and VMware object names are case sensitive.
author:
    - Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>
options:
   name:
     description:
     - Name of the virtual machine.
     - This is required parameter, if parameter C(uuid) or C(moid) is not supplied.
     type: str
   uuid:
     description:
     - UUID of the instance to gather information if known, this is VMware's unique identifier.
     - This is required parameter, if parameter C(name) or C(moid) is not supplied.
     type: str
   moid:
     description:
     - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
     - This is required if C(name) or C(uuid) is not supplied.
     type: str
   use_instance_uuid:
     description:
     - Whether to use the VMware instance UUID rather than the BIOS UUID.
     default: false
     type: bool
   folder:
     description:
     - Destination folder, absolute or relative path to find an existing guest.
     - This is required parameter, only if multiple VMs are found with same name.
     - The folder should include the datacenter. ESX's datacenter is ha-datacenter
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
     required: true
     type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather disk info from virtual machine using UUID
  community.vmware.vmware_guest_disk_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: ha-datacenter
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
  delegate_to: localhost
  register: disk_info

- name: Gather disk info from virtual machine using name
  community.vmware.vmware_guest_disk_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: ha-datacenter
    name: VM_225
  delegate_to: localhost
  register: disk_info

- name: Gather disk info from virtual machine using moid
  community.vmware.vmware_guest_disk_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: ha-datacenter
    moid: vm-42
  delegate_to: localhost
  register: disk_info
'''

RETURN = r'''
guest_disk_info:
    description: metadata about the virtual machine's disks
    returned: always
    type: dict
    sample: {
        "0": {
            "backing_datastore": "datastore2",
            "backing_disk_mode": "persistent",
            "backing_diskmode": "persistent",
            "backing_eagerlyscrub": false,
            "backing_filename": "[datastore2] VM_225/VM_225.vmdk",
            "backing_thinprovisioned": false,
            "backing_type": "FlatVer2",
            "backing_writethrough": false,
            "backing_uuid": "200C3A00-f82a-97af-02ff-62a595f0020a",
            "capacity_in_bytes": 10485760,
            "capacity_in_kb": 10240,
            "controller_bus_number": 0,
            "controller_key": 1000,
            "controller_type": "paravirtual",
            "key": 2000,
            "label": "Hard disk 1",
            "summary": "10,240 KB",
            "unit_number": 0
        },
        "1": {
            "backing_datastore": "datastore3",
            "backing_devicename": "vml.012345678901234567890123456789012345678901234567890123",
            "backing_disk_mode": "independent_persistent",
            "backing_diskmode": "independent_persistent",
            "backing_filename": "[datastore3] VM_226/VM_226.vmdk",
            "backing_lunuuid": "012345678901234567890123456789012345678901234567890123",
            "backing_type": "RawDiskMappingVer1",
            "backing_uuid": null,
            "capacity_in_bytes": 15728640,
            "capacity_in_kb": 15360,
            "controller_bus_number": 0,
            "controller_key": 1000,
            "controller_type": "paravirtual",
            "key": 2001,
            "label": "Hard disk 3",
            "summary": "15,360 KB",
            "unit_number": 1
        },
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vm_device_helper import PyVmomiDeviceHelper


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
        folder=dict(type='str'),
        datacenter=dict(type='str', required=True),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['name', 'uuid', 'moid']
        ],
        supports_check_mode=True,
    )

    if module.params['folder']:
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    pyv = PyVmomi(module)
    device_helper = PyVmomiDeviceHelper(module)
    # Check if the VM exists before continuing
    vm = pyv.get_vm()

    if vm:
        # VM exists
        try:
            module.exit_json(guest_disk_info=device_helper.gather_disk_info(vm))
        except Exception as exc:
            module.fail_json(msg="Failed to gather information with exception : %s" % to_text(exc))
    else:
        # We unable to find the virtual machine user specified
        # Bail out
        vm_id = (module.params.get('uuid') or module.params.get('moid') or module.params.get('name'))
        module.fail_json(msg="Unable to gather disk information for non-existing VM %s" % vm_id)


if __name__ == '__main__':
    main()
