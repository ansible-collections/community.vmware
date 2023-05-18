#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Hewlett Packard Enterprise Development LP
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later


from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vsan_release_catalog
version_added: '3.7.0'
short_description: Uploads the vSAN Release Catalog
description:
  - Manually upload the vSAN Release Catalog the the vCenter
  - See https://kb.vmware.com/s/article/58891 for more details
author:
  - Philipp Fruck (@p-fruck)
requirements:
  - vSAN Management SDK, which needs to be downloaded from VMware and installed manually.
options:
  source:
    description:
      - The path to the release catalog file
    type: str
    required: true
extends_documentation_fragment:
  - community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Upload release catalog file to vCenter
  community.vmware.vmware_vsan_release_catalog:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    source: release_catalog.json
  delegate_to: localhost
'''

RETURN = r'''#
'''

import traceback

VSANPYTHONSDK_IMP_ERR = None
try:
    import vsanapiutils
    HAS_VSANPYTHONSDK = True
except ImportError:
    VSANPYTHONSDK_IMP_ERR = traceback.format_exc()
    HAS_VSANPYTHONSDK = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec


class VsanApi(PyVmomi):
    def __init__(self, module):
        super(VsanApi, self).__init__(module)

        client_stub = self.si._GetStub()
        ssl_context = client_stub.schemeArgs.get('context')
        apiVersion = vsanapiutils.GetLatestVmodlVersion(module.params['hostname'])
        vcMos = vsanapiutils.GetVsanVcMos(client_stub, context=ssl_context, version=apiVersion)
        self.vsanVumSystem = vcMos['vsan-vum-system']

    def upload_release_catalog(self, content):
        self.vsanVumSystem.VsanVcUploadReleaseDb(db=content)


def main():
    argument_spec = vmware_argument_spec()

    argument_spec.update(dict(
        source=dict(type='str', required=True)
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
    )

    source = module.params['source']
    api = VsanApi(module)

    try:
        with open(source, 'r') as f:
            api.upload_release_catalog(f.read())
    except Exception as e:
        module.fail_json(msg=str(e))

    module.exit_json(changed=True)


if __name__ == '__main__':
    main()
