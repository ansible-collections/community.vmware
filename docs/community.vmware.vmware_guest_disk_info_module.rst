

community.vmware.vmware_guest_disk_info module -- Gather info about disks of given virtual machine
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_guest_disk_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about disks belonging to given virtual machine.
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

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The datacenter name to which virtual machine belongs to.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute or relative path to find an existing guest.

      This is required parameter, only if multiple VMs are found with same name.

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

      This is required parameter, if parameter \ :literal:`uuid`\  or \ :literal:`moid`\  is not supplied.



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
      UUID of the instance to gather information if known, this is VMware's unique identifier.

      This is required parameter, if parameter \ :literal:`name`\  or \ :literal:`moid`\  is not supplied.



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

    
    - name: Gather disk info from virtual machine using UUID
      community.vmware.vmware_guest_disk_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
      delegate_to: localhost
      register: disk_info

    - name: Gather disk info from virtual machine using name
      community.vmware.vmware_guest_disk_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        name: VM_225
      delegate_to: localhost
      register: disk_info

    - name: Gather disk info from virtual machine using moid
      community.vmware.vmware_guest_disk_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        moid: vm-42
      delegate_to: localhost
      register: disk_info





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

      .. _return-guest_disk_info:

      **guest_disk_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine's disks


      Returned: always

      Sample: :literal:`{"0": {"backing\_datastore": "datastore2", "backing\_disk\_mode": "persistent", "backing\_diskmode": "persistent", "backing\_eagerlyscrub": false, "backing\_filename": "[datastore2] VM\_225/VM\_225.vmdk", "backing\_thinprovisioned": false, "backing\_type": "FlatVer2", "backing\_uuid": "200C3A00-f82a-97af-02ff-62a595f0020a", "backing\_writethrough": false, "capacity\_in\_bytes": 10485760, "capacity\_in\_kb": 10240, "controller\_bus\_number": 0, "controller\_key": 1000, "controller\_type": "paravirtual", "key": 2000, "label": "Hard disk 1", "summary": "10,240 KB", "unit\_number": 0}, "1": {"backing\_datastore": "datastore3", "backing\_devicename": "vml.012345678901234567890123456789012345678901234567890123", "backing\_disk\_mode": "independent\_persistent", "backing\_diskmode": "independent\_persistent", "backing\_filename": "[datastore3] VM\_226/VM\_226.vmdk", "backing\_lunuuid": "012345678901234567890123456789012345678901234567890123", "backing\_type": "RawDiskMappingVer1", "backing\_uuid": null, "capacity\_in\_bytes": 15728640, "capacity\_in\_kb": 15360, "controller\_bus\_number": 0, "controller\_key": 1000, "controller\_type": "paravirtual", "key": 2001, "label": "Hard disk 3", "summary": "15,360 KB", "unit\_number": 1}}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

