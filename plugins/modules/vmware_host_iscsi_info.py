#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
module: vmware_host_iscsi_info
short_description: Gather iSCSI configuration information of ESXi host
author:
  - sky-joker (@sky-joker)
description:
  - This module can be used to gather information about the iSCSI configuration of the ESXi host.
requirements:
  - python >= 2.7
  - PyVmomi
options:
  esxi_hostname:
    description:
    - The ESXi hostname on which to gather iSCSI settings.
    type: str
    required: True
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
'''

try:
    from pyVmomi import vim
except ImportError:
    pass


from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec
from ansible.module_utils.basic import AnsibleModule


class VMwareHostiScsiInfo(PyVmomi):
    def __init__(self, module):
        super(VMwareHostiScsiInfo, self).__init__(module)
        self.esxi_hostname = self.params['esxi_hostname']

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
        for vnic in self.host_obj.configManager.iscsiManager.QueryBoundVnics(iScsiHbaName=self.existing_system_iscsi_config['vmhba_name']):
            vnic_devices.append(vnic.vnicDevice)
        self.existing_system_iscsi_config['port_bind'] = vnic_devices

    def execute(self):
        self.host_obj = self.find_hostsystem_by_name(self.esxi_hostname)
        if not self.host_obj:
            self.module.fail_json(msg="Cannot find the specified ESXi host: %s" % self.esxi_hostname)

        self.get_iscsi_config()
        self.module.exit_json(changed=False, iscsi_properties=self.existing_system_iscsi_config)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=True)
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_host_iscsi_info = VMwareHostiScsiInfo(module)
    vmware_host_iscsi_info.execute()


if __name__ == "__main__":
    main()
