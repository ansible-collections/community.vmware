

community.vmware.vmware_vcenter_settings module -- Configures general settings on a vCenter server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vcenter_settings`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure the vCenter server general settings (except the statistics).
- The statistics can be configured with the module \ :literal:`vmware\_vcenter\_statistics`\ .








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
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>A dictionary of advanced settings.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-database"></div>
      <p style="display: inline;"><strong>database</strong></p>
      <a class="ansibleOptionLink" href="#parameter-database" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>The database settings for vCenter server.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;event_cleanup&#34;: true, &#34;event_retention&#34;: 30, &#34;max_connections&#34;: 50, &#34;task_cleanup&#34;: true, &#34;task_retention&#34;: 30}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-database/event_cleanup"></div>
      <p style="display: inline;"><strong>event_cleanup</strong></p>
      <a class="ansibleOptionLink" href="#parameter-database/event_cleanup" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Event cleanup.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-database/event_retention"></div>
      <p style="display: inline;"><strong>event_retention</strong></p>
      <a class="ansibleOptionLink" href="#parameter-database/event_retention" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Event retention in days.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">30</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-database/max_connections"></div>
      <p style="display: inline;"><strong>max_connections</strong></p>
      <a class="ansibleOptionLink" href="#parameter-database/max_connections" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Maximum connections.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">50</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-database/task_cleanup"></div>
      <p style="display: inline;"><strong>task_cleanup</strong></p>
      <a class="ansibleOptionLink" href="#parameter-database/task_cleanup" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Task cleanup.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-database/task_retention"></div>
      <p style="display: inline;"><strong>task_retention</strong></p>
      <a class="ansibleOptionLink" href="#parameter-database/task_retention" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Task retention in days.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">30</code></p>
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
      <div class="ansibleOptionAnchor" id="parameter-logging_options"></div>
      <p style="display: inline;"><strong>logging_options</strong></p>
      <a class="ansibleOptionLink" href="#parameter-logging_options" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The level of detail that vCenter server usesfor log files.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;none&#34;</code></p></li>
        <li><p><code>&#34;error&#34;</code></p></li>
        <li><p><code>&#34;warning&#34;</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">&#34;info&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;verbose&#34;</code></p></li>
        <li><p><code>&#34;trivia&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mail"></div>
      <p style="display: inline;"><strong>mail</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mail" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>The settings vCenter server uses to send email alerts.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;sender&#34;: &#34;&#34;, &#34;server&#34;: &#34;&#34;}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mail/sender"></div>
      <p style="display: inline;"><strong>sender</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mail/sender" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Mail sender address.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mail/server"></div>
      <p style="display: inline;"><strong>server</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mail/server" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Mail server.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-runtime_settings"></div>
      <p style="display: inline;"><strong>runtime_settings</strong></p>
      <a class="ansibleOptionLink" href="#parameter-runtime_settings" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>The unique runtime settings for vCenter server.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-runtime_settings/managed_address"></div>
      <p style="display: inline;"><strong>managed_address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-runtime_settings/managed_address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>vCenter server managed address.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-runtime_settings/unique_id"></div>
      <p style="display: inline;"><strong>unique_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-runtime_settings/unique_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>vCenter server unique ID.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-runtime_settings/vcenter_server_name"></div>
      <p style="display: inline;"><strong>vcenter_server_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-runtime_settings/vcenter_server_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>vCenter server name. Default is FQDN.</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers"></div>
      <p style="display: inline;"><strong>snmp_receivers</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>SNMP trap destinations for vCenter server alerts.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;snmp_receiver_1_community&#34;: &#34;public&#34;, &#34;snmp_receiver_1_enabled&#34;: true, &#34;snmp_receiver_1_port&#34;: 162, &#34;snmp_receiver_1_url&#34;: &#34;localhost&#34;, &#34;snmp_receiver_2_community&#34;: &#34;&#34;, &#34;snmp_receiver_2_enabled&#34;: false, &#34;snmp_receiver_2_port&#34;: 162, &#34;snmp_receiver_2_url&#34;: &#34;&#34;, &#34;snmp_receiver_3_community&#34;: &#34;&#34;, &#34;snmp_receiver_3_enabled&#34;: false, &#34;snmp_receiver_3_port&#34;: 162, &#34;snmp_receiver_3_url&#34;: &#34;&#34;, &#34;snmp_receiver_4_community&#34;: &#34;&#34;, &#34;snmp_receiver_4_enabled&#34;: false, &#34;snmp_receiver_4_port&#34;: 162, &#34;snmp_receiver_4_url&#34;: &#34;&#34;}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_1_community"></div>
      <p style="display: inline;"><strong>snmp_receiver_1_community</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_1_community" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Community string.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;public&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_1_enabled"></div>
      <p style="display: inline;"><strong>snmp_receiver_1_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_1_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Enable receiver.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_1_port"></div>
      <p style="display: inline;"><strong>snmp_receiver_1_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_1_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Receiver port.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">162</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_1_url"></div>
      <p style="display: inline;"><strong>snmp_receiver_1_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_1_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Primary Receiver ULR.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;localhost&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_2_community"></div>
      <p style="display: inline;"><strong>snmp_receiver_2_community</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_2_community" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Community string.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_2_enabled"></div>
      <p style="display: inline;"><strong>snmp_receiver_2_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_2_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Enable receiver.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_2_port"></div>
      <p style="display: inline;"><strong>snmp_receiver_2_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_2_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Receiver port.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">162</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_2_url"></div>
      <p style="display: inline;"><strong>snmp_receiver_2_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_2_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Receiver 2 ULR.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_3_community"></div>
      <p style="display: inline;"><strong>snmp_receiver_3_community</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_3_community" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Community string.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_3_enabled"></div>
      <p style="display: inline;"><strong>snmp_receiver_3_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_3_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Enable receiver.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_3_port"></div>
      <p style="display: inline;"><strong>snmp_receiver_3_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_3_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Receiver port.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">162</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_3_url"></div>
      <p style="display: inline;"><strong>snmp_receiver_3_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_3_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Receiver 3 ULR.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_4_community"></div>
      <p style="display: inline;"><strong>snmp_receiver_4_community</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_4_community" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Community string.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_4_enabled"></div>
      <p style="display: inline;"><strong>snmp_receiver_4_enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_4_enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Enable receiver.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_4_port"></div>
      <p style="display: inline;"><strong>snmp_receiver_4_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_4_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Receiver port.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">162</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-snmp_receivers/snmp_receiver_4_url"></div>
      <p style="display: inline;"><strong>snmp_receiver_4_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snmp_receivers/snmp_receiver_4_url" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Receiver 4 ULR.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-timeout_settings"></div>
      <p style="display: inline;"><strong>timeout_settings</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout_settings" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>The vCenter server connection timeout for normal and long operations.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;long_operations&#34;: 120, &#34;normal_operations&#34;: 30}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-timeout_settings/long_operations"></div>
      <p style="display: inline;"><strong>long_operations</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout_settings/long_operations" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Long operation timeout.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">120</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-timeout_settings/normal_operations"></div>
      <p style="display: inline;"><strong>normal_operations</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout_settings/normal_operations" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Normal operation timeout.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">30</code></p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-user_directory"></div>
      <p style="display: inline;"><strong>user_directory</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_directory" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>The user directory settings for the vCenter server installation.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;query_limit&#34;: true, &#34;query_limit_size&#34;: 5000, &#34;timeout&#34;: 60, &#34;validation&#34;: true, &#34;validation_period&#34;: 1440}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-user_directory/query_limit"></div>
      <p style="display: inline;"><strong>query_limit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_directory/query_limit" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Query limit.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-user_directory/query_limit_size"></div>
      <p style="display: inline;"><strong>query_limit_size</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_directory/query_limit_size" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Query limit size.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">5000</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-user_directory/timeout"></div>
      <p style="display: inline;"><strong>timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_directory/timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>User directory timeout.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">60</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-user_directory/validation"></div>
      <p style="display: inline;"><strong>validation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_directory/validation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Mail Validation.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-user_directory/validation_period"></div>
      <p style="display: inline;"><strong>validation_period</strong></p>
      <a class="ansibleOptionLink" href="#parameter-user_directory/validation_period" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Validation period.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">1440</code></p>
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

    
    - name: Configure vCenter general settings
      community.vmware.vmware_vcenter_settings:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        database:
          max_connections: 50
          task_cleanup: true
          task_retention: 30
          event_cleanup: true
          event_retention: 30
        runtime_settings:
          unique_id: 1
          managed_address: "{{ lookup('dig', inventory_hostname) }}"
          vcenter_server_name: "{{ inventory_hostname }}"
        user_directory:
          timeout: 60
          query_limit: true
          query_limit_size: 5000
          validation: true
          validation_period: 1440
        mail:
          server: mail.example.com
          sender: vcenter@{{ inventory_hostname }}
        snmp_receivers:
          snmp_receiver_1_url: localhost
          snmp_receiver_1_enabled: true
          snmp_receiver_1_port: 162
          snmp_receiver_1_community: public
        timeout_settings:
          normal_operations: 30
          long_operations: 120
        logging_options: info
      delegate_to: localhost

    - name: Enable Retreat Mode for cluster with MOID domain-c8 (https://kb.vmware.com/kb/80472)
      community.vmware.vmware_vcenter_settings:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        advanced_settings:
          'config.vcls.clusters.domain-c8.enabled': 'false'
      delegate_to: localhost





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
      <div class="ansibleOptionAnchor" id="return-results"></div>
      <p style="display: inline;"><strong>results</strong></p>
      <a class="ansibleOptionLink" href="#return-results" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>metadata about vCenter settings</p>
      <p>supported diff mode from version 1.8.0</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Returned:</span> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>{&#34;changed&#34;: false, &#34;db_event_cleanup&#34;: true, &#34;db_event_retention&#34;: 30, &#34;db_max_connections&#34;: 50, &#34;db_task_cleanup&#34;: true, &#34;db_task_retention&#34;: 30, &#34;diff&#34;: {&#34;after&#34;: {&#34;db_event_cleanup&#34;: true, &#34;db_event_retention&#34;: 30, &#34;db_max_connections&#34;: 50, &#34;db_task_cleanup&#34;: true, &#34;db_task_retention&#34;: 30, &#34;directory_query_limit&#34;: true, &#34;directory_query_limit_size&#34;: 5000, &#34;directory_timeout&#34;: 60, &#34;directory_validation&#34;: true, &#34;directory_validation_period&#34;: 1440, &#34;logging_options&#34;: &#34;info&#34;, &#34;mail_sender&#34;: &#34;vcenter@vcenter01.example.com&#34;, &#34;mail_server&#34;: &#34;mail.example.com&#34;, &#34;runtime_managed_address&#34;: &#34;192.168.1.10&#34;, &#34;runtime_server_name&#34;: &#34;vcenter01.example.com&#34;, &#34;runtime_unique_id&#34;: 1, &#34;snmp_receiver_1_community&#34;: &#34;public&#34;, &#34;snmp_receiver_1_enabled&#34;: true, &#34;snmp_receiver_1_port&#34;: 162, &#34;snmp_receiver_1_url&#34;: &#34;localhost&#34;, &#34;snmp_receiver_2_community&#34;: &#34;&#34;, &#34;snmp_receiver_2_enabled&#34;: false, &#34;snmp_receiver_2_port&#34;: 162, &#34;snmp_receiver_2_url&#34;: &#34;&#34;, &#34;snmp_receiver_3_community&#34;: &#34;&#34;, &#34;snmp_receiver_3_enabled&#34;: false, &#34;snmp_receiver_3_port&#34;: 162, &#34;snmp_receiver_3_url&#34;: &#34;&#34;, &#34;snmp_receiver_4_community&#34;: &#34;&#34;, &#34;snmp_receiver_4_enabled&#34;: false, &#34;snmp_receiver_4_port&#34;: 162, &#34;snmp_receiver_4_url&#34;: &#34;&#34;, &#34;timeout_long_operations&#34;: 120, &#34;timeout_normal_operations&#34;: 30}, &#34;before&#34;: {&#34;db_event_cleanup&#34;: true, &#34;db_event_retention&#34;: 30, &#34;db_max_connections&#34;: 50, &#34;db_task_cleanup&#34;: true, &#34;db_task_retention&#34;: 30, &#34;directory_query_limit&#34;: true, &#34;directory_query_limit_size&#34;: 5000, &#34;directory_timeout&#34;: 60, &#34;directory_validation&#34;: true, &#34;directory_validation_period&#34;: 1440, &#34;logging_options&#34;: &#34;info&#34;, &#34;mail_sender&#34;: &#34;vcenter@vcenter01.example.com&#34;, &#34;mail_server&#34;: &#34;mail.example.com&#34;, &#34;runtime_managed_address&#34;: &#34;192.168.1.10&#34;, &#34;runtime_server_name&#34;: &#34;vcenter01.example.com&#34;, &#34;runtime_unique_id&#34;: 1, &#34;snmp_receiver_1_community&#34;: &#34;public&#34;, &#34;snmp_receiver_1_enabled&#34;: true, &#34;snmp_receiver_1_port&#34;: 162, &#34;snmp_receiver_1_url&#34;: &#34;localhost&#34;, &#34;snmp_receiver_2_community&#34;: &#34;&#34;, &#34;snmp_receiver_2_enabled&#34;: false, &#34;snmp_receiver_2_port&#34;: 162, &#34;snmp_receiver_2_url&#34;: &#34;&#34;, &#34;snmp_receiver_3_community&#34;: &#34;&#34;, &#34;snmp_receiver_3_enabled&#34;: false, &#34;snmp_receiver_3_port&#34;: 162, &#34;snmp_receiver_3_url&#34;: &#34;&#34;, &#34;snmp_receiver_4_community&#34;: &#34;&#34;, &#34;snmp_receiver_4_enabled&#34;: false, &#34;snmp_receiver_4_port&#34;: 162, &#34;snmp_receiver_4_url&#34;: &#34;&#34;, &#34;timeout_long_operations&#34;: 120, &#34;timeout_normal_operations&#34;: 30}}, &#34;directory_query_limit&#34;: true, &#34;directory_query_limit_size&#34;: 5000, &#34;directory_timeout&#34;: 60, &#34;directory_validation&#34;: true, &#34;directory_validation_period&#34;: 1440, &#34;logging_options&#34;: &#34;info&#34;, &#34;mail_sender&#34;: &#34;vcenter@vcenter01.example.com&#34;, &#34;mail_server&#34;: &#34;mail.example.com&#34;, &#34;msg&#34;: &#34;vCenter settings already configured properly&#34;, &#34;runtime_managed_address&#34;: &#34;192.168.1.10&#34;, &#34;runtime_server_name&#34;: &#34;vcenter01.example.com&#34;, &#34;runtime_unique_id&#34;: 1, &#34;timeout_long_operations&#34;: 120, &#34;timeout_normal_operations&#34;: 30}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

