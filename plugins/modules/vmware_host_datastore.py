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
module: vmware_host_datastore
short_description: Manage a datastore on ESXi host
description:
- This module can be used to mount/umount datastore on ESXi host.
- This module only supports NFS (NFS v3 or NFS v4.1) and VMFS datastores.
- For VMFS datastore, available device must already be connected on ESXi host.
author:
- Ludovic Rivallain (@lrivallain) <ludovic.rivallain@gmail.com>
- Christian Kotte (@ckotte) <christian.kotte@gmx.de>
- Eugenio Grosso (@genegr) <eugenio.grosso@purestorage.com>
notes:
- Kerberos authentication with NFS v4.1 isn't implemented
options:
  datastore_name:
    description:
    - Name of the datastore to add/remove.
    required: true
    type: str
  datastore_type:
    description:
    - Type of the datastore to configure (nfs/nfs41/vmfs/vvol).
    choices: [ 'nfs', 'nfs41', 'vmfs', 'vvol' ]
    type: str
  nfs_server:
    description:
    - NFS host serving nfs datastore.
    - Required if O(datastore_type=nfs) / O(datastore_type=nfs41) and O(state=present), else unused.
    - Two or more servers can be defined if O(datastore_type=nfs41)
    type: str
  nfs_path:
    description:
    - Resource path on NFS host.
    - Required if O(datastore_type=nfs) / O(datastore_type=nfs41) and O(state=present), else unused.
    type: str
  nfs_ro:
    description:
    - ReadOnly or ReadWrite mount.
    - Unused if datastore type is not set to O(datastore_type=nfs) / O(datastore_type=nfs41) and not O(state=present).
    default: false
    type: bool
  resignature:
    description:
    - Allows forcing resignature of unresolved VMFS datastore that already exists on the specified disk device.
    - Unused if not O(datastore_type=vmfs) and not O(state=present).
    default: false
    type: bool
    version_added: '3.9.0'
  vmfs_device_name:
    description:
    - Name of the device to be used as VMFS datastore.
    - Required for VMFS datastore type and O(state=present), else unused.
    type: str
  vmfs_version:
    description:
    - VMFS version to use for datastore creation.
    - Unused if not O(datastore_type=vmfs) and not O(state=present).
    type: int
  vasa_provider:
    description:
    - hostname or ipaddress of the VASA provider to use for vVols provisioning
    type: str
    required: false
    version_added: '3.9.0'
  esxi_hostname:
    description:
    - ESXi hostname to manage the datastore.
    - Required when used with a vcenter
    type: str
    required: false
  auto_expand:
    description:
    - Expand a datastore capacity to full if it has free capacity.
    - This parameter can't be extend using another datastore.
    - Can be used to expand a datastore capacity after increasing LUN volume.
    type: bool
    default: true
  state:
    description:
    - "present: Mount datastore on host if datastore is absent else do nothing."
    - "absent: Umount datastore if datastore is present else do nothing."
    default: present
    choices: [ present, absent ]
    type: str
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
      datastore_type: '{{ item.type }}'
      vmfs_device_name: 'naa.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
      vmfs_version: 6
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost

- name: Mount NFS datastores to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: '{{ item.name }}'
      datastore_type: '{{ item.type }}'
      nfs_server: '{{ item.server }}'
      nfs_path: '{{ item.path }}'
      nfs_ro: false
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost
  loop:
      - { 'name': 'NasDS_vol01', 'server': 'nas01', 'path': '/mnt/vol01', 'type': 'nfs'}
      - { 'name': 'NasDS_vol02', 'server': 'nas01', 'path': '/mnt/vol02', 'type': 'nfs'}

- name: Mount NFS v4.1 datastores to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: '{{ item.name }}'
      datastore_type: '{{ item.type }}'
      nfs_server: '{{ item.server }}'
      nfs_path: '{{ item.path }}'
      nfs_ro: false
      esxi_hostname: '{{ inventory_hostname }}'
      state: present
  delegate_to: localhost
  loop:
      - { 'name': 'NasDS_vol03', 'server': 'nas01,nas02', 'path': '/mnt/vol01', 'type': 'nfs41'}
      - { 'name': 'NasDS_vol04', 'server': 'nas01,nas02', 'path': '/mnt/vol02', 'type': 'nfs41'}

- name: Mount vVols datastore to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: myvvolds
      datastore_type: vvol
      vasa_provider: pure-X90a
      esxi_hostname: esxi-1
      state: absent
  delegate_to: localhost

- name: Mount unresolved VMFS datastores to ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ vcenter_hostname }}'
      username: '{{ vcenter_username }}'
      password: '{{ vcenter_password }}'
      datastore_name: mydatastore01
      vmfs_device_name: 'naa.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
      vmfs_version: 6
      esxi_hostname:  esxi01
      resignature: true
      state: present
  delegate_to: localhost

- name: Remove/Umount Datastores from a ESXi
  community.vmware.vmware_host_datastore:
      hostname: '{{ esxi_hostname }}'
      username: '{{ esxi_username }}'
      password: '{{ esxi_password }}'
      datastore_name: NasDS_vol01
      state: absent
  delegate_to: localhost
'''

RETURN = r'''
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import vmware_argument_spec, find_datastore_by_name, wait_for_task
from ansible_collections.community.vmware.plugins.module_utils.vmware_sms import SMS
from ansible.module_utils._text import to_native


class VMwareHostDatastore(SMS):
    def __init__(self, module):
        super(VMwareHostDatastore, self).__init__(module)

        self.datastore_name = module.params['datastore_name']
        self.datastore_type = module.params['datastore_type']
        self.nfs_server = module.params['nfs_server']
        self.nfs_path = module.params['nfs_path']
        self.nfs_ro = module.params['nfs_ro']
        self.vmfs_device_name = module.params['vmfs_device_name']
        self.vasa_provider_name = module.params['vasa_provider']
        self.vmfs_version = module.params['vmfs_version']
        self.resignature = module.params['resignature']
        self.esxi_hostname = module.params['esxi_hostname']
        self.auto_expand = module.params['auto_expand']
        self.state = module.params['state']

        if self.is_vcenter():
            if not self.esxi_hostname:
                self.module.fail_json(msg="esxi_hostname is mandatory with a vcenter")
            self.esxi = self.find_hostsystem_by_name(self.esxi_hostname)
            if self.esxi is None:
                self.module.fail_json(msg="Failed to find ESXi hostname %s" % self.esxi_hostname)
        else:
            self.esxi = self.find_obj([vim.HostSystem], None)

    def process_state(self):
        ds_states = {
            'absent': {
                'present': self.umount_datastore_host,
                'absent': self.state_exit_unchanged,
            },
            'present': {
                'present': self.state_exit_unchanged,
                'absent': self.mount_datastore_host,
            }
        }
        try:
            ds_states[self.state][self.check_datastore_host_state()]()
        except (vmodl.RuntimeFault, vmodl.MethodFault) as vmodl_fault:
            self.module.fail_json(msg=to_native(vmodl_fault.msg))
        except Exception as e:
            self.module.fail_json(msg=to_native(e))

    def expand_datastore_up_to_full(self):
        """
        Expand a datastore capacity up to full if there is free capacity.
        """
        cnf_mng = self.esxi.configManager

        # Find attached datastore at host.
        for datastore_obj in self.esxi.datastore:
            if datastore_obj.name == self.datastore_name:
                expand_datastore_obj = datastore_obj
                break

        # Check that whether the datastore has free capacity to expand.
        vmfs_ds_options = cnf_mng.datastoreSystem.QueryVmfsDatastoreExpandOptions(expand_datastore_obj)
        if vmfs_ds_options:
            if self.module.check_mode is False:
                try:
                    cnf_mng.datastoreSystem.ExpandVmfsDatastore(datastore=expand_datastore_obj,
                                                                spec=vmfs_ds_options[0].spec)
                except Exception as e:
                    self.module.fail_json(msg="%s can not expand the datastore: %s" % (to_native(e.msg), self.datastore_name))

            self.module.exit_json(changed=True)

    def state_exit_unchanged(self):
        self.module.exit_json(changed=False)

    def check_datastore_host_state(self):
        storage_system = self.esxi.configManager.storageSystem
        host_file_sys_vol_mount_info = storage_system.fileSystemVolumeInfo.mountInfo
        for host_mount_info in host_file_sys_vol_mount_info:
            if host_mount_info.volume.name == self.datastore_name:
                if self.auto_expand and host_mount_info.volume.type == "VMFS":
                    self.expand_datastore_up_to_full()
                return 'present'
        return 'absent'

    def get_used_disks_names(self):
        used_disks = []
        storage_system = self.esxi.configManager.storageSystem
        for each_vol_mount_info in storage_system.fileSystemVolumeInfo.mountInfo:
            if hasattr(each_vol_mount_info.volume, 'extent'):
                for each_partition in each_vol_mount_info.volume.extent:
                    used_disks.append(each_partition.diskName)
        return used_disks

    def umount_datastore_host(self):
        ds = find_datastore_by_name(self.content, self.datastore_name)
        if not ds:
            self.module.fail_json(msg="No datastore found with name %s" % self.datastore_name)
        if self.module.check_mode is False:
            error_message_umount = "Cannot umount datastore %s from host %s" % (self.datastore_name, self.esxi.name)
            try:
                self.esxi.configManager.datastoreSystem.RemoveDatastore(ds)
            except (vim.fault.NotFound, vim.fault.HostConfigFault, vim.fault.ResourceInUse) as fault:
                self.module.fail_json(msg="%s: %s" % (error_message_umount, to_native(fault.msg)))
            except Exception as e:
                self.module.fail_json(msg="%s: %s" % (error_message_umount, to_native(e)))
        self.module.exit_json(changed=True, result="Datastore %s on host %s" % (self.datastore_name, self.esxi.name))

    def mount_datastore_host(self):
        if self.datastore_type == 'nfs' or self.datastore_type == 'nfs41':
            self.mount_nfs_datastore_host()
        if self.datastore_type == 'vmfs':
            self.mount_vmfs_datastore_host()
        if self.datastore_type == 'vvol':
            self.mount_vvol_datastore_host()

    def mount_nfs_datastore_host(self):
        if self.module.check_mode is False:
            mnt_specs = vim.host.NasVolume.Specification()
            # NFS v3
            if self.datastore_type == 'nfs':
                mnt_specs.type = "NFS"
                mnt_specs.remoteHost = self.nfs_server
            # NFS v4.1
            if self.datastore_type == 'nfs41':
                mnt_specs.type = "NFS41"
                # remoteHost needs to be set to a non-empty string, but the value is not used
                mnt_specs.remoteHost = "something"
                mnt_specs.remoteHostNames = [self.nfs_server]
            mnt_specs.remotePath = self.nfs_path
            mnt_specs.localPath = self.datastore_name
            if self.nfs_ro:
                mnt_specs.accessMode = "readOnly"
            else:
                mnt_specs.accessMode = "readWrite"
            error_message_mount = "Cannot mount datastore %s on host %s" % (self.datastore_name, self.esxi.name)
            try:
                ds = self.esxi.configManager.datastoreSystem.CreateNasDatastore(mnt_specs)
                if not ds:
                    self.module.fail_json(msg=error_message_mount)
            except (vim.fault.NotFound, vim.fault.DuplicateName,
                    vim.fault.AlreadyExists, vim.fault.HostConfigFault,
                    vmodl.fault.InvalidArgument, vim.fault.NoVirtualNic,
                    vim.fault.NoGateway) as fault:
                self.module.fail_json(msg="%s: %s" % (error_message_mount, to_native(fault.msg)))
            except Exception as e:
                self.module.fail_json(msg="%s : %s" % (error_message_mount, to_native(e)))
        self.module.exit_json(changed=True, result="Datastore %s on host %s" % (self.datastore_name, self.esxi.name))

    def mount_vmfs_datastore_host(self):
        if self.module.check_mode is False:
            ds_path = "/vmfs/devices/disks/" + str(self.vmfs_device_name)
            host_ds_system = self.esxi.configManager.datastoreSystem
            ds_system = vim.host.DatastoreSystem
            if self.vmfs_device_name in self.get_used_disks_names():
                error_message_used_disk = "VMFS disk %s already in use" % self.vmfs_device_name
                self.module.fail_json(msg="%s" % error_message_used_disk)
            error_message_mount = "Cannot mount datastore %s on host %s" % (self.datastore_name, self.esxi.name)
            try:
                if self.resignature:
                    storage_system = self.esxi.configManager.storageSystem
                    host_unres_volumes = storage_system.QueryUnresolvedVmfsVolume()
                    unres_vol_extents = {}
                    for unres_vol in host_unres_volumes:
                        for ext in unres_vol.extent:
                            unres_vol_extents[ext.device.diskName] = ext
                    if self.vmfs_device_name in unres_vol_extents:
                        spec = vim.host.UnresolvedVmfsResignatureSpec()
                        spec.extentDevicePath = unres_vol_extents[self.vmfs_device_name].devicePath
                        task = host_ds_system.ResignatureUnresolvedVmfsVolume_Task(spec)
                        wait_for_task(task=task)
                        task.info.result.result.RenameDatastore(self.datastore_name)
                else:
                    vmfs_ds_options = ds_system.QueryVmfsDatastoreCreateOptions(host_ds_system,
                                                                                ds_path,
                                                                                self.vmfs_version)
                    vmfs_ds_options[0].spec.vmfs.volumeName = self.datastore_name
                    ds_system.CreateVmfsDatastore(
                        host_ds_system,
                        vmfs_ds_options[0].spec)
            except (vim.fault.NotFound, vim.fault.DuplicateName,
                    vim.fault.HostConfigFault, vmodl.fault.InvalidArgument) as fault:
                self.module.fail_json(msg="%s : %s" % (error_message_mount, to_native(fault.msg)))
            except Exception as e:
                self.module.fail_json(msg="%s : %s" % (error_message_mount, to_native(e)))
        self.module.exit_json(changed=True, result="Datastore %s on host %s" % (self.datastore_name, self.esxi.name))

    def mount_vvol_datastore_host(self):
        if self.module.check_mode is False:
            self.get_sms_connection()
            storage_manager = self.sms_si.QueryStorageManager()
            container_result = storage_manager.QueryStorageContainer()
            provider = None
            for p in container_result.providerInfo:
                if p.name == self.vasa_provider_name:
                    provider = p
                    break
            if provider is None:
                error_message_provider = "VASA provider %s not found" % self.vasa_provider_name
                self.module.fail_json(msg="%s" % error_message_provider)

            container = None
            for sc in container_result.storageContainer:
                if sc.providerId[0] == provider.uid:
                    container = sc
                    break
            if container is None:
                error_message_container = "vVol container for provider %s not found" % provider.uid
                self.module.fail_json(msg="%s" % error_message_container)

            vvol_spec = vim.HostDatastoreSystem.VvolDatastoreSpec(name=self.datastore_name, scId=container.uuid)
            host_ds_system = self.esxi.configManager.datastoreSystem
            error_message_mount = "Cannot mount datastore %s on host %s" % (self.datastore_name, self.esxi.name)
            try:
                host_ds_system.CreateVvolDatastore(vvol_spec)
            except Exception as e:
                self.module.fail_json(msg="%s : %s" % (error_message_mount, to_native(e)))
        self.module.exit_json(changed=True, result="Datastore %s on host %s" % (self.datastore_name, self.esxi.name))


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        datastore_name=dict(type='str', required=True),
        datastore_type=dict(type='str', choices=['nfs', 'nfs41', 'vmfs', 'vvol']),
        nfs_server=dict(type='str'),
        nfs_path=dict(type='str'),
        nfs_ro=dict(type='bool', default=False),
        vmfs_device_name=dict(type='str'),
        vmfs_version=dict(type='int'),
        resignature=dict(type='bool', default=False),
        esxi_hostname=dict(type='str', required=False),
        auto_expand=dict(type='bool', default=True),
        vasa_provider=dict(type='str'),
        state=dict(type='str', default='present', choices=['absent', 'present'])
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ['state', 'present', ['datastore_type']],
            ['datastore_type', 'vmfs', ['vmfs_device_name']],
            ['datastore_type', 'nfs', ['nfs_server', 'nfs_path']],
            ['datastore_type', 'nfs41', ['nfs_server', 'nfs_path']],
            ['datastore_type', 'vvol', ['vasa_provider']],
        ]
    )

    vmware_host_datastore = VMwareHostDatastore(module)
    vmware_host_datastore.process_state()


if __name__ == '__main__':
    main()
