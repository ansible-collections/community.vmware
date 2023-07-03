

community.vmware.vmware_guest_cross_vc_clone module -- Cross-vCenter VM/template clone
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_cross_vc_clone`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used for Cross-vCenter vm/template clone








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_datastore:

      **destination_datastore**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the destination datastore or the datastore cluster.

      If datastore cluster name is specified, we will find the Storage DRS recommended datastore in that cluster.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_host:

      **destination_host**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the destination host.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_resource_pool:

      **destination_resource_pool**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination resource pool.

      If not provided, the destination host's parent's resource pool will be used.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vcenter:

      **destination_vcenter**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The hostname or IP address of the destination VCenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vcenter_password:

      **destination_vcenter_password**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The password of the destination VCenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vcenter_port:

      **destination_vcenter_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The port to establish connection in the destination VCenter.


      Default: :literal:`443`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vcenter_username:

      **destination_vcenter_username**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The username of the destination VCenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vcenter_validate_certs:

      **destination_vcenter_validate_certs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Parameter to indicate if certification validation needs to be done on destination VCenter.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vm_folder:

      **destination_vm_folder**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute path to deploy the cloned vm.

      This parameter is case sensitive.

      Examples:

         folder: vm

         folder: ha-datacenter/vm

         folder: /datacenter1/vm



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vm_name:

      **destination_vm_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the cloned VM.



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

      .. _parameter-is_template:

      **is_template**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Specifies whether or not the new virtual machine should be marked as a template.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-moid:

      **moid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Managed Object ID of the vm/template instance to manage if known, this is a unique identifier only within a single vCenter instance.

      This is required if \ :literal:`name`\  or \ :literal:`uuid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the virtual machine or template.

      This is a required parameter, if parameter \ :literal:`uuid`\  or \ :literal:`moid`\  is not supplied.



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
      The state of Virtual Machine deployed.

      If set to \ :literal:`present`\  and VM does not exists, then VM is created.

      If set to \ :literal:`present`\  and VM exists, no action is taken.

      If set to \ :literal:`poweredon`\  and VM does not exists, then VM is created with powered on state.

      If set to \ :literal:`poweredon`\  and VM exists, no action is taken.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"poweredon"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-timeout:

      **timeout**

      :literal:`integer`

      added in community.vmware 3.5.0


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

      .. _parameter-uuid:

      **uuid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      UUID of the vm/template instance to clone from, this is VMware's unique identifier.

      This is a required parameter, if parameter \ :literal:`name`\  or \ :literal:`moid`\  is not supplied.



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

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    # Clone template
    - name: clone a template across VC
      community.vmware.vmware_guest_cross_vc_clone:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        name: "test_vm1"
        destination_vm_name: "cloned_vm_from_template"
        destination_vcenter: '{{ destination_vcenter_hostname }}'
        destination_vcenter_username: '{{ destination_vcenter_username }}'
        destination_vcenter_password: '{{ destination_vcenter_password }}'
        destination_vcenter_port: '{{ destination_vcenter_port }}'
        destination_vcenter_validate_certs: '{{ destination_vcenter_validate_certs }}'
        destination_host: '{{ destination_esxi }}'
        destination_datastore: '{{ destination_datastore }}'
        destination_vm_folder: '{{ destination_vm_folder }}'
        state: present
      register: cross_vc_clone_from_template

    - name: clone a VM across VC
      community.vmware.vmware_guest_cross_vc_clone:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: "{{ vcenter_password }}"
        name: "test_vm1"
        destination_vm_name: "cloned_vm_from_vm"
        destination_vcenter: '{{ destination_vcenter_hostname }}'
        destination_vcenter_username: '{{ destination_vcenter_username }}'
        destination_vcenter_password: '{{ destination_vcenter_password }}'
        destination_host: '{{ destination_esxi }}'
        destination_datastore: '{{ destination_datastore }}'
        destination_vm_folder: '{{ destination_vm_folder }}'
        state: poweredon
      register: cross_vc_clone_from_vm

    - name: check_mode support
      community.vmware.vmware_guest_cross_vc_clone:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: "{{ vcenter_password }}"
        name: "test_vm1"
        destination_vm_name: "cloned_vm_from_vm"
        destination_vcenter: '{{ destination_vcenter_hostname }}'
        destination_vcenter_username: '{{ destination_vcenter_username }}'
        destination_vcenter_password: '{{ destination_vcenter_password }}'
        destination_host: '{{ destination_esxi }}'
        destination_datastore: '{{ destination_datastore }}'
        destination_vm_folder: '{{ destination_vm_folder }}'
      check_mode: true





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

      .. _return-vm_info:

      **vm_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine


      Returned: always

      Sample: :literal:`{"datastore": "", "host": "", "power\_on": "", "vcenter": "", "vm\_folder": "", "vm\_name": ""}`




Authors
~~~~~~~

- Anusha Hegde (@anusha94)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

