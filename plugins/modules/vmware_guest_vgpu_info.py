#!/usr/bin/python
#  -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Diane Wang <dianew@vmware.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: vmware_guest_vgpu_info
version_added: '3.3.0'
short_description: Gather information about vGPU profiles of the specified virtual machine in the given vCenter infrastructure
description:
    - This module is used to gather metadata about vGPU profiles of the given virtual machine.
author:
    - Jared Priddy (@jdptechnc)
options:
   name:
     description:
       - Name of the virtual machine.
       - This is a required parameter, if parameter O(uuid) or O(moid) is not supplied.
     type: str
   uuid:
     description:
       - UUID of the instance to gather facts if known, this is VMware's unique identifier.
       - This is a required parameter, if parameter O(name) or O(moid) is not supplied.
     type: str
   moid:
     description:
       - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
       - This is required if O(name) or O(uuid) is not supplied.
     type: str
   folder:
     description:
       - Destination folder, absolute or relative path to find an existing guest.
       - This is a required parameter, only if multiple VMs are found with same name.
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
     default: ha-datacenter
     description:
       - The datacenter name to which virtual machine belongs to.
     type: str
   use_instance_uuid:
     description:
       - Whether to use the VMware instance UUID rather than the BIOS UUID.
     default: false
     type: bool
extends_documentation_fragment:
- community.vmware.vmware.documentation
"""

EXAMPLES = r"""
- name: Gather information about vGPU profiles of a VM
  community.vmware.vmware_guest_vgpu_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    validate_certs: false
    name: UbuntuTest
  delegate_to: localhost
  register: vgpu_info

"""

RETURN = r"""
vgpu_info:
    description: metadata about the virtual machine's vGPU profiles
    returned: always
    type: list
    sample: {
        "vgpu": [
            {
                "Controller_Key": 100,
                "Key": 13000,
                "Label": "PCI device 0",
                "Summary": "NVIDIA GRID vGPU grid_m10-8q",
                "Unit_Number": 18,
                "Vgpu": "grid_m10-8q"
            }
        ]
    }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class PyVmomiHelper(PyVmomi):
    def __init__(self, module):
        super(PyVmomiHelper, self).__init__(module)

    def gather_vgpu_profile_facts(self, vm_obj):
        """
        Gather facts about VM's vGPU profile settings
        Args:
            vm_obj: Managed object of virtual machine
        Returns: list of vGPU profiles with facts
        """
        vgpu_info = []
        for vgpu_VirtualDevice_obj in vm_obj.config.hardware.device:
            if hasattr(vgpu_VirtualDevice_obj.backing, "vgpu"):
                vgpu = dict(
                    Vgpu=vgpu_VirtualDevice_obj.backing.vgpu,
                    Key=vgpu_VirtualDevice_obj.key,
                    Summary=vgpu_VirtualDevice_obj.deviceInfo.summary,
                    Label=vgpu_VirtualDevice_obj.deviceInfo.label,
                    Unit_Number=vgpu_VirtualDevice_obj.unitNumber,
                    Controller_Key=vgpu_VirtualDevice_obj.controllerKey,
                )
                vgpu_info.append(vgpu)
        return vgpu_info


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type="str"),
        uuid=dict(type="str"),
        use_instance_uuid=dict(type="bool", default=False),
        moid=dict(type="str"),
        folder=dict(type="str"),
        datacenter=dict(type="str", default="ha-datacenter"),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[["name", "uuid", "moid"]],
        supports_check_mode=True,
    )

    pyv = PyVmomiHelper(module)
    vm = pyv.get_vm()

    if not vm:
        vm_id = (
            module.params.get("uuid")
            or module.params.get("name")
            or module.params.get("moid")
        )
        module.fail_json(
            msg="Unable to gather vGPU information for non-existing VM %s" % vm_id
        )
    else:
        try:
            module.exit_json(vgpu=pyv.gather_vgpu_profile_facts(vm))
        except Exception as exc:
            module.fail_json(msg="Failed to gather information with exception : %s" % to_text(exc))


if __name__ == "__main__":
    main()
