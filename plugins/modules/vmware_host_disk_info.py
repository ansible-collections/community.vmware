#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'author': 'Matt Proud'
}

DOCUMENTATION = '''
---
module: vmware_host_disk_info
short_description: Gathers information about disks attached to given ESXi host/s
description:
- This module returns information about disks attached to given ESXi host/s
- If cluster_name is provide, then disk information about all hosts from given cluster will be returned.
- If esxi_hostname is provided, then disk information about given host system will be returned.
authot:
- Matt Proud
notes:
- Tested on vSphere 6.7 and 7.0
requirements:
- python >= 2.6
- PyVmomi
options:

'''

EXAMPLES = '''
- name: Gather info about vmhbas of all ESXi Host in the given Cluster
  vmware_host_disk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_host_vmhbas

- name: Gather info about vmhbas of an ESXi Host
  vmware_host_disk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_vmhbas
'''

RETURN = '''
"hosts_disk_info": {
    "192.168.0.182": [
        {
            "canonical_name": "naa.6000c296ed6217bd61df35622eb21a3a",
            "capacity_mb": 4096,
            "device_path": "/vmfs/devices/disks/naa.6000c296ed6217bd61df35622eb21a3a",
            "device_type": "disk",
            "device_ctd_list": [
                "vmhba0:C0:T1:L0"
            ],
            "disk_uid": "key-vim.host.ScsiDisk-02000000006000c296ed6217bd61df35622eb21a3a566972747561",
            "display_name": "Local VMware Disk (naa.6000c296ed6217bd61df35622eb21a3a)"
        },
        {
            "canonical_name": "naa.6000c2968ad7142d93faae527fe8822b",
            "capacity_mb": 204800,
            "device_path": "/vmfs/devices/disks/naa.6000c2968ad7142d93faae527fe8822b",
            "device_type": "disk",
            "device_ctd_list": [
                "vmhba0:C0:T3:L0"
            ],
            "disk_uid": "key-vim.host.ScsiDisk-02000000006000c2968ad7142d93faae527fe8822b566972747561",
            "display_name": "Local VMware Disk (naa.6000c2968ad7142d93faae527fe8822b)"
        },]
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import vmware_argument_spec, PyVmomi, get_all_objs

class HostDiskInfo(PyVmomi):
    """Class to return host disk info"""

    def __init__(self, module):
        super(HostDiskInfo, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system.")

    def gather_host_disk_info(self):
        hosts_disk_info = {}
        for host in self.hosts:
            host_disk_info = []
            storage_system = host.configManager.storageSystem.storageDeviceInfo
            # Collect target lookup for naa devices
            lun_lookup = {}
            for lun in storage_system.multipathInfo.lun:
                key = lun.lun
                paths = []
                for path in lun.path:
                    paths.append(path.name)
                lun_lookup[key] = paths

            for disk in storage_system.scsiLun:
                canonical_name = disk.canonicalName
                try:
                    capacity = int(disk.capacity.block * disk.capacity.blockSize / 1048576)
                except AttributeError:
                    capacity = 0
                try:
                    device_path = disk.devicePath
                except AttributeError:
                    device_path = ""
                device_type = disk.deviceType
                display_name = disk.displayName
                disk_uid = disk.key
                device_ctd_list = lun_lookup[disk_uid]
                
                disk_dict = {"capacity_mb": capacity,
                                        "device_path": device_path,
                                            "device_type": device_type,
                                            "display_name": display_name,
                                            "disk_uid": disk_uid,
                                            "device_ctd_list": device_ctd_list,
                                            "canonical_name": canonical_name}
                host_disk_info.append(disk_dict)

            hosts_disk_info[host.name] = host_disk_info
        
        return hosts_disk_info



def main():
    """Main"""
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str', required=False),
        esxi_hostname=dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True,
    )

    host_disk_mgr = HostDiskInfo(module)
    module.exit_json(changed=False, hosts_disk_facts=host_disk_mgr.gather_host_disk_info())


if __name__ == "__main__":
    main()