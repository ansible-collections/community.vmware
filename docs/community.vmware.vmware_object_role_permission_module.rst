

community.vmware.vmware_object_role_permission module -- Manage local roles on an ESXi host or vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_object_role_permission`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage object permissions on the given host or vCenter.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-group:

      **group**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The group to be assigned permission.

      Required if \ :literal:`principal`\  is not specified.



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

      .. _parameter-object_name:

      **object_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The object name to assigned permission.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-object_type:

      **object_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The object type being targeted.


      Choices:

      - :literal:`"Folder"` ← (default)
      - :literal:`"VirtualMachine"`
      - :literal:`"Datacenter"`
      - :literal:`"ResourcePool"`
      - :literal:`"Datastore"`
      - :literal:`"Network"`
      - :literal:`"HostSystem"`
      - :literal:`"ComputeResource"`
      - :literal:`"ClusterComputeResource"`
      - :literal:`"DistributedVirtualSwitch"`
      - :literal:`"DistributedVirtualPortgroup"`
      - :literal:`"StoragePod"`



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

      .. _parameter-principal:

      **principal**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The user to be assigned permission.

      Required if \ :literal:`group`\  is not specified.

      If specifying domain user, required separator of domain uses backslash.



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

      .. _parameter-recursive:

      **recursive**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Should the permissions be recursively applied.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-role:

      **role**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The role to be assigned permission.

      User can also specify role name presented in Web UI. Supported added in 1.5.0.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Indicate desired state of the object's permission.

      When \ :literal:`state=present`\ , the permission will be added if it doesn't already exist.

      When \ :literal:`state=absent`\ , the permission is removed if it exists.


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
   - The login user must have the appropriate rights to administer permissions.
   - Permissions for a distributed switch must be defined and managed on either the datacenter or a folder containing the switch.
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Assign user to VM folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        role: Admin
        principal: user_bob
        object_name: services
        state: present
      delegate_to: localhost

    - name: Remove user from VM folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        role: Admin
        principal: user_bob
        object_name: services
        state: absent
      delegate_to: localhost

    - name: Assign finance group to VM folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        role: Limited Users
        group: finance
        object_name: Accounts
        state: present
      delegate_to: localhost

    - name: Assign view_user Read Only permission at root folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        role: ReadOnly
        principal: view_user
        object_name: rootFolder
        state: present
      delegate_to: localhost

    - name: Assign domain user to VM folder
      community.vmware.vmware_object_role_permission:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        role: Admin
        principal: "vsphere.local\\domainuser"
        object_name: services
        state: present
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

      .. _return-changed:

      **changed**

      :literal:`boolean`

      .. raw:: html

        </div></div>
    - 
      whether or not a change was made to the object's role


      Returned: always




Authors
~~~~~~~

- Derek Rushing (@kryptsi)
- Joseph Andreatta (@vmwjoseph)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

