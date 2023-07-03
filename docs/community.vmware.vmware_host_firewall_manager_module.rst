

community.vmware.vmware_host_firewall_manager module -- Manage firewall configurations about an ESXi host
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_firewall_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage firewall configurations about an ESXi host when ESXi hostname or Cluster name is given.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster_name:

      **cluster_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the cluster.

      Firewall settings are applied to every ESXi host system in given cluster.

      If \ :literal:`esxi\_hostname`\  is not given, this parameter is required.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      ESXi hostname.

      Firewall settings are applied to this ESXi host system.

      If \ :literal:`cluster\_name`\  is not given, this parameter is required.



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

      .. _parameter-rules:

      **rules**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of Rule set which needs to be managed.

      Each member of list is rule set name and state to be set the rule.

      Both rule name and rule state are required parameters.

      Additional IPs and networks can also be specified

      Please see examples for more information.


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rules/allowed_hosts:

      **allowed_hosts**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Define the allowed hosts for this rule set.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rules/allowed_hosts/all_ip:

      **all_ip**

      :literal:`boolean` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Whether all hosts should be allowed or not.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rules/allowed_hosts/ip_address:

      **ip_address**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of allowed IP addresses.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rules/allowed_hosts/ip_network:

      **ip_network**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of allowed IP networks.


      Default: :literal:`[]`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rules/enabled:

      **enabled**

      :literal:`boolean` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Whether the rule set is enabled or not.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rules/name:

      **name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Rule set name.




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

    
    - name: Enable vvold rule set for all ESXi Host in given Cluster
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: cluster_name
        rules:
            - name: vvold
              enabled: true
              allowed_hosts:
                all_ip: true
      delegate_to: localhost

    - name: Enable vvold rule set for an ESXi Host
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        rules:
            - name: vvold
              enabled: true
              allowed_hosts:
                all_ip: true
      delegate_to: localhost

    - name: Manage multiple rule set for an ESXi Host
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        rules:
            - name: vvold
              enabled: true
              allowed_hosts:
                all_ip: true
            - name: CIMHttpServer
              enabled: false
      delegate_to: localhost

    - name: Manage IP and network based firewall permissions for ESXi
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        rules:
            - name: gdbserver
              enabled: true
              allowed_hosts:
                all_ip: false
                ip_address:
                  - 192.168.20.10
                  - 192.168.20.11
            - name: CIMHttpServer
              enabled: true
              allowed_hosts:
                all_ip: false
                ip_network:
                  - 192.168.100.0/24
            - name: remoteSerialPort
              enabled: true
              allowed_hosts:
                all_ip: false
                ip_address:
                  - 192.168.100.11
                ip_network:
                  - 192.168.200.0/24
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

      .. _return-rule_set_state:

      **rule_set_state**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dict with hostname as key and dict with firewall rule set facts as value


      Returned: success

      Sample: :literal:`{"rule\_set\_state": {"localhost.localdomain": {"CIMHttpServer": {"allowed\_hosts": {"current\_allowed\_all": true, "current\_allowed\_ip": [], "current\_allowed\_networks": [], "desired\_allowed\_all": true, "desired\_allowed\_ip": [], "desired\_allowed\_networks": [], "previous\_allowed\_all": true, "previous\_allowed\_ip": [], "previous\_allowed\_networks": []}, "current\_state": false, "desired\_state": false, "previous\_state": true}, "remoteSerialPort": {"allowed\_hosts": {"current\_allowed\_all": false, "current\_allowed\_ip": ["192.168.100.11"], "current\_allowed\_networks": ["192.168.200.0/24"], "desired\_allowed\_all": false, "desired\_allowed\_ip": ["192.168.100.11"], "desired\_allowed\_networks": ["192.168.200.0/24"], "previous\_allowed\_all": true, "previous\_allowed\_ip": [], "previous\_allowed\_networks": []}, "current\_state": true, "desired\_state": true, "previous\_state": true}}}}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Aaron Longchamps (@alongchamps)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

