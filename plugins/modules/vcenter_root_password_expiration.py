#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2023, Valentin Yonev <valentin.ionev@live.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

DOCUMENTATION = r'''
---
module: vcenter_root_password_expiration
short_description: root password expiration of vCSA
description: Manages password expiration configuration for root user of vCSA appliance
author:
    - Valentin Yonev (@valentinJonev)
requirements:
    - "python >= 3.8"
    - vSphere Automation SDK
options:
    hostname:
        description:
        - The vCenter hostname.
        required: True
        type: str
    username:
        description:
        - vCenter username
        required: True
        type: str
    password:
        description:
        - Password for specified vCenter user
        required: True
        type: str
    state:
        description:
        - present - represents that password expiration must be configured
        - absent - represents no expiration for root user
        choices: [ present, absent ]
        default: 'present'
        type: str
    email:
        description:
        - e-mail to send password expiration warnings to
        type: str
        required: false
    max_days_between_password_change:
        description:
        - Maximum days between password change
        type: int
        required: false
    min_days_between_password_change:
        description:
        - Minimum days between password change
        type: int
        required: false
    warn_days_before_password_expiration:
        description:
        - Days before password expires and password expiration e-mail should be sent
        type: int
        required: false
'''

EXAMPLES = r'''
- name: Configures expiring root password
  sap.hec.vcenter_root_password_expiration:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_localos_username }}'
    password: '{{ vcenter_password }}'
    max_days_between_password_change: 60
    min_days_between_password_change: 6
    warn_days_before_password_expiration: 7
    email: example@vmware.com
    state: present
  delegate_to: localhost

- name: Configures non-expiring root password
  sap.hec.vcenter_root_password_expiration:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_localos_username }}'
    password: '{{ vcenter_localos_password }}'
    state: absent
  delegate_to: localhost
'''

import requests

from vmware.vapi.vsphere.client import create_vsphere_client
from ansible_collections.community.vmware.plugins.module_utils.vmware import vmware_argument_spec
from ansible.module_utils.basic import AnsibleModule

class VcRootPasswordExpiration():
    def __init__(self, module: AnsibleModule) -> None:
        self.module = module
        self._state = True if self.module.params['state'] == 'present' else False
    def configure_root_account_password_policy(self):
        session = requests.session()
        session.verify = False
        requests.packages.urllib3.disable_warnings()
        _vcsa_access_endpoint = f"{self.module.params['hostname']}:5480"
        client = create_vsphere_client(server=_vcsa_access_endpoint,
                                    username=self.module.params['username'],
                                    password=self.module.params['password'],
                                    session=session)
        default_config = client.appliance.LocalAccounts.UpdateConfig()

        current_vcenter_info = client.appliance.LocalAccounts.get('root').to_dict()

        if self._state and self.module.params['min_days_between_password_change'] > self.module.params['max_days_between_password_change']:
            self.module.fail_json("min_days_between_password_change cannot be higher than max_days_between_password_change")

        if self._state:
            _password_expiration_config = {
                "email": self.module.params['email'],
                "min_days_between_password_change": self.module.params['min_days_between_password_change'],
                "max_days_between_password_change": self.module.params['max_days_between_password_change'],
                "warn_days_before_password_expiration": self.module.params['warn_days_before_password_expiration'],

            }
        else:
            _password_expiration_config = {
                "max_days_between_password_change": -1
            }
        
        _changes_dict = dict()
        for k, v in _password_expiration_config.items():
            try:
                if current_vcenter_info[k] != v:
                    _changes_dict[k] = v
                if k == 'fullname':
                    setattr(default_config, 'full_name', v)
                    continue
            except KeyError:
                '''
                Handles the case of newly installed vCenter when email field isn't present in the current config,
                because it was never set befores
                '''
                _changes_dict[k] = v
            setattr(default_config, k, v)
        session.close()
        _change_result_key = 'values_would_be_changed'
        if _changes_dict:
            if not self.module.check_mode:
                _change_result_key = 'values_changed'
                client.appliance.LocalAccounts.update('root', default_config)
            self.module.exit_json(changed=True, result={_change_result_key:_changes_dict})
        self.module.exit_json(changed=False, result="No configuration changes needed")

def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        dict(
            state=dict(default='present',
                        choices=['present', 'absent'],
                        type='str')
            ),
            email=dict(required=False, type='str'),
            max_days_between_password_change=dict(reqired=False, type='int'),
            min_days_between_password_change=dict(reqired=False, type='int'),
            warn_days_before_password_expiration=dict(reqired=False, type='int'),
        )

    module = AnsibleModule(argument_spec=argument_spec,
                            required_if=[
                                ('state', 'present', ('email', 'max_days_between_password_change', 'min_days_between_password_change', 'warn_days_before_password_expiration')),
                            ],
                           supports_check_mode=True)

    vc_root_password_policy_manager = VcRootPasswordExpiration(module)
    vc_root_password_policy_manager.configure_root_account_password_policy()
    
if __name__ == '__main__':
    main()