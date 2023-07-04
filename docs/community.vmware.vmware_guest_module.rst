

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

.. raw:: html

  <table style="width: 100%; height: 1px;">
  <thead>
  <tr>
    <th><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-advanced_settings"></div>
      <p style="display: inline;"><strong>advanced_settings</strong></p>
      <a class="ansibleOptionLink" href="#parameter-advanced_settings" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Define a list of advanced settings to be added to the VMX config.</p>
      <p>An advanced settings object takes two fields <code class='docutils literal notranslate'>key</code> and <code class='docutils literal notranslate'>value</code>.</p>
      <p>Incorrect key and values will be ignored.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-annotation"></div>
      <div class="ansibleOptionAnchor" id="parameter-notes"></div>
      <p style="display: inline;"><strong>annotation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-annotation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: notes</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>A note or annotation to include in the virtual machine.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cdrom"></div>
      <p style="display: inline;"><strong>cdrom</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cdrom" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">any</span>
      </p>
    </div></td>
    <td>
      <p>A list of CD-ROM configurations for the virtual machine. Added in version 2.9.</p>
      <p>Providing CD-ROM configuration as dict is deprecated and will be removed VMware collection 4.0.0. Please use a list instead.</p>
      <p>Parameters <code class='docutils literal notranslate'>controller_type</code>, <code class='docutils literal notranslate'>controller_number</code>, <code class='docutils literal notranslate'>unit_number</code>, <code class='docutils literal notranslate'>state</code> are added for a list of CD-ROMs configuration support.</p>
      <p>For <code class='docutils literal notranslate'>ide</code> controller, hot-add or hot-remove CD-ROM is not supported.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cdrom/controller_number"></div>
      <p style="display: inline;"><strong>controller_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cdrom/controller_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>For <code class='docutils literal notranslate'>ide</code> controller, valid value is 0 or 1.</p>
      <p>For <code class='docutils literal notranslate'>sata</code> controller, valid value is 0 to 3.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cdrom/controller_type"></div>
      <p style="display: inline;"><strong>controller_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cdrom/controller_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Valid options are <code class='docutils literal notranslate'>ide</code> and <code class='docutils literal notranslate'>sata</code>.</p>
      <p>Default value is <code class='docutils literal notranslate'>ide</code>.</p>
      <p>When set to <code class='docutils literal notranslate'>sata</code>, please make sure <code class='docutils literal notranslate'>unit_number</code> is correct and not used by SATA disks.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cdrom/iso_path"></div>
      <p style="display: inline;"><strong>iso_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cdrom/iso_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The datastore path to the ISO file to use, in the form of <code class='docutils literal notranslate'>[datastore1] path/to/file.iso</code>.</p>
      <p>Required if type is set <code class='docutils literal notranslate'>iso</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cdrom/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cdrom/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Valid value is <code class='docutils literal notranslate'>present</code> or <code class='docutils literal notranslate'>absent</code>.</p>
      <p>Default is <code class='docutils literal notranslate'>present</code>.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code>, then the specified CD-ROM will be removed.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cdrom/type"></div>
      <p style="display: inline;"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cdrom/type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The type of CD-ROM, valid options are <code class='docutils literal notranslate'>none</code>, <code class='docutils literal notranslate'>client</code> or <code class='docutils literal notranslate'>iso</code>.</p>
      <p>With <code class='docutils literal notranslate'>none</code> the CD-ROM will be disconnected but present.</p>
      <p>The default value is <code class='docutils literal notranslate'>client</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cdrom/unit_number"></div>
      <p style="display: inline;"><strong>unit_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cdrom/unit_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>For CD-ROM device attach to <code class='docutils literal notranslate'>ide</code> controller, valid value is 0 or 1.</p>
      <p>For CD-ROM device attach to <code class='docutils literal notranslate'>sata</code> controller, valid value is 0 to 29.</p>
      <p><code class='docutils literal notranslate'>controller_number</code> and <code class='docutils literal notranslate'>unit_number</code> are mandatory attributes.</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cluster"></div>
      <p style="display: inline;"><strong>cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The cluster name where the virtual machine will run.</p>
      <p>This is a required parameter, if <code class='docutils literal notranslate'>esxi_hostname</code> is not set.</p>
      <p><code class='docutils literal notranslate'>esxi_hostname</code> and <code class='docutils literal notranslate'>cluster</code> are mutually exclusive parameters.</p>
      <p>This parameter is case sensitive.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-convert"></div>
      <p style="display: inline;"><strong>convert</strong></p>
      <a class="ansibleOptionLink" href="#parameter-convert" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Specify convert disk type while cloning template or virtual machine.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;thin&#34;</code></p></li>
        <li><p><code>&#34;thick&#34;</code></p></li>
        <li><p><code>&#34;eagerzeroedthick&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization"></div>
      <p style="display: inline;"><strong>customization</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Parameters for OS customization when cloning from the template or the virtual machine, or apply to the existing virtual machine directly.</p>
      <p>Not all operating systems are supported for customization with respective vCenter version, please check VMware documentation for respective OS customization.</p>
      <p>For supported customization operating system matrix, (see <a href='http://partnerweb.vmware.com/programs/guestOS/guest-os-customization-matrix.pdf'>http://partnerweb.vmware.com/programs/guestOS/guest-os-customization-matrix.pdf</a>)</p>
      <p>All parameters and VMware object names are case sensitive.</p>
      <p>Linux based OSes requires Perl package to be installed for OS customizations.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/autologon"></div>
      <p style="display: inline;"><strong>autologon</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/autologon" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Auto logon after virtual machine customization.</p>
      <p>Specific to Windows customization.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/autologoncount"></div>
      <p style="display: inline;"><strong>autologoncount</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/autologoncount" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Number of autologon after reboot.</p>
      <p>Specific to Windows customization.</p>
      <p>Ignored if <code class='docutils literal notranslate'>autologon</code> is unset or set to <code class='docutils literal notranslate'>false</code>.</p>
      <p>If unset, 1 will be used.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/dns_servers"></div>
      <p style="display: inline;"><strong>dns_servers</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/dns_servers" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </div></td>
    <td>
      <p>List of DNS servers to configure.</p>
      <p>Common for Linux and Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/dns_suffix"></div>
      <p style="display: inline;"><strong>dns_suffix</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/dns_suffix" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </div></td>
    <td>
      <p>List of domain suffixes, also known as DNS search path.</p>
      <p>Default <code class='docutils literal notranslate'>domain</code> parameter.</p>
      <p>Common for Linux and Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/domain"></div>
      <p style="display: inline;"><strong>domain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/domain" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>DNS domain name to use.</p>
      <p>Common for Linux and Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/domainadmin"></div>
      <p style="display: inline;"><strong>domainadmin</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/domainadmin" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>User used to join in AD domain.</p>
      <p>Required if <code class='docutils literal notranslate'>joindomain</code> specified.</p>
      <p>Specific to Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/domainadminpassword"></div>
      <p style="display: inline;"><strong>domainadminpassword</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/domainadminpassword" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Password used to join in AD domain.</p>
      <p>Required if <code class='docutils literal notranslate'>joindomain</code> specified.</p>
      <p>Specific to Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/existing_vm"></div>
      <p style="display: inline;"><strong>existing_vm</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/existing_vm" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>If set to <code class='docutils literal notranslate'>true</code>, do OS customization on the specified virtual machine directly.</p>
      <p>Common for Linux and Windows customization.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/fullname"></div>
      <p style="display: inline;"><strong>fullname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/fullname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Server owner name.</p>
      <p>Specific to Windows customization.</p>
      <p>If unset, "Administrator" will be used as a fall-back.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Computer hostname.</p>
      <p>Default is shortened <code class='docutils literal notranslate'>name</code> parameter.</p>
      <p>Allowed characters are alphanumeric (uppercase and lowercase) and minus, rest of the characters are dropped as per RFC 952.</p>
      <p>Common for Linux and Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/hwclockUTC"></div>
      <p style="display: inline;"><strong>hwclockUTC</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/hwclockUTC" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Specifies whether the hardware clock is in UTC or local time.</p>
      <p>Specific to Linux customization.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/joindomain"></div>
      <p style="display: inline;"><strong>joindomain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/joindomain" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>AD domain to join.</p>
      <p>Not compatible with <code class='docutils literal notranslate'>joinworkgroup</code>.</p>
      <p>Specific to Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/joinworkgroup"></div>
      <p style="display: inline;"><strong>joinworkgroup</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/joinworkgroup" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Workgroup to join.</p>
      <p>Not compatible with <code class='docutils literal notranslate'>joindomain</code>.</p>
      <p>Specific to Windows customization.</p>
      <p>If unset, "WORKGROUP" will be used as a fall-back.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/orgname"></div>
      <p style="display: inline;"><strong>orgname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/orgname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Organisation name.</p>
      <p>Specific to Windows customization.</p>
      <p>If unset, "ACME" will be used as a fall-back.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/password"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Local administrator password.</p>
      <p>If not defined, the password will be set to blank (that is, no password).</p>
      <p>Specific to Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/productid"></div>
      <p style="display: inline;"><strong>productid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/productid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Product ID.</p>
      <p>Specific to Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/runonce"></div>
      <p style="display: inline;"><strong>runonce</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/runonce" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </div></td>
    <td>
      <p>List of commands to run at first user logon.</p>
      <p>Specific to Windows customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/script_text"></div>
      <p style="display: inline;"><strong>script_text</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/script_text" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 3.1.0</span></p>
    </div></td>
    <td>
      <p>Script to run with shebang.</p>
      <p>Needs to be enabled in vmware tools with vmware-toolbox-cmd config set deployPkg enable-custom-scripts true</p>
      <p>https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-9A5093A5-C54F-4502-941B-3F9C0F573A39.html</p>
      <p>Specific to Linux customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization/timezone"></div>
      <p style="display: inline;"><strong>timezone</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization/timezone" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Timezone.</p>
      <p>See List of supported time zones for different vSphere versions in Linux/Unix.</p>
      <p>Common for Linux and Windows customization.</p>
      <p><a href='https://msdn.microsoft.com/en-us/library/ms912391.aspx'>Windows</a>.</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customization_spec"></div>
      <p style="display: inline;"><strong>customization_spec</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customization_spec" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Unique name identifying the requested customization specification.</p>
      <p>This parameter is case sensitive.</p>
      <p>If set, then overrides <code class='docutils literal notranslate'>customization</code> parameter values.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-customvalues"></div>
      <p style="display: inline;"><strong>customvalues</strong></p>
      <a class="ansibleOptionLink" href="#parameter-customvalues" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Define a list of custom values to set on virtual machine.</p>
      <p>A custom value object takes two fields <code class='docutils literal notranslate'>key</code> and <code class='docutils literal notranslate'>value</code>.</p>
      <p>Incorrect key and values will be ignored.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Destination datacenter for the deploy operation.</p>
      <p>This parameter is case sensitive.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;ha-datacenter&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-datastore"></div>
      <p style="display: inline;"><strong>datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Specify datastore or datastore cluster to provision virtual machine.</p>
      <p>This parameter takes precedence over <code class='docutils literal notranslate'>disk.datastore</code> parameter.</p>
      <p>This parameter can be used to override datastore or datastore cluster setting of the virtual machine when deployed from the template.</p>
      <p>Please see example for more usage.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-delete_from_inventory"></div>
      <p style="display: inline;"><strong>delete_from_inventory</strong></p>
      <a class="ansibleOptionLink" href="#parameter-delete_from_inventory" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Whether to delete Virtual machine from inventory or delete from disk.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk"></div>
      <p style="display: inline;"><strong>disk</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </div></td>
    <td>
      <p>A list of disks to add.</p>
      <p>This parameter is case sensitive.</p>
      <p>Shrinking disks is not supported.</p>
      <p>Removing existing disks of the virtual machine is not supported.</p>
      <p>Attributes <code class='docutils literal notranslate'>controller_type</code>, <code class='docutils literal notranslate'>controller_number</code>, <code class='docutils literal notranslate'>unit_number</code> are used to configure multiple types of disk controllers and disks for creating or reconfiguring virtual machine. Added in Ansible 2.10.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/autoselect_datastore"></div>
      <p style="display: inline;"><strong>autoselect_datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/autoselect_datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Select the less used datastore.</p>
      <p><code class='docutils literal notranslate'>disk.datastore</code> and <code class='docutils literal notranslate'>disk.autoselect_datastore</code> will not be used if <code class='docutils literal notranslate'>datastore</code> is specified outside this <code class='docutils literal notranslate'>disk</code> configuration.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/controller_number"></div>
      <p style="display: inline;"><strong>controller_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/controller_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Disk controller bus number.</p>
      <p>The maximum number of same type controller is 4 per VM.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>0</code></p></li>
        <li><p><code>1</code></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/controller_type"></div>
      <p style="display: inline;"><strong>controller_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/controller_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Type of disk controller.</p>
      <p><code class='docutils literal notranslate'>nvme</code> controller type support starts on ESXi 6.5 with VM hardware version <code class='docutils literal notranslate'>version</code> 13. Set this type on not supported ESXi or VM hardware version will lead to failure in deployment.</p>
      <p>When set to <code class='docutils literal notranslate'>sata</code>, please make sure <code class='docutils literal notranslate'>unit_number</code> is correct and not used by SATA CDROMs.</p>
      <p>If set to <code class='docutils literal notranslate'>sata</code> type, please make sure <code class='docutils literal notranslate'>controller_number</code> and <code class='docutils literal notranslate'>unit_number</code> are set correctly when <code class='docutils literal notranslate'>cdrom</code> also set to <code class='docutils literal notranslate'>sata</code> type.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;buslogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogicsas&#34;</code></p></li>
        <li><p><code>&#34;paravirtual&#34;</code></p></li>
        <li><p><code>&#34;sata&#34;</code></p></li>
        <li><p><code>&#34;nvme&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/datastore"></div>
      <p style="display: inline;"><strong>datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The name of datastore which will be used for the disk.</p>
      <p>If <code class='docutils literal notranslate'>autoselect_datastore</code> is set to True, will select the less used datastore whose name contains this "disk.datastore" string.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/disk_mode"></div>
      <p style="display: inline;"><strong>disk_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/disk_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Type of disk mode.</p>
      <p>Added in Ansible 2.6.</p>
      <p>If <code class='docutils literal notranslate'>persistent</code> specified, changes are immediately and permanently written to the virtual disk. This is default.</p>
      <p>If <code class='docutils literal notranslate'>independent_persistent</code> specified, same as persistent, but not affected by snapshots.</p>
      <p>If <code class='docutils literal notranslate'>independent_nonpersistent</code> specified, changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;persistent&#34;</code></p></li>
        <li><p><code>&#34;independent_persistent&#34;</code></p></li>
        <li><p><code>&#34;independent_nonpersistent&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/filename"></div>
      <p style="display: inline;"><strong>filename</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/filename" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Existing disk image to be used.</p>
      <p>Filename must already exist on the datastore.</p>
      <p>Specify filename string in <code class='docutils literal notranslate'>[datastore_name] path/to/file.vmdk</code> format. Added in Ansible 2.8.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/size"></div>
      <p style="display: inline;"><strong>size</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/size" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Disk storage size.</p>
      <p>Please specify storage unit like [kb, mb, gb, tb].</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/size_gb"></div>
      <p style="display: inline;"><strong>size_gb</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/size_gb" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Disk storage size in gb.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/size_kb"></div>
      <p style="display: inline;"><strong>size_kb</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/size_kb" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Disk storage size in kb.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/size_mb"></div>
      <p style="display: inline;"><strong>size_mb</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/size_mb" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Disk storage size in mb.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/size_tb"></div>
      <p style="display: inline;"><strong>size_tb</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/size_tb" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Disk storage size in tb.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/type"></div>
      <p style="display: inline;"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Type of disk.</p>
      <p>If <code class='docutils literal notranslate'>thin</code> specified, disk type is set to thin disk.</p>
      <p>If <code class='docutils literal notranslate'>eagerzeroedthick</code> specified, disk type is set to eagerzeroedthick disk. Added Ansible 2.5.</p>
      <p>If not specified, disk type is inherited from the source VM or template when cloned and thick disk, no eagerzero otherwise.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;thin&#34;</code></p></li>
        <li><p><code>&#34;thick&#34;</code></p></li>
        <li><p><code>&#34;eagerzeroedthick&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/unit_number"></div>
      <p style="display: inline;"><strong>unit_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/unit_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Disk Unit Number.</p>
      <p>Valid value range from 0 to 15 for SCSI controller, except 7.</p>
      <p>Valid value range from 0 to 14 for NVME controller.</p>
      <p>Valid value range from 0 to 29 for SATA controller.</p>
      <p><code class='docutils literal notranslate'>controller_type</code>, <code class='docutils literal notranslate'>controller_number</code> and <code class='docutils literal notranslate'>unit_number</code> are required when creating or reconfiguring VMs with multiple types of disk controllers and disks.</p>
      <p>When creating new VM, the first configured disk in the <code class='docutils literal notranslate'>disk</code> list will be "Hard Disk 1".</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The ESXi hostname where the virtual machine will run.</p>
      <p>This is a required parameter, if <code class='docutils literal notranslate'>cluster</code> is not set.</p>
      <p><code class='docutils literal notranslate'>esxi_hostname</code> and <code class='docutils literal notranslate'>cluster</code> are mutually exclusive parameters.</p>
      <p>This parameter is case sensitive.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Destination folder, absolute path to find an existing guest or create the new guest.</p>
      <p>The folder should include the datacenter. ESXi&#x27;s datacenter is ha-datacenter.</p>
      <p>This parameter is case sensitive.</p>
      <p>If multiple machines are found with same name, this parameter is used to identify</p>
      <p>uniqueness of the virtual machine. Added in Ansible 2.5.</p>
      <p>Examples:</p>
      <p>   folder: /ha-datacenter/vm</p>
      <p>   folder: ha-datacenter/vm</p>
      <p>   folder: /datacenter1/vm</p>
      <p>   folder: datacenter1/vm</p>
      <p>   folder: /datacenter1/vm/folder1</p>
      <p>   folder: datacenter1/vm/folder1</p>
      <p>   folder: /folder1/datacenter1/vm</p>
      <p>   folder: folder1/datacenter1/vm</p>
      <p>   folder: /folder1/datacenter1/vm/folder2</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-force"></div>
      <p style="display: inline;"><strong>force</strong></p>
      <a class="ansibleOptionLink" href="#parameter-force" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Ignore warnings and complete the actions.</p>
      <p>This parameter is useful while removing virtual machine which is powered on state.</p>
      <p>This module reflects the VMware vCenter API and UI workflow, as such, in some cases the `force` flag will be mandatory to perform the action to ensure you are certain the action has to be taken, no matter what the consequence. This is specifically the case for removing a powered on the virtual machine when <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>absent</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-guest_id"></div>
      <p style="display: inline;"><strong>guest_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-guest_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Set the guest ID.</p>
      <p>This parameter is case sensitive.</p>
      <p><code class='docutils literal notranslate'>rhel7_64Guest</code> for virtual machine with RHEL7 64 bit.</p>
      <p><code class='docutils literal notranslate'>centos64Guest</code> for virtual machine with CentOS 64 bit.</p>
      <p><code class='docutils literal notranslate'>ubuntu64Guest</code> for virtual machine with Ubuntu 64 bit.</p>
      <p>This field is required when creating a virtual machine, not required when creating from the template.</p>
      <p>Valid values are referenced here: <a href='https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html'>https://code.vmware.com/apis/358/doc/vim.vm.GuestOsDescriptor.GuestOsIdentifier.html</a>
      </p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware"></div>
      <p style="display: inline;"><strong>hardware</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Manage virtual machine&#x27;s hardware attributes.</p>
      <p>All parameters case sensitive.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/boot_firmware"></div>
      <p style="display: inline;"><strong>boot_firmware</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/boot_firmware" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Choose which firmware should be used to boot the virtual machine.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;bios&#34;</code></p></li>
        <li><p><code>&#34;efi&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/cpu_limit"></div>
      <p style="display: inline;"><strong>cpu_limit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/cpu_limit" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The CPU utilization of a virtual machine will not exceed this limit.</p>
      <p>Unit is MHz.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/cpu_reservation"></div>
      <p style="display: inline;"><strong>cpu_reservation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/cpu_reservation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The amount of CPU resource that is guaranteed available to the virtual machine.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/cpu_shares"></div>
      <p style="display: inline;"><strong>cpu_shares</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/cpu_shares" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 3.2.0</span></p>
    </div></td>
    <td>
      <p>The number of shares of CPU allocated to this virtual machine</p>
      <p>cpu_shares_level will automatically be set to &#x27;custom&#x27;</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/cpu_shares_level"></div>
      <p style="display: inline;"><strong>cpu_shares_level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/cpu_shares_level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 3.2.0</span></p>
    </div></td>
    <td>
      <p>The allocation level of CPU resources for the virtual machine.</p>
      <p>Valid Values are <code class='docutils literal notranslate'>low</code>, <code class='docutils literal notranslate'>normal</code>, <code class='docutils literal notranslate'>high</code> and <code class='docutils literal notranslate'>custom</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;low&#34;</code></p></li>
        <li><p><code>&#34;normal&#34;</code></p></li>
        <li><p><code>&#34;high&#34;</code></p></li>
        <li><p><code>&#34;custom&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/hotadd_cpu"></div>
      <p style="display: inline;"><strong>hotadd_cpu</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/hotadd_cpu" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Allow virtual CPUs to be added while the virtual machine is running.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/hotadd_memory"></div>
      <p style="display: inline;"><strong>hotadd_memory</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/hotadd_memory" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Allow memory to be added while the virtual machine is running.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/hotremove_cpu"></div>
      <p style="display: inline;"><strong>hotremove_cpu</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/hotremove_cpu" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Allow virtual CPUs to be removed while the virtual machine is running.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/iommu"></div>
      <p style="display: inline;"><strong>iommu</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/iommu" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Flag to specify if I/O MMU is enabled for this virtual machine.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/max_connections"></div>
      <p style="display: inline;"><strong>max_connections</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/max_connections" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Maximum number of active remote display connections for the virtual machines.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/mem_limit"></div>
      <p style="display: inline;"><strong>mem_limit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/mem_limit" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The memory utilization of a virtual machine will not exceed this limit.</p>
      <p>Unit is MB.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/mem_reservation"></div>
      <div class="ansibleOptionAnchor" id="parameter-hardware/memory_reservation"></div>
      <p style="display: inline;"><strong>mem_reservation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/mem_reservation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: memory_reservation</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The amount of memory resource that is guaranteed available to the virtual machine.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/mem_shares"></div>
      <p style="display: inline;"><strong>mem_shares</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/mem_shares" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 3.2.0</span></p>
    </div></td>
    <td>
      <p>The number of shares of memory allocated to this virtual machine</p>
      <p>mem_shares_level will automatically be set to &#x27;custom&#x27;</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/mem_shares_level"></div>
      <p style="display: inline;"><strong>mem_shares_level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/mem_shares_level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 3.2.0</span></p>
    </div></td>
    <td>
      <p>The allocation level of memory resources for the virtual machine.</p>
      <p>Valid Values are <code class='docutils literal notranslate'>low</code>, <code class='docutils literal notranslate'>normal</code>, <code class='docutils literal notranslate'>high</code> and <code class='docutils literal notranslate'>custom</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;low&#34;</code></p></li>
        <li><p><code>&#34;normal&#34;</code></p></li>
        <li><p><code>&#34;high&#34;</code></p></li>
        <li><p><code>&#34;custom&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/memory_mb"></div>
      <p style="display: inline;"><strong>memory_mb</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/memory_mb" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Amount of memory in MB.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/memory_reservation_lock"></div>
      <p style="display: inline;"><strong>memory_reservation_lock</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/memory_reservation_lock" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>If set <code class='docutils literal notranslate'>true</code>, memory resource reservation for the virtual machine.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/nested_virt"></div>
      <p style="display: inline;"><strong>nested_virt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/nested_virt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Enable nested virtualization.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/num_cpu_cores_per_socket"></div>
      <p style="display: inline;"><strong>num_cpu_cores_per_socket</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/num_cpu_cores_per_socket" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Number of Cores Per Socket.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/num_cpus"></div>
      <p style="display: inline;"><strong>num_cpus</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/num_cpus" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Number of CPUs.</p>
      <p><code class='docutils literal notranslate'>num_cpus</code> must be a multiple of <code class='docutils literal notranslate'>num_cpu_cores_per_socket</code>.</p>
      <p>For example, to create a VM with 2 sockets of 4 cores, specify <code class='docutils literal notranslate'>num_cpus</code> as 8 and <code class='docutils literal notranslate'>num_cpu_cores_per_socket</code> as 4.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/scsi"></div>
      <p style="display: inline;"><strong>scsi</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/scsi" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Valid values are <code class='docutils literal notranslate'>buslogic</code>, <code class='docutils literal notranslate'>lsilogic</code>, <code class='docutils literal notranslate'>lsilogicsas</code> and <code class='docutils literal notranslate'>paravirtual</code>.</p>
      <p><code class='docutils literal notranslate'>paravirtual</code> is default.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;buslogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogicsas&#34;</code></p></li>
        <li><p><code>&#34;paravirtual&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/secure_boot"></div>
      <p style="display: inline;"><strong>secure_boot</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/secure_boot" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Whether to enable or disable (U)EFI secure boot.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/version"></div>
      <p style="display: inline;"><strong>version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/version" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The Virtual machine hardware versions.</p>
      <p>Default is 10 (ESXi 5.5 and onwards).</p>
      <p>If set to <code class='docutils literal notranslate'>latest</code>, the specified virtual machine will be upgraded to the most current hardware version supported on the host.</p>
      <p><code class='docutils literal notranslate'>latest</code> is added in Ansible 2.10.</p>
      <p>Please check VMware documentation for correct virtual machine hardware version.</p>
      <p>Incorrect hardware version may lead to failure in deployment. If hardware version is already equal to the given.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/virt_based_security"></div>
      <p style="display: inline;"><strong>virt_based_security</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/virt_based_security" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Enable Virtualization Based Security feature for Windows on ESXi 6.7 and later, from hardware version 14.</p>
      <p>Supported Guest OS are Windows 10 64 bit, Windows Server 2016, Windows Server 2019 and later.</p>
      <p>The firmware of virtual machine must be EFI and secure boot must be enabled.</p>
      <p>Virtualization Based Security depends on nested virtualization and Intel Virtualization Technology for Directed I/O.</p>
      <p>Deploy on unsupported ESXi, hardware version or firmware may lead to failure or deployed VM with unexpected configurations.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hardware/vpmc_enabled"></div>
      <p style="display: inline;"><strong>vpmc_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hardware/vpmc_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 3.2.0</span></p>
    </div></td>
    <td>
      <p>Enable virtual CPU Performance Counters.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The hostname or IP address of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-is_template"></div>
      <p style="display: inline;"><strong>is_template</strong></p>
      <a class="ansibleOptionLink" href="#parameter-is_template" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Flag the instance as a template.</p>
      <p>This will mark the given virtual machine as template.</p>
      <p>Note, this may need to be done in a dedicated task invocation that is not making any other changes. For example, user cannot change the state from powered-on to powered-off AND save as template in the same task.</p>
      <p>See <a href='../../community/vmware/vmware_guest_module.html' class='module'>community.vmware.vmware_guest</a> source for more details.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-linked_clone"></div>
      <p style="display: inline;"><strong>linked_clone</strong></p>
      <a class="ansibleOptionLink" href="#parameter-linked_clone" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Whether to create a linked clone from the snapshot specified.</p>
      <p>If specified, then <code class='docutils literal notranslate'>snapshot_src</code> is required parameter.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Name of the virtual machine to work with.</p>
      <p>Virtual machine names in vCenter are not necessarily unique, which may be problematic, see <code class='docutils literal notranslate'>name_match</code>.</p>
      <p>If multiple virtual machines with same name exists, then <code class='docutils literal notranslate'>folder</code> is required parameter to identify uniqueness of the virtual machine.</p>
      <p>This parameter is required, if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>poweredon</code>, <code class='docutils literal notranslate'>powered-on</code>, <code class='docutils literal notranslate'>poweredoff</code>, <code class='docutils literal notranslate'>powered-off</code>, <code class='docutils literal notranslate'>present</code>, <code class='docutils literal notranslate'>restarted</code>, <code class='docutils literal notranslate'>suspended</code> and virtual machine does not exists.</p>
      <p>This parameter is case sensitive.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-name_match"></div>
      <p style="display: inline;"><strong>name_match</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name_match" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>If multiple virtual machines matching the name, use the first or last found.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">&#34;first&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;last&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks"></div>
      <p style="display: inline;"><strong>networks</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </div></td>
    <td>
      <p>A list of networks (in the order of the NICs).</p>
      <p>Removing NICs is not allowed, while reconfiguring the virtual machine.</p>
      <p>All parameters and VMware object names are case sensitive.</p>
      <p>The <em>type</em>, <em>ip</em>, <em>netmask</em>, <em>gateway</em>, <em>domain</em>, <em>dns_servers</em> options don&#x27;t set to a guest when creating a blank new virtual machine. They are set by the customization via vmware-tools. If you want to set the value of the options to a guest, you need to clone from a template with installed OS and vmware-tools(also Perl when Linux).</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/connected"></div>
      <p style="display: inline;"><strong>connected</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/connected" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether the NIC is currently connected.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/device_type"></div>
      <p style="display: inline;"><strong>device_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/device_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Virtual network device.</p>
      <p>Valid value can be one of <code class='docutils literal notranslate'>e1000</code>, <code class='docutils literal notranslate'>e1000e</code>, <code class='docutils literal notranslate'>pcnet32</code>, <code class='docutils literal notranslate'>vmxnet2</code>, <code class='docutils literal notranslate'>vmxnet3</code>, <code class='docutils literal notranslate'>sriov</code>.</p>
      <p><code class='docutils literal notranslate'>vmxnet3</code> is default.</p>
      <p>Optional per entry.</p>
      <p>Used for virtual hardware.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/dns_servers"></div>
      <p style="display: inline;"><strong>dns_servers</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/dns_servers" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>DNS servers for this network interface (Windows).</p>
      <p>Optional per entry.</p>
      <p>Used for OS customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/domain"></div>
      <p style="display: inline;"><strong>domain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/domain" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Domain name for this network interface (Windows).</p>
      <p>Optional per entry.</p>
      <p>Used for OS customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/dvswitch_name"></div>
      <p style="display: inline;"><strong>dvswitch_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/dvswitch_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Name of the distributed vSwitch.</p>
      <p>Optional per entry.</p>
      <p>Used for virtual hardware.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/gateway"></div>
      <p style="display: inline;"><strong>gateway</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/gateway" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Static gateway.</p>
      <p>Optional per entry.</p>
      <p>Used for OS customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/ip"></div>
      <p style="display: inline;"><strong>ip</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/ip" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Static IP address. Implies <code class='docutils literal notranslate'>type=static</code>.</p>
      <p>Optional per entry.</p>
      <p>Used for OS customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/mac"></div>
      <p style="display: inline;"><strong>mac</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/mac" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Customize MAC address.</p>
      <p>Optional per entry.</p>
      <p>Used for virtual hardware.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Name of the portgroup or distributed virtual portgroup for this interface.</p>
      <p>Required per entry.</p>
      <p>When specifying distributed virtual portgroup make sure given <code class='docutils literal notranslate'>esxi_hostname</code> or <code class='docutils literal notranslate'>cluster</code> is associated with it.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/netmask"></div>
      <p style="display: inline;"><strong>netmask</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/netmask" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Static netmask required for <code class='docutils literal notranslate'>ip</code>.</p>
      <p>Optional per entry.</p>
      <p>Used for OS customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/start_connected"></div>
      <p style="display: inline;"><strong>start_connected</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/start_connected" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Specifies whether or not to connect the device when the virtual machine starts.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/type"></div>
      <p style="display: inline;"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Type of IP assignment.</p>
      <p>Valid values are one of <code class='docutils literal notranslate'>dhcp</code>, <code class='docutils literal notranslate'>static</code>.</p>
      <p><code class='docutils literal notranslate'>dhcp</code> is default.</p>
      <p>Optional per entry.</p>
      <p>Used for OS customization.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks/vlan"></div>
      <p style="display: inline;"><strong>vlan</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks/vlan" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>VLAN number for this interface.</p>
      <p>Required per entry.</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-nvdimm"></div>
      <p style="display: inline;"><strong>nvdimm</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nvdimm" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Add or remove a virtual NVDIMM device to the virtual machine.</p>
      <p>VM virtual hardware version must be 14 or higher on vSphere 6.7 or later.</p>
      <p>Verify that guest OS of the virtual machine supports PMem before adding virtual NVDIMM device.</p>
      <p>Verify that you have the <em>Datastore.Allocate</em> space privilege on the virtual machine.</p>
      <p>Make sure that the host or the cluster on which the virtual machine resides has available PMem resources.</p>
      <p>To add or remove virtual NVDIMM device to the existing virtual machine, it must be in power off state.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-nvdimm/label"></div>
      <p style="display: inline;"><strong>label</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nvdimm/label" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The label of the virtual NVDIMM device to be removed or configured, e.g., "NVDIMM 1".</p>
      <p>This parameter is required when <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>absent</code>, or <code class='docutils literal notranslate'>present</code> to reconfigure NVDIMM device size. When add a new device, please do not set <code class='docutils literal notranslate'>label</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-nvdimm/size_mb"></div>
      <p style="display: inline;"><strong>size_mb</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nvdimm/size_mb" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Virtual NVDIMM device size in MB.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">1024</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-nvdimm/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nvdimm/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Valid value is <code class='docutils literal notranslate'>present</code> or <code class='docutils literal notranslate'>absent</code>.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code>, then the NVDIMM device with specified <code class='docutils literal notranslate'>label</code> will be removed.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;present&#34;</code></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <div class="ansibleOptionAnchor" id="parameter-pass"></div>
      <div class="ansibleOptionAnchor" id="parameter-pwd"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: pass, pwd</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The password of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The port number of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Address of a proxy that will receive all HTTPS requests and relay them.</p>
      <p>The format is a hostname or a IP.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_HOST</code> will be used instead.</p>
      <p>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-resource_pool"></div>
      <p style="display: inline;"><strong>resource_pool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_pool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Use the given resource pool for virtual machine operation.</p>
      <p>This parameter is case sensitive.</p>
      <p>Resource pool should be child of the selected host parent.</p>
      <p>When not specified <em>Resources</em> is taken as default value.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snapshot_src"></div>
      <p style="display: inline;"><strong>snapshot_src</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snapshot_src" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Name of the existing snapshot to use to create a clone of a virtual machine.</p>
      <p>This parameter is case sensitive.</p>
      <p>While creating linked clone using <code class='docutils literal notranslate'>linked_clone</code> parameter, this parameter is required.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Specify the state the virtual machine should be in.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code> and virtual machine exists, ensure the virtual machine configurations conforms to task arguments.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>absent</code> and virtual machine exists, then the specified virtual machine is removed with it&#x27;s associated components.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to one of the following <code class='docutils literal notranslate'>poweredon</code>, <code class='docutils literal notranslate'>powered-on</code>, <code class='docutils literal notranslate'>poweredoff</code>, <code class='docutils literal notranslate'>powered-off</code>, <code class='docutils literal notranslate'>present</code>, <code class='docutils literal notranslate'>restarted</code>, <code class='docutils literal notranslate'>suspended</code> and virtual machine does not exists, virtual machine is deployed with the given parameters.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>poweredon</code> or <code class='docutils literal notranslate'>powered-on</code> and virtual machine exists with powerstate other than powered on, then the specified virtual machine is powered on.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>poweredoff</code> or <code class='docutils literal notranslate'>powered-off</code> and virtual machine exists with powerstate other than powered off, then the specified virtual machine is powered off.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>restarted</code> and virtual machine exists, then the virtual machine is restarted.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>suspended</code> and virtual machine exists, then the virtual machine is set to suspended mode.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>shutdownguest</code> or <code class='docutils literal notranslate'>shutdown-guest</code> and virtual machine exists, then the virtual machine is shutdown.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>rebootguest</code> or <code class='docutils literal notranslate'>reboot-guest</code> and virtual machine exists, then the virtual machine is rebooted.</p>
      <p>Powerstate <code class='docutils literal notranslate'>powered-on</code> and <code class='docutils literal notranslate'>powered-off</code> is added in version 2.10.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code>&#34;poweredon&#34;</code></p></li>
        <li><p><code>&#34;powered-on&#34;</code></p></li>
        <li><p><code>&#34;poweredoff&#34;</code></p></li>
        <li><p><code>&#34;powered-off&#34;</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">&#34;present&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;rebootguest&#34;</code></p></li>
        <li><p><code>&#34;reboot-guest&#34;</code></p></li>
        <li><p><code>&#34;restarted&#34;</code></p></li>
        <li><p><code>&#34;suspended&#34;</code></p></li>
        <li><p><code>&#34;shutdownguest&#34;</code></p></li>
        <li><p><code>&#34;shutdown-guest&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-state_change_timeout"></div>
      <p style="display: inline;"><strong>state_change_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state_change_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>If the <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>shutdownguest</code>, by default the module will return immediately after sending the shutdown signal.</p>
      <p>If this argument is set to a positive integer, the module will instead wait for the virtual machine to reach the poweredoff state.</p>
      <p>The value sets a timeout in seconds for the module to wait for the state change.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">0</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-template"></div>
      <div class="ansibleOptionAnchor" id="parameter-template_src"></div>
      <p style="display: inline;"><strong>template</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: template_src</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Template or existing virtual machine used to create new virtual machine.</p>
      <p>If this value is not set, virtual machine is created without using a template.</p>
      <p>If the virtual machine already exists, this parameter will be ignored.</p>
      <p>This parameter is case sensitive.</p>
      <p>From version 2.8 onwards, absolute path to virtual machine or template can be used.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-use_instance_uuid"></div>
      <p style="display: inline;"><strong>use_instance_uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-use_instance_uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Whether to use the VMware instance UUID rather than the BIOS UUID.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <div class="ansibleOptionAnchor" id="parameter-admin"></div>
      <div class="ansibleOptionAnchor" id="parameter-user"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: admin, user</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The username of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-uuid"></div>
      <p style="display: inline;"><strong>uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>UUID of the virtual machine to manage if known, this is VMware&#x27;s unique identifier.</p>
      <p>This is required if <code class='docutils literal notranslate'>name</code> is not supplied.</p>
      <p>If virtual machine does not exists, then this parameter is ignored.</p>
      <p>Please note that a supplied UUID will be ignored on virtual machine creation, as VMware creates the UUID internally.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Allows connection when SSL certificates are not valid. Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_VALIDATE_CERTS</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p>If set to <code class='docutils literal notranslate'>true</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vapp_properties"></div>
      <p style="display: inline;"><strong>vapp_properties</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vapp_properties" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </div></td>
    <td>
      <p>A list of vApp properties.</p>
      <p>For full list of attributes and types refer to: <a href='https://code.vmware.com/apis/704/vsphere/vim.vApp.PropertyInfo.html'>https://code.vmware.com/apis/704/vsphere/vim.vApp.PropertyInfo.html</a></p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vapp_properties/id"></div>
      <p style="display: inline;"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vapp_properties/id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Property ID.</p>
      <p>Required per entry.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vapp_properties/operation"></div>
      <p style="display: inline;"><strong>operation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vapp_properties/operation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The <code class='docutils literal notranslate'>remove</code> attribute is required only when removing properties.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vapp_properties/type"></div>
      <p style="display: inline;"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vapp_properties/type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Value type, string type by default.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vapp_properties/value"></div>
      <p style="display: inline;"><strong>value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vapp_properties/value" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Property value.</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-wait_for_customization"></div>
      <p style="display: inline;"><strong>wait_for_customization</strong></p>
      <a class="ansibleOptionLink" href="#parameter-wait_for_customization" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Wait until vCenter detects all guest customizations as successfully completed.</p>
      <p>When enabled, the VM will automatically be powered on.</p>
      <p>If vCenter does not detect guest customization start or succeed, failed events after time <code class='docutils literal notranslate'>wait_for_customization_timeout</code> parameter specified, warning message will be printed and task result is fail.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-wait_for_customization_timeout"></div>
      <p style="display: inline;"><strong>wait_for_customization_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-wait_for_customization_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Define a timeout (in seconds) for the wait_for_customization parameter.</p>
      <p>Be careful when setting this value since the time guest customization took may differ among guest OSes.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">3600</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-wait_for_ip_address"></div>
      <p style="display: inline;"><strong>wait_for_ip_address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-wait_for_ip_address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Wait until vCenter detects an IP address for the virtual machine.</p>
      <p>This requires vmware-tools (vmtoolsd) to properly work after creation.</p>
      <p>vmware-tools needs to be installed on the given virtual machine in order to work with this parameter.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-wait_for_ip_address_timeout"></div>
      <p style="display: inline;"><strong>wait_for_ip_address_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-wait_for_ip_address_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Define a timeout (in seconds) for the wait_for_ip_address parameter.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">300</code></p>
    </td>
  </tr>
  </tbody>
  </table>




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

.. raw:: html

  <table style="width: 100%; height: 1px;">
  <thead>
  <tr>
    <th><p>Key</p></th>
    <th><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="return-instance"></div>
      <p style="display: inline;"><strong>instance</strong></p>
      <a class="ansibleOptionLink" href="#return-instance" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>metadata about the new virtual machine</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Returned:</span> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>&#34;None&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




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

