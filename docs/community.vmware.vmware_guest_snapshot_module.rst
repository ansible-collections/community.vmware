

community.vmware.vmware_guest_snapshot module -- Manages virtual machines snapshots in vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_snapshot`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to create, delete and update snapshot(s) of the given virtual machine.
- All parameters and VMware object names are case sensitive.








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

      **datacenter**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Destination datacenter for the deploy operation.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-description:

      **description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Define an arbitrary description to attach to snapshot.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute or relative path to find an existing guest.

      This is required parameter, if \ :literal:`name`\  is supplied.

      The folder should include the datacenter. ESX's datacenter is ha-datacenter.

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

      .. _parameter-memory_dump:

      **memory_dump**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , memory dump of virtual machine is also included in snapshot.

      Note that memory snapshots take time and resources, this will take longer time to create.

      If virtual machine does not provide capability to take memory snapshot, then this flag is set to \ :literal:`false`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-moid:

      **moid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.

      This is required if \ :literal:`name`\  or \ :literal:`uuid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the virtual machine to work with.

      This is required parameter, if \ :literal:`uuid`\  or \ :literal:`moid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name_match:

      **name_match**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If multiple VMs matching the name, use the first or last found.


      Choices:

      - :literal:`"first"` ← (default)
      - :literal:`"last"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-new_description:

      **new_description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Value to change the description of an existing snapshot to.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-new_snapshot_name:

      **new_snapshot_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Value to rename the existing snapshot to.



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

      .. _parameter-quiesce:

      **quiesce**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\  and virtual machine is powered on, it will quiesce the file system in virtual machine.

      Note that VMware Tools are required for this flag.

      If virtual machine is powered off or VMware Tools are not available, then this flag is set to \ :literal:`false`\ .

      If virtual machine does not provide capability to take quiesce snapshot, then this flag is set to \ :literal:`false`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-remove_children:

      **remove_children**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\  and state is set to \ :literal:`absent`\ , then entire snapshot subtree is set for removal.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snapshot_name:

      **snapshot_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Sets the snapshot name to manage.

      This param is required only if state is not \ :literal:`remove\_all`\ 



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Manage snapshot(s) attached to a specific virtual machine.

      If set to \ :literal:`present`\  and snapshot absent, then will create a new snapshot with the given name.

      If set to \ :literal:`present`\  and snapshot present, then no changes are made.

      If set to \ :literal:`absent`\  and snapshot present, then snapshot with the given name is removed.

      If set to \ :literal:`absent`\  and snapshot absent, then no changes are made.

      If set to \ :literal:`revert`\  and snapshot present, then virtual machine state is reverted to the given snapshot.

      If set to \ :literal:`revert`\  and snapshot absent, then no changes are made.

      If set to \ :literal:`remove\_all`\  and snapshot(s) present, then all snapshot(s) will be removed.

      If set to \ :literal:`remove\_all`\  and snapshot(s) absent, then no changes are made.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`
      - :literal:`"revert"`
      - :literal:`"remove\_all"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-use_instance_uuid:

      **use_instance_uuid**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to use the VMware instance UUID rather than the BIOS UUID.


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

      .. _parameter-uuid:

      **uuid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      UUID of the instance to manage if known, this is VMware's BIOS UUID by default.

      This is required if \ :literal:`name`\  or \ :literal:`moid`\  parameter is not supplied.



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

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
      - name: Create a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: present
          snapshot_name: snap1
          description: snap1_description
        delegate_to: localhost

      - name: Remove a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: absent
          snapshot_name: snap1
        delegate_to: localhost

      - name: Revert to a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: revert
          snapshot_name: snap1
        delegate_to: localhost

      - name: Remove all snapshots of a VM
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: remove_all
        delegate_to: localhost

      - name: Remove all snapshots of a VM using MoID
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          moid: vm-42
          state: remove_all
        delegate_to: localhost

      - name: Take snapshot of a VM using quiesce and memory flag on
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: present
          snapshot_name: dummy_vm_snap_0001
          quiesce: true
          memory_dump: true
        delegate_to: localhost

      - name: Remove a snapshot and snapshot subtree
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: absent
          remove_children: true
          snapshot_name: snap1
        delegate_to: localhost

      - name: Rename a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: present
          snapshot_name: current_snap_name
          new_snapshot_name: im_renamed
          new_description: "{{ new_snapshot_description }}"
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

      .. _return-snapshot_results:

      **snapshot_results**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine snapshots


      Returned: always

      Sample: :literal:`{"current\_snapshot": {"creation\_time": "2019-04-09T14:40:26.617427+00:00", "description": "Snapshot 4 example", "id": 4, "name": "snapshot4", "state": "poweredOff"}, "snapshots": [{"creation\_time": "2019-04-09T14:38:24.667543+00:00", "description": "Snapshot 3 example", "id": 3, "name": "snapshot3", "state": "poweredOff"}, {"creation\_time": "2019-04-09T14:40:26.617427+00:00", "description": "Snapshot 4 example", "id": 4, "name": "snapshot4", "state": "poweredOff"}]}`




Authors
~~~~~~~

- Loic Blot (@nerzhul) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

