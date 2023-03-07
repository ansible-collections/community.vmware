# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import traceback
from random import randint
from ansible.module_utils.common.network import is_mac
from ansible.module_utils.basic import missing_required_lib

PYVMOMI_IMP_ERR = None
try:
    from pyVmomi import vim
    HAS_PYVMOMI = True
except ImportError:
    PYVMOMI_IMP_ERR = traceback.format_exc()
    HAS_PYVMOMI = False


class PyVmomiDeviceHelper(object):
    """ This class is a helper to create easily VMware Objects for PyVmomiHelper """

    def __init__(self, module):
        if not HAS_PYVMOMI:
            module.fail_json(msg=missing_required_lib('PyVmomi'),
                             exception=PYVMOMI_IMP_ERR)

        self.module = module
        # This is not used for the multiple controller with multiple disks scenario,
        # disk unit number can not be None
        # self.next_disk_unit_number = 0
        self.scsi_device_type = {
            'lsilogic': vim.vm.device.VirtualLsiLogicController,
            'paravirtual': vim.vm.device.ParaVirtualSCSIController,
            'buslogic': vim.vm.device.VirtualBusLogicController,
            'lsilogicsas': vim.vm.device.VirtualLsiLogicSASController
        }
        self.sata_device_type = vim.vm.device.VirtualAHCIController
        self.nvme_device_type = vim.vm.device.VirtualNVMEController
        self.ide_device_type = vim.vm.device.VirtualIDEController
        self.disk_ctl_device_type = self.scsi_device_type.copy()
        self.disk_ctl_device_type.update({
            'sata': self.sata_device_type,
            'nvme': self.nvme_device_type,
            'ide': self.ide_device_type
        })
        self.usb_device_type = {
            'usb2': vim.vm.device.VirtualUSBController,
            'usb3': vim.vm.device.VirtualUSBXHCIController
        }
        self.nic_device_type = {
            'pcnet32': vim.vm.device.VirtualPCNet32,
            'vmxnet2': vim.vm.device.VirtualVmxnet2,
            'vmxnet3': vim.vm.device.VirtualVmxnet3,
            'e1000': vim.vm.device.VirtualE1000,
            'e1000e': vim.vm.device.VirtualE1000e,
            'sriov': vim.vm.device.VirtualSriovEthernetCard,
            'pvrdma': vim.vm.device.VirtualVmxnet3Vrdma
        }

    def create_scsi_controller(self, scsi_type, bus_number, bus_sharing='noSharing'):
        """
        Create SCSI Controller with given SCSI Type and SCSI Bus Number
        Args:
            scsi_type: Type of SCSI
            bus_number: SCSI Bus number to be assigned
            bus_sharing: noSharing, virtualSharing, physicalSharing

        Returns: Virtual device spec for SCSI Controller

        """
        scsi_ctl = vim.vm.device.VirtualDeviceSpec()
        scsi_ctl.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        scsi_device = self.scsi_device_type.get(scsi_type, vim.vm.device.ParaVirtualSCSIController)
        scsi_ctl.device = scsi_device()
        scsi_ctl.device.deviceInfo = vim.Description()
        scsi_ctl.device.busNumber = bus_number
        # While creating a new SCSI controller, temporary key value
        # should be unique negative integers
        scsi_ctl.device.key = -randint(1000, 9999)
        scsi_ctl.device.hotAddRemove = True
        scsi_ctl.device.sharedBus = bus_sharing
        scsi_ctl.device.scsiCtlrUnitNumber = 7

        return scsi_ctl

    def is_scsi_controller(self, device):
        return isinstance(device, tuple(self.scsi_device_type.values()))

    @staticmethod
    def create_sata_controller(bus_number):
        sata_ctl = vim.vm.device.VirtualDeviceSpec()
        sata_ctl.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        sata_ctl.device = vim.vm.device.VirtualAHCIController()
        sata_ctl.device.deviceInfo = vim.Description()
        sata_ctl.device.busNumber = bus_number
        sata_ctl.device.key = -randint(15000, 19999)

        return sata_ctl

    @staticmethod
    def is_sata_controller(device):
        return isinstance(device, vim.vm.device.VirtualAHCIController)

    @staticmethod
    def create_nvme_controller(bus_number):
        nvme_ctl = vim.vm.device.VirtualDeviceSpec()
        nvme_ctl.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        nvme_ctl.device = vim.vm.device.VirtualNVMEController()
        nvme_ctl.device.deviceInfo = vim.Description()
        nvme_ctl.device.key = -randint(31000, 39999)
        nvme_ctl.device.busNumber = bus_number

        return nvme_ctl

    @staticmethod
    def is_nvme_controller(device):
        return isinstance(device, vim.vm.device.VirtualNVMEController)

    def create_disk_controller(self, ctl_type, ctl_number, bus_sharing='noSharing'):
        disk_ctl = None
        if ctl_type in self.scsi_device_type.keys():
            disk_ctl = self.create_scsi_controller(ctl_type, ctl_number, bus_sharing)
        if ctl_type == 'sata':
            disk_ctl = self.create_sata_controller(ctl_number)
        if ctl_type == 'nvme':
            disk_ctl = self.create_nvme_controller(ctl_number)

        return disk_ctl

    def get_controller_disks(self, vm_obj, ctl_type, ctl_number):
        disk_controller = None
        disk_list = []
        disk_key_list = []
        if vm_obj is None:
            return disk_controller, disk_list
        disk_controller_type = self.scsi_device_type.copy()
        disk_controller_type.update({'sata': vim.vm.device.VirtualAHCIController, 'nvme': vim.vm.device.VirtualNVMEController})
        for device in vm_obj.config.hardware.device:
            if isinstance(device, disk_controller_type[ctl_type]):
                if device.busNumber == ctl_number:
                    disk_controller = device
                    disk_key_list = device.device
                    break
        if len(disk_key_list) != 0:
            for device in vm_obj.config.hardware.device:
                if isinstance(device, vim.vm.device.VirtualDisk):
                    if device.key in disk_key_list:
                        disk_list.append(device)

        return disk_controller, disk_list

    @staticmethod
    def create_ide_controller(bus_number=0):
        ide_ctl = vim.vm.device.VirtualDeviceSpec()
        ide_ctl.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        ide_ctl.device = vim.vm.device.VirtualIDEController()
        ide_ctl.device.deviceInfo = vim.Description()
        # While creating a new IDE controller, temporary key value
        # should be unique negative integers
        ide_ctl.device.key = -randint(200, 299)
        ide_ctl.device.busNumber = bus_number

        return ide_ctl

    @staticmethod
    def create_cdrom(ctl_device, cdrom_type, iso_path=None, unit_number=0):
        cdrom_spec = vim.vm.device.VirtualDeviceSpec()
        cdrom_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        cdrom_spec.device = vim.vm.device.VirtualCdrom()
        cdrom_spec.device.controllerKey = ctl_device.key
        if isinstance(ctl_device, vim.vm.device.VirtualIDEController):
            cdrom_spec.device.key = -randint(3000, 3999)
        elif isinstance(ctl_device, vim.vm.device.VirtualAHCIController):
            cdrom_spec.device.key = -randint(16000, 16999)
        cdrom_spec.device.unitNumber = unit_number
        cdrom_spec.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        cdrom_spec.device.connectable.allowGuestControl = True
        cdrom_spec.device.connectable.startConnected = (cdrom_type != "none")
        if cdrom_type in ["none", "client"]:
            cdrom_spec.device.backing = vim.vm.device.VirtualCdrom.RemotePassthroughBackingInfo()
        elif cdrom_type == "iso":
            cdrom_spec.device.backing = vim.vm.device.VirtualCdrom.IsoBackingInfo(fileName=iso_path)
            cdrom_spec.device.connectable.connected = True

        return cdrom_spec

    @staticmethod
    def is_equal_cdrom(vm_obj, cdrom_device, cdrom_type, iso_path):
        if cdrom_type == "none":
            return (
                isinstance(
                    cdrom_device.backing,
                    vim.vm.device.VirtualCdrom.RemotePassthroughBackingInfo,
                )
                and cdrom_device.connectable.allowGuestControl
                and not cdrom_device.connectable.startConnected
                and (
                    vm_obj.runtime.powerState != vim.VirtualMachinePowerState.poweredOn
                    or not cdrom_device.connectable.connected
                )
            )
        elif cdrom_type == "client":
            return (
                isinstance(
                    cdrom_device.backing,
                    vim.vm.device.VirtualCdrom.RemotePassthroughBackingInfo,
                )
                and cdrom_device.connectable.allowGuestControl
                and cdrom_device.connectable.startConnected
                and (
                    vm_obj.runtime.powerState != vim.VirtualMachinePowerState.poweredOn
                    or cdrom_device.connectable.connected
                )
            )
        elif cdrom_type == "iso":
            return (
                isinstance(
                    cdrom_device.backing, vim.vm.device.VirtualCdrom.IsoBackingInfo
                )
                and cdrom_device.backing.fileName == iso_path
                and cdrom_device.connectable.allowGuestControl
                and cdrom_device.connectable.startConnected
                and (
                    vm_obj.runtime.powerState != vim.VirtualMachinePowerState.poweredOn
                    or cdrom_device.connectable.connected
                )
            )

    @staticmethod
    def update_cdrom_config(vm_obj, cdrom_spec, cdrom_device, iso_path=None):
        # Updating an existing CD-ROM
        if cdrom_spec["type"] in ["client", "none"]:
            cdrom_device.backing = vim.vm.device.VirtualCdrom.RemotePassthroughBackingInfo()
        elif cdrom_spec["type"] == "iso" and iso_path is not None:
            cdrom_device.backing = vim.vm.device.VirtualCdrom.IsoBackingInfo(fileName=iso_path)
        cdrom_device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        cdrom_device.connectable.allowGuestControl = True
        cdrom_device.connectable.startConnected = (cdrom_spec["type"] != "none")
        if vm_obj and vm_obj.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
            cdrom_device.connectable.connected = (cdrom_spec["type"] != "none")

    def remove_cdrom(self, cdrom_device):
        cdrom_spec = vim.vm.device.VirtualDeviceSpec()
        cdrom_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.remove
        cdrom_spec.device = cdrom_device

        return cdrom_spec

    def create_hard_disk(self, disk_ctl, disk_index=None):
        diskspec = vim.vm.device.VirtualDeviceSpec()
        diskspec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        diskspec.device = vim.vm.device.VirtualDisk()
        diskspec.device.key = -randint(20000, 24999)
        diskspec.device.backing = vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
        diskspec.device.controllerKey = disk_ctl.device.key

        if self.is_scsi_controller(disk_ctl.device):
            # one scsi controller attach 0-15 (except 7) disks
            if disk_index is None:
                self.module.fail_json(msg='unitNumber for sata disk is None.')
            else:
                if disk_index == 7 or disk_index > 15:
                    self.module.fail_json(msg='Invalid scsi disk unitNumber, valid 0-15(except 7).')
                else:
                    diskspec.device.unitNumber = disk_index
        elif self.is_sata_controller(disk_ctl.device):
            # one sata controller attach 0-29 disks
            if disk_index is None:
                self.module.fail_json(msg='unitNumber for sata disk is None.')
            else:
                if disk_index > 29:
                    self.module.fail_json(msg='Invalid sata disk unitNumber, valid 0-29.')
                else:
                    diskspec.device.unitNumber = disk_index
        elif self.is_nvme_controller(disk_ctl.device):
            # one nvme controller attach 0-14 disks
            if disk_index is None:
                self.module.fail_json(msg='unitNumber for nvme disk is None.')
            else:
                if disk_index > 14:
                    self.module.fail_json(msg='Invalid nvme disk unitNumber, valid 0-14.')
                else:
                    diskspec.device.unitNumber = disk_index

        return diskspec

    def create_nic(self, device_type, device_label, device_infos):
        nic = vim.vm.device.VirtualDeviceSpec()
        nic_device = self.nic_device_type.get(device_type)
        nic.device = nic_device()
        nic.device.key = -randint(25000, 29999)
        nic.device.wakeOnLanEnabled = bool(device_infos.get('wake_on_lan', True))
        nic.device.deviceInfo = vim.Description()
        nic.device.deviceInfo.label = device_label
        nic.device.deviceInfo.summary = device_infos['name']
        nic.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        nic.device.connectable.startConnected = bool(device_infos.get('start_connected', True))
        nic.device.connectable.allowGuestControl = bool(device_infos.get('allow_guest_control', True))
        nic.device.connectable.connected = bool(device_infos.get('connected', True))
        if device_type == 'sriov':
            pf_backing = device_infos.get('physical_function_backing', None)
            vf_backing = device_infos.get('virtual_function_backing', None)

            nic.device.allowGuestOSMtuChange = bool(device_infos.get('allow_guest_os_mtu_change', True))
            nic.device.sriovBacking = vim.vm.device.VirtualSriovEthernetCard.SriovBackingInfo()
            if pf_backing is not None:
                nic.device.sriovBacking.physicalFunctionBacking = vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo()
                nic.device.sriovBacking.physicalFunctionBacking.id = pf_backing
            if vf_backing is not None:
                nic.device.sriovBacking.virtualFunctionBacking = vim.vm.device.VirtualPCIPassthrough.DeviceBackingInfo()
                nic.device.sriovBacking.virtualFunctionBacking.id = vf_backing
        if 'mac' in device_infos and is_mac(device_infos['mac']):
            nic.device.addressType = 'manual'
            nic.device.macAddress = device_infos['mac']
        else:
            nic.device.addressType = 'generated'

        return nic

    def integer_value(self, input_value, name):
        """
        Function to return int value for given input, else return error
        Args:
            input_value: Input value to retrieve int value from
            name:  Name of the Input value (used to build error message)
        Returns: (int) if integer value can be obtained, otherwise will send a error message.
        """
        if isinstance(input_value, int):
            return input_value
        elif isinstance(input_value, str) and input_value.isdigit():
            return int(input_value)
        else:
            self.module.fail_json(msg='"%s" attribute should be an'
                                  ' integer value.' % name)

    def create_nvdimm_controller(self):
        nvdimm_ctl = vim.vm.device.VirtualDeviceSpec()
        nvdimm_ctl.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        nvdimm_ctl.device = vim.vm.device.VirtualNVDIMMController()
        nvdimm_ctl.device.deviceInfo = vim.Description()
        nvdimm_ctl.device.key = -randint(27000, 27999)

        return nvdimm_ctl

    @staticmethod
    def is_nvdimm_controller(device):
        return isinstance(device, vim.vm.device.VirtualNVDIMMController)

    def create_nvdimm_device(self, nvdimm_ctl_dev_key, pmem_profile_id, nvdimm_dev_size_mb=1024):
        nvdimm_dev_spec = vim.vm.device.VirtualDeviceSpec()
        nvdimm_dev_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        nvdimm_dev_spec.fileOperation = vim.vm.device.VirtualDeviceSpec.FileOperation.create
        nvdimm_dev_spec.device = vim.vm.device.VirtualNVDIMM()
        nvdimm_dev_spec.device.controllerKey = nvdimm_ctl_dev_key
        nvdimm_dev_spec.device.key = -randint(28000, 28999)
        nvdimm_dev_spec.device.capacityInMB = nvdimm_dev_size_mb
        nvdimm_dev_spec.device.deviceInfo = vim.Description()
        nvdimm_dev_spec.device.backing = vim.vm.device.VirtualNVDIMM.BackingInfo()
        if pmem_profile_id is not None:
            profile = vim.vm.DefinedProfileSpec()
            profile.profileId = pmem_profile_id
            nvdimm_dev_spec.profile = [profile]

        return nvdimm_dev_spec

    @staticmethod
    def is_nvdimm_device(device):
        return isinstance(device, vim.vm.device.VirtualNVDIMM)

    def find_nvdimm_by_label(self, nvdimm_label, nvdimm_devices):
        nvdimm_dev = None
        for nvdimm in nvdimm_devices:
            if nvdimm.deviceInfo.label == nvdimm_label:
                nvdimm_dev = nvdimm

        return nvdimm_dev

    def remove_nvdimm(self, nvdimm_device):
        nvdimm_spec = vim.vm.device.VirtualDeviceSpec()
        nvdimm_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.remove
        nvdimm_spec.fileOperation = vim.vm.device.VirtualDeviceSpec.FileOperation.destroy
        nvdimm_spec.device = nvdimm_device

        return nvdimm_spec

    def update_nvdimm_config(self, nvdimm_device, nvdimm_size):
        nvdimm_spec = vim.vm.device.VirtualDeviceSpec()
        nvdimm_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
        nvdimm_spec.device = nvdimm_device
        nvdimm_device.capacityInMB = nvdimm_size

        return nvdimm_spec

    def is_tpm_device(self, device):
        return isinstance(device, vim.vm.device.VirtualTPM)

    def create_tpm(self):
        vtpm_device_spec = vim.vm.device.VirtualDeviceSpec()
        vtpm_device_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        vtpm_device_spec.device = vim.vm.device.VirtualTPM()
        vtpm_device_spec.device.deviceInfo = vim.Description()

        return vtpm_device_spec

    def remove_tpm(self, vtpm_device):
        vtpm_device_spec = vim.vm.device.VirtualDeviceSpec()
        vtpm_device_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.remove
        vtpm_device_spec.device = vtpm_device

        return vtpm_device_spec

    def gather_disk_info(self, vm_obj):
        """
        Gather information about VM's disks
        Args:
            vm_obj: Managed object of virtual machine
        Returns: A list of dict containing disks information
        """
        controller_info = dict()
        disks_info = dict()
        if vm_obj is None:
            return disks_info

        controller_index = 0
        for controller in vm_obj.config.hardware.device:
            for name, type in self.disk_ctl_device_type.items():
                if isinstance(controller, type):
                    controller_info[controller_index] = dict(
                        key=controller.key,
                        controller_type=name,
                        bus_number=controller.busNumber,
                        devices=controller.device
                    )
                    controller_index += 1

        disk_index = 0
        for disk in vm_obj.config.hardware.device:
            if isinstance(disk, vim.vm.device.VirtualDisk):
                if disk.storageIOAllocation is None:
                    disk.storageIOAllocation = vim.StorageResourceManager.IOAllocationInfo()
                    disk.storageIOAllocation.shares = vim.SharesInfo()

                if disk.shares is None:
                    disk.shares = vim.SharesInfo()

                disks_info[disk_index] = dict(
                    key=disk.key,
                    label=disk.deviceInfo.label,
                    summary=disk.deviceInfo.summary,
                    backing_filename=disk.backing.fileName,
                    backing_datastore=disk.backing.datastore.name,
                    backing_sharing=disk.backing.sharing if hasattr(disk.backing, 'sharing') else None,
                    backing_uuid=disk.backing.uuid if hasattr(disk.backing, 'uuid') else None,
                    backing_writethrough=disk.backing.writeThrough if hasattr(disk.backing, 'writeThrough') else None,
                    backing_diskmode=disk.backing.diskMode if hasattr(disk.backing, 'diskMode') else None,
                    backing_disk_mode=disk.backing.diskMode if hasattr(disk.backing, 'diskMode') else None,
                    iolimit_limit=disk.storageIOAllocation.limit,
                    iolimit_shares_level=disk.storageIOAllocation.shares.level,
                    iolimit_shares_limit=disk.storageIOAllocation.shares.shares,
                    shares_level=disk.shares.level,
                    shares_limit=disk.shares.shares,
                    controller_key=disk.controllerKey,
                    unit_number=disk.unitNumber,
                    capacity_in_kb=disk.capacityInKB,
                    capacity_in_bytes=disk.capacityInBytes,
                )
                if isinstance(disk.backing, vim.vm.device.VirtualDisk.FlatVer1BackingInfo):
                    disks_info[disk_index]['backing_type'] = 'FlatVer1'

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.FlatVer2BackingInfo):
                    disks_info[disk_index]['backing_type'] = 'FlatVer2'
                    disks_info[disk_index]['backing_thinprovisioned'] = disk.backing.thinProvisioned
                    disks_info[disk_index]['backing_eagerlyscrub'] = disk.backing.eagerlyScrub

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.LocalPMemBackingInfo):
                    disks_info[disk_index]['backing_type'] = 'LocalPMem'
                    disks_info[disk_index]['backing_volumeuuid'] = disk.backing.volumeUUID

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.PartitionedRawDiskVer2BackingInfo):
                    disks_info[disk_index]['backing_type'] = 'PartitionedRawDiskVer2'
                    disks_info[disk_index]['backing_descriptorfilename'] = disk.backing.descriptorFileName

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo):
                    disks_info[disk_index]['backing_type'] = 'RawDiskMappingVer1'
                    disks_info[disk_index]['backing_devicename'] = disk.backing.deviceName
                    disks_info[disk_index]['backing_lunuuid'] = disk.backing.lunUuid
                    disks_info[disk_index]['backing_compatibility_mode'] = disk.backing.compatibilityMode

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo):
                    disks_info[disk_index]['backing_type'] = 'RawDiskVer2'
                    disks_info[disk_index]['backing_descriptorfilename'] = disk.backing.descriptorFileName

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.SeSparseBackingInfo):
                    disks_info[disk_index]['backing_type'] = 'SeSparse'

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.SparseVer1BackingInfo):
                    disks_info[disk_index]['backing_type'] = 'SparseVer1'
                    disks_info[disk_index]['backing_spaceusedinkb'] = disk.backing.spaceUsedInKB
                    disks_info[disk_index]['backing_split'] = disk.backing.split

                elif isinstance(disk.backing, vim.vm.device.VirtualDisk.SparseVer2BackingInfo):
                    disks_info[disk_index]['backing_type'] = 'SparseVer2'
                    disks_info[disk_index]['backing_spaceusedinkb'] = disk.backing.spaceUsedInKB
                    disks_info[disk_index]['backing_split'] = disk.backing.split

                for controller_index in range(len(controller_info)):
                    if controller_info[controller_index]['key'] == disks_info[disk_index]['controller_key']:
                        disks_info[disk_index]['controller_bus_number'] = controller_info[controller_index]['bus_number']
                        disks_info[disk_index]['controller_type'] = controller_info[controller_index]['controller_type']

                disk_index += 1
        return disks_info
