

community.vmware.vmware_vc_infraprofile_info module -- List and Export VMware vCenter infra profile configs.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this module,
see `Requirements <ansible_collections.community.vmware.vmware_vc_infraprofile_info_module_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_vc_infraprofile_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Module to manage VMware vCenter infra profile configs.
- vCenter infra profile Library feature is introduced in vSphere 7.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_vc_infraprofile_info_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- vSphere Automation SDK






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
      <div class="ansibleOptionAnchor" id="parameter-api"></div>
      <p style="display: inline;"><strong>api</strong></p>
      <a class="ansibleOptionLink" href="#parameter-api" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>API which needs to be executed</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;export&#34;</code></p></li>
        <li><p><code>&#34;import&#34;</code></p></li>
        <li><p><code>&#34;list&#34;</code></p></li>
        <li><p><code>&#34;validate&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-config_path"></div>
      <p style="display: inline;"><strong>config_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-config_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Config file path which contains infra profile config JSON data, supports both relative and absolute path.</p>
      <p>This parameter is required only when <code class='docutils literal notranslate'>import</code>,<code class='docutils literal notranslate'>validate</code> APIs are being used.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-decryption_key"></div>
      <p style="display: inline;"><strong>decryption_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-decryption_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>decryption_key argument for while doing import profile task as of now its not taken into account form API team.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p style="display: inline;"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Description of about encryption or decryption key.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-encryption_key"></div>
      <p style="display: inline;"><strong>encryption_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-encryption_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>encryption_key argument for while doing import profile task as of now its not taken into account form API team.</p>
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
      <p>The hostname or IP address of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
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
      <p>The password of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
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
      <p>The port number of the vSphere vCenter.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-profiles"></div>
      <p style="display: inline;"><strong>profiles</strong></p>
      <a class="ansibleOptionLink" href="#parameter-profiles" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>A list of profile names to be exported, imported, and validated.</p>
      <p>This parameter is not required while running for List API, not for <code class='docutils literal notranslate'>export</code>,<code class='docutils literal notranslate'>import</code> and <code class='docutils literal notranslate'>validate</code>.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-protocol"></div>
      <p style="display: inline;"><strong>protocol</strong></p>
      <a class="ansibleOptionLink" href="#parameter-protocol" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The connection to protocol.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;http&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;https&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

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
      <p>The username of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
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
      <p>Allows connection when SSL certificates are not valid.</p>
      <p>Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_VALIDATE_CERTS</code> will be used instead.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Get information about VC infraprofile
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost

    - name: export vCenter appliance infra profile config
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        api: "export"
        profiles: "ApplianceManagement"
      delegate_to: localhost

    - name: validate vCenter appliance infra profile config
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        api: "validate"
        profiles: "ApplianceManagement"
        config_path: "export.json"

    - name: import vCenter appliance infra profile config
      vmware_vc_infraprofile_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        api: "import"
        profiles: "ApplianceManagement"
        config_path: "import.json"
      delegate_to: localhost
      




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
      <div class="ansibleOptionAnchor" id="return-export_infra"></div>
      <p style="display: inline;"><strong>export_infra</strong></p>
      <a class="ansibleOptionLink" href="#return-export_infra" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>A message about the exported file</p>
      <p style="margin-top: 8px;"><b>Returned:</b> On success with API set as "export"</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;export_config_json&#34;: &#34;json exported to file&#34;}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-import_profile"></div>
      <p style="display: inline;"><strong>import_profile</strong></p>
      <a class="ansibleOptionLink" href="#return-import_profile" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>A message about import on import_profile spec</p>
      <p style="margin-top: 8px;"><b>Returned:</b> On success with API set as "import"</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;changed&#34;: true, &#34;failed&#34;: false, &#34;status&#34;: &#34;0.0&#34;}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-list_infra"></div>
      <p style="display: inline;"><strong>list_infra</strong></p>
      <a class="ansibleOptionLink" href="#return-list_infra" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>A list of infra configs,</p>
      <p style="margin-top: 8px;"><b>Returned:</b> on success with API as "list"</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>[{&#34;info&#34;: &#34;ApplianceManagement&#34;, &#34;name&#34;: &#34;ApplianceManagement&#34;}, {&#34;info&#34;: &#34;ApplianceNetwork&#34;, &#34;name&#34;: &#34;ApplianceNetwork&#34;}, {&#34;info&#34;: &#34;Authentication &amp; Authorization Management&#34;, &#34;name&#34;: &#34;AuthManagement&#34;}]</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-validate_infra"></div>
      <p style="display: inline;"><strong>validate_infra</strong></p>
      <a class="ansibleOptionLink" href="#return-validate_infra" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>A message about validate on exported file</p>
      <p style="margin-top: 8px;"><b>Returned:</b> On success with API set as "validate"</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;changed&#34;: false, &#34;failed&#34;: false, &#34;status&#34;: &#34;VALID&#34;}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Naveenkumar G P (@ngp)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

