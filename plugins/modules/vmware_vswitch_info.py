#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vswitch_info
short_description: Gathers info about an ESXi host's vswitch configurations
description:
- This module can be used to gather information about an ESXi host's vswitch configurations when ESXi hostname or Cluster name is given.
- The vSphere Client shows the value for the number of ports as elastic from vSphere 5.5 and above.
- Other tools like esxcli might show the number of ports as 1536 or 5632.
- See U(https://kb.vmware.com/s/article/2064511) for more details.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  policies:
    description:
    - Gather information about Security, Traffic Shaping, as well as Teaming and failover.
    - The property C(ts) stands for Traffic Shaping and C(lb) for Load Balancing.
    type: bool
    default: false
  cluster_name:
    description:
    - Name of the cluster.
    - Info about vswitch belonging to every ESXi host systems under this cluster will be returned.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname to gather information from.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
extends_documentation_fragment:
- vmware.vmware.base_options

'''

EXAMPLES = r'''
- name: Gather vswitch info about all ESXi Host in given Cluster
  community.vmware.vmware_vswitch_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
    delegate_to: localhost
  register: all_hosts_vswitch_info

- name: Gather vswitch info about ESXi Host
  community.vmware.vmware_vswitch_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    delegate_to: localhost
  register: all_vswitch_info
'''

RETURN = r'''
hosts_vswitch_info:
    description: metadata about host's vswitch configuration
    returned: on success
    type: dict
    sample: {
        "10.76.33.218": {
            "vSwitch0": {
                "mtu": 1500,
                "num_ports": 128,
                "pnics": [
                    "vmnic0"
                ],
                "failback": true,
                "failover_active": ["vmnic0"],
                "failover_standby": [],
                "failure_detection": "link_status_only",
                "lb": "loadbalance_srcid",
                "notify": true,
                "security": [false, false, false],
                "ts": false
            },
            "vSwitch_0011": {
                "mtu": 1500,
                "num_ports": 128,
                "pnics": [
                    "vmnic2",
                    "vmnic1"
                    ],
                "failback": true,
                "failover_active": ["vmnic1"],
                "failover_standby": ["vmnic2"],
                "failure_detection": "link_status_only",
                "lb": "loadbalance_srcid",
                "notify": true,
                "security": [false, false, false],
                "ts": false,
            },
        },
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class VswitchInfoManager(PyVmomi):
    """Class to gather vSwitch info"""

    def __init__(self, module):
        super(VswitchInfoManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system.")
        self.policies = self.params.get('policies')

    @staticmethod
    def serialize_pnics(vswitch_obj):
        """Get pnic names"""
        pnics = []
        for pnic in vswitch_obj.pnic:
            # vSwitch contains all PNICs as string in format of 'key-vim.host.PhysicalNic-vmnic0'
            pnics.append(pnic.split("-", 3)[-1])
        return pnics

    @staticmethod
    def normalize_vswitch_info(vswitch_obj, policy_info):
        """Create vSwitch information"""
        vswitch_info_dict = dict()
        spec = vswitch_obj.spec
        vswitch_info_dict['pnics'] = VswitchInfoManager.serialize_pnics(vswitch_obj)
        vswitch_info_dict['mtu'] = vswitch_obj.mtu
        vswitch_info_dict['num_ports'] = spec.numPorts

        if policy_info:
            # Security info
            if spec.policy.security:
                vswitch_info_dict['security'] = (
                    [
                        spec.policy.security.allowPromiscuous,
                        spec.policy.security.macChanges,
                        spec.policy.security.forgedTransmits
                    ]
                )

            # Traffic Shaping info
            if spec.policy.shapingPolicy:
                vswitch_info_dict['ts'] = spec.policy.shapingPolicy.enabled

            # Teaming and failover info
            if spec.policy.nicTeaming:
                vswitch_info_dict['lb'] = spec.policy.nicTeaming.policy
                vswitch_info_dict['notify'] = spec.policy.nicTeaming.notifySwitches
                vswitch_info_dict['failback'] = not spec.policy.nicTeaming.rollingOrder
                vswitch_info_dict['failover_active'] = spec.policy.nicTeaming.nicOrder.activeNic
                vswitch_info_dict['failover_standby'] = spec.policy.nicTeaming.nicOrder.standbyNic
                if spec.policy.nicTeaming.failureCriteria.checkBeacon:
                    vswitch_info_dict['failure_detection'] = "beacon_probing"
                else:
                    vswitch_info_dict['failure_detection'] = "link_status_only"

        return vswitch_info_dict

    def gather_vswitch_info(self):
        """Gather vSwitch info"""
        hosts_vswitch_info = dict()
        for host in self.hosts:
            network_manager = host.configManager.networkSystem
            if network_manager:
                temp_switch_dict = dict()
                for vswitch in network_manager.networkInfo.vswitch:
                    temp_switch_dict[vswitch.name] = self.normalize_vswitch_info(vswitch_obj=vswitch, policy_info=self.policies)
                hosts_vswitch_info[host.name] = temp_switch_dict
        return hosts_vswitch_info


def main():
    """Main"""
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str', required=False),
        esxi_hostname=dict(type='str', required=False),
        policies=dict(type='bool', required=False, default=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True
    )

    vmware_vswitch_mgr = VswitchInfoManager(module)
    module.exit_json(changed=False, hosts_vswitch_info=vmware_vswitch_mgr.gather_vswitch_info())


if __name__ == "__main__":
    main()
