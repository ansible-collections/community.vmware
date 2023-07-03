

community.vmware.vmware_dvswitch_uplink_pg module -- Manage uplink portproup configuration of a Distributed Switch
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_dvswitch_uplink_pg`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure the uplink portgroup of a Distributed Switch.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced:
      .. _parameter-port_policy:

      **advanced**

      aliases: port_policy

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the advanced policy settings for the uplink portgroup.


      Default: :literal:`{"block\_override": true, "netflow\_override": false, "port\_config\_reset\_at\_disconnect": true, "traffic\_filter\_override": false, "vendor\_config\_override": false, "vlan\_override": false}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced/block_override:
      .. _parameter-port_policy/block_override:

      **block_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the block policy can be changed per port.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced/netflow_override:
      .. _parameter-port_policy/netflow_override:

      **netflow_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the NetFlow policy can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced/port_config_reset_at_disconnect:
      .. _parameter-port_policy/port_config_reset_at_disconnect:

      **port_config_reset_at_disconnect**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the configuration of a port is reset automatically after disconnect.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced/traffic_filter_override:
      .. _parameter-port_policy/traffic_filter_override:

      **traffic_filter_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the traffic filter can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced/vendor_config_override:
      .. _parameter-port_policy/vendor_config_override:

      **vendor_config_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the vendor config can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced/vlan_override:
      .. _parameter-port_policy/vlan_override:

      **vlan_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the vlan can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-block_all_ports:

      **block_all_ports**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if all ports are blocked on the uplink portgroup.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-description:

      **description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The description of the uplink portgroup.



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

      .. _parameter-lacp:

      **lacp**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the LACP settings for the uplink portgroup.

      The options are only used if the LACP support mode is set to 'basic'.


      Default: :literal:`{"mode": "passive", "status": "disabled"}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-lacp/mode:

      **mode**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The negotiating state of the uplinks/ports.


      Choices:

      - :literal:`"active"`
      - :literal:`"passive"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-lacp/status:

      **status**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Indicates if LACP is enabled.


      Choices:

      - :literal:`"enabled"`
      - :literal:`"disabled"` ← (default)




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The name of the uplink portgroup.

      The current name will be used if not specified.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-netflow_enabled:

      **netflow_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if NetFlow is enabled on the uplink portgroup.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



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

      .. _parameter-dvswitch:
      .. _parameter-switch:

      **switch**

      aliases: dvswitch

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the Distributed Switch.



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

      .. _parameter-vlan_trunk_range:

      **vlan_trunk_range**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      The VLAN trunk range that should be configured with the uplink portgroup.

      This can be a combination of multiple ranges and numbers, example: [ 2-3967, 4049-4092 ].


      Default: :literal:`["0-4094"]`




Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Configure Uplink portgroup
      community.vmware.vmware_dvswitch_uplink_pg:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcsa_username }}'
        password: '{{ vcsa_password }}'
        switch: dvSwitch
        name: dvSwitch-DVUplinks
        advanced:
          port_config_reset_at_disconnect: true
          block_override: true
          vendor_config_override: false
          vlan_override: false
          netflow_override: false
          traffic_filter_override: false
        vlan_trunk_range:
          - '0-4094'
        netflow_enabled: false
        block_all_ports: false
      delegate_to: localhost

    - name: Enabled LACP on Uplink portgroup
      community.vmware.vmware_dvswitch_uplink_pg:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcsa_username }}'
        password: '{{ vcsa_password }}'
        switch: dvSwitch
        lacp:
          status: enabled
          mode: active
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

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      information about performed operation


      Returned: always

      Sample: :literal:`"{'adv\_block\_ports': True, 'adv\_netflow': False, 'adv\_reset\_at\_disconnect': True, 'adv\_traffic\_filtering': False, 'adv\_vendor\_conf': False, 'adv\_vlan': False, 'block\_all\_ports': False, 'changed': False, 'description': None, 'dvswitch': 'dvSwitch', 'lacp\_status': 'disabled', 'lacp\_status\_previous': 'enabled', 'name': 'dvSwitch-DVUplinks', 'netflow\_enabled': False, 'result': 'Uplink portgroup already configured properly', 'vlan\_trunk\_range': ['2-3967', '4049-4092']}"`




Authors
~~~~~~~

- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

