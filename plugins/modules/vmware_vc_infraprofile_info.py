#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019-2020, Ansible Project
# Copyright: (c) 2019-2020, Naveenkumar G P <ngp@vmware.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vc_infraprofile_info
short_description: List and Export VMware vCenter infra profile configs.
description:
- Module to manage VMware vCenter infra profile configs.
- vCenter infra profile Library feature is introduced in vSphere 7.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.
author:
- Naveenkumar G P (@ngp)
requirements:
- vSphere Automation SDK
options:
    decryption_key:
      description:
      - decryption_key argument for while doing import profile task as of now its not taken into account form API team.
      type: str
      required: false
    encryption_key:
      description:
      - encryption_key argument for while doing import profile task as of now its not taken into account form API team.
      type: str
      required: false
    api:
      description:
      - API which needs to be executed
      type: str
      required: false
      choices: [ export, import, list, validate ]
    config_path:
      description:
      - Config file path which contains infra profile config JSON data, supports both relative and absolute path.
      - This parameter is required only when C(import),C(validate) APIs are being used.
      type: str
      required: false
    profiles:
      description:
      - A list of profile names to be exported, imported, and validated.
      - This parameter is not required while running for List API, not for C(export),C(import) and C(validate).
      type: str
      required: false
    description:
      description:
      - Description of about encryption or decryption key.
      type: str
      required: false
extends_documentation_fragment:
- community.vmware.vmware_rest_client.documentation
'''

EXAMPLES = r'''
- name: Get information about VC infraprofile
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: export vCenter appliance infra profile config
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    api: "export"
    profiles: "ApplianceManagement"
  delegate_to: localhost

- name: validate vCenter appliance infra profile config
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    api: "validate"
    profiles: "ApplianceManagement"
    config_path: "export.json"

- name: import vCenter appliance infra profile config
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    api: "import"
    profiles: "ApplianceManagement"
    config_path: "import.json"
  delegate_to: localhost
  '''

RETURN = r'''
list_infra:
    description: A list of infra configs,
    returned: on success with API as "list"
    type: list
    "sample": [
        {
            "info": "ApplianceManagement",
            "name": "ApplianceManagement"
        },
        {
            "info": "ApplianceNetwork",
            "name": "ApplianceNetwork"
        },
        {
            "info": "Authentication & Authorization Management",
            "name": "AuthManagement"
        }
    ]

export_infra:
    description: A message about the exported file
    returned: On success with API set as "export"
    type: dict
    sample: {
        "export_config_json":"json exported to file"
    }

validate_infra:
    description: A message about validate on exported file
    returned: On success with API set as "validate"
    type: dict
    "sample": {
        "changed": false,
        "failed": false,
        "status": "VALID"
    }

import_profile:
    description: A message about import on import_profile spec
    returned: On success with API set as "import"
    type: dict
    "sample": {
        "changed": true,
        "failed": false,
        "status": "0.0"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.version import LooseVersion
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
import json
import time


class VcVersionChecker(PyVmomi):
    def __init__(self, module):
        super(VcVersionChecker, self).__init__(module)

    def check_vc_version(self):
        if LooseVersion(self.content.about.version) < LooseVersion('7'):
            self.module.fail_json(msg="vCenter version is less than 7.0.0 Please specify vCenter with version greater than or equal to 7.0.0")


class VcenterProfile(VmwareRestClient):

    def __init__(self, module):
        super(VcenterProfile, self).__init__(module)
        self.config_path = self.params['config_path']

    def list_vc_infraprofile_configs(self):
        profile_configs_list = self.api_client.appliance.infraprofile.Configs.list()
        config_list = []
        for x in profile_configs_list:
            config_list.append({'info': x.info, 'name': x.name})
        self.module.exit_json(changed=False, infra_configs_list=config_list)

    def get_profile_spec(self):
        infra = self.api_client.appliance.infraprofile.Configs
        profiles = {}
        profiles = self.params['profiles'].split(",")
        profile_spec = infra.ProfilesSpec(encryption_key="encryption_key", description="description", profiles=set(profiles))
        return profile_spec

    def vc_export_profile_task(self):
        profile_spec = self.get_profile_spec()
        infra = self.api_client.appliance.infraprofile.Configs
        config_json = infra.export(spec=profile_spec)
        if self.config_path is None:
            self.config_path = self.params.get('api') + ".json"
        parsed = json.loads(config_json)
        with open(self.config_path, 'w', encoding='utf-8') as outfile:
            json.dump(parsed, outfile, ensure_ascii=False, indent=2)
        self.module.exit_json(changed=False, export_config_json=config_json)

    def read_profile(self):
        with open(self.config_path, "r") as file:
            return file.read()

    def get_import_profile_spec(self):
        infra = self.api_client.appliance.infraprofile.Configs
        config_spec = self.read_profile()
        profile_spec = self.get_profile_spec()
        import_profile_spec = infra.ImportProfileSpec(config_spec=config_spec, profile_spec=profile_spec)
        return import_profile_spec

    def vc_import_profile_task(self):
        infra = self.api_client.appliance.infraprofile.Configs
        import_profile_spec = self.get_import_profile_spec()
        import_task = infra.import_profile_task(import_profile_spec)
        self.wait_for_task(import_task)
        if "SUCCEEDED" == import_task.get_info().status:
            self.module.exit_json(changed=True, status=import_task.get_info().result.value)
        self.module.fail_json(msg='Failed to import profile status:"%s" ' % import_task.get_info().status)

    def vc_validate_profile_task(self):
        infra = self.api_client.appliance.infraprofile.Configs
        import_profile_spec = self.get_import_profile_spec()
        validate_task = infra.validate_task(import_profile_spec)
        if "VALID" == validate_task.get_info().result.get_field("status").value:
            self.module.exit_json(changed=False, status=validate_task.get_info().result.get_field("status").value)
        elif "INVALID" == validate_task.get_info().result.get_field("status").value:
            # TO-DO: move to vmware_rest_client
            self.module.exit_json(changed=False, status=validate_task.get_info().result.get_field("status").value)
        else:
            # TO-DO: move to vmware_rest_client
            self.module.fail_json(msg='Failed to validate profile status:"%s" ' % dir(validate_task.get_info().status))

    def wait_for_task(self, task, poll_interval=1):
        while task.get_info().status == "RUNNING":
            time.sleep(poll_interval)


def main():
    argument_spec = VmwareRestClient.vmware_client_argument_spec()
    argument_spec.update(
        encryption_key=dict(type='str', required=False, no_log=True),
        description=dict(type='str', required=False),
        decryption_key=dict(type='str', required=False, no_log=True),
        api=dict(type='str', required=False, choices=['list', 'export', 'import', 'validate']),
        profiles=dict(type='str', required=False),
        config_path=dict(type='str', required=False),
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    result = {'failed': False, 'changed': False}
    vmware_vc_infra_profile = VcenterProfile(module)
    vmware_vc_version = VcVersionChecker(module)
    vmware_vc_version.check_vc_version()

    if module.params['api'].lower() == "list":
        if module.check_mode:
            result.update(
                changed=False, desired_operation='list_vc_profile_configs',)
            module.exit_json(**result)
        vmware_vc_infra_profile.list_vc_infraprofile_configs()
    if module.params['api'].lower() == "export":
        if module.check_mode:
            result.update(
                changed=False,
                desired_operation='export_vc_profile_configs',)
            module.exit_json(**result)
        vmware_vc_infra_profile.vc_export_profile_task()

    if module.params['api'].lower() == "import":
        if module.check_mode:
            result.update(
                changed=True,
                desired_operation='import_vc_profile_configs',
            )
            module.exit_json(**result)
        vmware_vc_infra_profile.vc_import_profile_task()

    if module.params['api'].lower() == "validate":
        if module.check_mode:
            result.update(
                changed=True,
                desired_operation='import_vc_profile_configs',
            )
            module.exit_json(**result)
        vmware_vc_infra_profile.vc_validate_profile_task()


if __name__ == '__main__':
    main()
