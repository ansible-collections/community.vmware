#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Pure Storage, Inc.
# Author(s): Eugenio Grosso, <eugenio.grosso@purestorage.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
module: vmware_vasa
version_added: '3.8.0'
short_description: Manage VMware Virtual Volumes storage provider
author:
  - Eugenio Grosso (@genegr) <eugenio.grosso@purestorage.com>
description:
  - This module can be used to register and unregister a VASA provider
options:
  vasa_name:
    description:
    - The name of the VASA provider to be managed.
    type: str
    required: True
  vasa_url:
    description:
    - The url  of the VASA provider to be managed.
    - This parameter is required if O(state=present)
    type: str
    required: True
  vasa_username:
    description:
    - The user account to connect to the VASA provider.
    - This parameter is required if O(state=present)
    type: str
  vasa_password:
    description:
    - The password of the user account to connect to the VASA provider.
    - This parameter is required if O(state=present)
    type: str
  vasa_certificate:
    description:
    - The SSL certificate of the VASA provider.
    - This parameter is required if O(state=present)
    type: str
  state:
    description:
    - Create (V(present)) or remove (V(absent)) a VASA provider.
    choices: [ absent, present ]
    default: present
    type: str
seealso:
- module: community.vmware.vmware_vasa_info
extends_documentation_fragment:
- vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Create Cluster
  community.vmware.vmware_cluster:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    vasa_name: "{{ vasa_name }}"
    vasa_url: "{{ vasa_url }}"
    vasa_username: "{{ vasa_username }}"
    vasa_password: "{{ vasa_password }}"
    vasa_certificate: "{{ vasa_certificate }}"
    state: present
  delegate_to: localhost

- name: Unregister VASA provider
  community.vmware.vmware_vasa:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    vasa_name: "{{ vasa_name }}"
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
'''
try:
    from pyVmomi import sms
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_sms import (
    SMS,
    TaskError,
    wait_for_sms_task)
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.common.text.converters import to_native


class VMwareVASA(SMS):
    def __init__(self, module):
        super(VMwareVASA, self).__init__(module)
        self.vasa_name = module.params['vasa_name']
        self.vasa_url = module.params['vasa_url']
        self.vasa_username = module.params['vasa_username']
        self.vasa_password = module.params['vasa_password']
        self.vasa_certificate = module.params['vasa_certificate']
        self.desired_state = module.params['state']
        self.storage_manager = None

    def process_state(self):
        """
        Manage internal states of VASA provider
        """
        vasa_states = {
            'absent': {
                'present': self.state_unregister_vasa,
                'absent': self.state_exit_unchanged,
            },
            'present': {
                'present': self.state_exit_unchanged,
                'absent': self.state_register_vasa,
            }
        }
        # Initialize connection to SMS manager
        self.get_sms_connection()
        current_state = self.check_vasa_configuration()
        # Based on the desired_state and the current_state call
        # the appropriate method from the dictionary
        vasa_states[self.desired_state][current_state]()

    def state_register_vasa(self):
        """
        Register VASA provider with vcenter
        """
        changed, result = True, None
        vasa_provider_spec = sms.provider.VasaProviderSpec()
        vasa_provider_spec.name = self.vasa_name
        vasa_provider_spec.username = self.vasa_username
        vasa_provider_spec.password = self.vasa_password
        vasa_provider_spec.url = self.vasa_url
        vasa_provider_spec.certificate = self.vasa_certificate
        try:
            if not self.module.check_mode:
                task = self.storage_manager.RegisterProvider_Task(vasa_provider_spec)
                changed, result = wait_for_sms_task(task)
                # This second step is required to register self-signed certs,
                # since the previous task returns the certificate back waiting
                # for confirmation
                if isinstance(result, sms.fault.CertificateNotTrusted):
                    vasa_provider_spec.certificate = result.certificate
                    task = self.storage_manager.RegisterProvider_Task(vasa_provider_spec)
                    changed, result = wait_for_sms_task(task)
                if isinstance(result, sms.provider.VasaProvider):
                    provider_info = result.QueryProviderInfo()
                    temp_provider_info = {
                        'name': provider_info.name,
                        'uid': provider_info.uid,
                        'description': provider_info.description,
                        'version': provider_info.version,
                        'certificate_status': provider_info.certificateStatus,
                        'url': provider_info.url,
                        'status': provider_info.status,
                        'related_storage_array': []
                    }
                    for a in provider_info.relatedStorageArray:
                        temp_storage_array = {
                            'active': str(a.active),
                            'array_id': a.arrayId,
                            'manageable': str(a.manageable),
                            'priority': str(a.priority)
                        }
                        temp_provider_info['related_storage_array'].append(temp_storage_array)
                    result = temp_provider_info

            self.module.exit_json(changed=changed, result=result)
        except TaskError as task_err:
            self.module.fail_json(msg="Failed to register VASA provider"
                                      " due to task exception %s" % to_native(task_err))
        except Exception as generic_exc:
            self.module.fail_json(msg="Failed to register VASA"
                                      " due to generic exception %s" % to_native(generic_exc))

    def state_unregister_vasa(self):
        """
        Unregister VASA provider
        """
        changed, result = True, None

        try:
            if not self.module.check_mode:
                uid = self.vasa_provider_info.uid
                task = self.storage_manager.UnregisterProvider_Task(uid)
                changed, result = wait_for_sms_task(task)
            self.module.exit_json(changed=changed, result=result)
        except Exception as generic_exc:
            self.module.fail_json(msg="Failed to unregister VASA"
                                      " due to generic exception %s" % to_native(generic_exc))

    def state_exit_unchanged(self):
        """
        Exit without any change
        """
        self.module.exit_json(changed=False)

    def check_vasa_configuration(self):
        """
        Check VASA configuration
        Returns: 'Present' if VASA provider exists, else 'absent'

        """
        self.vasa_provider_info = None
        self.storage_manager = self.sms_si.QueryStorageManager()
        storage_providers = self.storage_manager.QueryProvider()

        try:
            for provider in storage_providers:
                provider_info = provider.QueryProviderInfo()
                if provider_info.name == self.vasa_name:
                    if provider_info.url != self.vasa_url:
                        raise Exception("VASA provider '%s' URL '%s' "
                                        "is inconsistent  with task parameter '%s'"
                                        % (self.vasa_name, provider_info.url, self.vasa_url))
                    self.vasa_provider_info = provider_info
                    break
            if self.vasa_provider_info is None:
                return 'absent'
            return 'present'
        except Exception as generic_exc:
            self.module.fail_json(msg="Failed to check configuration"
                                      " due to generic exception %s" % to_native(generic_exc))


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        vasa_name=dict(type='str', required=True),
        vasa_url=dict(type='str', required=True),
        vasa_username=dict(type='str'),
        vasa_password=dict(type='str', no_log=True),
        vasa_certificate=dict(type='str'),
        state=dict(type='str',
                   default='present',
                   choices=['absent', 'present']),
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ['state', 'present', ['vasa_username', 'vasa_password', 'vasa_certificate']]
        ]
    )

    vmware_vasa = VMwareVASA(module)
    vmware_vasa.process_state()


if __name__ == '__main__':
    main()
