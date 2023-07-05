

community.vmware.vmware_vswitch module -- Manage a VMware Standard Switch to an ESXi host.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vswitch`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add, remove and update a VMware Standard Switch to an ESXi host.








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
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <div class="ansibleOptionAnchor" id="parameter-host"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: host</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Manage the vSwitch using this ESXi host system.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
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
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-mtu"></div>
      <p style="display: inline;"><strong>mtu</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mtu" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>MTU to configure on vSwitch.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">1500</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-nics"></div>
      <div class="ansibleOptionAnchor" id="parameter-nic_name"></div>
      <p style="display: inline;"><strong>nics</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nics" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: nic_name</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>A list of vmnic names or vmnic name to attach to vSwitch.</p>
      <p>Alias <code class='docutils literal notranslate'>nics</code> is added in version 2.4.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-number_of_ports"></div>
      <p style="display: inline;"><strong>number_of_ports</strong></p>
      <a class="ansibleOptionLink" href="#parameter-number_of_ports" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Number of port to configure on vSwitch.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">128</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
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
    <td colspan="2">
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
    <td colspan="2">
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
    <td colspan="2">
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
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-security"></div>
      <div class="ansibleOptionAnchor" id="parameter-security_policy"></div>
      <div class="ansibleOptionAnchor" id="parameter-network_policy"></div>
      <p style="display: inline;"><strong>security</strong></p>
      <a class="ansibleOptionLink" href="#parameter-security" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: security_policy, network_policy</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.4.0</i></p>
    </td>
    <td>
      <p>Network policy specifies layer 2 security settings for a portgroup such as promiscuous mode, where guest adapter listens to all the packets, MAC address changes and forged transmits.</p>
      <p>Dict which configures the different security values for portgroup.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-security/forged_transmits"></div>
      <div class="ansibleOptionAnchor" id="parameter-security_policy/forged_transmits"></div>
      <div class="ansibleOptionAnchor" id="parameter-network_policy/forged_transmits"></div>
      <p style="display: inline;"><strong>forged_transmits</strong></p>
      <a class="ansibleOptionLink" href="#parameter-security/forged_transmits" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicates whether forged transmits are allowed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-security/mac_changes"></div>
      <div class="ansibleOptionAnchor" id="parameter-security_policy/mac_changes"></div>
      <div class="ansibleOptionAnchor" id="parameter-network_policy/mac_changes"></div>
      <p style="display: inline;"><strong>mac_changes</strong></p>
      <a class="ansibleOptionLink" href="#parameter-security/mac_changes" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicates whether mac changes are allowed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-security/promiscuous_mode"></div>
      <div class="ansibleOptionAnchor" id="parameter-security_policy/promiscuous_mode"></div>
      <div class="ansibleOptionAnchor" id="parameter-network_policy/promiscuous_mode"></div>
      <p style="display: inline;"><strong>promiscuous_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-security/promiscuous_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicates whether promiscuous mode is allowed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Add or remove the switch.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-switch"></div>
      <div class="ansibleOptionAnchor" id="parameter-switch_name"></div>
      <p style="display: inline;"><strong>switch</strong></p>
      <a class="ansibleOptionLink" href="#parameter-switch" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: switch_name</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>vSwitch name to add.</p>
      <p>Alias <code class='docutils literal notranslate'>switch</code> is added in version 2.4.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-teaming"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy"></div>
      <p style="display: inline;"><strong>teaming</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: teaming_policy</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.4.0</i></p>
    </td>
    <td>
      <p>Dictionary which configures the different teaming values for portgroup.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-teaming/active_adapters"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/active_adapters"></div>
      <p style="display: inline;"><strong>active_adapters</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming/active_adapters" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>List of active adapters used for load balancing.</p>
      <p>All vmnics are used as active adapters if <code class='docutils literal notranslate'>active_adapters</code> and <code class='docutils literal notranslate'>standby_adapters</code> are not defined.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-teaming/failback"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/failback"></div>
      <p style="display: inline;"><strong>failback</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming/failback" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicate whether or not to use a failback when restoring links.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-teaming/load_balancing"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/load_balancing"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming/load_balance_policy"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/load_balance_policy"></div>
      <p style="display: inline;"><strong>load_balancing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming/load_balancing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: load_balance_policy</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Network adapter teaming policy.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;loadbalance_ip&#34;</code></p></li>
        <li><p><code>&#34;loadbalance_srcmac&#34;</code></p></li>
        <li><p><code>&#34;loadbalance_srcid&#34;</code></p></li>
        <li><p><code>&#34;failover_explicit&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-teaming/network_failure_detection"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/network_failure_detection"></div>
      <p style="display: inline;"><strong>network_failure_detection</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming/network_failure_detection" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Network failure detection.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;link_status_only&#34;</code></p></li>
        <li><p><code>&#34;beacon_probing&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-teaming/notify_switches"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/notify_switches"></div>
      <p style="display: inline;"><strong>notify_switches</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming/notify_switches" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicate whether or not to notify the physical switch if a link fails.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-teaming/standby_adapters"></div>
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/standby_adapters"></div>
      <p style="display: inline;"><strong>standby_adapters</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming/standby_adapters" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>List of standby adapters used for failover.</p>
      <p>All vmnics are used as active adapters if <code class='docutils literal notranslate'>active_adapters</code> and <code class='docutils literal notranslate'>standby_adapters</code> are not defined.</p>
    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-traffic_shaping"></div>
      <p style="display: inline;"><strong>traffic_shaping</strong></p>
      <a class="ansibleOptionLink" href="#parameter-traffic_shaping" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.4.0</i></p>
    </td>
    <td>
      <p>Dictionary which configures traffic shaping for the switch.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-traffic_shaping/average_bandwidth"></div>
      <p style="display: inline;"><strong>average_bandwidth</strong></p>
      <a class="ansibleOptionLink" href="#parameter-traffic_shaping/average_bandwidth" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Average bandwidth (kbit/s).</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-traffic_shaping/burst_size"></div>
      <p style="display: inline;"><strong>burst_size</strong></p>
      <a class="ansibleOptionLink" href="#parameter-traffic_shaping/burst_size" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Burst size (KB).</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-traffic_shaping/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-traffic_shaping/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Status of Traffic Shaping Policy.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-traffic_shaping/peak_bandwidth"></div>
      <p style="display: inline;"><strong>peak_bandwidth</strong></p>
      <a class="ansibleOptionLink" href="#parameter-traffic_shaping/peak_bandwidth" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Peak bandwidth (kbit/s).</p>
    </td>
  </tr>

  <tr>
    <td colspan="2">
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
    <td colspan="2">
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

    
    - name: Add a VMware vSwitch
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        switch: vswitch_name
        nics: vmnic_name
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch without any physical NIC attached
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        switch: vswitch_0001
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch with multiple NICs
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        switch: vmware_vswitch_0004
        nics:
        - vmnic1
        - vmnic2
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name: vmnic0
        mtu: 9000
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system with Promiscuous Mode Enabled
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name: vmnic0
        mtu: 9000
        security:
            promiscuous_mode: true
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system with active/standby teaming
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name:
          - vmnic0
          - vmnic1
        teaming:
          active_adapters:
            - vmnic0
          standby_adapters:
            - vmnic1
      delegate_to: localhost

    - name: Add a VMware vSwitch to a specific host system with traffic shaping
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        nic_name:
          - vmnic0
          - vmnic1
        traffic_shaping:
            enabled: true
            average_bandwidth: 100000
            peak_bandwidth: 100000
            burst_size: 102400
      delegate_to: localhost

    - name: Delete a VMware vSwitch in a specific host system
      community.vmware.vmware_vswitch:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        esxi_hostname: DC0_H0
        switch_name: vswitch_001
        state: absent
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
    <td>
      <div class="ansibleOptionAnchor" id="return-result"></div>
      <p style="display: inline;"><strong>result</strong></p>
      <a class="ansibleOptionLink" href="#return-result" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>information about performed operation</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>&#34;vSwitch &#39;vSwitch_1002&#39; is created successfully&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

