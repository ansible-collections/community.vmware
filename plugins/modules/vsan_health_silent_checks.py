#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Hewlett Packard Enterprise Development LP
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later


from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vsan_health_silent_checks
version_added: '3.6.0'
short_description: Silence vSAN health checks
description:
  - Take a list of vSAN health checks and silence them
  - Re-enable alerts for previously silenced health checks
author:
  - Philipp Fruck (@p-fruck)
requirements:
  - vSAN Management SDK, which needs to be downloaded from VMware and installed manually.
options:
  cluster_name:
    description:
      - Name of the vSAN cluster.
    type: str
    required: true
  checks:
    description:
      - The checks to silence.
    type: list
    elements: str
    required: false
  state:
    description:
      - The state of the health checks.
      - If set to C(present), all given health checks will be silenced.
      - If set to C(absent), all given health checks will be removed from the list of silent checks.
    default: 'present'
    choices: [ 'present', 'absent' ]
    type: str
extends_documentation_fragment:
  - community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Disable the vSAN Support Insight health check
  community.vmware.vsan_health_silent_checks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    checks: vsanenablesupportinsight
    cluster_name: 'vSAN01'
  delegate_to: localhost

- name: Re-enable health check alerts for release catalog and HCL DB
  community.vmware.vsan_health_silent_checks:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    checks:
      - releasecataloguptodate
      - autohclupdate
    state: absent
    cluster_name: 'vSAN01'
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
        self.vsanClusterHealthSystem = vcMos['vsan-cluster-health-system']

        self.cluster = None

    def silence_checks(self):
        cluster_name = self.params.get('cluster_name')
        if cluster_name:
            self.cluster = self.find_cluster_by_name(cluster_name=cluster_name)
            if self.cluster is None:
                self.module.fail_json(msg="Cluster %s does not exist." % cluster_name)

        kwargs = {'cluster': self.cluster}
        checks = self.params.get('checks')
        state = self.params.get('state')
        if state == 'present':
            kwargs['addSilentChecks'] = checks
        else:
            kwargs['removeSilentChecks'] = checks

        success = self.vsanClusterHealthSystem.VsanHealthSetVsanClusterSilentChecks(**kwargs)
        self.module.exit_json(changed=success)


def main():
    argument_spec = vmware_argument_spec()

    argument_spec.update(dict(
        checks=dict(type='list', elements='str', required=False),
        cluster_name=dict(type='str', required=True),
        state=dict(type='str', choices=['present', 'absent'], default='present'),
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
    )

    api = VsanApi(module)
    try:
        api.silence_checks()
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
