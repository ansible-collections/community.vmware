#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# Copyright: (c) 2019, VMware Inc.
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_dvs_host
short_description: Add or remove a host from distributed virtual switch
description:
    - Manage a host system from distributed virtual switch.
author:
- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Joseph Andreatta (@vmwjoseph)
options:
    esxi_hostname:
        description:
        - The ESXi hostname.
        required: true
        type: str
    switch_name:
        description:
        - The name of the Distributed vSwitch.
        required: true
        type: str
    vmnics:
        description:
        - The ESXi hosts vmnics to use with the Distributed vSwitch.
        - If unset, the current non-LAG uplinks will be kept.
        - To remove all non-LAG uplinks, use the empty list V([]).
        required: false
        type: list
        elements: str
    lag_uplinks:
        required: false
        type: list
        elements: dict
        description:
        - The ESXi hosts vmnics to use with specific LAGs.
        - If unset, the current LAG uplinks will be kept.
        - If set, LAG uplinks will be set to I(exactly) this list. So you always have to define the complete LAG uplink configuration;
          if you don't, you might loose LAG uplinks.
        - To remove all LAG uplinks, use the empty list V([]).
        suboptions:
            lag:
                description:
                - Name of the LAG.
                type: str
                required: true
            vmnics:
                description:
                - The ESXi hosts vmnics to use with the LAG.
                required: false
                type: list
                default: []
                elements: str
    state:
        description:
        - If the host should be present or absent attached to the vSwitch.
        choices: [ present, absent ]
        default: 'present'
        type: str
    vendor_specific_config:
        description:
            - List of key, value dictionaries for the Vendor Specific Configuration.
        suboptions:
            key:
              description:
              - Key of setting.
              type: str
              required: true
            value:
              description:
              - Value of setting.
              type: str
              required: true
        required: false
        type: list
        elements: dict
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Add Host to dVS
  community.vmware.vmware_dvs_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    switch_name: dvSwitch
    vmnics:
        - vmnic0
        - vmnic1
    state: present
  delegate_to: localhost

- name: Add vmnics to LAGs
  community.vmware.vmware_dvs_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    switch_name: dvSwitch
    lag_uplinks:
        - lag: lag1
          vmnics:
              - vmnic0
              - vmnic1
        - lag: lag2
          vmnics:
              - vmnic2
              - vmnic3
    state: present
  delegate_to: localhost

- name: Add Host to dVS/enable learnswitch (https://labs.vmware.com/flings/learnswitch)
  community.vmware.vmware_dvs_host:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    switch_name: dvSwitch
    vendor_specific_config:
        - key: com.vmware.netoverlay.layer1
          value: learnswitch
    vmnics:
        - vmnic0
        - vmnic1
    state: present
  delegate_to: localhost
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    find_dvs_by_name,
    find_hostsystem_by_name,
    wait_for_task)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VMwareDvsHost(PyVmomi):
    def __init__(self, module):
        super(VMwareDvsHost, self).__init__(module)
        self.host = None
        self.dv_switch = None
        self.desired_state = {}

        self.state = self.module.params['state']
        self.switch_name = self.module.params['switch_name']
        self.esxi_hostname = self.module.params['esxi_hostname']
        self.vmnics = self.module.params['vmnics']
        self.lag_uplinks = self.module.params['lag_uplinks']
        self.vendor_specific_config = self.module.params['vendor_specific_config']

        self.dv_switch = find_dvs_by_name(self.content, self.switch_name)

        if self.dv_switch is None:
            self.module.fail_json(msg="A distributed virtual switch %s "
                                      "does not exist" % self.switch_name)

        self.uplink_portgroup = self.find_dvs_uplink_pg()

        self.lags = {}
        for lag in self.dv_switch.config.lacpGroupConfig:
            self.lags[lag.name] = lag

        if self.lag_uplinks is not None:
            for lag_uplink in self.lag_uplinks:
                if lag_uplink['lag'] not in self.lags:
                    self.module.fail_json(msg="LAG %s not found" % lag_uplink['lag'])

    def process_state(self):
        dvs_host_states = {
            'absent': {
                'present': self.state_destroy_dvs_host,
                'absent': self.state_exit_unchanged,
            },
            'present': {
                'update': self.state_update_dvs_host,
                'present': self.state_exit_unchanged,
                'absent': self.state_create_dvs_host,
            }
        }

        try:
            dvs_host_states[self.state][self.check_dvs_host_state()]()
        except vmodl.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=to_native(runtime_fault.msg))
        except vmodl.MethodFault as method_fault:
            self.module.fail_json(msg=to_native(method_fault.msg))
        except Exception as e:
            self.module.fail_json(msg=to_native(e))

    def find_dvs_uplink_pg(self):
        # There should only always be a single uplink port group on
        # a distributed virtual switch
        dvs_uplink_pg = self.dv_switch.config.uplinkPortgroup[0] if len(self.dv_switch.config.uplinkPortgroup) else None
        return dvs_uplink_pg

    # operation should be edit, add and remove
    def modify_dvs_host(self, operation):
        changed, result = False, None
        spec = vim.DistributedVirtualSwitch.ConfigSpec()
        spec.configVersion = self.dv_switch.config.configVersion
        spec.host = [vim.dvs.HostMember.ConfigSpec()]
        spec.host[0].operation = operation
        spec.host[0].host = self.host
        if self.vendor_specific_config:
            config = list()
            for item in self.vendor_specific_config:
                config.append(vim.dvs.KeyedOpaqueBlob(key=item['key'], opaqueData=item['value']))
            spec.host[0].vendorSpecificConfig = config

        if operation == "edit":
            spec.host[0].backing = vim.dvs.HostMember.PnicBacking()

            for nic, uplinkPortKey in self.desired_state.items():
                pnicSpec = vim.dvs.HostMember.PnicSpec()
                pnicSpec.pnicDevice = nic
                pnicSpec.uplinkPortgroupKey = self.uplink_portgroup.key
                pnicSpec.uplinkPortKey = uplinkPortKey
                spec.host[0].backing.pnicSpec.append(pnicSpec)

        try:
            task = self.dv_switch.ReconfigureDvs_Task(spec)
            changed, result = wait_for_task(task)
        except vmodl.fault.NotSupported as not_supported:
            self.module.fail_json(msg="Failed to configure DVS host %s as it is not"
                                      " compatible with the VDS version." % self.esxi_hostname,
                                  details=to_native(not_supported.msg))
        return changed, result

    def state_destroy_dvs_host(self):
        operation, changed, result = ("remove", True, None)

        if not self.module.check_mode:
            changed, result = self.modify_dvs_host(operation)
        self.module.exit_json(changed=changed, result=to_native(result))

    def state_exit_unchanged(self):
        self.module.exit_json(changed=False)

    def state_update_dvs_host(self):
        operation, changed, result = ("edit", True, None)

        if not self.module.check_mode:
            changed, result = self.modify_dvs_host(operation)
        self.module.exit_json(changed=changed, result=to_native(result))

    def state_create_dvs_host(self):
        operation, changed, result = ("add", True, None)

        if not self.module.check_mode:
            changed, result = self.modify_dvs_host(operation)
            if changed:
                self.set_desired_state()
                changed, result = self.modify_dvs_host("edit")
            else:
                self.module.exit_json(changed=changed, result=to_native(result))

        self.module.exit_json(changed=changed, result=to_native(result))

    def find_host_attached_dvs(self):
        for dvs_host_member in self.dv_switch.config.host:
            if dvs_host_member.config.host.name == self.esxi_hostname:
                return dvs_host_member.config.host

        return None

    def set_desired_state(self):
        lag_uplinks = []
        switch_uplink_ports = {'non_lag': []}

        for dvs_host_member in self.dv_switch.config.host:
            if dvs_host_member.config.host.name == self.esxi_hostname:
                break

        portCriteria = vim.dvs.PortCriteria()
        portCriteria.host = [self.host]
        portCriteria.portgroupKey = self.uplink_portgroup.key
        portCriteria.uplinkPort = True
        ports = self.dv_switch.FetchDVPorts(portCriteria)

        for name, lag in self.lags.items():
            switch_uplink_ports[name] = []
            for uplinkName in lag.uplinkName:
                for port in ports:
                    if port.config.name == uplinkName:
                        switch_uplink_ports[name].append(port.key)
                        lag_uplinks.append(port.key)

        for port in sorted(ports, key=lambda port: port.config.name):
            if port.key in self.uplink_portgroup.portKeys and port.key not in lag_uplinks:
                switch_uplink_ports['non_lag'].append(port.key)

        # If defined, use vmnics as non-LAG uplinks
        if self.vmnics is not None:
            count = 0
            for vmnic in self.vmnics:
                self.desired_state[vmnic] = switch_uplink_ports['non_lag'][count]
                count += 1
        # Otherwise keep current non-LAG uplinks
        else:
            for pnicSpec in dvs_host_member.config.backing.pnicSpec:
                if pnicSpec.uplinkPortKey not in lag_uplinks:
                    self.desired_state[pnicSpec.pnicDevice] = pnicSpec.uplinkPortKey

        # If defined, use lag_uplinks as LAG uplinks
        if self.lag_uplinks is not None:
            for lag in self.lag_uplinks:
                count = 0
                for vmnic in lag['vmnics']:
                    self.desired_state[vmnic] = switch_uplink_ports[lag['lag']][count]
                    count += 1
        # Otherwise keep current LAG uplinks
        else:
            for pnicSpec in dvs_host_member.config.backing.pnicSpec:
                if pnicSpec.uplinkPortKey in lag_uplinks:
                    self.desired_state[pnicSpec.pnicDevice] = pnicSpec.uplinkPortKey

    def check_uplinks(self):
        pnic_device = []

        self.set_desired_state()

        for dvs_host_member in self.dv_switch.config.host:
            if dvs_host_member.config.host.name == self.esxi_hostname:
                break

        for pnicSpec in dvs_host_member.config.backing.pnicSpec:
            pnic_device.append(pnicSpec.pnicDevice)
            if pnicSpec.pnicDevice not in self.desired_state:
                return False
            if pnicSpec.uplinkPortKey != self.desired_state[pnicSpec.pnicDevice]:
                return False

        for vmnic in self.desired_state:
            if vmnic not in pnic_device:
                return False

        return True

    def check_dvs_host_state(self):
        if self.uplink_portgroup is None:
            self.module.fail_json(msg="An uplink portgroup does not exist on"
                                      " the distributed virtual switch %s" % self.switch_name)

        self.host = self.find_host_attached_dvs()

        if self.host is None:
            # We still need the HostSystem object to add the host
            # to the distributed vswitch
            self.host = find_hostsystem_by_name(self.content, self.esxi_hostname)
            if self.host is None:
                self.module.fail_json(msg="The esxi_hostname %s does not exist "
                                          "in vCenter" % self.esxi_hostname)
            return 'absent'
        # Skip checking uplinks if the host should be absent, anyway
        elif self.state == 'absent':
            return 'present'
        else:
            if self.check_uplinks():
                return 'present'
            else:
                return 'update'


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        dict(
            esxi_hostname=dict(required=True, type='str'),
            switch_name=dict(required=True, type='str'),
            vmnics=dict(required=False, type='list', elements='str'),
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            vendor_specific_config=dict(
                type='list',
                elements='dict',
                required=False,
                options=dict(
                    key=dict(type='str', required=True, no_log=False),
                    value=dict(type='str', required=True),
                ),
            ),
            lag_uplinks=dict(
                type='list',
                required=False,
                elements='dict',
                options=dict(
                    lag=dict(
                        type='str',
                        required=True,
                    ),
                    vmnics=dict(
                        type='list',
                        required=False,
                        elements='str',
                        default=[],
                    ),
                ),
            ),
        )
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    vmware_dvs_host = VMwareDvsHost(module)
    vmware_dvs_host.process_state()


if __name__ == '__main__':
    main()
