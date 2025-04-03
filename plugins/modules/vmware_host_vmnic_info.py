#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# Copyright: (c) 2018, Christian Kotte <christian.kotte@gmx.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_vmnic_info
short_description: Gathers info about vmnics available on the given ESXi host
description:
- This module can be used to gather information about vmnics available on the given ESXi host.
- If O(cluster_name) is provided, then vmnic information about all hosts from given cluster will be returned.
- If O(esxi_hostname) is provided, then vmnic information about given host system will be returned.
author:
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)
options:
  capabilities:
    description:
    - Gather information about general capabilities (Auto negotiation, Wake On LAN, and Network I/O Control).
    type: bool
    default: false
  directpath_io:
    description:
    - Gather information about DirectPath I/O capabilities and configuration.
    type: bool
    default: false
  sriov:
    description:
    - Gather information about SR-IOV capabilities and configuration.
    type: bool
    default: false
  esxi_hostname:
    description:
    - Name of the host system to work with.
    - Vmnic information about this ESXi server will be returned.
    - This parameter is required if O(cluster_name) is not specified.
    type: str
  cluster_name:
    description:
    - Name of the cluster from which all host systems will be used.
    - Vmnic information about each ESXi server will be returned for the given cluster.
    - This parameter is required if O(esxi_hostname) is not specified.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather info about vmnics of all ESXi Host in the given Cluster
  community.vmware.vmware_host_vmnic_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
  register: cluster_host_vmnics

- name: Gather info about vmnics of an ESXi Host
  community.vmware.vmware_host_vmnic_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: host_vmnics
'''

RETURN = r'''
hosts_vmnics_info:
    description:
    - dict with hostname as key and dict with vmnics information as value.
    - for C(num_vmnics), only NICs starting with vmnic are counted. NICs like vusb* are not counted.
    returned: hosts_vmnics_info
    type: dict
    sample:
        {
            "10.76.33.204": {
                "all": [
                    "vmnic0",
                    "vmnic1"
                ],
                "available": [],
                "dvswitch": {
                    "dvs_0002": [
                        "vmnic1"
                    ]
                },
                "num_vmnics": 2,
                "used": [
                    "vmnic1",
                    "vmnic0"
                ],
                "vmnic_details": [
                    {
                        "actual_duplex": "Full Duplex",
                        "actual_speed": 10000,
                        "adapter": "Intel(R) 82599 10 Gigabit Dual Port Network Connection",
                        "configured_duplex": "Auto negotiate",
                        "configured_speed": "Auto negotiate",
                        "device": "vmnic0",
                        "driver": "ixgbe",
                        "lldp_info": {
                            "Aggregated Port ID": "0",
                            "Aggregation Status": "1",
                            "Enabled Capabilities": {
                                "_vimtype": "vim.host.PhysicalNic.CdpDeviceCapability",
                                "host": false,
                                "igmpEnabled": false,
                                "networkSwitch": false,
                                "repeater": false,
                                "router": true,
                                "sourceRouteBridge": false,
                                "transparentBridge": true
                            },
                            "MTU": "9216",
                            "Port Description": "switch port description",
                            "Samples": 18814,
                            "System Description": "omitted from output",
                            "System Name": "sw1",
                            "TimeOut": 30,
                            "Vlan ID": "1"
                        },
                        "location": "0000:01:00.0",
                        "mac": "aa:bb:cc:dd:ee:ff",
                        "status": "Connected",
                    },
                    {
                        "actual_duplex": "Full Duplex",
                        "actual_speed": 10000,
                        "adapter": "Intel(R) 82599 10 Gigabit Dual Port Network Connection",
                        "configured_duplex": "Auto negotiate",
                        "configured_speed": "Auto negotiate",
                        "device": "vmnic1",
                        "driver": "ixgbe",
                        "lldp_info": "N/A",
                        "location": "0000:01:00.1",
                        "mac": "ab:ba:cc:dd:ee:ff",
                        "status": "Connected",
                    },
                ],
                "vswitch": {
                    "vSwitch0": [
                        "vmnic0"
                    ]
                }
            }
        }
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, get_all_objs
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class HostVmnicMgr(PyVmomi):
    """Class to manage vmnic info"""

    def __init__(self, module):
        super(HostVmnicMgr, self).__init__(module)
        self.capabilities = self.params.get('capabilities')
        self.directpath_io = self.params.get('directpath_io')
        self.sriov = self.params.get('sriov')
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)
        if not self.hosts:
            self.module.fail_json(msg="Failed to find host system.")

    def find_dvs_by_uuid(self, uuid=None):
        """Find DVS by it's UUID"""
        dvs_obj = None
        if uuid is None:
            return dvs_obj

        dvswitches = get_all_objs(self.content, [vim.DistributedVirtualSwitch])
        for dvs in dvswitches:
            if dvs.uuid == uuid:
                dvs_obj = dvs
                break

        return dvs_obj

    def gather_host_vmnic_info(self):
        """Gather vmnic info"""
        hosts_vmnic_info = {}
        for host in self.hosts:
            host_vmnic_info = dict(all=[], available=[], used=[], vswitch=dict(), dvswitch=dict())
            host_nw_system = host.configManager.networkSystem
            if host_nw_system:
                nw_config = host_nw_system.networkConfig
                vmnics = [pnic.device for pnic in nw_config.pnic if pnic.device.startswith('vmnic')]
                host_vmnic_info['all'] = [pnic.device for pnic in nw_config.pnic]
                host_vmnic_info['num_vmnics'] = len(vmnics)
                host_vmnic_info['vmnic_details'] = []
                for pnic in host.config.network.pnic:
                    pnic_info = dict()
                    if pnic.device.startswith('vmnic'):
                        if pnic.pci:
                            pnic_info['location'] = pnic.pci
                            for pci_device in host.hardware.pciDevice:
                                if pci_device.id == pnic.pci:
                                    pnic_info['adapter'] = pci_device.vendorName + ' ' + pci_device.deviceName
                                    break
                        else:
                            pnic_info['location'] = 'PCI'
                        pnic_info['device'] = pnic.device
                        pnic_info['driver'] = pnic.driver
                        if pnic.linkSpeed:
                            pnic_info['status'] = 'Connected'
                            pnic_info['actual_speed'] = pnic.linkSpeed.speedMb
                            pnic_info['actual_duplex'] = 'Full Duplex' if pnic.linkSpeed.duplex else 'Half Duplex'
                            try:
                                network_hint = host_nw_system.QueryNetworkHint(pnic.device)
                                for hint in self.to_json(network_hint):
                                    if hint.get('lldpInfo'):
                                        pnic_info['lldp_info'] = {x['key']: x['value'] for x in hint['lldpInfo'].get('parameter')}
                                    else:
                                        pnic_info['lldp_info'] = 'N/A'
                                    if hint.get('connectedSwitchPort'):
                                        pnic_info['cdp_info'] = hint.get('connectedSwitchPort')
                                    else:
                                        pnic_info['cdp_info'] = 'N/A'
                            except (vmodl.fault.HostNotConnected, vmodl.fault.HostNotReachable):
                                pnic_info['lldp_info'] = 'N/A'
                                pnic_info['cdp_info'] = 'N/A'
                        else:
                            pnic_info['status'] = 'Disconnected'
                            pnic_info['actual_speed'] = 'N/A'
                            pnic_info['actual_duplex'] = 'N/A'
                            pnic_info['lldp_info'] = 'N/A'
                            pnic_info['cdp_info'] = 'N/A'
                        if pnic.spec.linkSpeed:
                            pnic_info['configured_speed'] = pnic.spec.linkSpeed.speedMb
                            pnic_info['configured_duplex'] = 'Full Duplex' if pnic.spec.linkSpeed.duplex else 'Half Duplex'
                        else:
                            pnic_info['configured_speed'] = 'Auto negotiate'
                            pnic_info['configured_duplex'] = 'Auto negotiate'
                        pnic_info['mac'] = pnic.mac
                        # General NIC capabilities
                        if self.capabilities:
                            pnic_info['nioc_status'] = 'Allowed' if pnic.resourcePoolSchedulerAllowed else 'Not allowed'
                            pnic_info['auto_negotiation_supported'] = pnic.autoNegotiateSupported
                            pnic_info['wake_on_lan_supported'] = pnic.wakeOnLanSupported
                        # DirectPath I/O and SR-IOV capabilities and configuration
                        if self.directpath_io:
                            pnic_info['directpath_io_supported'] = pnic.vmDirectPathGen2Supported
                        if self.directpath_io or self.sriov:
                            if pnic.pci:
                                for pci_device in host.configManager.pciPassthruSystem.pciPassthruInfo:
                                    if pci_device.id == pnic.pci:
                                        if self.directpath_io:
                                            pnic_info['passthru_enabled'] = pci_device.passthruEnabled
                                            pnic_info['passthru_capable'] = pci_device.passthruCapable
                                            pnic_info['passthru_active'] = pci_device.passthruActive
                                        if self.sriov:
                                            try:
                                                if pci_device.sriovCapable:
                                                    pnic_info['sriov_status'] = (
                                                        'Enabled' if pci_device.sriovEnabled else 'Disabled'
                                                    )
                                                    pnic_info['sriov_active'] = \
                                                        pci_device.sriovActive
                                                    pnic_info['sriov_virt_functions'] = \
                                                        pci_device.numVirtualFunction
                                                    pnic_info['sriov_virt_functions_requested'] = \
                                                        pci_device.numVirtualFunctionRequested
                                                    pnic_info['sriov_virt_functions_supported'] = \
                                                        pci_device.maxVirtualFunctionSupported
                                                else:
                                                    pnic_info['sriov_status'] = 'Not supported'
                                            except AttributeError:
                                                pnic_info['sriov_status'] = 'Not supported'
                        host_vmnic_info['vmnic_details'].append(pnic_info)

                vswitch_vmnics = []
                proxy_switch_vmnics = []
                if nw_config.vswitch:
                    for vswitch in nw_config.vswitch:
                        host_vmnic_info['vswitch'][vswitch.name] = []
                        # Workaround for "AttributeError: 'NoneType' object has no attribute 'nicDevice'"
                        # this issue doesn't happen every time; vswitch.spec.bridge.nicDevice exists!
                        try:
                            for vnic in vswitch.spec.bridge.nicDevice:
                                vswitch_vmnics.append(vnic)
                                host_vmnic_info['vswitch'][vswitch.name].append(vnic)
                        except AttributeError:
                            pass

                if nw_config.proxySwitch:
                    for proxy_config in nw_config.proxySwitch:
                        dvs_obj = self.find_dvs_by_uuid(uuid=proxy_config.uuid)
                        if dvs_obj:
                            host_vmnic_info['dvswitch'][dvs_obj.name] = []
                        for proxy_nic in proxy_config.spec.backing.pnicSpec:
                            proxy_switch_vmnics.append(proxy_nic.pnicDevice)
                            if dvs_obj:
                                host_vmnic_info['dvswitch'][dvs_obj.name].append(proxy_nic.pnicDevice)

                used_vmics = proxy_switch_vmnics + vswitch_vmnics
                host_vmnic_info['used'] = used_vmics
                host_vmnic_info['available'] = [pnic.device for pnic in nw_config.pnic if pnic.device not in used_vmics]

            hosts_vmnic_info[host.name] = host_vmnic_info
        return hosts_vmnic_info


def main():
    """Main"""
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str', required=False),
        esxi_hostname=dict(type='str', required=False),
        capabilities=dict(type='bool', required=False, default=False),
        directpath_io=dict(type='bool', required=False, default=False),
        sriov=dict(type='bool', required=False, default=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True,
    )

    host_vmnic_mgr = HostVmnicMgr(module)
    module.exit_json(changed=False, hosts_vmnics_info=host_vmnic_mgr.gather_host_vmnic_info())


if __name__ == "__main__":
    main()
