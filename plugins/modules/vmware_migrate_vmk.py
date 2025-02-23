#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_migrate_vmk
short_description: Migrate a VMK interface from VSS to VDS
description:
    - Migrate a VMK interface from VSS to VDS
author:
- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
options:
    esxi_hostname:
        description:
            - ESXi hostname to be managed
        required: true
        type: str
    device:
        description:
            - VMK interface name
        required: true
        type: str
    current_switch_name:
        description:
            - Switch VMK interface is currently on
        required: true
        type: str
    current_portgroup_name:
        description:
            - Portgroup name VMK interface is currently on
        required: true
        type: str
    migrate_switch_name:
        description:
            - Switch name to migrate VMK interface to
        required: true
        type: str
    migrate_portgroup_name:
        description:
            - Portgroup name to migrate VMK interface to
        required: true
        type: str
    migrate_vlan_id:
        description:
            - VLAN to use for the VMK interface when migrating from VDS to VSS
            - Will be ignored when migrating from VSS to VDS
        type: int
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Migrate Management vmk
  community.vmware.vmware_migrate_vmk:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    device: vmk1
    current_switch_name: temp_vswitch
    current_portgroup_name: esx-mgmt
    migrate_switch_name: dvSwitch
    migrate_portgroup_name: Management
  delegate_to: localhost
'''
try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    vmware_argument_spec, find_dvs_by_name, find_hostsystem_by_name,
    PyVmomi, find_dvspg_by_name)


class VMwareMigrateVmk(PyVmomi):

    def __init__(self, module):
        super(VMwareMigrateVmk, self).__init__(module)
        self.host_system = None
        self.migrate_switch_name = self.module.params['migrate_switch_name']
        self.migrate_portgroup_name = self.module.params['migrate_portgroup_name']
        self.migrate_vlan_id = self.module.params['migrate_vlan_id']
        self.device = self.module.params['device']
        self.esxi_hostname = self.module.params['esxi_hostname']
        self.current_portgroup_name = self.module.params['current_portgroup_name']
        self.current_switch_name = self.module.params['current_switch_name']

    def process_state(self):
        try:
            vmk_migration_states = {
                'migrate_vss_vds': self.state_migrate_vss_vds,
                'migrate_vds_vss': self.state_migrate_vds_vss,
                'migrated': self.state_exit_unchanged
            }

            vmk_migration_states[self.check_vmk_current_state()]()

        except vmodl.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=runtime_fault.msg)
        except vmodl.MethodFault as method_fault:
            self.module.fail_json(msg=method_fault.msg)
        except Exception as e:
            self.module.fail_json(msg=str(e))

    def state_exit_unchanged(self):
        self.module.exit_json(changed=False)

    def create_host_vnic_config_vds_vss(self):
        host_vnic_config = vim.host.VirtualNic.Config()
        host_vnic_config.spec = vim.host.VirtualNic.Specification()
        host_vnic_config.changeOperation = "edit"
        host_vnic_config.device = self.device
        host_vnic_config.spec.portgroup = self.migrate_portgroup_name
        return host_vnic_config

    def create_port_group_config_vds_vss(self):
        port_group_config = vim.host.PortGroup.Config()
        port_group_config.spec = vim.host.PortGroup.Specification()
        port_group_config.changeOperation = "add"
        port_group_config.spec.name = self.migrate_portgroup_name
        port_group_config.spec.vlanId = self.migrate_vlan_id if self.migrate_vlan_id is not None else 0
        port_group_config.spec.vswitchName = self.migrate_switch_name
        port_group_config.spec.policy = vim.host.NetworkPolicy()
        return port_group_config

    def state_migrate_vds_vss(self):
        host_network_system = self.host_system.configManager.networkSystem
        config = vim.host.NetworkConfig()
        config.portgroup = [self.create_port_group_config_vds_vss()]
        host_network_system.UpdateNetworkConfig(config, "modify")
        config = vim.host.NetworkConfig()
        config.vnic = [self.create_host_vnic_config_vds_vss()]
        host_network_system.UpdateNetworkConfig(config, "modify")
        self.module.exit_json(changed=True)

    def create_host_vnic_config(self, dv_switch_uuid, portgroup_key):
        host_vnic_config = vim.host.VirtualNic.Config()
        host_vnic_config.spec = vim.host.VirtualNic.Specification()

        host_vnic_config.changeOperation = "edit"
        host_vnic_config.device = self.device
        host_vnic_config.portgroup = ""
        host_vnic_config.spec.distributedVirtualPort = vim.dvs.PortConnection()
        host_vnic_config.spec.distributedVirtualPort.switchUuid = dv_switch_uuid
        host_vnic_config.spec.distributedVirtualPort.portgroupKey = portgroup_key

        return host_vnic_config

    def create_port_group_config(self):
        port_group_config = vim.host.PortGroup.Config()
        port_group_config.spec = vim.host.PortGroup.Specification()

        port_group_config.changeOperation = "remove"
        port_group_config.spec.name = self.current_portgroup_name
        port_group_config.spec.vlanId = -1
        port_group_config.spec.vswitchName = self.current_switch_name
        port_group_config.spec.policy = vim.host.NetworkPolicy()

        return port_group_config

    def state_migrate_vss_vds(self):
        host_network_system = self.host_system.configManager.networkSystem

        dv_switch = find_dvs_by_name(self.content, self.migrate_switch_name)
        pg = find_dvspg_by_name(dv_switch, self.migrate_portgroup_name)

        config = vim.host.NetworkConfig()
        config.portgroup = [self.create_port_group_config()]
        config.vnic = [self.create_host_vnic_config(dv_switch.uuid, pg.key)]
        host_network_system.UpdateNetworkConfig(config, "modify")
        self.module.exit_json(changed=True)

    def check_vmk_current_state(self):
        self.host_system = find_hostsystem_by_name(self.content, self.esxi_hostname)

        for vnic in self.host_system.configManager.networkSystem.networkInfo.vnic:
            if vnic.device == self.device:
                if vnic.spec.distributedVirtualPort is None:
                    std_vswitches = [vswitch.name for vswitch in self.host_system.configManager.networkSystem.networkInfo.vswitch]
                    if self.current_switch_name not in std_vswitches:
                        return "migrated"
                    if vnic.portgroup == self.current_portgroup_name:
                        return "migrate_vss_vds"
                else:
                    dvs = find_dvs_by_name(self.content, self.current_switch_name)
                    if dvs is None:
                        return "migrated"
                    if vnic.spec.distributedVirtualPort.switchUuid == dvs.uuid:
                        return "migrate_vds_vss"

        self.module.fail_json(msg='Unable to find the specified device %s.' % self.device)


def main():

    argument_spec = vmware_argument_spec()
    argument_spec.update(dict(esxi_hostname=dict(required=True, type='str'),
                              device=dict(required=True, type='str'),
                              current_switch_name=dict(required=True, type='str'),
                              current_portgroup_name=dict(required=True, type='str'),
                              migrate_switch_name=dict(required=True, type='str'),
                              migrate_portgroup_name=dict(required=True, type='str'),
                              migrate_vlan_id=dict(required=False, type='int')))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    vmware_migrate_vmk = VMwareMigrateVmk(module)
    vmware_migrate_vmk.process_state()


if __name__ == '__main__':
    main()
