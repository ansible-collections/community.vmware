

community.vmware.vmware_vm_shell module -- Run commands in a VMware guest operating system
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vm_shell`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Module allows user to run common system administration commands in the guest operating system.








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

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute or relative path to find an existing guest or create the new guest.

      The folder should include the datacenter. ESX's datacenter is ha-datacenter.

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

      .. raw:: html

        </div></div>

    - 
      Timeout in seconds.

      If set to positive integers, then \ :literal:`wait\_for\_process`\  will honor this parameter and will exit after this timeout.


      Default: :literal:`3600`


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

      .. _parameter-vm_shell:

      **vm_shell**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The absolute path to the program to start.

      On Linux, shell is executed via bash.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_shell_args:

      **vm_shell_args**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The argument to the program.

      The characters which must be escaped to the shell also be escaped on the command line provided.


      Default: :literal:`" "`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_shell_cwd:

      **vm_shell_cwd**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The current working directory of the application from which it will be run.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_shell_env:

      **vm_shell_env**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      Comma separated list of environment variable, specified in the guest OS notation.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_username:

      **vm_username**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The user to login-in to the virtual machine.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_for_process:

      **wait_for_process**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , module will wait for process to complete in the given virtual machine.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`





Notes
-----

- Only the first match against vm\_id is used, even if there are multiple matches.
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Run command inside a virtual machine
      community.vmware.vmware_vm_shell:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        folder: "/{{datacenter}}/vm"
        vm_id: "{{ vm_name }}"
        vm_username: root
        vm_password: superSecret
        vm_shell: /bin/echo
        vm_shell_args: " $var >> myFile "
        vm_shell_env:
          - "PATH=/bin"
          - "VAR=test"
        vm_shell_cwd: "/tmp"
      delegate_to: localhost
      register: shell_command_output

    - name: Run command inside a virtual machine with wait and timeout
      community.vmware.vmware_vm_shell:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        folder: "/{{datacenter}}/vm"
        vm_id: NameOfVM
        vm_username: root
        vm_password: superSecret
        vm_shell: /bin/sleep
        vm_shell_args: 100
        wait_for_process: true
        timeout: 2000
      delegate_to: localhost
      register: shell_command_with_wait_timeout

    - name: Change user password in the guest machine
      community.vmware.vmware_vm_shell:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        folder: "/{{datacenter}}/vm"
        vm_id: "{{ vm_name }}"
        vm_username: sample
        vm_password: old_password
        vm_shell: "/bin/echo"
        vm_shell_args: "-e 'old_password\nnew_password\nnew_password' | passwd sample > /tmp/$$.txt 2>&1"
      delegate_to: localhost

    - name: Change hostname of guest machine
      community.vmware.vmware_vm_shell:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        folder: "/{{datacenter}}/vm"
        vm_id: "{{ vm_name }}"
        vm_username: testUser
        vm_password: SuperSecretPassword
        vm_shell: "/usr/bin/hostnamectl"
        vm_shell_args: "set-hostname new_hostname > /tmp/$$.txt 2>&1"
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

      .. _return-results:

      **results**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the new process after completion with wait\_for\_process


      Returned: on success

      Sample: :literal:`{"cmd\_line": "\\"/bin/sleep\\" 1", "end\_time": "2018-04-26T05:03:21+00:00", "exit\_code": 0, "name": "sleep", "owner": "dev1", "start\_time": "2018-04-26T05:03:19+00:00", "uuid": "564db1e2-a3ff-3b0e-8b77-49c25570bb66"}`




Authors
~~~~~~~

- Ritesh Khadgaray (@ritzk)
- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

