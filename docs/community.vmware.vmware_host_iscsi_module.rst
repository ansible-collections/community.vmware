

community.vmware.vmware_host_iscsi module -- Manage the iSCSI configuration of ESXi host
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_iscsi`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- In this module, can manage the iSCSI configuration of ESXi host








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th colspan="4"><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The ESXi hostname on which to change iSCSI settings.</p>
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The hostname or IP address of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config"></div>
      <p style="display: inline;"><strong>iscsi_config</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>The iSCSI configs.</p>
      <p>This parameter is required if <em>state=present</em> or <em>state=absent</em>.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/alias"></div>
      <p style="display: inline;"><strong>alias</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/alias" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The new value for the alias of the adapter.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication"></div>
      <p style="display: inline;"><strong>authentication</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>CHAP authentication parent settings for iSCSI.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication/chap_auth_enabled"></div>
      <p style="display: inline;"><strong>chap_auth_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication/chap_auth_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Whether to enable CHAP authentication.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication/chap_authentication_type"></div>
      <p style="display: inline;"><strong>chap_authentication_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication/chap_authentication_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;chapDiscouraged&#34;</code></p></li>
        <li><p><code>&#34;chapPreferred&#34;</code></p></li>
        <li><p><code>&#34;chapRequired&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;chapProhibited&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication/chap_name"></div>
      <p style="display: inline;"><strong>chap_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication/chap_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>CHAP user name if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication/chap_secret"></div>
      <p style="display: inline;"><strong>chap_secret</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication/chap_secret" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The secret password of CHAP if CHAP is enabled.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication/mutual_chap_authentication_type"></div>
      <p style="display: inline;"><strong>mutual_chap_authentication_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication/mutual_chap_authentication_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;chapProhibited&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;chapRequired&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication/mutual_chap_name"></div>
      <p style="display: inline;"><strong>mutual_chap_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication/mutual_chap_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/authentication/mutual_chap_secret"></div>
      <p style="display: inline;"><strong>mutual_chap_secret</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/authentication/mutual_chap_secret" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The secret password of mutual CHAP if Mutual-CHAP is enabled.</p>
    </td>
  </tr>

  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/force"></div>
      <p style="display: inline;"><strong>force</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/force" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Force port bind VMkernels to be removed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/iscsi_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/initiator_iqn"></div>
      <p style="display: inline;"><strong>iscsi_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/iscsi_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: initiator_iqn</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The name for the iSCSI HBA adapter.</p>
      <p>This is iSCSI qualified name.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/port_bind"></div>
      <p style="display: inline;"><strong>port_bind</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/port_bind" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>The list of the VMkernels if use port bindings.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target"></div>
      <p style="display: inline;"><strong>send_target</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>The iSCSI dynamic target settings.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/address"></div>
      <p style="display: inline;"><strong>address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The IP address or hostname of the storage device.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication"></div>
      <p style="display: inline;"><strong>authentication</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>CHAP authentication settings of a dynamic target for iSCSI.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/chap_auth_enabled"></div>
      <p style="display: inline;"><strong>chap_auth_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/chap_auth_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Whether to enable CHAP authentication.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/chap_authentication_type"></div>
      <p style="display: inline;"><strong>chap_authentication_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/chap_authentication_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;chapDiscouraged&#34;</code></p></li>
        <li><p><code>&#34;chapPreferred&#34;</code></p></li>
        <li><p><code>&#34;chapRequired&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;chapProhibited&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/chap_inherited"></div>
      <p style="display: inline;"><strong>chap_inherited</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/chap_inherited" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Whether or not to inherit CHAP settings from the parent settings.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/chap_name"></div>
      <p style="display: inline;"><strong>chap_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/chap_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>CHAP user name if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/chap_secret"></div>
      <p style="display: inline;"><strong>chap_secret</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/chap_secret" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The secret password of CHAP if CHAP is enabled.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/mutual_chap_authentication_type"></div>
      <p style="display: inline;"><strong>mutual_chap_authentication_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/mutual_chap_authentication_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;chapProhibited&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;chapRequired&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/mutual_chap_inherited"></div>
      <p style="display: inline;"><strong>mutual_chap_inherited</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/mutual_chap_inherited" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Whether or not to inherit Mutual-CHAP settings from the parent settings.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/mutual_chap_name"></div>
      <p style="display: inline;"><strong>mutual_chap_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/mutual_chap_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/authentication/mutual_chap_secret"></div>
      <p style="display: inline;"><strong>mutual_chap_secret</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/authentication/mutual_chap_secret" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The secret password of mutual CHAP if Mutual-CHAP is enabled.</p>
    </td>
  </tr>

  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/send_target/port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/send_target/port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The TCP port of the storage device.</p>
      <p>If not specified, the standard default of 3260 is used.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">3260</code></p>
    </td>
  </tr>

  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target"></div>
      <p style="display: inline;"><strong>static_target</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>The iSCSI static target settings.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/address"></div>
      <p style="display: inline;"><strong>address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The IP address or hostname of the storage device.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication"></div>
      <p style="display: inline;"><strong>authentication</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>CHAP authentication settings of a static target for iSCSI.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/chap_auth_enabled"></div>
      <p style="display: inline;"><strong>chap_auth_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/chap_auth_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Whether to enable CHAP authentication.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/chap_authentication_type"></div>
      <p style="display: inline;"><strong>chap_authentication_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/chap_authentication_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;chapDiscouraged&#34;</code></p></li>
        <li><p><code>&#34;chapPreferred&#34;</code></p></li>
        <li><p><code>&#34;chapRequired&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;chapProhibited&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/chap_inherited"></div>
      <p style="display: inline;"><strong>chap_inherited</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/chap_inherited" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Whether or not to inherit CHAP settings from the parent settings.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/chap_name"></div>
      <p style="display: inline;"><strong>chap_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/chap_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>CHAP user name if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/chap_secret"></div>
      <p style="display: inline;"><strong>chap_secret</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/chap_secret" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The secret password of CHAP if CHAP is enabled.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/mutual_chap_authentication_type"></div>
      <p style="display: inline;"><strong>mutual_chap_authentication_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/mutual_chap_authentication_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;chapProhibited&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;chapRequired&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/mutual_chap_inherited"></div>
      <p style="display: inline;"><strong>mutual_chap_inherited</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/mutual_chap_inherited" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Whether or not to inherit Mutual-CHAP settings from the parent settings.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/mutual_chap_name"></div>
      <p style="display: inline;"><strong>mutual_chap_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/mutual_chap_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/authentication/mutual_chap_secret"></div>
      <p style="display: inline;"><strong>mutual_chap_secret</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/authentication/mutual_chap_secret" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The secret password of mutual CHAP if Mutual-CHAP is enabled.</p>
    </td>
  </tr>

  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/iscsi_name"></div>
      <p style="display: inline;"><strong>iscsi_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/iscsi_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The name of the iSCSI target to connect to.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/static_target/port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/static_target/port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The TCP port of the storage device.</p>
      <p>If not specified, the standard default of 3260 is used.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">3260</code></p>
    </td>
  </tr>

  <tr>
    <td></td>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-iscsi_config/vmhba_name"></div>
      <p style="display: inline;"><strong>vmhba_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iscsi_config/vmhba_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The iSCSI adapter name.</p>
    </td>
  </tr>

  <tr>
    <td colspan="4">
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
    <td>
      <p>The password of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The port number of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Address of a proxy that will receive all HTTPS requests and relay them.</p>
      <p>The format is a hostname or a IP.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_HOST</code> will be used instead.</p>
      <p>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</p>
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>If set to <code class='docutils literal notranslate'>present</code>, add the iSCSI target or the bind ports if they are not existing.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code>, update the iSCSI settings if they already exist and occur change.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code>, remove the iSCSI target or the bind ports if they are existing.</p>
      <p>If set to (enabled), enable the iSCSI of ESXi if the iSCSI is disabled.</p>
      <p>If set to (disabled), disable the iSCSI of ESXi if the iSCSI is enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code>&#34;enabled&#34;</code></p></li>
        <li><p><code>&#34;disabled&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="4">
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
    <td>
      <p>The username of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td colspan="4">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
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

    
    - name: Enable iSCSI of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        state: enabled

    - name: Add a dynamic target to iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          send_target:
            address: "{{ send_target_address }}"
        state: present

    - name: Add a static target to iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          static_target:
            iscsi_name: iqn.2011-08.com.xxxxxxx:as6104t-8c3e9d.target001
            address: "{{ send_target_address }}"
        state: present

    - name: Add VMKernels to iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          port_bind:
            - vmk0
            - vmk1
        state: present

    - name: Use CHAP authentication
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          authentication:
            chap_auth_enabled: true
            chap_authentication_type: chapPreferred
            chap_name: chap_user_name
            chap_secret: secret
        state: present

    - name: Remove a dynamic target from iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          send_target:
            address: "{{ send_target_address }}"
        state: absent





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
    <td>
      <div class="ansibleOptionAnchor" id="return-iscsi_properties"></div>
      <p style="display: inline;"><strong>iscsi_properties</strong></p>
      <a class="ansibleOptionLink" href="#return-iscsi_properties" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Parameter return when system defaults config is changed.</p>
      <p style="margin-top: 8px;"><b>Returned:</b> changed</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;iscsi_alias&#34;: &#34;&#34;, &#34;iscsi_authentication_properties&#34;: {&#34;_vimtype&#34;: &#34;vim.host.InternetScsiHba.AuthenticationProperties&#34;, &#34;chapAuthEnabled&#34;: false, &#34;chapAuthenticationType&#34;: &#34;chapProhibited&#34;, &#34;chapInherited&#34;: null, &#34;chapName&#34;: &#34;&#34;, &#34;chapSecret&#34;: &#34;XXXXXXXXXXXXXXXXXXXXX&#34;, &#34;mutualChapAuthenticationType&#34;: &#34;chapProhibited&#34;, &#34;mutualChapInherited&#34;: null, &#34;mutualChapName&#34;: &#34;XXXXXXXXXXXXXXXXXXXXX&#34;, &#34;mutualChapSecret&#34;: &#34;&#34;}, &#34;iscsi_enabled&#34;: true, &#34;iscsi_name&#34;: &#34;&#34;, &#34;iscsi_send_targets&#34;: [], &#34;iscsi_static_targets&#34;: [], &#34;port_bind&#34;: [], &#34;vmhba_name&#34;: &#34;vmhba65&#34;}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

