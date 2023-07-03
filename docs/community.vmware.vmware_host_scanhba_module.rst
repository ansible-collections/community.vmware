

community.vmware.vmware_host_scanhba module -- Rescan host HBA's and optionally refresh the storage system
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_scanhba`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can force a rescan of the hosts HBA subsystem which is needed when wanting to mount a new datastore.
- You could use this before using \ `community.vmware.vmware\_host\_datastore <vmware_host_datastore_module.rst>`__\  to mount a new datastore to ensure your device/volume is ready.
- You can also optionally force a Refresh of the Storage System in vCenter/ESXi Web Client.
- All parameters and VMware object names are case sensitive.
- You can supply an esxi\_hostname or a cluster\_name








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
      Cluster name to Rescan the storage subsystem on (this will run the rescan task on each host in the cluster).



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      ESXi hostname to Rescan the storage subsystem on.



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

      .. _parameter-refresh_storage:

      **refresh_storage**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Refresh the storage system in vCenter/ESXi Web Client for each host found


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rescan_hba:

      **rescan_hba**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Rescan all host bus adapters for new storage devices. Rescanning all adapters can be slow.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-rescan_vmfs:

      **rescan_vmfs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Rescan all known storage devices for new VMFS volumes.


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

    
    - name: Rescan HBA's for a given ESXi host and refresh storage system objects
      community.vmware.vmware_host_scanhba:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ inventory_hostname }}'
          refresh_storage: true
      delegate_to: localhost

    - name: Rescan HBA's for a given cluster - all found hosts will be scanned
      community.vmware.vmware_host_scanhba:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ inventory_hostname }}'
          refresh_storage: true
      delegate_to: localhost

    - name: Rescan for new VMFS Volumes in a given cluster, but do not scan for new Devices - all found hosts will be scanned
      community.vmware.vmware_host_scanhba:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ inventory_hostname }}'
          rescan_vmfs: true
          rescan_hba: false
      delegate_to: localhost

    - name: Rescan HBA's for a given ESXi host and don't refresh storage system objects
      community.vmware.vmware_host_scanhba:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ inventory_hostname }}'
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

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      return confirmation of requested host and updated / refreshed storage system


      Returned: always

      Sample: :literal:`{"esxi01.example.com": {"refreshed\_storage": "true", "rescaned\_hba": "true", "rescaned\_vmfs": "true"}}`




Authors
~~~~~~~

- Michael Eaton (@michaeldeaton)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

