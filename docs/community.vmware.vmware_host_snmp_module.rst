

community.vmware.vmware_host_snmp module -- Configures SNMP on an ESXi host system
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_snmp`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure the embedded SNMP agent on an ESXi host.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-community:

      **community**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of SNMP community strings.


      Default: :literal:`[]`


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

      .. _parameter-hw_source:

      **hw_source**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Source hardware events from IPMI sensors or CIM Indications.

      The embedded SNMP agent receives hardware events either from IPMI sensors \ :literal:`sensors`\  or CIM indications \ :literal:`indications`\ .


      Choices:

      - :literal:`"indications"` ← (default)
      - :literal:`"sensors"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-log_level:

      **log_level**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Syslog logging level.


      Choices:

      - :literal:`"debug"`
      - :literal:`"info"` ← (default)
      - :literal:`"warning"`
      - :literal:`"error"`



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

      .. _parameter-send_trap:

      **send_trap**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Send a test trap to validate the configuration.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_port:

      **snmp_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Port used by the SNMP agent.


      Default: :literal:`161`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Enable, disable, or reset the SNMP agent.


      Choices:

      - :literal:`"disabled"` ← (default)
      - :literal:`"enabled"`
      - :literal:`"reset"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-sys_contact:

      **sys_contact**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      System contact who manages the system.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-sys_location:

      **sys_location**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      System location.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-trap_filter:

      **trap_filter**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      A list of trap oids for traps not to be sent by agent, e.g. [ 1.3.6.1.4.1.6876.4.1.1.0, 1.3.6.1.4.1.6876.4.1.1.1 ]

      Use value \ :literal:`reset`\  to clear settings.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-trap_targets:

      **trap_targets**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of trap targets.

      You need to use \ :literal:`hostname`\ , \ :literal:`port`\ , and \ :literal:`community`\  for each trap target.


      Default: :literal:`[]`


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

- You need to reset the agent (to factory defaults) if you want to clear all community strings, trap targets, or filters
- SNMP v3 configuration isn't implemented yet
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Enable and configure SNMP community
      community.vmware.vmware_host_snmp:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        community: [ test ]
        state: enabled
      delegate_to: localhost

    - name: Configure SNMP traps and filters
      community.vmware.vmware_host_snmp:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        community: [ test ]
        trap_targets:
          - hostname: 192.168.1.100
            port: 162
            community: test123
          - hostname: 192.168.1.101
            port: 162
            community: test1234
        trap_filter:
          - 1.3.6.1.4.1.6876.4.1.1.0
          - 1.3.6.1.4.1.6876.4.1.1.1
        state: enabled
      delegate_to: localhost

    - name: Enable and configure SNMP system contact and location
      community.vmware.vmware_host_snmp:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        sys_contact: "admin@testemail.com"
        sys_location: "Austin, USA"
        state: enabled
      delegate_to: localhost

    - name: Disable SNMP
      community.vmware.vmware_host_snmp:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        state: disabled
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

      .. _return-results:

      **results**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about host system's SNMP configuration


      Returned: always

      Sample: :literal:`{"esxi01": {"changed": false, "community": ["test"], "hw\_source": "indications", "msg": "SNMP already configured properly", "port": 161, "state": "enabled", "trap\_targets": []}}`




Authors
~~~~~~~

- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

