

community.vmware.vmware_guest_controller module -- Manage disk or USB controllers related to virtual machine in given vCenter infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_controller`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add, remove disk controllers or USB controllers belonging to given virtual machine.
- All parameters and VMware object names are case sensitive.








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th colspan="2"><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-controllers"></div>
      <p style="display: inline;"><strong>controllers</strong></p>
      <a class="ansibleOptionLink" href="#parameter-controllers" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>A list of disk or USB controllers to add or remove.</p>
      <p>Total 4 disk controllers with the same type are allowed per VM.</p>
      <p>Total 2 USB controllers are allowed per VM, 1 USB 2.0 and 1 USB 3.0 or 3.1.</p>
      <p>For specific guest OS, supported controller types please refer to VMware Compatibility Guide.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-controllers/bus_sharing"></div>
      <p style="display: inline;"><strong>bus_sharing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-controllers/bus_sharing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Bus sharing type for SCSI controller.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;noSharing&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;physicalSharing&#34;</code></p></li>
        <li><p><code>&#34;virtualSharing&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-controllers/controller_number"></div>
      <p style="display: inline;"><strong>controller_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-controllers/controller_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Disk controller bus number. When <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>absent</code>, this parameter is required.</p>
      <p>When <code class='docutils literal notranslate'>type</code> set to <code class='docutils literal notranslate'>usb2</code> or <code class='docutils literal notranslate'>usb3</code>, this parameter is not required.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>0</code></p></li>
        <li><p><code>1</code></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-controllers/state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-controllers/state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Add new controller or remove specified existing controller.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>absent</code>, the specified controller will be removed from virtual machine when there is no disk or device attaching to it.</p>
      <p>If specified controller is removed or not exist, no action will be taken only warning message.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>, new controller with specified type will be added.</p>
      <p>If the number of controller with specified controller type reaches it&#x27;s maximum, no action will be taken only warning message.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;present&#34;</code></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-controllers/type"></div>
      <p style="display: inline;"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-controllers/type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Type of disk or USB controller.</p>
      <p>From vSphere 6.5 and virtual machine with hardware version 13, <code class='docutils literal notranslate'>nvme</code> controller starts to be supported.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;buslogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogic&#34;</code></p></li>
        <li><p><code>&#34;lsilogicsas&#34;</code></p></li>
        <li><p><code>&#34;paravirtual&#34;</code></p></li>
        <li><p><code>&#34;sata&#34;</code></p></li>
        <li><p><code>&#34;nvme&#34;</code></p></li>
        <li><p><code>&#34;usb2&#34;</code></p></li>
        <li><p><code>&#34;usb3&#34;</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The datacenter name to which virtual machine belongs to.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;ha-datacenter&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
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
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-gather_disk_controller_facts"></div>
      <p style="display: inline;"><strong>gather_disk_controller_facts</strong></p>
      <a class="ansibleOptionLink" href="#parameter-gather_disk_controller_facts" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Whether to collect existing disk and USB controllers facts only.</p>
      <p>When this parameter is set to <code class='docutils literal notranslate'>true</code>, <code class='docutils literal notranslate'>controllers</code> parameter will be ignored.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The hostname or IP address of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-moid"></div>
      <p style="display: inline;"><strong>moid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-moid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.</p>
      <p>This is required if <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>uuid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the virtual machine.</p>
      <p>This is a required parameter, if parameter <code class='docutils literal notranslate'>uuid</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <div class="ansibleOptionAnchor" id="parameter-pass"></div>
      <div class="ansibleOptionAnchor" id="parameter-pwd"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: pass, pwd</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The password of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The port number of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Address of a proxy that will receive all HTTPS requests and relay them.</p>
      <p>The format is a hostname or a IP.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_HOST</code> will be used instead.</p>
      <p>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-sleep_time"></div>
      <p style="display: inline;"><strong>sleep_time</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sleep_time" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The sleep time in seconds after VM reconfigure task completes, used when not get the updated VM controller facts after VM reconfiguration.</p>
      <p>This parameter is not required. Maximum value is 600.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">10</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-use_instance_uuid"></div>
      <p style="display: inline;"><strong>use_instance_uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-use_instance_uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Whether to use the VMware instance UUID rather than the BIOS UUID.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <div class="ansibleOptionAnchor" id="parameter-admin"></div>
      <div class="ansibleOptionAnchor" id="parameter-user"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: admin, user</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The username of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-uuid"></div>
      <p style="display: inline;"><strong>uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>UUID of the instance to gather facts if known, this is VMware&#x27;s unique identifier.</p>
      <p>This is a required parameter, if parameter <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Allows connection when SSL certificates are not valid. Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_VALIDATE_CERTS</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p>If set to <code class='docutils literal notranslate'>true</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
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

    
    - name: Add disk and USB 3.0 controllers for virtual machine located by name
      community.vmware.vmware_guest_controller:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: test_VM
        controllers:
          - state: present
            type: sata
          - state: present
            type: nvme
          - state: present
            type: usb3
      delegate_to: localhost
      register: disk_controller_facts

    - name: Remove disk controllers and USB 2.0 from virtual machine located by moid
      community.vmware.vmware_guest_controller:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        moid: vm-33
        controllers:
          - state: absent
            controller_number: 1
            type: sata
          - state: absent
            controller_number: 0
            type: nvme
          - state: absent
            type: usb2
      delegate_to: localhost
      register: disk_controller_facts





Return Values
-------------
The following are the fields unique to this module:

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Key</p></th>
    <th><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-disk_controller_status"></div>
      <p style="display: inline;"><strong>disk_controller_status</strong></p>
      <a class="ansibleOptionLink" href="#return-disk_controller_status" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>metadata about the virtual machine&#x27;s existing disk controllers or after adding or removing operation</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;nvme&#34;: {&#34;0&#34;: {&#34;controller_busnumber&#34;: 0, &#34;controller_controllerkey&#34;: 100, &#34;controller_devicekey&#34;: 31000, &#34;controller_disks_devicekey&#34;: [], &#34;controller_label&#34;: &#34;NVME controller 0&#34;, &#34;controller_summary&#34;: &#34;NVME controller 0&#34;, &#34;controller_unitnumber&#34;: 30}}, &#34;sata&#34;: {&#34;0&#34;: {&#34;controller_busnumber&#34;: 0, &#34;controller_controllerkey&#34;: 100, &#34;controller_devicekey&#34;: 15000, &#34;controller_disks_devicekey&#34;: [16000, 16001], &#34;controller_label&#34;: &#34;SATA controller 0&#34;, &#34;controller_summary&#34;: &#34;AHCI&#34;, &#34;controller_unitnumber&#34;: 24}}, &#34;scsi&#34;: {&#34;0&#34;: {&#34;controller_bus_sharing&#34;: &#34;noSharing&#34;, &#34;controller_busnumber&#34;: 0, &#34;controller_controllerkey&#34;: 100, &#34;controller_devicekey&#34;: 1000, &#34;controller_disks_devicekey&#34;: [2000], &#34;controller_label&#34;: &#34;SCSI controller 0&#34;, &#34;controller_summary&#34;: &#34;LSI Logic SAS&#34;, &#34;controller_unitnumber&#34;: 3}, &#34;1&#34;: {&#34;controller_bus_sharing&#34;: &#34;physicalSharing&#34;, &#34;controller_busnumber&#34;: 1, &#34;controller_controllerkey&#34;: 100, &#34;controller_devicekey&#34;: 1001, &#34;controller_disks_devicekey&#34;: [], &#34;controller_label&#34;: &#34;SCSI controller 1&#34;, &#34;controller_summary&#34;: &#34;VMware paravirtual SCSI&#34;, &#34;controller_unitnumber&#34;: 4}}, &#34;usb2&#34;: {&#34;0&#34;: {&#34;controller_busnumber&#34;: 0, &#34;controller_controllerkey&#34;: 100, &#34;controller_devicekey&#34;: 7000, &#34;controller_disks_devicekey&#34;: [], &#34;controller_label&#34;: &#34;USB Controller&#34;, &#34;controller_summary&#34;: &#34;Auto connect Disabled&#34;, &#34;controller_unitnumber&#34;: 22}}}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Diane Wang (@Tomorrow9) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

