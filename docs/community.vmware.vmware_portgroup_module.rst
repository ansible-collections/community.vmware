

community.vmware.vmware_portgroup module -- Create a VMware portgroup
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_portgroup`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Create a VMware Port Group on a VMware Standard Switch (vSS) for given ESXi host(s) or hosts of given cluster.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster:
      .. _parameter-cluster_name:

      **cluster_name**

      aliases: cluster

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of cluster name for host membership.

      Portgroup will be created on all hosts of the given cluster.

      This option is required if \ :literal:`hosts`\  is not specified.



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

      .. _parameter-esxi_hostname:
      .. _parameter-hosts:

      **hosts**

      aliases: esxi_hostname

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of name of host or hosts on which portgroup needs to be added.

      This option is required if \ :literal:`cluster\_name`\  is not specified.



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

      **portgroup**

      aliases: portgroup_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Portgroup name to add.



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
      Determines if the portgroup should be present or not.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-switch:
      .. _parameter-switch_name:
      .. _parameter-vswitch:

      **switch**

      aliases: switch_name, vswitch

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      vSwitch to modify.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-teaming:
      .. _parameter-teaming_policy:

      **teaming**

      aliases: teaming_policy

      :literal:`dictionary`

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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vlan:
      .. _parameter-vlan_id:

      **vlan_id**

      aliases: vlan

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      VLAN ID to assign to portgroup.

      Set to 0 (no VLAN tagging) by default.


      Default: :literal:`0`




Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add Management Network VM Portgroup
      community.vmware.vmware_portgroup:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
      delegate_to: localhost

    - name: Add Portgroup with Promiscuous Mode Enabled
      community.vmware.vmware_portgroup:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        security:
            promiscuous_mode: true
      delegate_to: localhost

    - name: Add Management Network VM Portgroup to specific hosts
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        hosts: [esxi_hostname_one]
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
      delegate_to: localhost

    - name: Add Management Network VM Portgroup to all hosts in a cluster
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        cluster_name: "{{ cluster_name }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
      delegate_to: localhost

    - name: Remove Management Network VM Portgroup to all hosts in a cluster
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        cluster_name: "{{ cluster_name }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
        state: absent
      delegate_to: localhost

    - name: Add Portgroup with all settings defined
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ inventory_hostname }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: 10
        security:
            promiscuous_mode: false
            mac_changes: false
            forged_transmits: false
        traffic_shaping:
            enabled: true
            average_bandwidth: 100000
            peak_bandwidth: 100000
            burst_size: 102400
        teaming:
            load_balancing: failover_explicit
            network_failure_detection: link_status_only
            notify_switches: true
            failback: true
            active_adapters:
                - vmnic0
            standby_adapters:
                - vmnic1
      delegate_to: localhost
      register: teaming_result





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
      metadata about the portgroup


      Returned: always

      Sample: :literal:`{"esxi01.example.com": {"changed": true, "failback": "No override", "failover\_active": "No override", "failover\_standby": "No override", "failure\_detection": "No override", "load\_balancing": "No override", "msg": "Port Group added", "notify\_switches": "No override", "portgroup": "vMotion", "sec\_forged\_transmits": false, "sec\_mac\_changes": false, "sec\_promiscuous\_mode": false, "traffic\_shaping": "No override", "vlan\_id": 33, "vswitch": "vSwitch1"}}`




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

