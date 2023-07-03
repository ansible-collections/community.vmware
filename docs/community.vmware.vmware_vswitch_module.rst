

community.vmware.vmware_vswitch module -- Manage a VMware Standard Switch to an ESXi host.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vswitch`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add, remove and update a VMware Standard Switch to an ESXi host.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:
      .. _parameter-host:

      **esxi_hostname**

      aliases: host

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Manage the vSwitch using this ESXi host system.



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
      MTU to configure on vSwitch.


      Default: :literal:`1500`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nic_name:
      .. _parameter-nics:

      **nics**

      aliases: nic_name

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      A list of vmnic names or vmnic name to attach to vSwitch.

      Alias \ :literal:`nics`\  is added in version 2.4.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-number_of_ports:

      **number_of_ports**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Number of port to configure on vSwitch.


      Default: :literal:`128`


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

      .. _parameter-network_policy:
      .. _parameter-security:
      .. _parameter-security_policy:

      **security**

      aliases: security_policy, network_policy

      :literal:`dictionary`

      added in community.vmware 2.4.0


      .. raw:: html

        </div></div>

    - 
      Network policy specifies layer 2 security settings for a portgroup such as promiscuous mode, where guest adapter listens to all the packets, MAC address changes and forged transmits.

      Dict which configures the different security values for portgroup.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy/forged_transmits:
      .. _parameter-security/forged_transmits:
      .. _parameter-security_policy/forged_transmits:

      **forged_transmits**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether forged transmits are allowed.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy/mac_changes:
      .. _parameter-security/mac_changes:
      .. _parameter-security_policy/mac_changes:

      **mac_changes**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether mac changes are allowed.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-network_policy/promiscuous_mode:
      .. _parameter-security/promiscuous_mode:
      .. _parameter-security_policy/promiscuous_mode:

      **promiscuous_mode**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether promiscuous mode is allowed.


      Choices:

      - :literal:`false`
      - :literal:`true`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Add or remove the switch.


      Choices:

      - :literal:`"absent"`
      - :literal:`"present"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-switch:
      .. _parameter-switch_name:

      **switch**

      aliases: switch_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      vSwitch name to add.

      Alias \ :literal:`switch`\  is added in version 2.4.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming:
      .. _parameter-teaming_policy:

      **teaming**

      aliases: teaming_policy

      :literal:`dictionary`

      added in community.vmware 2.4.0


      .. raw:: html

        </div></div>

    - 
      Dictionary which configures the different teaming values for portgroup.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming/active_adapters:
      .. _parameter-teaming_policy/active_adapters:

      **active_adapters**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of active adapters used for load balancing.

      All vmnics are used as active adapters if \ :literal:`active\_adapters`\  and \ :literal:`standby\_adapters`\  are not defined.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming/failback:
      .. _parameter-teaming_policy/failback:

      **failback**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicate whether or not to use a failback when restoring links.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming/load_balance_policy:
      .. _parameter-teaming/load_balancing:
      .. _parameter-teaming_policy/load_balance_policy:
      .. _parameter-teaming_policy/load_balancing:

      **load_balancing**

      aliases: load_balance_policy

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Network adapter teaming policy.


      Choices:

      - :literal:`"loadbalance\_ip"`
      - :literal:`"loadbalance\_srcmac"`
      - :literal:`"loadbalance\_srcid"`
      - :literal:`"failover\_explicit"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming/network_failure_detection:
      .. _parameter-teaming_policy/network_failure_detection:

      **network_failure_detection**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Network failure detection.


      Choices:

      - :literal:`"link\_status\_only"`
      - :literal:`"beacon\_probing"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming/notify_switches:
      .. _parameter-teaming_policy/notify_switches:

      **notify_switches**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicate whether or not to notify the physical switch if a link fails.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming/standby_adapters:
      .. _parameter-teaming_policy/standby_adapters:

      **standby_adapters**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of standby adapters used for failover.

      All vmnics are used as active adapters if \ :literal:`active\_adapters`\  and \ :literal:`standby\_adapters`\  are not defined.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-traffic_shaping:

      **traffic_shaping**

      :literal:`dictionary`

      added in community.vmware 2.4.0


      .. raw:: html

        </div></div>

    - 
      Dictionary which configures traffic shaping for the switch.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-traffic_shaping/average_bandwidth:

      **average_bandwidth**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Average bandwidth (kbit/s).



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-traffic_shaping/burst_size:

      **burst_size**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Burst size (KB).



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-traffic_shaping/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Status of Traffic Shaping Policy.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-traffic_shaping/peak_bandwidth:

      **peak_bandwidth**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Peak bandwidth (kbit/s).




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





Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Add a VMware vSwitch
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        switch: vswitch_name
        nics: vmnic_name
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch without any physical NIC attached
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        switch: vswitch_0001
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch with multiple NICs
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        switch: vmware_vswitch_0004
        nics:
        - vmnic1
        - vmnic2
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name: vmnic0
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system with Promiscuous Mode Enabled
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name: vmnic0
        mtu: 9000
        security:
            promiscuous_mode: true
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system with active/standby teaming
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name:
          - vmnic0
          - vmnic1
        teaming:
          active_adapters:
            - vmnic0
          standby_adapters:
            - vmnic1
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system with traffic shaping
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name:
          - vmnic0
          - vmnic1
        traffic_shaping:
            enabled: true
            average_bandwidth: 100000
            peak_bandwidth: 100000
            burst_size: 102400
      delegate_to: localhost

    - name: Delete a VMware vSwitch in a specific host system
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        state: absent
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

      Sample: :literal:`"vSwitch 'vSwitch\_1002' is created successfully"`




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

