#!/usr/bin/python

# Copyright: (c) 2019, OVH SAS
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vsan_health_info
short_description: Gather information about a VMware vSAN cluster's health
description:
    - "Gather information about a VMware vSAN cluster's health."
options:
    datacenter:
        description:
            - Name of the Datacenter.
        required: false
        type: str
        aliases: [ 'datacenter_name' ]
    cluster_name:
        description:
            - Name of the vSAN cluster.
        required: true
        type: str
    fetch_from_cache:
        description:
            - V(true) to return the result from cache directly instead of running the full health check.
        required: false
        default: false
        type: bool
requirements:
    - VMware vSAN Python's SDK
extends_documentation_fragment:
- vmware.vmware.base_options
author:
    - Erwan Quelin (@equelin)
'''

EXAMPLES = r'''
- name: Gather health info from a vSAN's cluster
  community.vmware.vmware_vsan_health_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: 'vSAN01'
    fetch_from_cache: false

- name: Gather health info from a vSAN's cluster with datacenter
  community.vmware.vmware_vsan_health_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: 'vSAN01'
    datacenter: 'Datacenter_01'
    fetch_from_cache: true
'''

RETURN = r'''
vsan_health_info:
    description: vSAN cluster health info
    returned: on success
    type: dict
    sample: {
        "_vimtype": "vim.cluster.VsanClusterHealthSummary",
        "burnInTest": null,
        "clusterStatus": {
            "_vimtype": "vim.cluster.VsanClusterHealthSystemStatusResult",
            "goalState": "installed",
            "status": "green",
            "trackedHostsStatus": [
                {
                    "_vimtype": "vim.host.VsanHostHealthSystemStatusResult",
                    "hostname": "esxi01.example.com",
                    "issues": [],
                    "status": "green"
                },
                {
                    "_vimtype": "vim.host.VsanHostHealthSystemStatusResult",
                    "hostname": "esxi04.example.com",
                    "issues": [],
                    "status": "green"
                },
                {
                    "_vimtype": "vim.host.VsanHostHealthSystemStatusResult",
                    "hostname": "esxi02.example.com",
                    "issues": [],
                    "status": "green"
                },
                {
                    "_vimtype": "vim.host.VsanHostHealthSystemStatusResult",
                    "hostname": "esxi03.example.com",
                    "issues": [],
                    "status": "green"
                }
            ],
            "untrackedHosts": []
        }
    }
'''

import json
import traceback

try:
    from pyVmomi import vmodl, VmomiJSONEncoder
except ImportError:
    pass

VSANPYTHONSDK_IMP_ERR = None
try:
    import vsanapiutils
    HAS_VSANPYTHONSDK = True
except ImportError:
    VSANPYTHONSDK_IMP_ERR = traceback.format_exc()
    HAS_VSANPYTHONSDK = False

from ansible.module_utils.basic import AnsibleModule, missing_required_lib
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class VSANInfoManager(PyVmomi):
    def __init__(self, module):
        super(VSANInfoManager, self).__init__(module)
        self.datacenter = None
        self.cluster = None

    def gather_info(self):
        datacenter_name = self.module.params.get('datacenter')
        if datacenter_name:
            self.datacenter = self.find_datacenter_by_name(datacenter_name)
            if self.datacenter is None:
                self.module.fail_json(msg="Datacenter %s does not exist." % datacenter_name)

        cluster_name = self.module.params.get('cluster_name')
        self.cluster = self.find_cluster_by_name(cluster_name=cluster_name, datacenter_name=self.datacenter)
        if self.cluster is None:
            self.module.fail_json(msg="Cluster %s does not exist." % cluster_name)

        fetch_from_cache = self.module.params.get('fetch_from_cache')

        client_stub = self.si._GetStub()
        ssl_context = client_stub.schemeArgs.get('context')

        api_version = vsanapiutils.GetLatestVmodlVersion(self.module.params['hostname'])
        vc_mos = vsanapiutils.GetVsanVcMos(client_stub, context=ssl_context, version=api_version)

        vsan_cluster_health_system = vc_mos['vsan-cluster-health-system']

        cluster_health = {}
        try:
            cluster_health = vsan_cluster_health_system.VsanQueryVcClusterHealthSummary(
                cluster=self.cluster,
                fetchFromCache=fetch_from_cache,
            )
        except vmodl.fault.NotFound as not_found:
            self.module.fail_json(msg=not_found.msg)
        except vmodl.fault.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=runtime_fault.msg)

        health = json.dumps(cluster_health, cls=VmomiJSONEncoder.VmomiJSONEncoder, sort_keys=True, strip_dynamic=True)

        self.module.exit_json(changed=False, vsan_health_info=json.loads(health))


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(required=False, type='str', aliases=['datacenter_name']),
        cluster_name=dict(required=True, type='str'),
        fetch_from_cache=dict(required=False, type='bool', default=False)
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    if not HAS_VSANPYTHONSDK:
        module.fail_json(msg=missing_required_lib('vSAN Management SDK for Python'), exception=VSANPYTHONSDK_IMP_ERR)

    vsan_info_manager = VSANInfoManager(module)
    vsan_info_manager.gather_info()


if __name__ == '__main__':
    main()
