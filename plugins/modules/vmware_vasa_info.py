#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Pure Storage, Inc.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vasa_info
version_added: '3.8.0'
short_description: Gather information about vSphere VASA providers.
description:
- Returns basic information on the vSphere VASA providers registered in the
  vcenter.
author:
- Eugenio Grosso (@genegr) <eugenio.grosso@purestorage.com>
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Get VASA providers info
  community.vmware.vmware_vasa_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost
  register: providers
'''

RETURN = r'''
vasa_providers:
  description: list of dictionary of VASA info
  returned: success
  type: list
  sample: [
            {
                "certificate_status": "valid",
                "description": "IOFILTER VASA Provider on host host01.domain.local",
                "name": "IOFILTER Provider host01.domain.local",
                "related_storage_array": [
                    {
                        "active": "True",
                        "array_id": "IOFILTERS:616d4715-7de2-7be2-997a-10f920c5fdbe",
                        "manageable": "True",
                        "priority": "1"
                    }
                ],
                "status": "online",
                "uid": "02e10bc5-dd77-4ce4-9100-5aee44e7abaa",
                "url": "https://host01.domain.local:9080/version.xml",
                "version": "1.0"
            },
    ]
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_sms import SMS
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class SMSClient(SMS):
    def __init__(self, module):
        super(SMSClient, self).__init__(module)

    def get_vasa_provider_info(self):
        self.get_sms_connection()

        results = dict(changed=False, vasa_providers=[])
        storage_manager = self.sms_si.QueryStorageManager()
        storage_providers = storage_manager.QueryProvider()

        for provider in storage_providers:
            provider_info = provider.QueryProviderInfo()
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

            results['vasa_providers'].append(temp_provider_info)

        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    sms_client = SMSClient(module)
    sms_client.get_vasa_provider_info()


if __name__ == '__main__':
    main()
