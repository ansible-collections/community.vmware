#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2020, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_scsidisk_info
short_description: Gather information about SCSI disk attached to the given ESXi
description:
- This module can be used to gather information about SCSI disk attached to the given ESXi.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  esxi_hostname:
    description:
    - Name of the host system to work with.
    - SCSI disk information about this ESXi server will be returned.
    - This parameter is required if O(cluster_name) is not specified.
    type: str
  cluster_name:
    description:
    - Name of the cluster from which all host systems will be used.
    - SCSI disk information about each ESXi server will be returned for the given cluster.
    - This parameter is required if O(esxi_hostname) is not specified.
    type: str
extends_documentation_fragment:
- vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Gather information SCSI disk attached to the given ESXi
  community.vmware.vmware_host_scsidisk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost

- name: Gather information of all host systems from the given cluster
  community.vmware.vmware_host_scsidisk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
'''

RETURN = r'''
hosts_scsidisk_info:
    description: metadata about host system SCSI disk information
    returned: always
    type: dict
    sample: {
        "10.65.201.106": [
            {
                "block": 41943040,
                "block_size": 512,
                "canonical_name": "t10.ATA_QEMU_HARDDISK_QM00001_",
                "device_name": "/vmfs/devices/disks/t10.ATA_QEMU_HARDDISK_QM00001_",
                "device_path": "/vmfs/devices/disks/t10.ATA_QEMU_HARDDISK_QM00001_",
                "device_type": "disk",
                "display_name": "Local ATA Disk (t10.ATA_QEMU_HARDDISK_QM00001_)",
                "key": "key-vim.host.ScsiDisk-0100000000514d30303030312020202020202020202020202051454d552048",
                "local_disk": true,
                "lun_type": "disk",
                "model": "QEMU HARDDISK   ",
                "perenniallyReserved": null,
                "protocol_endpoint": false,
                "revision": "1.5.",
                "scsi_disk_type": "native512",
                "scsi_level": 5,
                "serial_number": "unavailable",
                "ssd": false,
                "uuid": "0100000000514d30303030312020202020202020202020202051454d552048",
                "vStorageSupport": "vStorageUnsupported",
                "vendor": "ATA     "
            }
        ]
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class VmwareHostDiskManager(PyVmomi):
    def __init__(self, module):
        super(VmwareHostDiskManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name')
        esxi_host_name = self.params.get('esxi_hostname')
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system with given configuration.")

    def gather_disk_info(self):
        """
        Gather information about SCSI disks

        """
        results = dict(changed=False, hosts_scsidisk_info=dict())
        for host in self.hosts:
            disk_info = []
            storage_system = host.configManager.storageSystem
            for disk in storage_system.storageDeviceInfo.scsiLun:
                temp_disk_info = {
                    'device_name': disk.deviceName,
                    'device_type': disk.deviceType,
                    'key': disk.key,
                    'uuid': disk.uuid,
                    'canonical_name': disk.canonicalName,
                    'display_name': disk.displayName,
                    'lun_type': disk.lunType,
                    'vendor': disk.vendor,
                    'model': disk.model,
                    'revision': disk.revision,
                    'scsi_level': disk.scsiLevel,
                    'serial_number': disk.serialNumber,
                    'vStorageSupport': disk.vStorageSupport,
                    'protocol_endpoint': disk.protocolEndpoint,
                    'perenniallyReserved': disk.perenniallyReserved,
                    'block_size': None,
                    'block': None,
                    'device_path': '',
                    'ssd': False,
                    'local_disk': False,
                    'scsi_disk_type': None,
                }
                if hasattr(disk, 'capacity'):
                    temp_disk_info['block_size'] = disk.capacity.blockSize
                    temp_disk_info['block'] = disk.capacity.block
                if hasattr(disk, 'devicePath'):
                    temp_disk_info['device_path'] = disk.devicePath
                if hasattr(disk, 'ssd'):
                    temp_disk_info['ssd'] = disk.ssd
                if hasattr(disk, 'localDisk'):
                    temp_disk_info['local_disk'] = disk.localDisk
                if hasattr(disk, 'scsiDiskType'):
                    temp_disk_info['scsi_disk_type'] = disk.scsiDiskType

                disk_info.append(temp_disk_info)
            results['hosts_scsidisk_info'][host.name] = disk_info
        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=False),
        cluster_name=dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ]
    )

    host_scsidisk_manager = VmwareHostDiskManager(module)
    host_scsidisk_manager.gather_disk_info()


if __name__ == '__main__':
    main()
