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
module: vmware_content_library_manager
deprecated:
  removed_in: 7.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.local_content_library) and M(vmware.vmware.subscribed_content_library) instead.
short_description: Create, update and delete VMware content library
description:
- Module to manage VMware content Library
- Content Library feature is introduced in vSphere 6.0 version, so this module is not supported in the earlier versions of vSphere.
author:
- Pavan Bidkar (@pgbidkar)
requirements:
- vSphere Automation SDK
options:
    library_name:
      description:
      - The name of VMware content library to manage.
      type: str
      required: true
    library_description:
      description:
      - The content library description.
      - This is required only if O(state=present).
      - This parameter is ignored, when O(state=absent).
      - Process of updating content library only allows description change.
      type: str
      required: false
    library_type:
      description:
      - The content library type.
      - This is required only if O(state=resent).
      - This parameter is ignored, when O(state=absent).
      type: str
      required: false
      default: 'local'
      choices: [ 'local', 'subscribed' ]
    datastore_name:
      description:
      - Name of the datastore on which backing content library is created.
      - This is required if O(state=present).
      - This parameter is ignored, when O(state=absent).
      - Currently only datastore backing creation is supported.
      type: str
      required: false
      aliases: ['datastore']
    subscription_url:
      description:
      - The url of the content library to subscribe to.
      - This is required if O(library_type=subscribed).
      - This parameter is ignored, when O(state=absent).
      type: str
      default: ''
      required: false
    ssl_thumbprint:
      description:
      - The SHA1 SSL thumbprint of the subscribed content library to subscribe to.
      - This is required if O(library_type=subscribed) and the library is https.
      - This parameter is ignored, when O(state=absent).
      - 'The information can be extracted using openssl using the following example:
        C(echo | openssl s_client -connect test-library.com:443 |& openssl x509 -fingerprint -noout)'
      type: str
      default: ''
      required: false
    update_on_demand:
      description:
      - Whether to download all content on demand.
      - If set to V(true), all content will be downloaded on demand.
      - If set to V(false) content will be downloaded ahead of time.
      - This is required if O(library_type=subscribed).
      - This parameter is ignored, when O(state=absent).
      type: bool
      default: false
    state:
      description:
      - The state of content library.
      - If set to V(present) and library does not exists, then content library is created.
      - If set to V(present) and library exists, then content library is updated.
      - If set to V(absent) and library exists, then content library is deleted.
      - If set to V(absent) and library does not exists, no action is taken.
      type: str
      required: false
      default: 'present'
      choices: [ 'present', 'absent' ]
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation

'''
EXAMPLES = r'''
- name: Create Local Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    library_description: 'Library with Datastore Backing'
    library_type: local
    datastore_name: datastore
    state: present
  delegate_to: localhost

- name: Create Subscribed Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    library_description: 'Subscribed Library with Datastore Backing'
    library_type: subscribed
    datastore_name: datastore
    subscription_url: 'https://library.url'
    ssl_thumbprint: 'aa:bb:cc:dd:ee:ff:gg:hh:ii:jj:kk:ll:mm:nn:oo:pp:qq:rr:ss:tt'
    update_on_demand: true
    state: present
  delegate_to: localhost

- name: Update Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    library_description: 'Library with Datastore Backing'
    state: present
  delegate_to: localhost

- name: Delete Content Library
  community.vmware.vmware_content_library_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    library_name: test-content-lib
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
content_library_info:
  description: library creation success and library_id
  returned: on success
  type: dict
  sample: {
      "library_id": "d0b92fa9-7039-4f29-8e9c-0debfcb22b72",
      "library_description": 'Test description',
      "library_type": 'LOCAL',
      "msg": "Content Library 'demo-local-lib-4' created.",
    }
'''

import uuid
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import rest_compatible_argument_spec

HAS_VAUTOMATION_PYTHON_SDK = False
try:
    from com.vmware.content_client import LibraryModel
    from com.vmware.content.library_client import StorageBacking, SubscriptionInfo
    from com.vmware.vapi.std.errors_client import ResourceInaccessible
    HAS_VAUTOMATION_PYTHON_SDK = True
except ImportError:
    pass


class VmwareContentLibCreate(VmwareRestClient):
    def __init__(self, module):
        """Constructor."""
        super(VmwareContentLibCreate, self).__init__(module)
        self.content_service = self.api_client
        self.local_libraries = dict()
        # Track all existing library names, to  block update/delete if duplicates exist
        self.existing_library_names = []
        self.library_name = self.params.get('library_name')
        self.library_description = self.params.get('library_description')
        self.library_type = self.params.get('library_type')
        self.library_types = dict()
        self.subscription_url = self.params.get('subscription_url')
        self.ssl_thumbprint = self.params.get('ssl_thumbprint')
        self.datastore_name = self.params.get('datastore_name')
        self.update_on_demand = self.params.get('update_on_demand')
        self.library_types = {
            'local': self.content_service.content.LocalLibrary,
            'subscribed': self.content_service.content.SubscribedLibrary
        }

        # Import objects of both types to prevent duplicate names
        self.get_all_libraries(self.library_types['local'])
        self.get_all_libraries(self.library_types['subscribed'])

        # Set library type for create/update actions
        self.library_service = self.library_types[self.library_type]
        self.pyv = PyVmomi(module=module)

    def process_state(self):
        """
        Manage states of Content Library
        """
        self.desired_state = self.params.get('state')
        library_states = {
            'absent': {
                'present': self.state_destroy_library,
                'absent': self.state_exit_unchanged,
            },
            'present': {
                'present': self.state_update_library,
                'absent': self.state_create_library,
            }
        }
        library_states[self.desired_state][self.check_content_library_status()]()

    def get_all_libraries(self, library_service):
        content_libs = library_service.list()
        if content_libs:
            for content_lib in content_libs:
                lib_details = library_service.get(content_lib)
                lib_dict = dict(
                    lib_name=lib_details.name,
                    lib_description=lib_details.description,
                    lib_id=lib_details.id,
                    lib_type=lib_details.type
                )
                if lib_details.type == "SUBSCRIBED":
                    lib_dict["lib_sub_url"] = lib_details.subscription_info.subscription_url
                    lib_dict["lib_sub_on_demand"] = lib_details.subscription_info.on_demand
                    lib_dict["lib_sub_ssl_thumbprint"] = lib_details.subscription_info.ssl_thumbprint

                self.local_libraries[lib_details.name] = lib_dict
                self.existing_library_names.append(lib_details.name)

    def check_content_library_status(self):
        """
        Check if Content Library exists or not
        Returns: 'present' if library found, else 'absent'

        """
        ret = 'present' if self.library_name in self.local_libraries else 'absent'
        return ret

    def fail_when_duplicated(self):
        if self.existing_library_names.count(self.library_name) > 1:
            self.module.fail_json(msg="Operation cannot continue, library [%s] is not unique" % self.library_name)

    def state_exit_unchanged(self):
        """
        Return unchanged state

        """
        self.module.exit_json(changed=False)

    def set_subscription_spec(self):
        if "https:" in self.subscription_url and not self.ssl_thumbprint:
            self.module.fail_json(msg="While using HTTPS, a SSL thumbprint must be provided.")
        subscription_info = SubscriptionInfo()
        subscription_info.on_demand = self.update_on_demand
        subscription_info.automatic_sync_enabled = True
        subscription_info.subscription_url = self.subscription_url

        if "https:" in self.subscription_url:
            subscription_info.ssl_thumbprint = self.ssl_thumbprint
        return subscription_info

    def create_update(self, spec, library_id=None, update=False):
        """
        Create or update call and exit cleanly if call completes
        """
        if self.module.check_mode:
            action = 'would be updated' if update else 'would be created'
        else:
            try:
                if update:
                    self.library_service.update(library_id, spec)
                    action = "updated"
                else:
                    library_id = self.library_service.create(
                        create_spec=spec,
                        client_token=str(uuid.uuid4())
                    )
                    action = "created"
            except ResourceInaccessible as e:
                message = ("vCenter Failed to make connection to %s with exception: %s "
                           "If using HTTPS, check that the SSL thumbprint is valid" % (self.subscription_url, str(e)))
                self.module.fail_json(msg=message)

        content_library_info = dict(
            msg="Content Library '%s' %s." % (spec.name, action),
            library_id=library_id,
            library_description=self.library_description,
            library_type=spec.type,
        )
        if spec.type == "SUBSCRIBED":
            content_library_info["library_subscription_url"] = spec.subscription_info.subscription_url
            content_library_info["library_subscription_on_demand"] = spec.subscription_info.on_demand
            content_library_info["library_subscription_ssl_thumbprint"] = spec.subscription_info.ssl_thumbprint
        self.module.exit_json(
            changed=True,
            content_library_info=content_library_info
        )

    def state_create_library(self):
        # Fail if no datastore is specified
        if not self.datastore_name:
            self.module.fail_json(msg="datastore_name must be specified for create operations")
        # Find the datastore by the given datastore name
        datastore_id = self.pyv.find_datastore_by_name(datastore_name=self.datastore_name)
        if not datastore_id:
            self.module.fail_json(msg="Failed to find the datastore %s" % self.datastore_name)
        self.datastore_id = datastore_id._moId
        # Build the storage backing for the library to be created
        storage_backings = []
        storage_backing = StorageBacking(type=StorageBacking.Type.DATASTORE, datastore_id=self.datastore_id)
        storage_backings.append(storage_backing)

        # Build the specification for the library to be created
        create_spec = LibraryModel()
        create_spec.name = self.library_name
        create_spec.description = self.library_description
        self.library_types = {'local': create_spec.LibraryType.LOCAL,
                              'subscribed': create_spec.LibraryType.SUBSCRIBED}
        create_spec.type = self.library_types[self.library_type]
        create_spec.storage_backings = storage_backings

        # Build subscribed specification
        if self.library_type == "subscribed":
            subscription_info = self.set_subscription_spec()
            subscription_info.authentication_method = SubscriptionInfo.AuthenticationMethod.NONE
            create_spec.subscription_info = subscription_info

        self.create_update(spec=create_spec)

    def state_update_library(self):
        """
        Update Content Library

        """
        self.fail_when_duplicated()
        changed = False
        library_id = self.local_libraries[self.library_name]['lib_id']

        library_update_spec = LibraryModel()

        # Ensure library types are consistent
        existing_library_type = self.local_libraries[self.library_name]['lib_type'].lower()
        if existing_library_type != self.library_type:
            self.module.fail_json(msg="Library [%s] is of type %s, cannot be changed to %s" %
                                  (self.library_name, existing_library_type, self.library_type))

        # Compare changeable subscribed attributes
        if self.library_type == "subscribed":
            existing_subscription_url = self.local_libraries[self.library_name]['lib_sub_url']
            sub_url_changed = (existing_subscription_url != self.subscription_url)

            existing_on_demand = self.local_libraries[self.library_name]['lib_sub_on_demand']
            sub_on_demand_changed = (existing_on_demand != self.update_on_demand)

            sub_ssl_thumbprint_changed = False
            if "https:" in self.subscription_url and self.ssl_thumbprint:
                existing_ssl_thumbprint = self.local_libraries[self.library_name]['lib_sub_ssl_thumbprint']
                sub_ssl_thumbprint_changed = (existing_ssl_thumbprint != self.ssl_thumbprint)

            if sub_url_changed or sub_on_demand_changed or sub_ssl_thumbprint_changed:
                subscription_info = self.set_subscription_spec()
                library_update_spec.subscription_info = subscription_info
                changed = True

        # Compare description
        library_desc = self.local_libraries[self.library_name]['lib_description']
        desired_lib_desc = self.params.get('library_description')
        if library_desc != desired_lib_desc:
            library_update_spec.description = desired_lib_desc
            changed = True

        if changed:
            library_update_spec.name = self.library_name
            self.create_update(spec=library_update_spec, library_id=library_id, update=True)

        content_library_info = dict(msg="Content Library %s is unchanged." % self.library_name, library_id=library_id)
        self.module.exit_json(changed=False,
                              content_library_info=dict(msg=content_library_info, library_id=library_id))

    def state_destroy_library(self):
        """
        Delete Content Library

        """
        self.fail_when_duplicated()
        library_id = self.local_libraries[self.library_name]['lib_id']
        # Setup library service based on existing object type to allow library_type to unspecified
        library_service = self.library_types[self.local_libraries[self.library_name]['lib_type'].lower()]
        if self.module.check_mode:
            action = 'would be deleted'
        else:
            action = 'deleted'
            library_service.delete(library_id=library_id)
        self.module.exit_json(
            changed=True,
            content_library_info=dict(
                msg="Content Library '%s' %s." % (self.library_name, action),
                library_id=library_id
            )
        )


def main():
    argument_spec = rest_compatible_argument_spec()
    argument_spec.update(
        library_name=dict(type='str', required=True),
        library_description=dict(type='str', required=False),
        library_type=dict(type='str', required=False, choices=['local', 'subscribed'], default='local'),
        datastore_name=dict(type='str', required=False, aliases=['datastore']),
        state=dict(type='str', choices=['present', 'absent'], default='present', required=False),
        subscription_url=dict(type='str', default='', required=False),
        ssl_thumbprint=dict(type='str', default='', required=False),
        update_on_demand=dict(type='bool', default=False, required=False),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_if=[
            ('library_type', 'subscribed', ['subscription_url']),
        ],
    )

    vmware_contentlib_create = VmwareContentLibCreate(module)
    vmware_contentlib_create.process_state()


if __name__ == '__main__':
    main()
