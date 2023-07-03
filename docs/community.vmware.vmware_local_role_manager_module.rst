

community.vmware.vmware_local_role_manager module -- Manage local roles on an ESXi host or vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_local_role_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage local roles on an ESXi host or vCenter.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-action:

      **action**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      This parameter is only valid while updating an existing role with privileges.

      \ :literal:`add`\  will add the privileges to the existing privilege list.

      \ :literal:`remove`\  will remove the privileges from the existing privilege list.

      \ :literal:`set`\  will replace the privileges of the existing privileges with user defined list of privileges.


      Choices:

      - :literal:`"add"`
      - :literal:`"remove"`
      - :literal:`"set"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-force_remove:

      **force_remove**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`false`\  then prevents the role from being removed if any permissions are using it.


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

      .. _parameter-local_privilege_ids:

      **local_privilege_ids**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      The list of privileges that role needs to have.

      Please see \ https://docs.vmware.com/en/VMware-vSphere/6.0/com.vmware.vsphere.security.doc/GUID-ED56F3C4-77D0-49E3-88B6-B99B8B437B62.html\ 


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-local_role_name:

      **local_role_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The local role name to be managed.



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

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Indicate desired state of the role.

      If the role already exists when \ :literal:`state=present`\ , the role info is updated.


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





Notes
-----

.. note::
   - Be sure that the user used for login, has the appropriate rights to create / delete / edit roles
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add local role to ESXi
      community.vmware.vmware_local_role_manager:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        local_role_name: vmware_qa
        state: present
      delegate_to: localhost

    - name: Add local role with privileges to vCenter
      community.vmware.vmware_local_role_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        local_role_name: vmware_qa
        local_privilege_ids: [ 'Folder.Create', 'Folder.Delete']
        state: present
      delegate_to: localhost

    - name: Remove local role from ESXi
      community.vmware.vmware_local_role_manager:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        local_role_name: vmware_qa
        state: absent
      delegate_to: localhost

    - name: Add a privilege to an existing local role
      community.vmware.vmware_local_role_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        local_role_name: vmware_qa
        local_privilege_ids: [ 'Folder.Create' ]
        action: add
      delegate_to: localhost

    - name: Remove a privilege to an existing local role
      community.vmware.vmware_local_role_manager:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        local_role_name: vmware_qa
        local_privilege_ids: [ 'Folder.Create' ]
        action: remove
      delegate_to: localhost

    - name: Set a privilege to an existing local role
      community.vmware.vmware_local_role_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        local_role_name: vmware_qa
        local_privilege_ids: [ 'Folder.Create' ]
        action: set
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

      .. _return-local_role_name:

      **local_role_name**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      Name of local role


      Returned: always


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-new_privileges:

      **new_privileges**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      List of privileges


      Returned: always


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-old_privileges:

      **old_privileges**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      List of privileges of role before the update


      Returned: on update


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-privileges:

      **privileges**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      List of privileges


      Returned: always


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-privileges_previous:

      **privileges_previous**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      List of privileges of role before the update


      Returned: on update


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-role_id:

      **role_id**

      :literal:`integer`

      .. raw:: html

        </div></div>
    - 
      Generated local role id


      Returned: always


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-role_name:

      **role_name**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      Name of local role


      Returned: always




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

