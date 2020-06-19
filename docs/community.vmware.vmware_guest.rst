:orphan:

.. _community.vmware.vmware_guest_module:


*****************************
community.vmware.vmware_guest
*****************************

**Manages virtual machines in vCenter**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to create new virtual machines from templates or other virtual machines, manage power state of virtual machine such as power on, power off, suspend, shutdown, reboot, restart etc., modify various virtual machine components like network, disk, customization etc., rename a virtual machine and remove a virtual machine with associated components.




Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.6
- PyVmomi


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>annotation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A note or annotation to include in the virtual machine.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cdrom</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A CD-ROM configuration for the virtual machine.</div>
                                            <div>Or a list of CD-ROMs configuration for the virtual machine. Added in version 2.9.</div>
                                            <div>Parameters <code>controller_type</code>, <code>controller_number</code>, <code>unit_number</code>, <code>state</code> are added for a list of CD-ROMs configuration support.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>type</code> (string): The type of CD-ROM, valid options are <code>none</code>, <code>client</code> or <code>iso</code>. With <code>none</code> the CD-ROM will be disconnected but present. The default value is <code>client</code>.</div>
                                            <div>- <code>iso_path</code> (string): The datastore path to the ISO file to use, in the form of <code>[datastore1] path/to/file.iso</code>. Required if type is set <code>iso</code>.</div>
                                            <div>- <code>controller_type</code> (string): Valid options are <code>ide</code> and <code>sata</code>. Default value is <code>ide</code>.</div>
                                            <div>When set to <code>sata</code>, please make sure <code>unit_number</code> is correct and not used by SATA disks.</div>
                                            <div>- <code>controller_number</code> (int): For <code>ide</code> controller, valid value is 0 or 1. For <code>sata</code> controller, valid value is 0 to 3.</div>
                                            <div>- <code>unit_number</code> (int): For CD-ROM device attach to <code>ide</code> controller, valid value is 0 or 1, attach to <code>sata</code> controller, valid value is 0 to 29. <code>controller_number</code> and <code>unit_number</code> are mandatory attributes.</div>
                                            <div>- <code>state</code> (string): Valid value is <code>present</code> or <code>absent</code>. Default is <code>present</code>. If set to <code>absent</code>, then the specified CD-ROM will be removed. For <code>ide</code> controller, hot-add or hot-remove CD-ROM is not supported.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cluster</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The cluster name where the virtual machine will run.</div>
                                            <div>This is a required parameter, if <code>esxi_hostname</code> is not set.</div>
                                            <div><code>esxi_hostname</code> and <code>cluster</code> are mutually exclusive parameters.</div>
                                            <div>This parameter is case sensitive.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>convert</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>thin</li>
                                                                                                                                                                                                <li>thick</li>
                                                                                                                                                                                                <li>eagerzeroedthick</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specify convert disk type while cloning template or virtual machine.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>customization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Parameters for OS customization when cloning from the template or the virtual machine, or apply to the existing virtual machine directly.</div>
                                            <div>Not all operating systems are supported for customization with respective vCenter version, please check VMware documentation for respective OS customization.</div>
                                            <div>For supported customization operating system matrix, (see <a href='http://partnerweb.vmware.com/programs/guestOS/guest-os-customization-matrix.pdf'>http://partnerweb.vmware.com/programs/guestOS/guest-os-customization-matrix.pdf</a>)</div>
                                            <div>All parameters and VMware object names are case sensitive.</div>
                                            <div>Linux based OSes requires Perl package to be installed for OS customizations.</div>
                                            <div>Common parameters (Linux/Windows):</div>
                                            <div>- <code>existing_vm</code> (bool): If set to <code>True</code>, do OS customization on the specified virtual machine directly.</div>
                                            <div>- <code>dns_servers</code> (list): List of DNS servers to configure.</div>
                                            <div>- <code>dns_suffix</code> (list): List of domain suffixes, also known as DNS search path (default: <code>domain</code> parameter).</div>
                                            <div>- <code>domain</code> (string): DNS domain name to use.</div>
                                            <div>- <code>hostname</code> (string): Computer hostname (default: shorted <code>name</code> parameter). Allowed characters are alphanumeric (uppercase and lowercase) and minus, rest of the characters are dropped as per RFC 952.</div>
                                            <div>Parameters related to Linux customization:</div>
                                            <div>- <code>timezone</code> (string): Timezone (See List of supported time zones for different vSphere versions in Linux/Unix</div>
                                            <div>- <code>hwclockUTC</code> (bool): Specifies whether the hardware clock is in UTC or local time.</div>
                                            <div>Parameters related to Windows customization:</div>
                                            <div>- <code>autologon</code> (bool): Auto logon after virtual machine customization (default: False).</div>
                                            <div>- <code>autologoncount</code> (int): Number of autologon after reboot (default: 1).</div>
                                            <div>- <code>domainadmin</code> (string): User used to join in AD domain (mandatory with <code>joindomain</code>).</div>
                                            <div>- <code>domainadminpassword</code> (string): Password used to join in AD domain (mandatory with <code>joindomain</code>).</div>
                                            <div>- <code>fullname</code> (string): Server owner name (default: Administrator).</div>
                                            <div>- <code>joindomain</code> (string): AD domain to join (Not compatible with <code>joinworkgroup</code>).</div>
                                            <div>- <code>joinworkgroup</code> (string): Workgroup to join (Not compatible with <code>joindomain</code>, default: WORKGROUP).</div>
                                            <div>- <code>orgname</code> (string): Organisation name (default: ACME).</div>
                                            <div>- <code>password</code> (string): Local administrator password.</div>
                                            <div>- <code>productid</code> (string): Product ID.</div>
                                            <div>- <code>runonce</code> (list): List of commands to run at first user logon.</div>
                                            <div>- <code>timezone</code> (int): Timezone (See <a href='https://msdn.microsoft.com/en-us/library/ms912391.aspx'>https://msdn.microsoft.com/en-us/library/ms912391.aspx</a>).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>customization_spec</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Unique name identifying the requested customization specification.</div>
                                            <div>This parameter is case sensitive.</div>
                                            <div>If set, then overrides <code>customization</code> parameter values.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>customvalues</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Define a list of custom values to set on virtual machine.</div>
                                            <div>A custom value object takes two fields <code>key</code> and <code>value</code>.</div>
                                            <div>Incorrect key and values will be ignored.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datacenter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"ha-datacenter"</div>
                                    </td>
                                                                <td>
                                            <div>Destination datacenter for the deploy operation.</div>
                                            <div>This parameter is case sensitive.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datastore</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Specify datastore or datastore cluster to provision virtual machine.</div>
                                            <div>This parameter takes precedence over &quot;disk.datastore&quot; parameter.</div>
                                            <div>This parameter can be used to override datastore or datastore cluster setting of the virtual machine when deployed from the template.</div>
                                            <div>Please see example for more usage.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>delete_from_inventory</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to delete Virtual machine from inventory or delete from disk.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disk</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of disks to add.</div>
                                            <div>This parameter is case sensitive.</div>
                                            <div>Shrinking disks is not supported.</div>
                                            <div>Removing existing disks of the virtual machine is not supported.</div>
                                            <div>Attributes <code>controller_type</code>, <code>controller_number</code>, <code>unit_number</code> are used to configure multiple types of disk controllers and disks for creating or reconfiguring virtual machine. Added in version 2.10</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>size_[tb,gb,mb,kb]</code> (integer): Disk storage size in specified unit.</div>
                                            <div>- <code>type</code> (string): Valid values are:</div>
                                            <div>- <code>thin</code> thin disk</div>
                                            <div>- <code>eagerzeroedthick</code> eagerzeroedthick disk, added in version 2.5</div>
                                            <div>Default: <code>None</code> thick disk, no eagerzero.</div>
                                            <div>- <code>datastore</code> (string): The name of datastore which will be used for the disk. If <code>autoselect_datastore</code> is set to True, then will select the less used datastore whose name contains this &quot;disk.datastore&quot; string.</div>
                                            <div>- <code>filename</code> (string): Existing disk image to be used. Filename must already exist on the datastore.</div>
                                            <div>Specify filename string in <code>[datastore_name] path/to/file.vmdk</code> format. Added in version 2.8.</div>
                                            <div>- <code>autoselect_datastore</code> (bool): select the less used datastore. &quot;disk.datastore&quot; and &quot;disk.autoselect_datastore&quot; will not be used if <code>datastore</code> is specified outside this <code>disk</code> configuration.</div>
                                            <div>- <code>disk_mode</code> (string): Type of disk mode. Added in version 2.6</div>
                                            <div>- Available options are :</div>
                                            <div>- <code>persistent</code>: Changes are immediately and permanently written to the virtual disk. This is default.</div>
                                            <div>- <code>independent_persistent</code>: Same as persistent, but not affected by snapshots.</div>
                                            <div>- <code>independent_nonpersistent</code>: Changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.</div>
                                            <div>- <code>controller_type</code> (string): Type of disk controller. Valid values are <code>buslogic</code>, <code>lsilogic</code>, <code>lsilogicsas</code>, <code>paravirtual</code>, <code>sata</code> and <code>nvme</code>. When set to <code>sata</code>, please make sure <code>unit_number</code> is correct and not used by SATA CDROMs.</div>
                                            <div><code>nvme</code> support starts from hardware <code>version</code> 13 and ESXi version 6.5.</div>
                                            <div>If set to <code>sata</code> type, please make sure <code>controller_number</code> and <code>unit_number</code> are set correctly when <code>cdrom</code> also set to <code>sata</code> type.</div>
                                            <div>- <code>controller_number</code> (integer): Disk controller bus number. The maximum number of same type controller is 4 per VM. Valid value range from 0 to 3.</div>
                                            <div>- <code>unit_number</code> (integer): Disk Unit Number.</div>
                                            <div>Valid value range from 0 to 15 for SCSI controller, except 7.</div>
                                            <div>Valid value range from 0 to 14 for NVME controller.</div>
                                            <div>Valid value range from 0 to 29 for SATA controller.</div>
                                            <div><code>controller_type</code>, <code>controller_number</code> and <code>unit_number</code> are required when creating or reconfiguring VMs with multiple types of disk controllers and disks. When creating new VM, the first configured disk in the <code>disk</code> list will be &quot;Hard Disk 1&quot;.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esxi_hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The ESXi hostname where the virtual machine will run.</div>
                                            <div>This is a required parameter, if <code>cluster</code> is not set.</div>
                                            <div><code>esxi_hostname</code> and <code>cluster</code> are mutually exclusive parameters.</div>
                                            <div>This parameter is case sensitive.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>folder</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Destination folder, absolute path to find an existing guest or create the new guest.</div>
                                            <div>The folder should include the datacenter. ESX&#x27;s datacenter is ha-datacenter.</div>
                                            <div>This parameter is case sensitive.</div>
                                            <div>If multiple machines are found with same name, this parameter is used to identify</div>
                                            <div>Examples:</div>
                                            <div>folder: /ha-datacenter/vm</div>
                                            <div>folder: ha-datacenter/vm</div>
                                            <div>folder: /datacenter1/vm</div>
                                            <div>folder: datacenter1/vm</div>
                                            <div>folder: /datacenter1/vm/folder1</div>
                                            <div>folder: datacenter1/vm/folder1</div>
                                            <div>folder: /folder1/datacenter1/vm</div>
                                            <div>folder: folder1/datacenter1/vm</div>
                                            <div>folder: /folder1/datacenter1/vm/folder2</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>force</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Ignore warnings and complete the actions.</div>
                                            <div>This parameter is useful while removing virtual machine which is powered on state.</div>
                                            <div>This module reflects the VMware vCenter API and UI workflow, as such, in some cases the `force` flag will be mandatory to perform the action to ensure you are certain the action has to be taken, no matter what the consequence. This is specifically the case for removing a powered on the virtual machine when <code>state</code> is set to <code>absent</code>.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>guest_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Set the guest ID.</div>
                                            <div>This parameter is case sensitive. For instance:</div>
                                            <div>- virtual machine with RHEL7 64 bit, will be &#x27;rhel7_64Guest&#x27;</div>
                                            <div>- virtual machine with CentOS 64 bit, will be &#x27;centos64Guest&#x27;</div>
                                            <div>- virtual machine with Ubuntu 64 bit, will be &#x27;ubuntu64Guest&#x27;</div>
                                            <div>This field is required when creating a virtual machine, not required when creating from the template.</div>
                                            <div>Valid values are referenced here: <a href='https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html'>https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html</a></div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hardware</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Manage virtual machine&#x27;s hardware attributes.</div>
                                            <div>All parameters case sensitive.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>hotadd_cpu</code> (boolean): Allow virtual CPUs to be added while the virtual machine is running.</div>
                                            <div>- <code>hotremove_cpu</code> (boolean): Allow virtual CPUs to be removed while the virtual machine is running.</div>
                                            <div>- <code>hotadd_memory</code> (boolean): Allow memory to be added while the virtual machine is running.</div>
                                            <div>- <code>memory_mb</code> (integer): Amount of memory in MB.</div>
                                            <div>- <code>num_cpus</code> (integer): Number of CPUs. <code>num_cpus</code> must be a multiple of <code>num_cpu_cores_per_socket</code>.</div>
                                            <div>For example to create a VM with 2 sockets of 4 cores, specify <code>num_cpus</code>: 8 and <code>num_cpu_cores_per_socket</code>: 4</div>
                                            <div>- <code>num_cpu_cores_per_socket</code> (integer): Number of Cores Per Socket.</div>
                                            <div>- <code>scsi</code> (string): Valid values are <code>buslogic</code>, <code>lsilogic</code>, <code>lsilogicsas</code> and <code>paravirtual</code> (default).</div>
                                            <div>- <code>memory_reservation_lock</code> (boolean): If set true, memory resource reservation for the virtual machine</div>
                                            <div>- <code>max_connections</code> (integer): Maximum number of active remote display connections for the virtual machines.</div>
                                            <div>- <code>mem_limit</code> (integer): The memory utilization of a virtual machine will not exceed this limit. Unit is MB.</div>
                                            <div>- <code>mem_reservation</code> (integer): The amount of memory resource that is guaranteed available to the virtual</div>
                                            <div>- <code>cpu_limit</code> (integer): The CPU utilization of a virtual machine will not exceed this limit. Unit is MHz.</div>
                                            <div>- <code>cpu_reservation</code> (integer): The amount of CPU resource that is guaranteed available to the virtual machine.</div>
                                            <div>- <code>version</code> (integer): The Virtual machine hardware versions. Default is 10 (ESXi 5.5 and onwards).</div>
                                            <div>If value specified as <code>latest</code>, version is set to the most current virtual hardware supported on the host.</div>
                                            <div><code>latest</code> is added in version 2.10.</div>
                                            <div>Please check VMware documentation for correct virtual machine hardware version.</div>
                                            <div>Incorrect hardware version may lead to failure in deployment. If hardware version is already equal to the given</div>
                                            <div>- <code>boot_firmware</code> (string): Choose which firmware should be used to boot the virtual machine.</div>
                                            <div>- <code>virt_based_security</code> (bool): Enable Virtualization Based Security feature for Windows 10.</div>
                                            <div>(Support from Virtual machine hardware version 14, Guest OS Windows 10 64 bit, Windows Server 2016)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The hostname or IP address of the vSphere vCenter or ESXi server.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_HOST</code> will be used instead.</div>
                                            <div>Environment variable support added in Ansible 2.6.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>is_template</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Flag the instance as a template.</div>
                                            <div>This will mark the given virtual machine as template.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>linked_clone</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to create a linked clone from the snapshot specified.</div>
                                            <div>If specified, then <code>snapshot_src</code> is required parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the virtual machine to work with.</div>
                                            <div>Virtual machine names in vCenter are not necessarily unique, which may be problematic, see <code>name_match</code>.</div>
                                            <div>If multiple virtual machines with same name exists, then <code>folder</code> is required parameter to identify uniqueness of the virtual machine.</div>
                                            <div>This parameter is required, if <code>state</code> is set to <code>poweredon</code>, <code>poweredoff</code>, <code>present</code>, <code>restarted</code>, <code>suspended</code> and virtual machine does not exists.</div>
                                            <div>This parameter is case sensitive.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name_match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>first</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>last</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>If multiple virtual machines matching the name, use the first or last found.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>networks</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of networks (in the order of the NICs).</div>
                                            <div>Removing NICs is not allowed, while reconfiguring the virtual machine.</div>
                                            <div>All parameters and VMware object names are case sensitive.</div>
                                            <div>One of the below parameters is required per entry:</div>
                                            <div>- <code>name</code> (string): Name of the portgroup or distributed virtual portgroup for this interface. When specifying distributed virtual portgroup make sure given <code>esxi_hostname</code> or <code>cluster</code> is associated with it.</div>
                                            <div>- <code>vlan</code> (integer): VLAN number for this interface.</div>
                                            <div>Optional parameters per entry (used for virtual hardware):</div>
                                            <div>- <code>device_type</code> (string): Virtual network device (one of <code>e1000</code>, <code>e1000e</code>, <code>pcnet32</code>, <code>vmxnet2</code>, <code>vmxnet3</code> (default), <code>sriov</code>).</div>
                                            <div>- <code>mac</code> (string): Customize MAC address.</div>
                                            <div>- <code>dvswitch_name</code> (string): Name of the distributed vSwitch.</div>
                                            <div>Optional parameters per entry (used for OS customization):</div>
                                            <div>- <code>type</code> (string): Type of IP assignment (either <code>dhcp</code> or <code>static</code>). <code>dhcp</code> is default.</div>
                                            <div>- <code>ip</code> (string): Static IP address (implies <code>type: static</code>).</div>
                                            <div>- <code>netmask</code> (string): Static netmask required for <code>ip</code>.</div>
                                            <div>- <code>gateway</code> (string): Static gateway.</div>
                                            <div>- <code>dns_servers</code> (string): DNS servers for this network interface (Windows).</div>
                                            <div>- <code>domain</code> (string): Domain name for this network interface (Windows).</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The password of the vSphere vCenter or ESXi server.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PASSWORD</code> will be used instead.</div>
                                            <div>Environment variable support added in Ansible 2.6.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: pass, pwd</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">443</div>
                                    </td>
                                                                <td>
                                            <div>The port number of the vSphere vCenter or ESXi server.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PORT</code> will be used instead.</div>
                                            <div>Environment variable support added in Ansible 2.6.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>proxy_host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Address of a proxy that will receive all HTTPS requests and relay them.</div>
                                            <div>The format is a hostname or a IP.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PROXY_HOST</code> will be used instead.</div>
                                            <div>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>proxy_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PROXY_PORT</code> will be used instead.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>resource_pool</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Use the given resource pool for virtual machine operation.</div>
                                            <div>This parameter is case sensitive.</div>
                                            <div>Resource pool should be child of the selected host parent.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>snapshot_src</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of the existing snapshot to use to create a clone of a virtual machine.</div>
                                            <div>This parameter is case sensitive.</div>
                                            <div>While creating linked clone using <code>linked_clone</code> parameter, this parameter is required.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                                                                                                                                <li>poweredon</li>
                                                                                                                                                                                                <li>poweredoff</li>
                                                                                                                                                                                                <li>restarted</li>
                                                                                                                                                                                                <li>suspended</li>
                                                                                                                                                                                                <li>shutdownguest</li>
                                                                                                                                                                                                <li>rebootguest</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Specify the state the virtual machine should be in.</div>
                                            <div>If <code>state</code> is set to <code>present</code> and virtual machine exists, ensure the virtual machine configurations conforms to task arguments.</div>
                                            <div>If <code>state</code> is set to <code>absent</code> and virtual machine exists, then the specified virtual machine is removed with its associated components.</div>
                                            <div>If <code>state</code> is set to one of the following <code>poweredon</code>, <code>poweredoff</code>, <code>present</code>, <code>restarted</code>, <code>suspended</code> and virtual machine does not exists, then virtual machine is deployed with given parameters.</div>
                                            <div>If <code>state</code> is set to <code>poweredon</code> and virtual machine exists with powerstate other than powered on, then the specified virtual machine is powered on.</div>
                                            <div>If <code>state</code> is set to <code>poweredoff</code> and virtual machine exists with powerstate other than powered off, then the specified virtual machine is powered off.</div>
                                            <div>If <code>state</code> is set to <code>restarted</code> and virtual machine exists, then the virtual machine is restarted.</div>
                                            <div>If <code>state</code> is set to <code>suspended</code> and virtual machine exists, then the virtual machine is set to suspended mode.</div>
                                            <div>If <code>state</code> is set to <code>shutdownguest</code> and virtual machine exists, then the virtual machine is shutdown.</div>
                                            <div>If <code>state</code> is set to <code>rebootguest</code> and virtual machine exists, then the virtual machine is rebooted.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state_change_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">0</div>
                                    </td>
                                                                <td>
                                            <div>If the <code>state</code> is set to <code>shutdownguest</code>, by default the module will return immediately after sending the shutdown signal.</div>
                                            <div>If this argument is set to a positive integer, the module will instead wait for the virtual machine to reach the poweredoff state.</div>
                                            <div>The value sets a timeout in seconds for the module to wait for the state change.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>template</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Template or existing virtual machine used to create new virtual machine.</div>
                                            <div>If this value is not set, virtual machine is created without using a template.</div>
                                            <div>If the virtual machine already exists, this parameter will be ignored.</div>
                                            <div>This parameter is case sensitive.</div>
                                            <div>From version 2.8 onwards, absolute path to virtual machine or template can be used.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: template_src</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>use_instance_uuid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Whether to use the VMware instance UUID rather than the BIOS UUID.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The username of the vSphere vCenter or ESXi server.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_USER</code> will be used instead.</div>
                                            <div>Environment variable support added in Ansible 2.6.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: admin, user</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>uuid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>UUID of the virtual machine to manage if known, this is VMware&#x27;s unique identifier.</div>
                                            <div>This is required if <code>name</code> is not supplied.</div>
                                            <div>If virtual machine does not exists, then this parameter is ignored.</div>
                                            <div>Please note that a supplied UUID will be ignored on virtual machine creation, as VMware creates the UUID internally.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                                                                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Allows connection when SSL certificates are not valid. Set to <code>false</code> when certificates are not trusted.</div>
                                            <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_VALIDATE_CERTS</code> will be used instead.</div>
                                            <div>Environment variable support added in Ansible 2.6.</div>
                                            <div>If set to <code>yes</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vapp_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>A list of vApp properties.</div>
                                            <div>For full list of attributes and types refer to:</div>
                                            <div><a href='https://vdc-download.vmware.com/vmwb-repository/dcr-public/6b586ed2-655c-49d9-9029-bc416323cb22/ fa0b429a-a695-4c11-b7d2-2cbc284049dc/doc/vim.vApp.PropertyInfo.html'>https://vdc-download.vmware.com/vmwb-repository/dcr-public/6b586ed2-655c-49d9-9029-bc416323cb22/ fa0b429a-a695-4c11-b7d2-2cbc284049dc/doc/vim.vApp.PropertyInfo.html</a></div>
                                            <div>Basic attributes are:</div>
                                            <div>- <code>id</code> (string): Property id - required.</div>
                                            <div>- <code>value</code> (string): Property value.</div>
                                            <div>- <code>type</code> (string): Value type, string type by default.</div>
                                            <div>- <code>operation</code>: <code>remove</code>: This attribute is required only when removing properties.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wait_for_customization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Wait until vCenter detects all guest customizations as successfully completed.</div>
                                            <div>When enabled, the VM will automatically be powered on.</div>
                                            <div>If vCenter does not detect guest customization start or succeed, failed events after time <code>wait_for_customization_timeout</code> parameter specified, warning message will be printed and task result is fail.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wait_for_customization_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"3600"</div>
                                    </td>
                                                                <td>
                                            <div>Define a timeout (in seconds) for the wait_for_customization parameter.</div>
                                            <div>Be careful when setting this value since the time guest customization took may differ among guest OSes.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wait_for_ip_address</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Wait until vCenter detects an IP address for the virtual machine.</div>
                                            <div>This requires vmware-tools (vmtoolsd) to properly work after creation.</div>
                                            <div>vmware-tools needs to be installed on the given virtual machine in order to work with this parameter.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>wait_for_ip_address_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">"300"</div>
                                    </td>
                                                                <td>
                                            <div>Define a timeout (in seconds) for the wait_for_ip_address parameter.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
   - Please make sure that the user used for :ref:`vmware_guest <vmware_guest_module>` has the correct level of privileges.
   - For example, following is the list of minimum privileges required by users to create virtual machines.
   -    DataStore > Allocate Space
   -    Virtual Machine > Configuration > Add New Disk
   -    Virtual Machine > Configuration > Add or Remove Device
   -    Virtual Machine > Inventory > Create New
   -    Network > Assign Network
   -    Resource > Assign Virtual Machine to Resource Pool
   - Module may require additional privileges as well, which may be required for gathering facts - e.g. ESXi configurations.
   - Tested on vSphere 5.5, 6.0, 6.5 and 6.7.
   - Use SCSI disks instead of IDE when you want to expand online disks by specifying a SCSI controller.
   - Uses SysPrep for Windows VM (depends on 'guest_id' parameter match 'win') with PyVmomi.
   - In order to change the VM's parameters (e.g. number of CPUs), the VM must be powered off unless the hot-add support is enabled and the ``state=present`` must be used to apply the changes.
   - For additional information please visit Ansible VMware community wiki - https://github.com/ansible/community/wiki/VMware.



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create a virtual machine on given ESXi hostname
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: no
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
        wait_for_ip_address: yes
        wait_for_ip_address_timeout: 600
      delegate_to: localhost
      register: deploy_vm

    - name: Create a virtual machine from a template
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: no
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
          memory_reservation_lock: True
          mem_limit: 8096
          mem_reservation: 4096
          cpu_limit: 8096
          cpu_reservation: 4096
          max_connections: 5
          hotadd_cpu: True
          hotremove_cpu: True
          hotadd_memory: False
          version: 12 # Hardware version of virtual machine
          boot_firmware: "efi"
        cdrom:
          type: iso
          iso_path: "[datastore1] livecd.iso"
        networks:
        - name: VM Network
          mac: aa:bb:dd:aa:00:14
        wait_for_ip_address: yes
      delegate_to: localhost
      register: deploy

    - name: Clone a virtual machine from Windows template and customize
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: no
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
          autologon: yes
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
        validate_certs: no
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
        wait_for_ip_address: True
        customization:
          domain: "{{ guest_domain }}"
          dns_servers:
            - 8.9.9.9
            - 7.8.8.9
          dns_suffix:
            - example.com
            - example2.com
      delegate_to: localhost

    - name: Rename a virtual machine (requires the virtual machine's uuid)
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: no
        uuid: "{{ vm_uuid }}"
        name: new_name
        state: present
      delegate_to: localhost

    - name: Remove a virtual machine by uuid
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: no
        uuid: "{{ vm_uuid }}"
        state: absent
      delegate_to: localhost

    - name: Remove a virtual machine from inventory
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: no
        name: vm_name
        delete_from_inventory: True
        state: absent
      delegate_to: localhost

    - name: Manipulate vApp properties
      community.vmware.vmware_guest:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: no
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
        validate_certs: no
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
        validate_certs: False
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
        validate_certs: no
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




Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>instance</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                                                        <div>metadata about the new virtual machine</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">None</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Loic Blot (@nerzhul) <loic.blot@unix-experience.fr>
- Philippe Dellaert (@pdellaert) <philippe@dellaert.org>
- Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
