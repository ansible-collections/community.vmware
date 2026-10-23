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
module: vmware_vmdk_clone
short_description: Clone a virtual disk file, optionally converting its format or copying it onto a LUN as an RDM
description:
    - Copy a virtual disk (VMDK) file to a new descriptor, like C(vmkfstools -i) on an ESXi host.
    - The copy can use another disk format, or be written onto a SCSI LUN that the new descriptor maps as a
      raw device mapping (RDM) in virtual or physical compatibility mode.
    - If the destination already exists, nothing is done unless O(force=true).
    - vCenter does not apply a destination format when it copies a disk, so a clone that changes the format, or that targets
      an RDM, needs a direct connection to an ESXi host that mounts the datastores and sees the LUN.
      Through vCenter, the module copies the disk in its source format.
author:
    - Eugenio Grosso (@genegr)

version_added: 7.1.0

options:
    source:
        description:
            - Path of the descriptor of the disk to copy.
            - Either a datastore path such as V([datastore1] vm1/vm1.vmdk) or a path such as
              V(/vmfs/volumes/datastore1/vm1/vm1.vmdk). The datastore can be given by name or, in the second form, by VMFS UUID.
            - The disk should not be in use by a running VM. To copy the disk of a running VM, take a snapshot
              and copy the base disk.
        type: str
        required: true
    destination:
        description:
            - Path of the new descriptor, in the same formats as O(source).
        type: str
        required: true
    disk_format:
        description:
            - Format of the copy.
            - V(thin), V(zeroedthick) and V(eagerzeroedthick) create a VMDK file with that provisioning.
            - V(rdm) and V(rdmp) map the LUN given in O(device) in virtual or physical compatibility mode,
              and write the disk data onto the LUN.
            - V(2gbsparse) creates a sparse disk split in 2 GB extents, as used by hosted VMware products.
            - If not set, the copy keeps the provisioning of the source. On an ESXi host, a thick source becomes
              V(zeroedthick), because the API does not report whether a detached disk is eager zeroed.
            - When connected to vCenter, only the format of the source can be used.
        type: str
        choices: [thin, zeroedthick, eagerzeroedthick, rdm, rdmp, 2gbsparse]
    device:
        description:
            - The LUN that receives the disk data when O(disk_format) is V(rdm) or V(rdmp).
            - Its canonical name, for example V(naa.624a93706c1b16ce1c034d1c0638cb69), or its device path,
              for example V(/vmfs/devices/disks/naa.624a93706c1b16ce1c034d1c0638cb69).
            - The LUN must be at least as large as the source disk and must not hold a VMFS datastore.
              Its current content is overwritten.
        type: str
    create_folders:
        description:
            - Create the folder of O(destination) when it does not exist.
        type: bool
        default: false
    force:
        description:
            - Replace the destination if it already exists.
            - The existing disk is deleted before the copy. A disk that a VM uses is never replaced.
            - Deleting an RDM descriptor does not change the data on its LUN.
        type: bool
        default: false
    datacenter:
        description:
            - Name or MOID of the datacenter that holds the datastores.
            - Only needed when several datacenters have a datastore with the same name.
            - Ignored when connected to an ESXi host.
        type: str
    timeout:
        description:
            - Seconds to wait for the copy to complete. Copying a large disk can take hours.
        type: int
        default: 3600

notes:
    - vCenter ignores the destination specification of the API call that copies disks, so the module refuses a format
      change through vCenter instead of silently making a copy in the source format.
    - The idempotency check is based on the destination path only. An existing destination is not compared with the source.

extends_documentation_fragment:
    - vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Copy a disk to another datastore, through vCenter
  community.vmware.vmware_vmdk_clone:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    source: "[datastore1] vm1/vm1.vmdk"
    destination: "[datastore2] backup/vm1.vmdk"
    create_folders: true

- name: Clone a disk onto a LUN as a virtual compatibility RDM, like vmkfstools -i src.vmdk -d rdm:/vmfs/devices/disks/naa...
  community.vmware.vmware_vmdk_clone:
    hostname: "{{ esxi_hostname }}"
    username: root
    password: "{{ esxi_password }}"
    source: "[datastore1] vm1/vm1.vmdk"
    destination: "[datastore1] vm1/vm1-rdm.vmdk"
    disk_format: rdm
    device: naa.624a93706c1b16ce1c034d1c0638cb69

- name: Convert a thin disk to eager zeroed thick
  community.vmware.vmware_vmdk_clone:
    hostname: "{{ esxi_hostname }}"
    username: root
    password: "{{ esxi_password }}"
    source: /vmfs/volumes/datastore1/vm1/vm1.vmdk
    destination: /vmfs/volumes/datastore1/vm1/vm1-thick.vmdk
    disk_format: eagerzeroedthick
'''

RETURN = r'''
source:
    description:
        - Information about the source disk, in the format returned by M(community.vmware.vmware_vmdk_info).
    returned: always
    type: dict
    sample:
        path: "[datastore1] vm1/vm1.vmdk"
        exists: true
        datastore:
            name: datastore1
            moid: datastore-1001
        provisioning: thin
        capacity_bytes: 42949672960
destination:
    description:
        - Information about the destination disk after the module ran, in the format returned by M(community.vmware.vmware_vmdk_info).
        - In check mode, the destination as it is before the copy.
    returned: always
    type: dict
    sample:
        path: "[datastore1] vm1/vm1-rdm.vmdk"
        exists: true
        datastore:
            name: datastore1
            moid: datastore-1001
        backing_type: RawDiskMappingVer1BackingInfo
        provisioning: rdm
        capacity_bytes: 42949672960
        extents:
            - "[datastore1] vm1/vm1-rdm-rdm.vmdk"
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass
    # handled in base class

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native

from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    vmware_argument_spec
)
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    TaskError
)
from ansible_collections.community.vmware.plugins.module_utils.vmware_vmdk import (
    VmdkFiles,
    is_file_not_found,
    split_ds_path,
    type_short_name
)


DEVICE_PREFIX = '/vmfs/devices/disks/'
# controller type reported by the datastore browser -> adapter type expected by VirtualDiskManager
CONTROLLER_ADAPTERS = {
    'VirtualLsiLogicController': 'lsiLogic',
    'VirtualBusLogicController': 'busLogic',
    'VirtualIDEController': 'ide',
}
DISK_TYPES = {
    'thin': 'thin',
    'zeroedthick': 'preallocated',
    'eagerzeroedthick': 'eagerZeroedThick',
    'rdm': 'rdm',
    'rdmp': 'rdmp',
    '2gbsparse': 'sparse2Gb',
}
RDM_FORMATS = ('rdm', 'rdmp')
THICK_FORMATS = ('zeroedthick', 'eagerzeroedthick')


def same_format(disk_format, source_provisioning):
    """
    Check if a requested format matches the provisioning of the source, which is all that vCenter can copy.
    Args:
        disk_format: str or None, the requested format
        source_provisioning: str or None, the provisioning reported for the source
    Returns:
        bool
    """
    if disk_format is None or disk_format == source_provisioning:
        return True
    # a detached thick disk is reported as 'thick', its zeroing is unknown
    return disk_format in THICK_FORMATS and source_provisioning == 'thick'


def default_format(source_provisioning):
    """
    Return the format that keeps the provisioning of the source on an ESXi host.
    """
    return 'thin' if source_provisioning == 'thin' else 'zeroedthick'


def find_lun(host, device):
    """
    Find a SCSI disk of a host by canonical name, device path or SCSI LUN UUID.
    Args:
        host: vim.HostSystem
        device: str, the device as given by the user
    Returns:
        vim.host.ScsiDisk or None
    """
    name = device.strip()
    if name.startswith(DEVICE_PREFIX):
        name = name[len(DEVICE_PREFIX):]
    for lun in host.config.storageDevice.scsiLun:
        if not isinstance(lun, vim.host.ScsiDisk):
            continue
        if name in (lun.canonicalName, lun.uuid) or DEVICE_PREFIX + name in (lun.deviceName, lun.devicePath):
            return lun
    return None


def lun_volume(host, lun):
    """
    Return the name of the VMFS volume that uses the LUN, or None.
    """
    for mount in host.config.fileSystemVolume.mountInfo or []:
        volume = mount.volume
        if isinstance(volume, vim.host.VmfsVolume):
            for extent in volume.extent or []:
                if extent.diskName == lun.canonicalName:
                    return volume.name
    return None


class VmdkCloneModule(PyVmomi):
    def __init__(self, module):
        super().__init__(module)
        self.files = VmdkFiles(self)
        self.source = self.files.resolve(self.params['source'], 'source')
        self.destination = self.files.resolve(self.params['destination'], 'destination')

    def clone(self):
        """
        Copy the source disk to the destination unless the destination exists and force is not set.
        Returns:
            (bool, dict, dict), whether something changed, the source facts and the destination facts
        """
        source_info = self.files.file_info(self.source)
        if source_info is None:
            self.module.fail_json(msg='Source disk %s does not exist' % self.source.ds_path)
        source_facts = self.files.facts(self.source, source_info)

        destination_info = self.files.file_info(self.destination)
        if destination_info is not None and not self.params['force']:
            destination_facts = self.files.facts(self.destination, destination_info)
            self.warn_on_format_mismatch(destination_facts)
            return False, source_facts, destination_facts

        spec = self.destination_spec(source_info, source_facts)
        if destination_info is not None:
            self.check_unused(self.destination)
        elif not self.folder_exists(self.destination):
            if not self.params['create_folders']:
                self.module.fail_json(msg=(
                    'The folder of %s does not exist. Set create_folders to true to create it' % self.destination.ds_path))
            if not self.module.check_mode:
                self.make_folder(self.destination)

        if self.module.check_mode:
            return True, source_facts, self.files.facts(self.destination, destination_info)

        if destination_info is not None:
            # CopyVirtualDisk ignores its force flag and fails when the destination exists
            self.run_task('delete %s' % self.destination.ds_path, self.content.virtualDiskManager.DeleteVirtualDisk_Task,
                          name=self.destination.ds_path, datacenter=self.destination.datacenter)
        copy_args = dict(
            sourceName=self.source.ds_path, sourceDatacenter=self.source.datacenter,
            destName=self.destination.ds_path, destDatacenter=self.destination.datacenter,
        )
        if spec is not None:
            copy_args['destSpec'] = spec
        self.run_task('copy %s to %s' % (self.source.ds_path, self.destination.ds_path),
                      self.content.virtualDiskManager.CopyVirtualDisk_Task, **copy_args)
        return True, source_facts, self.files.describe(self.destination)

    def destination_spec(self, source_info, source_facts):
        """
        Build the destination specification of the copy, or None for a copy in the source format.
        vCenter does not apply a destination specification, so a format change needs a connection to an ESXi host.
        """
        disk_format = self.params['disk_format']
        if self.is_vcenter():
            if disk_format in RDM_FORMATS or disk_format == '2gbsparse' or not same_format(disk_format, source_facts['provisioning']):
                self.module.fail_json(msg=(
                    'Cloning to disk_format %s needs a connection to an ESXi host: vCenter ignores the destination format '
                    'and copies the disk in its source format (%s). Set hostname to an ESXi host that mounts the datastores%s.'
                    % (disk_format, source_facts['provisioning'] or 'unknown', ' and sees the LUN' if disk_format in RDM_FORMATS else '')
                ))
            return None

        disk_format = disk_format or default_format(source_facts['provisioning'])
        adapter = CONTROLLER_ADAPTERS.get(type_short_name(source_info.controllerType), 'lsiLogic')
        if disk_format in RDM_FORMATS:
            lun = self.check_lun(source_info.capacityKb)
            return vim.VirtualDiskManager.DeviceBackedVirtualDiskSpec(
                diskType=DISK_TYPES[disk_format], adapterType=adapter, device=lun.deviceName)
        return vim.VirtualDiskManager.FileBackedVirtualDiskSpec(
            diskType=DISK_TYPES[disk_format], adapterType=adapter, capacityKb=source_info.capacityKb or 0)

    def check_lun(self, capacity_kb):
        """
        Find the LUN for an RDM copy on the connected ESXi host and check that it can receive the disk.
        Returns:
            vim.host.ScsiDisk
        """
        host = self.get_all_objs_by_type([vim.HostSystem])[0]
        lun = find_lun(host, self.params['device'])
        if lun is None:
            self.module.fail_json(msg='Device %s is not a disk visible to host %s' % (self.params['device'], host.name))
        volume = lun_volume(host, lun)
        if volume is not None:
            self.module.fail_json(msg='Device %s holds the VMFS datastore %s; an RDM needs a LUN without a file system'
                                  % (lun.canonicalName, volume))
        lun_kb = lun.capacity.block * lun.capacity.blockSize // 1024
        if capacity_kb and lun_kb < capacity_kb:
            self.module.fail_json(msg='Device %s has %d KB, less than the %d KB of the source disk'
                                  % (lun.canonicalName, lun_kb, capacity_kb))
        return lun

    def folder_exists(self, path):
        """
        Return True if the folder that holds the disk exists.
        """
        folder, dummy = split_ds_path(path.ds_path)
        spec = vim.host.DatastoreBrowser.SearchSpec(matchPattern=['.'])
        try:
            self.files.wait(path.datastore.browser.SearchDatastore_Task(datastorePath=folder, searchSpec=spec))
        except TaskError as e:
            if is_file_not_found(e):
                return False
            self.module.fail_json(msg='Unable to read %s: %s' % (folder, to_native(e)))
        return True

    def make_folder(self, path):
        """
        Create the folder that holds the disk, with its parents.
        """
        folder, dummy = split_ds_path(path.ds_path)
        try:
            self.content.fileManager.MakeDirectory(name=folder, datacenter=path.datacenter, createParentDirectories=True)
        except vim.fault.FileAlreadyExists:
            pass
        except vmodl.MethodFault as e:
            self.module.fail_json(msg='Unable to create folder %s: %s' % (folder, to_native(e.msg)))

    def check_unused(self, path):
        """
        Fail if a VM uses the disk, which therefore cannot be replaced.
        """
        users = sorted(set(vm.name for vm, dummy_device, dummy_parent in self.files.users(path)))
        if users:
            self.module.fail_json(msg='%s is used by %s and cannot be replaced' % (path.ds_path, ', '.join(users)))

    def warn_on_format_mismatch(self, destination_facts):
        """
        Warn when an existing destination is not of the kind requested, since it is left unchanged.
        """
        disk_format = self.params['disk_format']
        if disk_format is None:
            return
        if (destination_facts['provisioning'] in RDM_FORMATS) != (disk_format in RDM_FORMATS):
            self.module.warn('%s already exists as a %s disk, not %s; set force to true to replace it'
                             % (destination_facts['path'], destination_facts['provisioning'], disk_format))

    def run_task(self, description, method, **kwargs):
        """
        Run a VirtualDiskManager task and fail the module with a readable message if it fails.
        """
        try:
            self.files.wait(method(**kwargs), timeout=self.params['timeout'])
        except TaskError as e:
            self.module.fail_json(msg='Unable to %s: %s' % (description, to_native(e)))


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        source=dict(type='str', required=True),
        destination=dict(type='str', required=True),
        disk_format=dict(type='str', required=False, choices=list(DISK_TYPES)),
        device=dict(type='str', required=False),
        create_folders=dict(type='bool', required=False, default=False),
        force=dict(type='bool', required=False, default=False),
        datacenter=dict(type='str', required=False),
        timeout=dict(type='int', required=False, default=3600),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        required_if=[
            ('disk_format', 'rdm', ['device']),
            ('disk_format', 'rdmp', ['device']),
        ],
        supports_check_mode=True,
    )

    vmdk_clone = VmdkCloneModule(module)
    changed, source, destination = vmdk_clone.clone()
    module.exit_json(changed=changed, source=source, destination=destination)


if __name__ == '__main__':
    main()
