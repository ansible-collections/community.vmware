

community.vmware.vmware_dvswitch_lacp module -- Manage LACP configuration on a Distributed Switch
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_dvswitch_lacp`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure Link Aggregation Control Protocol (LACP) support mode and Link Aggregation Groups (LAGs).








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
      <div class="ansibleOptionAnchor" id="parameter-link_aggregation_groups"></div>
      <p style="display: inline;"><strong>link_aggregation_groups</strong></p>
      <a class="ansibleOptionLink" href="#parameter-link_aggregation_groups" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </div></td>
    <td>
      <p>Can only be used if <code class='docutils literal notranslate'>lacp_support</code> is set to <code class='docutils literal notranslate'>enhanced</code>.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-link_aggregation_groups/load_balancing_mode"></div>
      <p style="display: inline;"><strong>load_balancing_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-link_aggregation_groups/load_balancing_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Load balancing algorithm.</p>
      <p>Valid values are as follows</p>
      <p>- srcTcpUdpPort: Source TCP/UDP port number.</p>
      <p>- srcDestIpTcpUdpPortVlan: Source and destination IP, source and destination TCP/UDP port number and VLAN.</p>
      <p>- srcIpVlan: Source IP and VLAN.</p>
      <p>- srcDestTcpUdpPort: Source and destination TCP/UDP port number.</p>
      <p>- srcMac: Source MAC address.</p>
      <p>- destIp: Destination IP.</p>
      <p>- destMac: Destination MAC address.</p>
      <p>- vlan: VLAN only.</p>
      <p>- srcDestIp: Source and Destination IP.</p>
      <p>- srcIpTcpUdpPortVlan: Source IP, TCP/UDP port number and VLAN.</p>
      <p>- srcDestIpTcpUdpPort: Source and destination IP and TCP/UDP port number.</p>
      <p>- srcDestMac: Source and destination MAC address.</p>
      <p>- destIpTcpUdpPort: Destination IP and TCP/UDP port number.</p>
      <p>- srcPortId: Source Virtual Port Id.</p>
      <p>- srcIp: Source IP.</p>
      <p>- srcIpTcpUdpPort: Source IP and TCP/UDP port number.</p>
      <p>- destIpTcpUdpPortVlan: Destination IP, TCP/UDP port number and VLAN.</p>
      <p>- destTcpUdpPort: Destination TCP/UDP port number.</p>
      <p>- destIpVlan: Destination IP and VLAN.</p>
      <p>- srcDestIpVlan: Source and destination IP and VLAN.</p>
      <p>Please see examples for more information.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;srcDestIpTcpUdpPortVlan&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-link_aggregation_groups/mode"></div>
      <p style="display: inline;"><strong>mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-link_aggregation_groups/mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The negotiating state of the uplinks/ports.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;active&#34;</code></p></li>
        <li><p><code>&#34;passive&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-link_aggregation_groups/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-link_aggregation_groups/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Name of the LAG.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-link_aggregation_groups/uplink_number"></div>
      <p style="display: inline;"><strong>uplink_number</strong></p>
      <a class="ansibleOptionLink" href="#parameter-link_aggregation_groups/uplink_number" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Number of uplinks.</p>
      <p>Can 1 to 30.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-support_mode"></div>
      <p style="display: inline;"><strong>support_mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-support_mode" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The LACP support mode.</p>
      <p><code class='docutils literal notranslate'>basic</code>: One Link Aggregation Control Protocol group in the switch (singleLag).</p>
      <p><code class='docutils literal notranslate'>enhanced</code>: Multiple Link Aggregation Control Protocol groups in the switch (multipleLag).</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">&#34;basic&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;enhanced&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-switch"></div>
      <div class="ansibleOptionAnchor" id="parameter-dvswitch"></div>
      <p style="display: inline;"><strong>switch</strong></p>
      <a class="ansibleOptionLink" href="#parameter-switch" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: dvswitch</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The name of the Distributed Switch to manage.</p>
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

- You need to run the task two times if you want to remove all LAGs and change the support mode to 'basic'
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Enable enhanced mode on a Distributed Switch
      community.vmware.vmware_dvswitch_lacp:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        support_mode: enhanced
        validate_certs: "{{ validate_vcenter_certs }}"
      delegate_to: localhost
      loop_control:
        label: "{{ item.name }}"
      with_items: "{{ vcenter_distributed_switches }}"

    - name: Enable enhanced mode and create two LAGs on a Distributed Switch
      community.vmware.vmware_dvswitch_lacp:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        support_mode: enhanced
        link_aggregation_groups:
            - name: lag1
              uplink_number: 2
              mode: active
              load_balancing_mode: srcDestIpTcpUdpPortVlan
            - name: lag2
              uplink_number: 2
              mode: passive
              load_balancing_mode: srcDestIp
        validate_certs: "{{ validate_vcenter_certs }}"
      delegate_to: localhost
      loop_control:
        label: "{{ item.name }}"
      with_items: "{{ vcenter_distributed_switches }}"





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
      <div class="ansibleOptionAnchor" id="return-result"></div>
      <p style="display: inline;"><strong>result</strong></p>
      <a class="ansibleOptionLink" href="#return-result" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>information about performed operation</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Returned:</span> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>&#34;{&#39;changed&#39;: True, &#39;dvswitch&#39;: &#39;dvSwitch&#39;, &#39;link_aggregation_groups&#39;: [{&#39;load_balancing_mode&#39;: &#39;srcDestIpTcpUdpPortVlan&#39;, &#39;mode&#39;: &#39;active&#39;, &#39;name&#39;: &#39;lag1&#39;, &#39;uplink_number&#39;: 2}, {&#39;load_balancing_mode&#39;: &#39;srcDestIp&#39;, &#39;mode&#39;: &#39;active&#39;, &#39;name&#39;: &#39;lag2&#39;, &#39;uplink_number&#39;: 2}], &#39;link_aggregation_groups_previous&#39;: [], &#39;result&#39;: &#39;lacp lags changed&#39;, &#39;support_mode&#39;: &#39;enhanced&#39;}&#34;</code></p>
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

