#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2023, Pure Storage, Inc.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_vmfs_datastore
short_description: Manage vmfs datastores on ESXi host
description:
- This module can be used to mount/unmount vmfs datastores on an ESXi host.
- This module only supports VMFS datastores.
- For VMFS datastore, available device must already be connected on ESXi host.
- The VMFS volume must have a single extent (usually the case since VMFS-5 as datastore size was increase from 2TB to 64TB, which diminishes the need for multiple extents).
author:
- Ryan BADAÏ (@ryanb74) <ryan.badai@dbi-services.com>
- Ludovic Rivallain (@lrivallain) <ludovic.rivallain@gmail.com>
- Christian Kotte (@ckotte) <christian.kotte@gmx.de>
- Eugenio Grosso (@genegr) <eugenio.grosso@purestorage.com>
options:
  datastore_name:
    description:
    - Name of the datastore to mount/unmount.
    - Datastore must have the same name as the VMFS volume
    required: true
    type: str
  esxi_hostname:
    description:
    - ESXi hostname to manage the datastore.
    - Required when used with a vcenter
    type: str
    required: false
  hostname:
    description:
    - vcenter hostname to manage the datastore.
    type: str
    required: true
  state:
    description:
    - "mounted: Mount VMFS datastore on host if datastore is not mounted else do nothing."
    - "unmounted: Unmount VMFS datastore if datastore is mounted else do nothing."
    default: mounted
    choices: [ mounted, unmounted ]
    type: str
seealso:
- VMware vSphere API Reference Documentation : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/right-pane.html
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Mount VMFS datastores to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: '{{ item.name }}'
      esxi_hostname: '{{ inventory_hostname }}'
      state: mounted
  delegate_to: localhost

- name: Remove/Umount Datastores from a ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      datastore_name: NasDS_vol01
      state: unmounted
  delegate_to: localhost
'''

RETURN = r'''
result:
  description: A string that describes whether the mount/unmount was successfully performed.
  returned: success or changed
  type: str
  sample:
    - Datastore datastore_name on host example.com successfully unmounted.
    - Datastore datastore_name on host example.com successfully mounted.
    - Datastore datastore_name is already unmounted.
    - Datastore datastore_name is already mounted.
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import vmware_argument_spec, find_obj
from ansible_collections.community.vmware.plugins.module_utils.vmware_sms import SMS
from ansible.module_utils._text import to_native


class VMwareHostVmfsDatastore(SMS):
    def __init__(self, module):
        super(VMwareHostVmfsDatastore, self).__init__(module)

        self.datastore_name = module.params['datastore_name']
        self.esxi_hostname = module.params['esxi_hostname']
        self.state = module.params['state']

        if self.is_vcenter():
            if not self.esxi_hostname:
                self.module.fail_json(msg="esxi_hostname is mandatory with a vcenter")
            self.esxi = self.find_hostsystem_by_name(self.esxi_hostname)
            if self.esxi is None:
                self.module.fail_json(msg="Failed to find ESXi hostname %s" % self.esxi_hostname)
        else:
            self.esxi = find_obj(self.content, [vim.HostSystem], None)

    def process_state(self):
        """Evaluates what must be done based on current state"""
        ds_states = {
            'unmounted': {
                'mounted': self.unmount_vmfs_datastore_from_host,
                'unmounted': lambda: self.module.exit_json(changed=False, result="Datastore %s is already unmounted." % self.datastore_name)
            },
            'mounted': {
                'mounted': lambda: self.module.exit_json(changed=False, result="Datastore %s is already mounted." % self.datastore_name),
                'unmounted': self.mount_vmfs_datastore_on_host,
            }
        }
        try:
            ds_states[self.state][self.get_host_vmfs_datastore_mount_state()]()
        except (vmodl.RuntimeFault, vmodl.MethodFault) as vmodl_fault:
            self.module.fail_json(msg=to_native(vmodl_fault.msg))
        except Exception as e:
            self.module.fail_json(msg=to_native(e))

    def get_host_vmfs_datastore_mount_state(self):
        """Checks whether the datastore is mounted or not.
           warning: case of when the lun is not attached is not handled properly
          :return: Current mount state of the datastore : "mounted" or "unmounted"
          :rtype: string
        """
        storage_system = self.esxi.configManager.storageSystem   # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html
        host_file_sys_vol_mount_info = storage_system.fileSystemVolumeInfo.mountInfo   # Array of : https://vdc-download.vmware.com/vmwb-repository/dcr-public/b50dcbbf-051d-4204-a3e7-e1b618c1e384/538cf2ec-b34f-4bae-a332-3820ef9e7773/vim.host.FileSystemMountInfo.html
        for host_mount_info in host_file_sys_vol_mount_info:
            if host_mount_info.volume.name == self.datastore_name:
                if host_mount_info.mountInfo.mounted:
                    return "mounted"   # Detects if the datastore is mounted, works for both original and snapshot
                else:
                    return "unmounted"   # This seems to work only for orignal datastores

        # Unmounted snapshot datastores may not appear in the host_file_sys_vol_mount_info list from above
        # which is why we need to do the following
        if self.is_unmounted_snapshot_datastore():
            return "unmounted"
        self.module.fail_json(msg='Datastore %s was not found ! ' % self.datastore_name)

    def is_unmounted_snapshot_datastore(self):
        """If a datastore is unmounted, this returns whether the datastore is original or not
        to be able to use which method must be used for mounting.
        """
        storage_system = self.esxi.configManager.storageSystem  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html
        unresolved_vmfs_volumes = storage_system.QueryUnresolvedVmfsVolume()  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html#queryUnresolvedVmfsVolume
        # Snapshot datastores that are not mounted are considered as "unresolved" vmfs volumes unlike unmounted original datastores.
        for vol in unresolved_vmfs_volumes:
            if vol.vmfsLabel == self.datastore_name:
                return True
        return False

    def unmount_vmfs_datastore_from_host(self):
        if self.module.check_mode is False:
            storage_system = self.esxi.configManager.storageSystem  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html
            host_file_sys_vol_mount_info = storage_system.fileSystemVolumeInfo.mountInfo  # Array of : https://vdc-download.vmware.com/vmwb-repository/dcr-public/b50dcbbf-051d-4204-a3e7-e1b618c1e384/538cf2ec-b34f-4bae-a332-3820ef9e7773/vim.host.FileSystemMountInfo.html

            for host_mount_info in host_file_sys_vol_mount_info:
                if host_mount_info.volume.name == self.datastore_name:
                    error_message_umount = "Cannot umount datastore %s from host %s" % (self.datastore_name, self.esxi.name)
                    try:
                        storage_system.UnmountVmfsVolume(host_mount_info.volume.uuid)  # VMware docs : https://vdc-download.vmware.com/vmwb-repository/dcr-public/b50dcbbf-051d-4204-a3e7-e1b618c1e384/538cf2ec-b34f-4bae-a332-3820ef9e7773/vim.host.StorageSystem.html#unmountVmfsVolume
                        self.module.exit_json(changed=True, result="Datastore %s on host %s successfully unmounted." % (self.datastore_name, self.esxi.name))
                    except (vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse) as fault:
                        self.module.fail_json(msg="%s: %s" % (error_message_umount, to_native(fault.msg)))
                    except Exception as e:
                        self.module.fail_json(msg="%s: %s" % (error_message_umount, to_native(e)))

        self.module.exit_json(changed=True, result="CHECK MODE: Datastore %s on host %s would be successfully unmounted." % (self.datastore_name, self.esxi.name))

    def mount_vmfs_datastore_on_host(self):
        # API calls are different depending on if the datastore is original
        if self.is_unmounted_snapshot_datastore():
            self.mount_snapshot_vmfs_datastore_on_host()
        self.mount_original_vmfs_datastore_on_host()

    def mount_original_vmfs_datastore_on_host(self):
        if self.module.check_mode is False:
            storage_system = self.esxi.configManager.storageSystem  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html
            host_file_sys_vol_mount_info = storage_system.fileSystemVolumeInfo.mountInfo  # Array of : https://vdc-download.vmware.com/vmwb-repository/dcr-public/b50dcbbf-051d-4204-a3e7-e1b618c1e384/538cf2ec-b34f-4bae-a332-3820ef9e7773/vim.host.FileSystemMountInfo.html

            for host_mount_info in host_file_sys_vol_mount_info:
                if host_mount_info.volume.name == self.datastore_name:
                    error_message_umount = "Cannot mount datastore %s on host %s" % (self.datastore_name, self.esxi.name)
                    try:
                        storage_system.MountVmfsVolume(host_mount_info.volume.uuid)
                        self.module.exit_json(changed=True, result="Datastore %s on host %s successfully mounted." % (self.datastore_name, self.esxi.name))
                    except Exception as e:
                        self.module.fail_json(msg="%s: %s" % (error_message_umount, to_native(e)))

        self.module.exit_json(changed=True, result="CHECK MODE: Datastore %s on host %s would be successfully mounted." % (self.datastore_name, self.esxi.name))

    def mount_snapshot_vmfs_datastore_on_host(self):
        if self.module.check_mode is False:
            storage_system = self.esxi.configManager.storageSystem  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html
            unresolved_vmfs_volumes = storage_system.QueryUnresolvedVmfsVolume()  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html#queryUnresolvedVmfsVolume
            error_message_mount = "Cannot mount datastore %s on host %s" % (self.datastore_name, self.esxi.name)
            for vol in unresolved_vmfs_volumes:
                if vol.vmfsLabel == self.datastore_name:
                    try:
                        resolution_spec = vim.host.UnresolvedVmfsResolutionSpec()  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/fa5d1ee7-fad5-4ebf-b150-bdcef1d38d35/a5e46da1-9b96-4f0c-a1d0-7b8f3ebfd4f5/doc/vim.host.UnresolvedVmfsResolutionSpec.html
                        resolution_spec.uuidResolution = 'forceMount'  # This is to prevent resignature of the VMFS volume
                        resolution_spec.extentDevicePath = [vol.extent[0].devicePath]
                        storage_system.ResolveMultipleUnresolvedVmfsVolumes([resolution_spec])  # VMware docs : https://vdc-repo.vmware.com/vmwb-repository/dcr-public/1ef6c336-7bef-477d-b9bb-caa1767d7e30/82521f49-9d9a-42b7-b19b-9e6cd9b30db1/vim.host.StorageSystem.html#resolveMultipleUnresolvedVmfsVolumes
                        self.module.exit_json(changed=True, result="Datastore %s on host %s successfully mounted." % (self.datastore_name, self.esxi.name))
                    except Exception as e:
                        self.module.fail_json(msg="%s : %s" % (error_message_mount, to_native(e)))
        self.module.exit_json(changed=True, result="CHECK MODE: Datastore %s on host %s would be successfully mounted." % (self.datastore_name, self.esxi.name))


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        datastore_name=dict(type='str', required=True),
        esxi_hostname=dict(type='str', required=False),
        state=dict(type='str', default='mounted', choices=['unmounted', 'mounted'])
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    vmware_host_datastore = VMwareHostVmfsDatastore(module)
    vmware_host_datastore.process_state()


if __name__ == '__main__':
    main()
