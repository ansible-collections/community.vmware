

community.vmware.vmware_guest_controller module -- Manage disk or USB controllers related to virtual machine in given vCenter infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_controller`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add, remove disk controllers or USB controllers belonging to given virtual machine.
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

      .. _parameter-controllers:

      **controllers**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of disk or USB controllers to add or remove.

      Total 4 disk controllers with the same type are allowed per VM.

      Total 2 USB controllers are allowed per VM, 1 USB 2.0 and 1 USB 3.0 or 3.1.

      For specific guest OS, supported controller types please refer to VMware Compatibility Guide.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-controllers/bus_sharing:

      **bus_sharing**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Bus sharing type for SCSI controller.


      Choices:

      - :literal:`"noSharing"` ← (default)
      - :literal:`"physicalSharing"`
      - :literal:`"virtualSharing"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-controllers/controller_number:

      **controller_number**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Disk controller bus number. When \ :literal:`state`\  is set to \ :literal:`absent`\ , this parameter is required.

      When \ :literal:`type`\  set to \ :literal:`usb2`\  or \ :literal:`usb3`\ , this parameter is not required.


      Choices:

      - :literal:`0`
      - :literal:`1`
      - :literal:`2`
      - :literal:`3`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-controllers/state:

      **state**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Add new controller or remove specified existing controller.

      If \ :literal:`state`\  is set to \ :literal:`absent`\ , the specified controller will be removed from virtual machine when there is no disk or device attaching to it.

      If specified controller is removed or not exist, no action will be taken only warning message.

      If \ :literal:`state`\  is set to \ :literal:`present`\ , new controller with specified type will be added.

      If the number of controller with specified controller type reaches it's maximum, no action will be taken only warning message.


      Choices:

      - :literal:`"present"`
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-controllers/type:

      **type**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Type of disk or USB controller.

      From vSphere 6.5 and virtual machine with hardware version 13, \ :literal:`nvme`\  controller starts to be supported.


      Choices:

      - :literal:`"buslogic"`
      - :literal:`"lsilogic"`
      - :literal:`"lsilogicsas"`
      - :literal:`"paravirtual"`
      - :literal:`"sata"`
      - :literal:`"nvme"`
      - :literal:`"usb2"`
      - :literal:`"usb3"`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The datacenter name to which virtual machine belongs to.


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

      This is a required parameter, only if multiple VMs are found with same name.

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

      .. _parameter-gather_disk_controller_facts:

      **gather_disk_controller_facts**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to collect existing disk and USB controllers facts only.

      When this parameter is set to \ :literal:`true`\ , \ :literal:`controllers`\  parameter will be ignored.


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
      Name of the virtual machine.

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

      .. _parameter-sleep_time:

      **sleep_time**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The sleep time in seconds after VM reconfigure task completes, used when not get the updated VM controller facts after VM reconfiguration.

      This parameter is not required. Maximum value is 600.


      Default: :literal:`10`


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
      UUID of the instance to gather facts if known, this is VMware's unique identifier.

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

    
    - name: Add disk and USB 3.0 controllers for virtual machine located by name
      community.vmware.vmware_guest_controller:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: test_VM
        controllers:
          - state: present
            type: sata
          - state: present
            type: nvme
          - state: present
            type: usb3
      delegate_to: localhost
      register: disk_controller_facts

    - name: Remove disk controllers and USB 2.0 from virtual machine located by moid
      community.vmware.vmware_guest_controller:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        moid: vm-33
        controllers:
          - state: absent
            controller_number: 1
            type: sata
          - state: absent
            controller_number: 0
            type: nvme
          - state: absent
            type: usb2
      delegate_to: localhost
      register: disk_controller_facts





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

      .. _return-disk_controller_status:

      **disk_controller_status**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine's existing disk controllers or after adding or removing operation


      Returned: always

      Sample: :literal:`{"nvme": {"0": {"controller\_busnumber": 0, "controller\_controllerkey": 100, "controller\_devicekey": 31000, "controller\_disks\_devicekey": [], "controller\_label": "NVME controller 0", "controller\_summary": "NVME controller 0", "controller\_unitnumber": 30}}, "sata": {"0": {"controller\_busnumber": 0, "controller\_controllerkey": 100, "controller\_devicekey": 15000, "controller\_disks\_devicekey": [16000, 16001], "controller\_label": "SATA controller 0", "controller\_summary": "AHCI", "controller\_unitnumber": 24}}, "scsi": {"0": {"controller\_bus\_sharing": "noSharing", "controller\_busnumber": 0, "controller\_controllerkey": 100, "controller\_devicekey": 1000, "controller\_disks\_devicekey": [2000], "controller\_label": "SCSI controller 0", "controller\_summary": "LSI Logic SAS", "controller\_unitnumber": 3}, "1": {"controller\_bus\_sharing": "physicalSharing", "controller\_busnumber": 1, "controller\_controllerkey": 100, "controller\_devicekey": 1001, "controller\_disks\_devicekey": [], "controller\_label": "SCSI controller 1", "controller\_summary": "VMware paravirtual SCSI", "controller\_unitnumber": 4}}, "usb2": {"0": {"controller\_busnumber": 0, "controller\_controllerkey": 100, "controller\_devicekey": 7000, "controller\_disks\_devicekey": [], "controller\_label": "USB Controller", "controller\_summary": "Auto connect Disabled", "controller\_unitnumber": 22}}}`




Authors
~~~~~~~

- Diane Wang (@Tomorrow9) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

