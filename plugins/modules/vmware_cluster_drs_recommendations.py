#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_cluster_drs_recommendations
version_added: '3.7.0'
short_description: Apply DRS Recommendations
description:
    - Apply DRS Recommendations for Cluster.
author:
- Nina Loser (@Nina2244)
deprecated:
  removed_in: 6.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.cluster_drs_recommendations) instead.
options:
    cluster_name:
      description:
      - The name of the cluster to be managed.
      type: str
      required: true
    datacenter:
      description:
      - The name of the datacenter.
      type: str
      required: true
      aliases: [ datacenter_name ]
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Apply DRS Recommendations for Cluster
  community.vmware.vmware_cluster:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
  delegate_to: localhost
'''

RETURN = r'''
result:
    description:
        - list of the recommendations
        - What server moved from which host to which host.
    returned: always
    type: list
    sample: ["server1 move from host1 to host2.", "server2 move from host1 to host2."]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    find_datacenter_by_name,
    wait_for_task)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VMwareCluster(PyVmomi):
    def __init__(self, module):
        super(VMwareCluster, self).__init__(module)
        self.cluster_name = module.params['cluster_name']
        self.datacenter_name = module.params['datacenter']
        self.datacenter = None
        self.cluster = None

        self.datacenter = find_datacenter_by_name(self.content, self.datacenter_name)
        if self.datacenter is None:
            self.module.fail_json(msg="Datacenter %s does not exist." % self.datacenter_name)

        self.cluster = self.find_cluster_by_name(cluster_name=self.cluster_name, datacenter_name=self.datacenter)
        if self.cluster is None:
            self.module.fail_json(msg="Cluster %s does not exist." % self.cluster_name)

    def recommendations(self):
        results = []
        changed = False
        self.cluster.RefreshRecommendation()
        if len(self.cluster.recommendation) == 0:
            self.module.exit_json(changed=changed, result="No recommendations.")
        else:
            for index, recommendation in enumerate(self.cluster.recommendation):
                results.append("%s move from %s to %s." % (recommendation.action[0].target.name,
                                                           recommendation.action[0].drsMigration.source.name,
                                                           recommendation.action[0].drsMigration.destination.name))
                if not self.module.check_mode:
                    task = self.cluster.ApplyRecommendation(recommendation.key)
                    changed = True
                    if index == len(self.cluster.recommendation) - 1 and hasattr(task, 'info'):
                        wait_for_task(task)
            self.module.exit_json(changed=changed, result=results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        cluster_name=dict(type='str', required=True),
        datacenter=dict(type='str', required=True, aliases=['datacenter_name']),
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    vmware_cluster = VMwareCluster(module)
    vmware_cluster.recommendations()


if __name__ == '__main__':
    main()
