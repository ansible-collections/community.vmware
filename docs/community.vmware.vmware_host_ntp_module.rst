

community.vmware.vmware_host_ntp module -- Manage NTP server configuration of an ESXi host
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_ntp`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure, add or remove NTP servers from an ESXi host.
- If \ :literal:`state`\  is not given, the NTP servers will be configured in the exact sequence.
- User can specify an ESXi hostname or Cluster name. In case of cluster name, all ESXi hosts are updated.








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
      Name of the cluster from which all host systems will be used.

      This parameter is required if \ :literal:`esxi\_hostname`\  is not specified.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the host system to work with.

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

      .. _parameter-ntp_servers:

      **ntp_servers**

      :literal:`list` / :literal:`elements=string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      IP or FQDN of NTP server(s).

      This accepts a list of NTP servers. For multiple servers, please look at the examples.



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

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      present: Add NTP server(s), if specified server(s) are absent else do nothing.

      absent: Remove NTP server(s), if specified server(s) are present else do nothing.

      Specified NTP server(s) will be configured if \ :literal:`state`\  isn't specified.


      Choices:

      - :literal:`"present"`
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

      .. _parameter-verbose:

      **verbose**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Verbose output of the configuration change.

      Explains if an NTP server was added, removed, or if the NTP server sequence was changed.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`





Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Configure NTP servers for an ESXi Host
      community.vmware.vmware_host_ntp:
        hostname: vcenter01.example.local
        username: administrator@vsphere.local
        password: SuperSecretPassword
        esxi_hostname: esx01.example.local
        ntp_servers:
            - 0.pool.ntp.org
            - 1.pool.ntp.org
      delegate_to: localhost

    - name: Set NTP servers for all ESXi Host in given Cluster
      community.vmware.vmware_host_ntp:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: '{{ cluster_name }}'
        state: present
        ntp_servers:
            - 0.pool.ntp.org
            - 1.pool.ntp.org
      delegate_to: localhost

    - name: Set NTP servers for an ESXi Host
      community.vmware.vmware_host_ntp:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        state: present
        ntp_servers:
            - 0.pool.ntp.org
            - 1.pool.ntp.org
      delegate_to: localhost

    - name: Remove NTP servers for an ESXi Host
      community.vmware.vmware_host_ntp:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        state: absent
        ntp_servers:
            - bad.server.ntp.org
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

      .. _return-host_ntp_status:

      **host_ntp_status**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about host system's NTP configuration


      Returned: always

      Sample: :literal:`{"esx01.example.local": {"ntp\_servers": ["time3.example.local", "time4.example.local"], "ntp\_servers\_changed": ["time1.example.local", "time2.example.local", "time3.example.local", "time4.example.local"], "ntp\_servers\_previous": ["time1.example.local", "time2.example.local"]}, "esx02.example.local": {"ntp\_servers\_changed": ["time3.example.local"], "ntp\_servers\_current": ["time1.example.local", "time2.example.local", "time3.example.local"], "ntp\_servers\_previous": ["time1.example.local", "time2.example.local"], "state": "present"}}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

