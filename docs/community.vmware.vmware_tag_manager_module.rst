

community.vmware.vmware_tag_manager module -- Manage association of VMware tags with VMware objects
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this module,
see `Requirements <ansible_collections.community.vmware.vmware_tag_manager_module_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_tag_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to assign / remove VMware tags from the given VMware objects.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_tag_manager_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- vSphere Automation SDK






Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hostname:

      **hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The hostname or IP address of the vSphere vCenter server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_HOST`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-moid:

      **moid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Managed object ID for the given object.

      Required if \ :literal:`object\_name`\  is not set.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-object_name:

      **object_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the object to work with.

      For DistributedVirtualPortgroups the format should be "switch\_name:portgroup\_name"

      Required if \ :literal:`moid`\  is not set.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-object_type:

      **object_type**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Type of object to work with.


      Choices:

      - :literal:`"VirtualMachine"`
      - :literal:`"Datacenter"`
      - :literal:`"ClusterComputeResource"`
      - :literal:`"HostSystem"`
      - :literal:`"DistributedVirtualSwitch"`
      - :literal:`"DistributedVirtualPortgroup"`
      - :literal:`"Datastore"`
      - :literal:`"DatastoreCluster"`
      - :literal:`"ResourcePool"`
      - :literal:`"Folder"`



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
      The password of the vSphere vCenter server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PASSWORD`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port:

      **port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The port number of the vSphere vCenter.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PORT`\  will be used instead.


      Default: :literal:`443`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-protocol:

      **protocol**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The connection to protocol.


      Choices:

      - :literal:`"http"`
      - :literal:`"https"` ← (default)



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

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If \ :literal:`state`\  is set to \ :literal:`add`\  or \ :literal:`present`\  will add the tags to the existing tag list of the given object.

      If \ :literal:`state`\  is set to \ :literal:`remove`\  or \ :literal:`absent`\  will remove the tags from the existing tag list of the given object.

      If \ :literal:`state`\  is set to \ :literal:`set`\  will replace the tags of the given objects with the user defined list of tags.


      Choices:

      - :literal:`"present"`
      - :literal:`"absent"`
      - :literal:`"add"` ← (default)
      - :literal:`"remove"`
      - :literal:`"set"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-tag_names:

      **tag_names**

      :literal:`list` / :literal:`elements=any` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      List of tag(s) to be managed.

      User can also specify category name by specifying colon separated value. For example, "category\_name:tag\_name".

      User can also specify tag and category as dict, when tag or category contains colon. See example for more information. Added in version 2.10.

      User can skip category name if you have unique tag names.



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
      The username of the vSphere vCenter server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_USER`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allows connection when SSL certificates are not valid.

      Set to \ :literal:`false`\  when certificates are not trusted.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_VALIDATE\_CERTS`\  will be used instead.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)







Examples
--------

.. code-block:: yaml

    
    - name: Add tags to a virtual machine
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0002
          - Category_0001:Sample_Tag_0003
        object_name: Fedora_VM
        object_type: VirtualMachine
        state: add
      delegate_to: localhost

    - name: Specify tag and category as dict
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - tag: tag_0001
            category: cat_0001
          - tag: tag_0002
            category: cat_0002
        object_name: Fedora_VM
        object_type: VirtualMachine
        state: add
      delegate_to: localhost

    - name: Remove a tag from a virtual machine
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0002
        object_name: Fedora_VM
        object_type: VirtualMachine
        state: remove
      delegate_to: localhost

    - name: Add tags to a distributed virtual switch
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0003
        object_name: Switch_0001
        object_type: DistributedVirtualSwitch
        state: add
      delegate_to: localhost

    - name: Add tags to a distributed virtual portgroup
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0004
        object_name: Switch_0001:Portgroup_0001
        object_type: DistributedVirtualPortgroup
        state: add
      delegate_to: localhost


    - name: Get information about folders
      community.vmware.vmware_folder_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: 'Asia-Datacenter1'
      delegate_to: localhost
      register: r
    - name: Set Managed object ID for the given folder
      ansible.builtin.set_fact:
        folder_mo_id: "{{ (r.flat_folder_info | selectattr('path', 'equalto', '/Asia-Datacenter1/vm/tier1/tier2') | map(attribute='moid'))[0] }}"
    - name: Add tags to a Folder using managed object id
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Cat_0004:Sample_Tag_0004
        object_type: Folder
        moid: "{{ folder_mo_id }}"
        state: add
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

      .. _return-tag_status:

      **tag_status**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      metadata about tags related to object configuration


      Returned: on success

      Sample: :literal:`{"attached\_tags": ["urn:vmomi:InventoryServiceCategory:76f69e84-f6b9-4e64-954c-fac545d2c0ba:GLOBAL:security"], "current\_tags": ["urn:vmomi:InventoryServiceCategory:927f5ff8-62e6-4364-bc94-23e3bfd7dee7:GLOBAL:backup", "urn:vmomi:InventoryServiceCategory:76f69e84-f6b9-4e64-954c-fac545d2c0ba:GLOBAL:security"], "detached\_tags": [], "previous\_tags": ["urn:vmomi:InventoryServiceCategory:927f5ff8-62e6-4364-bc94-23e3bfd7dee7:GLOBAL:backup"]}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Frederic Van Reet (@GBrawl)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

