

community.vmware.vmware_guest_network module -- Manage network adapters of specified virtual machine in given vCenter infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_network`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is used to add, reconfigure, remove network adapter of given virtual machine.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-allow_guest_os_mtu_change:

      **allow_guest_os_mtu_change**

      :literal:`boolean`

      added in community.vmware 2.3.0


      .. raw:: html

        </div></div>

    - 
      Allows the guest OS to change the MTU on a SR-IOV network adapter.

      This option is only compatible for SR-IOV network adapters.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster:

      **cluster**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of cluster where VM belongs to.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-connected:

      **connected**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If NIC should be connected to the network.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Datacenter the VM belongs to.


      Default: :literal:`"ha-datacenter"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-device_type:

      **device_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of virtual network device.

      Valid choices are - \ :literal:`e1000`\ , \ :literal:`e1000e`\ , \ :literal:`pcnet32`\ , \ :literal:`vmxnet2`\ , \ :literal:`vmxnet3`\  (default), \ :literal:`sriov`\ , \ :literal:`pvrdma`\ .


      Default: :literal:`"vmxnet3"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directpath_io:

      **directpath_io**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable Universal Pass-through (UPT).

      Only compatible with the \ :literal:`vmxnet3`\  device type.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The hostname of the ESXi host where the VM belongs to.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Folder location of given VM, this is only required when there's multiple VM's with the same name.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-force:

      **force**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Force adapter creation even if an existing adapter is attached to the same network.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-gather_network_facts:
      .. _parameter-gather_network_info:

      **gather_network_info**

      aliases: gather_network_facts

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Return information about current guest network adapters.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guest_control:

      **guest_control**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enables guest control over whether the connectable device is connected.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hostname:

      **hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The hostname or IP address of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_HOST`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-label:

      **label**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Label of the NIC that should be altered. \ :literal:`mac\_address`\  or \ :literal:`label`\  should be set to get the corresponding device to reconfigure.

      Alter the name of the network adapter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mac_address:

      **mac_address**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      MAC address of the NIC that should be altered, if a MAC address is not supplied a new nic will be created.

      Required when \ :emphasis:`state=absent`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-moid:

      **moid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.

      Required if \ :literal:`uuid`\  or \ :literal:`name`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of virtual machine

      Required if \ :literal:`uuid`\  or \ :literal:`moid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_name:

      **network_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of network in vSphere.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-pass:
      .. _parameter-password:
      .. _parameter-pwd:

      **password**

      aliases: pass, pwd

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The password of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PASSWORD`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-physical_function_backing:

      **physical_function_backing**

      :literal:`string`

      added in community.vmware 2.3.0


      .. raw:: html

        </div></div>

    - 
      If set, specifies the PCI ID of the physical function to use as backing for a SR-IOV network adapter.

      This option is only compatible for SR-IOV network adapters.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port:

      **port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The port number of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PORT`\  will be used instead.

      Environment variable support added in Ansible 2.6.


      Default: :literal:`443`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_host:

      **proxy_host**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Address of a proxy that will receive all HTTPS requests and relay them.

      The format is a hostname or a IP.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PROXY\_HOST`\  will be used instead.

      This feature depends on a version of pyvmomi greater than v6.7.1.2018.12



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_port:

      **proxy_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Port of the HTTP proxy that will receive all HTTPS requests and relay them.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PROXY\_PORT`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-pvrdma_device_protocol:

      **pvrdma_device_protocol**

      :literal:`string`

      added in community.vmware 3.3.0


      .. raw:: html

        </div></div>

    - 
      The PVRDMA device protocol used. Valid choices are - \ :literal:`rocev1`\ , \ :literal:`rocev2`\ .

      This parameter is only used on the VM with hardware version \>=14 and \<= 19.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-start_connected:

      **start_connected**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If NIC should be connected to network on startup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      NIC state.

      When \ :literal:`state=present`\ , a nic will be added if a mac address or label does not previously exists or is unset.

      When \ :literal:`state=absent`\ , the \ :emphasis:`mac\_address`\  parameter has to be set.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-switch:

      **switch**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the (dv)switch for destination network, this is only required for dvswitches.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-use_instance_uuid:

      **use_instance_uuid**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to use the VMware instance UUID rather than the BIOS UUID.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-admin:
      .. _parameter-user:
      .. _parameter-username:

      **username**

      aliases: admin, user

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The username of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_USER`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-uuid:

      **uuid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      vm uuid

      Required if \ :literal:`name`\  or \ :literal:`moid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allows connection when SSL certificates are not valid. Set to \ :literal:`false`\  when certificates are not trusted.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_VALIDATE\_CERTS`\  will be used instead.

      Environment variable support added in Ansible 2.6.

      If set to \ :literal:`true`\ , please make sure Python \>= 2.7.9 is installed on the given machine.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-virtual_function_backing:

      **virtual_function_backing**

      :literal:`string`

      added in community.vmware 2.3.0


      .. raw:: html

        </div></div>

    - 
      If set, specifies the PCI ID of the physical function to use as backing for a SR-IOV network adapter.

      This option is only compatible for SR-IOV network adapters.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vlan_id:

      **vlan_id**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      VLAN id associated with the network.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wake_onlan:

      **wake_onlan**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable wake on LAN.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`





Notes
-----

- For backwards compatibility network\_data is returned when using the gather\_network\_info parameter
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: change network for 00:50:56:11:22:33 on vm01.domain.fake
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: vm01.domain.fake
        mac_address: 00:50:56:11:22:33
        network_name: admin-network
        state: present

    - name: add a nic on network with vlan id 2001 for 422d000d-2000-ffff-0000-b00000000000
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        uuid: 422d000d-2000-ffff-0000-b00000000000
        vlan_id: 2001

    - name: remove nic with mac 00:50:56:11:22:33 from vm01.domain.fake
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        mac_address: 00:50:56:11:22:33
        name: vm01.domain.fake
        state: absent

    - name: add multiple nics to vm01.domain.fake
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: vm01.domain.fake
        state: present
        vlan_id: "{{ item.vlan_id | default(omit) }}"
        network_name: "{{ item.network_name | default(omit) }}"
        connected: "{{ item.connected | default(omit) }}"
      loop:
        - vlan_id: 2000
          connected: false
        - network_name: guest-net
          connected: true





Return Values
-------------
The following are the fields unique to this module:

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-network_data:

      **network_data**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      For backwards compatibility, metadata about the virtual machine network adapters


      Returned: when using gather\_network\_info parameter

      Sample: :literal:`{"network\_data": {"0": {"allow\_guest\_ctl": true, "connected": true, "device\_type": "vmxnet3", "label": "Network adapter 2", "mac\_addr": "00:50:56:AA:AA:AA", "mac\_address": "00:50:56:AA:AA:AA", "name": "admin-net", "network\_name": "admin-net", "start\_connected": true, "switch": "vSwitch0", "unit\_number": 8, "vlan\_id": 10, "wake\_onlan": false}, "1": {"allow\_guest\_ctl": true, "connected": true, "device\_type": "vmxnet3", "label": "Network adapter 1", "mac\_addr": "00:50:56:BB:BB:BB", "mac\_address": "00:50:56:BB:BB:BB", "name": "guest-net", "network\_name": "guest-net", "start\_connected": true, "switch": "vSwitch0", "unit\_number": 7, "vlan\_id": 10, "wake\_onlan": true}}}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-network_info:

      **network_info**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine network adapters


      Returned: always

      Sample: :literal:`{"network\_info": [{"allow\_guest\_ctl": true, "connected": true, "device\_type": "vmxnet3", "label": "Network adapter 2", "mac\_address": "00:50:56:AA:AA:AA", "network\_name": "admin-net", "start\_connected": true, "switch": "vSwitch0", "unit\_number": 8, "vlan\_id": 10, "wake\_onlan": false}, {"allow\_guest\_ctl": true, "connected": true, "device\_type": "vmxnet3", "label": "Network adapter 1", "mac\_address": "00:50:56:BB:BB:BB", "network\_name": "guest-net", "start\_connected": true, "switch": "vSwitch0", "unit\_number": 7, "vlan\_id": 10, "wake\_onlan": true}]}`




Authors
~~~~~~~

- Diane Wang (@Tomorrow9) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

