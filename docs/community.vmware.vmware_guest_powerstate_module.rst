

community.vmware.vmware_guest_powerstate module -- Manages power states of virtual machines in vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_powerstate`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Power on / Power off / Restart a virtual machine.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-answer:

      **answer**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of questions to answer, should one or more arise while waiting for the task to complete.

      Some common uses are to allow a cdrom to be changed even if locked, or to answer the question as to whether a VM was copied or moved.

      The \ :emphasis:`answer`\  can be used if \ :emphasis:`state`\  is \ :literal:`powered-on`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-answer/question:

      **question**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The message id, for example \ :literal:`msg.uuid.altered`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-answer/response:

      **response**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The choice key, for example \ :literal:`button.uuid.copiedTheVM`\ .




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The \ :emphasis:`datacenter`\  where the VM you'd like to operate the power.

      This parameter is case sensitive.


      Default: :literal:`"ha-datacenter"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute or relative path to find an existing guest.

      The folder should include the datacenter. ESX's datacenter is ha-datacenter

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

      .. _parameter-force:

      **force**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Ignore warnings and complete the actions.

      This parameter is useful while forcing virtual machine state.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



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

      This is required if \ :literal:`name`\  or \ :literal:`uuid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the virtual machine to work with.

      Virtual machine names in vCenter are not necessarily unique, which may be problematic, see \ :literal:`name\_match`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name_match:

      **name_match**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If multiple virtual machines matching the name, use the first or last found.


      Choices:

      - :literal:`"first"` ← (default)
      - :literal:`"last"`



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

      .. _parameter-schedule_task_description:

      **schedule_task_description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Description of schedule task.

      Valid only if \ :literal:`scheduled\_at`\  is specified.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-schedule_task_enabled:

      **schedule_task_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Flag to indicate whether the scheduled task is enabled or disabled.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-schedule_task_name:

      **schedule_task_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of schedule task.

      Valid only if \ :literal:`scheduled\_at`\  is specified.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-scheduled_at:

      **scheduled_at**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Date and time in string format at which specified task needs to be performed.

      The required format for date and time - 'dd/mm/yyyy hh:mm'.

      Scheduling task requires vCenter server. A standalone ESXi server does not support this option.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Set the state of the virtual machine.


      Choices:

      - :literal:`"powered-off"`
      - :literal:`"powered-on"`
      - :literal:`"reboot-guest"`
      - :literal:`"restarted"`
      - :literal:`"shutdown-guest"`
      - :literal:`"suspended"`
      - :literal:`"present"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state_change_timeout:

      **state_change_timeout**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      If the \ :literal:`state`\  is set to \ :literal:`shutdown-guest`\ , by default the module will return immediately after sending the shutdown signal.

      If this argument is set to a positive integer, the module will instead wait for the VM to reach the poweredoff state.

      The value sets a timeout in seconds for the module to wait for the state change.


      Default: :literal:`0`


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
      UUID of the instance to manage if known, this is VMware's unique identifier.

      This is required if \ :literal:`name`\  or \ :literal:`moid`\  is not supplied.



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

    
    - name: Set the state of a virtual machine to poweroff
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: "/{{ datacenter_name }}/vm/my_folder"
        name: "{{ guest_name }}"
        state: powered-off
      delegate_to: localhost
      register: deploy

    - name: Set the state of a virtual machine to poweron using MoID
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: "/{{ datacenter_name }}/vm/my_folder"
        moid: vm-42
        state: powered-on
      delegate_to: localhost
      register: deploy

    - name: Set the state of a virtual machine to poweroff at given scheduled time
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: "/{{ datacenter_name }}/vm/my_folder"
        name: "{{ guest_name }}"
        state: powered-off
        scheduled_at: "09/01/2018 10:18"
        schedule_task_name: "task_00001"
        schedule_task_description: "Sample task to poweroff VM"
        schedule_task_enabled: true
      delegate_to: localhost
      register: deploy_at_schedule_datetime

    - name: Wait for the virtual machine to shutdown
      community.vmware.vmware_guest_powerstate:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: "{{ guest_name }}"
        state: shutdown-guest
        state_change_timeout: 200
      delegate_to: localhost
      register: deploy

    - name: Automatically answer if a question locked a virtual machine
      block:
        - name: Power on a virtual machine without the answer param
          community.vmware.vmware_guest_powerstate:
            hostname: "{{ esxi_hostname }}"
            username: "{{ esxi_username }}"
            password: "{{ esxi_password }}"
            validate_certs: false
            folder: "{{ f1 }}"
            name: "{{ vm_name }}"
            state: powered-on
      rescue:
        - name: Power on a virtual machine with the answer param
          community.vmware.vmware_guest_powerstate:
            hostname: "{{ esxi_hostname }}"
            username: "{{ esxi_username }}"
            password: "{{ esxi_password }}"
            validate_certs: false
            folder: "{{ f1 }}"
            name: "{{ vm_name }}"
            answer:
              - question: "msg.uuid.altered"
                response: "button.uuid.copiedTheVM"
            state: powered-on







Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

