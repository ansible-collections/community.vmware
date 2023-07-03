

community.vmware.vmware_guest_instant_clone module -- Instant Clone VM
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_instant_clone`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used for Creating a powered-on Instant Clone of a virtual machine.
- All variables and VMware object names are case sensitive.
- \ `community.vmware.vmware\_guest <vmware_guest_module.rst>`__\  module is needed for creating a VM with poweredon state which would be used as a parent VM.
- \ `community.vmware.vmware\_guest\_powerstate <vmware_guest_powerstate_module.rst>`__\  module is also needed to poweroff the instant cloned module.
- The powered off VM would in turn be deleted by again using \ `community.vmware.vmware\_guest <vmware_guest_module.rst>`__\  module.
- Thus \ `community.vmware.vmware\_guest <vmware_guest_module.rst>`__\  module is necessary for removing Instant Cloned VM when VMs being created in testing environment.
- Also GuestOS Customization has now been added with guestinfo\_vars parameter.
- The Parent VM must have The Guest customization Engine for instant Clone to customize Guest OS.
- Only Linux Os in Parent VM enable support for native vSphere Guest Customization for Instant Clone in vSphere 7.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

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

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the datastore or the datastore cluster.

      If datastore cluster name is specified, module will find the Storage DRS recommended datastore in that cluster.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute path to deploy the cloned vm.

      This parameter is case sensitive.

      Examples:

      folder: ha-datacenter/vm

      folder: /datacenter1/vm



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guestinfo_vars:

      **guestinfo_vars**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      Provides GuestOS Customization functionality in instant cloned VM.

      A list of key value pairs that will be passed to the destination VM.

      These pairs should be used to provide user-defined customization to differentiate the destination VM from the source VM.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guestinfo_vars/dns:

      **dns**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      dns is used to set the dns in Instant Cloned Guest Operating System..



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guestinfo_vars/domain:

      **domain**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      domain is used to set A fully qualified domain name (FQDN) or complete domain name for Instant Cloned Guest operating System.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guestinfo_vars/gateway:

      **gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      netmask is used to set the netmask in Instant Cloned Guest Operating System.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guestinfo_vars/hostname:

      **hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      hostname is used to obtain the DNS(Domain Name System) name and set the Guest system's hostname.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guestinfo_vars/ipaddress:

      **ipaddress**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      ipaddress is used to set the ipaddress in Instant Cloned Guest Operating System.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guestinfo_vars/netmask:

      **netmask**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      netmask is used to set the netmask in Instant Cloned Guest Operating System.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:
      .. _parameter-host:

      **host**

      aliases: esxi_hostname

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the ESX Host in datacenter in which to place cloned VM.

      The host has to be a member of the cluster that contains the resource pool.

      Required with \ :emphasis:`resource\_pool`\  to find resource pool details. This will be used as additional information when there are resource pools with same name.



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
      Managed Object ID of the vm instance to manage if known, this is a unique identifier only within a single vCenter instance.

      This is required if \ :literal:`parent\_vm`\  or \ :literal:`uuid`\  is not supplied.



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
      Name of the Cloned virtual machine.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-parent_vm:

      **parent_vm**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the parent virtual machine.

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

      .. _parameter-resource_pool:

      **resource_pool**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the resource pool in datacenter in which to place deployed VM.

      Required if \ :emphasis:`cluster`\  is not specified.

      For default or non-unique resource pool names, specify \ :emphasis:`host`\  and \ :emphasis:`cluster`\ .

      \ :literal:`Resources`\  is the default name of resource pool.



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
      UUID of the vm instance to clone from, this is VMware's unique identifier.

      This is a required parameter, if parameter \ :literal:`parent\_vm`\  or \ :literal:`moid`\  is not supplied.



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

      .. _parameter-vm_password:

      **vm_password**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The password used to login-in to the virtual machine.

      Only required when using guest customization feature.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_username:

      **vm_username**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The user to login-in to the virtual machine.

      Only required when using guest customization feature.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_vm_tools:

      **wait_vm_tools**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether waiting until vm tools start after rebooting an instant clone vm.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_vm_tools_timeout:

      **wait_vm_tools_timeout**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Define a timeout (in seconds) for \ :emphasis:`the wait\_vm\_tools`\  parameter.


      Default: :literal:`300`




Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Instant Clone a VM
      community.vmware.vmware_guest_instant_clone:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        folder: "{{ f0 }}"
        datastore: "{{ rw_datastore }}"
        datacenter: "{{ dc1 }}"
        host: "{{ esxi1 }}"
        name: "{{ Clone_vm }}"
        parent_vm: "{{ testvm_1 }}"
        resource_pool: "{{ test_resource_001 }}"
      register: vm_clone
      delegate_to: localhost

    - name: set state to poweroff the Cloned VM
      community.vmware.vmware_guest_powerstate:
        validate_certs: false
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: "cloned_vm_from_vm_cluster"
        folder: "{{ f0 }}"
        state: powered-off
      register: poweroff_instant_clone_from_vm_when_cluster
      delegate_to: localhost

    - name: Clean VM
      community.vmware.vmware_guest:
        validate_certs: false
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: "cloned_vm_from_vm_cluster"
        datacenter: "{{ dc1 }}"
        state: absent
      register: delete_instant_clone_from_vm_when_cluster
      ignore_errors: true
      delegate_to: localhost

    - name: Instant Clone a VM with guest_customization
      community.vmware.vmware_guest_instant_clone:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        vm_username: "root"
        vm_password: "SuperSecret"
        validate_certs: false
        folder: "{{ f0 }}"
        datastore: "{{ rw_datastore }}"
        datacenter: "{{ dc1 }}"
        host: "{{ esxi1 }}"
        guestinfo_vars:
          - hostname: "{{ guestinfo.ic.hostname }}"
            ipaddress: "{{ guestinfo.ic.ipaddress }}"
            netmask: "{{ guestinfo.ic.netmask }}"
            gateway: "{{ guestinfo.ic.gateway }}"
            dns: "{{ guestinfo.ic.dns }}"
            domain: "{{ guestinfo.ic.domain }}"
        name: "Instant_clone_guest_customize"
        parent_vm: "test_vm1"
        resource_pool: DC0_C0_RP1
      register: Instant_cloned_guest_customize
      delegate_to: localhost

    - name: Instant Clone a VM when skipping optional params
      community.vmware.vmware_guest_instant_clone:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        name: "{{ Clone_vm }}"
        parent_vm: "{{ testvm_1 }}"
        datacenter: "{{ dc1 }}"
        datastore: "{{ rw_datastore }}"
        host: "{{ esxi1 }}"
      register: VM_clone_optional_arguments
      delegate_to: localhost

    - name: Instant clone in check mode
      community.vmware.vmware_guest_instant_clone:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        folder: "{{ f0 }}"
        datastore: "{{ rw_datastore }}"
        datacenter: "{{ dc1 }}"
        host: "{{ esx1 }}"
        name: "{{ Clone_vm }}"
        parent_vm: "{{ testvm_2 }}"
        resource_pool: "{{ test_resource_001 }}"
      check_mode: true
      register: check_mode_clone
      delegate_to: localhost
    - debug:
        var: check_mode_clone






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

      added instance\_uuid from version 1.12.0


      Returned: always

      Sample: :literal:`{"datastore": "", "host": "", "instance\_uuid": "", "vcenter": "", "vm\_folder": "", "vm\_name": ""}`




Authors
~~~~~~~

- Anant Chopra (@Anant99-sys)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

