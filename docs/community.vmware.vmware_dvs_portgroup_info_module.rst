

community.vmware.vmware_dvs_portgroup_info module -- Gathers info DVS portgroup configurations
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_dvs_portgroup_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about DVS portgroup configurations.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the datacenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-dvswitch:

      **dvswitch**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of a dvswitch to look for.



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

      .. _parameter-show_mac_learning:

      **show_mac_learning**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Show or hide MAC learning information of the DVS portgroup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_network_policy:

      **show_network_policy**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Show or hide network policies of DVS portgroup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_port_policy:

      **show_port_policy**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Show or hide port policies of DVS portgroup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_teaming_policy:

      **show_teaming_policy**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Show or hide teaming policies of DVS portgroup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_uplinks:

      **show_uplinks**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Show or hide uplinks of DVS portgroup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_vlan_info:

      **show_vlan_info**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Show or hide vlan information of the DVS portgroup.


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

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get info about DVPG
      community.vmware.vmware_dvs_portgroup_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
      register: dvpg_info

    - name: Get number of ports for portgroup 'dvpg_001' in 'dvs_001'
      debug:
        msg: "{{ item.num_ports }}"
      with_items:
        - "{{ dvpg_info.dvs_portgroup_info['dvs_001'] | json_query(query) }}"
      vars:
        query: "[?portgroup_name=='dvpg_001']"





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

      .. _return-dvs_portgroup_info:

      **dvs_portgroup_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about DVS portgroup configuration


      Returned: on success

      Sample: :literal:`{"dvs\_0": [{"description": null, "dvswitch\_name": "dvs\_001", "network\_policy": {"forged\_transmits": false, "mac\_changes": false, "promiscuous": false}, "num\_ports": 8, "port\_policy": {"block\_override": true, "ipfix\_override": false, "live\_port\_move": false, "network\_rp\_override": false, "port\_config\_reset\_at\_disconnect": true, "security\_override": false, "shaping\_override": false, "traffic\_filter\_override": false, "uplink\_teaming\_override": false, "vendor\_config\_override": false, "vlan\_override": false}, "portgroup\_name": "dvpg\_001", "teaming\_policy": {"inbound\_policy": true, "notify\_switches": true, "policy": "loadbalance\_srcid", "rolling\_order": false}, "type": "earlyBinding", "vlan\_info": {"pvlan": false, "trunk": false, "vlan\_id": 0}}]}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

