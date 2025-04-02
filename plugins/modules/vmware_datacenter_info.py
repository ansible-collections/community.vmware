#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Abhijeet Kasurde <akasurde@redhat.com>
# Copyright: (c) 2020, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_datacenter_info
short_description: Gather information about VMware vSphere Datacenters
description:
    - This module can be used to gather information VMware vSphere Datacenters.
author:
- Abhijeet Kasurde (@Akasurde)
options:
    datacenter:
      description:
      - The name of the datacenter to gather information for.
      - If not provided, will gather information about all datacenters from the VMware infra.
      type: str
      aliases: ['datacenter_name']
    schema:
      description:
      - Specify the output schema desired.
      - The V(summary) output schema is the legacy output from the module.
      - The V(vsphere) output schema is the vSphere API class definition.
      choices: ['summary', 'vsphere']
      default: 'summary'
      type: str
    properties:
      description:
      - Specify the properties to retrieve.
      - If not specified, all properties are retrieved (deeply).
      - Results are returned in a structure identical to the vSphere API.
      - 'Example:'
      - '   properties: ['
      - '      "overallStatus"'
      - '   ]'
      - Only valid when O(schema=vsphere).
      type: list
      elements: str
    show_tag:
      description:
      - Tags related to Datacenter are shown if set to V(true).
      default: false
      type: bool
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Gather information about all datacenters
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: Gather information about a particular datacenter
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
  delegate_to: localhost

- name: Gather information about a particular datacenter
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
    show_tag: true
  delegate_to: localhost

- name: Gather vSphere schema information
  community.vmware.vmware_datacenter_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
    schema: vsphere
    properties:
    - configStatus
    - overallStatus
'''

RETURN = r'''
datacenter_info:
  description: Information about datacenter
  returned: always
  type: list
  sample:
    [
        {
            "configStatus": "gray",
            "moid": "datacenter-2",
            "name": "Asia-Datacenter1"
        }
    ]
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient


class VmwareDatacenterInfo(PyVmomi):
    def __init__(self, module):
        super(VmwareDatacenterInfo, self).__init__(module)
        if self.params.get('show_tag'):
            self.vmware_client = VmwareRestClient(self.module)

    def get_datacenter_info(self):
        self.datacenter_name = self.params.get('datacenter')
        results = dict(
            changed=False,
            datacenter_info=[],
        )

        datacenter_objs = self.get_managed_objects_properties(vim_type=vim.Datacenter, properties=['name'])
        dcs = []
        for dc_obj in datacenter_objs:
            if len(dc_obj.propSet) == 1:
                if self.datacenter_name is not None:
                    if dc_obj.propSet[0].val == to_native(self.datacenter_name):
                        dcs.append(dc_obj.obj)
                        continue
                else:
                    dcs.append(dc_obj.obj)

        for obj in dcs:
            if obj is None:
                continue
            temp_dc = dict(
                name=obj.name,
                moid=obj._moId,
            )
            if self.module.params['schema'] == 'summary':
                temp_dc.update(
                    dict(
                        config_status=obj.configStatus,
                        overall_status=obj.overallStatus,
                    )
                )
            else:
                temp_dc.update(self.to_json(obj, self.params.get('properties')))
            if self.params.get('show_tag'):
                temp_dc.update({
                    'tags': self.vmware_client.get_tags_for_datacenter(datacenter_mid=obj._moId)
                })

            results['datacenter_info'].append(temp_dc)
        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        dict(
            datacenter=dict(type='str', aliases=['datacenter_name']),
            schema=dict(type='str', choices=['summary', 'vsphere'], default='summary'),
            properties=dict(type='list', elements='str'),
            show_tag=dict(type='bool', default=False),
        )
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    vmware_datacenter_mgr = VmwareDatacenterInfo(module)
    vmware_datacenter_mgr.get_datacenter_info()


if __name__ == '__main__':
    main()
