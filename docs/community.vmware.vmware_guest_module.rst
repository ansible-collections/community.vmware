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
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>advanced_settings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.7.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Define a list of advanced settings to be added to the VMX config.</div>
                        <div>An advanced settings object takes two fields <code>key</code> and <code>value</code>.</div>
                        <div>Incorrect key and values will be ignored.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>annotation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A note or annotation to include in the virtual machine.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: notes</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cdrom</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">raw</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of CD-ROM configurations for the virtual machine. Added in version 2.9.</div>
                        <div>Providing CD-ROM configuration as dict is deprecated and will be removed VMware collection 4.0.0. Please use a list instead.</div>
                        <div>Parameters <code>controller_type</code>, <code>controller_number</code>, <code>unit_number</code>, <code>state</code> are added for a list of CD-ROMs configuration support.</div>
                        <div>For <code>ide</code> controller, hot-add or hot-remove CD-ROM is not supported.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>controller_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>For <code>ide</code> controller, valid value is 0 or 1.</div>
                        <div>For <code>sata</code> controller, valid value is 0 to 3.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>controller_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Valid options are <code>ide</code> and <code>sata</code>.</div>
                        <div>Default value is <code>ide</code>.</div>
                        <div>When set to <code>sata</code>, please make sure <code>unit_number</code> is correct and not used by SATA disks.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>iso_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The datastore path to the ISO file to use, in the form of <code>[datastore1] path/to/file.iso</code>.</div>
                        <div>Required if type is set <code>iso</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Valid value is <code>present</code> or <code>absent</code>.</div>
                        <div>Default is <code>present</code>.</div>
                        <div>If set to <code>absent</code>, then the specified CD-ROM will be removed.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The type of CD-ROM, valid options are <code>none</code>, <code>client</code> or <code>iso</code>.</div>
                        <div>With <code>none</code> the CD-ROM will be disconnected but present.</div>
                        <div>The default value is <code>client</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unit_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>For CD-ROM device attach to <code>ide</code> controller, valid value is 0 or 1.</div>
                        <div>For CD-ROM device attach to <code>sata</code> controller, valid value is 0 to 29.</div>
                        <div><code>controller_number</code> and <code>unit_number</code> are mandatory attributes.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cluster</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>convert</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>customization</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
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
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>autologon</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Auto logon after virtual machine customization.</div>
                        <div>Specific to Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>autologoncount</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of autologon after reboot.</div>
                        <div>Specific to Windows customization.</div>
                        <div>Ignored if <code>autologon</code> is unset or set to <code>False</code>.</div>
                        <div>If unset, 1 will be used.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dns_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of DNS servers to configure.</div>
                        <div>Common for Linux and Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dns_suffix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of domain suffixes, also known as DNS search path.</div>
                        <div>Default <code>domain</code> parameter.</div>
                        <div>Common for Linux and Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DNS domain name to use.</div>
                        <div>Common for Linux and Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domainadmin</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>User used to join in AD domain.</div>
                        <div>Required if <code>joindomain</code> specified.</div>
                        <div>Specific to Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domainadminpassword</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Password used to join in AD domain.</div>
                        <div>Required if <code>joindomain</code> specified.</div>
                        <div>Specific to Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>existing_vm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>True</code>, do OS customization on the specified virtual machine directly.</div>
                        <div>Common for Linux and Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fullname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Server owner name.</div>
                        <div>Specific to Windows customization.</div>
                        <div>If unset, &quot;Administrator&quot; will be used as a fall-back.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Computer hostname.</div>
                        <div>Default is shortened <code>name</code> parameter.</div>
                        <div>Allowed characters are alphanumeric (uppercase and lowercase) and minus, rest of the characters are dropped as per RFC 952.</div>
                        <div>Common for Linux and Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hwclockUTC</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies whether the hardware clock is in UTC or local time.</div>
                        <div>Specific to Linux customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>joindomain</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>AD domain to join.</div>
                        <div>Not compatible with <code>joinworkgroup</code>.</div>
                        <div>Specific to Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>joinworkgroup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Workgroup to join.</div>
                        <div>Not compatible with <code>joindomain</code>.</div>
                        <div>Specific to Windows customization.</div>
                        <div>If unset, &quot;WORKGROUP&quot; will be used as a fall-back.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>orgname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Organisation name.</div>
                        <div>Specific to Windows customization.</div>
                        <div>If unset, &quot;ACME&quot; will be used as a fall-back.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
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
                        <div>Local administrator password.</div>
                        <div>Specific to Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>productid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Product ID.</div>
                        <div>Specific to Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>runonce</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>List of commands to run at first user logon.</div>
                        <div>Specific to Windows customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timezone</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Timezone.</div>
                        <div>See List of supported time zones for different vSphere versions in Linux/Unix.</div>
                        <div>Common for Linux and Windows customization.</div>
                        <div><a href='https://msdn.microsoft.com/en-us/library/ms912391.aspx'>Windows</a>.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>customization_spec</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>customvalues</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datacenter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datastore</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify datastore or datastore cluster to provision virtual machine.</div>
                        <div>This parameter takes precedence over <code>disk.datastore</code> parameter.</div>
                        <div>This parameter can be used to override datastore or datastore cluster setting of the virtual machine when deployed from the template.</div>
                        <div>Please see example for more usage.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disk</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of disks to add.</div>
                        <div>This parameter is case sensitive.</div>
                        <div>Shrinking disks is not supported.</div>
                        <div>Removing existing disks of the virtual machine is not supported.</div>
                        <div>Attributes <code>controller_type</code>, <code>controller_number</code>, <code>unit_number</code> are used to configure multiple types of disk controllers and disks for creating or reconfiguring virtual machine. Added in Ansible 2.10.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>autoselect_datastore</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Select the less used datastore.</div>
                        <div><code>disk.datastore</code> and <code>disk.autoselect_datastore</code> will not be used if <code>datastore</code> is specified outside this <code>disk</code> configuration.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>controller_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>0</li>
                                    <li>1</li>
                                    <li>2</li>
                                    <li>3</li>
                        </ul>
                </td>
                <td>
                        <div>Disk controller bus number.</div>
                        <div>The maximum number of same type controller is 4 per VM.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>controller_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>buslogic</li>
                                    <li>lsilogic</li>
                                    <li>lsilogicsas</li>
                                    <li>paravirtual</li>
                                    <li>sata</li>
                                    <li>nvme</li>
                        </ul>
                </td>
                <td>
                        <div>Type of disk controller.</div>
                        <div><code>nvme</code> controller type support starts on ESXi 6.5 with VM hardware version <code>version</code> 13. Set this type on not supported ESXi or VM hardware version will lead to failure in deployment.</div>
                        <div>When set to <code>sata</code>, please make sure <code>unit_number</code> is correct and not used by SATA CDROMs.</div>
                        <div>If set to <code>sata</code> type, please make sure <code>controller_number</code> and <code>unit_number</code> are set correctly when <code>cdrom</code> also set to <code>sata</code> type.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datastore</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The name of datastore which will be used for the disk.</div>
                        <div>If <code>autoselect_datastore</code> is set to True, will select the less used datastore whose name contains this &quot;disk.datastore&quot; string.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disk_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>persistent</li>
                                    <li>independent_persistent</li>
                                    <li>independent_nonpersistent</li>
                        </ul>
                </td>
                <td>
                        <div>Type of disk mode.</div>
                        <div>Added in Ansible 2.6.</div>
                        <div>If <code>persistent</code> specified, changes are immediately and permanently written to the virtual disk. This is default.</div>
                        <div>If <code>independent_persistent</code> specified, same as persistent, but not affected by snapshots.</div>
                        <div>If <code>independent_nonpersistent</code> specified, changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>filename</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Existing disk image to be used.</div>
                        <div>Filename must already exist on the datastore.</div>
                        <div>Specify filename string in <code>[datastore_name] path/to/file.vmdk</code> format. Added in Ansible 2.8.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Disk storage size.</div>
                        <div>Please specify storage unit like [kb, mb, gb, tb].</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size_gb</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Disk storage size in gb.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size_kb</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Disk storage size in kb.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size_mb</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Disk storage size in mb.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size_tb</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Disk storage size in tb.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                        <div>Type of disk.</div>
                        <div>If <code>thin</code> specified, disk type is set to thin disk.</div>
                        <div>If <code>eagerzeroedthick</code> specified, disk type is set to eagerzeroedthick disk. Added Ansible 2.5.</div>
                        <div>If not specified, disk type is inherited from the source VM or template when cloned and thick disk, no eagerzero otherwise.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>unit_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Disk Unit Number.</div>
                        <div>Valid value range from 0 to 15 for SCSI controller, except 7.</div>
                        <div>Valid value range from 0 to 14 for NVME controller.</div>
                        <div>Valid value range from 0 to 29 for SATA controller.</div>
                        <div><code>controller_type</code>, <code>controller_number</code> and <code>unit_number</code> are required when creating or reconfiguring VMs with multiple types of disk controllers and disks.</div>
                        <div>When creating new VM, the first configured disk in the <code>disk</code> list will be &quot;Hard Disk 1&quot;.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esxi_hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>folder</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination folder, absolute path to find an existing guest or create the new guest.</div>
                        <div>The folder should include the datacenter. ESXi&#x27;s datacenter is ha-datacenter.</div>
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
                <td colspan="2">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>guest_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Set the guest ID.</div>
                        <div>This parameter is case sensitive.</div>
                        <div><code>rhel7_64Guest</code> for virtual machine with RHEL7 64 bit.</div>
                        <div><code>centos64Guest</code> for virtual machine with CentOS 64 bit.</div>
                        <div><code>ubuntu64Guest</code> for virtual machine with Ubuntu 64 bit.</div>
                        <div>This field is required when creating a virtual machine, not required when creating from the template.</div>
                        <div>Valid values are referenced here: <a href='https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html'>https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html</a></div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hardware</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Manage virtual machine&#x27;s hardware attributes.</div>
                        <div>All parameters case sensitive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>boot_firmware</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>bios</li>
                                    <li>efi</li>
                        </ul>
                </td>
                <td>
                        <div>Choose which firmware should be used to boot the virtual machine.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cpu_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The CPU utilization of a virtual machine will not exceed this limit.</div>
                        <div>Unit is MHz.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cpu_reservation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The amount of CPU resource that is guaranteed available to the virtual machine.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hotadd_cpu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Allow virtual CPUs to be added while the virtual machine is running.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hotadd_memory</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Allow memory to be added while the virtual machine is running.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hotremove_cpu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Allow virtual CPUs to be removed while the virtual machine is running.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>iommu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.11.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Flag to specify if I/O MMU is enabled for this virtual machine.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>max_connections</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Maximum number of active remote display connections for the virtual machines.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mem_limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The memory utilization of a virtual machine will not exceed this limit.</div>
                        <div>Unit is MB.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mem_reservation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The amount of memory resource that is guaranteed available to the virtual machine.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: memory_reservation</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>memory_mb</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Amount of memory in MB.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>memory_reservation_lock</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set <code>true</code>, memory resource reservation for the virtual machine.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nested_virt</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable nested virtualization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>num_cpu_cores_per_socket</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of Cores Per Socket.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>num_cpus</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of CPUs.</div>
                        <div><code>num_cpus</code> must be a multiple of <code>num_cpu_cores_per_socket</code>.</div>
                        <div>For example, to create a VM with 2 sockets of 4 cores, specify <code>num_cpus</code> as 8 and <code>num_cpu_cores_per_socket</code> as 4.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>scsi</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>buslogic</li>
                                    <li>lsilogic</li>
                                    <li>lsilogicsas</li>
                                    <li>paravirtual</li>
                        </ul>
                </td>
                <td>
                        <div>Valid values are <code>buslogic</code>, <code>lsilogic</code>, <code>lsilogicsas</code> and <code>paravirtual</code>.</div>
                        <div><code>paravirtual</code> is default.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>secure_boot</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.11.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Whether to enable or disable (U)EFI secure boot.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The Virtual machine hardware versions.</div>
                        <div>Default is 10 (ESXi 5.5 and onwards).</div>
                        <div>If set to <code>latest</code>, the specified virtual machine will be upgraded to the most current hardware version supported on the host.</div>
                        <div><code>latest</code> is added in Ansible 2.10.</div>
                        <div>Please check VMware documentation for correct virtual machine hardware version.</div>
                        <div>Incorrect hardware version may lead to failure in deployment. If hardware version is already equal to the given.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>virt_based_security</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Enable Virtualization Based Security feature for Windows on ESXi 6.7 and later, from hardware version 14.</div>
                        <div>Supported Guest OS are Windows 10 64 bit, Windows Server 2016, Windows Server 2019 and later.</div>
                        <div>The firmware of virtual machine must be EFI and secure boot must be enabled.</div>
                        <div>Virtualization Based Security depends on nested virtualization and Intel Virtualization Technology for Directed I/O.</div>
                        <div>Deploy on unsupported ESXi, hardware version or firmware may lead to failure or deployed VM with unexpected configurations.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                <td colspan="2">
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
                        <div>Note, this may need to be done in a dedicated task invocation that is not making any other changes. For example, user cannot change the state from powered-on to powered-off AND save as template in the same task.</div>
                        <div>See <span class='module'>community.vmware.vmware_guest</span> source for more details.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the virtual machine to work with.</div>
                        <div>Virtual machine names in vCenter are not necessarily unique, which may be problematic, see <code>name_match</code>.</div>
                        <div>If multiple virtual machines with same name exists, then <code>folder</code> is required parameter to identify uniqueness of the virtual machine.</div>
                        <div>This parameter is required, if <code>state</code> is set to <code>poweredon</code>, <code>powered-on</code>, <code>poweredoff</code>, <code>powered-off</code>, <code>present</code>, <code>restarted</code>, <code>suspended</code> and virtual machine does not exists.</div>
                        <div>This parameter is case sensitive.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name_match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>networks</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of networks (in the order of the NICs).</div>
                        <div>Removing NICs is not allowed, while reconfiguring the virtual machine.</div>
                        <div>All parameters and VMware object names are case sensitive.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>connected</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.5.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Indicates whether the NIC is currently connected.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>device_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Virtual network device.</div>
                        <div>Valid value can be one of <code>e1000</code>, <code>e1000e</code>, <code>pcnet32</code>, <code>vmxnet2</code>, <code>vmxnet3</code>, <code>sriov</code>.</div>
                        <div><code>vmxnet3</code> is default.</div>
                        <div>Optional per entry.</div>
                        <div>Used for virtual hardware.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dns_servers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>DNS servers for this network interface (Windows).</div>
                        <div>Optional per entry.</div>
                        <div>Used for OS customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>domain</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Domain name for this network interface (Windows).</div>
                        <div>Optional per entry.</div>
                        <div>Used for OS customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dvswitch_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the distributed vSwitch.</div>
                        <div>Optional per entry.</div>
                        <div>Used for virtual hardware.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>gateway</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Static gateway.</div>
                        <div>Optional per entry.</div>
                        <div>Used for OS customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ip</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Static IP address. Implies <code>type=static</code>.</div>
                        <div>Optional per entry.</div>
                        <div>Used for OS customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mac</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Customize MAC address.</div>
                        <div>Optional per entry.</div>
                        <div>Used for virtual hardware.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the portgroup or distributed virtual portgroup for this interface.</div>
                        <div>Required per entry.</div>
                        <div>When specifying distributed virtual portgroup make sure given <code>esxi_hostname</code> or <code>cluster</code> is associated with it.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>netmask</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Static netmask required for <code>ip</code>.</div>
                        <div>Optional per entry.</div>
                        <div>Used for OS customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>start_connected</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies whether or not to connect the device when the virtual machine starts.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Type of IP assignment.</div>
                        <div>Valid values are one of <code>dhcp</code>, <code>static</code>.</div>
                        <div><code>dhcp</code> is default.</div>
                        <div>Optional per entry.</div>
                        <div>Used for OS customization.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>VLAN number for this interface.</div>
                        <div>Required per entry.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>nvdimm</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.13.0</div>
                </td>
                <td>
                </td>
                <td>
                        <div>Add or remove a virtual NVDIMM device to the virtual machine.</div>
                        <div>VM virtual hardware version must be 14 or higher on vSphere 6.7 or later.</div>
                        <div>Verify that guest OS of the virtual machine supports PMem before adding virtual NVDIMM device.</div>
                        <div>Verify that you have the <em>Datastore.Allocate</em> space privilege on the virtual machine.</div>
                        <div>Make sure that the host or the cluster on which the virtual machine resides has available PMem resources.</div>
                        <div>To add or remove virtual NVDIMM device to the existing virtual machine, it must be in power off state.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>label</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The label of the virtual NVDIMM device to be removed or configured, e.g., &quot;NVDIMM 1&quot;.</div>
                        <div>This parameter is required when <code>state</code> is set to <code>absent</code>, or <code>present</code> to reconfigure NVDIMM device size. When add a new device, please do not set <code>label</code>.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>size_mb</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">1024</div>
                </td>
                <td>
                        <div>Virtual NVDIMM device size in MB.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>present</li>
                                    <li>absent</li>
                        </ul>
                </td>
                <td>
                        <div>Valid value is <code>present</code> or <code>absent</code>.</div>
                        <div>If set to <code>absent</code>, then the NVDIMM device with specified <code>label</code> will be removed.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>resource_pool</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Use the given resource pool for virtual machine operation.</div>
                        <div>This parameter is case sensitive.</div>
                        <div>Resource pool should be child of the selected host parent.</div>
                        <div>When not specified <em>Resources</em> is taken as default value.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>snapshot_src</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>absent</li>
                                    <li>poweredon</li>
                                    <li>powered-on</li>
                                    <li>poweredoff</li>
                                    <li>powered-off</li>
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                    <li>rebootguest</li>
                                    <li>reboot-guest</li>
                                    <li>restarted</li>
                                    <li>suspended</li>
                                    <li>shutdownguest</li>
                                    <li>shutdown-guest</li>
                        </ul>
                </td>
                <td>
                        <div>Specify the state the virtual machine should be in.</div>
                        <div>If <code>state</code> is set to <code>present</code> and virtual machine exists, ensure the virtual machine configurations conforms to task arguments.</div>
                        <div>If <code>state</code> is set to <code>absent</code> and virtual machine exists, then the specified virtual machine is removed with it&#x27;s associated components.</div>
                        <div>If <code>state</code> is set to one of the following <code>poweredon</code>, <code>powered-on</code>, <code>poweredoff</code>, <code>powered-off</code>, <code>present</code>, <code>restarted</code>, <code>suspended</code> and virtual machine does not exists, virtual machine is deployed with the given parameters.</div>
                        <div>If <code>state</code> is set to <code>poweredon</code> or <code>powered-on</code> and virtual machine exists with powerstate other than powered on, then the specified virtual machine is powered on.</div>
                        <div>If <code>state</code> is set to <code>poweredoff</code> or <code>powered-off</code> and virtual machine exists with powerstate other than powered off, then the specified virtual machine is powered off.</div>
                        <div>If <code>state</code> is set to <code>restarted</code> and virtual machine exists, then the virtual machine is restarted.</div>
                        <div>If <code>state</code> is set to <code>suspended</code> and virtual machine exists, then the virtual machine is set to suspended mode.</div>
                        <div>If <code>state</code> is set to <code>shutdownguest</code> or <code>shutdown-guest</code> and virtual machine exists, then the virtual machine is shutdown.</div>
                        <div>If <code>state</code> is set to <code>rebootguest</code> or <code>reboot-guest</code> and virtual machine exists, then the virtual machine is rebooted.</div>
                        <div>Powerstate <code>powered-on</code> and <code>powered-off</code> is added in version 2.10.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state_change_timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>template</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>uuid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
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
                <td colspan="2">
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
                        <div>If set to <code>true</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vapp_properties</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>A list of vApp properties.</div>
                        <div>For full list of attributes and types refer to: <a href='https://code.vmware.com/apis/704/vsphere/vim.vApp.PropertyInfo.html'>https://code.vmware.com/apis/704/vsphere/vim.vApp.PropertyInfo.html</a></div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Property ID.</div>
                        <div>Required per entry.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>operation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The <code>remove</code> attribute is required only when removing properties.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Value type, string type by default.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Property value.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
   - Please make sure that the user used for :ref:`community.vmware.vmware_guest <community.vmware.vmware_guest_module>` has the correct level of privileges.
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
        delete_from_inventory: True
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
