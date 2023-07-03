

community.vmware.vmware_guest_boot_manager module -- Manage boot options for the given virtual machine
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_guest_boot_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage boot options for the given virtual machine.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-boot_delay:

      **boot_delay**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Delay in milliseconds before starting the boot sequence.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-boot_firmware:

      **boot_firmware**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Choose which firmware should be used to boot the virtual machine.


      Choices:

      - :literal:`"bios"`
      - :literal:`"efi"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-boot_hdd_name:

      **boot_hdd_name**

      :literal:`string`

      added in community.vmware 3.2.0


      .. raw:: html

        </div></div>

    - 
      Name of disk to be set as boot disk, which is case sensitive, e.g., 'Hard disk 1'.

      This parameter is optional, if not set, will use the first virtual disk found in VM device list.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-boot_order:

      **boot_order**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of the boot devices.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-boot_retry_delay:

      **boot_retry_delay**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Specify the time in milliseconds between virtual machine boot failure and subsequent attempt to boot again.

      If set, will automatically set \ :literal:`boot\_retry\_enabled`\  to \ :literal:`true`\  as this parameter is required.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-boot_retry_enabled:

      **boot_retry_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , the virtual machine that fails to boot, will try to boot again after \ :literal:`boot\_retry\_delay`\  is expired.

      If set to \ :literal:`false`\ , the virtual machine waits indefinitely for user intervention.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enter_bios_setup:

      **enter_bios_setup**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , the virtual machine automatically enters BIOS setup the next time it boots.

      The virtual machine resets this flag, so that the machine boots proceeds normally.


      Choices:

      - :literal:`false`
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
      Name of the VM to work with.

      This is required if \ :literal:`uuid`\  or \ :literal:`moid`\  parameter is not supplied.



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

      .. _parameter-secure_boot_enabled:

      **secure_boot_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Choose if EFI secure boot should be enabled.  EFI secure boot can only be enabled with boot\_firmware = efi


      Choices:

      - :literal:`false`
      - :literal:`true`



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
      UUID of the instance to manage if known, this is VMware's BIOS UUID by default.

      This is required if \ :literal:`name`\  or \ :literal:`moid`\  parameter is not supplied.



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

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Change virtual machine's boot order and related parameters
      community.vmware.vmware_guest_boot_manager:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: testvm
        boot_delay: 2000
        enter_bios_setup: true
        boot_retry_enabled: true
        boot_retry_delay: 22300
        boot_firmware: bios
        secure_boot_enabled: false
        boot_order:
          - floppy
          - cdrom
          - ethernet
          - disk
      delegate_to: localhost
      register: vm_boot_order

    - name: Change virtual machine's boot order using Virtual Machine MoID
      community.vmware.vmware_guest_boot_manager:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        moid: vm-42
        boot_delay: 2000
        enter_bios_setup: true
        boot_retry_enabled: true
        boot_retry_delay: 22300
        boot_firmware: bios
        secure_boot_enabled: false
        boot_order:
          - floppy
          - cdrom
          - ethernet
          - disk
      delegate_to: localhost
      register: vm_boot_order





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

      .. _return-vm_boot_status:

      **vm_boot_status**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about boot order of virtual machine


      Returned: always

      Sample: :literal:`{"current\_boot\_delay": 2000, "current\_boot\_firmware": "bios", "current\_boot\_order": ["floppy", "disk", "ethernet", "cdrom"], "current\_boot\_retry\_delay": 22300, "current\_boot\_retry\_enabled": true, "current\_enter\_bios\_setup": true, "current\_secure\_boot\_enabled": false, "previous\_boot\_delay": 10, "previous\_boot\_firmware": "efi", "previous\_boot\_order": ["ethernet", "cdrom", "floppy", "disk"], "previous\_boot\_retry\_delay": 10000, "previous\_boot\_retry\_enabled": true, "previous\_enter\_bios\_setup": false, "previous\_secure\_boot\_enabled": true}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

