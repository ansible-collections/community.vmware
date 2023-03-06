#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Tyler Gates <tgates81@gmail.com>
#
# Special thanks to:
#   * Vadim Aleksandrov <valeksandrov@me.com>: Original author of python script
#                                              `set_vm_storage_policy.py` from
#                                              which most methods were derived.
#   * William Lam (https://github.com/lamw): Author of script
#                                            `list_vm_storage_policy.py` whose
#                                            ideas were inspiration for
#                                            Vadim's script.
#   * Abhijeet Kasurde <akasurde@redhat.com>: Ansible modulization loosely
#                                             modeled after
#                                             `vmware_guest_disk.py'.
#
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_storage_policy
short_description: Set VM Home and disk(s) storage policy profiles.
description:
    - This module can be used to enforce storage policy profiles per disk and/or VM Home on a virtual machine.
author:
    - Tyler Gates (@tgates81)
options:
   name:
     description:
     - Name of the virtual machine.
     - One of C(name), C(uuid), or C(moid) are required to define the virtual machine.
     type: str
     required: false
   uuid:
     description:
     - UUID of the virtual machine.
     - One of C(name), C(uuid), or C(moid) are required to define the virtual machine.
     type: str
     required: false
   moid:
     description:
     - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
     - One of C(name), C(uuid), or C(moid) are required to define the virtual machine.
     type: str
     required: false
   folder:
     description:
     - Destination folder, absolute or relative path to find an existing guest.
     - This is a required parameter if multiple VMs are found with same name.
     - The folder should include the datacenter. ESX's datacenter is ha-datacenter.
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
     required: false
   vm_home:
     description:
     - A storage profile policy to set on VM Home.
     - All values and parameters are case sensitive.
     - At least one of C(disk) or C(vm_home) are required parameters.
     required: false
     type: str
   disk:
     description:
     - A list of disks with storage profile policies to enforce.
     - All values and parameters are case sensitive.
     - At least one of C(disk) and C(vm_home) are required parameters.
     required: false
     type: list
     elements: dict
     suboptions:
       unit_number:
         description:
         - Disk Unit Number.
         - Valid values range from 0 to 15.
         type: int
         required: true
       controller_number:
         description:
         - SCSI controller number.
         - Valid values range from 0 to 3.
         type: int
         default: 0
       policy:
         description:
         - Name of the storage profile policy to enforce for the disk.
         type: str
         required: true
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Enforce storepol1 policy for disk 0 and 1 on SCSI controller 0 using UUID
  community.vmware.vmware_guest_storage_policy:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    uuid: cefd316c-fc19-45f3-a539-2cd03427a78d
    disk:
      - unit_number: 0
        controller_number: 0
        policy: storepol1
      - unit_number: 1
        controller_number: 0
        policy: storepol1
  delegate_to: localhost
  register: policy_status

- name: Enforce storepol1 policy for VM Home using name
  community.vmware.vmware_guest_storage_policy:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: false
    name: hostname1
    vm_home: storepol1
  delegate_to: localhost
'''

RETURN = r'''
msg:
    description: Informational message on the job result.
    type: str
    returned: always
    sample: "Policies successfully set."
changed_policies:
    description: Dictionary containing the changed policies of disk (list of dictionaries) and vm_home.
    type: dict
    returned: always
    sample: {
        "disk": [
            {
                "policy": "storepol1",
                "unit_number": 0
            }
        ],
        "vm_home": "storepol1"
    }
'''

import traceback
from ansible.module_utils.basic import missing_required_lib
PYVMOMI_IMP_ERR = None
try:
    from pyVmomi import pbm, vim
    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False
    PYVMOMI_IMP_ERR = traceback.format_exc()
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import vmware_argument_spec, wait_for_task
from ansible_collections.community.vmware.plugins.module_utils.vmware_spbm import SPBM


class SPBM_helper(SPBM):
    def __init__(self, module):
        super().__init__(module)

    def SearchStorageProfileByName(self, profileManager, name):
        """
        Search VMware storage policy profile by name.

        :param profileManager: A VMware Storage Policy Service manager object.
        :type profileManager: pbm.profile.ProfileManager
        :param name: A VMware Storage Policy profile name.
        :type name: str
        :returns: A VMware Storage Policy profile object.
        :rtype: pbm.profile.Profile
        """

        profileIds = profileManager.PbmQueryProfile(
            resourceType=pbm.profile.ResourceType(resourceType="STORAGE"),
            profileCategory="REQUIREMENT"
        )
        if len(profileIds) > 0:
            storageProfiles = profileManager.PbmRetrieveContent(
                profileIds=profileIds)

        for storageProfile in storageProfiles:
            if storageProfile.name == name:
                return storageProfile

    def CheckAssociatedStorageProfile(self, profileManager, ref, name):
        """
        Check the associated storage policy profile.

        :param profileManager: A VMware Storage Policy Service manager object.
        :type profileManager: pbm.profile.ProfileManager
        :param ref: A server object ref to a virtual machine, virtual disk,
            or datastore.
        :type ref: pbm.ServerObjectRef
        :param name: A VMware storage policy profile name.
        :type name: str
        :returns: True if storage policy profile by name is associated to ref.
        :rtype: bool
        """

        profileIds = profileManager.PbmQueryAssociatedProfile(ref)
        if len(profileIds) > 0:
            profiles = profileManager.PbmRetrieveContent(profileIds=profileIds)
            for profile in profiles:
                if profile.name == name:
                    return True
        return False

    def SetVMHomeStorageProfile(self, vm, profile):
        """
        Set VM Home storage policy profile.

        :param vm: A virtual machine object.
        :type vm: VirtualMachine
        :param profile: A VMware Storage Policy profile.
        :type profile: pbm.profile.Profile
        :returns: VMware task object.
        :rtype: Task
        """

        spec = vim.vm.ConfigSpec()
        profileSpec = vim.vm.DefinedProfileSpec()
        profileSpec.profileId = profile.profileId.uniqueId
        spec.vmProfile = [profileSpec]
        return vm.ReconfigVM_Task(spec)

    def GetVirtualDiskObj(self, vm, unit_number, controller_number):
        """
        Get a virtual disk object.

        :param vm: A virtual machine object.
        :type vm: VirtualMachine
        :param unit_number: virtual machine's disk unit number.
        :type unit_number: int
        :param controller_number: virtual machine's controller number.
        :type controller_number: int
        :returns: VirtualDisk object if exists, else None.
        :rtype: VirtualDisk, None
        """
        controllerKey = None
        for device in vm.config.hardware.device:
            if isinstance(device, vim.vm.device.VirtualSCSIController):
                if device.busNumber == controller_number:
                    controllerKey = device.key
                    break

        if controllerKey is not None:  # if controller was found check disk
            for device in vm.config.hardware.device:
                if not isinstance(device, vim.vm.device.VirtualDisk):
                    continue
                if int(device.unitNumber) == int(unit_number) and \
                   int(device.controllerKey) == controllerKey:
                    return device

        return None

    def SetVMDiskStorageProfile(self, vm, unit_number, controller_number, profile):
        """
        Set VM's disk storage policy profile.

        :param vm: A virtual machine object
        :type vm: VirtualMachine
        :param unit_number: virtual machine's disk unit number.
        :type unit_number: int
        :param controller_number: virtual machine's controller number.
        :type controller_number: int
        :param profile: A VMware Storage Policy profile
        :type profile: pbm.profile.Profile
        :returns: VMware task object.
        :rtype: Task
        """

        spec = vim.vm.ConfigSpec()
        profileSpec = vim.vm.DefinedProfileSpec()
        profileSpec.profileId = profile.profileId.uniqueId

        deviceSpec = vim.vm.device.VirtualDeviceSpec()
        deviceSpec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
        disk_obj = self.GetVirtualDiskObj(vm, unit_number, controller_number)
        deviceSpec.device = disk_obj
        deviceSpec.profile = [profileSpec]
        spec.deviceChange = [deviceSpec]
        return vm.ReconfigVM_Task(spec)

    def ensure_storage_policies(self, vm_obj):
        """
        Ensure VM storage profile policies.

        :param vm_obj: VMware VM object.
        :type vm_obj: VirtualMachine
        :exits: self.module.exit_json on success, else self.module.fail_json.
        """

        disks = self.module.params.get('disk')
        vm_home = self.module.params.get('vm_home')
        success_msg = "Policies successfully set."
        result = dict(
            changed=False,
            msg="",
            changed_policies=dict(disk=[],
                                  vm_home="",
                                  ),
        )

        # Connect into vcenter and get the profile manager for the VM.
        self.get_spbm_connection()
        pm = self.spbm_content.profileManager

        #
        # VM HOME
        #
        if vm_home:
            policy = vm_home
            pmObjectType = pbm.ServerObjectRef.ObjectType("virtualMachine")
            pmRef = pbm.ServerObjectRef(key=vm_obj._moId,
                                        objectType=pmObjectType)
            pol_obj = self.SearchStorageProfileByName(pm, policy)

            if not pol_obj:
                result['msg'] = "Unable to find storage policy `%s' for vm_home" % policy
                self.module.fail_json(**result)

            if not self.CheckAssociatedStorageProfile(pm, pmRef, policy):
                # Existing policy is different than requested. Set, wait for
                # task success, and exit.
                if not self.module.check_mode:
                    task = self.SetVMHomeStorageProfile(vm_obj, pol_obj)
                    wait_for_task(task)  # will raise an Exception on failure
                result['changed'] = True
                result['changed_policies']['vm_home'] = policy

        #
        # DISKS
        #
        if disks is None:
            disks = list()
        # Check the requested disks[] information is sane or fail by looking up
        # and storing the object(s) in a new dict.
        disks_objs = dict()  # {unit_number: {disk: <obj>, policy: <obj>}}
        for disk in disks:
            policy = str(disk['policy'])
            unit_number = int(disk['unit_number'])
            controller_number = int(disk['controller_number'])
            disk_obj = self.GetVirtualDiskObj(vm_obj, unit_number, controller_number)
            pol_obj = self.SearchStorageProfileByName(pm, policy)
            if not pol_obj:
                result['msg'] = "Unable to find storage policy `%s' for disk %s." % (policy, disk)
                self.module.fail_json(**result)
            if not disk_obj:
                errmsg = "Unable to find disk for controller_number '%s' unit_number '%s'. 7 is reserved for SCSI adapters."
                result['msg'] = errmsg % (controller_number, unit_number)
                self.module.fail_json(**result)
            disks_objs[unit_number] = dict(disk=disk_obj, policy=pol_obj)

        # All requested profiles are valid. Iterate through each disk and set
        # accordingly.
        for disk in disks:
            policy = str(disk['policy'])
            unit_number = int(disk['unit_number'])
            controller_number = int(disk['controller_number'])
            disk_obj = disks_objs[unit_number]['disk']
            pol_obj = disks_objs[unit_number]['policy']
            pmObjectType = pbm.ServerObjectRef.ObjectType("virtualDiskId")
            pmRef = pbm.ServerObjectRef(key="%s:%s"
                                            % (vm_obj._moId, disk_obj.key),
                                        objectType=pmObjectType)

            if not self.CheckAssociatedStorageProfile(pm, pmRef, policy):
                # Existing policy is different than requested. Set, wait for
                # task success, and exit.
                if not self.module.check_mode:
                    task = self.SetVMDiskStorageProfile(vm_obj, unit_number,
                                                        controller_number,
                                                        pol_obj)
                    wait_for_task(task)
                result['changed'] = True
                result['changed_policies']['disk'].append(disk)

        #
        # END
        #
        # Check our results and exit.
        if result['changed']:
            result['msg'] = success_msg
        self.module.exit_json(**result)


def run_module():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        folder=dict(type='str'),
        disk=dict(type='list',
                  required=False,
                  elements='dict',
                  options=dict(
                       unit_number=dict(type='int', required=True),
                       controller_number=dict(type='int', default=0),
                       policy=dict(type='str', required=True)
                  )),
        vm_home=dict(type='str'),
    )
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=argument_spec,
        required_one_of=[
            ['name', 'uuid', 'moid'],
            ['disk', 'vm_home'],
        ],
    )

    if not HAS_PYVMOMI:
        module.fail_json(msg=missing_required_lib("pyVmomi"),
                         exception=PYVMOMI_IMP_ERR)

    if module.params['folder']:
        # FindByInventoryPath() does not require an absolute path
        # so we should leave the input folder path unmodified
        module.params['folder'] = module.params['folder'].rstrip('/')

    spbm_h = SPBM_helper(module)
    # Check if the VM exists before continuing
    vm = spbm_h.get_vm()
    if not vm:
        module.fail_json(msg="Unable to find virtual machine `%s'" %
                         (module.params.get('name')
                          or module.params.get('uuid')
                          or module.params.get('moid')))

    try:
        spbm_h.ensure_storage_policies(vm)
    except Exception as e:
        module.fail_json(msg="Failed to set storage policies for virtual"
                             "machine '%s' with exception: %s"
                             % (vm.name, to_native(e)))


def main():
    run_module()


if __name__ == "__main__":
    main()
