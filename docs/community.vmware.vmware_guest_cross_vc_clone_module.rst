

community.vmware.vmware_guest_cross_vc_clone module -- Cross-vCenter VM/template clone
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_cross_vc_clone`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used for Cross-vCenter vm/template clone








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_datastore"></div>
      <p style="display: inline;"><strong>destination_datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the destination datastore or the datastore cluster.</p>
      <p>If datastore cluster name is specified, we will find the Storage DRS recommended datastore in that cluster.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_host"></div>
      <p style="display: inline;"><strong>destination_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the destination host.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_resource_pool"></div>
      <p style="display: inline;"><strong>destination_resource_pool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_resource_pool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Destination resource pool.</p>
      <p>If not provided, the destination host&#x27;s parent&#x27;s resource pool will be used.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_vcenter"></div>
      <p style="display: inline;"><strong>destination_vcenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_vcenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The hostname or IP address of the destination VCenter.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_vcenter_password"></div>
      <p style="display: inline;"><strong>destination_vcenter_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_vcenter_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The password of the destination VCenter.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_vcenter_port"></div>
      <p style="display: inline;"><strong>destination_vcenter_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_vcenter_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The port to establish connection in the destination VCenter.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_vcenter_username"></div>
      <p style="display: inline;"><strong>destination_vcenter_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_vcenter_username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The username of the destination VCenter.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_vcenter_validate_certs"></div>
      <p style="display: inline;"><strong>destination_vcenter_validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_vcenter_validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Parameter to indicate if certification validation needs to be done on destination VCenter.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_vm_folder"></div>
      <p style="display: inline;"><strong>destination_vm_folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_vm_folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Destination folder, absolute path to deploy the cloned vm.</p>
      <p>This parameter is case sensitive.</p>
      <p>Examples:</p>
      <p>   folder: vm</p>
      <p>   folder: ha-datacenter/vm</p>
      <p>   folder: /datacenter1/vm</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_vm_name"></div>
      <p style="display: inline;"><strong>destination_vm_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_vm_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the cloned VM.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
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
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-is_template"></div>
      <p style="display: inline;"><strong>is_template</strong></p>
      <a class="ansibleOptionLink" href="#parameter-is_template" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Specifies whether or not the new virtual machine should be marked as a template.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-moid"></div>
      <p style="display: inline;"><strong>moid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-moid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Managed Object ID of the vm/template instance to manage if known, this is a unique identifier only within a single vCenter instance.</p>
      <p>This is required if <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>uuid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the virtual machine or template.</p>
      <p>This is a required parameter, if parameter <code class='docutils literal notranslate'>uuid</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
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
    <td valign="top">
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
    <td valign="top">
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
    <td valign="top">
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
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The state of Virtual Machine deployed.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code> and VM does not exists, then VM is created.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code> and VM exists, no action is taken.</p>
      <p>If set to <code class='docutils literal notranslate'>poweredon</code> and VM does not exists, then VM is created with powered on state.</p>
      <p>If set to <code class='docutils literal notranslate'>poweredon</code> and VM exists, no action is taken.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;poweredon&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
      <p style="display: inline;"><strong>timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td valign="top">
      <p>The timeout in seconds. When the timeout is reached, the module will fail.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">3600</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
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
    <td valign="top">
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
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-uuid"></div>
      <p style="display: inline;"><strong>uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>UUID of the vm/template instance to clone from, this is VMware&#x27;s unique identifier.</p>
      <p>This is a required parameter, if parameter <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
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

    
    # Clone template
    - name: clone a template across VC
      community.vmware.vmware_guest_cross_vc_clone:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        name: "test_vm1"
        destination_vm_name: "cloned_vm_from_template"
        destination_vcenter: '{{ destination_vcenter_hostname }}'
        destination_vcenter_username: '{{ destination_vcenter_username }}'
        destination_vcenter_password: '{{ destination_vcenter_password }}'
        destination_vcenter_port: '{{ destination_vcenter_port }}'
        destination_vcenter_validate_certs: '{{ destination_vcenter_validate_certs }}'
        destination_host: '{{ destination_esxi }}'
        destination_datastore: '{{ destination_datastore }}'
        destination_vm_folder: '{{ destination_vm_folder }}'
        state: present
      register: cross_vc_clone_from_template

    - name: clone a VM across VC
      community.vmware.vmware_guest_cross_vc_clone:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: "{{ vcenter_password }}"
        name: "test_vm1"
        destination_vm_name: "cloned_vm_from_vm"
        destination_vcenter: '{{ destination_vcenter_hostname }}'
        destination_vcenter_username: '{{ destination_vcenter_username }}'
        destination_vcenter_password: '{{ destination_vcenter_password }}'
        destination_host: '{{ destination_esxi }}'
        destination_datastore: '{{ destination_datastore }}'
        destination_vm_folder: '{{ destination_vm_folder }}'
        state: poweredon
      register: cross_vc_clone_from_vm

    - name: check_mode support
      community.vmware.vmware_guest_cross_vc_clone:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: "{{ vcenter_password }}"
        name: "test_vm1"
        destination_vm_name: "cloned_vm_from_vm"
        destination_vcenter: '{{ destination_vcenter_hostname }}'
        destination_vcenter_username: '{{ destination_vcenter_username }}'
        destination_vcenter_password: '{{ destination_vcenter_password }}'
        destination_host: '{{ destination_esxi }}'
        destination_datastore: '{{ destination_datastore }}'
        destination_vm_folder: '{{ destination_vm_folder }}'
      check_mode: true





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
      <div class="ansibleOptionAnchor" id="return-vm_info"></div>
      <p style="display: inline;"><strong>vm_info</strong></p>
      <a class="ansibleOptionLink" href="#return-vm_info" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>metadata about the virtual machine</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;datastore&#34;: &#34;&#34;, &#34;host&#34;: &#34;&#34;, &#34;power_on&#34;: &#34;&#34;, &#34;vcenter&#34;: &#34;&#34;, &#34;vm_folder&#34;: &#34;&#34;, &#34;vm_name&#34;: &#34;&#34;}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Anusha Hegde (@anusha94)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

