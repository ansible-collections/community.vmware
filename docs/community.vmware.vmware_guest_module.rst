

community.vmware.vmware_guest module -- Manages virtual machines in vCenter
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to create new virtual machines from templates or other virtual machines, manage power state of virtual machine such as power on, power off, suspend, shutdown, reboot, restart etc., modify various virtual machine components like network, disk, customization etc., rename a virtual machine and remove a virtual machine with associated components.









Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-advanced_settings:

      **advanced_settings**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      Define a list of advanced settings to be added to the VMX config.

      An advanced settings object takes two fields \ :literal:`key`\  and \ :literal:`value`\ .

      Incorrect key and values will be ignored.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-annotation:
      .. _parameter-notes:

      **annotation**

      aliases: notes

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      A note or annotation to include in the virtual machine.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cdrom:

      **cdrom**

      :literal:`any`

      .. raw:: html

        </div></div>

    - 
      A list of CD-ROM configurations for the virtual machine. Added in version 2.9.

      Providing CD-ROM configuration as dict is deprecated and will be removed VMware collection 4.0.0. Please use a list instead.

      Parameters \ :literal:`controller\_type`\ , \ :literal:`controller\_number`\ , \ :literal:`unit\_number`\ , \ :literal:`state`\  are added for a list of CD-ROMs configuration support.

      For \ :literal:`ide`\  controller, hot-add or hot-remove CD-ROM is not supported.


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cdrom/controller_number:

      **controller_number**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      For \ :literal:`ide`\  controller, valid value is 0 or 1.

      For \ :literal:`sata`\  controller, valid value is 0 to 3.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cdrom/controller_type:

      **controller_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Valid options are \ :literal:`ide`\  and \ :literal:`sata`\ .

      Default value is \ :literal:`ide`\ .

      When set to \ :literal:`sata`\ , please make sure \ :literal:`unit\_number`\  is correct and not used by SATA disks.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cdrom/iso_path:

      **iso_path**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The datastore path to the ISO file to use, in the form of \ :literal:`[datastore1] path/to/file.iso`\ .

      Required if type is set \ :literal:`iso`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cdrom/state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Valid value is \ :literal:`present`\  or \ :literal:`absent`\ .

      Default is \ :literal:`present`\ .

      If set to \ :literal:`absent`\ , then the specified CD-ROM will be removed.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cdrom/type:

      **type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The type of CD-ROM, valid options are \ :literal:`none`\ , \ :literal:`client`\  or \ :literal:`iso`\ .

      With \ :literal:`none`\  the CD-ROM will be disconnected but present.

      The default value is \ :literal:`client`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cdrom/unit_number:

      **unit_number**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      For CD-ROM device attach to \ :literal:`ide`\  controller, valid value is 0 or 1.

      For CD-ROM device attach to \ :literal:`sata`\  controller, valid value is 0 to 29.

      \ :literal:`controller\_number`\  and \ :literal:`unit\_number`\  are mandatory attributes.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster:

      **cluster**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The cluster name where the virtual machine will run.

      This is a required parameter, if \ :literal:`esxi\_hostname`\  is not set.

      \ :literal:`esxi\_hostname`\  and \ :literal:`cluster`\  are mutually exclusive parameters.

      This parameter is case sensitive.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-convert:

      **convert**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specify convert disk type while cloning template or virtual machine.


      Choices:

      - :literal:`"thin"`
      - :literal:`"thick"`
      - :literal:`"eagerzeroedthick"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization:

      **customization**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Parameters for OS customization when cloning from the template or the virtual machine, or apply to the existing virtual machine directly.

      Not all operating systems are supported for customization with respective vCenter version, please check VMware documentation for respective OS customization.

      For supported customization operating system matrix, (see \ http://partnerweb.vmware.com/programs/guestOS/guest-os-customization-matrix.pdf\ )

      All parameters and VMware object names are case sensitive.

      Linux based OSes requires Perl package to be installed for OS customizations.


      Default: :literal:`{}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/autologon:

      **autologon**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Auto logon after virtual machine customization.

      Specific to Windows customization.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/autologoncount:

      **autologoncount**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Number of autologon after reboot.

      Specific to Windows customization.

      Ignored if \ :literal:`autologon`\  is unset or set to \ :literal:`false`\ .

      If unset, 1 will be used.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/dns_servers:

      **dns_servers**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of DNS servers to configure.

      Common for Linux and Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/dns_suffix:

      **dns_suffix**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of domain suffixes, also known as DNS search path.

      Default \ :literal:`domain`\  parameter.

      Common for Linux and Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/domain:

      **domain**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      DNS domain name to use.

      Common for Linux and Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/domainadmin:

      **domainadmin**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      User used to join in AD domain.

      Required if \ :literal:`joindomain`\  specified.

      Specific to Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/domainadminpassword:

      **domainadminpassword**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Password used to join in AD domain.

      Required if \ :literal:`joindomain`\  specified.

      Specific to Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/existing_vm:

      **existing_vm**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , do OS customization on the specified virtual machine directly.

      Common for Linux and Windows customization.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/fullname:

      **fullname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Server owner name.

      Specific to Windows customization.

      If unset, "Administrator" will be used as a fall-back.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/hostname:

      **hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Computer hostname.

      Default is shortened \ :literal:`name`\  parameter.

      Allowed characters are alphanumeric (uppercase and lowercase) and minus, rest of the characters are dropped as per RFC 952.

      Common for Linux and Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/hwclockutc:

      **hwclockUTC**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Specifies whether the hardware clock is in UTC or local time.

      Specific to Linux customization.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/joindomain:

      **joindomain**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      AD domain to join.

      Not compatible with \ :literal:`joinworkgroup`\ .

      Specific to Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/joinworkgroup:

      **joinworkgroup**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Workgroup to join.

      Not compatible with \ :literal:`joindomain`\ .

      Specific to Windows customization.

      If unset, "WORKGROUP" will be used as a fall-back.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/orgname:

      **orgname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Organisation name.

      Specific to Windows customization.

      If unset, "ACME" will be used as a fall-back.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/password:

      **password**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Local administrator password.

      If not defined, the password will be set to blank (that is, no password).

      Specific to Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/productid:

      **productid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Product ID.

      Specific to Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/runonce:

      **runonce**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      List of commands to run at first user logon.

      Specific to Windows customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/script_text:

      **script_text**

      :literal:`string`

      added in community.vmware 3.1.0


      .. raw:: html

        </div></div>

    - 
      Script to run with shebang.

      Needs to be enabled in vmware tools with vmware-toolbox-cmd config set deployPkg enable-custom-scripts true

      https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm\_admin.doc/GUID-9A5093A5-C54F-4502-941B-3F9C0F573A39.html

      Specific to Linux customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization/timezone:

      **timezone**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Timezone.

      See List of supported time zones for different vSphere versions in Linux/Unix.

      Common for Linux and Windows customization.

      \ `Windows <https://msdn.microsoft.com/en-us/library/ms912391.aspx>`__\ .




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customization_spec:

      **customization_spec**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Unique name identifying the requested customization specification.

      This parameter is case sensitive.

      If set, then overrides \ :literal:`customization`\  parameter values.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-customvalues:

      **customvalues**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      Define a list of custom values to set on virtual machine.

      A custom value object takes two fields \ :literal:`key`\  and \ :literal:`value`\ .

      Incorrect key and values will be ignored.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination datacenter for the deploy operation.

      This parameter is case sensitive.


      Default: :literal:`"ha-datacenter"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore:

      **datastore**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specify datastore or datastore cluster to provision virtual machine.

      This parameter takes precedence over \ :literal:`disk.datastore`\  parameter.

      This parameter can be used to override datastore or datastore cluster setting of the virtual machine when deployed from the template.

      Please see example for more usage.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-delete_from_inventory:

      **delete_from_inventory**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to delete Virtual machine from inventory or delete from disk.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk:

      **disk**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of disks to add.

      This parameter is case sensitive.

      Shrinking disks is not supported.

      Removing existing disks of the virtual machine is not supported.

      Attributes \ :literal:`controller\_type`\ , \ :literal:`controller\_number`\ , \ :literal:`unit\_number`\  are used to configure multiple types of disk controllers and disks for creating or reconfiguring virtual machine. Added in Ansible 2.10.


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/autoselect_datastore:

      **autoselect_datastore**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Select the less used datastore.

      \ :literal:`disk.datastore`\  and \ :literal:`disk.autoselect\_datastore`\  will not be used if \ :literal:`datastore`\  is specified outside this \ :literal:`disk`\  configuration.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/controller_number:

      **controller_number**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Disk controller bus number.

      The maximum number of same type controller is 4 per VM.


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
      Type of disk controller.

      \ :literal:`nvme`\  controller type support starts on ESXi 6.5 with VM hardware version \ :literal:`version`\  13. Set this type on not supported ESXi or VM hardware version will lead to failure in deployment.

      When set to \ :literal:`sata`\ , please make sure \ :literal:`unit\_number`\  is correct and not used by SATA CDROMs.

      If set to \ :literal:`sata`\  type, please make sure \ :literal:`controller\_number`\  and \ :literal:`unit\_number`\  are set correctly when \ :literal:`cdrom`\  also set to \ :literal:`sata`\  type.


      Choices:

      - :literal:`"buslogic"`
      - :literal:`"lsilogic"`
      - :literal:`"lsilogicsas"`
      - :literal:`"paravirtual"`
      - :literal:`"sata"`
      - :literal:`"nvme"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/datastore:

      **datastore**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The name of datastore which will be used for the disk.

      If \ :literal:`autoselect\_datastore`\  is set to True, will select the less used datastore whose name contains this "disk.datastore" string.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/disk_mode:

      **disk_mode**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of disk mode.

      Added in Ansible 2.6.

      If \ :literal:`persistent`\  specified, changes are immediately and permanently written to the virtual disk. This is default.

      If \ :literal:`independent\_persistent`\  specified, same as persistent, but not affected by snapshots.

      If \ :literal:`independent\_nonpersistent`\  specified, changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.


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
      Existing disk image to be used.

      Filename must already exist on the datastore.

      Specify filename string in \ :literal:`[datastore\_name] path/to/file.vmdk`\  format. Added in Ansible 2.8.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/size:

      **size**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Disk storage size.

      Please specify storage unit like [kb, mb, gb, tb].



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

      .. _parameter-disk/type:

      **type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of disk.

      If \ :literal:`thin`\  specified, disk type is set to thin disk.

      If \ :literal:`eagerzeroedthick`\  specified, disk type is set to eagerzeroedthick disk. Added Ansible 2.5.

      If not specified, disk type is inherited from the source VM or template when cloned and thick disk, no eagerzero otherwise.


      Choices:

      - :literal:`"thin"`
      - :literal:`"thick"`
      - :literal:`"eagerzeroedthick"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk/unit_number:

      **unit_number**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Disk Unit Number.

      Valid value range from 0 to 15 for SCSI controller, except 7.

      Valid value range from 0 to 14 for NVME controller.

      Valid value range from 0 to 29 for SATA controller.

      \ :literal:`controller\_type`\ , \ :literal:`controller\_number`\  and \ :literal:`unit\_number`\  are required when creating or reconfiguring VMs with multiple types of disk controllers and disks.

      When creating new VM, the first configured disk in the \ :literal:`disk`\  list will be "Hard Disk 1".




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ESXi hostname where the virtual machine will run.

      This is a required parameter, if \ :literal:`cluster`\  is not set.

      \ :literal:`esxi\_hostname`\  and \ :literal:`cluster`\  are mutually exclusive parameters.

      This parameter is case sensitive.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination folder, absolute path to find an existing guest or create the new guest.

      The folder should include the datacenter. ESXi's datacenter is ha-datacenter.

      This parameter is case sensitive.

      If multiple machines are found with same name, this parameter is used to identify

      uniqueness of the virtual machine. Added in Ansible 2.5.

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

      .. _parameter-force:

      **force**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Ignore warnings and complete the actions.

      This parameter is useful while removing virtual machine which is powered on state.

      This module reflects the VMware vCenter API and UI workflow, as such, in some cases the \`force\` flag will be mandatory to perform the action to ensure you are certain the action has to be taken, no matter what the consequence. This is specifically the case for removing a powered on the virtual machine when \ :literal:`state`\  is set to \ :literal:`absent`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-guest_id:

      **guest_id**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Set the guest ID.

      This parameter is case sensitive.

      \ :literal:`rhel7\_64Guest`\  for virtual machine with RHEL7 64 bit.

      \ :literal:`centos64Guest`\  for virtual machine with CentOS 64 bit.

      \ :literal:`ubuntu64Guest`\  for virtual machine with Ubuntu 64 bit.

      This field is required when creating a virtual machine, not required when creating from the template.

      Valid values are referenced here: \ https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html\ 
          



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware:

      **hardware**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Manage virtual machine's hardware attributes.

      All parameters case sensitive.


      Default: :literal:`{}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/boot_firmware:

      **boot_firmware**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Choose which firmware should be used to boot the virtual machine.


      Choices:

      - :literal:`"bios"`
      - :literal:`"efi"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/cpu_limit:

      **cpu_limit**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The CPU utilization of a virtual machine will not exceed this limit.

      Unit is MHz.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/cpu_reservation:

      **cpu_reservation**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The amount of CPU resource that is guaranteed available to the virtual machine.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/cpu_shares:

      **cpu_shares**

      :literal:`integer`

      added in community.vmware 3.2.0


      .. raw:: html

        </div></div>

    - 
      The number of shares of CPU allocated to this virtual machine

      cpu\_shares\_level will automatically be set to 'custom'



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/cpu_shares_level:

      **cpu_shares_level**

      :literal:`string`

      added in community.vmware 3.2.0


      .. raw:: html

        </div></div>

    - 
      The allocation level of CPU resources for the virtual machine.

      Valid Values are \ :literal:`low`\ , \ :literal:`normal`\ , \ :literal:`high`\  and \ :literal:`custom`\ .


      Choices:

      - :literal:`"low"`
      - :literal:`"normal"`
      - :literal:`"high"`
      - :literal:`"custom"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/hotadd_cpu:

      **hotadd_cpu**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allow virtual CPUs to be added while the virtual machine is running.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/hotadd_memory:

      **hotadd_memory**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allow memory to be added while the virtual machine is running.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/hotremove_cpu:

      **hotremove_cpu**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allow virtual CPUs to be removed while the virtual machine is running.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/iommu:

      **iommu**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Flag to specify if I/O MMU is enabled for this virtual machine.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/max_connections:

      **max_connections**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Maximum number of active remote display connections for the virtual machines.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/mem_limit:

      **mem_limit**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The memory utilization of a virtual machine will not exceed this limit.

      Unit is MB.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/mem_reservation:
      .. _parameter-hardware/memory_reservation:

      **mem_reservation**

      aliases: memory_reservation

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The amount of memory resource that is guaranteed available to the virtual machine.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/mem_shares:

      **mem_shares**

      :literal:`integer`

      added in community.vmware 3.2.0


      .. raw:: html

        </div></div>

    - 
      The number of shares of memory allocated to this virtual machine

      mem\_shares\_level will automatically be set to 'custom'



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/mem_shares_level:

      **mem_shares_level**

      :literal:`string`

      added in community.vmware 3.2.0


      .. raw:: html

        </div></div>

    - 
      The allocation level of memory resources for the virtual machine.

      Valid Values are \ :literal:`low`\ , \ :literal:`normal`\ , \ :literal:`high`\  and \ :literal:`custom`\ .


      Choices:

      - :literal:`"low"`
      - :literal:`"normal"`
      - :literal:`"high"`
      - :literal:`"custom"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/memory_mb:

      **memory_mb**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Amount of memory in MB.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/memory_reservation_lock:

      **memory_reservation_lock**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set \ :literal:`true`\ , memory resource reservation for the virtual machine.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/nested_virt:

      **nested_virt**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable nested virtualization.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/num_cpu_cores_per_socket:

      **num_cpu_cores_per_socket**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Number of Cores Per Socket.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/num_cpus:

      **num_cpus**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Number of CPUs.

      \ :literal:`num\_cpus`\  must be a multiple of \ :literal:`num\_cpu\_cores\_per\_socket`\ .

      For example, to create a VM with 2 sockets of 4 cores, specify \ :literal:`num\_cpus`\  as 8 and \ :literal:`num\_cpu\_cores\_per\_socket`\  as 4.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/scsi:

      **scsi**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Valid values are \ :literal:`buslogic`\ , \ :literal:`lsilogic`\ , \ :literal:`lsilogicsas`\  and \ :literal:`paravirtual`\ .

      \ :literal:`paravirtual`\  is default.


      Choices:

      - :literal:`"buslogic"`
      - :literal:`"lsilogic"`
      - :literal:`"lsilogicsas"`
      - :literal:`"paravirtual"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/secure_boot:

      **secure_boot**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to enable or disable (U)EFI secure boot.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/version:

      **version**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The Virtual machine hardware versions.

      Default is 10 (ESXi 5.5 and onwards).

      If set to \ :literal:`latest`\ , the specified virtual machine will be upgraded to the most current hardware version supported on the host.

      \ :literal:`latest`\  is added in Ansible 2.10.

      Please check VMware documentation for correct virtual machine hardware version.

      Incorrect hardware version may lead to failure in deployment. If hardware version is already equal to the given.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/virt_based_security:

      **virt_based_security**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable Virtualization Based Security feature for Windows on ESXi 6.7 and later, from hardware version 14.

      Supported Guest OS are Windows 10 64 bit, Windows Server 2016, Windows Server 2019 and later.

      The firmware of virtual machine must be EFI and secure boot must be enabled.

      Virtualization Based Security depends on nested virtualization and Intel Virtualization Technology for Directed I/O.

      Deploy on unsupported ESXi, hardware version or firmware may lead to failure or deployed VM with unexpected configurations.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hardware/vpmc_enabled:

      **vpmc_enabled**

      :literal:`boolean`

      added in community.vmware 3.2.0


      .. raw:: html

        </div></div>

    - 
      Enable virtual CPU Performance Counters.


      Choices:

      - :literal:`false`
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

      .. _parameter-is_template:

      **is_template**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Flag the instance as a template.

      This will mark the given virtual machine as template.

      Note, this may need to be done in a dedicated task invocation that is not making any other changes. For example, user cannot change the state from powered-on to powered-off AND save as template in the same task.

      See \ `community.vmware.vmware\_guest <vmware_guest_module.rst>`__\  source for more details.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-linked_clone:

      **linked_clone**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to create a linked clone from the snapshot specified.

      If specified, then \ :literal:`snapshot\_src`\  is required parameter.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the virtual machine to work with.

      Virtual machine names in vCenter are not necessarily unique, which may be problematic, see \ :literal:`name\_match`\ .

      If multiple virtual machines with same name exists, then \ :literal:`folder`\  is required parameter to identify uniqueness of the virtual machine.

      This parameter is required, if \ :literal:`state`\  is set to \ :literal:`poweredon`\ , \ :literal:`powered-on`\ , \ :literal:`poweredoff`\ , \ :literal:`powered-off`\ , \ :literal:`present`\ , \ :literal:`restarted`\ , \ :literal:`suspended`\  and virtual machine does not exists.

      This parameter is case sensitive.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name_match:

      **name_match**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If multiple virtual machines matching the name, use the first or last found.


      Choices:

      - :literal:`"first"` ← (default)
      - :literal:`"last"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks:

      **networks**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of networks (in the order of the NICs).

      Removing NICs is not allowed, while reconfiguring the virtual machine.

      All parameters and VMware object names are case sensitive.

      The \ :emphasis:`type`\ , \ :emphasis:`ip`\ , \ :emphasis:`netmask`\ , \ :emphasis:`gateway`\ , \ :emphasis:`domain`\ , \ :emphasis:`dns\_servers`\  options don't set to a guest when creating a blank new virtual machine. They are set by the customization via vmware-tools. If you want to set the value of the options to a guest, you need to clone from a template with installed OS and vmware-tools(also Perl when Linux).


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/connected:

      **connected**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Indicates whether the NIC is currently connected.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/device_type:

      **device_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Virtual network device.

      Valid value can be one of \ :literal:`e1000`\ , \ :literal:`e1000e`\ , \ :literal:`pcnet32`\ , \ :literal:`vmxnet2`\ , \ :literal:`vmxnet3`\ , \ :literal:`sriov`\ .

      \ :literal:`vmxnet3`\  is default.

      Optional per entry.

      Used for virtual hardware.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/dns_servers:

      **dns_servers**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      DNS servers for this network interface (Windows).

      Optional per entry.

      Used for OS customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/domain:

      **domain**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Domain name for this network interface (Windows).

      Optional per entry.

      Used for OS customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/dvswitch_name:

      **dvswitch_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the distributed vSwitch.

      Optional per entry.

      Used for virtual hardware.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/gateway:

      **gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Static gateway.

      Optional per entry.

      Used for OS customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/ip:

      **ip**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Static IP address. Implies \ :literal:`type=static`\ .

      Optional per entry.

      Used for OS customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/mac:

      **mac**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Customize MAC address.

      Optional per entry.

      Used for virtual hardware.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the portgroup or distributed virtual portgroup for this interface.

      Required per entry.

      When specifying distributed virtual portgroup make sure given \ :literal:`esxi\_hostname`\  or \ :literal:`cluster`\  is associated with it.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/netmask:

      **netmask**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Static netmask required for \ :literal:`ip`\ .

      Optional per entry.

      Used for OS customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/start_connected:

      **start_connected**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Specifies whether or not to connect the device when the virtual machine starts.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/type:

      **type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Type of IP assignment.

      Valid values are one of \ :literal:`dhcp`\ , \ :literal:`static`\ .

      \ :literal:`dhcp`\  is default.

      Optional per entry.

      Used for OS customization.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks/vlan:

      **vlan**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      VLAN number for this interface.

      Required per entry.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nvdimm:

      **nvdimm**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Add or remove a virtual NVDIMM device to the virtual machine.

      VM virtual hardware version must be 14 or higher on vSphere 6.7 or later.

      Verify that guest OS of the virtual machine supports PMem before adding virtual NVDIMM device.

      Verify that you have the \ :emphasis:`Datastore.Allocate`\  space privilege on the virtual machine.

      Make sure that the host or the cluster on which the virtual machine resides has available PMem resources.

      To add or remove virtual NVDIMM device to the existing virtual machine, it must be in power off state.


      Default: :literal:`{}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nvdimm/label:

      **label**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The label of the virtual NVDIMM device to be removed or configured, e.g., "NVDIMM 1".

      This parameter is required when \ :literal:`state`\  is set to \ :literal:`absent`\ , or \ :literal:`present`\  to reconfigure NVDIMM device size. When add a new device, please do not set \ :literal:`label`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nvdimm/size_mb:

      **size_mb**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Virtual NVDIMM device size in MB.


      Default: :literal:`1024`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nvdimm/state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Valid value is \ :literal:`present`\  or \ :literal:`absent`\ .

      If set to \ :literal:`absent`\ , then the NVDIMM device with specified \ :literal:`label`\  will be removed.


      Choices:

      - :literal:`"present"`
      - :literal:`"absent"`




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

      .. _parameter-resource_pool:

      **resource_pool**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Use the given resource pool for virtual machine operation.

      This parameter is case sensitive.

      Resource pool should be child of the selected host parent.

      When not specified \ :emphasis:`Resources`\  is taken as default value.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snapshot_src:

      **snapshot_src**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the existing snapshot to use to create a clone of a virtual machine.

      This parameter is case sensitive.

      While creating linked clone using \ :literal:`linked\_clone`\  parameter, this parameter is required.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specify the state the virtual machine should be in.

      If \ :literal:`state`\  is set to \ :literal:`present`\  and virtual machine exists, ensure the virtual machine configurations conforms to task arguments.

      If \ :literal:`state`\  is set to \ :literal:`absent`\  and virtual machine exists, then the specified virtual machine is removed with it's associated components.

      If \ :literal:`state`\  is set to one of the following \ :literal:`poweredon`\ , \ :literal:`powered-on`\ , \ :literal:`poweredoff`\ , \ :literal:`powered-off`\ , \ :literal:`present`\ , \ :literal:`restarted`\ , \ :literal:`suspended`\  and virtual machine does not exists, virtual machine is deployed with the given parameters.

      If \ :literal:`state`\  is set to \ :literal:`poweredon`\  or \ :literal:`powered-on`\  and virtual machine exists with powerstate other than powered on, then the specified virtual machine is powered on.

      If \ :literal:`state`\  is set to \ :literal:`poweredoff`\  or \ :literal:`powered-off`\  and virtual machine exists with powerstate other than powered off, then the specified virtual machine is powered off.

      If \ :literal:`state`\  is set to \ :literal:`restarted`\  and virtual machine exists, then the virtual machine is restarted.

      If \ :literal:`state`\  is set to \ :literal:`suspended`\  and virtual machine exists, then the virtual machine is set to suspended mode.

      If \ :literal:`state`\  is set to \ :literal:`shutdownguest`\  or \ :literal:`shutdown-guest`\  and virtual machine exists, then the virtual machine is shutdown.

      If \ :literal:`state`\  is set to \ :literal:`rebootguest`\  or \ :literal:`reboot-guest`\  and virtual machine exists, then the virtual machine is rebooted.

      Powerstate \ :literal:`powered-on`\  and \ :literal:`powered-off`\  is added in version 2.10.


      Choices:

      - :literal:`"absent"`
      - :literal:`"poweredon"`
      - :literal:`"powered-on"`
      - :literal:`"poweredoff"`
      - :literal:`"powered-off"`
      - :literal:`"present"` ← (default)
      - :literal:`"rebootguest"`
      - :literal:`"reboot-guest"`
      - :literal:`"restarted"`
      - :literal:`"suspended"`
      - :literal:`"shutdownguest"`
      - :literal:`"shutdown-guest"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state_change_timeout:

      **state_change_timeout**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      If the \ :literal:`state`\  is set to \ :literal:`shutdownguest`\ , by default the module will return immediately after sending the shutdown signal.

      If this argument is set to a positive integer, the module will instead wait for the virtual machine to reach the poweredoff state.

      The value sets a timeout in seconds for the module to wait for the state change.


      Default: :literal:`0`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-template:
      .. _parameter-template_src:

      **template**

      aliases: template_src

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Template or existing virtual machine used to create new virtual machine.

      If this value is not set, virtual machine is created without using a template.

      If the virtual machine already exists, this parameter will be ignored.

      This parameter is case sensitive.

      From version 2.8 onwards, absolute path to virtual machine or template can be used.



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
      UUID of the virtual machine to manage if known, this is VMware's unique identifier.

      This is required if \ :literal:`name`\  is not supplied.

      If virtual machine does not exists, then this parameter is ignored.

      Please note that a supplied UUID will be ignored on virtual machine creation, as VMware creates the UUID internally.



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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vapp_properties:

      **vapp_properties**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of vApp properties.

      For full list of attributes and types refer to: \ https://code.vmware.com/apis/704/vsphere/vim.vApp.PropertyInfo.html\ 


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vapp_properties/id:

      **id**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Property ID.

      Required per entry.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vapp_properties/operation:

      **operation**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The \ :literal:`remove`\  attribute is required only when removing properties.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vapp_properties/type:

      **type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Value type, string type by default.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vapp_properties/value:

      **value**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Property value.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_for_customization:

      **wait_for_customization**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Wait until vCenter detects all guest customizations as successfully completed.

      When enabled, the VM will automatically be powered on.

      If vCenter does not detect guest customization start or succeed, failed events after time \ :literal:`wait\_for\_customization\_timeout`\  parameter specified, warning message will be printed and task result is fail.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_for_customization_timeout:

      **wait_for_customization_timeout**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Define a timeout (in seconds) for the wait\_for\_customization parameter.

      Be careful when setting this value since the time guest customization took may differ among guest OSes.


      Default: :literal:`3600`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_for_ip_address:

      **wait_for_ip_address**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Wait until vCenter detects an IP address for the virtual machine.

      This requires vmware-tools (vmtoolsd) to properly work after creation.

      vmware-tools needs to be installed on the given virtual machine in order to work with this parameter.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_for_ip_address_timeout:

      **wait_for_ip_address_timeout**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Define a timeout (in seconds) for the wait\_for\_ip\_address parameter.


      Default: :literal:`300`




Notes
-----

- Please make sure that the user used for \ `community.vmware.vmware\_guest <vmware_guest_module.rst>`__\  has the correct level of privileges.
- For example, following is the list of minimum privileges required by users to create virtual machines.
-    DataStore \> Allocate Space
-    Virtual Machine \> Configuration \> Add New Disk
-    Virtual Machine \> Configuration \> Add or Remove Device
-    Virtual Machine \> Inventory \> Create New
-    Network \> Assign Network
-    Resource \> Assign Virtual Machine to Resource Pool
- Module may require additional privileges as well, which may be required for gathering facts - e.g. ESXi configurations.
- Use SCSI disks instead of IDE when you want to expand online disks by specifying a SCSI controller.
- Uses SysPrep for Windows VM (depends on 'guest\_id' parameter match 'win') with PyVmomi.
- In order to change the VM's parameters (e.g. number of CPUs), the VM must be powered off unless the hot-add support is enabled and the \ :literal:`state=present`\  must be used to apply the changes.
- For additional information please visit Ansible VMware community wiki - \ https://github.com/ansible/community/wiki/VMware\ .
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Create a virtual machine on given ESXi hostname
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: /DC1/vm/
        name: test_vm_0001
        state: poweredon
        guest_id: centos64Guest
        # This is hostname of particular ESXi server on which user wants VM to be deployed
        esxi_hostname: "{{ esxi_hostname }}"
        disk:
        - size_gb: 10
          type: thin
          datastore: datastore1
        hardware:
          memory_mb: 512
          num_cpus: 4
          scsi: paravirtual
        networks:
        - name: VM Network
          mac: aa:bb:dd:aa:00:14
          ip: 10.10.10.100
          netmask: 255.255.255.0
          device_type: vmxnet3
        wait_for_ip_address: true
        wait_for_ip_address_timeout: 600
      delegate_to: localhost
      register: deploy_vm

    - name: Create a virtual machine from a template
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: /testvms
        name: testvm_2
        state: poweredon
        template: template_el7
        disk:
        - size_gb: 10
          type: thin
          datastore: g73_datastore
        # Add another disk from an existing VMDK
        - filename: "[datastore1] testvms/testvm_2_1/testvm_2_1.vmdk"
        hardware:
          memory_mb: 512
          num_cpus: 6
          num_cpu_cores_per_socket: 3
          scsi: paravirtual
          memory_reservation_lock: true
          mem_limit: 8096
          mem_reservation: 4096
          cpu_shares_level: "high"
          mem_shares_level: "high"
          cpu_limit: 8096
          cpu_reservation: 4096
          max_connections: 5
          hotadd_cpu: true
          hotremove_cpu: true
          hotadd_memory: false
          version: 12 # Hardware version of virtual machine
          boot_firmware: "efi"
        cdrom:
            - controller_number: 0
              unit_number: 0
              state: present
              type: iso
              iso_path: "[datastore1] livecd.iso"
        networks:
        - name: VM Network
          mac: aa:bb:dd:aa:00:14
        wait_for_ip_address: true
      delegate_to: localhost
      register: deploy

    - name: Clone a virtual machine from Windows template and customize
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: datacenter1
        cluster: cluster
        name: testvm-2
        template: template_windows
        networks:
        - name: VM Network
          ip: 192.168.1.100
          netmask: 255.255.255.0
          gateway: 192.168.1.1
          mac: aa:bb:dd:aa:00:14
          domain: my_domain
          dns_servers:
          - 192.168.1.1
          - 192.168.1.2
        - vlan: 1234
          type: dhcp
        customization:
          autologon: true
          dns_servers:
          - 192.168.1.1
          - 192.168.1.2
          domain: my_domain
          password: new_vm_password
          runonce:
          - powershell.exe -ExecutionPolicy Unrestricted -File C:\Windows\Temp\ConfigureRemotingForAnsible.ps1 -ForceNewSSLCert -EnableCredSSP
      delegate_to: localhost

    - name:  Clone a virtual machine from Linux template and customize
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        state: present
        folder: /DC1/vm
        template: "{{ template }}"
        name: "{{ vm_name }}"
        cluster: DC1_C1
        networks:
          - name: VM Network
            ip: 192.168.10.11
            netmask: 255.255.255.0
        wait_for_ip_address: true
        customization:
          domain: "{{ guest_domain }}"
          dns_servers:
            - 8.9.9.9
            - 7.8.8.9
          dns_suffix:
            - example.com
            - example2.com
          script_text: |
            #!/bin/bash
            touch /tmp/touch-from-playbook
      delegate_to: localhost

    - name: Rename a virtual machine (requires the virtual machine's uuid)
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        uuid: "{{ vm_uuid }}"
        name: new_name
        state: present
      delegate_to: localhost

    - name: Remove a virtual machine by uuid
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        uuid: "{{ vm_uuid }}"
        state: absent
      delegate_to: localhost

    - name: Remove a virtual machine from inventory
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: vm_name
        delete_from_inventory: true
        state: absent
      delegate_to: localhost

    - name: Manipulate vApp properties
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: vm_name
        state: present
        vapp_properties:
          - id: remoteIP
            category: Backup
            label: Backup server IP
            type: string
            value: 10.10.10.1
          - id: old_property
            operation: remove
      delegate_to: localhost

    - name: Set powerstate of a virtual machine to poweroff by using UUID
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        uuid: "{{ vm_uuid }}"
        state: poweredoff
      delegate_to: localhost

    - name: Deploy a virtual machine in a datastore different from the datastore of the template
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: "{{ vm_name }}"
        state: present
        template: "{{ template_name }}"
        # Here datastore can be different which holds template
        datastore: "{{ virtual_machine_datastore }}"
        hardware:
          memory_mb: 512
          num_cpus: 2
          scsi: paravirtual
      delegate_to: localhost

    - name: Create a diskless VM
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ dc1 }}"
        state: poweredoff
        cluster: "{{ ccr1 }}"
        name: diskless_vm
        folder: /Asia-Datacenter1/vm
        guest_id: centos64Guest
        datastore: "{{ ds1 }}"
        hardware:
            memory_mb: 1024
            num_cpus: 2
            num_cpu_cores_per_socket: 1

    - name: Create a VM with multiple disks of different disk controller types
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: /DC1/vm/
        name: test_vm_multi_disks
        state: poweredoff
        guest_id: centos64Guest
        datastore: datastore1
        disk:
        - size_gb: 10
          controller_type: 'nvme'
          controller_number: 0
          unit_number: 0
        - size_gb: 10
          controller_type: 'paravirtual'
          controller_number: 0
          unit_number: 1
        - size_gb: 10
          controller_type: 'sata'
          controller_number: 0
          unit_number: 2
        hardware:
          memory_mb: 512
          num_cpus: 4
          version: 14
        networks:
        - name: VM Network
          device_type: vmxnet3
      delegate_to: localhost
      register: deploy_vm

    - name: Create a VM with NVDIMM device
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: /DC1/vm/
        name: test_vm_nvdimm
        state: poweredoff
        guest_id: centos7_64Guest
        datastore: datastore1
        hardware:
          memory_mb: 512
          num_cpus: 4
          version: 14
        networks:
        - name: VM Network
          device_type: vmxnet3
        nvdimm:
          state: present
          size_mb: 2048
      delegate_to: localhost
      register: deploy_vm





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

      .. _return-instance:

      **instance**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the new virtual machine


      Returned: always

      Sample: :literal:`"None"`




Authors
~~~~~~~

- Loic Blot (@nerzhul) 
- Philippe Dellaert (@pdellaert) 
- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

