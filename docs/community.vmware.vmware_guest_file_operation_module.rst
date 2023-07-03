

community.vmware.vmware_guest_file_operation module -- Files operation in a VMware guest operating system without network
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_file_operation`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Module to copy a file to a VM, fetch a file from a VM and create or delete a directory in the guest OS.








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
      The cluster hosting the virtual machine.

      If set, it will help to speed up virtual machine search.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-copy:

      **copy**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Copy file to vm without requiring network.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-copy/dest:

      **dest**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      File destination, path must be exist.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-copy/overwrite:

      **overwrite**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Overwrite or not.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-copy/src:

      **src**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      File source absolute or relative.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The datacenter hosting the virtual machine.

      If set, it will help to speed up virtual machine search.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directory:

      **directory**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Create or delete a directory.

      Can be used to create temp directory inside guest using mktemp operation.

      mktemp sets variable \ :literal:`dir`\  in the result with the name of the new directory.

      mktemp operation option is added in version 2.8.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directory/operation:

      **operation**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Operation to perform.


      Choices:

      - :literal:`"create"`
      - :literal:`"delete"`
      - :literal:`"mktemp"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directory/path:

      **path**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Directory path.

      Required for \ :literal:`create`\  or \ :literal:`remove`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directory/prefix:

      **prefix**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Temporary directory prefix.

      Required for \ :literal:`mktemp`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directory/recurse:

      **recurse**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Not required.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-directory/suffix:

      **suffix**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Temporary directory suffix.

      Required for \ :literal:`mktemp`\ .




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-fetch:

      **fetch**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Get file from virtual machine without requiring network.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-fetch/dest:

      **dest**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      File destination on localhost, path must be exist.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-fetch/src:

      **src**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The file on the remote system to fetch.

      This \ :emphasis:`must`\  be a file, not a directory.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute path to find an existing guest or create the new guest.

      The folder should include the datacenter. ESX's datacenter is ha-datacenter

      Used only if \ :literal:`vm\_id\_type`\  is \ :literal:`inventory\_path`\ .

      Examples:

         folder: /ha-datacenter/vm

         folder: ha-datacenter/vm

         folder: /datacenter1/vm

         folder: datacenter1/vm

         folder: /datacenter1/vm/folder1

         folder: datacenter1/vm/folder1

         folder: /folder1/datacenter1/vm

         folder: folder1/datacenter1/vm

         folder: /folder1/datacenter1/vm/folder2

         folder: vm/folder2

         folder: folder2



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

      .. _parameter-timeout:

      **timeout**

      :literal:`integer`

      added in community.vmware 3.1.0


      .. raw:: html

        </div></div>

    - 
      Timeout seconds for fetching or copying a file.


      Default: :literal:`100`


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

      .. _parameter-vm_id:

      **vm_id**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the virtual machine to work with.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_id_type:

      **vm_id_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The VMware identification method by which the virtual machine will be identified.


      Choices:

      - :literal:`"uuid"`
      - :literal:`"instance\_uuid"`
      - :literal:`"dns\_name"`
      - :literal:`"inventory\_path"`
      - :literal:`"vm\_name"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_password:

      **vm_password**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The password used to login-in to the virtual machine.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_username:

      **vm_username**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The user to login in to the virtual machine.





Notes
-----

- Only the first match against vm\_id is used, even if there are multiple matches
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Create directory inside a vm
      community.vmware.vmware_guest_file_operation:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        vm_id: "{{ guest_name }}"
        vm_username: "{{ guest_username }}"
        vm_password: "{{ guest_userpassword }}"
        directory:
          path: "/test"
          operation: create
          recurse: false
      delegate_to: localhost

    - name: copy file to vm
      community.vmware.vmware_guest_file_operation:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        vm_id: "{{ guest_name }}"
        vm_username: "{{ guest_username }}"
        vm_password: "{{ guest_userpassword }}"
        copy:
            src: "files/test.zip"
            dest: "/root/test.zip"
            overwrite: false
      delegate_to: localhost

    - name: fetch file from vm
      community.vmware.vmware_guest_file_operation:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        vm_id: "{{ guest_name }}"
        vm_username: "{{ guest_username }}"
        vm_password: "{{ guest_userpassword }}"
        fetch:
            src: "/root/test.zip"
            dest: "files/test.zip"
      delegate_to: localhost

    - name: If a timeout error occurs, specify a high(er) timeout value
      community.vmware.vmware_guest_file_operation:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        vm_id: "{{ guest_name }}"
        vm_username: "{{ guest_username }}"
        vm_password: "{{ guest_userpassword }}"
        timeout: 10000
        copy:
            src: "files/test.zip"
            dest: "/root/test.zip"
            overwrite: false
      delegate_to: localhost







Authors
~~~~~~~

- Stéphane Travassac (@stravassac)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

