

community.vmware.vmware_host module -- Add, remove, or move an ESXi host to, from, or within vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add, reconnect, or remove an ESXi host to or from vCenter.
- This module can also be used to move an ESXi host to a cluster or folder, or vice versa, within the same datacenter.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-add_connected:

      **add_connected**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , then the host should be connected as soon as it is added.

      This parameter is ignored if state is set to a value other than \ :literal:`present`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



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
      Name of the cluster to add the host.

      If \ :literal:`folder`\  is not set, then this parameter is required.

      Aliases added in version 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:
      .. _parameter-datacenter_name:

      **datacenter_name**

      aliases: datacenter

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the datacenter to add the host.

      Aliases added in version 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      ESXi hostname to manage.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_password:

      **esxi_password**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      ESXi password.

      Required for adding a host.

      Optional for reconnect.

      Unused for removing.

      No longer a required parameter from version 2.5.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_ssl_thumbprint:
      .. _parameter-ssl_thumbprint:

      **esxi_ssl_thumbprint**

      aliases: ssl_thumbprint

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specifying the hostsystem certificate's thumbprint.

      Use following command to get hostsystem certificate's thumbprint - 

      # openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha1 -noout

      Only used if \ :literal:`fetch\_thumbprint`\  isn't set to \ :literal:`true`\ .


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_username:

      **esxi_username**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      ESXi username.

      Required for adding a host.

      Optional for reconnect. If both \ :literal:`esxi\_username`\  and \ :literal:`esxi\_password`\  are used

      Unused for removing.

      No longer a required parameter from version 2.5.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-fetch_ssl_thumbprint:

      **fetch_ssl_thumbprint**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Fetch the thumbprint of the host's SSL certificate.

      This basically disables the host certificate verification (check if it was signed by a recognized CA).

      Disable this option if you want to allow only hosts with valid certificates to be added to vCenter.

      If this option is set to \ :literal:`false`\  and the certificate can't be verified, an add or reconnect will fail.

      Unused when \ :literal:`esxi\_ssl\_thumbprint`\  is set.

      Optional for reconnect, but only used if \ :literal:`esxi\_username`\  and \ :literal:`esxi\_password`\  are used.

      Unused for removing.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:
      .. _parameter-folder_name:

      **folder**

      aliases: folder_name

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the folder under which host to add.

      If \ :literal:`cluster\_name`\  is not set, then this parameter is required.

      For example, if there is a datacenter 'dc1' under folder called 'Site1' then, this value will be '/Site1/dc1/host'.

      Here 'host' is an invisible folder under VMware Web Client.

      Another example, if there is a nested folder structure like '/myhosts/india/pune' under datacenter 'dc2', then \ :literal:`folder`\  value will be '/dc2/host/myhosts/india/pune'.

      Other Examples: '/Site2/dc2/Asia-Cluster/host' or '/dc3/Asia-Cluster/host'



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-force_connection:

      **force_connection**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Force the connection if the host is already being managed by another vCenter server.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



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

      .. _parameter-reconnect_disconnected:

      **reconnect_disconnected**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Reconnect disconnected hosts.

      This is only used if \ :literal:`state`\  is set to \ :literal:`present`\  and if the host already exists.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`present`\ , add the host if host is absent.

      If set to \ :literal:`present`\ , update the location of the host if host already exists.

      If set to \ :literal:`absent`\ , remove the host if host is present.

      If set to \ :literal:`absent`\ , do nothing if host already does not exists.

      If set to \ :literal:`add\_or\_reconnect`\ , add the host if it's absent else reconnect it and update the location.

      If set to \ :literal:`reconnect`\ , then reconnect the host if it's present and update the location.

      If set to \ :literal:`disconnected`\ , disconnect the host if the host already exists.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`
      - :literal:`"add\_or\_reconnect"`
      - :literal:`"reconnect"`
      - :literal:`"disconnected"`



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

    
    - name: Add ESXi Host to vCenter
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: present
      delegate_to: localhost

    - name: Add ESXi Host to vCenter under a specific folder
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        folder: '/Site2/Asia-Cluster/host'
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: present
        add_connected: true
      delegate_to: localhost

    - name: Reconnect ESXi Host (with username/password set)
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: reconnect
      delegate_to: localhost

    - name: Reconnect ESXi Host (with default username/password)
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        state: reconnect
      delegate_to: localhost

    - name: Add ESXi Host with SSL Thumbprint to vCenter
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        esxi_ssl_thumbprint: "3C:A5:60:6F:7A:B7:C4:6C:48:28:3D:2F:A5:EC:A3:58:13:88:F6:DD"
        state: present
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
      metadata about the new host system added


      Returned: on successful addition

      Sample: :literal:`"Host already connected to vCenter 'vcenter01' in cluster 'cluster01'"`




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Maxime de Roucy (@tchernomax)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

