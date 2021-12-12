#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Ansible Project
# Copyright: (c) 2022, Nick Curry <code@nickcurry.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: vmware_content_library_item
short_description: Create, update and delete VMware content library items
description:
- Module to manage VMware content library items
- Content Library feature is introduced in vSphere 6.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.
author:
- Nick Curry (@nccurry)
notes:
- Tested on vSphere 7.0
requirements:
- python >= 3.5
- PyVmomi
- vSphere Automation SDK
options:
    content_library_name:
      description:
      - The name of VMware content library where the item is stored
      - One of content_library_name or content_library_id is required
      type: str
      required: false
    content_library_id:
      description:
      - The id of VMware content library where the item is stored
      - One of content_library_name or content_library_id is required
      type: str
      required: false
    content_library_item_name:
      description:
      - The name of the content library item
      - One of content_library_item_name or content_library_id is required
      type: str
      required: false
    content_library_item_id:
      description:
      - The id of the content library item
      - One of content_library_item_id or content_library_id is required
      type: str
      required: false
    content_library_item_description:
      description:
      - The description of the content library item
      type: str
      required: false
    content_library_item_type:
      description:
      - The content library service type of the content library item
      type: str
      required: false
    content_library_item_uri_ssl_thumbprint:
      description:
      - SSL thumbprint of the uri web server certificate
      - This is required only if I(uri) uses an https URI scheme and I(state) is set to C(present)
      - This parameter is ignored, when I(state) is set to C(absent).
      type: str
      required: false
    uri:
      description:
      - https, http, or ds URI to the content library item
      - This is required only if I(state) is set to C(present).
      - This parameter is ignored, when I(state) is set to C(absent).
      type: str
      required: false
    create_only:
      description:
      - Create the content library item only if an item with the same name or id doesn't already exist
      - If a content library item with the same name or id already exists, do nothing
      type: bool
      required: false
    state:
      description:
      - The state of content library item.
      - If set to C(present) and item does not exists, then content library item is created.
      - If set to C(present) and item exists, then content library item is updated.
      - If set to C(absent) and item exists, then content library is deleted.
      - If set to C(absent) and item does not exists, no action is taken.
      type: str
      required: false
      default: 'present'
      choices: [ 'present', 'absent' ]
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation
'''
EXAMPLES = r'''
- name: Create a local content library item using an https URI scheme
  community.vmware.vmware_content_library_item:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    content_library_name: content_library
    content_library_item_name: fedora-coreos-35.20211029.3.0-vmware.x86_64.ova
    content_library_item_description: "Fedora CoreOS 35"
    uri: "https://builds.coreos.fedoraproject.org/prod/streams/stable/builds/35.20211119.3.0/x86_64/fedora-coreos-35.20211119.3.0-vmware.x86_64.ova"
    content_library_item_uri_ssl_thumbprint: "EC:AA:D8:83:2C:05:ED:4F:B7:B1:0D:C4:27:79:FF:BE:B9:F9:F5:5C"

- name: Create a local content library item using an http URI scheme
  community.vmware.vmware_content_library_item:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    content_library_id: f19e22d1-290c-4fda-800b-8550ff36380b
    content_library_item_name: fedora-coreos-35.20211029.3.0-vmware.x86_64.ova
    content_library_item_type: ovf
    uri: "http://webserver.com/fedora-coreos-35.20211029.3.0-vmware.x86_64.ova"

- name: Create a local content library item using an ds URI scheme
  community.vmware.vmware_content_library_item:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    content_library_id: f19e22d1-290c-4fda-800b-8550ff36380b
    content_library_item_name: cli_tools.tar.gz
    uri: "ds:///vmfs/volumes/71a9a63f-4ec2bd96-556e-a8a1599a907d/cli_tools.tar.gz"

- name: Delete a local content library item by name
  community.vmware.vmware_content_library_item:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    content_library_name: content_library
    content_library_item_name: fedora-coreos-35.20211029.3.0-vmware.x86_64.ova
    state: absent
    
- name: Delete a local content library item by id
  community.vmware.vmware_content_library_item:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    content_library_id: f19e22d1-290c-4fda-800b-8550ff36380b
    content_library_item_id: 33aa3990-7f2d-49fc-86b5-c96988c78ab2
    state: absent
'''
RETURN = r'''
vmware_content_library:
  description: VMware content library information
  returned: on success
  type: dict
  sample: {
    "id": "e19e22d1-290c-4fda-800b-8550ff36380a",
    "name": "fedora-content-library"
  }
vmware_content_library_item:
  description: VMware content library item information
  returned: on success
  type: dict
  sample: {
    "cached": "true",
    "certificate_verification_info": {
        "status": "NOT_AVAILABLE"
    },
    "content_version": "2",
    "creation_time": "2021-12-10 20:21:45.868000",
    "description": "Fedora CoreOS 35",
    "id": "8aa3612a-a4cf-4a0d-a8d8-86658d5f9ea7",
    "last_modified_time": "2021-12-10 20:24:28.558000",
    "last_sync_time": "None",
    "library_id": "f19e22d1-290c-4fda-800b-8550ff36380a",
    "metadata_version": "1",
    "name": "fedora-coreos-35.20211119.3.0-vmware.x86_64.ova" ,
    "security_compliance": "true",
    "size": 817418240,
    "source_id": "None",
    "type": "ovf",
    "version": "1"
  }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
import uuid
import urllib3
import time

try:
    from com.vmware.vapi.std_client import LocalizableMessage
    from com.vmware.vapi.std.errors_client import NotFound, Error

except ImportError:
    pass


class VmwareContentLibraryItemClient(VmwareRestClient):
    def __init__(self, module):
        """Constructor."""
        # Initialize superclass methods
        super(VmwareContentLibraryItemClient, self).__init__(module)

        # Initialize member variables
        self.module = module
        self.result = dict(
            changed=False,
            vmware_content_library=None,
            vmware_content_library_item=None
        )
        self._content_library = None
        self._content_library_item = None
        self._error = None

        # Get parameters
        self.content_library_name = self.params.get('content_library_name')
        self.content_library_id = self.params.get('content_library_id')
        self.content_library_item_name = self.params.get('content_library_item_name')
        self.content_library_item_id = self.params.get('content_library_item_id')
        self.content_library_item_description = self.params.get('content_library_item_description')
        self.content_library_item_type = self.params.get('content_library_item_type')
        self.content_library_item_uri_ssl_thumbprint = self.params.get('content_library_item_uri_ssl_thumbprint')
        self.create_only = self.params.get('create_only')
        self.uri = self.params.get('uri')
        self.state = self.params.get('state')

    def get_content_library(self):
        """Get a vCenter content library and store it as a member variable. On error, state is stored in self._error."""
        if self.content_library_id is not None:
            self._content_library, self._error = self.get_content_library_by_id(self.api_client, self.content_library_id)

            if self._error:
                self._fail()

            # Now that we have the name too, set it
            self.content_library_name = self._content_library.name

        elif self.content_library_name is not None:
            self._content_library, self._error = self.get_content_library_by_name(self.api_client, self.content_library_name)

            if self._error:
                self._fail()

            # Now that we have the id too, set it
            self.content_library_id = self._content_library.id

        else:
            self._fail("You must supply a value for either content_library_id or content_library_name")

    @staticmethod
    def get_content_library_by_id(api_client, content_library_id):
        """Get a vCenter content library by its ID.
        Parameters
        ---------
        api_client: vmware.vapi.vsphere.client.VsphereClient
            vSphere API Client
        content_library_id: str
            The ID of the vCenter content library.
        Returns
        ---------
        result: (LibraryModel, Union[Error, str])
            A tuple of the com.vmware.content_client.LibraryModel object of the vCenter content library and an Union[com.vmware.vapi.std.errors_client.Error, str] object if there is an error.
        """
        try:
            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.html#com.vmware.content_client.Library.get
            return api_client.content.Library.get(content_library_id), None
        except Error as e:
            return None, e

    @staticmethod
    def get_content_library_by_name(api_client, content_library_name):
        """Get a vCenter content library by its name. Method will fail if two libraries have the same name.
        Parameters
        ---------
        api_client: vmware.vapi.vsphere.client.VsphereClient
            vSphere API Client
        content_library_name: str
            The ID of the vCenter content library.
        Returns
        ---------
        result: (LibraryModel, Union[Error, str'v)
            A tuple of the com.vmware.content_client.LibraryModel object of the vCenter content library and an Union[com.vmware.vapi.std.errors_client.Error, str] object if there is an error.
        """
        try:
            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.html#com.vmware.content_client.Library.find
            content_library_ids = api_client.content.Library.find({'name': content_library_name})

            if len(content_library_ids) > 1:  # More than one library with name content_library_name
                return None, "There are two content libraries with name %s, library name must be unique to get content library by name." % content_library_name

            if len(content_library_ids) < 1:  # No libraries with name content_library_name
                return None, "Could not find library with name %s." % content_library_name

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.html#com.vmware.content_client.Library.get
            return api_client.content.Library.get(content_library_ids[0]), None

        except Error as e:
            return None, e

    def get_content_library_item(self, ignore_not_found=False):
        """Get a vCenter content library item and store it as a member variable. On error, state is stored in self._error.
        Parameters
        ---------
        ignore_not_found: bool
            Should NotFound errors be ignored. Used when it is expected that the content library item might not exist
        Returns
        ---------
        """
        if self.content_library_item_id is not None:
            self._content_library_item, self._error = self.get_content_library_item_by_id(self.api_client, self.content_library_item_id)

            if self._error:
                if isinstance(self._error, NotFound) and ignore_not_found:
                    self._content_library_item = None
                    self._error = None
                else:
                    self._fail()
            else:
                # Now that we have the name too, set it
                self.content_library_item_name = self._content_library_item.name

        elif self.content_library_item_name is not None and self.content_library_id is not None:
            self._content_library_item, self._error = self.get_content_library_item_by_name(self.api_client, self.content_library_id, self.content_library_item_name)

            if self._error:
                if isinstance(self._error, NotFound) and ignore_not_found:
                    self._content_library_item = None
                    self._error = None
                else:
                    self._fail()
            else:
                # Now that we have the id too, set it
                self.content_library_item_id = self._content_library_item.id

        else:
            self._fail("You must supply a value for either content_library_item_id or both content_library_item_name and content_library_id")

    @staticmethod
    def get_content_library_item_by_id(api_client, content_library_item_id):
        """Get a vCenter content library item by its ID.
        Parameters
        ---------
        api_client: vmware.vapi.vsphere.client.VsphereClient
            vSphere API Client
        content_library_item_id: str
            The ID of the vCenter content library item.
        Returns
        ---------
        result: (ItemModel, Union[Error, str])
            A tuple of the com.vmware.content.library_client.ItemModel object of the vCenter content library item and an Union[com.vmware.vapi.std.errors_client.Error, str] object if there is an error.
        """
        try:
            return api_client.content.library.Item.get(content_library_item_id), None

        except Error as e:
            return None, e

    @staticmethod
    def get_content_library_item_by_name(api_client, content_library_id, content_library_item_name):
        """Get a vCenter content library item by its name. Method will fail if two items have the same name.
        Parameters
        ---------
        api_client: vmware.vapi.vsphere.client.VsphereClient
            vSphere API Client
        content_library_id: str
            The ID of the vCenter content library.
        content_library_item_name: str
            The name of the vCenter content library item.
        Returns
        ---------
        result: (ItemModel, Union[Error, str])
            A tuple of the com.vmware.content.library_client.ItemModel object of the vCenter content library item and an Union[com.vmware.vapi.std.errors_client.Error, str] object if there is an error.
        """
        try:
            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.html#com.vmware.content.library_client.Item.find
            content_library_item_ids = api_client.content.library.Item.find({
                'name': content_library_item_name,
                'library_id': content_library_id
            })

            if len(content_library_item_ids) > 1:  # More than one library item with name content_library_item_name
                return None, "There are two content library items with name %s, libary item name must be unique to get by name." % content_library_item_name

            if len(content_library_item_ids) < 1:  # No library items with name content_library_item_name
                # Borrowing the com.vmware.vapi.std.errors_client.Error class lets us isinstance(var, NotFound) later
                return None, NotFound(
                    messages=[
                        LocalizableMessage(
                            id='not-found',
                            default_message="Could not find library item with name %s." % content_library_item_name,
                            args=[content_library_item_name]
                        )
                    ]
                )

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.html#com.vmware.content.library_client.Item.get
            return api_client.content.library.Item.get(content_library_item_ids[0]), None

        except Error as e:
            return None, e

    def create_content_library_item(self):
        """Create a vCenter content library item"""
        # If the item already exists and we're only supposed to create it, exit
        if self._content_library_item and self.create_only:
            self._exit()

        # A unique token generated on the client for each creation request, this token is used to guarantee idempotent creation
        content_library_item_session_token = str(uuid.uuid4())

        if self.content_library_id is not None \
                and self.content_library_item_name is not None \
                and self.uri is not None:

            # If content library item doesn't already exist, create it first
            new_content_library_item = False
            if not self._content_library_item:
                new_content_library_item = True
                self.content_library_item_id, self._error = self.create_content_library_item_by_details(
                    api_client=self.api_client,
                    content_library_item_session_token=content_library_item_session_token,
                    content_library_id=self.content_library_id,
                    content_library_item_name=self.content_library_item_name,
                    content_library_item_description=self.content_library_item_description,
                    content_library_item_type=self.content_library_item_type
                )

                if self._error:
                    self._fail()

            # Update content library item file contents
            file_info, self._error = self.update_content_library_item_file_by_details(
                api_client=self.api_client,
                content_library_item_session_token=content_library_item_session_token,
                uri=self.uri,
                content_library_item_id=self.content_library_item_id,
                content_library_item_name=self.content_library_item_name,
                content_library_item_uri_ssl_thumbprint=self.content_library_item_uri_ssl_thumbprint
            )

            if self._error:
                # If we failed to fully create the file and its new, cleanup after ourselves
                if new_content_library_item:
                    # TODO: Find a way to report errors here too
                    _, _ = self.delete_content_library_item_by_id(self.api_client, self.content_library_item_id)

                self._fail()

            self._changed()

        else:
            self._fail("You must supply a value for all of content_library_id, content_library_item_name, and uri.")

    @staticmethod
    def create_content_library_item_by_details(
            api_client,
            content_library_item_session_token,
            content_library_id,
            content_library_item_name,
            content_library_item_description,
            content_library_item_type=None
    ):
        """Create a vCenter content library item.
        Parameters
        ---------
        api_client: vmware.vapi.vsphere.client.VsphereClient
            vSphere API Client
        content_library_item_session_token: str
            A unique token generated on the client for each creation request, this token is used to guarantee idempotent creation.
        content_library_id: str
            The ID of the vCenter content library.
        content_library_item_name: str
            The name of the vCenter content library item.
        content_library_item_description: str
            The description of the vCenter content library item.
        content_library_item_type: str
            The content library service type of the content library item
        Returns
        ---------
        result: (Item, Union[Error, str])
            A tuple of the com.vmware.content.library.Item object of the vCenter content library item and an Union[com.vmware.vapi.std.errors_client.Error, str] object if there is an error.
        """
        try:
            if not content_library_item_type and content_library_item_name[-3:] in ['ova', 'ovf']:  # TODO: Support other content library file types
                content_library_item_type = 'ovf'

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.html#com.vmware.content.library_client.ItemModel
            content_library_item_create_spec = {
                'library_id': content_library_id,
                'description': content_library_item_description,
                'name': content_library_item_name,
                'type': content_library_item_type
            }

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.html#com.vmware.content.library_client.Item.create
            return api_client.content.library.Item.create(
                client_token=content_library_item_session_token,
                create_spec=content_library_item_create_spec
            ), None

        except Error as e:
            return None, e

    @staticmethod
    def update_content_library_item_file_by_details(
            api_client,
            uri,
            content_library_item_session_token,
            content_library_item_id,
            content_library_item_name,
            content_library_item_uri_ssl_thumbprint=None
    ):
        """Update the contents of a content library item file
        Parameters
        ---------
        api_client: vmware.vapi.vsphere.client.VsphereClient
            vSphere API Client
        content_library_item_session_token: str
            A unique token generated on the client for each creation request, this token is used to guarantee idempotent creation.
        uri: str
            https, http, or ds URI to the content library item
        content_library_item_id: str
            The id of the vCenter content library item.
        content_library_item_name: str
            The name of the vCenter content library item.
        content_library_item_uri_ssl_thumbprint: bool
            Thumbprint for the SSL certificate. Required when uri is https.
        Returns
        ---------
        result: (File.Info, Union[Error, str])
            A tuple of the com.vmware.content.library.item.updatesession_client.File.Info object of the vCenter content library item and an Union[com.vmware.vapi.std.errors_client.Error, str] object if there is an error.
        """
        content_library_item_update_session_id = None

        try:
            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.html#com.vmware.content.library.item_client.UpdateSessionModel
            content_library_item_update_session_create_spec = {
                'library_item_id': content_library_item_id,
            }

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.html#com.vmware.content.library.item_client.UpdateSession.create
            content_library_item_update_session_id = api_client.content.library.item.UpdateSession.create(
                client_token=content_library_item_session_token,
                create_spec=content_library_item_update_session_create_spec
            )

            # TODO: Figure out why this fails with large files using the ds scheme
            if uri[:8] == "https://" or uri[:7] == "http://" or uri[:5] == "ds://":  # PULL content item from external source
                # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.item.html#com.vmware.content.library.item.updatesession_client.File.AddSpec
                content_library_item_add_spec = {
                    'name': content_library_item_name,
                    'source_type': 'PULL',
                    # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.html#com.vmware.content.library.item_client.TransferEndpoint
                    'source_endpoint': {
                        'uri': uri,
                        'ssl_certificate_thumbprint': content_library_item_uri_ssl_thumbprint
                    }
                }

                # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.item.html#com.vmware.content.library.item.updatesession_client.File.add
                content_library_item_file = api_client.content.library.item.updatesession.File.add(
                    update_session_id=content_library_item_update_session_id,
                    file_spec=content_library_item_add_spec
                )

                # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.html#com.vmware.content.library.item_client.TransferStatus
                while content_library_item_file.status in ["TRANSFERRING", "VALIDATING", "WAITING_FOR_TRANSFER"]:
                    time.sleep(0.5)
                    content_library_item_file = api_client.content.library.item.updatesession.File.get(
                        content_library_item_update_session_id, content_library_item_name)

                if content_library_item_file.status == "ERROR":
                    return None, content_library_item_file.error_message.default_message

            elif uri[:7] == "file://":  # Push from local file system
                return None, "File URI file:// not supported for uri. You must use either https://, http:// or ds:// URI schemes."

                # TODO: Implement this so it works reliably for large files.
                # com.vmware.vapi.std.errors_client.NotAllowedInCurrentState: {messages : [LocalizableMessage(id='com.vmware.vdcs.cls-main.update_session_file_not_received', default_message='File fedora-coreos-35.20211119.3.0-vmware.x86_64.ova has transfer errors or has not been fully received yet (status: WAITING).', args=['fedora-coreos-35.20211119.3.0-vmware.x86_64.ova', 'WAITING'], params=None, localized=None)], data : None, error_type : NOT_ALLOWED_IN_CURRENT_STATE}
                # 2021-12-11T19:29:12.560Z | ERROR    | 8393e620-b835-4a2f-a186-18d28d454c9f-63 | transferService-pool-6-thread-9 | TransferEndpointImpl           | Session 9cdddfd6-cbc5-5a77-8c1c-96045d492d54, Item fedora-coreos-35.20211119.3.0-vmware.x86_64.ova, Endpoint ds:/vmfs/volumes/61a1a63f-4ec2bd96-556e-a8a1599a907d/contentlib-f19e22d2-290c-4fda-800b-8550ff36380a/4dd2d055-cd65-4415-9b3e-c57245ba1c30/disk_2d36c6a9-9767-48e9-805a-dda56207fd52.vmdk: IO error during transfer of ds:/vmfs/volumes/61a9a63a-4ec2bd96-556e-a8a1599a907d/contentlib-f19e22d1-290c-4fda-800b-8550ff36380d/3dd2d055-cd65-4415-9b3e-c57245ba1c31/disk_2d36c6a9-9767-48e9-805a-dda56207fd52.vmdk: Pipe closed
                # java.io.IOException: Pipe closed
                # # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.item.html#com.vmware.content.library.item.updatesession_client.File.AddSpec
                # file_size = os.path.getsize(uri)
                # content_library_item_add_spec = {
                #     'name': content_library_item_name,
                #     'source_type': 'PUSH',
                #     'size': file_size
                # }
                #
                # # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.item.html#com.vmware.content.library.item.updatesession_client.File.add
                # content_library_item_file = api_client.content.library.item.updatesession.File.add(
                #     update_session_id=content_library_item_update_session_id,
                #     file_spec=content_library_item_add_spec
                # )
                #
                # session = requests.Session()
                # session.verify = validate_certs
                # # TODO: Look into doing this asyncrounously and updating status along the way
                # with open(uri, 'rb') as file_data:
                #     response = session.put(content_library_item_file.upload_endpoint.uri, data=file_data,
                #                            timeout=None)
                #
                # if response.status_code.__str__()[0] != "2":
                #     return None, "There was an error uploading the file. %s: %s" % (
                #     response.status_code, response.reason)

            else:
                return None, "Unsupported URI scheme for uri, you must use either https://, http:// or ds:// URI schemes."

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.item.html#com.vmware.content.library.item.updatesession_client.File.validate
            content_library_item_validation_result = api_client.content.library.item.updatesession.File.validate(content_library_item_update_session_id)

            if content_library_item_validation_result.has_errors:
                if content_library_item_validation_result.missing_files is not None:
                    return None, "These files are missing and failed to upload: %s" % " ".join(content_library_item_validation_result.missing_files)

                elif content_library_item_validation_result.invalid_files is not None:
                    return None, "These files are invalid and failed to upload: %s" % " ".join(content_library_item_validation_result.invalid_files)

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.html#com.vmware.content.library.item_client.UpdateSession.complete
            api_client.content.library.item.UpdateSession.complete(content_library_item_update_session_id)

            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.item.html#com.vmware.content.library.item.updatesession_client.File.get
            return api_client.content.library.item.updatesession.File.get(content_library_item_update_session_id, content_library_item_name), None

        except Exception as e:
            if content_library_item_update_session_id is not None:
                # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.html#com.vmware.content.library.item_client.UpdateSession.get
                update_session = api_client.content.library.item.UpdateSession.get(content_library_item_update_session_id)

                if update_session.state == "ACTIVE":
                    # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.library.html#com.vmware.content.library.item_client.UpdateSession.fail
                    api_client.content.library.item.UpdateSession.fail(content_library_item_update_session_id, repr(e))

            if isinstance(e, Error):
                return None, e
            else:
                return None, repr(e)

    def delete_content_library_item(self):
        """Delete a vCenter content library item."""
        if self.content_library_item_id is not None:
            _, self._error = self.delete_content_library_item_by_id(self.api_client, self.content_library_item_id)
            self._changed()

        elif self.content_library_item_name is not None:
            self._content_library_item, self._error = self.get_content_library_item_by_name(self.api_client, self.content_library_id, self.content_library_item_name)

            if self._error:
                self._fail()
            else:
                _, self._error = self.delete_content_library_item_by_id(self.api_client, self._content_library_item.id)
                self._changed()

        else:
            self._error = "You must supply a value for either content_library_item_id or content_library_item_name"

        if self._error:
            self._fail()

    @staticmethod
    def delete_content_library_item_by_id(api_client, content_library_item_id):
        """Delete a vCenter content library item.
        Parameters
        ---------
        api_client: vmware.vapi.vsphere.client.VsphereClient
            vSphere API Client
        content_library_item_id: str
            The ID of the vCenter content library.
        Returns
        ---------
        result: (str, Union[Error, str])
            A tuple of the str of the ID of the vCenter content library and an Union[com.vmware.vapi.std.errors_client.Error, str] object if there is an error.
        """
        try:
            # https://vmware.github.io/vsphere-automation-sdk-python/vsphere/cloud/com.vmware.content.html#com.vmware.content.library_client.Item.delete
            api_client.content.library.Item.delete(library_item_id=content_library_item_id)
            return content_library_item_id, None

        except Error as e:
            return None, e

    def _verbose_log(self, message):
        if self.module._debug or self.module._verbosity >= 3:
            pass  # TODO: Implement verbose logging

    def _changed(self):
        """Set changed status in Ansible module result."""
        self.result['changed'] = True

    def _fail(self, error=None):
        """Fail Ansible module and return formatted error message.
        Parameters
        ---------
        error: Union[com.vmware.vapi.std.errors_client.Error, str]
            Error object or message
        Returns
        ---------
        """
        if error:
            self._error = error

        if isinstance(self._error, Error):
            message = ""
            for error_message in self._error.to_dict()['messages']:
                message += " " + error_message['default_message']

            self.module.fail_json(msg=message, **self.result)
        elif self._error:
            self.module.fail_json(msg=repr(self._error), **self.result)
        else:
            self.module.fail_json(msg="An unknown error occurred", **self.result)

    def _exit(self):
        """End Ansible module execution and set result values"""
        if self._content_library:
            self.result['vmware_content_library'] = dict(id=self._content_library.id, name=self._content_library.name)
        if self._content_library_item:
            self.result['vmware_content_library_item'] = self._content_library_item.to_dict()

        self.module.exit_json(**self.result)

    def process_state(self):
        """Ansible module entrypoint"""
        # Get content library.
        self.get_content_library()

        # Get content library item
        self.get_content_library_item(ignore_not_found=True)

        if self.state == 'absent':
            if not self._content_library_item:  # Item shouldn't exist and it doesn't, great!
                self._exit()

            else:  # Item exists and it shouldn't, delete it.
                self.delete_content_library_item()

        elif self.state == 'present':  # We don't care if it already exists or not, upsert it.
            self.create_content_library_item()

        else:
            self._fail("Valid values for state are either present or absent")


def main():
    # Disable InsecureRequestWarning, if they set validate_certs=false, they know the risk
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Wrangle Ansible arguments
    argument_spec = VmwareRestClient.vmware_client_argument_spec()
    argument_spec.update(
        content_library_name=dict(type='str', aliases=['library_name']),
        content_library_id=dict(type='str', aliases=['library_id']),
        content_library_item_name=dict(type='str', aliases=['item_name', 'name']),
        content_library_item_id=dict(type='str', aliases=['item_id', 'id']),
        content_library_item_description=dict(type='str', aliases=['item_description', 'description'], default=''),
        content_library_item_type=dict(type='str', aliases=['item_type', 'type']),
        content_library_item_uri_ssl_thumbprint=dict(type='str', aliases=['ssl_thumbprint'], default=None),
        create_only=dict(type='str', default=False),
        uri=dict(type='str', aliases=['file_path']),
        state=dict(type='str', choices=['present', 'absent'], default='present')
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ('content_library_name', 'content_library_id'),
            ('content_library_item_name', 'content_library_item_id')
        ],
        mutually_exclusive=[
            ('content_library_name', 'content_library_id'),
            ('content_library_item_name', 'content_library_item_id')
        ],
        required_if=[
            ('state', 'present', ['uri'], True)
        ]
    )

    # Initialize client and execute module
    vmware_content_library_item_client = VmwareContentLibraryItemClient(module)
    vmware_content_library_item_client.process_state()


if __name__ == '__main__':
    main()
