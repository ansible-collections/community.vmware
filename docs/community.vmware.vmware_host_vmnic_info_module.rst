

community.vmware.vmware_host_vmnic_info module -- Gathers info about vmnics available on the given ESXi host
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_vmnic_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about vmnics available on the given ESXi host.
- If \ :literal:`cluster\_name`\  is provided, then vmnic information about all hosts from given cluster will be returned.
- If \ :literal:`esxi\_hostname`\  is provided, then vmnic information about given host system will be returned.
- Additional details about vswitch and dvswitch with respective vmnic is also provided which is added in 2.7 version.
- Additional details about lldp added in 1.11.0








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-capabilities:

      **capabilities**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Gather information about general capabilities (Auto negotiation, Wake On LAN, and Network I/O Control).


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster_name:

      **cluster_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the cluster from which all host systems will be used.

      Vmnic information about each ESXi server will be returned for the given cluster.

      This parameter is required if \ :literal:`esxi\_hostname`\  is not specified.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directpath_io:

      **directpath_io**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Gather information about DirectPath I/O capabilities and configuration.


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
      Name of the host system to work with.

      Vmnic information about this ESXi server will be returned.

      This parameter is required if \ :literal:`cluster\_name`\  is not specified.



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

      .. _parameter-sriov:

      **sriov**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Gather information about SR-IOV capabilities and configuration.


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

    
    - name: Gather info about vmnics of all ESXi Host in the given Cluster
      community.vmware.vmware_host_vmnic_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: '{{ cluster_name }}'
      delegate_to: localhost
      register: cluster_host_vmnics

    - name: Gather info about vmnics of an ESXi Host
      community.vmware.vmware_host_vmnic_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
      delegate_to: localhost
      register: host_vmnics





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

      .. _return-hosts_vmnics_info:

      **hosts_vmnics_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dict with hostname as key and dict with vmnics information as value.

      for \ :literal:`num\_vmnics`\ , only NICs starting with vmnic are counted. NICs like vusb\* are not counted.

      details about vswitch and dvswitch was added in version 2.7.

      details about vmnics was added in version 2.8.

      details about lldp was added in version 1.11.0


      Returned: hosts\_vmnics\_info

      Sample: :literal:`{"10.76.33.204": {"all": ["vmnic0", "vmnic1"], "available": [], "dvswitch": {"dvs\_0002": ["vmnic1"]}, "num\_vmnics": 2, "used": ["vmnic1", "vmnic0"], "vmnic\_details": [{"actual\_duplex": "Full Duplex", "actual\_speed": 10000, "adapter": "Intel(R) 82599 10 Gigabit Dual Port Network Connection", "configured\_duplex": "Auto negotiate", "configured\_speed": "Auto negotiate", "device": "vmnic0", "driver": "ixgbe", "lldp\_info": {"Aggregated Port ID": "0", "Aggregation Status": "1", "Enabled Capabilities": {"\_vimtype": "vim.host.PhysicalNic.CdpDeviceCapability", "host": false, "igmpEnabled": false, "networkSwitch": false, "repeater": false, "router": true, "sourceRouteBridge": false, "transparentBridge": true}, "MTU": "9216", "Port Description": "switch port description", "Samples": 18814, "System Description": "omitted from output", "System Name": "sw1", "TimeOut": 30, "Vlan ID": "1"}, "location": "0000:01:00.0", "mac": "aa:bb:cc:dd:ee:ff", "status": "Connected"}, {"actual\_duplex": "Full Duplex", "actual\_speed": 10000, "adapter": "Intel(R) 82599 10 Gigabit Dual Port Network Connection", "configured\_duplex": "Auto negotiate", "configured\_speed": "Auto negotiate", "device": "vmnic1", "driver": "ixgbe", "lldp\_info": "N/A", "location": "0000:01:00.1", "mac": "ab:ba:cc:dd:ee:ff", "status": "Connected"}], "vswitch": {"vSwitch0": ["vmnic0"]}}}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

