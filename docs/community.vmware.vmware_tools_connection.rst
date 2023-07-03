

community.vmware.vmware_tools connection -- Execute tasks inside a VM via VMware Tools
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This connection plugin is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.
    You need further requirements to be able to use this connection plugin,
    see `Requirements <ansible_collections.community.vmware.vmware_tools_connection_requirements_>`_ for details.

    To use it in a playbook, specify: :code:`community.vmware.vmware_tools`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Use VMware tools to run tasks in, or put/fetch files to guest operating systems running in VMware infrastructure.
- In case of Windows VMs, set \ :literal:`ansible\_shell\_type`\  to \ :literal:`powershell`\ .
- Does not work with 'become'.



.. _ansible_collections.community.vmware.vmware_tools_connection_requirements:

Requirements
------------
The below requirements are needed on the local controller node that executes this connection.

- requests (Python library)






Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-exec_command_sleep_interval:

      **exec_command_sleep_interval**

      :literal:`float`




      .. raw:: html

        </div></div>

    - 
      Time in seconds to sleep between execution of command.


      Default: :literal:`0.5`

      Configuration:

      - Variable: ansible\_vmware\_tools\_exec\_command\_sleep\_interval



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-executable:

      **executable**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      shell to use for execution inside container


      Default: :literal:`"/bin/sh"`

      Configuration:

      - INI entry:

        .. code-block::

          [defaults]
          executable = /bin/sh


      - Environment variable: :literal:`ANSIBLE\_EXECUTABLE`

      - Variable: ansible\_executable

      - Variable: ansible\_vmware\_tools\_executable



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-file_chunk_size:

      **file_chunk_size**

      :literal:`integer`




      .. raw:: html

        </div></div>

    - 
      File chunk size.

      (Applicable when writing a file to disk, example: using the \ :literal:`fetch`\  module.)


      Default: :literal:`128`

      Configuration:

      - Variable: ansible\_vmware\_tools\_file\_chunk\_size



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      Verify SSL for the connection.

      Note: This will validate certs for both \ :literal:`vmware\_host`\  and the ESXi host running the VM.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)


      Configuration:

      - Environment variable: :literal:`VMWARE\_VALIDATE\_CERTS`

      - Variable: ansible\_vmware\_validate\_certs



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_password:

      **vm_password**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      Password for the user in guest operating system.


      Configuration:

      - Variable: ansible\_password

      - Variable: ansible\_vmware\_tools\_password



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_path:

      **vm_path**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      Mutually exclusive with vm\_uuid

      VM path absolute to the connection.

      vCenter Example: \ :literal:`Datacenter/vm/Discovered virtual machine/testVM`\ .

      ESXi Host Example: \ :literal:`ha-datacenter/vm/testVM`\ .

      Must include VM name, appended to 'folder' as would be passed to \ `community.vmware.vmware\_guest <vmware_guest_module.rst>`__\ .

      Needs to include \ :emphasis:`vm`\  between the Datacenter and the rest of the VM path.

      Datacenter default value for ESXi server is \ :literal:`ha-datacenter`\ .

      Folder \ :emphasis:`vm`\  is not visible in the vSphere Web Client but necessary for VMware API to work.


      Configuration:

      - Variable: ansible\_vmware\_guest\_path



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_user:

      **vm_user**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      VM username.

      \ :literal:`ansible\_vmware\_tools\_user`\  is used for connecting to the VM.

      \ :literal:`ansible\_user`\  is used by Ansible on the VM.


      Configuration:

      - Variable: ansible\_user

      - Variable: ansible\_vmware\_tools\_user



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vm_uuid:

      **vm_uuid**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      Mutually exclusive with vm\_path

      VM UUID to the connection.

      UUID of the virtual machine from property config.uuid of vmware\_vm\_inventory plugin


      Configuration:

      - Variable: ansible\_vmware\_guest\_uuid



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmware_host:

      **vmware_host**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      FQDN or IP Address for the connection (vCenter or ESXi Host).


      Configuration:

      - Environment variable: :literal:`VI\_SERVER`

      - Environment variable: :literal:`VMWARE\_HOST`

      - Variable: ansible\_host

      - Variable: ansible\_vmware\_host



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmware_password:

      **vmware_password**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      Password for the connection.


      Configuration:

      - Environment variable: :literal:`VI\_PASSWORD`

      - Environment variable: :literal:`VMWARE\_PASSWORD`

      - Variable: ansible\_vmware\_password



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmware_port:

      **vmware_port**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      Port for the connection.


      Default: :literal:`443`

      Configuration:

      - Environment variable: :literal:`VI\_PORTNUMBER`

      - Environment variable: :literal:`VMWARE\_PORT`

      - Variable: ansible\_port

      - Variable: ansible\_vmware\_port



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmware_user:

      **vmware_user**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      Username for the connection.

      Requires the following permissions on the VM: - VirtualMachine.GuestOperations.Execute - VirtualMachine.GuestOperations.Modify - VirtualMachine.GuestOperations.Query


      Configuration:

      - Environment variable: :literal:`VI\_USERNAME`

      - Environment variable: :literal:`VMWARE\_USER`

      - Variable: ansible\_vmware\_user












Authors
~~~~~~~

- Deric Crago (@dericcrago) 


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

