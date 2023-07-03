

community.vmware.vmware_tag_info module -- Manage VMware tag info
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.
    You need further requirements to be able to use this module,
    see `Requirements <ansible_collections.community.vmware.vmware_tag_info_module_requirements_>`_ for details.

    To use it in a playbook, specify: :code:`community.vmware.vmware_tag_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to collect information about VMware tags.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_tag_info_module_requirements:

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

    
    - name: Get info about tag
      community.vmware.vmware_tag_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost

    - name: Get category id from the given tag
      community.vmware.vmware_tag_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost
      register: tag_details
    - debug:
        msg: "{{ tag_details.tag_facts['fedora_machines']['tag_category_id'] }}"

    - name: Gather tag id from the given tag
      community.vmware.vmware_tag_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
      delegate_to: localhost
      register: tag_results
    - set_fact:
        tag_id: "{{ item.tag_id }}"
      loop: "{{ tag_results.tag_info|json_query(query) }}"
      vars:
        query: "[?tag_name==`tag0001`]"
    - debug: var=tag_id





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

      .. _return-tag_facts:

      **tag_facts**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dictionary of tag metadata


      Returned: on success

      Sample: :literal:`{"Sample\_Tag\_0002": {"tag\_category\_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL", "tag\_description": "Sample Description", "tag\_id": "urn:vmomi:InventoryServiceTag:a141f212-0f82-4f05-8eb3-c49647c904c5:GLOBAL", "tag\_used\_by": []}, "fedora\_machines": {"tag\_category\_id": "urn:vmomi:InventoryServiceCategory:baa90bae-951b-4e87-af8c-be681a1ba30c:GLOBAL", "tag\_description": "", "tag\_id": "urn:vmomi:InventoryServiceTag:7d27d182-3ecd-4200-9d72-410cc6398a8a:GLOBAL", "tag\_used\_by": []}, "ubuntu\_machines": {"tag\_category\_id": "urn:vmomi:InventoryServiceCategory:89573410-29b4-4cac-87a4-127c084f3d50:GLOBAL", "tag\_description": "", "tag\_id": "urn:vmomi:InventoryServiceTag:7f3516d5-a750-4cb9-8610-6747eb39965d:GLOBAL", "tag\_used\_by": []}}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-tag_info:

      **tag_info**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      list of tag metadata


      Returned: on success

      Sample: :literal:`[{"tag\_category\_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL", "tag\_description": "Sample Description", "tag\_id": "urn:vmomi:InventoryServiceTag:a141f212-0f82-4f05-8eb3-c49647c904c5:GLOBAL", "tag\_name": "Sample\_Tag\_0002", "tag\_used\_by": []}, {"tag\_category\_id": "urn:vmomi:InventoryServiceCategory:6de17f28-7694-43ec-a783-d09c141819ae:GLOBAL", "tag\_description": "", "tag\_id": "urn:vmomi:InventoryServiceTag:7d27d182-3ecd-4200-9d72-410cc6398a8a:GLOBAL", "tag\_name": "Sample\_Tag\_0002", "tag\_used\_by": []}, {"tag\_category\_id": "urn:vmomi:InventoryServiceCategory:89573410-29b4-4cac-87a4-127c084f3d50:GLOBAL", "tag\_description": "", "tag\_id": "urn:vmomi:InventoryServiceTag:7f3516d5-a750-4cb9-8610-6747eb39965d:GLOBAL", "tag\_name": "ubuntu\_machines", "tag\_used\_by": []}]`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

