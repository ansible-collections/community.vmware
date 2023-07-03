

community.vmware.vcenter_folder module -- Manage folders on given datacenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vcenter_folder`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to create, delete, move and rename folder on then given datacenter.
- This module is only supported for vCenter.








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
      .. _parameter-datacenter_name:

      **datacenter**

      aliases: datacenter_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the datacenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder_name:

      **folder_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of folder to be managed.

      This is case sensitive parameter.

      Folder name should be under 80 characters. This is a VMware restriction.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder_type:

      **folder_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      This is type of folder.

      If set to \ :literal:`vm`\ , then 'VM and Template Folder' is created under datacenter.

      If set to \ :literal:`host`\ , then 'Host and Cluster Folder' is created under datacenter.

      If set to \ :literal:`datastore`\ , then 'Storage Folder' is created under datacenter.

      If set to \ :literal:`network`\ , then 'Network Folder' is created under datacenter.

      This parameter is required, if \ :literal:`state`\  is set to \ :literal:`present`\  and parent\_folder is absent.

      This option is ignored, if \ :literal:`parent\_folder`\  is set.


      Choices:

      - :literal:`"datastore"`
      - :literal:`"host"`
      - :literal:`"network"`
      - :literal:`"vm"` ← (default)



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

      .. _parameter-parent_folder:

      **parent_folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the parent folder under which new folder needs to be created.

      This is case sensitive parameter.

      If user wants to create a folder under '/DC0/vm/vm\_folder', this value will be 'vm\_folder'.

      If user wants to create a folder under '/DC0/vm/folder1/folder2', this value will be 'folder1/folder2'.



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
      State of folder.

      If set to \ :literal:`present`\  without parent folder parameter, then folder with \ :literal:`folder\_type`\  is created.

      If set to \ :literal:`present`\  with parent folder parameter,  then folder in created under parent folder. \ :literal:`folder\_type`\  is ignored.

      If set to \ :literal:`absent`\ , then folder is unregistered and destroyed.


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
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a VM folder on given datacenter
      community.vmware.vcenter_folder:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter_name
        folder_name: sample_vm_folder
        folder_type: vm
        state: present
      register: vm_folder_creation_result
      delegate_to: localhost

    - name: Create a datastore folder on given datacenter
      community.vmware.vcenter_folder:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter_name
        folder_name: sample_datastore_folder
        folder_type: datastore
        state: present
      register: datastore_folder_creation_result
      delegate_to: localhost

    - name: Create a sub folder under VM folder on given datacenter
      community.vmware.vcenter_folder:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter_name
        folder_name: sample_sub_folder
        parent_folder: vm_folder
        state: present
      register: sub_folder_creation_result
      delegate_to: localhost

    - name: Delete a VM folder on given datacenter
      community.vmware.vcenter_folder:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter_name
        folder_name: sample_vm_folder
        folder_type: vm
        state: absent
      register: vm_folder_deletion_result
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

      .. _return-result:

      **result**

      :literal:`complex`

      .. raw:: html

        </div></div>
    - 
      The detail about the new folder


      Returned: On success

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-result/msg:

      **msg**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      string stating about result


      Returned: success


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-result/path:

      **path**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      the full path of the new folder


      Returned: success





Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte) 
- Jan Meerkamp (@meerkampdvv)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

