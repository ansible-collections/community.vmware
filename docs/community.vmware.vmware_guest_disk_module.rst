

community.vmware.vmware_guest_disk module -- Manage disks related to virtual machine in given vCenter infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_guest_disk`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add, remove and update disks belonging to given virtual machine.
- All parameters and VMware object names are case sensitive.
- This module is destructive in nature, please read documentation carefully before proceeding.
- Be careful while removing disk specified as this may lead to data loss.








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
      The datacenter name to which virtual machine belongs to.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk:

      **disk**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of disks to add or remove.

      The virtual disk related information is provided using this list.

      All values and parameters are case sensitive.


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/autoselect_datastore:

      **autoselect_datastore**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Select the less used datastore. Specify only if \ :literal:`datastore`\  is not specified.

      Not applicable when disk \ :literal:`type`\  is set to \ :literal:`vpmemdisk`\ .


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/bus_sharing:

      **bus_sharing**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Only functions with Paravirtual SCSI Controller.

      Allows for the sharing of the scsi bus between two virtual machines.


      Choices:

      - :literal:`"noSharing"` ← (default)
      - :literal:`"physicalSharing"`
      - :literal:`"virtualSharing"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/cluster_disk:

      **cluster_disk**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      This value allows for the sharing of an RDM between two machines.

      The primary machine holding the RDM uses the default \ :literal:`false`\ .

      The secondary machine holding the RDM uses \ :literal:`true`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/compatibility_mode:

      **compatibility_mode**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Compatibility mode for raw devices. Required when disk type \ :literal:`type`\  is set to \ :literal:`rdm`\ .


      Choices:

      - :literal:`"physicalMode"`
      - :literal:`"virtualMode"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/controller_number:

      **controller_number**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      This parameter is used with \ :literal:`controller\_type`\  for specifying controller bus number.

      For \ :literal:`ide`\  controller type, valid value is 0 or 1.


      Choices:

      - :literal:`0`
      - :literal:`1`
      - :literal:`2`
      - :literal:`3`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/controller_type:

      **controller_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      This parameter is added for managing disks attaching other types of controllers, e.g., SATA or NVMe.

      If either \ :literal:`controller\_type`\  or \ :literal:`scsi\_type`\  is not specified, then use \ :literal:`paravirtual`\  type.


      Choices:

      - :literal:`"buslogic"`
      - :literal:`"lsilogic"`
      - :literal:`"lsilogicsas"`
      - :literal:`"paravirtual"`
      - :literal:`"sata"`
      - :literal:`"nvme"`
      - :literal:`"ide"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/datastore:

      **datastore**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of datastore or datastore cluster to be used for the disk.

      Not applicable when disk \ :literal:`type`\  is set to \ :literal:`vpmemdisk`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/destroy:

      **destroy**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If \ :literal:`state`\  is \ :literal:`absent`\ , make sure the disk file is deleted from the datastore. Added in version 2.10.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/disk_mode:

      **disk_mode**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of disk mode. If not specified then use \ :literal:`persistent`\  mode for new disk.

      If set to 'persistent' mode, changes are immediately and permanently written to the virtual disk.

      If set to 'independent\_persistent' mode, same as persistent, but not affected by snapshots.

      If set to 'independent\_nonpersistent' mode, changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.

      Not applicable when disk \ :literal:`type`\  is set to \ :literal:`vpmemdisk`\ .


      Choices:

      - :literal:`"persistent"`
      - :literal:`"independent\_persistent"`
      - :literal:`"independent\_nonpersistent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/filename:

      **filename**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Existing disk image to be used. Filename must already exist on the datastore.

      Specify filename string in \ :literal:`[datastore\_name] path/to/file.vmdk`\  format. Added in version 2.10.

      Not applicable when disk \ :literal:`type`\  is set to \ :literal:`vpmemdisk`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/iolimit:

      **iolimit**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Section specifies the shares and limit for storage I/O resource.

      Not applicable when disk \ :literal:`type`\  is set to \ :literal:`vpmemdisk`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/iolimit/limit:

      **limit**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Section specifies values for limit where the utilization of a virtual machine will not exceed, even if there are available resources.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/iolimit/shares:

      **shares**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Specifies different types of shares user can add for the given disk.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/iolimit/shares/level:

      **level**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specifies different level for the shares section.


      Choices:

      - :literal:`"low"`
      - :literal:`"normal"`
      - :literal:`"high"`
      - :literal:`"custom"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/iolimit/shares/level_value:

      **level_value**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Custom value when \ :literal:`level`\  is set as \ :literal:`custom`\ .





  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/rdm_path:

      **rdm_path**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Path of LUN for Raw Device Mapping required for disk type \ :literal:`rdm`\ .

      Only valid if \ :literal:`type`\  is set to \ :literal:`rdm`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/scsi_controller:

      **scsi_controller**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      SCSI controller number. Only 4 SCSI controllers are allowed per VM.

      Care should be taken while specifying 'scsi\_controller' is 0 and 'unit\_number' as 0 as this disk may contain OS.


      Choices:

      - :literal:`0`
      - :literal:`1`
      - :literal:`2`
      - :literal:`3`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/scsi_type:

      **scsi_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of SCSI controller. This value is required only for the first occurrence of SCSI Controller.

      This value is ignored, if SCSI Controller is already present or \ :literal:`state`\  is \ :literal:`absent`\ .


      Choices:

      - :literal:`"buslogic"`
      - :literal:`"lsilogic"`
      - :literal:`"lsilogicsas"`
      - :literal:`"paravirtual"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/shares:

      **shares**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Section for iolimit section tells about what are all different types of shares user can add for disk.

      Not applicable when disk \ :literal:`type`\  is set to \ :literal:`vpmemdisk`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/shares/level:

      **level**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Tells about different level for the shares section.


      Choices:

      - :literal:`"low"`
      - :literal:`"normal"`
      - :literal:`"high"`
      - :literal:`"custom"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/shares/level_value:

      **level_value**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Custom value when \ :literal:`level`\  is set as \ :literal:`custom`\ .




  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/sharing:

      **sharing**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      The sharing mode of the virtual disk.

      Setting sharing means that multiple virtual machines can write to the virtual disk.

      Sharing can only be set if \ :literal:`type`\  is set to \ :literal:`eagerzeroedthick`\  or \ :literal:`rdm`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/size:

      **size**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Disk storage size.

      If size specified then unit must be specified. There is no space allowed in between size number and unit.

      Only first occurrence in disk element will be considered, even if there are multiple size\* parameters available.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/size_gb:

      **size_gb**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Disk storage size in gb.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/size_kb:

      **size_kb**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Disk storage size in kb.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/size_mb:

      **size_mb**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Disk storage size in mb.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/size_tb:

      **size_tb**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Disk storage size in tb.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      State of disk.

      If set to 'absent', disk will be removed permanently from virtual machine configuration and from VMware storage.

      If set to 'present', disk will be added if not present at given Controller and Unit Number.

      or disk exists with different size, disk size is increased, reducing disk size is not allowed.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/type:

      **type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The type of disk, if not specified then use \ :literal:`thick`\  type for new disk, no eagerzero.

      The disk type \ :literal:`rdm`\  is added in version 1.13.0.

      The disk type \ :literal:`vpmemdisk`\  is added in version 2.7.0.


      Choices:

      - :literal:`"thin"`
      - :literal:`"eagerzeroedthick"`
      - :literal:`"thick"`
      - :literal:`"rdm"`
      - :literal:`"vpmemdisk"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/unit_number:

      **unit_number**

      :literal:`integer` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Disk Unit Number.

      Valid value range from 0 to 15, except 7 for SCSI Controller.

      Valid value range from 0 to 64, except 7 for Paravirtual SCSI Controller on Virtual Hardware version 14 or higher.

      Valid value range from 0 to 29 for SATA controller.

      Valid value range from 0 to 14 for NVME controller.

      Valid value range from 0 to 1 for IDE controller.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute or relative path to find an existing guest.

      This is a required parameter, only if multiple VMs are found with same name.

      The folder should include the datacenter. ESX's datacenter is ha-datacenter

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
      Name of the virtual machine.

      This is a required parameter, if parameter \ :literal:`uuid`\  or \ :literal:`moid`\  is not supplied.



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
      UUID of the instance to gather facts if known, this is VMware's unique identifier.

      This is a required parameter, if parameter \ :literal:`name`\  or \ :literal:`moid`\  is not supplied.



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

    
    - name: Add disks to virtual machine using UUID
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
        disk:
          - size_mb: 10
            type: thin
            datastore: datacluster0
            state: present
            scsi_controller: 1
            unit_number: 1
            scsi_type: 'paravirtual'
            disk_mode: 'persistent'
          - size_gb: 10
            type: eagerzeroedthick
            state: present
            autoselect_datastore: true
            scsi_controller: 2
            scsi_type: 'buslogic'
            unit_number: 12
            disk_mode: 'independent_persistent'
          - size: 10Gb
            type: eagerzeroedthick
            state: present
            autoselect_datastore: true
            scsi_controller: 2
            scsi_type: 'buslogic'
            unit_number: 1
            disk_mode: 'independent_nonpersistent'
          - filename: "[datastore1] path/to/existing/disk.vmdk"
      delegate_to: localhost
      register: disk_facts

    - name: Add disks with specified shares to the virtual machine
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        disk:
          - size_gb: 1
            type: thin
            datastore: datacluster0
            state: present
            scsi_controller: 1
            unit_number: 1
            disk_mode: 'independent_persistent'
            shares:
              level: custom
              level_value: 1300
      delegate_to: localhost
      register: test_custom_shares

    - name: Add physical raw device mapping to virtual machine using name
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: false
        name: "Test_VM"
        disk:
          - type: rdm
            state: present
            scsi_controller: 1
            unit_number: 5
            rdm_path: /vmfs/devices/disks/naa.060000003b1234efb453
            compatibility_mode: 'physicalMode'

    - name: Add virtual raw device mapping to virtual machine using name and virtual mode
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: false
        name: "Test_VM"
        disk:
          - type: rdm
            state: present
            scsi_controller: 1
            unit_number: 5
            rdm_path: /vmfs/devices/disks/naa.060000003b1234efb453
            compatibility_mode: 'virtualMode'
            disk_mode: 'persistent'

    - name: Add raw device mapping to virtual machine with Physical bus sharing
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: false
        name: "Test_VM"
        disk:
          - type: rdm
            state: present
            scsi_controller: 1
            unit_number: 5
            rdm_path: /vmfs/devices/disks/naa.060000003b1234efb453
            compatibility_mode: 'virtualMode'
            disk_mode: 'persistent'
            bus_sharing: physicalSharing

    - name: Add raw device mapping to virtual machine with Physical bus sharing and clustered disk
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: false
        name: "Test_VM"
        disk:
          - type: rdm
            state: present
            scsi_controller: 1
            unit_number: 5
            compatibility_mode: 'virtualMode'
            disk_mode: 'persistent'
            bus_sharing: physicalSharing
            filename: "[datastore1] path/to/rdm/disk-marker.vmdk"

    - name: create new disk with custom IO limits and shares in IO Limits
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        disk:
          - size_gb: 1
            type: thin
            datastore: datacluster0
            state: present
            scsi_controller: 1
            unit_number: 1
            disk_mode: 'independent_persistent'
            iolimit:
                limit: 1506
                shares:
                  level: custom
                  level_value: 1305
      delegate_to: localhost
      register: test_custom_IoLimit_shares

    - name: Remove disks from virtual machine using name
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: VM_225
        disk:
          - state: absent
            scsi_controller: 1
            unit_number: 1
      delegate_to: localhost
      register: disk_facts

    - name: Remove disk from virtual machine using moid
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        moid: vm-42
        disk:
          - state: absent
            scsi_controller: 1
            unit_number: 1
      delegate_to: localhost
      register: disk_facts

    - name: Remove disk from virtual machine but keep the VMDK file on the datastore
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: VM_225
        disk:
          - state: absent
            scsi_controller: 1
            unit_number: 2
            destroy: false
      delegate_to: localhost
      register: disk_facts

    - name: Add disks to virtual machine using UUID to SATA and NVMe controller
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: false
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
        disk:
          - size_mb: 256
            type: thin
            datastore: datacluster0
            state: present
            controller_type: sata
            controller_number: 1
            unit_number: 1
            disk_mode: 'persistent'
          - size_gb: 1
            state: present
            autoselect_datastore: true
            controller_type: nvme
            controller_number: 2
            unit_number: 3
            disk_mode: 'independent_persistent'
      delegate_to: localhost
      register: disk_facts

    - name: Add a new vPMem disk to virtual machine to SATA controller
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: false
        name: VM_226
        disk:
          - type: vpmemdisk
            size_gb: 1
            state: present
            controller_type: sata
            controller_number: 1
            unit_number: 2
      delegate_to: localhost
      register: disk_facts





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

      .. _return-disk_changes:

      **disk_changes**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      result of each task, key is the 0-based index with the same sequence in which the tasks were defined


      Returned: always

      Sample: :literal:`{"0": "Disk deleted.", "1": "Disk created."}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-disk_data:

      **disk_data**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine's disks after managing them


      Returned: always

      Sample: :literal:`{"0": {"backing\_datastore": "datastore2", "backing\_disk\_mode": "persistent", "backing\_eagerlyscrub": false, "backing\_filename": "[datastore2] VM\_225/VM\_225.vmdk", "backing\_thinprovisioned": false, "backing\_uuid": "421e4592-c069-924d-ce20-7e7533fab926", "backing\_writethrough": false, "capacity\_in\_bytes": 10485760, "capacity\_in\_kb": 10240, "controller\_key": 1000, "key": 2000, "label": "Hard disk 1", "summary": "10,240 KB", "unit\_number": 0}}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

