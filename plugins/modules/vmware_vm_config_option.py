#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ansible Project
# Copyright: (c) 2021, VMware, Inc. All Rights Reserved.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vm_config_option
short_description: Return supported guest ID list and VM recommended config option for specific guest OS
description: >
   This module is used for getting the hardware versions supported for creation, the guest ID list supported by ESXi
   host for the most recent virtual hardware supported or specified hardware version, the VM recommended config options
   for specified guest OS ID.
author:
- Diane Wang (@Tomorrow9) <dianew@vmware.com>
notes:
- Known issue on vSphere 7.0 (https://github.com/vmware/pyvmomi/issues/915)
options:
  datacenter:
    description:
    - The datacenter name used to get specified cluster or host.
    default: ha-datacenter
    type: str
  cluster_name:
    description:
    - Name of the cluster.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname.
    - Obtain VM configure options on this ESXi host.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
  get_hardware_versions:
    description:
    - Return the list of VM hardware versions supported for creation and the default hardware version on the
      specified entity.
    type: bool
    default: false
  get_guest_os_ids:
    description:
    - Return the list of guest OS IDs supported on the specified entity.
    - If O(hardware_version) is set, will return the corresponding guest OS ID list supported, or will return the
      guest OS ID list for the default hardware version.
    type: bool
    default: false
  get_config_options:
    description:
    - Return the dict of VM recommended config options for guest ID specified by O(guest_id) with hardware version
      specified by O(hardware_version) or the default hardware version.
    - When set to V(true), O(guest_id) must be set.
    type: bool
    default: false
  guest_id:
    description:
    - The guest OS ID from the returned list when O(get_guest_os_ids=true), e.g., 'rhel8_64Guest'.
    - This parameter must be set when O(get_config_options=true).
    type: str
  hardware_version:
    description:
    - The hardware version from the returned list when O(get_hardware_versions=true), e.g., 'vmx-19'.
    type: str
extends_documentation_fragment:
- vmware.vmware.base_options

'''

EXAMPLES = r'''
- name: Get supported guest ID list on given ESXi host for with default hardware version
  community.vmware.vmware_vm_config_option:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    get_guest_os_ids: true
  delegate_to: localhost

- name: Get VM recommended config option for Windows 10 guest OS on given ESXi host
  community.vmware.vmware_vm_config_option:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    get_config_options: true
    guest_id: "windows9_64Guest"
  delegate_to: localhost
'''

RETURN = r'''
instance:
    description: metadata about the VM recommended configuration
    returned: always
    type: dict
    sample: None
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import find_obj, PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vm_device_helper import PyVmomiDeviceHelper


class VmConfigOption(PyVmomi):
    def __init__(self, module):
        super(VmConfigOption, self).__init__(module)
        self.device_helper = PyVmomiDeviceHelper(self.module)
        self.ctl_device_type = self.device_helper.disk_ctl_device_type.copy()
        self.ctl_device_type.update(self.device_helper.usb_device_type)
        self.ctl_device_type.update(self.device_helper.nic_device_type)
        self.target_host = None

    def get_hardware_versions(self, env_browser):
        support_create = []
        default_config = ''
        try:
            desc = env_browser.QueryConfigOptionDescriptor()
        except Exception as e:
            self.module.fail_json(msg="Failed to obtain VM config option descriptor due to fault: %s" % to_native(e))
        if desc:
            for option_desc in desc:
                if option_desc.createSupported:
                    support_create = support_create + [option_desc.key]
                if option_desc.defaultConfigOption:
                    default_config = option_desc.key

        return support_create, default_config

    def get_config_option_by_spec(self, env_browser, guest_id=None, key=''):
        vm_config_option = None
        if guest_id is None:
            guest_id = []
        if self.is_vcenter():
            host = self.target_host
        else:
            host = None
        config_query_spec = vim.EnvironmentBrowser.ConfigOptionQuerySpec(guestId=guest_id, host=host, key=key)
        try:
            vm_config_option = env_browser.QueryConfigOptionEx(spec=config_query_spec)
        except Exception as e:
            self.module.fail_json(msg="Failed to obtain VM config options due to fault: %s" % to_native(e))

        return vm_config_option

    def get_config_option_recommended(self, guest_os_desc, hwv_version=''):
        guest_os_option_dict = {}
        support_usb_controller = []
        support_disk_controller = []
        support_ethernet_card = []
        if guest_os_desc and len(guest_os_desc) != 0:
            default_disk_ctl = default_ethernet = default_cdrom_ctl = default_usb_ctl = ''
            for name, dev_type in self.ctl_device_type.items():
                for supported_type in guest_os_desc[0].supportedUSBControllerList:
                    if supported_type == dev_type:
                        support_usb_controller = support_usb_controller + [name]
                    if dev_type == guest_os_desc[0].recommendedUSBController:
                        default_usb_ctl = name
                for supported_type in guest_os_desc[0].supportedEthernetCard:
                    if supported_type == dev_type:
                        support_ethernet_card = support_ethernet_card + [name]
                    if dev_type == guest_os_desc[0].recommendedEthernetCard:
                        default_ethernet = name
                for supported_type in guest_os_desc[0].supportedDiskControllerList:
                    if supported_type == dev_type:
                        support_disk_controller = support_disk_controller + [name]
                    if dev_type == guest_os_desc[0].recommendedDiskController:
                        default_disk_ctl = name
                    if dev_type == guest_os_desc[0].recommendedCdromController:
                        default_cdrom_ctl = name
            guest_os_option_dict = {
                'hardware_version': hwv_version,
                'guest_id': guest_os_desc[0].id,
                'guest_fullname': guest_os_desc[0].fullName,
                'rec_cpu_cores_per_socket': guest_os_desc[0].numRecommendedCoresPerSocket,
                'rec_cpu_socket': guest_os_desc[0].numRecommendedPhysicalSockets,
                'rec_memory_mb': guest_os_desc[0].recommendedMemMB,
                'rec_firmware': guest_os_desc[0].recommendedFirmware,
                'default_secure_boot': guest_os_desc[0].defaultSecureBoot,
                'support_secure_boot': guest_os_desc[0].supportsSecureBoot,
                'default_disk_controller': default_disk_ctl,
                'rec_disk_mb': guest_os_desc[0].recommendedDiskSizeMB,
                'default_ethernet': default_ethernet,
                'default_cdrom_controller': default_cdrom_ctl,
                'default_usb_controller': default_usb_ctl,
                'support_tpm_20': guest_os_desc[0].supportsTPM20,
                'support_persistent_memory': guest_os_desc[0].persistentMemorySupported,
                'rec_persistent_memory': guest_os_desc[0].recommendedPersistentMemoryMB,
                'support_min_persistent_mem_mb': guest_os_desc[0].supportedMinPersistentMemoryMB,
                'rec_vram_kb': guest_os_desc[0].vRAMSizeInKB.defaultValue,
                'support_usb_controller': support_usb_controller,
                'support_disk_controller': support_disk_controller,
                'support_ethernet_card': support_ethernet_card,
                'support_cpu_hotadd': guest_os_desc[0].supportsCpuHotAdd,
                'support_memory_hotadd': guest_os_desc[0].supportsMemoryHotAdd,
                'support_for_create': guest_os_desc[0].supportedForCreate
            }

        return guest_os_option_dict

    def get_guest_id_list(self, guest_os_desc):
        gos_id_list = []
        if guest_os_desc:
            for gos_desc in guest_os_desc.guestOSDescriptor:
                gos_id_list = gos_id_list + [gos_desc.id]

        return gos_id_list

    def get_config_option_for_guest(self):
        results = {}
        guest_id = []
        datacenter_name = self.params.get('datacenter')
        cluster_name = self.params.get('cluster_name')
        esxi_host_name = self.params.get('esxi_hostname')
        if self.params.get('guest_id'):
            guest_id = [self.params.get('guest_id')]

        if not self.params.get('get_hardware_versions') and not self.params.get('get_guest_os_ids') \
                and not self.params.get('get_config_options'):
            self.module.exit_json(msg="Please set at least one of these parameters 'get_hardware_versions',"
                                      " 'get_guest_os_ids', 'get_config_options' to True to get the desired info.")
        if self.params.get('get_config_options') and len(guest_id) == 0:
            self.module.fail_json(msg="Please set 'guest_id' when 'get_config_options' is set to True,"
                                      " to get the VM recommended config option for specific guest OS.")

        # Get the datacenter object
        datacenter = find_obj(self.content, [vim.Datacenter], datacenter_name)
        if not datacenter:
            self.module.fail_json(msg='Unable to find datacenter "%s"' % datacenter_name)
        # Get the cluster object
        if cluster_name:
            cluster = find_obj(self.content, [vim.ComputeResource], cluster_name, folder=datacenter)
            if not cluster:
                self.module.fail_json(msg='Unable to find cluster "%s"' % cluster_name)
        # If host is given, get the cluster object using the host
        elif esxi_host_name:
            host = find_obj(self.content, [vim.HostSystem], esxi_host_name, folder=datacenter)
            if not host:
                self.module.fail_json(msg='Unable to find host "%s"' % esxi_host_name)
            self.target_host = host
            cluster = host.parent
        # Define the environment browser object the ComputeResource presents
        env_browser = cluster.environmentBrowser
        if env_browser is None:
            self.module.fail_json(msg="The environmentBrowser of the ComputeResource is None, so can not get the"
                                      " desired config option info, please check your vSphere environment.")
        # Get supported hardware versions list
        support_create_list, default_config = self.get_hardware_versions(env_browser=env_browser)
        if self.params.get('get_hardware_versions'):
            results.update({'supported_hardware_versions': support_create_list,
                            'default_hardware_version': default_config})

        if self.params.get('get_guest_os_ids') or self.params.get('get_config_options'):
            # Get supported guest ID list
            hardware_version = self.params.get('hardware_version', '')
            if hardware_version and len(support_create_list) != 0 and hardware_version not in support_create_list:
                self.module.fail_json(msg="Specified hardware version '%s' is not in the supported create list: %s"
                                          % (hardware_version, support_create_list))
            vm_config_option_all = self.get_config_option_by_spec(env_browser=env_browser, key=hardware_version)
            supported_gos_list = self.get_guest_id_list(guest_os_desc=vm_config_option_all)
            if self.params.get('get_guest_os_ids'):
                results.update({vm_config_option_all.version: supported_gos_list})

            if self.params.get('get_config_options') and len(guest_id) != 0:
                if supported_gos_list and guest_id[0] not in supported_gos_list:
                    self.module.fail_json(msg="Specified guest ID '%s' is not in the supported guest ID list: '%s'"
                                              % (guest_id[0], supported_gos_list))
                vm_config_option_guest = self.get_config_option_by_spec(env_browser=env_browser, guest_id=guest_id,
                                                                        key=hardware_version)
                guest_os_options = vm_config_option_guest.guestOSDescriptor
                guest_os_option_dict = self.get_config_option_recommended(guest_os_desc=guest_os_options,
                                                                          hwv_version=vm_config_option_guest.version)
                results.update({'recommended_config_options': guest_os_option_dict})

        self.module.exit_json(changed=False, failed=False, instance=results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str', default='ha-datacenter'),
        cluster_name=dict(type='str'),
        esxi_hostname=dict(type='str'),
        get_hardware_versions=dict(type='bool', default=False),
        get_guest_os_ids=dict(type='bool', default=False),
        get_config_options=dict(type='bool', default=False),
        guest_id=dict(type='str'),
        hardware_version=dict(type='str'),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ]
    )
    vm_config_option_guest = VmConfigOption(module)
    vm_config_option_guest.get_config_option_for_guest()


if __name__ == "__main__":
    main()
