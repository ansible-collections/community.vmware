#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_drs_rule_info
short_description: Gathers info about DRS rule on the given cluster
description:
- 'This module can be used to gather information about DRS VM-VM and VM-HOST rules from the given cluster.'
author:
- Abhijeet Kasurde (@Akasurde)
options:
  cluster_name:
    description:
    - Name of the cluster.
    - DRS information for the given cluster will be returned.
    - This is required parameter if O(datacenter) parameter is not provided.
    type: str
  datacenter:
    description:
    - Name of the datacenter.
    - DRS information for all the clusters from the given datacenter will be returned.
    - This is required parameter if O(cluster_name) parameter is not provided.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather DRS info about given Cluster
  community.vmware.vmware_drs_rule_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_drs_info

- name: Gather DRS info about all Clusters in given datacenter
  community.vmware.vmware_drs_rule_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: '{{ datacenter_name }}'
  delegate_to: localhost
  register: datacenter_drs_info
'''

RETURN = r'''
drs_rule_info:
    description: metadata about DRS rule from given cluster / datacenter
    returned: always
    type: dict
    sample: {
            "DC0_C0": [
                {
                    "rule_affinity": false,
                    "rule_enabled": true,
                    "rule_key": 1,
                    "rule_mandatory": true,
                    "rule_name": "drs_rule_0001",
                    "rule_type": "vm_vm_rule",
                    "rule_uuid": "52be5061-665a-68dc-3d25-85cd2d37e114",
                    "rule_vms": [
                        "VM_65",
                        "VM_146"
                    ]
                },
            ],
            "DC1_C1": [
                {
                    "rule_affine_host_group_name": "host_group_1",
                    "rule_affine_hosts": [
                        "10.76.33.204"
                    ],
                    "rule_anti_affine_host_group_name": null,
                    "rule_anti_affine_hosts": [],
                    "rule_enabled": true,
                    "rule_key": 1,
                    "rule_mandatory": false,
                    "rule_name": "vm_host_rule_0001",
                    "rule_type": "vm_host_rule",
                    "rule_uuid": "52687108-4d3a-76f2-d29c-b708c40dbe40",
                    "rule_vm_group_name": "test_vm_group_1",
                    "rule_vms": [
                        "VM_8916",
                        "VM_4010"
                    ]
                }
            ],
            }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, find_datacenter_by_name, get_all_objs
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VmwareDrsInfoManager(PyVmomi):
    def __init__(self, module):
        super(VmwareDrsInfoManager, self).__init__(module)

        datacenter_name = self.params.get('datacenter', None)
        if datacenter_name:
            datacenter_obj = find_datacenter_by_name(self.content, datacenter_name=datacenter_name)
            self.cluster_obj_list = []
            if datacenter_obj:
                folder = datacenter_obj.hostFolder
                self.cluster_obj_list = get_all_objs(self.content, [vim.ClusterComputeResource], folder)
            else:
                self.module.fail_json(changed=False, msg="Datacenter '%s' not found" % datacenter_name)

        cluster_name = self.params.get('cluster_name', None)
        if cluster_name:
            cluster_obj = self.find_cluster_by_name(cluster_name=cluster_name)
            if cluster_obj is None:
                self.module.fail_json(changed=False, msg="Cluster '%s' not found" % cluster_name)
            else:
                self.cluster_obj_list = [cluster_obj]

    def get_all_from_group(self, group_name=None, cluster_obj=None, hostgroup=False):
        """
        Return all VM / Host names using given group name
        Args:
            group_name: Rule name
            cluster_obj: Cluster managed object
            hostgroup: True if we want only host name from group

        Returns: List of VM / Host names belonging to given group object

        """
        obj_name_list = []
        if not all([group_name, cluster_obj]):
            return obj_name_list

        for group in cluster_obj.configurationEx.group:
            if group.name == group_name:
                if not hostgroup and isinstance(group, vim.cluster.VmGroup):
                    obj_name_list = [vm.name for vm in group.vm]
                    break
                if hostgroup and isinstance(group, vim.cluster.HostGroup):
                    obj_name_list = [host.name for host in group.host]
                    break

        return obj_name_list

    @staticmethod
    def normalize_vm_vm_rule_spec(rule_obj=None):
        """
        Return human readable rule spec
        Args:
            rule_obj: Rule managed object

        Returns: Dictionary with DRS VM VM Rule info

        """
        if rule_obj is None:
            return {}
        return dict(rule_key=rule_obj.key,
                    rule_enabled=rule_obj.enabled,
                    rule_name=rule_obj.name,
                    rule_mandatory=rule_obj.mandatory,
                    rule_uuid=rule_obj.ruleUuid,
                    rule_vms=[vm.name for vm in rule_obj.vm],
                    rule_type="vm_vm_rule",
                    rule_affinity=True if isinstance(rule_obj, vim.cluster.AffinityRuleSpec) else False,
                    )

    def normalize_vm_host_rule_spec(self, rule_obj=None, cluster_obj=None):
        """
        Return human readable rule spec
        Args:
            rule_obj: Rule managed object
            cluster_obj: Cluster managed object

        Returns: Dictionary with DRS VM HOST Rule info

        """
        if not all([rule_obj, cluster_obj]):
            return {}
        return dict(rule_key=rule_obj.key,
                    rule_enabled=rule_obj.enabled,
                    rule_name=rule_obj.name,
                    rule_mandatory=rule_obj.mandatory,
                    rule_uuid=rule_obj.ruleUuid,
                    rule_vm_group_name=rule_obj.vmGroupName,
                    rule_affine_host_group_name=rule_obj.affineHostGroupName,
                    rule_anti_affine_host_group_name=rule_obj.antiAffineHostGroupName,
                    rule_vms=self.get_all_from_group(group_name=rule_obj.vmGroupName,
                                                     cluster_obj=cluster_obj),
                    rule_affine_hosts=self.get_all_from_group(group_name=rule_obj.affineHostGroupName,
                                                              cluster_obj=cluster_obj,
                                                              hostgroup=True),
                    rule_anti_affine_hosts=self.get_all_from_group(group_name=rule_obj.antiAffineHostGroupName,
                                                                   cluster_obj=cluster_obj,
                                                                   hostgroup=True),
                    rule_type="vm_host_rule",
                    )

    def gather_drs_rule_info(self):
        """
        Gather DRS rule information about given cluster
        Returns: Dictionary of clusters with DRS information

        """
        cluster_rule_info = dict()
        for cluster_obj in self.cluster_obj_list:
            cluster_rule_info[cluster_obj.name] = []
            for drs_rule in cluster_obj.configuration.rule:
                if isinstance(drs_rule, vim.cluster.VmHostRuleInfo):
                    cluster_rule_info[cluster_obj.name].append(self.normalize_vm_host_rule_spec(
                        rule_obj=drs_rule,
                        cluster_obj=cluster_obj))
                else:
                    cluster_rule_info[cluster_obj.name].append(self.normalize_vm_vm_rule_spec(rule_obj=drs_rule))

        return cluster_rule_info


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str', required=False),
        cluster_name=dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'datacenter'],
        ],
        supports_check_mode=True,
    )

    vmware_drs_info = VmwareDrsInfoManager(module)
    module.exit_json(changed=False, drs_rule_info=vmware_drs_info.gather_drs_rule_info())


if __name__ == "__main__":
    main()
