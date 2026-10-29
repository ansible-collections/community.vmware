from __future__ import absolute_import, division, print_function
__metaclass__ = type

import unittest

from unittest import mock

from pyVmomi import vim

from ansible_collections.community.vmware.plugins.modules import vmware_guest_network


class TestGetVlanIdFromNetwork(unittest.TestCase):

    def setUp(self):
        self.helper = vmware_guest_network.PyVmomiHelper.__new__(vmware_guest_network.PyVmomiHelper)

    def _distributed_portgroup(self, vlan):
        network = mock.Mock(spec=vim.dvs.DistributedVirtualPortgroup)
        network.name = 'dvpg-vlan'
        network.config.defaultPortConfig.vlan = vlan
        # Reading the hosts of a distributed port group is what made the lookup slow.
        type(network).host = mock.PropertyMock(side_effect=AssertionError('host list must not be read'))
        return network

    def test_distributed_portgroup_vlan_id(self):
        vlan = vim.dvs.VmwareDistributedVirtualSwitch.VlanIdSpec(vlanId=42)
        network = self._distributed_portgroup(vlan)

        self.assertEqual(self.helper._get_vlanid_from_network(network), 42)

    def test_distributed_portgroup_trunk_vlan(self):
        vlan = vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec()
        network = self._distributed_portgroup(vlan)

        self.assertIsNone(self.helper._get_vlanid_from_network(network))

    def test_standard_portgroup_vlan_id(self):
        other = mock.Mock()
        other.spec.name = 'Other Network'
        other.spec.vlanId = 10
        match = mock.Mock()
        match.spec.name = 'VM Network'
        match.spec.vlanId = 20
        host = mock.Mock()
        host.config.network.portgroup = [other, match]
        network = mock.Mock(spec=vim.Network)
        network.name = 'VM Network'
        network.host = [host]

        self.assertEqual(self.helper._get_vlanid_from_network(network), 20)
