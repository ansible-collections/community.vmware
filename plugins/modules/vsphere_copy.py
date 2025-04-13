#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Dag Wieers (@dagwieers) <dag@wieers.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vsphere_copy
short_description: Copy a file to a VMware datastore
description:
    - Upload files to a VMware datastore through a vCenter REST API.
author:
- Dag Wieers (@dagwieers)
options:
  src:
    description:
      - The file to push to vCenter.
    required: true
    type: str
    aliases: [ name ]
  datacenter:
    description:
      - The datacenter on the vCenter server that holds the datastore.
    required: false
    type: str
  datastore:
    description:
      - The datastore to push files to.
    required: true
    type: str
  path:
    description:
      - The file to push to the datastore.
    required: true
    type: str
    aliases: [ dest ]
  timeout:
    description:
      - The timeout in seconds for the upload to the datastore.
    default: 10
    type: int
  diskformat:
    version_added: 4.2.0
    description:
      - Optional argument - Set a diskformat for certain uploads like stream optimized VMDKs
      - There is no official documentation, but it looks like V(StreamVmdk) needs to be set for stream optimized VMDKs that are uploaded to vSAN storage
      - Setting this for non-VMDK files might lead to undefined behavior and is not supported.
    choices: ["StreamVmdk"]
    type: str

notes:
  - "This module ought to be run from a system that can access the vCenter or the ESXi directly and has the file to transfer.
    It can be the normal remote target or you can change it either by using C(transport: local) or using C(delegate_to)."
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Copy file to datastore using delegate_to
  community.vmware.vsphere_copy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    src: /some/local/file
    datacenter: DC1 Someplace
    datastore: datastore1
    path: some/remote/file
  delegate_to: localhost

- name: Copy file to datastore when datacenter is inside folder called devel
  community.vmware.vsphere_copy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    src: /some/local/file
    datacenter: devel/DC1
    datastore: datastore1
    path: some/remote/file
  delegate_to: localhost

- name: Copy file to datastore using other_system
  community.vmware.vsphere_copy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    src: /other/local/file
    datacenter: DC2 Someplace
    datastore: datastore2
    path: other/remote/file
  delegate_to: other_system

- name: Copy file to datastore using other_system
  community.vmware.vsphere_copy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    src: /other/local/streamOptimized.vmdk
    datacenter: DC2 Someplace
    datastore: datastore2
    path: disk_imports/streamOptimized.vmdk
    timeout: 360
    diskformat: StreamVmdk
  delegate_to: other_system
'''

import atexit
import errno
import mmap
import os
import socket
import traceback

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six.moves.urllib.parse import urlencode, quote
from ansible.module_utils._text import to_native
from ansible.module_utils.urls import open_url
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


def vmware_path(datastore, datacenter, path, diskformat):
    ''' Constructs a URL path that vSphere accepts reliably '''
    path = "/folder/%s" % quote(path.lstrip("/"))
    # Due to a software bug in vSphere, it fails to handle ampersand in datacenter names
    # The solution is to do what vSphere does (when browsing) and double-encode ampersands, maybe others ?
    if not path.startswith("/"):
        path = "/" + path
    params = dict(dsName=datastore)
    if datacenter:
        datacenter = datacenter.replace('&', '%26')
        params["dcPath"] = datacenter
    if diskformat:
        params["diskFormat"] = diskformat
    params = urlencode(params)
    return "%s?%s" % (path, params)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        src=dict(required=True, aliases=['name']),
        datacenter=dict(required=False),
        datastore=dict(required=True),
        path=dict(required=True, aliases=['dest'], type='str'),
        timeout=dict(default=10, type='int'),
        diskformat=dict(required=False, type='str', choices=['StreamVmdk']))
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        # Implementing check-mode using HEAD is impossible, since size/date is not 100% reliable
        supports_check_mode=False,
    )

    hostname = module.params['hostname']
    username = module.params['username']
    password = module.params.get('password')
    src = module.params.get('src')
    datacenter = module.params.get('datacenter')
    datastore = module.params.get('datastore')
    path = module.params.get('path')
    diskformat = module.params.get('diskformat')
    validate_certs = module.params.get('validate_certs')
    timeout = module.params.get('timeout')

    try:
        fd = open(src, "rb")
        atexit.register(fd.close)
    except Exception as e:
        module.fail_json(msg="Failed to open src file %s" % to_native(e))

    if os.stat(src).st_size == 0:
        data = ''
    else:
        data = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ)
        atexit.register(data.close)

    remote_path = vmware_path(datastore, datacenter, path, diskformat)

    if not all([hostname, username, password]):
        module.fail_json(msg="One of following parameter is missing - hostname, username, password")
    url = 'https://%s%s' % (hostname, remote_path)

    headers = {
        "Content-Type": "application/octet-stream",
        "Content-Length": str(len(data)),
    }

    r = None
    try:
        r = open_url(url, data=data, headers=headers, method='PUT', timeout=timeout,
                     url_username=username, url_password=password, validate_certs=validate_certs,
                     force_basic_auth=True)
    except socket.error as e:
        if isinstance(e.args, tuple):
            if len(e.args) > 0:
                if e[0] == errno.ECONNRESET:
                    # vSphere resets connection if the file is in use and cannot be replaced
                    module.fail_json(msg='Failed to upload, image probably in use', status=None, errno=e[0], reason=to_native(e), url=url)
            else:
                module.fail_json(msg=to_native(e))
        else:
            module.fail_json(msg=str(e), status=None, errno=e[0], reason=str(e),
                             url=url, exception=traceback.format_exc())
    except Exception as e:
        error_code = -1
        try:
            if isinstance(e[0], int):
                error_code = e[0]
        except (KeyError, TypeError):
            pass
        module.fail_json(msg=to_native(e), status=None, errno=error_code,
                         reason=to_native(e), url=url, exception=traceback.format_exc())

    if not r:
        module.fail_json(msg="Failed to upload", url=url,
                         errno=None, status=None, reason=None)
    status = r.getcode()
    if 200 <= status < 300:
        module.exit_json(changed=True, status=status, reason=r.msg, url=url)
    else:
        length = r.headers.get('content-length', None)
        if r.headers.get('transfer-encoding', '').lower() == 'chunked':
            chunked = 1
        else:
            chunked = 0

        module.fail_json(msg='Failed to upload', errno=None, status=status, reason=r.msg, length=length, headers=dict(r.headers), chunked=chunked, url=url)


if __name__ == '__main__':
    main()
