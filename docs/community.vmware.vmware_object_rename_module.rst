

community.vmware.vmware_object_rename module -- Renames VMware objects
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this module,
see `Requirements <ansible_collections.community.vmware.vmware_object_rename_module_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_object_rename`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to rename VMware objects.
- All variables and VMware object names are case sensitive.
- Renaming Host and Network is not supported by VMware APIs.



.. _ansible_collections.community.vmware.vmware_object_rename_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- vSphere Automation SDK






Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hostname:

      **hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The hostname or IP address of the vSphere vCenter server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_HOST`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-new_name:
      .. _parameter-object_new_name:

      **new_name**

      aliases: object_new_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      New name for VMware object.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-object_moid:

      **object_moid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Managed object id of the VMware object to work with.

      Mutually exclusive with \ :literal:`object\_name`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-object_name:

      **object_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the object to work with.

      Mutually exclusive with \ :literal:`object\_moid`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-object_type:

      **object_type**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Type of object to work with.

      Valid options are Cluster, ClusterComputeResource, Datacenter, Datastore, Folder, ResourcePool, VM or VirtualMachine.


      Choices:

      - :literal:`"ClusterComputeResource"`
      - :literal:`"Cluster"`
      - :literal:`"Datacenter"`
      - :literal:`"Datastore"`
      - :literal:`"Folder"`
      - :literal:`"Network"`
      - :literal:`"ResourcePool"`
      - :literal:`"VM"`
      - :literal:`"VirtualMachine"`



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
      The password of the vSphere vCenter server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PASSWORD`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port:

      **port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The port number of the vSphere vCenter.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PORT`\  will be used instead.


      Default: :literal:`443`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-protocol:

      **protocol**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The connection to protocol.


      Choices:

      - :literal:`"http"`
      - :literal:`"https"` ← (default)



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

      .. _parameter-admin:
      .. _parameter-user:
      .. _parameter-username:

      **username**

      aliases: admin, user

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The username of the vSphere vCenter server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_USER`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allows connection when SSL certificates are not valid.

      Set to \ :literal:`false`\  when certificates are not trusted.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_VALIDATE\_CERTS`\  will be used instead.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)







Examples
--------

.. code-block:: yaml

    
    - name: Rename a virtual machine
      community.vmware.vmware_object_rename:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        new_name: Fedora_31
        object_name: Fedora_VM
        object_type: VirtualMachine
      delegate_to: localhost

    - name: Rename a virtual machine using moid
      community.vmware.vmware_object_rename:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        new_name: Fedora_31
        object_moid: vm-14
        object_type: VirtualMachine
      delegate_to: localhost

    - name: Rename a datacenter
      community.vmware.vmware_object_rename:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        new_name: Asia_Datacenter
        object_name: dc1
        object_type: Datacenter
      delegate_to: localhost

    - name: Rename a folder with moid
      community.vmware.vmware_object_rename:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        new_name: backup
        object_moid: group-v46
        object_type: Folder
      delegate_to: localhost

    - name: Rename a cluster with moid
      community.vmware.vmware_object_rename:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        new_name: CCR_1
        object_moid: domain-c33
        object_type: Cluster
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

      .. _return-rename_status:

      **rename_status**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about VMware object rename operation


      Returned: on success

      Sample: :literal:`{"current\_name": "Fedora\_31", "desired\_name": "Fedora\_31", "previous\_name": "Fedora\_VM"}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

