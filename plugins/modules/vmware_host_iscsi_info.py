#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: vmware_host_iscsi_info
short_description: Gather iSCSI configuration information of ESXi host
author:
  - sky-joker (@sky-joker)
description:
  - This module can be used to gather information about the iSCSI configuration of the ESXi host.
options:
  esxi_hostname:
    description:
    - The ESXi hostname on which to gather iSCSI settings.
    type: str
    required: true
extends_documentation_fragment:
  - community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Gather iSCSI configuration information of ESXi host
  community.vmware.vmware_host_iscsi_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
  register: iscsi_info
'''

RETURN = r'''
iscsi_properties:
  description: dictionary of current iSCSI information
  returned: always
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
        "chapSecret": "XXXXXXXXX",
        "mutualChapAuthenticationType": "chapProhibited",
        "mutualChapInherited": null,
        "mutualChapName": "",
        "mutualChapSecret": "XXXXXXXXX"
      },
      "iscsi_enabled": true,
      "iscsi_name": "iqn.1998-01.com.vmware:esxi-033f58ee",
      "iscsi_send_targets": [
        {
          "address": "192.168.0.1",
          "authenticationProperties": {
            "_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties",
            "chapAuthEnabled": false,
            "chapAuthenticationType": "chapProhibited",
            "chapInherited": true,
            "chapName": "",
            "chapSecret": "XXXXXXXXX",
            "mutualChapAuthenticationType": "chapProhibited",
            "mutualChapInherited": true,
            "mutualChapName": "",
            "mutualChapSecret": "XXXXXXXXX"
          },
          "port": 3260
        }
      ],
      "iscsi_static_targets": [
        {
          "address": "192.168.0.1",
          "authenticationProperties": {
            "_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties",
            "chapAuthEnabled": false,
            "chapAuthenticationType": "chapProhibited",
            "chapInherited": true,
            "chapName": "",
            "chapSecret": "XXXXXXXXX",
            "mutualChapAuthenticationType": "chapProhibited",
            "mutualChapInherited": true,
            "mutualChapName": "",
            "mutualChapSecret": "XXXXXXXXX"
          },
          "iscsi_name": "iqn.2004-04.com.qnap:tvs-673:iscsi.vm3.2c580e",
          "port": 3260
        }
      ],
      "port_bind": [],
      "vmhba_name": "vmhba65"
    }
detected_iscsi_drives:
  description:
    - list of detected iSCSI drive
  returned: always
  type: list
  sample: >-
    [
        {
            "address": [
                "192.168.0.57:3260"
            ],
            "canonical_name": "naa.60014055f198fb3d0cb4bd7ae1f802e1",
            "iscsi_name": "iqn.2021-03.local.iscsi-target:iscsi-storage.target0"
        }
    ]
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

import re
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils.basic import AnsibleModule


class VMwareHostiScsiInfo(PyVmomi):
    def __init__(self, module):
        super(VMwareHostiScsiInfo, self).__init__(module)
        self.esxi_hostname = self.params['esxi_hostname']

    def get_iscsi_config(self):
        iscsi_enabled = self.host_obj.config.storageDevice.softwareInternetScsiEnabled
        self.existing_system_iscsi_config = {
            'iscsi_enabled': iscsi_enabled
        }
        self.detected_iscsi_drives = []
        if iscsi_enabled is True:
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

            detected_iscsi_drives_information = []
            for lun in self.host_obj.config.storageDevice.scsiLun:
                if isinstance(lun, vim.host.ScsiDisk):
                    detected_iscsi_drives_information.append({
                        'key': lun.key,
                        'canonical_name': lun.canonicalName
                    })

            for scsi_adapter in self.host_obj.config.storageDevice.scsiTopology.adapter:
                if isinstance(scsi_adapter, vim.host.ScsiTopology.Interface):
                    if re.search(self.existing_system_iscsi_config['vmhba_name'], scsi_adapter.key):
                        for target in scsi_adapter.target:
                            scsi_lun = target.lun[0].scsiLun
                            for scsi_info in detected_iscsi_drives_information:
                                if scsi_info['key'] == scsi_lun:
                                    self.detected_iscsi_drives.append({
                                        'iscsi_name': target.transport.iScsiName,
                                        'canonical_name': scsi_info['canonical_name'],
                                        'address': target.transport.address
                                    })

            vnic_devices = []
            for vnic in self.host_obj.configManager.iscsiManager.QueryBoundVnics(iScsiHbaName=self.existing_system_iscsi_config['vmhba_name']):
                vnic_devices.append(vnic.vnicDevice)
            self.existing_system_iscsi_config['port_bind'] = vnic_devices

    def execute(self):
        self.host_obj = self.find_hostsystem_by_name(self.esxi_hostname)
        if not self.host_obj:
            self.module.fail_json(msg="Cannot find the specified ESXi host: %s" % self.esxi_hostname)

        self.get_iscsi_config()
        self.module.exit_json(changed=False, iscsi_properties=self.existing_system_iscsi_config, detected_iscsi_drives=self.detected_iscsi_drives)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=True)
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_host_iscsi_info = VMwareHostiScsiInfo(module)
    vmware_host_iscsi_info.execute()


if __name__ == "__main__":
    main()
