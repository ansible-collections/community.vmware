# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):
    # Parameters for VMware REST Client based modules
    DOCUMENTATION = r'''
options:
  hostname:
    description:
    - The hostname or IP address of the vSphere vCenter server.
    - If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.
    type: str
  username:
    description:
    - The username of the vSphere vCenter server.
    - If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.
    type: str
    aliases: [ admin, user ]
  password:
    description:
    - The password of the vSphere vCenter server.
    - If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.
    type: str
    aliases: [ pass, pwd ]
  validate_certs:
    description:
    - Allows connection when SSL certificates are not valid.
    - Set to C(false) when certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
    default: true
  port:
    description:
    - The port number of the vSphere vCenter.
    - If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.
    type: int
    default: 443
  protocol:
    description:
    - The connection to protocol.
    type: str
    choices: [ http, https ]
    default: https
  proxy_host:
    description:
    - Address of a proxy that will receive all HTTPS requests and relay them.
    - The format is a hostname or a IP.
    - If the value is not specified in the task, the value of environment variable C(VMWARE_PROXY_HOST) will be used instead.
    type: str
    required: false
  proxy_port:
    description:
    - Port of the HTTP proxy that will receive all HTTPS requests and relay them.
    - If the value is not specified in the task, the value of environment variable C(VMWARE_PROXY_PORT) will be used instead.
    type: int
    required: false
'''
