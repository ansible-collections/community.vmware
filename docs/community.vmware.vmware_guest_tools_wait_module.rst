

community.vmware.vmware_guest_tools_wait module -- Wait for VMware tools to become available
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_tools_wait`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to wait for VMware tools to become available on the given VM and return facts.








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
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the datacenter.</p>
      <p>The datacenter to search for a virtual machine.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Destination folder, absolute or relative path to find an existing guest.</p>
      <p>This is required only, if multiple VMs with same <code class='docutils literal notranslate'>name</code> is found.</p>
      <p>The folder should include the datacenter. ESX&#x27;s datacenter is <code class='docutils literal notranslate'>ha-datacenter</code>.</p>
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
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the VM for which to wait until the tools become available.</p>
      <p>This is required if <code class='docutils literal notranslate'>uuid</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name_match"></div>
      <p style="display: inline;"><strong>name_match</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name_match" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>If multiple VMs match the name, use the first or last found.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;first&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;last&#34;</code></p></li>
      </ul>

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
      <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
      <p style="display: inline;"><strong>timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Max duration of the waiting period (seconds).</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">500</code></p>
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
      <p>UUID of the VM  for which to wait until the tools become available, if known. This is VMware&#x27;s unique identifier.</p>
      <p>This is required, if <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
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

    
    - name: Wait for VMware tools to become available by UUID
      vmware_guest_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        folder: "/{{datacenter}}/vm"
        name: "{{ vm_name }}"
      delegate_to: localhost
      register: vm_facts

    - name: Get UUID from previous task and pass it to this task
      community.vmware.vmware_guest_tools_wait:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        uuid: "{{ vm_facts.instance.hw_product_uuid }}"
      delegate_to: localhost
      register: facts


    - name: Wait for VMware tools to become available by MoID
      community.vmware.vmware_guest_tools_wait:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        moid: vm-42
      delegate_to: localhost
      register: facts

    - name: Wait for VMware tools to become available by name
      community.vmware.vmware_guest_tools_wait:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: test-vm
        folder: "/{{datacenter}}/vm"
        datacenter: "{{ datacenter }}"
      delegate_to: localhost
      register: facts





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
      <div class="ansibleOptionAnchor" id="return-instance"></div>
      <p style="display: inline;"><strong>instance</strong></p>
      <a class="ansibleOptionLink" href="#return-instance" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>metadata about the virtual machine</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>&#34;None&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Philippe Dellaert (@pdellaert) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

