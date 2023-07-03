

community.vmware.vmware_host_datastore module -- Manage a datastore on ESXi host
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_datastore`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to mount/umount datastore on ESXi host.
- This module only supports NFS (NFS v3 or NFS v4.1) and VMFS datastores.
- For VMFS datastore, available device must already be connected on ESXi host.
- All parameters and VMware object names are case sensitive.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-auto_expand:

      **auto_expand**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Expand a datastore capacity to full if it has free capacity.

      This parameter can't be extend using another datastore.

      A use case example in \ :emphasis:`auto\_expand`\ , it can be used to expand a datastore capacity after increasing LUN volume.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore_name:

      **datastore_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the datastore to add/remove.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore_type:

      **datastore_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of the datastore to configure (nfs/nfs41/vmfs).


      Choices:

      - :literal:`"nfs"`
      - :literal:`"nfs41"`
      - :literal:`"vmfs"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      ESXi hostname to manage the datastore.

      Required when used with a vcenter



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

      .. _parameter-nfs_path:

      **nfs_path**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Resource path on NFS host.

      Required if datastore type is set to \ :literal:`nfs`\ /\ :literal:`nfs41`\  and state is set to \ :literal:`present`\ , else unused.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nfs_ro:

      **nfs_ro**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      ReadOnly or ReadWrite mount.

      Unused if datastore type is not set to \ :literal:`nfs`\ /\ :literal:`nfs41`\  and state is not set to \ :literal:`present`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nfs_server:

      **nfs_server**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      NFS host serving nfs datastore.

      Required if datastore type is set to \ :literal:`nfs`\ /\ :literal:`nfs41`\  and state is set to \ :literal:`present`\ , else unused.

      Two or more servers can be defined if datastore type is set to \ :literal:`nfs41`\ 



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
      present: Mount datastore on host if datastore is absent else do nothing.

      absent: Umount datastore if datastore is present else do nothing.


      Choices:

      - :literal:`"present"` ← (default)
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

      .. _parameter-vmfs_device_name:

      **vmfs_device_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the device to be used as VMFS datastore.

      Required for VMFS datastore type and state is set to \ :literal:`present`\ , else unused.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmfs_version:

      **vmfs_version**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      VMFS version to use for datastore creation.

      Unused if datastore type is not set to \ :literal:`vmfs`\  and state is not set to \ :literal:`present`\ .





Notes
-----

.. note::
   - Kerberos authentication with NFS v4.1 isn't implemented
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Mount VMFS datastores to ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          datastore_name: '{{ item.name }}'
          datastore_type: '{{ item.type }}'
          vmfs_device_name: 'naa.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
          vmfs_version: 6
          esxi_hostname: '{{ inventory_hostname }}'
          state: present
      delegate_to: localhost

    - name: Mount NFS datastores to ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          datastore_name: '{{ item.name }}'
          datastore_type: '{{ item.type }}'
          nfs_server: '{{ item.server }}'
          nfs_path: '{{ item.path }}'
          nfs_ro: false
          esxi_hostname: '{{ inventory_hostname }}'
          state: present
      delegate_to: localhost
      loop:
          - { 'name': 'NasDS_vol01', 'server': 'nas01', 'path': '/mnt/vol01', 'type': 'nfs'}
          - { 'name': 'NasDS_vol02', 'server': 'nas01', 'path': '/mnt/vol02', 'type': 'nfs'}

    - name: Mount NFS v4.1 datastores to ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          datastore_name: '{{ item.name }}'
          datastore_type: '{{ item.type }}'
          nfs_server: '{{ item.server }}'
          nfs_path: '{{ item.path }}'
          nfs_ro: false
          esxi_hostname: '{{ inventory_hostname }}'
          state: present
      delegate_to: localhost
      loop:
          - { 'name': 'NasDS_vol03', 'server': 'nas01,nas02', 'path': '/mnt/vol01', 'type': 'nfs41'}
          - { 'name': 'NasDS_vol04', 'server': 'nas01,nas02', 'path': '/mnt/vol02', 'type': 'nfs41'}

    - name: Remove/Umount Datastores from a ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          datastore_name: NasDS_vol01
          state: absent
      delegate_to: localhost







Authors
~~~~~~~

- Ludovic Rivallain (@lrivallain) 
- Christian Kotte (@ckotte) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

