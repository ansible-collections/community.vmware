

community.vmware.vmware_dvswitch module -- Create or remove a Distributed Switch
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_dvswitch`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to create, remove a Distributed Switch.








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
      <div class="ansibleOptionAnchor" id="parameter-contact"></div>
      <p style="display: inline;"><strong>contact</strong></p>
      <a class="ansibleOptionLink" href="#parameter-contact" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Dictionary which configures administrator contact name and description for the Distributed Switch.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-contact/description"></div>
      <p style="display: inline;"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-contact/description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Description or other details.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-contact/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-contact/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Administrator name.</p>
    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-datacenter_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: datacenter</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The name of the datacenter that will contain the Distributed Switch.</p>
      <p>This parameter is optional, if <code class='docutils literal notranslate'>folder</code> is provided.</p>
      <p>Mutually exclusive with <code class='docutils literal notranslate'>folder</code> parameter.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p style="display: inline;"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Description of the Distributed Switch.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-discovery_operation"></div>
      <p style="display: inline;"><strong>discovery_operation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-discovery_operation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Select the discovery operation.</p>
      <p>Required parameter for <code class='docutils literal notranslate'>state</code> both <code class='docutils literal notranslate'>present</code> and <code class='docutils literal notranslate'>absent</code>, before Ansible 2.6 version.</p>
      <p>Required only if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>, for Ansible 2.6 and onwards.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;both&#34;</code></p></li>
        <li><p><code>&#34;advertise&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;listen&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-discovery_proto"></div>
      <div class="ansibleOptionAnchor" id="parameter-discovery_protocol"></div>
      <p style="display: inline;"><strong>discovery_proto</strong></p>
      <a class="ansibleOptionLink" href="#parameter-discovery_proto" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: discovery_protocol</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Link discovery protocol between Cisco and Link Layer discovery.</p>
      <p>Required parameter for <code class='docutils literal notranslate'>state</code> both <code class='docutils literal notranslate'>present</code> and <code class='docutils literal notranslate'>absent</code>, before Ansible 2.6 version.</p>
      <p>Required only if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>, for Ansible 2.6 and onwards.</p>
      <p><code class='docutils literal notranslate'>cdp</code>: Use Cisco Discovery Protocol (CDP).</p>
      <p><code class='docutils literal notranslate'>lldp</code>: Use Link Layer Discovery Protocol (LLDP).</p>
      <p><code class='docutils literal notranslate'>disabled</code>: Do not use a discovery protocol.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;cdp&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;lldp&#34;</code></p></li>
        <li><p><code>&#34;disabled&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Destination folder, absolute path to place dvswitch in.</p>
      <p>The folder should include the datacenter.</p>
      <p>This parameter is case sensitive.</p>
      <p>This parameter is optional, if <code class='docutils literal notranslate'>datacenter</code> is provided.</p>
      <p>Examples:</p>
      <p>   folder: /datacenter1/network</p>
      <p>   folder: datacenter1/network</p>
      <p>   folder: /datacenter1/network/folder1</p>
      <p>   folder: datacenter1/network/folder1</p>
      <p>   folder: /folder1/datacenter1/network</p>
      <p>   folder: folder1/datacenter1/network</p>
      <p>   folder: /folder1/datacenter1/network/folder2</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-health_check"></div>
      <p style="display: inline;"><strong>health_check</strong></p>
      <a class="ansibleOptionLink" href="#parameter-health_check" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Dictionary which configures Health Check for the Distributed Switch.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">{&#34;teaming_failover&#34;: false, &#34;teaming_failover_interval&#34;: 0, &#34;vlan_mtu&#34;: false, &#34;vlan_mtu_interval&#34;: 0}</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-health_check/teaming_failover"></div>
      <p style="display: inline;"><strong>teaming_failover</strong></p>
      <a class="ansibleOptionLink" href="#parameter-health_check/teaming_failover" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Teaming and failover health check.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-health_check/teaming_failover_interval"></div>
      <p style="display: inline;"><strong>teaming_failover_interval</strong></p>
      <a class="ansibleOptionLink" href="#parameter-health_check/teaming_failover_interval" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Teaming and failover health check interval (minutes).</p>
      <p>The default value is 1 in the vSphere Client if the Teaming and failover health check is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">0</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-health_check/vlan_mtu"></div>
      <p style="display: inline;"><strong>vlan_mtu</strong></p>
      <a class="ansibleOptionLink" href="#parameter-health_check/vlan_mtu" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>VLAN and MTU health check.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-health_check/vlan_mtu_interval"></div>
      <p style="display: inline;"><strong>vlan_mtu_interval</strong></p>
      <a class="ansibleOptionLink" href="#parameter-health_check/vlan_mtu_interval" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>VLAN and MTU health check interval (minutes).</p>
      <p>The default value is 1 in the vSphere Client if the VLAN and MTU health check is enabled.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">0</code></p>
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
      <p>The switch maximum transmission unit.</p>
      <p>Required parameter for <code class='docutils literal notranslate'>state</code> both <code class='docutils literal notranslate'>present</code> and <code class='docutils literal notranslate'>absent</code>, before Ansible 2.6 version.</p>
      <p>Required only if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>, for Ansible 2.6 and onwards.</p>
      <p>Accepts value between 1280 to 9000 (both inclusive).</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">1500</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-multicast_filtering_mode"></div>
      <p style="display: inline;"><strong>multicast_filtering_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-multicast_filtering_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The multicast filtering mode.</p>
      <p><code class='docutils literal notranslate'>basic</code> mode: multicast traffic for virtual machines is forwarded according to the destination MAC address of the multicast group.</p>
      <p><code class='docutils literal notranslate'>snooping</code> mode: the Distributed Switch provides IGMP and MLD snooping according to RFC 4541.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;basic&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;snooping&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-net_flow"></div>
      <p style="display: inline;"><strong>net_flow</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.7.0</i></p>
    </td>
    <td>
      <p>Dictionary which configures the Net Flow for the Distributed Switch.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">{&#34;active_flow_timeout&#34;: 60, &#34;collector_port&#34;: 0, &#34;idle_flow_timeout&#34;: 15, &#34;internal_flows_only&#34;: false, &#34;observation_domain_id&#34;: 0, &#34;sampling_rate&#34;: 4096}</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-net_flow/active_flow_timeout"></div>
      <p style="display: inline;"><strong>active_flow_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow/active_flow_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The time, in seconds, to wait before sending information after the flow is initiated.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">60</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-net_flow/collector_ip"></div>
      <p style="display: inline;"><strong>collector_ip</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow/collector_ip" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The IP Address (IPv4 or IPv6) of the NetFlow collector.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-net_flow/collector_port"></div>
      <p style="display: inline;"><strong>collector_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow/collector_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The Port of the NetFlow collector.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">0</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-net_flow/idle_flow_timeout"></div>
      <p style="display: inline;"><strong>idle_flow_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow/idle_flow_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The time, in seconds, to wait before sending information after the flow is initiated.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">15</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-net_flow/internal_flows_only"></div>
      <p style="display: inline;"><strong>internal_flows_only</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow/internal_flows_only" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>If True, data on network activity between vms on the same host will be collected only.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-net_flow/observation_domain_id"></div>
      <p style="display: inline;"><strong>observation_domain_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow/observation_domain_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Identifies the information related to the switch.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">0</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-net_flow/sampling_rate"></div>
      <p style="display: inline;"><strong>sampling_rate</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow/sampling_rate" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The portion of data that the switch collects.</p>
      <p>The sampling rate represents the number of packets that NetFlow drops after every collected packet.</p>
      <p>If the rate is 0, NetFlow samples every packet, that is, collect one packet and drop none.</p>
      <p>If the rate is 1, NetFlow samples a packet and drops the next one, and so on.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">4096</code></p>
    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-network_policy"></div>
      <p style="display: inline;"><strong>network_policy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Dictionary which configures the different default security values for portgroups.</p>
      <p>If set, these options are inherited by the portgroups of the DVS.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-network_policy/forged_transmits"></div>
      <p style="display: inline;"><strong>forged_transmits</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy/forged_transmits" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicates whether forged transmits are allowed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-network_policy/mac_changes"></div>
      <p style="display: inline;"><strong>mac_changes</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy/mac_changes" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicates whether mac changes are allowed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-network_policy/promiscuous"></div>
      <p style="display: inline;"><strong>promiscuous</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy/promiscuous" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Indicates whether promiscuous mode is allowed.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

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
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>If set to <code class='docutils literal notranslate'>present</code> and the Distributed Switch does not exist, the Distributed Switch will be created.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code> and the Distributed Switch exists, the Distributed Switch will be deleted.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-switch_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-switch"></div>
      <div class="ansibleOptionAnchor" id="parameter-dvswitch"></div>
      <p style="display: inline;"><strong>switch_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-switch_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: switch, dvswitch</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The name of the distribute vSwitch to create or remove.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-switch_version"></div>
      <div class="ansibleOptionAnchor" id="parameter-version"></div>
      <p style="display: inline;"><strong>switch_version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-switch_version" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: version</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The version of the Distributed Switch to create.</p>
      <p>The version must match the version of the ESXi hosts you want to connect.</p>
      <p>The version of the vCenter server is used if not specified.</p>
      <p>Required only if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-uplink_prefix"></div>
      <p style="display: inline;"><strong>uplink_prefix</strong></p>
      <a class="ansibleOptionLink" href="#parameter-uplink_prefix" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The prefix used for the naming of the uplinks.</p>
      <p>Only valid if the Distributed Switch will be created. Not used if the Distributed Switch is already present.</p>
      <p>Uplinks are created as Uplink 1, Uplink 2, etc. pp. by default.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;Uplink &#34;</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-uplink_quantity"></div>
      <p style="display: inline;"><strong>uplink_quantity</strong></p>
      <a class="ansibleOptionLink" href="#parameter-uplink_quantity" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Quantity of uplink per ESXi host added to the Distributed Switch.</p>
      <p>The uplink quantity can be increased or decreased, but a decrease will only be successfull if the uplink isn&#x27;t used by a portgroup.</p>
      <p>Required parameter for <code class='docutils literal notranslate'>state</code> both <code class='docutils literal notranslate'>present</code> and <code class='docutils literal notranslate'>absent</code>, before Ansible 2.6 version.</p>
      <p>Required only if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>, for Ansible 2.6 and onwards.</p>
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

    
    - name: Create dvSwitch
      community.vmware.vmware_dvswitch:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: '{{ datacenter }}'
        switch: dvSwitch
        version: 6.0.0
        mtu: 9000
        uplink_quantity: 2
        discovery_protocol: lldp
        discovery_operation: both
        state: present
      delegate_to: localhost

    - name: Create dvSwitch with all options
      community.vmware.vmware_dvswitch:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: '{{ datacenter }}'
        switch: dvSwitch
        version: 6.5.0
        mtu: 9000
        uplink_quantity: 2
        uplink_prefix: 'Uplink_'
        discovery_protocol: cdp
        discovery_operation: both
        multicast_filtering_mode: snooping
        health_check:
          vlan_mtu: true
          vlan_mtu_interval: 1
          teaming_failover: true
          teaming_failover_interval: 1
        net_flow:
            collector_ip: 192.168.10.50
            collector_port: 50034
            observation_domain_id: 0
            active_flow_timeout: 60
            idle_flow_timeout: 15
            sampling_rate: 4096
            internal_flows_only: false
        state: present
      delegate_to: localhost

    - name: Delete dvSwitch
      community.vmware.vmware_dvswitch:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: '{{ datacenter }}'
        switch: dvSwitch
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
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>&#34;{&#39;changed&#39;: False, &#39;contact&#39;: None, &#39;contact_details&#39;: None, &#39;description&#39;: None, &#39;discovery_operation&#39;: &#39;both&#39;, &#39;discovery_protocol&#39;: &#39;cdp&#39;, &#39;dvswitch&#39;: &#39;test&#39;, &#39;health_check_teaming&#39;: False, &#39;health_check_teaming_interval&#39;: 0, &#39;health_check_vlan&#39;: False, &#39;health_check_vlan_interval&#39;: 0, &#39;mtu&#39;: 9000, &#39;multicast_filtering_mode&#39;: &#39;basic&#39;, &#39;net_flow_active_flow_timeout&#39;: 60, &#39;net_flow_collector_ip&#39;: &#39;192.168.10.50&#39;, &#39;net_flow_collector_port&#39;: 50034, &#39;net_flow_idle_flow_timeout&#39;: 15, &#39;net_flow_internal_flows_only&#39;: False, &#39;net_flow_observation_domain_id&#39;: 0, &#39;net_flow_sampling_rate&#39;: 4096, &#39;result&#39;: &#39;DVS already configured properly&#39;, &#39;uplink_quantity&#39;: 2, &#39;uplinks&#39;: [&#39;Uplink_1&#39;, &#39;Uplink_2&#39;], &#39;version&#39;: &#39;6.6.0&#39;}&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

