

community.vmware.vmware_vc_infraprofile_info module -- List and Export VMware vCenter infra profile configs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.
    You need further requirements to be able to use this module,
    see `Requirements <ansible_collections.community.vmware.vmware_vc_infraprofile_info_module_requirements_>`_ for details.

    To use it in a playbook, specify: :code:`community.vmware.vmware_vc_infraprofile_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Module to manage VMware vCenter infra profile configs.
- vCenter infra profile Library feature is introduced in vSphere 7.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_vc_infraprofile_info_module_requirements:

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

      .. _parameter-api:

      **api**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      API which needs to be executed


      Choices:

      - :literal:`"export"`
      - :literal:`"import"`
      - :literal:`"list"`
      - :literal:`"validate"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-config_path:

      **config_path**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Config file path which contains infra profile config JSON data, supports both relative and absolute path.

      This parameter is required only when \ :literal:`import`\ ,\ :literal:`validate`\  APIs are being used.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-decryption_key:

      **decryption_key**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      decryption\_key argument for while doing import profile task as of now its not taken into account form API team.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-description:

      **description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Description of about encryption or decryption key.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-encryption_key:

      **encryption_key**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      encryption\_key argument for while doing import profile task as of now its not taken into account form API team.



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

      .. _parameter-profiles:

      **profiles**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      A list of profile names to be exported, imported, and validated.

      This parameter is not required while running for List API, not for \ :literal:`export`\ ,\ :literal:`import`\  and \ :literal:`validate`\ .



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

    
    - name: Get information about VC infraprofile
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost

    - name: export vCenter appliance infra profile config
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        api: "export"
        profiles: "ApplianceManagement"
      delegate_to: localhost

    - name: validate vCenter appliance infra profile config
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        api: "validate"
        profiles: "ApplianceManagement"
        config_path: "export.json"

    - name: import vCenter appliance infra profile config
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        api: "import"
        profiles: "ApplianceManagement"
        config_path: "import.json"
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

      .. _return-export_infra:

      **export_infra**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      A message about the exported file


      Returned: On success with API set as "export"

      Sample: :literal:`{"export\_config\_json": "json exported to file"}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-import_profile:

      **import_profile**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      A message about import on import\_profile spec


      Returned: On success with API set as "import"

      Sample: :literal:`{"changed": true, "failed": false, "status": "0.0"}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-list_infra:

      **list_infra**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      A list of infra configs,


      Returned: on success with API as "list"

      Sample: :literal:`[{"info": "ApplianceManagement", "name": "ApplianceManagement"}, {"info": "ApplianceNetwork", "name": "ApplianceNetwork"}, {"info": "Authentication & Authorization Management", "name": "AuthManagement"}]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-validate_infra:

      **validate_infra**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      A message about validate on exported file


      Returned: On success with API set as "validate"

      Sample: :literal:`{"changed": false, "failed": false, "status": "VALID"}`




Authors
~~~~~~~

- Naveenkumar G P (@ngp)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

