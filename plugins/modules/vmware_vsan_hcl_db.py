#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Hewlett Packard Enterprise Development LP
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later


from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vsan_hcl_db
version_added: '3.5.0'
short_description: Manages the vSAN Hardware Compatibility List (HCL) database
description:
  - Manages vSAN HCL db on vSphere
  - DB file can be downloaded from https://partnerweb.vmware.com/service/vsan/all.json
author:
  - Philipp Fruck (@p-fruck)
requirements:
  - vSAN Management SDK, which needs to be downloaded from VMware and installed manually.
options:
  source:
    description:
      - The path to the HCL db file
    type: str
    required: true
extends_documentation_fragment:
  - vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Fetch HCL db file
  ansible.builtin.get_url:
    url: https://partnerweb.vmware.com/service/vsan/all.json
    dest: hcl_db.json
    force: true
  delegate_to: localhost

- name: Upload HCL db file to vCenter
  community.vmware.vmware_vsan_hcl_db:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    source: hcl_db.json
  delegate_to: localhost
'''

RETURN = r'''#
'''

import base64
import gzip
import traceback

VSANPYTHONSDK_IMP_ERR = None
try:
    import vsanapiutils
    HAS_VSANPYTHONSDK = True
except ImportError:
    VSANPYTHONSDK_IMP_ERR = traceback.format_exc()
    HAS_VSANPYTHONSDK = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class VsanApi(PyVmomi):
    def __init__(self, module):
        super(VsanApi, self).__init__(module)

        client_stub = self.si._GetStub()
        ssl_context = client_stub.schemeArgs.get('context')
        apiVersion = vsanapiutils.GetLatestVmodlVersion(module.params['hostname'])
        vcMos = vsanapiutils.GetVsanVcMos(client_stub, context=ssl_context, version=apiVersion)
        self.vsanClusterHealthSystem = vcMos['vsan-cluster-health-system']

    def upload_hcl_db(self, content):
        compressed = gzip.compress(content)
        payload_b64 = base64.b64encode(compressed).decode('ascii')
        self.vsanClusterHealthSystem.VsanVcUploadHclDb(db=payload_b64)


def main():
    argument_spec = base_argument_spec()

    argument_spec.update(dict(
        source=dict(type='str', required=True)
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
    )

    source = module.params['source']
    api = VsanApi(module)

    try:
        with open(source, 'rb') as f:
            api.upload_hcl_db(f.read())
    except Exception as e:
        module.fail_json(msg=str(e))

    module.exit_json(changed=True)


if __name__ == '__main__':
    main()
