

community.vmware.vmware_guest_info module -- Gather info about a single VM
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Gather information about a single VM on a VMware ESX cluster.








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
      Destination datacenter for the deploy operation



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute or relative path to find an existing guest.

      This is required if name is supplied.

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
      Name of the VM to work with

      This is required if \ :literal:`uuid`\  or \ :literal:`moid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name_match:

      **name_match**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If multiple VMs matching the name, use the first or last found


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

      .. _parameter-properties:

      **properties**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      Specify the properties to retrieve.

      If not specified, all properties are retrieved (deeply).

      Results are returned in a structure identical to the vsphere API.

      Example:

         properties: [

            "config.hardware.memoryMB",

            "config.hardware.numCPU",

            "guest.disk",

            "overallStatus"

         ]

      Only valid when \ :literal:`schema`\  is \ :literal:`vsphere`\ .



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

      .. _parameter-schema:

      **schema**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specify the output schema desired.

      The 'summary' output schema is the legacy output from the module

      The 'vsphere' output schema is the vSphere API class definition which requires pyvmomi\>6.7.1


      Choices:

      - :literal:`"summary"` ← (default)
      - :literal:`"vsphere"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-tag_details:

      **tag_details**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set \ :literal:`true`\ , detail information about 'tags' returned.

      Without this flag, the 'tags' returns a list of tag names.

      With this flag, the 'tags' returns a list of dict about tag information with additional details like category name, category id, and tag id.

      This parameter is added to maintain backward compatability.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-tags:

      **tags**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to show tags or not.

      If set \ :literal:`true`\ , shows tags information. Returns a list of tag names.

      If set \ :literal:`false`\ , hides tags information.

      vSphere Automation SDK is required.


      Choices:

      - :literal:`false` ← (default)
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

    
    - name: Gather info from standalone ESXi server having datacenter as 'ha-datacenter'
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
      delegate_to: localhost
      register: info

    - name: Gather some info from a guest using the vSphere API output schema
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: "{{ vm_name }}"
        schema: "vsphere"
        properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
      delegate_to: localhost
      register: info

    - name: Gather some information about a guest using MoID
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        moid: vm-42
        schema: "vsphere"
        properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
      delegate_to: localhost
      register: vm_moid_info

    - name: Gather Managed object ID (moid) from a guest using the vSphere API output schema for REST Calls
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: "{{ vm_name }}"
        schema: "vsphere"
        properties:
          - _moId
      delegate_to: localhost
      register: moid_info

    - name: Gather detailed information about tags and category associated with the given VM
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: "{{ vm_name }}"
        tags: true
        tag_details: true
      register: detailed_tag_info





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

      .. _return-instance:

      **instance**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine


      Returned: always

      Sample: :literal:`{"advanced\_settings": {}, "annotation": "", "current\_snapshot": null, "customvalues": {}, "guest\_consolidation\_needed": false, "guest\_question": null, "guest\_tools\_status": "guestToolsNotRunning", "guest\_tools\_version": "10247", "hw\_cores\_per\_socket": 1, "hw\_datastores": ["ds\_226\_3"], "hw\_esxi\_host": "10.76.33.226", "hw\_eth0": {"addresstype": "assigned", "ipaddresses": null, "label": "Network adapter 1", "macaddress": "00:50:56:87:a5:9a", "macaddress\_dash": "00-50-56-87-a5-9a", "portgroup\_key": null, "portgroup\_portkey": null, "summary": "VM Network"}, "hw\_files": ["[ds\_226\_3] ubuntu\_t/ubuntu\_t.vmx", "[ds\_226\_3] ubuntu\_t/ubuntu\_t.nvram", "[ds\_226\_3] ubuntu\_t/ubuntu\_t.vmsd", "[ds\_226\_3] ubuntu\_t/vmware.log", "[ds\_226\_3] u0001/u0001.vmdk"], "hw\_folder": "/DC0/vm/Discovered virtual machine", "hw\_guest\_full\_name": null, "hw\_guest\_ha\_state": null, "hw\_guest\_id": null, "hw\_interfaces": ["eth0"], "hw\_is\_template": false, "hw\_memtotal\_mb": 1024, "hw\_name": "ubuntu\_t", "hw\_power\_status": "poweredOff", "hw\_processor\_count": 1, "hw\_product\_uuid": "4207072c-edd8-3bd5-64dc-903fd3a0db04", "hw\_version": "vmx-13", "instance\_uuid": "5007769d-add3-1e12-f1fe-225ae2a07caf", "ipv4": null, "ipv6": null, "module\_hw": true, "moid": "vm-42", "snapshots": [], "tags": ["backup"], "vimref": "vim.VirtualMachine:vm-42", "vnc": {}}`




Authors
~~~~~~~

- Loic Blot (@nerzhul) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

