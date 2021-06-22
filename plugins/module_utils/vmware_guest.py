#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from pyVmomi import vim
from random import randint
from ansible.module_utils.common.network import is_mac


class PyVmomiDeviceHelper(object):
    """ This class is a helper to create easily VMware Objects for PyVmomiHelper """

    def __init__(self, module):
        self.module = module
        # This is not used for the multiple controller with multiple disks scenario,
        # disk unit number can not be None
        # self.next_disk_unit_number = 0
        self.scsi_device_type = {
            'lsilogic': vim.vm.device.VirtualLsiLogicController,
            'paravirtual': vim.vm.device.ParaVirtualSCSIController,
            'buslogic': vim.vm.device.VirtualBusLogicController,
            'lsilogicsas': vim.vm.device.VirtualLsiLogicSASController,
        }

    def create_scsi_controller(self, scsi_type, bus_number):
        scsi_ctl = vim.vm.device.VirtualDeviceSpec()
        scsi_ctl.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        scsi_device = self.scsi_device_type.get(scsi_type, vim.vm.device.ParaVirtualSCSIController)
        scsi_ctl.device = scsi_device()
        scsi_ctl.device.busNumber = bus_number
        # While creating a new SCSI controller, temporary key value
        # should be unique negative integers
        scsi_ctl.device.key = -randint(1000, 9999)
        scsi_ctl.device.hotAddRemove = True
        scsi_ctl.device.sharedBus = 'noSharing'
        scsi_ctl.device.scsiCtlrUnitNumber = 7

        return scsi_ctl

    def is_scsi_controller(self, device):
        return isinstance(device, tuple(self.scsi_device_type.values()))

    @staticmethod
    def create_sata_controller(bus_number):
        sata_ctl = vim.vm.device.VirtualDeviceSpec()
        sata_ctl.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        sata_ctl.device = vim.vm.device.VirtualAHCIController()
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

    def create_disk_controller(self, ctl_type, ctl_number):
        disk_ctl = None
        if ctl_type in ['buslogic', 'paravirtual', 'lsilogic', 'lsilogicsas']:
            disk_ctl = self.create_scsi_controller(ctl_type, ctl_number)
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

    def get_device(self, device_type, name):
        nic_dict = dict(pcnet32=vim.vm.device.VirtualPCNet32(),
                        vmxnet2=vim.vm.device.VirtualVmxnet2(),
                        vmxnet3=vim.vm.device.VirtualVmxnet3(),
                        e1000=vim.vm.device.VirtualE1000(),
                        e1000e=vim.vm.device.VirtualE1000e(),
                        sriov=vim.vm.device.VirtualSriovEthernetCard(),
                        )
        if device_type in nic_dict:
            return nic_dict[device_type]
        else:
            self.module.fail_json(msg='Invalid device_type "%s"'
                                      ' for network "%s"' % (device_type, name))

    def create_nic(self, device_type, device_label, device_infos):
        nic = vim.vm.device.VirtualDeviceSpec()
        nic.device = self.get_device(device_type, device_infos['name'])
        nic.device.key = -randint(25000, 29999)
        nic.device.wakeOnLanEnabled = bool(device_infos.get('wake_on_lan', True))
        nic.device.deviceInfo = vim.Description()
        nic.device.deviceInfo.label = device_label
        nic.device.deviceInfo.summary = device_infos['name']
        nic.device.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        nic.device.connectable.startConnected = bool(device_infos.get('start_connected', True))
        nic.device.connectable.allowGuestControl = bool(device_infos.get('allow_guest_control', True))
        nic.device.connectable.connected = bool(device_infos.get('connected', True))
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
