

community.vmware.vmware_vmkernel module -- Manages a VMware VMkernel Adapter of an ESXi host.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_vmkernel`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage the VMKernel adapters / VMKernel network interfaces of an ESXi host.
- The module assumes that the host is already configured with the Port Group in case of a vSphere Standard Switch (vSS).
- The module assumes that the host is already configured with the Distributed Port Group in case of a vSphere Distributed Switch (vDS).
- The module automatically migrates the VMKernel adapter from vSS to vDS or vice versa if present.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-device:

      **device**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Search VMkernel adapter by device name.

      The parameter is required only in case of \ :literal:`type`\  is set to \ :literal:`dhcp`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-dvswitch:
      .. _parameter-dvswitch_name:

      **dvswitch_name**

      aliases: dvswitch

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The name of the vSphere Distributed Switch (vDS) where to add the VMKernel interface.

      Required parameter only if \ :literal:`state`\  is set to \ :literal:`present`\ .

      Optional parameter from version 2.8 and onwards.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_ft:

      **enable_ft**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable Fault Tolerance traffic on the VMKernel adapter.

      This option is only allowed if the default TCP/IP stack is used.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_mgmt:

      **enable_mgmt**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable Management traffic on the VMKernel adapter.

      This option is only allowed if the default TCP/IP stack is used.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_provisioning:

      **enable_provisioning**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable Provisioning traffic on the VMKernel adapter.

      This option is only allowed if the default TCP/IP stack is used.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_replication:

      **enable_replication**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable vSphere Replication traffic on the VMKernel adapter.

      This option is only allowed if the default TCP/IP stack is used.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_replication_nfc:

      **enable_replication_nfc**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable vSphere Replication NFC traffic on the VMKernel adapter.

      This option is only allowed if the default TCP/IP stack is used.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_vmotion:

      **enable_vmotion**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable vMotion traffic on the VMKernel adapter.

      This option is only allowed if the default TCP/IP stack is used.

      You cannot enable vMotion on an additional adapter if you already have an adapter with the vMotion TCP/IP stack configured.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_vsan:

      **enable_vsan**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable VSAN traffic on the VMKernel adapter.

      This option is only allowed if the default TCP/IP stack is used.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of ESXi host to which VMKernel is to be managed.

      From version 2.5 onwards, this parameter is required.



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

      .. _parameter-mtu:

      **mtu**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The MTU for the VMKernel interface.

      The default value of 1500 is valid from version 2.5 and onwards.


      Default: :literal:`1500`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network:

      **network**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      A dictionary of network details.


      Default: :literal:`{"tcpip\_stack": "default", "type": "static"}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network/default_gateway:

      **default_gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Default gateway (Override default gateway for this adapter).



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network/ip_address:

      **ip_address**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Static IP address.

      Required if \ :literal:`type`\  is set to \ :literal:`static`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network/subnet_mask:

      **subnet_mask**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Static netmask required.

      Required if \ :literal:`type`\  is set to \ :literal:`static`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network/tcpip_stack:

      **tcpip_stack**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The TCP/IP stack for the VMKernel interface.


      Choices:

      - :literal:`"default"` ← (default)
      - :literal:`"provisioning"`
      - :literal:`"vmotion"`
      - :literal:`"vxlan"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network/type:

      **type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of IP assignment.


      Choices:

      - :literal:`"static"` ← (default)
      - :literal:`"dhcp"`




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

      .. _parameter-portgroup:
      .. _parameter-portgroup_name:

      **portgroup_name**

      aliases: portgroup

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the port group for the VMKernel interface.



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

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`present`\ , the VMKernel adapter will be created with the given specifications.

      If set to \ :literal:`absent`\ , the VMKernel adapter will be removed.

      If set to \ :literal:`present`\  and VMKernel adapter exists, the configurations will be updated.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



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

      .. _parameter-vswitch:
      .. _parameter-vswitch_name:

      **vswitch_name**

      aliases: vswitch

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The name of the vSwitch where to add the VMKernel interface.

      Required parameter only if \ :literal:`state`\  is set to \ :literal:`present`\ .

      Optional parameter from version 2.5 and onwards.





Notes
-----

.. note::
   - The option \ :literal:`device`\  need to be used with DHCP because otherwise it's not possible to check if a VMkernel device is already present
   - You can only change from DHCP to static, and vSS to vDS, or vice versa, in one step, without creating a new device, with \ :literal:`device`\  specified.
   - You can only create the VMKernel adapter on a vDS if authenticated to vCenter and not if authenticated to ESXi.
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    -  name: Add Management vmkernel port using static network type
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0001
          network:
            type: 'static'
            ip_address: 192.168.127.10
            subnet_mask: 255.255.255.0
          state: present
          enable_mgmt: true
       delegate_to: localhost

    -  name: Add Management vmkernel port using DHCP network type
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0002
          state: present
          network:
            type: 'dhcp'
          enable_mgmt: true
       delegate_to: localhost

    -  name: Change IP allocation from static to dhcp
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0002
          state: present
          device: vmk1
          network:
            type: 'dhcp'
          enable_mgmt: true
       delegate_to: localhost

    -  name: Delete VMkernel port
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0002
          state: absent
       delegate_to: localhost

    -  name: Add Management vmkernel port to Distributed Switch
       community.vmware.vmware_vmkernel:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          dvswitch_name: dvSwitch1
          portgroup_name: dvPG_0001
          network:
            type: 'static'
            ip_address: 192.168.127.10
            subnet_mask: 255.255.255.0
          state: present
          enable_mgmt: true
       delegate_to: localhost

    -  name: Add vMotion vmkernel port with vMotion TCP/IP stack
       community.vmware.vmware_vmkernel:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          dvswitch_name: dvSwitch1
          portgroup_name: dvPG_0001
          network:
            type: 'static'
            ip_address: 192.168.127.10
            subnet_mask: 255.255.255.0
            tcpip_stack: vmotion
          state: present
       delegate_to: localhost





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

      .. _return-result:

      **result**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about VMKernel name


      Returned: always

      Sample: :literal:`{"changed": false, "device": "vmk1", "ipv4": "static", "ipv4\_gw": "No override", "ipv4\_ip": "192.168.1.15", "ipv4\_sm": "255.255.255.0", "msg": "VMkernel Adapter already configured properly", "mtu": 9000, "services": "vMotion", "switch": "vDS"}`




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

