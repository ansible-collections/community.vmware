

community.vmware.vmware_content_deploy_ovf_template module -- Deploy Virtual Machine from ovf template stored in content library.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.
    You need further requirements to be able to use this module,
    see `Requirements <ansible_collections.community.vmware.vmware_content_deploy_ovf_template_module_requirements_>`_ for details.

    To use it in a playbook, specify: :code:`community.vmware.vmware_content_deploy_ovf_template`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Module to deploy virtual machine from ovf template in content library.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_content_deploy_ovf_template_module_requirements:

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

      .. _parameter-cluster:

      **cluster**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the cluster in datacenter in which to place deployed VM.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the datacenter, where VM to be deployed.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore:

      **datastore**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the datastore to store deployed VM and disk.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore_cluster:

      **datastore_cluster**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the datastore cluster housing a datastore to store deployed VM and disk.

      If datastore is not specified, the recommended datastore from this cluster will be used.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the folder in datacenter in which to place deployed VM.


      Default: :literal:`"vm"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-host:

      **host**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the ESX Host in datacenter in which to place deployed VM. The host has to be a member of the cluster that contains the resource pool.



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

      .. _parameter-content_library:
      .. _parameter-content_library_src:
      .. _parameter-library:

      **library**

      aliases: content_library, content_library_src

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The name of the content library from where the template resides.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-log_level:

      **log_level**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The level of logging desired in this module.


      Choices:

      - :literal:`"debug"`
      - :literal:`"info"`
      - :literal:`"normal"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:
      .. _parameter-vm_name:

      **name**

      aliases: vm_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the VM to be deployed.



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

      .. _parameter-resource_pool:

      **resource_pool**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the resourcepool in datacenter in which to place deployed VM.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-storage_provisioning:

      **storage_provisioning**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Default storage provisioning type to use for all sections of type vmw:StorageSection in the OVF descriptor.


      Choices:

      - :literal:`"thin"` ← (default)
      - :literal:`"thick"`
      - :literal:`"eagerZeroedThick"`
      - :literal:`"eagerzeroedthick"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ovf:
      .. _parameter-ovf_template:
      .. _parameter-template:
      .. _parameter-template_src:

      **template**

      aliases: ovf, ovf_template, template_src

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of OVF template from which VM to be deployed.



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

.. code-block:: yaml+jinja

    
    - name: Deploy Virtual Machine from OVF template in content library
      community.vmware.vmware_content_deploy_ovf_template:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        ovf_template: rhel_test_template
        datastore: Shared_NFS_Volume
        folder: vm
        datacenter: Sample_DC_1
        name: Sample_VM
        resource_pool: test_rp
      delegate_to: localhost

    - name: Deploy Virtual Machine from OVF template in content library with eagerZeroedThick storage
      vmware_content_deploy_ovf_template:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        ovf_template: rhel_test_template
        datastore: Shared_NFS_Volume
        folder: vm
        datacenter: Sample_DC_1
        name: Sample_VM
        resource_pool: test_rp
        storage_provisioning: eagerZeroedThick
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

      .. _return-vm_deploy_info:

      **vm_deploy_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      Virtual machine deployment message and vm\_id


      Returned: on success

      Sample: :literal:`{"msg": "Deployed Virtual Machine 'Sample\_VM'.", "vm\_id": "vm-1009"}`




Authors
~~~~~~~

- Lev Goncharv (@ultral)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

