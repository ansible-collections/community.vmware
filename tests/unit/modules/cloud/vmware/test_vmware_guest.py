from __future__ import absolute_import, division, print_function
__metaclass__ = type

import unittest

from unittest import mock

from pyVmomi import vim

from ansible_collections.community.vmware.plugins.modules import vmware_guest


class TestConfigureNetwork(unittest.TestCase):

    def _helper(self, nic, network):
        helper = vmware_guest.PyVmomiHelper.__new__(vmware_guest.PyVmomiHelper)
        helper.module = mock.Mock()
        helper.module.fail_json.side_effect = AssertionError
        helper.params = {'networks': [{'name': 'VM Network'}], 'template': 'template-with-dvs-nic'}
        helper.device_helper = mock.Mock(nic_device_type={'vmxnet3': vim.vm.device.VirtualVmxnet3})
        helper.cache = mock.Mock()
        helper.cache.get_network.return_value = network
        helper.configspec = vim.vm.ConfigSpec()
        helper.relospec = vim.vm.RelocateSpec()
        helper.change_detected = False
        helper.sanitize_network_params = mock.Mock(return_value=[{'name': 'VM Network'}])
        helper.get_vm_network_interfaces = mock.Mock(return_value=[nic])
        helper.find_network_by_name = mock.Mock(return_value=[network])
        return helper

    def test_dvs_template_nic_to_standard_portgroup(self):
        """A template NIC on a distributed port group can move to a standard port group."""
        nic = vim.vm.device.VirtualVmxnet3()
        nic.deviceInfo = vim.Description(label='Network adapter 1', summary='DVSwitch: 50 2a 6e 1b')
        nic.connectable = vim.vm.device.VirtualDevice.ConnectInfo()
        nic.backing = vim.vm.device.VirtualEthernetCard.DistributedVirtualPortBackingInfo()
        nic.backing.port = vim.dvs.PortConnection(portgroupKey='dvportgroup-11', switchUuid='50 2a 6e 1b')
        # A standard vSwitch port group has no 'key' attribute.
        network = vim.Network('network-12')

        helper = self._helper(nic, network)
        helper.configure_network(vm_obj=None)

        self.assertTrue(helper.change_detected)
        self.assertEqual(len(helper.configspec.deviceChange), 1)
        backing = helper.configspec.deviceChange[0].device.backing
        self.assertIsInstance(backing, vim.vm.device.VirtualEthernetCard.NetworkBackingInfo)
        self.assertEqual(backing.network, network)
        self.assertEqual(backing.deviceName, 'VM Network')
