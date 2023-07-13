

community.vmware.vmware_host_kernel_manager module -- Manage kernel module options on ESXi hosts
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_kernel_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage kernel module options on ESXi hosts.
- All connected ESXi hosts in scope will be configured when specified.
- If a host is not connected at time of configuration, it will be marked as such in the output.
- Kernel module options may require a reboot to take effect which is not covered here.
- You can use \ `ansible.builtin.reboot <reboot_module.rst>`__\  or \ `community.vmware.vmware\_host\_powerstate <vmware_host_powerstate_module.rst>`__\  module to reboot all ESXi host systems.








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
      <div class="ansibleOptionAnchor" id="parameter-cluster_name"></div>
      <p style="display: inline;"><strong>cluster_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the VMware cluster to work on.</p>
      <p>All ESXi hosts in this cluster will be configured.</p>
      <p>This parameter is required if <code class='docutils literal notranslate'>esxi_hostname</code> is not specified.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the ESXi host to work on.</p>
      <p>This parameter is required if <code class='docutils literal notranslate'>cluster_name</code> is not specified.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-kernel_module_name"></div>
      <p style="display: inline;"><strong>kernel_module_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kernel_module_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the kernel module to be configured.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-kernel_module_option"></div>
      <p style="display: inline;"><strong>kernel_module_option</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kernel_module_option" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Specified configurations will be applied to the given module.</p>
      <p>These values are specified in key=value pairs and separated by a space when there are multiple options.</p>
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

    
    - name: Configure IPv6 to be off via tcpip4 kernel module
      community.vmware.vmware_host_kernel_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        kernel_module_name: "tcpip4"
        kernel_module_option: "ipv6=0"

    - name: Using cluster_name, configure vmw_psp_rr options
      community.vmware.vmware_host_kernel_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: '{{ virtual_cluster_name }}'
        kernel_module_name: "vmw_psp_rr"
        kernel_module_option: "maxPathsPerDevice=2"





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
      <div class="ansibleOptionAnchor" id="return-host_kernel_status"></div>
      <p style="display: inline;"><strong>host_kernel_status</strong></p>
      <a class="ansibleOptionLink" href="#return-host_kernel_status" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>dict with information on what was changed, by ESXi host in scope.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;results&#34;: {&#34;myhost01.example.com&#34;: {&#34;changed&#34;: true, &#34;configured_options&#34;: &#34;ipv6=0&#34;, &#34;msg&#34;: &#34;Options have been changed on the kernel module&#34;, &#34;original_options&#34;: &#34;ipv6=1&#34;}}}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Aaron Longchamps (@alongchamps)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

