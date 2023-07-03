

community.vmware.vmware_category module -- Manage VMware categories
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.
    You need further requirements to be able to use this module,
    see `Requirements <ansible_collections.community.vmware.vmware_category_module_requirements_>`_ for details.

    To use it in a playbook, specify: :code:`community.vmware.vmware_category`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to create / delete / update VMware categories.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_category_module_requirements:

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

      .. _parameter-associable_object_types:

      **associable_object_types**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of object types that can be associated with the given category.


      Choices:

      - :literal:`"All objects"`
      - :literal:`"Cluster"`
      - :literal:`"Content Library"`
      - :literal:`"Datacenter"`
      - :literal:`"Datastore"`
      - :literal:`"Datastore Cluster"`
      - :literal:`"Distributed Port Group"`
      - :literal:`"Distributed Switch"`
      - :literal:`"Folder"`
      - :literal:`"Host"`
      - :literal:`"Library item"`
      - :literal:`"Network"`
      - :literal:`"Host Network"`
      - :literal:`"Opaque Network"`
      - :literal:`"Resource Pool"`
      - :literal:`"vApp"`
      - :literal:`"Virtual Machine"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-category_cardinality:

      **category_cardinality**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The category cardinality.

      This parameter is ignored, when updating existing category.


      Choices:

      - :literal:`"multiple"` ← (default)
      - :literal:`"single"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-category_description:

      **category_description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The category description.

      This is required only if \ :literal:`state`\  is set to \ :literal:`present`\ .

      This parameter is ignored, when \ :literal:`state`\  is set to \ :literal:`absent`\ .


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-category_name:

      **category_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of category to manage.



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

      .. _parameter-new_category_name:

      **new_category_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The new name for an existing category.

      This value is used while updating an existing category.



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
      The state of category.

      If set to \ :literal:`present`\  and category does not exists, then category is created.

      If set to \ :literal:`present`\  and category exists, then category is updated.

      If set to \ :literal:`absent`\  and category exists, then category is deleted.

      If set to \ :literal:`absent`\  and category does not exists, no action is taken.

      Process of updating category only allows name, description change.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



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

.. code-block:: yaml+jinja

    
    - name: Create a category
      community.vmware.vmware_category:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        category_name: Sample_Cat_0001
        category_description: Sample Description
        category_cardinality: 'multiple'
        state: present

    - name: Rename category
      community.vmware.vmware_category:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        category_name: Sample_Category_0001
        new_category_name: Sample_Category_0002
        state: present

    - name: Update category description
      community.vmware.vmware_category:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        category_name: Sample_Category_0001
        category_description: Some fancy description
        state: present

    - name: Delete category
      community.vmware.vmware_category:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        category_name: Sample_Category_0002
        state: absent

    - name: Create category with 2 associable object types
      community.vmware.vmware_category:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        category_name: 'Sample_Category_0003'
        category_description: 'sample description'
        associable_object_types:
        - Datastore
        - Cluster
        state: present





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

      .. _return-category_results:

      **category_results**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dictionary of category metadata


      Returned: on success

      Sample: :literal:`{"category\_id": "urn:vmomi:InventoryServiceCategory:d7120bda-9fa5-4f92-9d71-aa1acff2e5a8:GLOBAL", "msg": "Category NewCat\_0001 updated."}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

