#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vsphere_file
short_description: Manage files on a vCenter datastore
description:
- Manage files on a vCenter datastore.
author:
- Dag Wieers (@dagwieers)
options:
  datacenter:
    description:
    - The datacenter on the vCenter server that holds the datastore.
    type: str
    required: true
  datastore:
    description:
    - The datastore on the vCenter server to push files to.
    type: str
    required: true
  path:
    description:
    - The file or directory on the datastore on the vCenter server.
    type: str
    required: true
    aliases: [ dest ]
  timeout:
    description:
    - The timeout in seconds for the upload to the datastore.
    type: int
    default: 10
  state:
    description:
    - The state of or the action on the provided path.
    - If V(absent), the file will be removed.
    - If V(directory), the directory will be created.
    - If V(file), more information of the (existing) file will be returned.
    - If V(touch), an empty file will be created if the path does not exist.
    type: str
    choices: [ absent, directory, file, touch ]
    default: file
notes:
- The vSphere folder API does not allow to remove directory objects.
extends_documentation_fragment:
- vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Create an empty file on a datastore
  community.vmware.vsphere_file:
    hostname: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC1 Someplace
    datastore: datastore1
    path: some/remote/file
    state: touch
  delegate_to: localhost

- name: Create a directory on a datastore
  community.vmware.vsphere_file:
    hostname: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC2 Someplace
    datastore: datastore2
    path: other/remote/file
    state: directory
  delegate_to: localhost

- name: Query a file on a datastore
  community.vmware.vsphere_file:
    hostname: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC1 Someplace
    datastore: datastore1
    path: some/remote/file
    state: file
  delegate_to: localhost
  ignore_errors: true

- name: Delete a file on a datastore
  community.vmware.vsphere_file:
    hostname: '{{ vhost }}'
    username: '{{ vuser }}'
    password: '{{ vpass }}'
    datacenter: DC2 Someplace
    datastore: datastore2
    path: other/remote/file
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
'''

import socket

from ansible.module_utils.basic import AnsibleModule
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
from ansible.module_utils.urls import open_url
from ansible.module_utils.common.text.converters import to_native
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


def vmware_path(datastore, datacenter, path):
    ''' Constructs a URL path that VSphere accepts reliably '''
    path = '/folder/{path}'.format(path=quote(path.strip('/')))
    # Due to a software bug in vSphere, it fails to handle ampersand in datacenter names
    # The solution is to do what vSphere does (when browsing) and double-encode ampersands, maybe others ?
    datacenter = datacenter.replace('&', '%26')
    if not path.startswith('/'):
        path = '/' + path
    params = dict(dsName=datastore)
    if datacenter:
        params['dcPath'] = datacenter
    return '{0}?{1}'.format(path, urlencode(params))


def main():

    argument_spec = base_argument_spec()

    argument_spec.update(dict(
        datacenter=dict(type='str', required=True),
        datastore=dict(type='str', required=True),
        path=dict(type='str', required=True, aliases=['dest']),
        state=dict(type='str', default='file', choices=['absent', 'directory', 'file', 'touch']),
        timeout=dict(type='int', default=10),
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    host = module.params.get('hostname')
    username = module.params.get('username')
    password = module.params.get('password')
    datacenter = module.params.get('datacenter')
    datastore = module.params.get('datastore')
    path = module.params.get('path')
    validate_certs = module.params.get('validate_certs')
    timeout = module.params.get('timeout')
    state = module.params.get('state')

    remote_path = vmware_path(datastore, datacenter, path)
    url = 'https://%s%s' % (host, remote_path)

    result = dict(
        path=path,
        size=None,
        state=state,
        status=None,
        url=url,
    )

    # Check if the file/directory exists
    try:
        r = open_url(url, method='HEAD', timeout=timeout,
                     url_username=username, url_password=password,
                     validate_certs=validate_certs, force_basic_auth=True)
    except HTTPError as e:
        r = e
    except socket.error as e:
        module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)
    except Exception as e:
        module.fail_json(msg=to_native(e), errno=dir(e), reason=to_native(e), **result)

    status = r.getcode()
    if status == 200:
        exists = True
        result['size'] = int(r.headers.get('content-length', None))
    elif status == 404:
        exists = False
    else:
        result['reason'] = r.msg
        result['status'] = status
        module.fail_json(msg="Failed to query for file '%s'" % path, errno=None, headers=dict(r.headers), **result)

    if state == 'absent':
        if not exists:
            module.exit_json(changed=False, **result)

        if module.check_mode:
            result['reason'] = 'No Content'
            result['status'] = 204
        else:
            try:
                r = open_url(url, method='DELETE', timeout=timeout,
                             url_username=username, url_password=password,
                             validate_certs=validate_certs, force_basic_auth=True)
            except HTTPError as e:
                r = e
            except socket.error as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)
            except Exception as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)

            result['reason'] = r.msg
            result['status'] = r.getcode()

            if result['status'] == 405:
                result['state'] = 'directory'
                module.fail_json(msg='Directories cannot be removed with this module', errno=None, headers=dict(r.headers), **result)
            elif result['status'] != 204:
                module.fail_json(msg="Failed to remove '%s'" % path, errno=None, headers=dict(r.headers), **result)

        result['size'] = None
        module.exit_json(changed=True, **result)

    # NOTE: Creating a file in a non-existing directory, then remove the file
    elif state == 'directory':
        if exists:
            module.exit_json(changed=False, **result)

        if module.check_mode:
            result['reason'] = 'Created'
            result['status'] = 201
        else:
            # Create a temporary file in the new directory
            remote_path = vmware_path(datastore, datacenter, path + '/foobar.tmp')
            temp_url = 'https://%s%s' % (host, remote_path)

            try:
                r = open_url(temp_url, method='PUT', timeout=timeout,
                             url_username=username, url_password=password,
                             validate_certs=validate_certs, force_basic_auth=True)
            except HTTPError as e:
                r = e
            except socket.error as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)
            except Exception as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)

            result['reason'] = r.msg
            result['status'] = r.getcode()
            if result['status'] != 201:
                result['url'] = temp_url
                module.fail_json(msg='Failed to create temporary file', errno=None, headers=dict(r.headers), **result)

            try:
                r = open_url(temp_url, method='DELETE', timeout=timeout,
                             url_username=username, url_password=password,
                             validate_certs=validate_certs, force_basic_auth=True)
            except HTTPError as e:
                r = e
            except socket.error as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)
            except Exception as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)

            status = r.getcode()
            if status != 204:
                result['reason'] = r.msg
                result['status'] = status
                module.warn('Failed to remove temporary file ({reason})'.format(**result))

        module.exit_json(changed=True, **result)

    elif state == 'file':

        if not exists:
            result['state'] = 'absent'
            result['status'] = status
            module.fail_json(msg="File '%s' is absent, cannot continue" % path, **result)

        result['status'] = status
        module.exit_json(changed=False, **result)

    elif state == 'touch':
        if exists:
            result['state'] = 'file'
            module.exit_json(changed=False, **result)

        if module.check_mode:
            result['reason'] = 'Created'
            result['status'] = 201
        else:
            try:
                r = open_url(url, method='PUT', timeout=timeout,
                             url_username=username, url_password=password,
                             validate_certs=validate_certs, force_basic_auth=True)
            except HTTPError as e:
                r = e
            except socket.error as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)
            except Exception as e:
                module.fail_json(msg=to_native(e), errno=e[0], reason=to_native(e), **result)

            result['reason'] = r.msg
            result['status'] = r.getcode()
            if result['status'] != 201:
                module.fail_json(msg="Failed to touch '%s'" % path, errno=None, headers=dict(r.headers), **result)

        result['size'] = 0
        result['state'] = 'file'
        module.exit_json(changed=True, **result)


if __name__ == '__main__':
    main()
