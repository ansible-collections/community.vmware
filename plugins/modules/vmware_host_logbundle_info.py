#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_logbundle_info
short_description: Gathers manifest info for logbundle
description:
    - This module can be used to gather manifest information for logbundle from ESXi.
author:
    - sky-joker (@sky-joker)
options:
    esxi_hostname:
      description:
        - Name of the host system to fetch the manifests for logbundle.
      type: str
      required: true
extends_documentation_fragment:
    - community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: fetch the manifests for logbundle from ESXi
  community.vmware.vmware_host_logbundle_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
  register: fetch_manifests_result
'''

RETURN = r'''
manifests:
    description: list of dictionary of manifest information for logbundle
    returned: always
    type: list
    sample:
      [
        {
          "enabled": "true",
          "group": "System",
          "id": "System:Base",
          "name": "Base",
          "vmOnly": "false"
        },
        {
          "enabled": "false",
          "group": "System",
          "id": "System:BaseMinmal",
          "name": "BaseMinmal",
          "vmOnly": "false"
        },
        {
          "enabled": "true",
          "group": "Fcd",
          "id": "Fcd:Catalog",
          "name": "Catalog",
          "vmOnly": "false"
        },
        {
          "enabled": "false",
          "group": "VirtualMachines",
          "id": "VirtualMachines:CoreDumpHung",
          "name": "CoreDumpHung",
          "vmOnly": "true"
        },
        {
          "enabled": "true",
          "group": "System",
          "id": "System:CoreDumps",
          "name": "CoreDumps",
          "vmOnly": "false"
        }
      ]
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
import xml.etree.ElementTree as ET


class VMwareHostLogbundleInfo(PyVmomi):
    def __init__(self, module):
        super(VMwareHostLogbundleInfo, self).__init__(module)
        self.esxi_hostname = self.params['esxi_hostname']

    def generate_req_headers(self, url):
        # get ticket
        req = vim.SessionManager.HttpServiceRequestSpec(method='httpGet', url=url)
        ticket = self.content.sessionManager.AcquireGenericServiceTicket(req)

        headers = {
            'Content-Type': 'application/octet-stream',
            'Cookie': 'vmware_cgi_ticket=%s' % ticket.id
        }

        return headers

    def get_listmanifests(self):
        url = 'https://' + self.esxi_hostname + '/cgi-bin/vm-support.cgi?listmanifests=1'
        headers = self.generate_req_headers(url)

        try:
            resp, info = fetch_url(self.module, method='GET', headers=headers, url=url)
            manifest_list = ET.fromstring(resp.read())
            manifests = []
            for manifest in manifest_list[0]:
                manifests.append(manifest.attrib)

            self.module.exit_json(changed=False, manifests=manifests)
        except Exception as e:
            self.module.fail_json(msg="Failed to fetch manifests from %s: %s" % (url, e))


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=True)
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_host_logbundle_info_mgr = VMwareHostLogbundleInfo(module)
    vmware_host_logbundle_info_mgr.get_listmanifests()


if __name__ == "__main__":
    main()
