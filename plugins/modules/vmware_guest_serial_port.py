#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Anusha Hegde <anushah@vmware.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_guest_serial_port
short_description: Manage serial ports on an existing VM
description:
  - "This module can be used to manage serial ports on an existing VM"
options:
  name:
    description:
      - Name of the virtual machine.
      - This is a required parameter, if parameter C(uuid) or C(moid) is not supplied.
    type: str
  uuid:
    description:
      - UUID of the instance to manage the serial ports, this is VMware's unique identifier.
      - This is a required parameter, if parameter C(name) or C(moid) is not supplied.
    type: str
  moid:
    description:
      - Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.
      - This is required if C(name) or C(uuid) is not supplied.
    type: str
  use_instance_uuid:
    description:
      - Whether to use the VMware instance UUID rather than the BIOS UUID.
    default: false
    type: bool
  backings:
    type: list
    elements: dict
    description:
      - A list of backings for serial ports.
      - 'C(backing_type) (str): is required to add or reconfigure or remove an existing serial port.'
    required: True
    suboptions:
      backing_type:
        description:
          - Backing type is required for the serial ports to be added or reconfigured or removed.
        type: str
        required: True
        aliases:
          - type
      state:
        description:
          - C(state) is required to identify whether we are adding, modifying or removing the serial port.
          - If C(state) is set to C(present), a serial port will be added or modified.
          - If C(state) is set to C(absent), an existing serial port will be removed.
          - If an existing serial port to modify or remove, C(backing_type) and either of C(service_uri) or C(pipe_name)
            or C(device_name) or C(file_path) are required.
        choices:
          - present
          - absent
        type: str
        default: present
      yield_on_poll:
        description:
          - Enables CPU yield behavior.
        type: bool
        default: True
      pipe_name:
        description:
          - Pipe name for the host pipe.
          - Required when I(backing_type=pipe).
        type: str
      endpoint:
        description:
          - When you use serial port pipe backing to connect a virtual machine to another process, you must define the endpoints.
          - Required when I(backing_type=pipe).
        type: str
        choices:
          - client
          - server
        default: client
      no_rx_loss:
        description:
          - Enables optimized data transfer over the pipe.
          - Required when I(backing_type=pipe).
        type: bool
        default: False
      service_uri:
        description:
          - Identifies the local host or a system on the network, depending on the value of I(direction).
          - If you use the virtual machine as a server, the URI identifies the host on which the virtual machine runs.
          - In this case, the host name part of the URI should be empty, or it should specify the address of the local host.
          - If you use the virtual machine as a client, the URI identifies the remote system on the network.
          - Required when I(backing_type=network).
        type: str
      direction:
        description:
          - The direction of the connection.
          - Required when I(backing_type=network).
        type: str
        choices:
          - client
          - server
        default: client
      device_name:
        description:
          - Serial device absolutely path.
          - Required when I(backing_type=device).
        type: str
      file_path:
        description:
          - File path for the host file used in this backing. Fully qualified path is required, like <datastore_name>/<file_name>.
          - Required when I(backing_type=file).
        type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation
author:
  - Anusha Hegde (@anusha94)
'''

EXAMPLES = r'''
# Create serial ports
- name: Create multiple serial ports with Backing type - network, pipe, device and file
  community.vmware.vmware_guest_serial_port:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: "test_vm1"
    backings:
    - type: 'network'
      direction: 'client'
      service_uri: 'tcp://6000'
      yield_on_poll: True
    - type: 'pipe'
      pipe_name: 'serial_pipe'
      endpoint: 'client'
    - type: 'device'
      device_name: '/dev/char/serial/uart0'
    - type: 'file'
      file_path: '[datastore1]/file1'
      yield_on_poll:  True
    register: create_multiple_ports

# Modify existing serial port
- name: Modify Network backing type
  community.vmware.vmware_guest_serial_port:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: '{{ name }}'
    backings:
    - type: 'network'
      state: 'present'
      direction: 'server'
      service_uri: 'tcp://6000'
  delegate_to: localhost

# Remove serial port
- name: Remove pipe backing type
  community.vmware.vmware_guest_serial_port:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: '{{ name }}'
    backings:
    - type: 'pipe'
      state: 'absent'
  delegate_to: localhost

'''

RETURN = r'''
serial_port_data:
    description: metadata about the virtual machine's serial ports after managing them
    returned: always
    type: dict
    sample: [
        {
          "backing_type": "network",
          "direction": "client",
          "service_uri": "tcp://6000"
        },
        {
          "backing_type": "pipe",
          "direction": "server",
          "pipe_name": "serial pipe"
        },
    ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec, wait_for_task
from ansible.module_utils._text import to_native
try:
    from pyVmomi import vim
except ImportError:
    pass


class PyVmomiHelper(PyVmomi):
    """ This class is a helper to create easily VMware Spec for PyVmomiHelper """

    def __init__(self, module):
        super(PyVmomiHelper, self).__init__(module)
        self.change_applied = False   # a change was applied meaning at least one task succeeded
        self.config_spec = vim.vm.ConfigSpec()
        self.config_spec.deviceChange = []
        self.serial_ports = []

    def check_vm_state(self, vm_obj):
        """
        To add serial port, the VM must be in powered off state

        Input:
          - vm: Virtual Machine

        Output:
          - True if vm is in poweredOff state
          - module fails otherwise
        """
        if vm_obj.runtime.powerState == vim.VirtualMachinePowerState.poweredOff:
            return True
        self.module.fail_json(msg="A serial device cannot be added to a VM in the current state(" + vm_obj.runtime.powerState + "). "
                                  "Please use the vmware_guest_powerstate module to power off the VM")

    def get_serial_port_config_spec(self, vm_obj):
        """
        Variables changed:
          - self.config_spec
          - self.change_applied
        """
        # create serial config spec for adding, editing, removing
        for backing in self.params.get('backings'):
            serial_port = get_serial_port(vm_obj, backing)
            if serial_port:
                serial_spec = vim.vm.device.VirtualDeviceSpec()
                serial_spec.device = serial_port
                if diff_serial_port_config(serial_port, backing):
                    if backing['state'] == 'present':
                        # modify existing serial port
                        serial_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.edit
                        backing_type = backing.get('type', backing.get('backing_type'))
                        serial_spec.device.backing = self.get_backing_info(serial_port, backing, backing_type)
                        serial_spec.device.yieldOnPoll = backing['yield_on_poll']
                        self.change_applied = True
                        self.config_spec.deviceChange.append(serial_spec)
                    elif backing['state'] == 'absent':
                        # remove serial port
                        serial_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.remove
                        self.change_applied = True
                        self.config_spec.deviceChange.append(serial_spec)
            else:
                if backing['state'] == 'present':
                    # if serial port is None
                    # create a new serial port
                    serial_port_spec = self.create_serial_port(backing)
                    serial_port_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
                    self.serial_ports.append(serial_port_spec)
                    self.change_applied = True

    def reconfigure_vm_serial_port(self, vm_obj):
        """
        Reconfigure vm with new or modified serial port config spec
        """
        self.get_serial_port_config_spec(vm_obj)
        try:
            # configure create tasks first
            if self.serial_ports:
                for serial_port in self.serial_ports:
                    # each type of serial port is of config_spec.device = vim.vm.device.VirtualSerialPort() object type
                    # because serial ports differ in the backing types and config_spec.device has to be unique,
                    # we are creating a new spec for every create port configuration
                    spec = vim.vm.ConfigSpec()
                    spec.deviceChange.append(serial_port)
                    task = vm_obj.ReconfigVM_Task(spec=spec)
                    wait_for_task(task)
            task = vm_obj.ReconfigVM_Task(spec=self.config_spec)
            wait_for_task(task)
        except vim.fault.InvalidDatastorePath as e:
            self.module.fail_json(msg="Failed to configure serial port on given virtual machine due to invalid path: %s" % to_native(e.msg))
        except vim.fault.RestrictedVersion as e:
            self.module.fail_json(msg="Failed to reconfigure virtual machine due to product versioning restrictions: %s" % to_native(e.msg))
        if task.info.state == 'error':
            results = {'changed': self.change_applied, 'failed': True, 'msg': task.info.error.msg}
        else:
            serial_port_info = get_serial_port_info(vm_obj)
            results = {'changed': self.change_applied, 'failed': False, 'serial_port_info': serial_port_info}

        return results

    def set_network_backing(self, serial_port, backing_info):
        """
        Set the networking backing params
        """
        required_params = ['service_uri', 'direction']
        if set(required_params).issubset(backing_info.keys()):
            backing = serial_port.URIBackingInfo()
            backing.serviceURI = backing_info['service_uri']
            backing.direction = backing_info['direction']
        else:
            self.module.fail_json(msg="Failed to create a new serial port of network backing type due to insufficient parameters."
                                  + "The required parameters are service_uri and direction")
        return backing

    def set_pipe_backing(self, serial_port, backing_info):
        """
        Set the pipe backing params
        """
        required_params = ['pipe_name', 'endpoint']
        if set(required_params).issubset(backing_info.keys()):
            backing = serial_port.PipeBackingInfo()
            backing.pipeName = backing_info['pipe_name']
            backing.endpoint = backing_info['endpoint']
        else:
            self.module.fail_json(msg="Failed to create a new serial port of pipe backing type due to insufficient parameters."
                                  + "The required parameters are pipe_name and endpoint")

        # since no_rx_loss is an optional argument, so check if the key is present
        if 'no_rx_loss' in backing_info.keys() and backing_info['no_rx_loss']:
            backing.noRxLoss = backing_info['no_rx_loss']
        return backing

    def set_device_backing(self, serial_port, backing_info):
        """
        Set the device backing params
        """
        required_params = ['device_name']
        if set(required_params).issubset(backing_info.keys()):
            backing = serial_port.DeviceBackingInfo()
            backing.deviceName = backing_info['device_name']
        else:
            self.module.fail_json(msg="Failed to create a new serial port of device backing type due to insufficient parameters."
                                  + "The required parameters are device_name")
        return backing

    def set_file_backing(self, serial_port, backing_info):
        """
        Set the file backing params
        """
        required_params = ['file_path']
        if set(required_params).issubset(backing_info.keys()):
            backing = serial_port.FileBackingInfo()
            backing.fileName = backing_info['file_path']
        else:
            self.module.fail_json(msg="Failed to create a new serial port of file backing type due to insufficient parameters."
                                  + "The required parameters are file_path")
        return backing

    def get_backing_info(self, serial_port, backing, backing_type):
        """
        Returns the call to the appropriate backing function based on the backing type
        """
        switcher = {
            "network": self.set_network_backing,
            "pipe": self.set_pipe_backing,
            "device": self.set_device_backing,
            "file": self.set_file_backing
        }
        backing_func = switcher.get(backing_type, None)
        if backing_func is None:
            self.module.fail_json(msg="Failed to find a valid backing type. "
                                      "Provided '%s', should be one of [%s]" % (backing_type, ', '.join(switcher.keys())))
        return backing_func(serial_port, backing)

    def create_serial_port(self, backing):
        """
        Create a new serial port
        """
        serial_spec = vim.vm.device.VirtualDeviceSpec()
        serial_port = vim.vm.device.VirtualSerialPort()
        serial_port.yieldOnPoll = backing['yield_on_poll']
        backing_type = backing.get('type', backing.get('backing_type', None))
        serial_port.backing = self.get_backing_info(serial_port, backing, backing_type)
        serial_spec.device = serial_port
        return serial_spec


def get_serial_port(vm_obj, backing):
    """
    Return the serial port of specified backing type
    """
    serial_port = None
    backing_type_mapping = {
        'network': vim.vm.device.VirtualSerialPort.URIBackingInfo,
        'pipe': vim.vm.device.VirtualSerialPort.PipeBackingInfo,
        'device': vim.vm.device.VirtualSerialPort.DeviceBackingInfo,
        'file': vim.vm.device.VirtualSerialPort.FileBackingInfo
    }
    valid_params = backing.keys()
    for device in vm_obj.config.hardware.device:
        if isinstance(device, vim.vm.device.VirtualSerialPort):
            backing_type = backing.get('type', backing.get('backing_type', None))
            if isinstance(device.backing, backing_type_mapping[backing_type]):
                if 'service_uri' in valid_params:
                    # network backing type
                    serial_port = device
                    break
                if 'pipe_name' in valid_params:
                    # named pipe backing type
                    serial_port = device
                    break
                if 'device_name' in valid_params:
                    # physical serial device backing type
                    serial_port = device
                    break
                if 'file_path' in valid_params:
                    # file backing type
                    serial_port = device
                    break
                # if there is a backing of only one type, user need not provide secondary details like service_uri, pipe_name, device_name or file_path
                # we will match the serial port with backing type only
                # in this case, the last matching serial port will be returned
                serial_port = device
    return serial_port


def get_serial_port_info(vm_obj):
    """
    Get the serial port info
    """
    serial_port_info = []
    if vm_obj is None:
        return serial_port_info
    for port in vm_obj.config.hardware.device:
        backing = dict()
        if isinstance(port, vim.vm.device.VirtualSerialPort):
            if isinstance(port.backing, vim.vm.device.VirtualSerialPort.URIBackingInfo):
                backing['backing_type'] = 'network'
                backing['direction'] = port.backing.direction
                backing['service_uri'] = port.backing.serviceURI
            elif isinstance(port.backing, vim.vm.device.VirtualSerialPort.PipeBackingInfo):
                backing['backing_type'] = 'pipe'
                backing['pipe_name'] = port.backing.pipeName
                backing['endpoint'] = port.backing.endpoint
                backing['no_rx_loss'] = port.backing.noRxLoss
            elif isinstance(port.backing, vim.vm.device.VirtualSerialPort.DeviceBackingInfo):
                backing['backing_type'] = 'device'
                backing['device_name'] = port.backing.deviceName
            elif isinstance(port.backing, vim.vm.device.VirtualSerialPort.FileBackingInfo):
                backing['backing_type'] = 'file'
                backing['file_path'] = port.backing.fileName
            else:
                continue
            serial_port_info.append(backing)
    return serial_port_info


def diff_serial_port_config(serial_port, backing):
    if backing['state'] == 'present':
        if 'yield_on_poll' in backing:
            if serial_port.yieldOnPoll != backing['yield_on_poll']:
                return True
        if backing['service_uri'] is not None:
            if serial_port.backing.serviceURI != backing['service_uri'] or \
                    serial_port.backing.direction != backing['direction']:
                return True
        if backing['pipe_name'] is not None:
            if serial_port.backing.pipeName != backing['pipe_name'] or \
                    serial_port.backing.endpoint != backing['endpoint'] or \
                    serial_port.backing.noRxLoss != backing['no_rx_loss']:
                return True
        if backing['device_name'] is not None:
            if serial_port.backing.deviceName != backing['device_name']:
                return True
        if backing['file_path'] is not None:
            if serial_port.backing.fileName != backing['file_path']:
                return True

    if backing['state'] == 'absent':
        if backing['service_uri'] is not None:
            if serial_port.backing.serviceURI == backing['service_uri']:
                return True
        if backing['pipe_name'] is not None:
            if serial_port.backing.pipeName == backing['pipe_name']:
                return True
        if backing['device_name'] is not None:
            if serial_port.backing.deviceName == backing['device_name']:
                return True
        if backing['file_path'] is not None:
            if serial_port.backing.fileName == backing['file_path']:
                return True

    return False


def main():
    """
    Main method
    """
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        uuid=dict(type='str'),
        moid=dict(type='str'),
        use_instance_uuid=dict(type='bool', default=False),
        backings=dict(type='list', elements='dict', required=True,
                      options=dict(
                          backing_type=dict(type='str', required=True, aliases=['type']),
                          pipe_name=dict(type='str', default=None),
                          endpoint=dict(type='str', choices=['client', 'server'], default='client'),
                          no_rx_loss=dict(type='bool', default=False),
                          service_uri=dict(type='str', default=None),
                          direction=dict(type='str', choices=['client', 'server'], default='client'),
                          device_name=dict(type='str', default=None),
                          file_path=dict(type='str', default=None),
                          yield_on_poll=dict(type='bool', default=True),
                          state=dict(type='str', choices=['present', 'absent'], default='present')
                      ),
                      required_if=[
                          ['backing_type', 'pipe', ['pipe_name', 'endpoint', 'no_rx_loss']],
                          ['backing_type', 'network', ['service_uri', 'direction']],
                          ['backing_type', 'device', ['device_name']],
                          ['backing_type', 'file', ['file_path']]
                      ]),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['name', 'uuid', 'moid']
        ],
        mutually_exclusive=[
            ['name', 'uuid', 'moid']
        ],
    )
    result = {'failed': False, 'changed': False}

    pyv = PyVmomiHelper(module)
    # Check if the VM exists before continuing
    vm_obj = pyv.get_vm()

    if vm_obj:
        proceed = pyv.check_vm_state(vm_obj)
        if proceed:
            result = pyv.reconfigure_vm_serial_port(vm_obj)

    else:
        # We are unable to find the virtual machine user specified
        # Bail out
        vm_id = (module.params.get('name') or module.params.get('uuid') or module.params.get('vm_id'))
        module.fail_json(msg="Unable to manage serial ports for non-existing"
                             " virtual machine '%s'." % vm_id)

    if result['failed']:
        module.fail_json(**result)
    else:
        module.exit_json(**result)


if __name__ == '__main__':
    main()
