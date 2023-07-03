

community.vmware.vmware_vmotion module -- Move a virtual machine using vMotion, and/or its vmdks using storage vMotion.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vmotion`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Using VMware vCenter, move a virtual machine using vMotion to a different host, and/or its vmdks to another datastore using storage vMotion.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_cluster:

      **destination_cluster**

      :literal:`string`

      added in community.vmware 2.5.0


      .. raw:: html

        </div></div>

    - 
      Name of the destination cluster the virtual machine should be running on.

      Only works if drs is enabled for this cluster.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_datacenter:

      **destination_datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the destination datacenter the datastore is located on.

      Optional, required only when datastores are shared across datacenters.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore:
      .. _parameter-destination_datastore:

      **destination_datastore**

      aliases: datastore

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the destination datastore the virtual machine's vmdk should be moved on.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_datastore_cluster:

      **destination_datastore_cluster**

      :literal:`string`

      added in community.vmware 2.5.0


      .. raw:: html

        </div></div>

    - 
      Name of the destination datastore cluster (storage pod) the virtual machine's vmdk should be moved on.

      Only works if drs is enabled for the cluster the vm is running / should run.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination:
      .. _parameter-destination_host:

      **destination_host**

      aliases: destination

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the destination host the virtual machine should be running on.

      Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_resourcepool:
      .. _parameter-resource_pool:

      **destination_resourcepool**

      aliases: resource_pool

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the destination resource pool where the virtual machine should be running.

      Resource pool is required if vmotion is done between hosts which are part of different clusters or datacenters.

      if not passed, resource\_pool object will be retrived from host\_obj parent.



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

      .. _parameter-moid:

      **moid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.

      This is required if \ :literal:`vm\_name`\  or \ :literal:`vm\_uuid`\  is not supplied.



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

      .. _parameter-timeout:

      **timeout**

      :literal:`integer`

      added in community.vmware 3.4.0


      .. raw:: html

        </div></div>

    - 
      The timeout in seconds. When the timeout is reached, the module will fail.


      Default: :literal:`3600`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-use_instance_uuid:

      **use_instance_uuid**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to use the VMware instance UUID rather than the BIOS UUID.


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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm:
      .. _parameter-vm_name:

      **vm_name**

      aliases: vm

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the VM to perform a vMotion on.

      This is required parameter, if \ :literal:`vm\_uuid`\  is not set.

      Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-uuid:
      .. _parameter-vm_uuid:

      **vm_uuid**

      aliases: uuid

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      UUID of the virtual machine to perform a vMotion operation on.

      This is a required parameter, if \ :literal:`vm\_name`\  or \ :literal:`moid`\  is not set.





Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Perform vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_host: 'destination_host_as_per_vcenter'
      delegate_to: localhost

    - name: Perform vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        moid: vm-42
        destination_host: 'destination_host_as_per_vcenter'
      delegate_to: localhost

    - name: Perform vMotion of virtual machine to resource_pool
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        moid: vm-42
        destination_host: 'destination_host_as_per_vcenter'
        destination_resourcepool: 'destination_resourcepool_as_per_vcenter'
      delegate_to: localhost

    - name: Perform storage vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_datastore: 'destination_datastore_as_per_vcenter'
      delegate_to: localhost

    - name: Perform storage vMotion and host vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_host: 'destination_host_as_per_vcenter'
        destination_datastore: 'destination_datastore_as_per_vcenter'
      delegate_to: localhost

    - name: Perform storage vMotion to a Storage Cluster and vMotion to a Cluster of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_cluster: 'destination_cluster_as_per_vcenter'
        destination_datastore_cluster: 'destination_datastore_cluster_as_per_vcenter'
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

      .. _return-datastore:

      **datastore**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      List the datastore the virtual machine is on.

      Only returned if there is asked for a Storage vMotion (Datastore or Datastore Cluster).


      Returned: changed or success

      Sample: :literal:`"datastore1"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-running_host:

      **running_host**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      List the host the virtual machine is registered to.

      Only returned if there is asked for a vMotion (Cluster or Host).


      Returned: changed or success

      Sample: :literal:`"host1.example.com"`




Authors
~~~~~~~

- Bede Carroll (@bedecarroll)
- Olivier Boukili (@oboukili)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

