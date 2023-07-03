

community.vmware.vmware_content_library_manager module -- Create, update and delete VMware content library
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this module,
see `Requirements <ansible_collections.community.vmware.vmware_content_library_manager_module_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_content_library_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Module to manage VMware content Library
- Content Library feature is introduced in vSphere 6.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_content_library_manager_module_requirements:

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

      .. _parameter-datastore:
      .. _parameter-datastore_name:

      **datastore_name**

      aliases: datastore

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the datastore on which backing content library is created.

      This is required only if \ :emphasis:`state`\  is set to \ :literal:`present`\ .

      This parameter is ignored, when \ :emphasis:`state`\  is set to \ :literal:`absent`\ .

      Currently only datastore backing creation is supported.



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

      .. _parameter-library_description:

      **library_description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The content library description.

      This is required only if \ :emphasis:`state`\  is set to \ :literal:`present`\ .

      This parameter is ignored, when \ :emphasis:`state`\  is set to \ :literal:`absent`\ .

      Process of updating content library only allows description change.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-library_name:

      **library_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of VMware content library to manage.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-library_type:

      **library_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The content library type.

      This is required only if \ :emphasis:`state`\  is set to \ :literal:`present`\ .

      This parameter is ignored, when \ :emphasis:`state`\  is set to \ :literal:`absent`\ .


      Choices:

      - :literal:`"local"` ← (default)
      - :literal:`"subscribed"`



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

      .. _parameter-ssl_thumbprint:

      **ssl_thumbprint**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The SHA1 SSL thumbprint of the subscribed content library to subscribe to.

      This is required only if \ :emphasis:`library\_type`\  is set to \ :literal:`subscribed`\  and the library is https.

      This parameter is ignored, when \ :emphasis:`state`\  is set to \ :literal:`absent`\ .

      The information can be extracted using openssl using the following example: \ :literal:`echo | openssl s\_client -connect test-library.com:443 |& openssl x509 -fingerprint -noout`\ 


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The state of content library.

      If set to \ :literal:`present`\  and library does not exists, then content library is created.

      If set to \ :literal:`present`\  and library exists, then content library is updated.

      If set to \ :literal:`absent`\  and library exists, then content library is deleted.

      If set to \ :literal:`absent`\  and library does not exists, no action is taken.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-subscription_url:

      **subscription_url**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The url of the content library to subscribe to.

      This is required only if \ :emphasis:`library\_type`\  is set to \ :literal:`subscribed`\ .

      This parameter is ignored, when \ :emphasis:`state`\  is set to \ :literal:`absent`\ .


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-update_on_demand:

      **update_on_demand**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to download all content on demand.

      If set to \ :literal:`true`\ , all content will be downloaded on demand.

      If set to \ :literal:`false`\  content will be downloaded ahead of time.

      This is required only if \ :emphasis:`library\_type`\  is set to \ :literal:`subscribed`\ .

      This parameter is ignored, when \ :emphasis:`state`\  is set to \ :literal:`absent`\ .


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

    
    - name: Create Local Content Library
      community.vmware.vmware_content_library_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        library_name: test-content-lib
        library_description: 'Library with Datastore Backing'
        library_type: local
        datastore_name: datastore
        state: present
      delegate_to: localhost

    - name: Create Subscribed Content Library
      community.vmware.vmware_content_library_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        library_name: test-content-lib
        library_description: 'Subscribed Library with Datastore Backing'
        library_type: subscribed
        datastore_name: datastore
        subscription_url: 'https://library.url'
        ssl_thumbprint: 'aa:bb:cc:dd:ee:ff:gg:hh:ii:jj:kk:ll:mm:nn:oo:pp:qq:rr:ss:tt'
        update_on_demand: true
        state: present
      delegate_to: localhost

    - name: Update Content Library
      community.vmware.vmware_content_library_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        library_name: test-content-lib
        library_description: 'Library with Datastore Backing'
        state: present
      delegate_to: localhost

    - name: Delete Content Library
      community.vmware.vmware_content_library_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        library_name: test-content-lib
        state: absent
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

      .. _return-content_library_info:

      **content_library_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      library creation success and library\_id


      Returned: on success

      Sample: :literal:`{"library\_description": "Test description", "library\_id": "d0b92fa9-7039-4f29-8e9c-0debfcb22b72", "library\_type": "LOCAL", "msg": "Content Library 'demo-local-lib-4' created."}`




Authors
~~~~~~~

- Pavan Bidkar (@pgbidkar)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

