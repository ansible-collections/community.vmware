

community.vmware.vmware_guest_disk module -- Manage disks related to virtual machine in given vCenter infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The datacenter name to which virtual machine belongs to.</p>
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
      <p>A list of disks to add or remove.</p>
      <p>The virtual disk related information is provided using this list.</p>
      <p>All values and parameters are case sensitive.</p>
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
      <p>Select the less used datastore. Specify only if <code class='docutils literal notranslate'>datastore</code> is not specified.</p>
      <p>Not applicable when disk <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>vpmemdisk</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/bus_sharing"></div>
      <p style="display: inline;"><strong>bus_sharing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/bus_sharing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Only functions with Paravirtual SCSI Controller.</p>
      <p>Allows for the sharing of the scsi bus between two virtual machines.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">&#34;noSharing&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;physicalSharing&#34;</code></p></li>
        <li><p><code>&#34;virtualSharing&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/cluster_disk"></div>
      <p style="display: inline;"><strong>cluster_disk</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/cluster_disk" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>This value allows for the sharing of an RDM between two machines.</p>
      <p>The primary machine holding the RDM uses the default <code class='docutils literal notranslate'>false</code>.</p>
      <p>The secondary machine holding the RDM uses <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/compatibility_mode"></div>
      <p style="display: inline;"><strong>compatibility_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/compatibility_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Compatibility mode for raw devices. Required when disk type <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>rdm</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;physicalMode&#34;</code></p></li>
        <li><p><code>&#34;virtualMode&#34;</code></p></li>
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
      <p>This parameter is used with <code class='docutils literal notranslate'>controller_type</code> for specifying controller bus number.</p>
      <p>For <code class='docutils literal notranslate'>ide</code> controller type, valid value is 0 or 1.</p>
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
      <p>This parameter is added for managing disks attaching other types of controllers, e.g., SATA or NVMe.</p>
      <p>If either <code class='docutils literal notranslate'>controller_type</code> or <code class='docutils literal notranslate'>scsi_type</code> is not specified, then use <code class='docutils literal notranslate'>paravirtual</code> type.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;buslogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogicsas&#34;</code></p></li>
        <li><p><code>&#34;paravirtual&#34;</code></p></li>
        <li><p><code>&#34;sata&#34;</code></p></li>
        <li><p><code>&#34;nvme&#34;</code></p></li>
        <li><p><code>&#34;ide&#34;</code></p></li>
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
      <p>Name of datastore or datastore cluster to be used for the disk.</p>
      <p>Not applicable when disk <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>vpmemdisk</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/destroy"></div>
      <p style="display: inline;"><strong>destroy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/destroy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>If <code class='docutils literal notranslate'>state</code> is <code class='docutils literal notranslate'>absent</code>, make sure the disk file is deleted from the datastore. Added in version 2.10.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

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
      <p>Type of disk mode. If not specified then use <code class='docutils literal notranslate'>persistent</code> mode for new disk.</p>
      <p>If set to &#x27;persistent&#x27; mode, changes are immediately and permanently written to the virtual disk.</p>
      <p>If set to &#x27;independent_persistent&#x27; mode, same as persistent, but not affected by snapshots.</p>
      <p>If set to &#x27;independent_nonpersistent&#x27; mode, changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.</p>
      <p>Not applicable when disk <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>vpmemdisk</code>.</p>
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
      <p>Existing disk image to be used. Filename must already exist on the datastore.</p>
      <p>Specify filename string in <code class='docutils literal notranslate'>[datastore_name] path/to/file.vmdk</code> format. Added in version 2.10.</p>
      <p>Not applicable when disk <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>vpmemdisk</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/iolimit"></div>
      <p style="display: inline;"><strong>iolimit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/iolimit" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Section specifies the shares and limit for storage I/O resource.</p>
      <p>Not applicable when disk <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>vpmemdisk</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/iolimit/limit"></div>
      <p style="display: inline;"><strong>limit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/iolimit/limit" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Section specifies values for limit where the utilization of a virtual machine will not exceed, even if there are available resources.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/iolimit/shares"></div>
      <p style="display: inline;"><strong>shares</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/iolimit/shares" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Specifies different types of shares user can add for the given disk.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/iolimit/shares/level"></div>
      <p style="display: inline;"><strong>level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/iolimit/shares/level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Specifies different level for the shares section.</p>
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
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/iolimit/shares/level_value"></div>
      <p style="display: inline;"><strong>level_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/iolimit/shares/level_value" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Custom value when <code class='docutils literal notranslate'>level</code> is set as <code class='docutils literal notranslate'>custom</code>.</p>
    </td>
  </tr>


  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/rdm_path"></div>
      <p style="display: inline;"><strong>rdm_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/rdm_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Path of LUN for Raw Device Mapping required for disk type <code class='docutils literal notranslate'>rdm</code>.</p>
      <p>Only valid if <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>rdm</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/scsi_controller"></div>
      <p style="display: inline;"><strong>scsi_controller</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/scsi_controller" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>SCSI controller number. Only 4 SCSI controllers are allowed per VM.</p>
      <p>Care should be taken while specifying &#x27;scsi_controller&#x27; is 0 and &#x27;unit_number&#x27; as 0 as this disk may contain OS.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-disk/scsi_type"></div>
      <p style="display: inline;"><strong>scsi_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/scsi_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Type of SCSI controller. This value is required only for the first occurrence of SCSI Controller.</p>
      <p>This value is ignored, if SCSI Controller is already present or <code class='docutils literal notranslate'>state</code> is <code class='docutils literal notranslate'>absent</code>.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-disk/shares"></div>
      <p style="display: inline;"><strong>shares</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/shares" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Section for iolimit section tells about what are all different types of shares user can add for disk.</p>
      <p>Not applicable when disk <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>vpmemdisk</code>.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/shares/level"></div>
      <p style="display: inline;"><strong>level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/shares/level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Tells about different level for the shares section.</p>
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
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/shares/level_value"></div>
      <p style="display: inline;"><strong>level_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/shares/level_value" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Custom value when <code class='docutils literal notranslate'>level</code> is set as <code class='docutils literal notranslate'>custom</code>.</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk/sharing"></div>
      <p style="display: inline;"><strong>sharing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/sharing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>The sharing mode of the virtual disk.</p>
      <p>Setting sharing means that multiple virtual machines can write to the virtual disk.</p>
      <p>Sharing can only be set if <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>eagerzeroedthick</code> or <code class='docutils literal notranslate'>rdm</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

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
      <p>If size specified then unit must be specified. There is no space allowed in between size number and unit.</p>
      <p>Only first occurrence in disk element will be considered, even if there are multiple size* parameters available.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-disk/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>State of disk.</p>
      <p>If set to &#x27;absent&#x27;, disk will be removed permanently from virtual machine configuration and from VMware storage.</p>
      <p>If set to &#x27;present&#x27;, disk will be added if not present at given Controller and Unit Number.</p>
      <p>or disk exists with different size, disk size is increased, reducing disk size is not allowed.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">&#34;present&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

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
      <p>The type of disk, if not specified then use <code class='docutils literal notranslate'>thick</code> type for new disk, no eagerzero.</p>
      <p>The disk type <code class='docutils literal notranslate'>rdm</code> is added in version 1.13.0.</p>
      <p>The disk type <code class='docutils literal notranslate'>vpmemdisk</code> is added in version 2.7.0.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;thin&#34;</code></p></li>
        <li><p><code>&#34;eagerzeroedthick&#34;</code></p></li>
        <li><p><code>&#34;thick&#34;</code></p></li>
        <li><p><code>&#34;rdm&#34;</code></p></li>
        <li><p><code>&#34;vpmemdisk&#34;</code></p></li>
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
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>Disk Unit Number.</p>
      <p>Valid value range from 0 to 15, except 7 for SCSI Controller.</p>
      <p>Valid value range from 0 to 64, except 7 for Paravirtual SCSI Controller on Virtual Hardware version 14 or higher.</p>
      <p>Valid value range from 0 to 29 for SATA controller.</p>
      <p>Valid value range from 0 to 14 for NVME controller.</p>
      <p>Valid value range from 0 to 1 for IDE controller.</p>
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
      <p>Destination folder, absolute or relative path to find an existing guest.</p>
      <p>This is a required parameter, only if multiple VMs are found with same name.</p>
      <p>The folder should include the datacenter. ESX&#x27;s datacenter is ha-datacenter</p>
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
      <div class="ansibleOptionAnchor" id="parameter-moid"></div>
      <p style="display: inline;"><strong>moid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-moid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.</p>
      <p>This is required if <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>uuid</code> is not supplied.</p>
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
      <p>Name of the virtual machine.</p>
      <p>This is a required parameter, if parameter <code class='docutils literal notranslate'>uuid</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
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
      <p>UUID of the instance to gather facts if known, this is VMware&#x27;s unique identifier.</p>
      <p>This is a required parameter, if parameter <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
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
  </tbody>
  </table>




Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
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
      <div class="ansibleOptionAnchor" id="return-disk_changes"></div>
      <p style="display: inline;"><strong>disk_changes</strong></p>
      <a class="ansibleOptionLink" href="#return-disk_changes" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>result of each task, key is the 0-based index with the same sequence in which the tasks were defined</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Returned:</span> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>{&#34;0&#34;: &#34;Disk deleted.&#34;, &#34;1&#34;: &#34;Disk created.&#34;}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="return-disk_data"></div>
      <p style="display: inline;"><strong>disk_data</strong></p>
      <a class="ansibleOptionLink" href="#return-disk_data" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>metadata about the virtual machine&#x27;s disks after managing them</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Returned:</span> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>{&#34;0&#34;: {&#34;backing_datastore&#34;: &#34;datastore2&#34;, &#34;backing_disk_mode&#34;: &#34;persistent&#34;, &#34;backing_eagerlyscrub&#34;: false, &#34;backing_filename&#34;: &#34;[datastore2] VM_225/VM_225.vmdk&#34;, &#34;backing_thinprovisioned&#34;: false, &#34;backing_uuid&#34;: &#34;421e4592-c069-924d-ce20-7e7533fab926&#34;, &#34;backing_writethrough&#34;: false, &#34;capacity_in_bytes&#34;: 10485760, &#34;capacity_in_kb&#34;: 10240, &#34;controller_key&#34;: 1000, &#34;key&#34;: 2000, &#34;label&#34;: &#34;Hard disk 1&#34;, &#34;summary&#34;: &#34;10,240 KB&#34;, &#34;unit_number&#34;: 0}}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

