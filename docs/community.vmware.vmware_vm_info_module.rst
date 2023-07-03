

community.vmware.vmware_vm_info module -- Return basic info pertaining to a VMware machine guest
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vm_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Return basic information pertaining to a vSphere or ESXi virtual machine guest.
- Cluster name as fact is added in version 2.7.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specify a folder location of VMs to gather information from.

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

      .. _parameter-show_allocated:

      **show_allocated**

      :literal:`boolean`

      added in community.vmware 2.5.0


      .. raw:: html

        </div></div>

    - 
      Allocated storage in byte and memory in MB are shown if it set to True.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_attribute:

      **show_attribute**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Attributes related to VM guest shown in information only when this is set \ :literal:`true`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_cluster:

      **show_cluster**

      :literal:`boolean`

      added in community.vmware 3.5.0


      .. raw:: html

        </div></div>

    - 
      Tags virtual machine's cluster is shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_datacenter:

      **show_datacenter**

      :literal:`boolean`

      added in community.vmware 3.5.0


      .. raw:: html

        </div></div>

    - 
      Tags virtual machine's datacenter is shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_datastore:

      **show_datastore**

      :literal:`boolean`

      added in community.vmware 3.5.0


      .. raw:: html

        </div></div>

    - 
      Tags virtual machine's datastore is shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_esxi_hostname:

      **show_esxi_hostname**

      :literal:`boolean`

      added in community.vmware 3.5.0


      .. raw:: html

        </div></div>

    - 
      Tags virtual machine's ESXi host is shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_folder:

      **show_folder**

      :literal:`boolean`

      added in community.vmware 3.7.0


      .. raw:: html

        </div></div>

    - 
      Show folders


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_mac_address:

      **show_mac_address**

      :literal:`boolean`

      added in community.vmware 3.5.0


      .. raw:: html

        </div></div>

    - 
      Tags virtual machine's mac address is shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_net:

      **show_net**

      :literal:`boolean`

      added in community.vmware 3.5.0


      .. raw:: html

        </div></div>

    - 
      Tags virtual machine's network is shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_resource_pool:

      **show_resource_pool**

      :literal:`boolean`

      added in community.vmware 3.5.0


      .. raw:: html

        </div></div>

    - 
      Tags virtual machine's resource pool is shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_tag:

      **show_tag**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Tags related to virtual machine are shown if set to \ :literal:`true`\ .


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

      .. _parameter-vm_name:

      **vm_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the virtual machine to get related configurations information from.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_type:

      **vm_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`vm`\ , then information are gathered for virtual machines only.

      If set to \ :literal:`template`\ , then information are gathered for virtual machine templates only.

      If set to \ :literal:`all`\ , then information are gathered for all virtual machines and virtual machine templates.


      Choices:

      - :literal:`"all"` ← (default)
      - :literal:`"vm"`
      - :literal:`"template"`





Notes
-----

- Fact about \ :literal:`moid`\  added in VMware collection 1.4.0.
- Fact about \ :literal:`datastore\_url`\  is added in VMware collection 1.18.0.
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Gather all registered virtual machines
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost
      register: vminfo

    - debug:
        var: vminfo.virtual_machines

    - name: Gather one specific VM
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
      delegate_to: localhost
      register: vm_info

    - debug:
        var: vminfo.virtual_machines

    - name: Gather only registered virtual machine templates
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_type: template
      delegate_to: localhost
      register: template_info

    - debug:
        var: template_info.virtual_machines

    - name: Gather only registered virtual machines
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_type: vm
      delegate_to: localhost
      register: vm_info

    - debug:
        var: vm_info.virtual_machines

    - name: Get UUID from given VM Name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
            folder: "/datacenter/vm/folder"
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.uuid }}"
          with_items:
            - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"

    - name: Get Tags from given VM Name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
            folder: "/datacenter/vm/folder"
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.tags }}"
          with_items:
            - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"

    - name: Gather all VMs from a specific folder
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        folder: "/Asia-Datacenter1/vm/prod"
      delegate_to: localhost
      register: vm_info

    - name: Get datastore_url from given VM name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.datastore_url }}"
          with_items:
            - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"





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

      .. _return-virtual_machines:

      **virtual_machines**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      list of dictionary of virtual machines and their information


      Returned: success

      Sample: :literal:`[{"allocated": {"cpu": 2, "memory": 16, "storage": 500000000}, "attributes": {"job": "backup-prepare"}, "cluster": null, "datacenter": "Datacenter-1", "datastore\_url": [{"name": "t880-o2g", "url": "/vmfs/volumes/e074264a-e5c82a58"}], "esxi\_hostname": "10.76.33.226", "folder": "/Datacenter-1/vm", "guest\_fullname": "Ubuntu Linux (64-bit)", "guest\_name": "ubuntu\_t", "ip\_address": "", "mac\_address": ["00:50:56:87:a5:9a"], "moid": "vm-24", "power\_state": "poweredOff", "tags": [{"category\_id": "urn:vmomi:InventoryServiceCategory:b316cc45-f1a9-4277-811d-56c7e7975203:GLOBAL", "category\_name": "cat\_0001", "description": "", "id": "urn:vmomi:InventoryServiceTag:43737ec0-b832-4abf-abb1-fd2448ce3b26:GLOBAL", "name": "tag\_0001"}], "uuid": "4207072c-edd8-3bd5-64dc-903fd3a0db04", "vm\_network": {"00:50:56:87:a5:9a": {"ipv4": ["10.76.33.228"], "ipv6": []}}}]`




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Fedor Vompe (@sumkincpp)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

