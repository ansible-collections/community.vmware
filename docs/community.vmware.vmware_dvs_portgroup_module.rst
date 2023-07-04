

community.vmware.vmware_dvs_portgroup module -- Create or remove a Distributed vSwitch portgroup.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_dvs_portgroup`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Create or remove a Distributed vSwitch portgroup.








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
      <div class="ansibleOptionAnchor" id="parameter-in_traffic_shaping"></div>
      <p style="display: inline;"><strong>in_traffic_shaping</strong></p>
      <a class="ansibleOptionLink" href="#parameter-in_traffic_shaping" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 2.3.0</span></p>
    </div></td>
    <td>
      <p>Dictionary which configures the ingress traffic shaping settings for the portgroup.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-in_traffic_shaping/average_bandwidth"></div>
      <p style="display: inline;"><strong>average_bandwidth</strong></p>
      <a class="ansibleOptionLink" href="#parameter-in_traffic_shaping/average_bandwidth" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Establishes the number of bits per second to allow across a port, averaged over time, that is, the allowed average load.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-in_traffic_shaping/burst_size"></div>
      <p style="display: inline;"><strong>burst_size</strong></p>
      <a class="ansibleOptionLink" href="#parameter-in_traffic_shaping/burst_size" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The maximum number of bits per second to allow across a port when it is sending/sending or receiving a burst of traffic.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-in_traffic_shaping/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-in_traffic_shaping/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether ingress traffic shaping is activated or not.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-in_traffic_shaping/inherited"></div>
      <p style="display: inline;"><strong>inherited</strong></p>
      <a class="ansibleOptionLink" href="#parameter-in_traffic_shaping/inherited" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>Inherit the settings from the switch or not.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-in_traffic_shaping/peak_bandwidth"></div>
      <p style="display: inline;"><strong>peak_bandwidth</strong></p>
      <a class="ansibleOptionLink" href="#parameter-in_traffic_shaping/peak_bandwidth" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The maximum number of bytes to allow in a burst.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mac_learning"></div>
      <p style="display: inline;"><strong>mac_learning</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mac_learning" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Dictionary which configures MAC learning for portgroup.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mac_learning/allow_unicast_flooding"></div>
      <p style="display: inline;"><strong>allow_unicast_flooding</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mac_learning/allow_unicast_flooding" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>The flag to allow flooding of unlearned MAC for ingress traffic.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mac_learning/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mac_learning/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>The flag to indicate if source MAC address learning is allowed.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mac_learning/limit"></div>
      <p style="display: inline;"><strong>limit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mac_learning/limit" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The maximum number of MAC addresses that can be learned.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-mac_learning/limit_policy"></div>
      <p style="display: inline;"><strong>limit_policy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mac_learning/limit_policy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The default switching policy after MAC limit is exceeded.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;allow&#34;</code></p></li>
        <li><p><code>&#34;drop&#34;</code></p></li>
      </ul>

    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-net_flow"></div>
      <p style="display: inline;"><strong>net_flow</strong></p>
      <a class="ansibleOptionLink" href="#parameter-net_flow" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 2.3.0</span></p>
    </div></td>
    <td>
      <p>Indicate whether or not the virtual machine IP traffic that flows through a vds gets analyzed by sending reports to a NetFlow collector.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;true&#34;</code></p></li>
        <li><p><code>&#34;on&#34;</code></p></li>
        <li><p><code>&#34;yes&#34;</code></p></li>
        <li><p><code>&#34;false&#34;</code></p></li>
        <li><p><code>&#34;off&#34;</code></p></li>
        <li><p><code>&#34;no&#34;</code></p></li>
        <li><p><code>&#34;inherited&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-network_policy"></div>
      <p style="display: inline;"><strong>network_policy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Dictionary which configures the different security values for portgroup.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-network_policy/forged_transmits"></div>
      <p style="display: inline;"><strong>forged_transmits</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy/forged_transmits" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether forged transmits are allowed. Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-network_policy/inherited"></div>
      <p style="display: inline;"><strong>inherited</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy/inherited" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>Inherit the settings from the switch or not.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-network_policy/mac_changes"></div>
      <p style="display: inline;"><strong>mac_changes</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy/mac_changes" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether mac changes are allowed. Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-network_policy/promiscuous"></div>
      <p style="display: inline;"><strong>promiscuous</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_policy/promiscuous" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether promiscuous mode is allowed. Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-num_ports"></div>
      <p style="display: inline;"><strong>num_ports</strong></p>
      <a class="ansibleOptionLink" href="#parameter-num_ports" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The number of ports the portgroup should contain.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-out_traffic_shaping"></div>
      <p style="display: inline;"><strong>out_traffic_shaping</strong></p>
      <a class="ansibleOptionLink" href="#parameter-out_traffic_shaping" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
      <p><span style="font-style: italic; font-size: small; color: darkgreen;">added in community.vmware 2.3.0</span></p>
    </div></td>
    <td>
      <p>Dictionary which configures the egress traffic shaping settings for the portgroup.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-out_traffic_shaping/average_bandwidth"></div>
      <p style="display: inline;"><strong>average_bandwidth</strong></p>
      <a class="ansibleOptionLink" href="#parameter-out_traffic_shaping/average_bandwidth" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Establishes the number of bits per second to allow across a port, averaged over time, that is, the allowed average load.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-out_traffic_shaping/burst_size"></div>
      <p style="display: inline;"><strong>burst_size</strong></p>
      <a class="ansibleOptionLink" href="#parameter-out_traffic_shaping/burst_size" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The maximum number of bits per second to allow across a port when it is sending/sending or receiving a burst of traffic.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-out_traffic_shaping/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-out_traffic_shaping/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether egress traffic shaping is activated or not.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-out_traffic_shaping/inherited"></div>
      <p style="display: inline;"><strong>inherited</strong></p>
      <a class="ansibleOptionLink" href="#parameter-out_traffic_shaping/inherited" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>Inherit the settings from the switch or not.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-out_traffic_shaping/peak_bandwidth"></div>
      <p style="display: inline;"><strong>peak_bandwidth</strong></p>
      <a class="ansibleOptionLink" href="#parameter-out_traffic_shaping/peak_bandwidth" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The maximum number of bytes to allow in a burst.</p>
      <p>Ignored if <code class='docutils literal notranslate'>inherited</code> is true.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-port_allocation"></div>
      <p style="display: inline;"><strong>port_allocation</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_allocation" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Elastic port groups automatically increase or decrease the number of ports as needed.</p>
      <p>Only valid if <em>port_binding</em> is set to <code class='docutils literal notranslate'>static</code>.</p>
      <p>Will be <code class='docutils literal notranslate'>elastic</code> if not specified and <em>port_binding</em> is set to <code class='docutils literal notranslate'>static</code>.</p>
      <p>Will be <code class='docutils literal notranslate'>fixed</code> if not specified and <em>port_binding</em> is set to <code class='docutils literal notranslate'>ephemeral</code>.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;elastic&#34;</code></p></li>
        <li><p><code>&#34;fixed&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_binding"></div>
      <p style="display: inline;"><strong>port_binding</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_binding" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The type of port binding determines when ports in a port group are assigned to virtual machines.</p>
      <p>See VMware KB 1022312 <a href='https://kb.vmware.com/s/article/1022312'>https://kb.vmware.com/s/article/1022312</a> for more details.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;static&#34;</code></p></li>
        <li><p><code>&#34;ephemeral&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy"></div>
      <p style="display: inline;"><strong>port_policy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Dictionary which configures the advanced policy settings for the portgroup.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;block_override&#34;: true, &#34;ipfix_override&#34;: false, &#34;live_port_move&#34;: false, &#34;mac_management_override&#34;: false, &#34;network_rp_override&#34;: false, &#34;port_config_reset_at_disconnect&#34;: true, &#34;shaping_override&#34;: false, &#34;traffic_filter_override&#34;: false, &#34;uplink_teaming_override&#34;: false, &#34;vendor_config_override&#34;: false, &#34;vlan_override&#34;: false}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/block_override"></div>
      <p style="display: inline;"><strong>block_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/block_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the block policy can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/ipfix_override"></div>
      <p style="display: inline;"><strong>ipfix_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/ipfix_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the ipfix policy can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/live_port_move"></div>
      <p style="display: inline;"><strong>live_port_move</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/live_port_move" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if a live port can be moved in or out of the portgroup.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/mac_management_override"></div>
      <div class="ansibleOptionAnchor" id="parameter-port_policy/security_override"></div>
      <p style="display: inline;"><strong>mac_management_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/mac_management_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: security_override</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the security policy can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/network_rp_override"></div>
      <p style="display: inline;"><strong>network_rp_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/network_rp_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the network resource pool can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/port_config_reset_at_disconnect"></div>
      <p style="display: inline;"><strong>port_config_reset_at_disconnect</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/port_config_reset_at_disconnect" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the configuration of a port is reset automatically after disconnect.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/shaping_override"></div>
      <p style="display: inline;"><strong>shaping_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/shaping_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the shaping policy can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/traffic_filter_override"></div>
      <p style="display: inline;"><strong>traffic_filter_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/traffic_filter_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the traffic filter can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/uplink_teaming_override"></div>
      <p style="display: inline;"><strong>uplink_teaming_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/uplink_teaming_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the uplink teaming policy can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/vendor_config_override"></div>
      <p style="display: inline;"><strong>vendor_config_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/vendor_config_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the vendor config can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port_policy/vlan_override"></div>
      <p style="display: inline;"><strong>vlan_override</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port_policy/vlan_override" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates if the vlan can be changed per port.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-portgroup_name"></div>
      <p style="display: inline;"><strong>portgroup_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-portgroup_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The name of the portgroup that is to be created or deleted.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>Determines if the portgroup should be present or not.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;present&#34;</code></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-switch_name"></div>
      <p style="display: inline;"><strong>switch_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-switch_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The name of the distributed vSwitch the port group should be created on.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy"></div>
      <p style="display: inline;"><strong>teaming_policy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming_policy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Dictionary which configures the different teaming values for portgroup.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;load_balance_policy&#34;: &#34;loadbalance_srcid&#34;, &#34;notify_switches&#34;: true, &#34;rolling_order&#34;: false}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/active_uplinks"></div>
      <p style="display: inline;"><strong>active_uplinks</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming_policy/active_uplinks" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </div></td>
    <td>
      <p>List of active uplinks used for load balancing.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/inbound_policy"></div>
      <p style="display: inline;"><strong>inbound_policy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming_policy/inbound_policy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicate whether or not the teaming policy is applied to inbound frames as well.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/load_balance_policy"></div>
      <p style="display: inline;"><strong>load_balance_policy</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming_policy/load_balance_policy" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Network adapter teaming policy.</p>
      <p><code class='docutils literal notranslate'>loadbalance_loadbased</code> is available from version 2.6 and onwards.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;loadbalance_ip&#34;</code></p></li>
        <li><p><code>&#34;loadbalance_srcmac&#34;</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">&#34;loadbalance_srcid&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;loadbalance_loadbased&#34;</code></p></li>
        <li><p><code>&#34;failover_explicit&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/notify_switches"></div>
      <p style="display: inline;"><strong>notify_switches</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming_policy/notify_switches" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicate whether or not to notify the physical switch if a link fails.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/rolling_order"></div>
      <p style="display: inline;"><strong>rolling_order</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming_policy/rolling_order" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicate whether or not to use a rolling policy when restoring links.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-teaming_policy/standby_uplinks"></div>
      <p style="display: inline;"><strong>standby_uplinks</strong></p>
      <a class="ansibleOptionLink" href="#parameter-teaming_policy/standby_uplinks" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </div></td>
    <td>
      <p>List of standby uplinks used for failover.</p>
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
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vlan_id"></div>
      <p style="display: inline;"><strong>vlan_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vlan_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The VLAN ID that should be configured with the portgroup, use 0 for no VLAN.</p>
      <p>If <code class='docutils literal notranslate'>vlan_trunk</code> is configured to be <em>true</em>, this can be a combination of multiple ranges and numbers, example: 1-200, 205, 400-4094.</p>
      <p>The valid <code class='docutils literal notranslate'>vlan_id</code> range is from 0 to 4094. Overlapping ranges are allowed.</p>
      <p>If <code class='docutils literal notranslate'>vlan_private</code> is configured to be <em>true</em>, the corresponding private VLAN should already be configured in the distributed vSwitch.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vlan_private"></div>
      <p style="display: inline;"><strong>vlan_private</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vlan_private" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether this is for a private VLAN or not.</p>
      <p>Mutually exclusive with <code class='docutils literal notranslate'>vlan_trunk</code> parameter.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-vlan_trunk"></div>
      <p style="display: inline;"><strong>vlan_trunk</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vlan_trunk" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Indicates whether this is a VLAN trunk or not.</p>
      <p>Mutually exclusive with <code class='docutils literal notranslate'>vlan_private</code> parameter.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
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

    
    - name: Create vlan portgroup
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: vlan-123-portrgoup
        switch_name: dvSwitch
        vlan_id: 123
        num_ports: 120
        port_binding: static
        state: present
      delegate_to: localhost

    - name: Create vlan trunk portgroup
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: vlan-trunk-portrgoup
        switch_name: dvSwitch
        vlan_id: 1-1000, 1005, 1100-1200
        vlan_trunk: true
        num_ports: 120
        port_binding: static
        state: present
      delegate_to: localhost

    - name: Create private vlan portgroup
      vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: private-vlan-portrgoup
        switch_name: dvSwitch
        vlan_id: 1001
        vlan_private: true
        num_ports: 120
        port_binding: static
        state: present
      delegate_to: localhost

    - name: Create no-vlan portgroup
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: no-vlan-portrgoup
        switch_name: dvSwitch
        vlan_id: 0
        num_ports: 120
        port_binding: static
        state: present
      delegate_to: localhost

    - name: Create vlan portgroup with all security and port policies
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: vlan-123-portrgoup
        switch_name: dvSwitch
        vlan_id: 123
        num_ports: 120
        port_binding: static
        state: present
        network_policy:
          inherited: false
          promiscuous: true
          forged_transmits: true
          mac_changes: true
        port_policy:
          block_override: true
          ipfix_override: true
          live_port_move: true
          network_rp_override: true
          port_config_reset_at_disconnect: true
          mac_management_override: true
          shaping_override: true
          traffic_filter_override: true
          uplink_teaming_override: true
          vendor_config_override: true
          vlan_override: true
      delegate_to: localhost







Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Philippe Dellaert (@pdellaert) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

