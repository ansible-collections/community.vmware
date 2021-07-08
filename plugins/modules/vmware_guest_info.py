#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This module is also sponsored by E.T.A.I. (www.etai.fr)
# Copyright (C) 2018 James E. King III (@jeking3) <jking@apache.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_info
short_description: Gather info about a single VM
description:
    - Gather information about a single VM on a VMware ESX cluster.
    - This module was called C(vmware_guest_facts) before Ansible 2.9. The usage did not change.
author:
    - Loic Blot (@nerzhul) <loic.blot@unix-experience.fr>
notes:
    - Tested on vSphere 5.5, 6.7
requirements:
    - "python >= 2.6"
    - PyVmomi
options:
   name:
     description:
     - Name of the VM to work with
     - This is required if C(uuid) or C(moid) is not supplied.
     type: str
   name_match:
     description:
     - If multiple VMs matching the name, use the first or last found
     default: 'first'
     choices: ['first', 'last']
     type: str
   uuid:
     description:
     - UUID of the instance to manage if known, this is VMware's unique identifier.
     - This is required if C(name) or C(moid) is not supplied.
     type: str
   use_instance_uuid:
     description:
     - Whether to use the VMware instance UUID rather than the BIOS UUID.
     default: false
     type: bool
   moid:
     description:
     - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
     - This is required if C(name) or C(uuid) is not supplied.
     type: str
   folder:
     description:
     - Destination folder, absolute or relative path to find an existing guest.
     - This is required if name is supplied.
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
     - Destination datacenter for the deploy operation
     required: True
     type: str
   tags:
     description:
     - Whether to show tags or not.
     - If set C(True), shows tags information. Returns a list of tag names.
     - If set C(False), hides tags information.
     - vSphere Automation SDK is required.
     default: false
     type: bool
   tag_details:
     description:
     - If set C(True), detail information about 'tags' returned.
     - Without this flag, the 'tags' returns a list of tag names.
     - With this flag, the 'tags' returns a list of dict about tag information with additional details like category name, category id, and tag id.
     - This parameter is added to maintain backward compatability.
     default: false
     type: bool
     version_added: '1.4.0'
   schema:
     description:
     - Specify the output schema desired.
     - The 'summary' output schema is the legacy output from the module
     - The 'vsphere' output schema is the vSphere API class definition
       which requires pyvmomi>6.7.1
     choices: ['summary', 'vsphere']
     default: 'summary'
     type: str
   properties:
     description:
     - Specify the properties to retrieve.
     - If not specified, all properties are retrieved (deeply).
     - Results are returned in a structure identical to the vsphere API.
     - 'Example:'
     - '   properties: ['
     - '      "config.hardware.memoryMB",'
     - '      "config.hardware.numCPU",'
     - '      "guest.disk",'
     - '      "overallStatus"'
     - '   ]'
     - Only valid when C(schema) is C(vsphere).
     type: list
     elements: str
     required: False
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather info from standalone ESXi server having datacenter as 'ha-datacenter'
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: ha-datacenter
    uuid: 421e4592-c069-924d-ce20-7e7533fab926
  delegate_to: localhost
  register: info

- name: Gather some info from a guest using the vSphere API output schema
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: "{{ vm_name }}"
    schema: "vsphere"
    properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
  delegate_to: localhost
  register: info

- name: Gather some information about a guest using MoID
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    moid: vm-42
    schema: "vsphere"
    properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
  delegate_to: localhost
  register: vm_moid_info

- name: Gather Managed object ID (moid) from a guest using the vSphere API output schema for REST Calls
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: "{{ vm_name }}"
    schema: "vsphere"
    properties:
      - _moId
  delegate_to: localhost
  register: moid_info

- name: Gather detailed information about tags and category associated with the given VM
  community.vmware.vmware_guest_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
    name: "{{ vm_name }}"
    tags: True
    tag_details: True
  register: detailed_tag_info
'''

RETURN = r'''
instance:
    description: metadata about the virtual machine
    returned: always
    type: dict
    sample: {
        "advanced_settings": {},
        "annotation": "",
        "current_snapshot": null,
        "customvalues": {},
        "guest_consolidation_needed": false,
        "guest_question": null,
        "guest_tools_status": "guestToolsNotRunning",
        "guest_tools_version": "10247",
        "hw_cores_per_socket": 1,
        "hw_datastores": [
            "ds_226_3"
        ],
        "hw_esxi_host": "10.76.33.226",
        "hw_eth0": {
            "addresstype": "assigned",
            "ipaddresses": null,
            "label": "Network adapter 1",
            "macaddress": "00:50:56:87:a5:9a",
            "macaddress_dash": "00-50-56-87-a5-9a",
            "portgroup_key": null,
            "portgroup_portkey": null,
            "summary": "VM Network"
        },
        "hw_files": [
            "[ds_226_3] ubuntu_t/ubuntu_t.vmx",
            "[ds_226_3] ubuntu_t/ubuntu_t.nvram",
            "[ds_226_3] ubuntu_t/ubuntu_t.vmsd",
            "[ds_226_3] ubuntu_t/vmware.log",
            "[ds_226_3] u0001/u0001.vmdk"
        ],
        "hw_folder": "/DC0/vm/Discovered virtual machine",
        "hw_guest_full_name": null,
        "hw_guest_ha_state": null,
        "hw_guest_id": null,
        "hw_interfaces": [
            "eth0"
        ],
        "hw_is_template": false,
        "hw_memtotal_mb": 1024,
        "hw_name": "ubuntu_t",
        "hw_power_status": "poweredOff",
        "hw_processor_count": 1,
        "hw_product_uuid": "4207072c-edd8-3bd5-64dc-903fd3a0db04",
        "hw_version": "vmx-13",
        "instance_uuid": "5007769d-add3-1e12-f1fe-225ae2a07caf",
        "ipv4": null,
        "ipv6": null,
        "module_hw": true,
        "snapshots": [],
        "tags": [
            "backup"
        ],
        "vnc": {},
        "moid": "vm-42",
        "vimref": "vim.VirtualMachine:vm-42"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
try:
    from com.vmware.vapi.std_client import DynamicID  # noqa: F401
    HAS_VSPHERE = True
except ImportError:
    HAS_VSPHERE = False


class VmwareTag(VmwareRestClient):
    def __init__(self, module):
        super(VmwareTag, self).__init__(module)
        self.tag_service = self.api_client.tagging.Tag
        self.tag_association_svc = self.api_client.tagging.TagAssociation


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        name_match=dict(type='str', choices=['first', 'last'], default='first'),
        uuid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
        moid=dict(type='str'),
        folder=dict(type='str'),
        datacenter=dict(type='str', required=True),
        tags=dict(type='bool', default=False),
        schema=dict(type='str', choices=['summary', 'vsphere'], default='summary'),
        properties=dict(type='list', elements='str'),
        tag_details=dict(type='bool', default=False),
    )
    module = AnsibleModule(argument_spec=argument_spec,
                           required_one_of=[['name', 'uuid', 'moid']],
                           supports_check_mode=True)
    if module._name in ('vmware_guest_facts', 'community.vmware.vmware_guest_facts'):
        module.deprecate(
            msg="The 'vmware_guest_facts' module has been renamed to 'vmware_guest_info'",
            version='3.0.0',
            collection_name='community.vmware'
        )

    if module.params.get('folder'):
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    if module.params['schema'] != 'vsphere' and module.params.get('properties'):
        module.fail_json(msg="The option 'properties' is only valid when the schema is 'vsphere'")

    pyv = PyVmomi(module)
    # Check if the VM exists before continuing
    vm = pyv.get_vm()

    # VM already exists
    if vm:
        try:
            if module.params['schema'] == 'summary':
                instance = pyv.gather_facts(vm)
            else:
                instance = pyv.to_json(vm, module.params['properties'])
            if module.params.get('tags'):
                if not HAS_VSPHERE:
                    module.fail_json(msg="Unable to find 'vCloud Suite SDK' Python library which is required."
                                         " Please refer this URL for installation steps"
                                         " - https://code.vmware.com/web/sdk/vsphere-automation-python")

                vm_rest_client = VmwareTag(module)
                tags = []
                if module.params.get('tag_details'):
                    tags = vm_rest_client.get_tags_for_vm(vm_mid=vm._moId)
                else:
                    dynamic_obj = DynamicID(type='VirtualMachine', id=vm._moId)
                    tags = vm_rest_client.get_vm_tags(vm_rest_client.tag_service,
                                                      vm_rest_client.tag_association_svc,
                                                      vm_mid=dynamic_obj)
                instance.update(tags=tags)
            module.exit_json(instance=instance)
        except Exception as exc:
            module.fail_json(msg="Information gathering failed with exception %s" % to_text(exc))
    else:
        vm_id = (module.params.get('uuid') or module.params.get('name') or module.params.get('moid'))
        module.fail_json(msg="Unable to gather information for non-existing VM %s" % vm_id)


if __name__ == '__main__':
    main()
