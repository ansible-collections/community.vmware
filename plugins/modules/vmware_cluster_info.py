#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_cluster_info
deprecated:
  removed_in: 7.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.cluster_info) instead.
short_description: Gather info about clusters available in given vCenter
description:
    - This module can be used to gather information about clusters in VMWare infrastructure.
author:
    - Abhijeet Kasurde (@Akasurde)
    - Christian Neugum (@digifuchsi)
options:
   datacenter:
     description:
     - Datacenter to search for cluster/s.
     - This parameter is required, if O(cluster_name) is not supplied.
     required: false
     type: str
   cluster_name:
     description:
     - Name of the cluster.
     - If set, information of this cluster will be returned.
     - This parameter is required, if O(datacenter) is not supplied.
     required: false
     type: str
   show_tag:
    description:
    - Tags related to cluster are shown if set to V(true).
    default: false
    type: bool
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
       - 'Example:'
       - '   properties: ['
       - '      "name",'
       - '      "configuration.dasConfig.enabled",'
       - '      "summary.totalCpu"'
       - '   ]'
       - Only valid when O(schema=vsphere).
     type: list
     elements: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather cluster info from given datacenter
  community.vmware.vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: ha-datacenter
  delegate_to: localhost
  register: cluster_info

- name: Gather info from datacenter about specific cluster
  community.vmware.vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: DC0_C0
  delegate_to: localhost
  register: cluster_info

- name: Gather info from datacenter about specific cluster with tags
  community.vmware.vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: DC0_C0
    show_tag: true
  delegate_to: localhost
  register: cluster_info

- name: Gather some info from a cluster using the vSphere API output schema
  vmware_cluster_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: DC0_C0
    schema: vsphere
    properties:
      - name
      - configuration.dasConfig.enabled
      - summary.totalCpu
  delegate_to: localhost
  register: cluster_info
'''

RETURN = r'''
clusters:
    description:
      - metadata about the available clusters
    returned: always
    type: dict
    sample: {
        "DC0_C0": {
            "datacenter": "DC0",
            "moid": "domain-c9",
            "drs_default_vm_behavior": null,
            "drs_enable_vm_behavior_overrides": null,
            "drs_vmotion_rate": null,
            "enable_ha": null,
            "enabled_drs": true,
            "enabled_vsan": false,
            "ha_admission_control_enabled": null,
            "ha_failover_level": null,
            "ha_host_monitoring": null,
            "ha_restart_priority": null,
            "ha_vm_failure_interval": null,
            "ha_vm_max_failure_window": null,
            "ha_vm_max_failures": null,
            "ha_vm_min_up_time": null,
            "ha_vm_monitoring": null,
            "ha_vm_tools_monitoring": null,
            "vsan_auto_claim_storage": false,
            "hosts": [
                {
                    "name": "esxi01.vsphere.local",
                    "folder": "/DC0/host/DC0_C0",
                },
                {
                    "name": "esxi02.vsphere.local",
                    "folder": "/DC0/host/DC0_C0",
                },
                {
                    "name": "esxi03.vsphere.local",
                    "folder": "/DC0/host/DC0_C0",
                },
                {
                    "name": "esxi04.vsphere.local",
                    "folder": "/DC0/host/DC0_C0",
                },
            ],
            "resource_summary": {
                "cpuCapacityMHz": 4224,
                "cpuUsedMHz": 87,
                "memCapacityMB": 6139,
                "memUsedMB": 1254,
                "pMemAvailableMB": 0,
                "pMemCapacityMB": 0,
                "storageCapacityMB": 33280,
                "storageUsedMB": 19953
            },
            "tags": [
                {
                    "category_id": "urn:vmomi:InventoryServiceCategory:9fbf83de-7903-442e-8004-70fd3940297c:GLOBAL",
                    "category_name": "sample_cluster_cat_0001",
                    "description": "",
                    "id": "urn:vmomi:InventoryServiceTag:93d680db-b3a6-4834-85ad-3e9516e8fee8:GLOBAL",
                    "name": "sample_cluster_tag_0001"
                }
            ],
        },
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six.moves.urllib.parse import unquote
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, find_datacenter_by_name, find_cluster_by_name, get_parent_datacenter
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient


class VmwreClusterInfoManager(PyVmomi):
    def __init__(self, module):
        super(VmwreClusterInfoManager, self).__init__(module)
        datacenter = self.params.get('datacenter')
        cluster_name = self.params.get('cluster_name')
        self.schema = self.params.get('schema')
        self.properties = self.params.get('properties')
        self.cluster_objs = []
        if datacenter:
            datacenter_obj = find_datacenter_by_name(self.content, datacenter_name=datacenter)
            if datacenter_obj is None:
                self.module.fail_json(msg="Failed to find datacenter '%s'" % datacenter)
            self.cluster_objs = self.get_all_cluster_objs(parent=datacenter_obj)
        elif cluster_name:
            cluster_obj = find_cluster_by_name(self.content, cluster_name=cluster_name)
            if cluster_obj is None:
                self.module.fail_json(msg="Failed to find cluster '%s'" % cluster_name)

            self.cluster_objs = [cluster_obj]

    def get_all_cluster_objs(self, parent):
        """
        Get all cluster managed objects from given parent object
        Args:
            parent: Managed objected of datacenter or host folder

        Returns: List of host managed objects

        """
        cluster_objs = []
        if isinstance(parent, vim.Datacenter):
            folder = parent.hostFolder
        else:
            folder = parent

        for child in folder.childEntity:
            if isinstance(child, vim.Folder):
                cluster_objs = cluster_objs + self.get_all_cluster_objs(child)
            if isinstance(child, vim.ClusterComputeResource):
                cluster_objs.append(child)
        return cluster_objs

    def gather_cluster_info(self):
        """
        Gather information about cluster
        """
        results = dict(changed=False, clusters=dict())

        if self.schema == 'summary':
            for cluster in self.cluster_objs:
                # Default values
                ha_failover_level = None
                ha_restart_priority = None
                ha_vm_tools_monitoring = None
                ha_vm_min_up_time = None
                ha_vm_max_failures = None
                ha_vm_max_failure_window = None
                ha_vm_failure_interval = None
                enabled_vsan = False
                vsan_auto_claim_storage = False
                hosts = []

                # Hosts
                for host in cluster.host:
                    hosts.append({
                        'name': host.name,
                        'folder': self.get_vm_path(self.content, host),
                    })

                # HA
                das_config = cluster.configurationEx.dasConfig
                if das_config.admissionControlPolicy:
                    ha_failover_level = das_config.admissionControlPolicy.failoverLevel
                if das_config.defaultVmSettings:
                    ha_restart_priority = das_config.defaultVmSettings.restartPriority
                    ha_vm_tools_monitoring = das_config.defaultVmSettings.vmToolsMonitoringSettings.vmMonitoring
                    ha_vm_min_up_time = das_config.defaultVmSettings.vmToolsMonitoringSettings.minUpTime
                    ha_vm_max_failures = das_config.defaultVmSettings.vmToolsMonitoringSettings.maxFailures
                    ha_vm_max_failure_window = das_config.defaultVmSettings.vmToolsMonitoringSettings.maxFailureWindow
                    ha_vm_failure_interval = das_config.defaultVmSettings.vmToolsMonitoringSettings.failureInterval

                # DRS
                drs_config = cluster.configurationEx.drsConfig

                # VSAN
                if hasattr(cluster.configurationEx, 'vsanConfigInfo'):
                    vsan_config = cluster.configurationEx.vsanConfigInfo
                    enabled_vsan = vsan_config.enabled
                    vsan_auto_claim_storage = vsan_config.defaultConfig.autoClaimStorage

                tag_info = []
                if self.params.get('show_tag'):
                    vmware_client = VmwareRestClient(self.module)
                    tag_info = vmware_client.get_tags_for_cluster(cluster_mid=cluster._moId)

                resource_summary = self.to_json(cluster.GetResourceUsage())
                if '_vimtype' in resource_summary:
                    del resource_summary['_vimtype']

                results['clusters'][unquote(cluster.name)] = dict(
                    hosts=hosts,
                    enable_ha=das_config.enabled,
                    ha_failover_level=ha_failover_level,
                    ha_vm_monitoring=das_config.vmMonitoring,
                    ha_host_monitoring=das_config.hostMonitoring,
                    ha_admission_control_enabled=das_config.admissionControlEnabled,
                    ha_restart_priority=ha_restart_priority,
                    ha_vm_tools_monitoring=ha_vm_tools_monitoring,
                    ha_vm_min_up_time=ha_vm_min_up_time,
                    ha_vm_max_failures=ha_vm_max_failures,
                    ha_vm_max_failure_window=ha_vm_max_failure_window,
                    ha_vm_failure_interval=ha_vm_failure_interval,
                    enabled_drs=drs_config.enabled,
                    drs_enable_vm_behavior_overrides=drs_config.enableVmBehaviorOverrides,
                    drs_default_vm_behavior=drs_config.defaultVmBehavior,
                    drs_vmotion_rate=drs_config.vmotionRate,
                    enabled_vsan=enabled_vsan,
                    vsan_auto_claim_storage=vsan_auto_claim_storage,
                    tags=tag_info,
                    resource_summary=resource_summary,
                    moid=cluster._moId,
                    datacenter=get_parent_datacenter(cluster).name
                )
        else:
            for cluster in self.cluster_objs:
                results['clusters'][unquote(cluster.name)] = self.to_json(cluster, self.properties)

        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str'),
        cluster_name=dict(type='str'),
        show_tag=dict(type='bool', default=False),
        schema=dict(type='str', choices=['summary', 'vsphere'], default='summary'),
        properties=dict(type='list', elements='str')
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'datacenter'],
        ],
        supports_check_mode=True,
    )

    pyv = VmwreClusterInfoManager(module)
    pyv.gather_cluster_info()


if __name__ == '__main__':
    main()
