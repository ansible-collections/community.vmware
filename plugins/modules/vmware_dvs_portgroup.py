#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# Copyright: (c) 2017, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_dvs_portgroup
short_description: Create or remove a Distributed vSwitch portgroup.
description:
    - Create or remove a Distributed vSwitch portgroup.
author:
    - Joseph Callen (@jcpowermac)
    - Philippe Dellaert (@pdellaert) <philippe@dellaert.org>
notes:
    - Tested on vSphere 7.0
requirements:
    - "python >= 2.6"
    - PyVmomi
options:
    portgroup_name:
        description:
            - The name of the portgroup that is to be created or deleted.
        required: True
        type: str
    switch_name:
        description:
            - The name of the distributed vSwitch the port group should be created on.
        required: True
        type: str
    vlan_id:
        description:
            - The VLAN ID that should be configured with the portgroup, use 0 for no VLAN.
            - 'If C(vlan_trunk) is configured to be I(true), this can be a combination of multiple ranges and numbers, example: 1-200, 205, 400-4094.'
            - The valid C(vlan_id) range is from 0 to 4094. Overlapping ranges are allowed.
            - 'If C(vlan_private) is configured to be I(true), the corresponding private VLAN should already be configured in the distributed vSwitch.'
        required: True
        type: str
    num_ports:
        description:
            - The number of ports the portgroup should contain.
        type: int
    portgroup_type:
        description:
            - See VMware KB 1022312 regarding portgroup types.
            - Deprecated. Will be removed 2021-12-01.
        choices:
            - 'earlyBinding'
            - 'lateBinding'
            - 'ephemeral'
        type: str
    port_binding:
        description:
            - The type of port binding determines when ports in a port group are assigned to virtual machines.
            - See VMware KB 1022312 U(https://kb.vmware.com/s/article/1022312) for more details.
        type: str
        choices:
            - 'static'
            - 'ephemeral'
        version_added: '1.10.0'
    port_allocation:
        description:
            - Elastic port groups automatically increase or decrease the number of ports as needed.
            - Only valid if I(port_binding) is set to C(static).
            - Will be C(elastic) if not specified and I(port_binding) is set to C(static).
        type: str
        choices:
            - 'elastic'
            - 'fixed'
        version_added: '1.10.0'
    state:
        description:
            - Determines if the portgroup should be present or not.
        required: True
        type: str
        choices:
            - 'present'
            - 'absent'
    vlan_trunk:
        description:
            - Indicates whether this is a VLAN trunk or not.
            - Mutually exclusive with C(vlan_private) parameter.
        required: False
        default: False
        type: bool
    vlan_private:
        description:
            - Indicates whether this is for a private VLAN or not.
            - Mutually exclusive with C(vlan_trunk) parameter.
        required: False
        default: False
        type: bool
    mac_learning:
        description:
            - Dictionary which configures MAC learning for portgroup.
        suboptions:
            allow_unicast_flooding:
                type: bool
                description: The flag to allow flooding of unlearned MAC for ingress traffic.
                required: False
            enabled:
                type: bool
                description: The flag to indicate if source MAC address learning is allowed.
                required: False
            limit:
                type: int
                description: The maximum number of MAC addresses that can be learned.
                required: False
            limit_policy:
                type: str
                description: The default switching policy after MAC limit is exceeded.
                required: False
                choices:
                    - 'allow'
                    - 'drop'
        type: dict
        version_added: '1.10.0'
    network_policy:
        description:
            - Dictionary which configures the different security values for portgroup.
        suboptions:
            promiscuous:
                type: bool
                description: Indicates whether promiscuous mode is allowed.
                default: False
            forged_transmits:
                type: bool
                description: Indicates whether forged transmits are allowed.
                default: False
            mac_changes:
                type: bool
                description: Indicates whether mac changes are allowed.
                default: False
        required: False
        default: {
            promiscuous: False,
            forged_transmits: False,
            mac_changes: False,
        }
        type: dict
    teaming_policy:
        description:
            - Dictionary which configures the different teaming values for portgroup.
        suboptions:
            load_balance_policy:
                description:
                - Network adapter teaming policy.
                - C(loadbalance_loadbased) is available from version 2.6 and onwards.
                default: 'loadbalance_srcid'
                type: str
                choices:
                - loadbalance_ip
                - loadbalance_srcmac
                - loadbalance_srcid
                - loadbalance_loadbased
                - failover_explicit
            notify_switches:
                description:
                - Indicate whether or not to notify the physical switch if a link fails.
                default: True
                type: bool
            inbound_policy:
                description:
                - Indicate whether or not the teaming policy is applied to inbound frames as well.
                type: bool
            rolling_order:
                description:
                - Indicate whether or not to use a rolling policy when restoring links.
                default: False
                type: bool
            active_uplinks:
                description:
                - List of active uplinks used for load balancing.
                type: list
                elements: str
                version_added: '1.10.0'
            standby_uplinks:
                description:
                - List of standby uplinks used for failover.
                type: list
                elements: str
                version_added: '1.10.0'
        default: {
            'notify_switches': True,
            'load_balance_policy': 'loadbalance_srcid',
            'rolling_order': False
        }
        type: dict
    port_policy:
        description:
        - Dictionary which configures the advanced policy settings for the portgroup.
        suboptions:
            block_override:
                description:
                - Indicates if the block policy can be changed per port.
                default: True
                type: bool
            port_config_reset_at_disconnect:
                description:
                - Indicates if the configuration of a port is reset automatically after disconnect.
                default: True
                type: bool
                required: False
            ipfix_override:
                description:
                - Indicates if the ipfix policy can be changed per port.
                default: False
                type: bool
            live_port_move:
                description:
                - Indicates if a live port can be moved in or out of the portgroup.
                default: False
                type: bool
            network_rp_override:
                description:
                - Indicates if the network resource pool can be changed per port.
                default: False
                type: bool
            security_override:
                description:
                - Indicates if the security policy can be changed per port.
                default: False
                type: bool
            shaping_override:
                description:
                - Indicates if the shaping policy can be changed per port.
                default: False
                type: bool
            traffic_filter_override:
                description:
                - Indicates if the traffic filter can be changed per port.
                default: False
                type: bool
            uplink_teaming_override:
                description:
                - Indicates if the uplink teaming policy can be changed per port.
                default: False
                type: bool
            vendor_config_override:
                description:
                - Indicates if the vendor config can be changed per port.
                type: bool
                default: False
            vlan_override:
                description:
                - Indicates if the vlan can be changed per port.
                type: bool
                default: False
        default: {
            'traffic_filter_override': False,
            'network_rp_override': False,
            'live_port_move': False,
            'security_override': False,
            'vendor_config_override': False,
            'port_config_reset_at_disconnect': True,
            'uplink_teaming_override': False,
            'block_override': True,
            'shaping_override': False,
            'vlan_override': False,
            'ipfix_override': False
        }
        type: dict
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Create vlan portgroup
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-123-portrgoup
    switch_name: dvSwitch
    vlan_id: 123
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create vlan trunk portgroup
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-trunk-portrgoup
    switch_name: dvSwitch
    vlan_id: 1-1000, 1005, 1100-1200
    vlan_trunk: True
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create private vlan portgroup
  vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: private-vlan-portrgoup
    switch_name: dvSwitch
    vlan_id: 1001
    vlan_private: True
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create no-vlan portgroup
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: no-vlan-portrgoup
    switch_name: dvSwitch
    vlan_id: 0
    num_ports: 120
    port_binding: static
    state: present
  delegate_to: localhost

- name: Create vlan portgroup with all security and port policies
  community.vmware.vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-123-portrgoup
    switch_name: dvSwitch
    vlan_id: 123
    num_ports: 120
    port_binding: static
    state: present
    network_policy:
      promiscuous: true
      forged_transmits: true
      mac_changes: true
    port_policy:
      block_override: true
      ipfix_override: true
      live_port_move: true
      network_rp_override: true
      port_config_reset_at_disconnect: true
      security_override: true
      shaping_override: true
      traffic_filter_override: true
      uplink_teaming_override: true
      vendor_config_override: true
      vlan_override: true
  delegate_to: localhost
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    dvs_supports_mac_learning,
    find_dvs_by_name,
    find_dvspg_by_name,
    vmware_argument_spec,
    wait_for_task)


class VMwareDvsPortgroup(PyVmomi):
    def __init__(self, module):
        super(VMwareDvsPortgroup, self).__init__(module)
        self.dvs_portgroup = None
        self.dv_switch = None

        # Some sanity checks
        if self.module.params['port_allocation'] == 'elastic':
            if self.module.params['port_binding'] == 'ephemeral':
                self.module.fail_json(
                    msg="'elastic' port allocation is not supported on an 'ephemeral' portgroup."
                )

            if self.module.params['num_ports']:
                self.module.fail_json(
                    msg="The number of ports cannot be configured when port allocation is set to 'elastic'."
                )

    def create_vlan_list(self):
        vlan_id_list = []
        for vlan_id_splitted in self.module.params['vlan_id'].split(','):
            vlans = vlan_id_splitted.split('-')
            if len(vlans) > 2:
                self.module.fail_json(msg="Invalid VLAN range %s." % vlan_id_splitted)
            if len(vlans) == 2:
                vlan_id_start = vlans[0].strip()
                vlan_id_end = vlans[1].strip()
                if not vlan_id_start.isdigit():
                    self.module.fail_json(msg="Invalid VLAN %s." % vlan_id_start)
                if not vlan_id_end.isdigit():
                    self.module.fail_json(msg="Invalid VLAN %s." % vlan_id_end)
                vlan_id_start = int(vlan_id_start)
                vlan_id_end = int(vlan_id_end)
                if vlan_id_start not in range(0, 4095) or vlan_id_end not in range(0, 4095):
                    self.module.fail_json(msg="vlan_id range %s specified is incorrect. The valid vlan_id range is from 0 to 4094." % vlan_id_splitted)
                vlan_id_list.append((vlan_id_start, vlan_id_end))
            else:
                vlan_id = vlans[0].strip()
                if not vlan_id.isdigit():
                    self.module.fail_json(msg="Invalid VLAN %s." % vlan_id)
                vlan_id = int(vlan_id)
                vlan_id_list.append((vlan_id, vlan_id))

        vlan_id_list.sort()

        return vlan_id_list

    def build_config(self):
        config = vim.dvs.DistributedVirtualPortgroup.ConfigSpec()

        # Basic config
        config.name = self.module.params['portgroup_name']

        if self.module.params['port_allocation'] != 'elastic' and self.module.params['port_binding'] != 'ephemeral':
            config.numPorts = self.module.params['num_ports']

        # Default port config
        config.defaultPortConfig = vim.dvs.VmwareDistributedVirtualSwitch.VmwarePortConfigPolicy()
        if self.module.params['vlan_trunk']:
            config.defaultPortConfig.vlan = vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec()
            config.defaultPortConfig.vlan.vlanId = list(map(lambda x: vim.NumericRange(start=x[0], end=x[1]), self.create_vlan_list()))
        elif self.module.params['vlan_private']:
            # Check that private VLAN exists in dvs
            if self.module.params['vlan_private']:
                pvlan_exists = self.check_dvs_pvlan()
                if not pvlan_exists:
                    self.module.fail_json(msg="No private vlan with id %s in distributed vSwitch %s"
                                          % (self.module.params['vlan_id'], self.module.params['switch_name']))

            config.defaultPortConfig.vlan = vim.dvs.VmwareDistributedVirtualSwitch.PvlanSpec()
            config.defaultPortConfig.vlan.pvlanId = int(self.module.params['vlan_id'])
        else:
            config.defaultPortConfig.vlan = vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec()
            config.defaultPortConfig.vlan.vlanId = int(self.module.params['vlan_id'])

        config.defaultPortConfig.vlan.inherited = False

        # If the dvSwitch supports MAC learning, it's a version where securityPolicy is deprecated
        if dvs_supports_mac_learning(self.dv_switch):
            config.defaultPortConfig.macManagementPolicy = vim.dvs.VmwareDistributedVirtualSwitch.MacManagementPolicy()
            config.defaultPortConfig.macManagementPolicy.allowPromiscuous = self.module.params['network_policy']['promiscuous']
            config.defaultPortConfig.macManagementPolicy.forgedTransmits = self.module.params['network_policy']['forged_transmits']
            config.defaultPortConfig.macManagementPolicy.macChanges = self.module.params['network_policy']['mac_changes']

            macLearning = self.module.params['mac_learning']
            if macLearning:
                macLearningPolicy = vim.dvs.VmwareDistributedVirtualSwitch.MacLearningPolicy()
                if macLearning['allow_unicast_flooding'] is not None:
                    macLearningPolicy.allowUnicastFlooding = macLearning['allow_unicast_flooding']
                if macLearning['enabled'] is not None:
                    macLearningPolicy.enabled = macLearning['enabled']
                if macLearning['limit'] is not None:
                    macLearningPolicy.limit = macLearning['limit']
                if macLearning['limit_policy']:
                    macLearningPolicy.limitPolicy = macLearning['limit_policy']
                config.defaultPortConfig.macManagementPolicy.macLearningPolicy = macLearningPolicy
        else:
            config.defaultPortConfig.securityPolicy = vim.dvs.VmwareDistributedVirtualSwitch.SecurityPolicy()
            config.defaultPortConfig.securityPolicy.allowPromiscuous = vim.BoolPolicy(value=self.module.params['network_policy']['promiscuous'])
            config.defaultPortConfig.securityPolicy.forgedTransmits = vim.BoolPolicy(value=self.module.params['network_policy']['forged_transmits'])
            config.defaultPortConfig.securityPolicy.macChanges = vim.BoolPolicy(value=self.module.params['network_policy']['mac_changes'])

        # Teaming Policy
        teamingPolicy = vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortTeamingPolicy()
        teamingPolicy.policy = vim.StringPolicy(value=self.module.params['teaming_policy']['load_balance_policy'])
        if self.module.params['teaming_policy']['inbound_policy'] is not None:
            teamingPolicy.reversePolicy = vim.BoolPolicy(value=self.module.params['teaming_policy']['inbound_policy'])
        teamingPolicy.notifySwitches = vim.BoolPolicy(value=self.module.params['teaming_policy']['notify_switches'])
        teamingPolicy.rollingOrder = vim.BoolPolicy(value=self.module.params['teaming_policy']['rolling_order'])

        if self.module.params['teaming_policy']['active_uplinks'] or self.module.params['teaming_policy']['standby_uplinks']:
            teamingPolicy.uplinkPortOrder = vim.dvs.VmwareDistributedVirtualSwitch.UplinkPortOrderPolicy()
            if self.module.params['teaming_policy']['active_uplinks']:
                teamingPolicy.uplinkPortOrder.activeUplinkPort = self.module.params['teaming_policy']['active_uplinks']
            if self.module.params['teaming_policy']['standby_uplinks']:
                teamingPolicy.uplinkPortOrder.standbyUplinkPort = self.module.params['teaming_policy']['standby_uplinks']

        config.defaultPortConfig.uplinkTeamingPolicy = teamingPolicy

        # PG policy (advanced_policy)
        config.policy = vim.dvs.VmwareDistributedVirtualSwitch.VMwarePortgroupPolicy()
        config.policy.blockOverrideAllowed = self.module.params['port_policy']['block_override']
        config.policy.ipfixOverrideAllowed = self.module.params['port_policy']['ipfix_override']
        config.policy.livePortMovingAllowed = self.module.params['port_policy']['live_port_move']
        config.policy.networkResourcePoolOverrideAllowed = self.module.params['port_policy']['network_rp_override']
        config.policy.portConfigResetAtDisconnect = self.module.params['port_policy']['port_config_reset_at_disconnect']
        config.policy.securityPolicyOverrideAllowed = self.module.params['port_policy']['security_override']
        config.policy.shapingOverrideAllowed = self.module.params['port_policy']['shaping_override']
        config.policy.trafficFilterOverrideAllowed = self.module.params['port_policy']['traffic_filter_override']
        config.policy.uplinkTeamingOverrideAllowed = self.module.params['port_policy']['uplink_teaming_override']
        config.policy.vendorConfigOverrideAllowed = self.module.params['port_policy']['vendor_config_override']
        config.policy.vlanOverrideAllowed = self.module.params['port_policy']['vlan_override']

        # PG Type
        # NOTE: 'portgroup_type' is deprecated.
        if self.module.params['portgroup_type']:
            config.type = self.module.params['portgroup_type']
        elif self.module.params['port_binding'] == 'ephemeral':
            config.type = 'ephemeral'
        else:
            config.type = 'earlyBinding'

        if self.module.params['port_allocation']:
            if self.module.params['port_allocation'] == 'elastic':
                config.autoExpand = True
            else:
                config.autoExpand = False

        return config

    def process_state(self):
        dvspg_states = {
            'absent': {
                'present': self.state_destroy_dvspg,
                'absent': self.state_exit_unchanged,
            },
            'present': {
                'update': self.state_update_dvspg,
                'present': self.state_exit_unchanged,
                'absent': self.state_create_dvspg,
            }
        }
        try:
            dvspg_states[self.module.params['state']][self.check_dvspg_state()]()
        except vmodl.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=runtime_fault.msg)
        except vmodl.MethodFault as method_fault:
            self.module.fail_json(msg=method_fault.msg)
        except Exception as e:
            self.module.fail_json(msg=str(e))

    def update_port_group(self):
        config = self.build_config()
        config.configVersion = self.dvs_portgroup.config.configVersion
        task = self.dvs_portgroup.ReconfigureDVPortgroup_Task(config)
        changed, result = wait_for_task(task)
        return changed, result

    def create_port_group(self):
        config = self.build_config()
        task = self.dv_switch.AddDVPortgroup_Task([config])
        changed, result = wait_for_task(task)
        return changed, result

    def state_destroy_dvspg(self):
        changed = True
        result = None

        if not self.module.check_mode:
            task = self.dvs_portgroup.Destroy_Task()
            changed, result = wait_for_task(task)
        self.module.exit_json(changed=changed, result=str(result))

    def state_exit_unchanged(self):
        self.module.exit_json(changed=False)

    def state_update_dvspg(self):
        changed = True
        result = None

        if not self.module.check_mode:
            changed, result = self.update_port_group()
        self.module.exit_json(changed=changed, result=str(result))

    def state_create_dvspg(self):
        changed = True
        result = None

        if not self.module.check_mode:
            changed, result = self.create_port_group()
        self.module.exit_json(changed=changed, result=str(result))

    def check_dvs_pvlan(self):
        for pvlan in self.dv_switch.config.pvlanConfig:
            if pvlan.primaryVlanId == int(self.module.params['vlan_id']):
                return True
            if pvlan.secondaryVlanId == int(self.module.params['vlan_id']):
                return True
        return False

    def check_dvspg_state(self):
        self.dv_switch = find_dvs_by_name(self.content, self.module.params['switch_name'])

        if self.dv_switch is None:
            self.module.fail_json(msg="A distributed virtual switch with name %s does not exist" % self.module.params['switch_name'])
        self.dvs_portgroup = find_dvspg_by_name(self.dv_switch, self.module.params['portgroup_name'])

        if self.dvs_portgroup is None:
            return 'absent'

        # Check config
        if self.module.params['port_allocation'] != 'elastic' and self.module.params['port_binding'] != 'ephemeral':
            if self.dvs_portgroup.config.numPorts != self.module.params['num_ports']:
                return 'update'

        # Default port config
        defaultPortConfig = self.dvs_portgroup.config.defaultPortConfig
        if self.module.params['vlan_trunk']:
            if not isinstance(defaultPortConfig.vlan, vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec):
                return 'update'
            if list(map(lambda x: (x.start, x.end), defaultPortConfig.vlan.vlanId)) != self.create_vlan_list():
                return 'update'
        elif self.module.params['vlan_private']:
            if not isinstance(defaultPortConfig.vlan, vim.dvs.VmwareDistributedVirtualSwitch.PvlanSpec):
                return 'update'
            if defaultPortConfig.vlan.pvlanId != int(self.module.params['vlan_id']):
                return 'update'
        else:
            if not isinstance(defaultPortConfig.vlan, vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec):
                return 'update'
            if defaultPortConfig.vlan.vlanId != int(self.module.params['vlan_id']):
                return 'update'

        # If the dvSwitch supports MAC learning, it's a version where securityPolicy is deprecated
        if dvs_supports_mac_learning(self.dv_switch):
            if defaultPortConfig.macManagementPolicy.allowPromiscuous != self.module.params['network_policy']['promiscuous'] or \
                    defaultPortConfig.macManagementPolicy.forgedTransmits != self.module.params['network_policy']['forged_transmits'] or \
                    defaultPortConfig.macManagementPolicy.macChanges != self.module.params['network_policy']['mac_changes']:
                return 'update'

            macLearning = self.module.params['mac_learning']
            if macLearning:
                macLearningPolicy = defaultPortConfig.macManagementPolicy.macLearningPolicy
                if macLearning['allow_unicast_flooding'] is not None and macLearningPolicy.allowUnicastFlooding != macLearning['allow_unicast_flooding']:
                    return 'update'
                if macLearning['enabled'] is not None and macLearningPolicy.enabled != macLearning['enabled']:
                    return 'update'
                if macLearning['limit'] is not None and macLearningPolicy.limit != macLearning['limit']:
                    return 'update'
                if macLearning['limit_policy'] and macLearningPolicy.limitPolicy != macLearning['limit_policy']:
                    return 'update'
        else:
            if defaultPortConfig.securityPolicy.allowPromiscuous.value != self.module.params['network_policy']['promiscuous'] or \
                    defaultPortConfig.securityPolicy.forgedTransmits.value != self.module.params['network_policy']['forged_transmits'] or \
                    defaultPortConfig.securityPolicy.macChanges.value != self.module.params['network_policy']['mac_changes']:
                return 'update'

        # Teaming Policy
        teamingPolicy = self.dvs_portgroup.config.defaultPortConfig.uplinkTeamingPolicy

        if self.module.params['teaming_policy']['inbound_policy'] is not None and \
                teamingPolicy.reversePolicy.value != self.module.params['teaming_policy']['inbound_policy']:
            return 'update'

        if teamingPolicy.policy.value != self.module.params['teaming_policy']['load_balance_policy'] or \
                teamingPolicy.notifySwitches.value != self.module.params['teaming_policy']['notify_switches'] or \
                teamingPolicy.rollingOrder.value != self.module.params['teaming_policy']['rolling_order']:
            return 'update'

        if self.module.params['teaming_policy']['active_uplinks'] and \
                teamingPolicy.uplinkPortOrder.activeUplinkPort != self.module.params['teaming_policy']['active_uplinks']:
            return 'update'

        if self.module.params['teaming_policy']['standby_uplinks'] and \
                teamingPolicy.uplinkPortOrder.standbyUplinkPort != self.module.params['teaming_policy']['standby_uplinks']:
            return 'update'

        # PG policy (advanced_policy)
        policy = self.dvs_portgroup.config.policy
        if policy.blockOverrideAllowed != self.module.params['port_policy']['block_override'] or \
                policy.ipfixOverrideAllowed != self.module.params['port_policy']['ipfix_override'] or \
                policy.livePortMovingAllowed != self.module.params['port_policy']['live_port_move'] or \
                policy.networkResourcePoolOverrideAllowed != self.module.params['port_policy']['network_rp_override'] or \
                policy.portConfigResetAtDisconnect != self.module.params['port_policy']['port_config_reset_at_disconnect'] or \
                policy.securityPolicyOverrideAllowed != self.module.params['port_policy']['security_override'] or \
                policy.shapingOverrideAllowed != self.module.params['port_policy']['shaping_override'] or \
                policy.trafficFilterOverrideAllowed != self.module.params['port_policy']['traffic_filter_override'] or \
                policy.uplinkTeamingOverrideAllowed != self.module.params['port_policy']['uplink_teaming_override'] or \
                policy.vendorConfigOverrideAllowed != self.module.params['port_policy']['vendor_config_override'] or \
                policy.vlanOverrideAllowed != self.module.params['port_policy']['vlan_override']:
            return 'update'

        # PG Type
        # NOTE: 'portgroup_type' is deprecated.
        if self.module.params['portgroup_type']:
            if self.dvs_portgroup.config.type != self.module.params['portgroup_type']:
                return 'update'
        elif self.module.params['port_binding'] == 'ephemeral':
            if self.dvs_portgroup.config.type != 'ephemeral':
                return 'update'
        elif self.dvs_portgroup.config.type != 'earlyBinding':
            return 'update'

        # Check port allocation
        if self.module.params['port_allocation']:
            if self.module.params['port_allocation'] == 'elastic' and self.dvs_portgroup.config.autoExpand is False:
                return 'update'
            elif self.module.params['port_allocation'] == 'fixed' and self.dvs_portgroup.config.autoExpand is True:
                return 'update'

        return 'present'


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        dict(
            portgroup_name=dict(required=True, type='str'),
            switch_name=dict(required=True, type='str'),
            vlan_id=dict(required=True, type='str'),
            num_ports=dict(type='int'),
            portgroup_type=dict(
                type='str',
                choices=['earlyBinding', 'lateBinding', 'ephemeral'],
                removed_at_date='2021-12-01',
                removed_from_collection='community.vmware',
            ),
            port_binding=dict(type='str', choices=['static', 'ephemeral']),
            port_allocation=dict(type='str', choices=['fixed', 'elastic']),
            state=dict(required=True, choices=['present', 'absent'], type='str'),
            vlan_trunk=dict(type='bool', default=False),
            vlan_private=dict(type='bool', default=False),
            network_policy=dict(
                type='dict',
                options=dict(
                    promiscuous=dict(type='bool', default=False),
                    forged_transmits=dict(type='bool', default=False),
                    mac_changes=dict(type='bool', default=False)
                ),
                default=dict(
                    promiscuous=False,
                    forged_transmits=False,
                    mac_changes=False
                )
            ),
            teaming_policy=dict(
                type='dict',
                options=dict(
                    inbound_policy=dict(type='bool'),
                    notify_switches=dict(type='bool', default=True),
                    rolling_order=dict(type='bool', default=False),
                    load_balance_policy=dict(type='str',
                                             default='loadbalance_srcid',
                                             choices=[
                                                 'loadbalance_ip',
                                                 'loadbalance_srcmac',
                                                 'loadbalance_srcid',
                                                 'loadbalance_loadbased',
                                                 'failover_explicit',
                                             ],
                                             ),
                    active_uplinks=dict(type='list', elements='str'),
                    standby_uplinks=dict(type='list', elements='str'),
                ),
                default=dict(
                    notify_switches=True,
                    rolling_order=False,
                    load_balance_policy='loadbalance_srcid',
                ),
            ),
            port_policy=dict(
                type='dict',
                options=dict(
                    block_override=dict(type='bool', default=True),
                    ipfix_override=dict(type='bool', default=False),
                    live_port_move=dict(type='bool', default=False),
                    network_rp_override=dict(type='bool', default=False),
                    port_config_reset_at_disconnect=dict(type='bool', default=True),
                    security_override=dict(type='bool', default=False),
                    shaping_override=dict(type='bool', default=False),
                    traffic_filter_override=dict(type='bool', default=False),
                    uplink_teaming_override=dict(type='bool', default=False),
                    vendor_config_override=dict(type='bool', default=False),
                    vlan_override=dict(type='bool', default=False)
                ),
                default=dict(
                    block_override=True,
                    ipfix_override=False,
                    live_port_move=False,
                    network_rp_override=False,
                    port_config_reset_at_disconnect=True,
                    security_override=False,
                    shaping_override=False,
                    traffic_filter_override=False,
                    uplink_teaming_override=False,
                    vendor_config_override=False,
                    vlan_override=False
                ),
            ),
            mac_learning=dict(
                type='dict',
                options=dict(
                    allow_unicast_flooding=dict(type='bool'),
                    enabled=dict(type='bool'),
                    limit=dict(type='int'),
                    limit_policy=dict(type='str', choices=['allow', 'drop']),
                ),
            )
        )
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           required_one_of=[
                               ['portgroup_type', 'port_binding'],
                           ],
                           mutually_exclusive=[
                               ['portgroup_type', 'port_binding'],
                               ['portgroup_type', 'port_allocation'],
                               ['vlan_trunk', 'vlan_private'],
                           ],
                           supports_check_mode=True)

    vmware_dvs_portgroup = VMwareDvsPortgroup(module)
    vmware_dvs_portgroup.process_state()


if __name__ == '__main__':
    main()
