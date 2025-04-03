#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later


from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_dvs_portgroup_info
short_description: Gathers info DVS portgroup configurations
description:
- This module can be used to gather information about DVS portgroup configurations.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  datacenter:
    description:
    - Name of the datacenter.
    required: true
    type: str
  dvswitch:
    description:
    - Name of a dvswitch to look for.
    required: false
    type: str
  show_mac_learning:
    description:
    - Show or hide MAC learning information of the DVS portgroup.
    type: bool
    default: true
  show_network_policy:
    description:
    - Show or hide network policies of DVS portgroup.
    type: bool
    default: true
  show_port_policy:
    description:
    - Show or hide port policies of DVS portgroup.
    type: bool
    default: true
  show_teaming_policy:
    description:
    - Show or hide teaming policies of DVS portgroup.
    type: bool
    default: true
  show_uplinks:
    description:
    - Show or hide uplinks of DVS portgroup.
    type: bool
    default: true
  show_vlan_info:
    description:
    - Show or hide vlan information of the DVS portgroup.
    type: bool
    default: false
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Get info about DVPG
  community.vmware.vmware_dvs_portgroup_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter: "{{ datacenter_name }}"
  register: dvpg_info

- name: Get number of ports for portgroup 'dvpg_001' in 'dvs_001'
  debug:
    msg: "{{ item.num_ports }}"
  with_items:
    - "{{ dvpg_info.dvs_portgroup_info['dvs_001'] | json_query(query) }}"
  vars:
    query: "[?portgroup_name=='dvpg_001']"
'''

RETURN = r'''
dvs_portgroup_info:
    description: metadata about DVS portgroup configuration
    returned: on success
    type: dict
    sample: {
        "dvs_0":[
            {
                "active_uplinks": [
                    "uplink 1"
                ],
                "description": null,
                "dvswitch_name": "dvs_001",
                "key": "dvportgroup-1014",
                "mac_learning": {
                    "allow_unicast_flooding": null,
                    "enabled": false,
                    "limit": null,
                    "limit_policy": null
                },
                "moid": "dvportgroup-1014",
                "network_policy": {
                    "forged_transmits": false,
                    "mac_changes": false,
                    "promiscuous": false
                },
                "num_ports": 8,
                "port_allocation": "elastic",
                "port_binding": "static",
                "standby_uplinks": [],
                "port_policy": {
                    "block_override": true,
                    "ipfix_override": false,
                    "live_port_move": false,
                    "network_rp_override": false,
                    "port_config_reset_at_disconnect": true,
                    "shaping_override": false,
                    "traffic_filter_override": false,
                    "uplink_teaming_override": false,
                    "vendor_config_override": false,
                    "vlan_override": false
                },
                "portgroup_name": "dvpg_001",
                "teaming_policy": {
                    "inbound_policy": true,
                    "notify_switches": true,
                    "policy": "loadbalance_srcid",
                    "rolling_order": false
                },
                "vlan_info": {
                    "trunk": false,
                    "pvlan": false,
                    "vlan_id": 0
                },
                "type": "earlyBinding"
            },
        ]
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    get_all_objs,
    find_dvs_by_name)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils.six.moves.urllib.parse import unquote


class DVSPortgroupInfoManager(PyVmomi):
    def __init__(self, module):
        super(DVSPortgroupInfoManager, self).__init__(module)
        self.dc_name = self.params['datacenter']
        self.dvs_name = self.params['dvswitch']

        datacenter = self.find_datacenter_by_name(self.dc_name)
        if datacenter is None:
            self.module.fail_json(msg="Failed to find the datacenter %s" % self.dc_name)
        if self.dvs_name:
            # User specified specific dvswitch name to gather information
            dvsn = find_dvs_by_name(self.content, self.dvs_name)
            if dvsn is None:
                self.module.fail_json(msg="Failed to find the dvswitch %s" % self.dvs_name)

            self.dvsls = [dvsn]
        else:
            # default behaviour, gather information about all dvswitches
            self.dvsls = get_all_objs(self.content, [vim.DistributedVirtualSwitch], folder=datacenter.networkFolder)

    def get_vlan_info(self, vlan_obj=None):
        """
        Return vlan information from given object
        Args:
            vlan_obj: vlan managed object
        Returns: Dict of vlan details of the specific object
        """

        vdret = dict()
        if not vlan_obj:
            return vdret

        if isinstance(vlan_obj, vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec):
            vlan_id_list = []
            for vli in vlan_obj.vlanId:
                if vli.start == vli.end:
                    vlan_id_list.append(str(vli.start))
                else:
                    vlan_id_list.append(str(vli.start) + "-" + str(vli.end))
            vdret = dict(trunk=True, pvlan=False, vlan_id=vlan_id_list)
        elif isinstance(vlan_obj, vim.dvs.VmwareDistributedVirtualSwitch.PvlanSpec):
            vdret = dict(trunk=False, pvlan=True, vlan_id=str(vlan_obj.pvlanId))
        else:
            vdret = dict(trunk=False, pvlan=False, vlan_id=str(vlan_obj.vlanId))

        return vdret

    def gather_dvs_portgroup_info(self):
        dvs_lists = self.dvsls
        result = dict()
        for dvs in dvs_lists:
            result[dvs.name] = list()
            for dvs_pg in dvs.portgroup:
                mac_learning = dict()
                network_policy = dict()
                teaming_policy = dict()
                port_policy = dict()
                vlan_info = dict()
                active_uplinks = list()
                standby_uplinks = list()

                if dvs_pg.config.type == 'ephemeral':
                    port_binding = 'ephemeral'
                else:
                    port_binding = 'static'

                if dvs_pg.config.autoExpand is True:
                    port_allocation = 'elastic'
                else:
                    port_allocation = 'fixed'

                if self.module.params['show_network_policy']:
                    network_policy = dict(
                        forged_transmits=dvs_pg.config.defaultPortConfig.macManagementPolicy.forgedTransmits,
                        promiscuous=dvs_pg.config.defaultPortConfig.macManagementPolicy.allowPromiscuous,
                        mac_changes=dvs_pg.config.defaultPortConfig.macManagementPolicy.macChanges
                    )

                if self.module.params['show_mac_learning']:
                    macLearningPolicy = dvs_pg.config.defaultPortConfig.macManagementPolicy.macLearningPolicy
                    mac_learning = dict(
                        allow_unicast_flooding=macLearningPolicy.allowUnicastFlooding,
                        enabled=macLearningPolicy.enabled,
                        limit=macLearningPolicy.limit,
                        limit_policy=macLearningPolicy.limitPolicy
                    )

                if self.module.params['show_teaming_policy']:
                    teaming_policy = dict(
                        policy=dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy.policy.value,
                        inbound_policy=dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy.reversePolicy.value,
                        notify_switches=dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy.notifySwitches.value,
                        rolling_order=dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy.rollingOrder.value,
                    )

                if self.module.params['show_uplinks'] and \
                        dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy and \
                        dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy.uplinkPortOrder:
                    active_uplinks = dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy.uplinkPortOrder.activeUplinkPort
                    standby_uplinks = dvs_pg.config.defaultPortConfig.uplinkTeamingPolicy.uplinkPortOrder.standbyUplinkPort

                if self.params['show_port_policy']:
                    port_policy = dict(
                        block_override=dvs_pg.config.policy.blockOverrideAllowed,
                        ipfix_override=dvs_pg.config.policy.ipfixOverrideAllowed,
                        live_port_move=dvs_pg.config.policy.livePortMovingAllowed,
                        network_rp_override=dvs_pg.config.policy.networkResourcePoolOverrideAllowed,
                        port_config_reset_at_disconnect=dvs_pg.config.policy.portConfigResetAtDisconnect,
                        shaping_override=dvs_pg.config.policy.shapingOverrideAllowed,
                        traffic_filter_override=dvs_pg.config.policy.trafficFilterOverrideAllowed,
                        uplink_teaming_override=dvs_pg.config.policy.uplinkTeamingOverrideAllowed,
                        vendor_config_override=dvs_pg.config.policy.vendorConfigOverrideAllowed,
                        vlan_override=dvs_pg.config.policy.vlanOverrideAllowed
                    )

                if self.params['show_vlan_info']:
                    vlan_info = self.get_vlan_info(dvs_pg.config.defaultPortConfig.vlan)

                dvpg_details = dict(
                    portgroup_name=unquote(dvs_pg.name),
                    moid=dvs_pg._moId,
                    num_ports=dvs_pg.config.numPorts,
                    dvswitch_name=dvs_pg.config.distributedVirtualSwitch.name,
                    description=dvs_pg.config.description,
                    type=dvs_pg.config.type,
                    port_binding=port_binding,
                    port_allocation=port_allocation,
                    teaming_policy=teaming_policy,
                    port_policy=port_policy,
                    mac_learning=mac_learning,
                    network_policy=network_policy,
                    vlan_info=vlan_info,
                    key=dvs_pg.key,
                    active_uplinks=active_uplinks,
                    standby_uplinks=standby_uplinks,
                )
                result[dvs.name].append(dvpg_details)

        return result


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str', required=True),
        show_mac_learning=dict(type='bool', default=True),
        show_network_policy=dict(type='bool', default=True),
        show_teaming_policy=dict(type='bool', default=True),
        show_uplinks=dict(type='bool', default=True),
        show_port_policy=dict(type='bool', default=True),
        dvswitch=dict(),
        show_vlan_info=dict(type='bool', default=False),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    dvs_pg_mgr = DVSPortgroupInfoManager(module)
    module.exit_json(changed=False,
                     dvs_portgroup_info=dvs_pg_mgr.gather_dvs_portgroup_info())


if __name__ == "__main__":
    main()
