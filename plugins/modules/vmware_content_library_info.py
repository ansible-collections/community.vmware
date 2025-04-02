#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Ansible Project
# Copyright: (c) 2019, Pavan Bidkar <pbidkar@vmware.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_content_library_info
short_description: Gather information about VMWare Content Library
description:
- Module to list the content libraries.
- Module to get information about specific content library.
- Content Library feature is introduced in vSphere 6.0 version, so this module is not supported in the earlier versions of vSphere.
author:
- Pavan Bidkar (@pgbidkar)
requirements:
- vSphere Automation SDK
options:
    library_id:
      description:
      - content library id for which details needs to be fetched.
      type: str
      required: false
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation

'''

EXAMPLES = r'''
- name: Get List of Content Libraries
  community.vmware.vmware_content_library_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: Get information about content library
  community.vmware.vmware_content_library_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_id: '13b0f060-f4d3-4f84-b61f-0fe1b0c0a5a8'
  delegate_to: localhost
'''

RETURN = r'''
content_lib_details:
  description: list of content library metadata
  returned: on success
  type: list
  sample: [
      {
          "library_creation_time": "2019-07-02T11:50:52.242000",
          "library_description": "new description",
          "library_id": "13b0f060-f4d3-4f84-b61f-0fe1b0c0a5a8",
          "library_name": "demo-local-lib",
          "library_publish_info": {
              "authentication_method": "NONE",
              "persist_json_enabled": false,
              "publish_url": null,
              "published": false,
              "user_name": null
              },
          "library_server_guid": "0fd5813b-aac7-4b92-9fb7-f18f16565613",
          "library_type": "LOCAL",
          "library_version": "3"
        }
    ]
content_libs:
    description: list of content libraries
    returned: on success
    type: list
    sample: [
        "ded9c4d5-0dcd-4837-b1d8-af7398511e33",
        "36b72549-14ed-4b5f-94cb-6213fecacc02"
    ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import rest_compatible_argument_spec


class VmwareContentLibInfo(VmwareRestClient):
    def __init__(self, module):
        """Constructor."""
        super(VmwareContentLibInfo, self).__init__(module)
        self.content_service = self.api_client
        self.local_content_libraries = self.content_service.content.LocalLibrary.list()
        if self.local_content_libraries is None:
            self.local_content_libraries = []

        self.subscribed_content_libraries = self.content_service.content.SubscribedLibrary.list()
        if self.subscribed_content_libraries is None:
            self.subscribed_content_libraries = []

        self.library_info = []

    def get_all_content_libs(self):
        """Method to retrieve List of content libraries."""
        content_libraries = self.local_content_libraries + self.subscribed_content_libraries

        self.module.exit_json(changed=False, content_libs=content_libraries)

    def get_content_lib_details(self, library_id):
        """Method to retrieve Details of contentlib with library_id"""
        lib_publish_info = None

        if library_id in self.local_content_libraries:
            try:
                lib_details = self.content_service.content.LocalLibrary.get(library_id)
                lib_publish_info = dict(
                    persist_json_enabled=lib_details.publish_info.persist_json_enabled,
                    authentication_method=lib_details.publish_info.authentication_method,
                    publish_url=lib_details.publish_info.publish_url,
                    published=lib_details.publish_info.published,
                    user_name=lib_details.publish_info.user_name
                )
            except Exception as e:
                self.module.fail_json(exists=False, msg="%s" % self.get_error_message(e))
        elif library_id in self.subscribed_content_libraries:
            try:
                lib_details = self.content_service.content.SubscribedLibrary.get(library_id)
            except Exception as e:
                self.module.fail_json(exists=False, msg="%s" % self.get_error_message(e))
        else:
            self.module.fail_json(exists=False, msg="Library %s not found." % library_id)

        self.library_info.append(
            dict(
                library_name=lib_details.name,
                library_description=lib_details.description,
                library_id=lib_details.id,
                library_type=lib_details.type,
                library_creation_time=lib_details.creation_time,
                library_server_guid=lib_details.server_guid,
                library_version=lib_details.version,
                library_publish_info=lib_publish_info
            )
        )

        self.module.exit_json(exists=False, changed=False, content_lib_details=self.library_info)


def main():
    argument_spec = rest_compatible_argument_spec()
    argument_spec.update(
        library_id=dict(type='str', required=False),
    )
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    vmware_contentlib_info = VmwareContentLibInfo(module)
    if module.params.get('library_id'):
        vmware_contentlib_info.get_content_lib_details(module.params['library_id'])
    else:
        vmware_contentlib_info.get_all_content_libs()


if __name__ == '__main__':
    main()
