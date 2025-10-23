#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: vmware_host_iscsi
short_description: Manage the iSCSI configuration of ESXi host
author:
  - sky-joker (@sky-joker)
description:
  - In this module, can manage the iSCSI configuration of ESXi host
options:
  esxi_hostname:
    description:
    - The ESXi hostname on which to change iSCSI settings.
    type: str
    required: true
  iscsi_config:
    description:
    - The iSCSI configs.
    - This parameter is required if O(state=present) or O(state=absent).
    type: dict
    suboptions:
      iscsi_name:
        description:
        - The name for the iSCSI HBA adapter.
        - This is iSCSI qualified name.
        type: str
        aliases:
        - initiator_iqn
      alias:
        description:
        - The new value for the alias of the adapter.
        type: str
        default: ''
      authentication:
        description:
        - CHAP authentication parent settings for iSCSI.
        type: dict
        suboptions:
          chap_auth_enabled:
            description:
            - Whether to enable CHAP authentication.
            type: bool
            default: false
          chap_authentication_type:
            description:
              - The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.
            type: str
            default: chapProhibited
            choices:
            - chapDiscouraged
            - chapPreferred
            - chapRequired
            - chapProhibited
          chap_name:
            description:
            - CHAP user name if CHAP is enabled.
            type: str
            default: ''
          chap_secret:
            description:
            - The secret password of CHAP if CHAP is enabled.
            type: str
          mutual_chap_authentication_type:
            description:
            - The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.
            type: str
            default: chapProhibited
            choices:
            - chapProhibited
            - chapRequired
          mutual_chap_name:
            description:
            - The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.
            type: str
            default: ''
          mutual_chap_secret:
            description:
            - The secret password of mutual CHAP if Mutual-CHAP is enabled.
            type: str
      port_bind:
        description:
        - The list of the VMkernels if use port bindings.
        type: list
        elements: str
        default: []
      force:
        description:
        - Force port bind VMkernels to be removed.
        type: bool
        default: false
      vmhba_name:
        description:
        - The iSCSI adapter name.
        type: str
        required: true
      send_target:
        description:
        - The iSCSI dynamic target settings.
        type: dict
        suboptions:
          address:
            description:
            - The IP address or hostname of the storage device.
            type: str
            required: true
          port:
            description:
            - The TCP port of the storage device.
            - If not specified, the standard default of 3260 is used.
            type: int
            default: 3260
          authentication:
            description:
            - CHAP authentication settings of a dynamic target for iSCSI.
            type: dict
            suboptions:
              chap_auth_enabled:
                description:
                - Whether to enable CHAP authentication.
                type: bool
                default: false
              chap_authentication_type:
                description:
                  - The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.
                type: str
                default: chapProhibited
                choices:
                - chapDiscouraged
                - chapPreferred
                - chapRequired
                - chapProhibited
              chap_inherited:
                description:
                - Whether or not to inherit CHAP settings from the parent settings.
                type: bool
                default: true
              chap_name:
                description:
                - CHAP user name if CHAP is enabled.
                type: str
                default: ''
              chap_secret:
                description:
                - The secret password of CHAP if CHAP is enabled.
                type: str
              mutual_chap_authentication_type:
                description:
                - The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.
                type: str
                default: chapProhibited
                choices:
                - chapProhibited
                - chapRequired
              mutual_chap_inherited:
                description:
                - Whether or not to inherit Mutual-CHAP settings from the parent settings.
                type: bool
                default: true
              mutual_chap_name:
                description:
                - The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.
                type: str
                default: ''
              mutual_chap_secret:
                description:
                - The secret password of mutual CHAP if Mutual-CHAP is enabled.
                type: str
      static_target:
        description:
        - The iSCSI static target settings.
        type: dict
        suboptions:
          iscsi_name:
            description:
            - The name of the iSCSI target to connect to.
            type: str
            required: true
          address:
            description:
            - The IP address or hostname of the storage device.
            type: str
            required: true
          port:
            description:
            - The TCP port of the storage device.
            - If not specified, the standard default of 3260 is used.
            type: int
            default: 3260
          authentication:
            description:
            - CHAP authentication settings of a static target for iSCSI.
            type: dict
            suboptions:
              chap_auth_enabled:
                description:
                - Whether to enable CHAP authentication.
                type: bool
                default: false
              chap_authentication_type:
                description:
                  - The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.
                type: str
                default: chapProhibited
                choices:
                - chapDiscouraged
                - chapPreferred
                - chapRequired
                - chapProhibited
              chap_inherited:
                description:
                - Whether or not to inherit CHAP settings from the parent settings.
                type: bool
                default: true
              chap_name:
                description:
                - CHAP user name if CHAP is enabled.
                type: str
                default: ''
              chap_secret:
                description:
                - The secret password of CHAP if CHAP is enabled.
                type: str
              mutual_chap_authentication_type:
                description:
                - The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.
                type: str
                default: chapProhibited
                choices:
                - chapProhibited
                - chapRequired
              mutual_chap_inherited:
                description:
                - Whether or not to inherit Mutual-CHAP settings from the parent settings.
                type: bool
                default: true
              mutual_chap_name:
                description:
                - The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.
                type: str
                default: ''
              mutual_chap_secret:
                description:
                - The secret password of mutual CHAP if Mutual-CHAP is enabled.
                type: str
  state:
    description:
    - If set to V(present), add the iSCSI target or the bind ports if they are not existing.
    - If set to V(present), update the iSCSI settings if they already exist and occur change.
    - If set to V(absent), remove the iSCSI target or the bind ports if they are existing.
    - If set to V(enabled), enable the iSCSI of ESXi if the iSCSI is disabled.
    - If set to V(disabled), disable the iSCSI of ESXi if the iSCSI is enabled.
    type: str
    default: present
    choices:
    - present
    - absent
    - enabled
    - disabled
extends_documentation_fragment:
- vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Enable iSCSI of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    state: enabled

- name: Add a dynamic target to iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      send_target:
        address: "{{ send_target_address }}"
    state: present

- name: Add a static target to iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      static_target:
        iscsi_name: iqn.2011-08.com.xxxxxxx:as6104t-8c3e9d.target001
        address: "{{ send_target_address }}"
    state: present

- name: Add VMKernels to iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      port_bind:
        - vmk0
        - vmk1
    state: present

- name: Use CHAP authentication
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      authentication:
        chap_auth_enabled: true
        chap_authentication_type: chapPreferred
        chap_name: chap_user_name
        chap_secret: secret
    state: present

- name: Remove a dynamic target from iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      send_target:
        address: "{{ send_target_address }}"
    state: absent
'''

RETURN = r'''
iscsi_properties:
  description: Parameter return when system defaults config is changed.
  returned: changed
  type: dict
  sample: >-
    {
        "iscsi_alias": "",
        "iscsi_authentication_properties": {
            "_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties",
            "chapAuthEnabled": false,
            "chapAuthenticationType": "chapProhibited",
            "chapInherited": null,
            "chapName": "",
            "chapSecret": "XXXXXXXXXXXXXXXXXXXXX",
            "mutualChapAuthenticationType": "chapProhibited",
            "mutualChapInherited": null,
            "mutualChapName": "XXXXXXXXXXXXXXXXXXXXX",
            "mutualChapSecret": ""
        },
        "iscsi_enabled": true,
        "iscsi_name": "",
        "iscsi_send_targets": [],
        "iscsi_static_targets": [],
        "port_bind": [],
        "vmhba_name": "vmhba65"
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.common.text.converters import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.basic import AnsibleModule
from copy import deepcopy


class VMwareHostiScsiManager(PyVmomi):
    def __init__(self, module):
        super(VMwareHostiScsiManager, self).__init__(module)
        self.esxi_hostname = self.params['esxi_hostname']
        self.iscsi_config = self.params['iscsi_config']
        self.state = self.params['state']

        if self.iscsi_config:
            self.iscsi_name = self.iscsi_config['iscsi_name']
            self.alias = self.iscsi_config['alias']
            self.authentication = self.iscsi_config['authentication']
            self.port_bind = self.iscsi_config['port_bind']
            self.force = self.iscsi_config['force']
            self.vmhba_name = self.iscsi_config['vmhba_name']
            self.send_target = self.iscsi_config['send_target']
            self.static_target = self.iscsi_config['static_target']

    def get_iscsi_config(self):
        self.existing_system_iscsi_config = {}
        for hba in self.host_obj.config.storageDevice.hostBusAdapter:
            if isinstance(hba, vim.host.InternetScsiHba):
                self.existing_system_iscsi_config.update(
                    {
                        'vmhba_name': hba.device,
                        'iscsi_name': hba.iScsiName,
                        'iscsi_alias': hba.iScsiAlias,
                        'iscsi_authentication_properties': self.to_json(hba.authenticationProperties)
                    }
                )

                iscsi_send_targets = []
                for iscsi_send_target in self.to_json(hba.configuredSendTarget):
                    iscsi_send_targets.append({
                        'address': iscsi_send_target['address'],
                        'authenticationProperties': iscsi_send_target['authenticationProperties'],
                        'port': iscsi_send_target['port']
                    })
                self.existing_system_iscsi_config['iscsi_send_targets'] = iscsi_send_targets

                iscsi_static_targets = []
                for iscsi_static_target in self.to_json(hba.configuredStaticTarget):
                    iscsi_static_targets.append({
                        'iscsi_name': iscsi_static_target['iScsiName'],
                        'address': iscsi_static_target['address'],
                        'authenticationProperties': iscsi_static_target['authenticationProperties'],
                        'port': iscsi_static_target['port']
                    })
                self.existing_system_iscsi_config['iscsi_static_targets'] = iscsi_static_targets

        self.existing_system_iscsi_config['iscsi_enabled'] = self.to_json(self.host_obj.config.storageDevice.softwareInternetScsiEnabled)

        vnic_devices = []
        if self.iscsi_config:
            for vnic in self.host_obj.configManager.iscsiManager.QueryBoundVnics(iScsiHbaName=self.vmhba_name):
                vnic_devices.append(vnic.vnicDevice)
        self.existing_system_iscsi_config['port_bind'] = vnic_devices

    def check_hba_name(self):
        if self.existing_system_iscsi_config['vmhba_name'] != self.vmhba_name:
            self.module.fail_json(msg="%s is not an iSCSI device." % self.vmhba_name)

    def diff_iscsi_config(self):
        if self.state == 'enabled':
            self.change_flag = True
            if self.existing_system_iscsi_config['iscsi_enabled'] == 'true':
                self.change_flag = False

        if self.state == 'disabled':
            self.change_flag = True
            if self.existing_system_iscsi_config['iscsi_enabled'] == 'false':
                self.change_flag = False

        if self.state == 'present':
            self.change_flag = True

            self.add_send_interface_flag = True
            if self.send_target:
                for config in self.existing_system_iscsi_config['iscsi_send_targets']:
                    if config['address'] == self.send_target['address'] and config['port'] == self.send_target['port']:
                        self.change_flag = False
                        self.add_send_interface_flag = False

            self.add_static_interface_flag = True
            if self.static_target:
                for config in self.existing_system_iscsi_config['iscsi_static_targets']:
                    if config['address'] == self.static_target['address'] and config['port'] == self.static_target['port'] \
                            and config['iscsi_name'] == self.static_target['iscsi_name']:
                        self.change_flag = False
                        self.add_static_interface_flag = False

            self.update_iscsi_name_flag = False
            if self.existing_system_iscsi_config['iscsi_name'] != self.iscsi_name and self.iscsi_name:
                self.change_flag = True
                self.update_iscsi_name_flag = True

            self.update_alias_flag = False
            if self.existing_system_iscsi_config['iscsi_alias'] != self.alias:
                self.change_flag = True
                self.update_alias_flag = True

            self.update_auth_flag = False
            if self.authentication:
                auth_properties = self.existing_system_iscsi_config['iscsi_authentication_properties']
                if auth_properties['chapAuthEnabled'] != self.authentication['chap_auth_enabled']:
                    self.change_flag = True
                    self.update_auth_flag = True
                if auth_properties['chapAuthenticationType'] != self.authentication['chap_authentication_type']:
                    self.change_flag = True
                    self.update_auth_flag = True
                if auth_properties['chapName'] != self.authentication['chap_name']:
                    self.change_flag = True
                    self.update_auth_flag = True
                if auth_properties['mutualChapAuthenticationType'] != self.authentication['mutual_chap_authentication_type']:
                    self.change_flag = True
                    self.update_auth_flag = True
                if auth_properties['mutualChapName'] != self.authentication['mutual_chap_name']:
                    self.change_flag = True
                    self.update_auth_flag = True

            self.update_port_bind_flag = False
            if sorted(self.existing_system_iscsi_config['port_bind']) != sorted(self.port_bind):
                self.change_flag = True
                self.update_port_bind_flag = True

            self.update_send_target_authentication = False
            if self.add_send_interface_flag is False:
                for config in self.existing_system_iscsi_config['iscsi_send_targets']:
                    if config['address'] == self.send_target['address'] and \
                            config['port'] == self.send_target['port']:
                        auth_properties = config['authenticationProperties']
                        if auth_properties['chapAuthEnabled'] != self.send_target['authentication']['chap_auth_enabled']:
                            self.change_flag = True
                            self.update_send_target_authentication = True
                        if auth_properties['chapAuthenticationType'] != self.send_target['authentication']['chap_authentication_type']:
                            self.change_flag = True
                            self.update_send_target_authentication = True
                        if auth_properties['chapInherited'] != self.send_target['authentication']['chap_inherited']:
                            self.change_flag = True
                            self.update_send_target_authentication = True
                        if auth_properties['chapName'] != self.send_target['authentication']['chap_name']:
                            self.change_flag = True
                            self.update_send_target_authentication = True
                        if auth_properties['mutualChapAuthenticationType'] != self.send_target['authentication']['mutual_chap_authentication_type']:
                            self.change_flag = True
                            self.update_send_target_authentication = True
                        if auth_properties['mutualChapInherited'] != self.send_target['authentication']['mutual_chap_inherited']:
                            self.change_flag = True
                            self.update_send_target_authentication = True
                        if auth_properties['mutualChapName'] != self.send_target['authentication']['mutual_chap_name']:
                            self.change_flag = True
                            self.update_send_target_authentication = True
                        break

            self.update_static_target_authentication = False
            if self.add_static_interface_flag is False:
                for config in self.existing_system_iscsi_config['iscsi_static_targets']:
                    if config['address'] == self.static_target['address'] and \
                            config['port'] == self.static_target['port']:
                        auth_properties = config['authenticationProperties']
                        if auth_properties['chapAuthEnabled'] != self.static_target['authentication']['chap_auth_enabled']:
                            self.change_flag = True
                            self.update_static_target_authentication = True
                        if auth_properties['chapAuthenticationType'] != self.static_target['authentication']['chap_authentication_type']:
                            self.change_flag = True
                            self.update_static_target_authentication = True
                        if auth_properties['chapInherited'] != self.static_target['authentication']['chap_inherited']:
                            self.change_flag = True
                            self.update_static_target_authentication = True
                        if auth_properties['chapName'] != self.static_target['authentication']['chap_name']:
                            self.change_flag = True
                            self.update_static_target_authentication = True
                        if auth_properties['mutualChapAuthenticationType'] != self.static_target['authentication']['mutual_chap_authentication_type']:
                            self.change_flag = True
                            self.update_static_target_authentication = True
                        if auth_properties['mutualChapInherited'] != self.static_target['authentication']['mutual_chap_inherited']:
                            self.change_flag = True
                            self.update_static_target_authentication = True
                        if auth_properties['mutualChapName'] != self.static_target['authentication']['mutual_chap_name']:
                            self.change_flag = True
                            self.update_static_target_authentication = True
                        break

        if self.state == 'absent':
            self.change_flag = False

            self.remove_send_interface_flag = False
            if self.existing_system_iscsi_config['iscsi_send_targets'] and self.send_target:
                for config in self.existing_system_iscsi_config['iscsi_send_targets']:
                    if config['address'] == self.send_target['address'] and \
                            config['port'] == self.send_target['port']:
                        self.change_flag = True
                        self.remove_send_interface_flag = True

            self.remove_static_interface_flag = False
            if self.existing_system_iscsi_config['iscsi_static_targets'] and self.static_target:
                for config in self.existing_system_iscsi_config['iscsi_static_targets']:
                    if config['address'] == self.static_target['address'] and \
                            config['port'] == self.static_target['port'] and \
                            config['iscsi_name'] == self.static_target['iscsi_name']:
                        self.change_flag = True
                        self.remove_static_interface_flag = True

            self.remove_port_bind_flag = False
            if self.iscsi_config:
                for vnic in self.port_bind:
                    for existing_vnic in self.existing_system_iscsi_config['port_bind']:
                        if vnic == existing_vnic:
                            self.change_flag = True
                            self.remove_port_bind_flag = True

    def generate_iscsi_config(self):
        self.authentication_config = ''
        self.authentication_send_target_config = ''
        self.send_target_configs = []
        self.static_target_configs = []

        if self.authentication:
            self.authentication_config = vim.host.InternetScsiHba.AuthenticationProperties()
            self.authentication_config.chapAuthEnabled = self.authentication['chap_auth_enabled']
            self.authentication_config.chapAuthenticationType = self.authentication['chap_authentication_type']
            self.authentication_config.chapName = self.authentication['chap_name']
            self.authentication_config.chapSecret = self.authentication['chap_secret']
            self.authentication_config.mutualChapAuthenticationType = self.authentication['mutual_chap_authentication_type']
            self.authentication_config.mutualChapName = self.authentication['mutual_chap_name']
            self.authentication_config.mutualChapSecret = self.authentication['mutual_chap_secret']

        if self.send_target:
            send_target_config = vim.host.InternetScsiHba.SendTarget()
            send_target_config.address = self.send_target['address']
            send_target_config.port = self.send_target['port']

            if self.send_target['authentication']:
                self.send_target_authentication_config = vim.host.InternetScsiHba.AuthenticationProperties()
                self.send_target_authentication_config.chapAuthEnabled = self.send_target['authentication']['chap_auth_enabled']
                self.send_target_authentication_config.chapAuthenticationType = self.send_target['authentication']['chap_authentication_type']
                self.send_target_authentication_config.chapInherited = self.send_target['authentication']['chap_inherited']
                self.send_target_authentication_config.chapName = self.send_target['authentication']['chap_name']
                self.send_target_authentication_config.chapSecret = self.send_target['authentication']['chap_secret']
                self.send_target_authentication_config.mutualChapAuthenticationType = self.send_target['authentication']['mutual_chap_authentication_type']
                self.send_target_authentication_config.mutualChapInherited = self.send_target['authentication']['mutual_chap_inherited']
                self.send_target_authentication_config.mutualChapName = self.send_target['authentication']['mutual_chap_name']
                self.send_target_authentication_config.mutualChapSecret = self.send_target['authentication']['mutual_chap_secret']

            self.send_target_configs.append(send_target_config)

        if self.static_target:
            static_target_config = vim.host.InternetScsiHba.StaticTarget()
            static_target_config.iScsiName = self.static_target['iscsi_name']
            static_target_config.address = self.static_target['address']
            static_target_config.port = self.static_target['port']

            if self.static_target['authentication']:
                self.static_target_authentication_config = vim.host.InternetScsiHba.AuthenticationProperties()
                self.static_target_authentication_config.chapAuthEnabled = self.static_target['authentication']['chap_auth_enabled']
                self.static_target_authentication_config.chapAuthenticationType = self.static_target['authentication']['chap_authentication_type']
                self.static_target_authentication_config.chapInherited = self.static_target['authentication']['chap_inherited']
                self.static_target_authentication_config.chapName = self.static_target['authentication']['chap_name']
                self.static_target_authentication_config.chapSecret = self.static_target['authentication']['chap_secret']
                self.static_target_authentication_config.mutualChapAuthenticationType = self.static_target['authentication']['mutual_chap_authentication_type']
                self.static_target_authentication_config.mutualChapInherited = self.static_target['authentication']['mutual_chap_inherited']
                self.static_target_authentication_config.mutualChapName = self.static_target['authentication']['mutual_chap_name']
                self.static_target_authentication_config.mutualChapSecret = self.static_target['authentication']['mutual_chap_secret']

            self.static_target_configs.append(static_target_config)

    def execute(self):
        self.host_obj = self.find_hostsystem_by_name(self.esxi_hostname)
        if not self.host_obj:
            self.module.fail_json(msg="Cannot find the specified ESXi host: %s" % self.esxi_hostname)

        if not self.iscsi_config and (self.state == 'present' or self.state == 'absent'):
            self.module.fail_json(msg="If state is present or absent must specify the iscsi_config parameter.")
        else:
            self.get_iscsi_config()

        result = dict(changed=False)

        if self.state == 'enabled':
            self.diff_iscsi_config()
            if self.module.check_mode:
                self.module.exit_json(changed=self.change_flag)

            if self.existing_system_iscsi_config['iscsi_enabled'] is False:
                try:
                    self.host_obj.configManager.storageSystem.UpdateSoftwareInternetScsiEnabled(enabled=True)
                    result['changed'] = True
                except Exception as e:
                    self.module.fail_json(msg="Failed to enable iSCSI: %s" % to_native(e))

        if self.state == 'disabled':
            self.diff_iscsi_config()
            if self.module.check_mode:
                self.module.exit_json(changed=self.change_flag)

            if self.existing_system_iscsi_config['iscsi_enabled']:
                try:
                    self.host_obj.configManager.storageSystem.UpdateSoftwareInternetScsiEnabled(enabled=False)
                    result['changed'] = True
                except Exception as e:
                    self.module.fail_json(msg="Failed to disable iSCSI: %s" % to_native(e))

        if self.state == 'present':
            self.check_hba_name()
            self.diff_iscsi_config()

            if self.module.check_mode:
                self.module.exit_json(changed=self.change_flag)

            if self.change_flag:
                self.generate_iscsi_config()

                # add a dynamic target to an iSCSI configuration
                if self.add_send_interface_flag:
                    if self.send_target_configs:
                        try:
                            self.host_obj.configManager.storageSystem.AddInternetScsiSendTargets(
                                iScsiHbaDevice=self.vmhba_name,
                                targets=self.send_target_configs)
                            result['changed'] = True
                        except Exception as e:
                            self.module.fail_json(msg="Failed to add a dynamic target: %s" % to_native(e))

                # add a static target to an iSCSI configuration
                if self.add_static_interface_flag:
                    if self.static_target_configs:
                        try:
                            self.host_obj.configManager.storageSystem.AddInternetScsiStaticTargets(
                                iScsiHbaDevice=self.vmhba_name,
                                targets=self.static_target_configs)
                            result['changed'] = True
                        except Exception as e:
                            self.module.fail_json(msg="Failed to add a static target: %s" % to_native(e))

                # update a CHAP authentication of a dynamic target in an iSCSI configuration
                if self.update_send_target_authentication:
                    target_set = vim.host.InternetScsiHba.TargetSet()
                    target_set.sendTargets = self.send_target_configs
                    try:
                        self.host_obj.configManager.storageSystem.UpdateInternetScsiAuthenticationProperties(
                            iScsiHbaDevice=self.vmhba_name,
                            authenticationProperties=self.send_target_authentication_config,
                            targetSet=target_set)
                        result['changed'] = True
                    except Exception as e:
                        self.module.fail_json(msg="Failed to update a CHAP authentication of a dynamic target: %s" % to_native(e))

                # update a CHAP authentication of a static target in an iSCSI configuration
                if self.update_static_target_authentication:
                    target_set = vim.host.InternetScsiHba.TargetSet()
                    target_set.staticTargets = self.static_target_configs
                    try:
                        self.host_obj.configManager.storageSystem.UpdateInternetScsiAuthenticationProperties(
                            iScsiHbaDevice=self.vmhba_name,
                            authenticationProperties=self.static_target_authentication_config,
                            targetSet=target_set)
                        result['changed'] = True
                    except Exception as e:
                        self.module.fail_json(msg="Failed to update a CHAP authentication of a static target: %s" % to_native(e))

                # update an iqn in an iSCSI configuration
                if self.update_iscsi_name_flag:
                    try:
                        self.host_obj.configManager.storageSystem.UpdateInternetScsiName(
                            iScsiHbaDevice=self.vmhba_name, iScsiName=self.iscsi_name)
                        result['changed'] = True
                    except Exception as e:
                        self.module.fail_json(msg="Failed to update an iqn: %s" % to_native(e))

                # update an alias in an iSCSI configuration
                if self.update_alias_flag:
                    try:
                        self.host_obj.configManager.storageSystem.UpdateInternetScsiAlias(
                            iScsiHbaDevice=self.vmhba_name, iScsiAlias=self.alias)
                        result['changed'] = True
                    except Exception as e:
                        self.module.fail_json(msg="Failed to update an alias: %s" % to_native(e))

                # update a CHAP authentication an iSCSI configuration
                if self.update_auth_flag:
                    try:
                        self.host_obj.configManager.storageSystem.UpdateInternetScsiAuthenticationProperties(
                            iScsiHbaDevice=self.vmhba_name,
                            authenticationProperties=self.authentication_config,
                            targetSet=None)
                        result['changed'] = True
                    except Exception as e:
                        self.module.fail_json(msg="Failed to update a CHAP authentication: %s" % to_native(e))

                # add port binds in an iSCSI configuration
                if self.update_port_bind_flag:
                    for vnic in list(filter(lambda x: x not in self.existing_system_iscsi_config['port_bind'],
                                            self.port_bind)):
                        try:
                            self.host_obj.configManager.iscsiManager.BindVnic(iScsiHbaName=self.vmhba_name,
                                                                              vnicDevice=vnic)
                            result['changed'] = True
                        except Exception as e:
                            self.module.fail_json(msg="Failed to add a port bind: %s" % to_native(e))

        if self.state == 'absent':
            self.check_hba_name()
            self.diff_iscsi_config()

            if self.module.check_mode:
                self.module.exit_json(changed=self.change_flag)

            if self.change_flag:
                self.generate_iscsi_config()

                # remove a dynamic target to an iSCSI configuration
                if self.remove_send_interface_flag:
                    try:
                        self.host_obj.configManager.storageSystem.RemoveInternetScsiSendTargets(
                            iScsiHbaDevice=self.vmhba_name,
                            targets=self.send_target_configs)
                        result['changed'] = True
                    except Exception as e:
                        self.module.fail_json(msg="Failed to remove a dynamic target: %s" % to_native(e))

                # remove a static target to an iSCSI configuration
                if self.remove_static_interface_flag:
                    try:
                        self.host_obj.configManager.storageSystem.RemoveInternetScsiStaticTargets(
                            iScsiHbaDevice=self.vmhba_name,
                            targets=self.static_target_configs)
                        result['changed'] = True
                    except Exception as e:
                        self.module.fail_json(msg="Failed to remove a static target: %s" % to_native(e))

                # remove port binds from an iSCSI configuration
                if self.remove_port_bind_flag:
                    for vnic in list(set(self.existing_system_iscsi_config['port_bind']) & set(self.port_bind)):
                        try:
                            self.host_obj.configManager.iscsiManager.UnbindVnic(iScsiHbaName=self.vmhba_name,
                                                                                vnicDevice=vnic,
                                                                                force=self.force)
                            result['changed'] = True
                        except Exception as e:
                            self.module.fail_json(msg="Failed to remove a port bind: %s" % to_native(e))

        if result['changed'] is True:
            self.get_iscsi_config()
            result['iscsi_properties'] = self.existing_system_iscsi_config

        self.module.exit_json(**result)


def main():
    # base authentication parameters.
    authentication = dict(type='dict', apply_defaults=True,
                          options=dict(
                              chap_auth_enabled=dict(type='bool', default=False),
                              chap_authentication_type=dict(type='str', default='chapProhibited',
                                                            choices=['chapDiscouraged', 'chapPreferred', 'chapRequired',
                                                                     'chapProhibited']),
                              chap_name=dict(type='str', default=''),
                              chap_secret=dict(type='str', no_log=True),
                              mutual_chap_authentication_type=dict(type='str', default='chapProhibited',
                                                                   choices=['chapProhibited', 'chapRequired']),
                              mutual_chap_name=dict(type='str', default=''),
                              mutual_chap_secret=dict(type='str', no_log=True)))

    authentication_target = deepcopy(authentication)
    authentication_target['options'].update(
        chap_inherited=dict(type='bool', default=True),
        mutual_chap_inherited=dict(type='bool', default=True)
    )

    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=True),
        iscsi_config=dict(type='dict',
                          options=dict(
                              iscsi_name=dict(type='str', default=None, aliases=['initiator_iqn']),
                              alias=dict(type='str', default=''),
                              authentication=authentication,
                              port_bind=dict(type='list', elements='str', default=[]),
                              force=dict(type='bool', default=False),
                              vmhba_name=dict(type='str', required=True),
                              send_target=dict(type='dict',
                                               options=dict(
                                                   address=dict(type='str', required=True),
                                                   port=dict(type='int', default=3260),
                                                   authentication=authentication_target
                                               )),
                              static_target=dict(type='dict',
                                                 options=dict(
                                                     iscsi_name=dict(type='str', required=True),
                                                     address=dict(type='str', required=True),
                                                     port=dict(type='int', default=3260),
                                                     authentication=authentication_target
                                                 ))
                          )),
        state=dict(type='str', choices=['present', 'absent', 'enabled', 'disabled'], default='present')
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_host_iscsi_manager = VMwareHostiScsiManager(module)
    vmware_host_iscsi_manager.execute()


if __name__ == "__main__":
    main()
