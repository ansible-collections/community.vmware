

community.vmware.vmware_host_dns module -- Manage DNS configuration of an ESXi host system
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_dns`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure DNS for the default TCP/IP stack on an ESXi host system.








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

      This parameter is required if \ :literal:`esxi\_hostname`\  is not specified and you connect to a vCenter.

      Cannot be used when you connect directly to an ESXi host.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-device:

      **device**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The VMkernel network adapter to obtain DNS settings from.

      Needs to get its IP through DHCP, a static network configuration combined with a dynamic DNS configuration doesn't work.

      The parameter is only required in case of \ :literal:`type`\  is set to \ :literal:`dhcp`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-dns_servers:

      **dns_servers**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      A list of DNS servers to be used.

      The order of the DNS servers is important as they are used consecutively in order.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-domain:

      **domain**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The domain name to be used for the ESXi host.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the host system to work with.

      This parameter is required if \ :literal:`cluster\_name`\  is not specified and you connect to a vCenter.

      Cannot be used when you connect directly to an ESXi host.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-host_name:

      **host_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The hostname to be used for the ESXi host.

      Cannot be used when configuring a complete cluster.



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

      .. _parameter-search_domains:

      **search_domains**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      A list of domains to be searched through by the resolver.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-type:

      **type**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Type of DNS assignment. Either \ :literal:`dhcp`\  or \ :literal:`static`\ .

      A VMkernel adapter needs to be set to DHCP if \ :literal:`type`\  is set to \ :literal:`dhcp`\ .


      Choices:

      - :literal:`"dhcp"`
      - :literal:`"static"`



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
      Verbose output of the DNS server configuration change.

      Explains if an DNS server was added, removed, or if the DNS server sequence was changed.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`





Notes
-----

.. note::
   - This module is a replacement for the module \ :literal:`vmware\_dns\_config`\ 
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Configure DNS for an ESXi host
      community.vmware.vmware_host_dns:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        type: static
        host_name: esx01
        domain: example.local
        dns_servers:
          - 192.168.1.10
          - 192.168.1.11
        search_domains:
          - subdomain.example.local
          - example.local
      delegate_to: localhost

    - name: Configure DNS for all ESXi hosts of a cluster
      community.vmware.vmware_host_dns:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: '{{ cluster_name }}'
        type: static
        domain: example.local
        dns_servers:
          - 192.168.1.10
          - 192.168.1.11
        search_domains:
          - subdomain.example.local
          - example.local
      delegate_to: localhost

    - name: Configure DNS via DHCP for an ESXi host
      community.vmware.vmware_host_dns:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        type: dhcp
        device: vmk0
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

      .. _return-dns_config_result:

      **dns_config_result**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about host system's DNS configuration


      Returned: always

      Sample: :literal:`{"esx01.example.local": {"changed": true, "dns\_servers": ["192.168.1.10", "192.168.1.11"], "dns\_servers\_changed": ["192.168.1.12", "192.168.1.13"], "dns\_servers\_previous": ["192.168.1.10", "192.168.1.11", "192.168.1.12", "192.168.1.13"], "domain": "example.local", "host\_name": "esx01", "msg": "DNS servers and Search domains changed", "search\_domains": ["subdomain.example.local", "example.local"], "search\_domains\_changed": ["subdomain.example.local"], "search\_domains\_previous": ["example.local"]}}`




Authors
~~~~~~~

- Christian Kotte (@ckotte)
- Mario Lenz (@mariolenz)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

