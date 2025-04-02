#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Karsten Kaj Jakobsen <kj@patientsky.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
author:
  - "Karsten Kaj Jakobsen (@karstenjakobsen)"
description:
  - "This module can be used to gather information about DRS VM/HOST groups from the given cluster."
extends_documentation_fragment:
- community.vmware.vmware.documentation

module: vmware_drs_group_info
options:
  cluster_name:
    description:
      - "Cluster to search for VM/Host groups."
      - "If set, information of DRS groups belonging this cluster will be returned."
      - "Needed if O(datacenter) is not set."
      - "O(cluster_name) and O(datacenter) are mutually exclusive parameters."
    required: false
    type: str
  datacenter:
    aliases:
      - datacenter_name
    description:
      - "Datacenter to search for DRS VM/Host groups."
      - "Needed if O(cluster_name) is not set."
      - "O(cluster_name) and O(datacenter) are mutually exclusive parameters."
    required: false
    type: str
short_description: "Gathers info about DRS VM/Host groups on the given cluster"
'''

EXAMPLES = r'''
---
- name: "Gather DRS info about given Cluster"
  register: cluster_drs_group_info
  community.vmware.vmware_drs_group_info:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster_name: "{{ cluster_name }}"
  delegate_to: localhost

- name: "Gather DRS group info about all clusters in given datacenter"
  register: cluster_drs_group_info
  community.vmware.vmware_drs_group_info:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    datacenter: "{{ datacenter }}"
  delegate_to: localhost
'''

RETURN = r'''
drs_group_info:
    description: Metadata about DRS group from given cluster / datacenter
    returned: always
    type: dict
    sample:
        "drs_group_info": {
            "DC0_C0": [
                {
                    "group_name": "GROUP_HOST_S01",
                    "hosts": [
                        "vm-01.zone",
                        "vm-02.zone"
                    ],
                    "type": "host"
                },
                {
                    "group_name": "GROUP_HOST_S02",
                    "hosts": [
                        "vm-03.zone",
                        "vm-04.zone"
                    ],
                    "type": "host"
                },
                {
                    "group_name": "GROUP_VM_S01",
                    "type": "vm",
                    "vms": [
                        "test-node01"
                    ]
                },
                {
                    "group_name": "GROUP_VM_S02",
                    "type": "vm",
                    "vms": [
                        "test-node02"
                    ]
                }
            ],
            "DC0_C1": []
        }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, find_datacenter_by_name, get_all_objs
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VmwareDrsGroupInfoManager(PyVmomi):

    def __init__(self, module, datacenter_name, cluster_name=None):
        """
        Doctring: Init
        """

        super(VmwareDrsGroupInfoManager, self).__init__(module)

        self.__datacenter_name = datacenter_name
        self.__datacenter_obj = None
        self.__cluster_name = cluster_name
        self.__cluster_obj = None
        self.__result = dict()

        if self.__datacenter_name:

            self.__datacenter_obj = find_datacenter_by_name(self.content, datacenter_name=self.__datacenter_name)
            self.cluster_obj_list = []

            if self.__datacenter_obj:
                folder = self.__datacenter_obj.hostFolder
                self.cluster_obj_list = get_all_objs(self.content, [vim.ClusterComputeResource], folder)
            else:
                raise Exception("Datacenter '%s' not found" % self.__datacenter_name)

        if self.__cluster_name:

            self.__cluster_obj = self.find_cluster_by_name(cluster_name=self.__cluster_name)

            if self.__cluster_obj is None:
                raise Exception("Cluster '%s' not found" % self.__cluster_name)
            else:
                self.cluster_obj_list = [self.__cluster_obj]

    def get_result(self):
        """
        Docstring
        """
        return self.__result

    def __set_result(self, result):
        """
        Sets result
        Args:
            result: drs group result list

        Returns: None

        """
        self.__result = result

    def __get_all_from_group(self, group_obj, host_group=False):
        """
        Return all VM / Host names using given group
        Args:
            group_obj: Group object
            host_group: True if we want only host name from group

        Returns: List of VM / Host names belonging to given group object

        """
        obj_name_list = []

        if not all([group_obj]):
            return obj_name_list

        if not host_group and isinstance(group_obj, vim.cluster.VmGroup):
            obj_name_list = [vm.name for vm in group_obj.vm]
        elif host_group and isinstance(group_obj, vim.cluster.HostGroup):
            obj_name_list = [host.name for host in group_obj.host]

        return obj_name_list

    def __normalize_group_data(self, group_obj):
        """
        Return human readable group spec
        Args:
            group_obj: Group object

        Returns: Dictionary with DRS groups

        """
        if not all([group_obj]):
            return {}

        # Check if group is a host group
        if hasattr(group_obj, 'host'):
            return dict(
                group_name=group_obj.name,
                hosts=self.__get_all_from_group(group_obj=group_obj, host_group=True),
                type="host"
            )
        else:
            return dict(
                group_name=group_obj.name,
                vms=self.__get_all_from_group(group_obj=group_obj),
                type="vm"
            )

    def gather_info(self):
        """
        Gather DRS group information about given cluster
        Returns: Dictionary of clusters with DRS groups

        """
        cluster_group_info = dict()

        for cluster_obj in self.cluster_obj_list:

            cluster_group_info[cluster_obj.name] = []

            for drs_group in cluster_obj.configurationEx.group:
                cluster_group_info[cluster_obj.name].append(self.__normalize_group_data(drs_group))

        self.__set_result(cluster_group_info)


def main():

    argument_spec = base_argument_spec()

    argument_spec.update(
        datacenter=dict(type='str', required=False, aliases=['datacenter_name']),
        cluster_name=dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[['cluster_name', 'datacenter']],
        mutually_exclusive=[['cluster_name', 'datacenter']],
    )

    try:
        # Create instance of VmwareDrsGroupManager
        vmware_drs_group_info = VmwareDrsGroupInfoManager(
            module=module,
            datacenter_name=module.params.get('datacenter'),
            cluster_name=module.params.get('cluster_name', None))

        vmware_drs_group_info.gather_info()

        # Set results
        results = dict(failed=False,
                       drs_group_info=vmware_drs_group_info.get_result())

    except Exception as error:
        results = dict(failed=True, msg="Error: %s" % error)

    if results['failed']:
        module.fail_json(**results)
    else:
        module.exit_json(**results)


if __name__ == "__main__":
    main()
