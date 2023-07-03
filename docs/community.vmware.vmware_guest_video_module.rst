

community.vmware.vmware_guest_video module -- Modify video card configurations of specified virtual machine in given vCenter infrastructure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_guest_video`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is used to reconfigure video card settings of given virtual machine.
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

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The datacenter name to which virtual machine belongs to.

      This parameter is case sensitive.


      Default: :literal:`"ha-datacenter"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-display_number:

      **display_number**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of display. Valid value from 1 to 10. The maximum display number is 4 on vCenter 6.0, 6.5 web UI.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable_3d:

      **enable_3D**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable 3D for guest operating systems on which VMware supports 3D.


      Choices:

      - :literal:`false`
      - :literal:`true`



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

      The folder should include the datacenter. ESXi server's datacenter is ha-datacenter.

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

      .. _parameter-gather_video_facts:

      **gather_video_facts**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , return settings of the video card, other attributes are ignored.

      If set to \ :literal:`false`\ , will do reconfiguration and return video card settings.


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

      .. _parameter-memory_3d_mb:

      **memory_3D_mb**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The value of 3D Memory must be power of 2 and valid value is from 32 MB to 2048 MB.



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

      .. _parameter-renderer_3d:

      **renderer_3D**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`automatic`\ , selects the appropriate option (software or hardware) for this virtual machine automatically.

      If set to \ :literal:`software`\ , uses normal CPU processing for 3D calculations.

      If set to \ :literal:`hardware`\ , requires graphics hardware (GPU) for faster 3D calculations.


      Choices:

      - :literal:`"automatic"`
      - :literal:`"software"`
      - :literal:`"hardware"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-use_auto_detect:

      **use_auto_detect**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , applies common video settings to the guest operating system, attributes \ :literal:`display\_number`\  and \ :literal:`video\_memory\_mb`\  are ignored.

      If set to \ :literal:`false`\ , the number of display and the total video memory will be reconfigured using \ :literal:`display\_number`\  and \ :literal:`video\_memory\_mb`\ .


      Choices:

      - :literal:`false`
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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-video_memory_mb:

      **video_memory_mb**

      :literal:`float`

      .. raw:: html

        </div></div>

    - 
      Valid total MB of video memory range of virtual machine is from 1.172 MB to 256 MB on ESXi 6.7U1, from 1.172 MB to 128 MB on ESXi 6.7 and previous versions.

      For specific guest OS, supported minimum and maximum video memory are different, please be careful on setting this.





Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Change video card settings of virtual machine
      community.vmware.vmware_guest_video:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: test-vm
        gather_video_facts: false
        use_auto_detect: false
        display_number: 2
        video_memory_mb: 8.0
        enable_3D: true
        renderer_3D: automatic
        memory_3D_mb: 512
      delegate_to: localhost
      register: video_facts

    - name: Change video card settings of virtual machine using MoID
      community.vmware.vmware_guest_video:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        moid: vm-42
        gather_video_facts: false
        use_auto_detect: false
        display_number: 2
        video_memory_mb: 8.0
        enable_3D: true
        renderer_3D: automatic
        memory_3D_mb: 512
      delegate_to: localhost
      register: video_facts

    - name: Gather video card settings of virtual machine
      community.vmware.vmware_guest_video:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: test-vm
        gather_video_facts: false
      delegate_to: localhost
      register: video_facts





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

      .. _return-video_status:

      **video_status**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine's video card after managing them


      Returned: always

      Sample: :literal:`{"auto\_detect": false, "display\_number": 2, "enable\_3D\_support": true, "memory\_3D": 524288, "renderer\_3D": "automatic", "video\_memory": 8192}`




Authors
~~~~~~~

- Diane Wang (@Tomorrow9) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

