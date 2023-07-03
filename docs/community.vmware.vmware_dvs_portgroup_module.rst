

community.vmware.vmware_dvs_portgroup module -- Create or remove a Distributed vSwitch portgroup.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_dvs_portgroup`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Create or remove a Distributed vSwitch portgroup.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

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

      .. _parameter-in_traffic_shaping:

      **in_traffic_shaping**

      :literal:`dictionary`

      added in community.vmware 2.3.0


      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the ingress traffic shaping settings for the portgroup.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-in_traffic_shaping/average_bandwidth:

      **average_bandwidth**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Establishes the number of bits per second to allow across a port, averaged over time, that is, the allowed average load.

      Ignored if \ :literal:`inherited`\  is true.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-in_traffic_shaping/burst_size:

      **burst_size**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of bits per second to allow across a port when it is sending/sending or receiving a burst of traffic.

      Ignored if \ :literal:`inherited`\  is true.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-in_traffic_shaping/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether ingress traffic shaping is activated or not.

      Ignored if \ :literal:`inherited`\  is true.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-in_traffic_shaping/inherited:

      **inherited**

      :literal:`boolean` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Inherit the settings from the switch or not.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-in_traffic_shaping/peak_bandwidth:

      **peak_bandwidth**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of bytes to allow in a burst.

      Ignored if \ :literal:`inherited`\  is true.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mac_learning:

      **mac_learning**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Dictionary which configures MAC learning for portgroup.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mac_learning/allow_unicast_flooding:

      **allow_unicast_flooding**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      The flag to allow flooding of unlearned MAC for ingress traffic.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mac_learning/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      The flag to indicate if source MAC address learning is allowed.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mac_learning/limit:

      **limit**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of MAC addresses that can be learned.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mac_learning/limit_policy:

      **limit_policy**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The default switching policy after MAC limit is exceeded.


      Choices:

      - :literal:`"allow"`
      - :literal:`"drop"`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-net_flow:

      **net_flow**

      :literal:`string`

      added in community.vmware 2.3.0


      .. raw:: html

        </div></div>

    - 
      Indicate whether or not the virtual machine IP traffic that flows through a vds gets analyzed by sending reports to a NetFlow collector.


      Choices:

      - :literal:`"true"`
      - :literal:`"on"`
      - :literal:`"yes"`
      - :literal:`"false"`
      - :literal:`"off"`
      - :literal:`"no"`
      - :literal:`"inherited"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy:

      **network_policy**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the different security values for portgroup.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy/forged_transmits:

      **forged_transmits**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether forged transmits are allowed. Ignored if \ :literal:`inherited`\  is true.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy/inherited:

      **inherited**

      :literal:`boolean` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Inherit the settings from the switch or not.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy/mac_changes:

      **mac_changes**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether mac changes are allowed. Ignored if \ :literal:`inherited`\  is true.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy/promiscuous:

      **promiscuous**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether promiscuous mode is allowed. Ignored if \ :literal:`inherited`\  is true.


      Choices:

      - :literal:`false`
      - :literal:`true`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-num_ports:

      **num_ports**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of ports the portgroup should contain.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-out_traffic_shaping:

      **out_traffic_shaping**

      :literal:`dictionary`

      added in community.vmware 2.3.0


      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the egress traffic shaping settings for the portgroup.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-out_traffic_shaping/average_bandwidth:

      **average_bandwidth**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Establishes the number of bits per second to allow across a port, averaged over time, that is, the allowed average load.

      Ignored if \ :literal:`inherited`\  is true.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-out_traffic_shaping/burst_size:

      **burst_size**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of bits per second to allow across a port when it is sending/sending or receiving a burst of traffic.

      Ignored if \ :literal:`inherited`\  is true.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-out_traffic_shaping/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether egress traffic shaping is activated or not.

      Ignored if \ :literal:`inherited`\  is true.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-out_traffic_shaping/inherited:

      **inherited**

      :literal:`boolean` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Inherit the settings from the switch or not.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-out_traffic_shaping/peak_bandwidth:

      **peak_bandwidth**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of bytes to allow in a burst.

      Ignored if \ :literal:`inherited`\  is true.




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

      .. _parameter-port_allocation:

      **port_allocation**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Elastic port groups automatically increase or decrease the number of ports as needed.

      Only valid if \ :emphasis:`port\_binding`\  is set to \ :literal:`static`\ .

      Will be \ :literal:`elastic`\  if not specified and \ :emphasis:`port\_binding`\  is set to \ :literal:`static`\ .

      Will be \ :literal:`fixed`\  if not specified and \ :emphasis:`port\_binding`\  is set to \ :literal:`ephemeral`\ .


      Choices:

      - :literal:`"elastic"`
      - :literal:`"fixed"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port_binding:

      **port_binding**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The type of port binding determines when ports in a port group are assigned to virtual machines.

      See VMware KB 1022312 \ https://kb.vmware.com/s/article/1022312\  for more details.


      Choices:

      - :literal:`"static"`
      - :literal:`"ephemeral"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port_policy:

      **port_policy**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the advanced policy settings for the portgroup.


      Default: :literal:`{"block\_override": true, "ipfix\_override": false, "live\_port\_move": false, "mac\_management\_override": false, "network\_rp\_override": false, "port\_config\_reset\_at\_disconnect": true, "shaping\_override": false, "traffic\_filter\_override": false, "uplink\_teaming\_override": false, "vendor\_config\_override": false, "vlan\_override": false}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

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

      .. _parameter-port_policy/ipfix_override:

      **ipfix_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the ipfix policy can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port_policy/live_port_move:

      **live_port_move**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if a live port can be moved in or out of the portgroup.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port_policy/mac_management_override:
      .. _parameter-port_policy/security_override:

      **mac_management_override**

      aliases: security_override

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the security policy can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port_policy/network_rp_override:

      **network_rp_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the network resource pool can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

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

      .. _parameter-port_policy/shaping_override:

      **shaping_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the shaping policy can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

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

      .. _parameter-port_policy/uplink_teaming_override:

      **uplink_teaming_override**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates if the uplink teaming policy can be changed per port.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

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

      .. _parameter-portgroup_name:

      **portgroup_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the portgroup that is to be created or deleted.



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

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Determines if the portgroup should be present or not.


      Choices:

      - :literal:`"present"`
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-switch_name:

      **switch_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the distributed vSwitch the port group should be created on.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming_policy:

      **teaming_policy**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the different teaming values for portgroup.


      Default: :literal:`{"load\_balance\_policy": "loadbalance\_srcid", "notify\_switches": true, "rolling\_order": false}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming_policy/active_uplinks:

      **active_uplinks**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of active uplinks used for load balancing.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming_policy/inbound_policy:

      **inbound_policy**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicate whether or not the teaming policy is applied to inbound frames as well.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming_policy/load_balance_policy:

      **load_balance_policy**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Network adapter teaming policy.

      \ :literal:`loadbalance\_loadbased`\  is available from version 2.6 and onwards.


      Choices:

      - :literal:`"loadbalance\_ip"`
      - :literal:`"loadbalance\_srcmac"`
      - :literal:`"loadbalance\_srcid"` ← (default)
      - :literal:`"loadbalance\_loadbased"`
      - :literal:`"failover\_explicit"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming_policy/notify_switches:

      **notify_switches**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicate whether or not to notify the physical switch if a link fails.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming_policy/rolling_order:

      **rolling_order**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicate whether or not to use a rolling policy when restoring links.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming_policy/standby_uplinks:

      **standby_uplinks**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of standby uplinks used for failover.




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

      .. _parameter-vlan_id:

      **vlan_id**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The VLAN ID that should be configured with the portgroup, use 0 for no VLAN.

      If \ :literal:`vlan\_trunk`\  is configured to be \ :emphasis:`true`\ , this can be a combination of multiple ranges and numbers, example: 1-200, 205, 400-4094.

      The valid \ :literal:`vlan\_id`\  range is from 0 to 4094. Overlapping ranges are allowed.

      If \ :literal:`vlan\_private`\  is configured to be \ :emphasis:`true`\ , the corresponding private VLAN should already be configured in the distributed vSwitch.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vlan_private:

      **vlan_private**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether this is for a private VLAN or not.

      Mutually exclusive with \ :literal:`vlan\_trunk`\  parameter.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vlan_trunk:

      **vlan_trunk**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether this is a VLAN trunk or not.

      Mutually exclusive with \ :literal:`vlan\_private`\  parameter.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`





Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
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
        vlan_trunk: true
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
        vlan_private: true
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
          inherited: false
          promiscuous: true
          forged_transmits: true
          mac_changes: true
        port_policy:
          block_override: true
          ipfix_override: true
          live_port_move: true
          network_rp_override: true
          port_config_reset_at_disconnect: true
          mac_management_override: true
          shaping_override: true
          traffic_filter_override: true
          uplink_teaming_override: true
          vendor_config_override: true
          vlan_override: true
      delegate_to: localhost







Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Philippe Dellaert (@pdellaert) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

