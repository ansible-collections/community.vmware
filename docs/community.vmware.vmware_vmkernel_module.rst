

community.vmware.vmware_vmkernel module -- Manages a VMware VMkernel Adapter of an ESXi host.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vmkernel`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage the VMKernel adapters / VMKernel network interfaces of an ESXi host.
- The module assumes that the host is already configured with the Port Group in case of a vSphere Standard Switch (vSS).
- The module assumes that the host is already configured with the Distributed Port Group in case of a vSphere Distributed Switch (vDS).
- The module automatically migrates the VMKernel adapter from vSS to vDS or vice versa if present.








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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-device"></div>
      <p style="display: inline;"><strong>device</strong></p>
      <a class="ansibleOptionLink" href="#parameter-device" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Search VMkernel adapter by device name.</p>
      <p>The parameter is required only in case of <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>dhcp</code>.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-dvswitch_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-dvswitch"></div>
      <p style="display: inline;"><strong>dvswitch_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dvswitch_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: dvswitch</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the vSphere Distributed Switch (vDS) where to add the VMKernel interface.</p>
      <p>Required parameter only if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>.</p>
      <p>Optional parameter from version 2.8 and onwards.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_ft"></div>
      <p style="display: inline;"><strong>enable_ft</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_ft" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable Fault Tolerance traffic on the VMKernel adapter.</p>
      <p>This option is only allowed if the default TCP/IP stack is used.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_mgmt"></div>
      <p style="display: inline;"><strong>enable_mgmt</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_mgmt" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable Management traffic on the VMKernel adapter.</p>
      <p>This option is only allowed if the default TCP/IP stack is used.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_provisioning"></div>
      <p style="display: inline;"><strong>enable_provisioning</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_provisioning" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable Provisioning traffic on the VMKernel adapter.</p>
      <p>This option is only allowed if the default TCP/IP stack is used.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_replication"></div>
      <p style="display: inline;"><strong>enable_replication</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_replication" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable vSphere Replication traffic on the VMKernel adapter.</p>
      <p>This option is only allowed if the default TCP/IP stack is used.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_replication_nfc"></div>
      <p style="display: inline;"><strong>enable_replication_nfc</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_replication_nfc" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable vSphere Replication NFC traffic on the VMKernel adapter.</p>
      <p>This option is only allowed if the default TCP/IP stack is used.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_vmotion"></div>
      <p style="display: inline;"><strong>enable_vmotion</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_vmotion" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable vMotion traffic on the VMKernel adapter.</p>
      <p>This option is only allowed if the default TCP/IP stack is used.</p>
      <p>You cannot enable vMotion on an additional adapter if you already have an adapter with the vMotion TCP/IP stack configured.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable_vsan"></div>
      <p style="display: inline;"><strong>enable_vsan</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable_vsan" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable VSAN traffic on the VMKernel adapter.</p>
      <p>This option is only allowed if the default TCP/IP stack is used.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of ESXi host to which VMKernel is to be managed.</p>
      <p>From version 2.5 onwards, this parameter is required.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-mtu"></div>
      <p style="display: inline;"><strong>mtu</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mtu" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The MTU for the VMKernel interface.</p>
      <p>The default value of 1500 is valid from version 2.5 and onwards.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">1500</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-network"></div>
      <p style="display: inline;"><strong>network</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>A dictionary of network details.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">{&#34;tcpip_stack&#34;: &#34;default&#34;, &#34;type&#34;: &#34;static&#34;}</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-network/default_gateway"></div>
      <p style="display: inline;"><strong>default_gateway</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network/default_gateway" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Default gateway (Override default gateway for this adapter).</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-network/ip_address"></div>
      <p style="display: inline;"><strong>ip_address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network/ip_address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Static IP address.</p>
      <p>Required if <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>static</code>.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-network/subnet_mask"></div>
      <p style="display: inline;"><strong>subnet_mask</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network/subnet_mask" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Static netmask required.</p>
      <p>Required if <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>static</code>.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-network/tcpip_stack"></div>
      <p style="display: inline;"><strong>tcpip_stack</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network/tcpip_stack" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The TCP/IP stack for the VMKernel interface.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;default&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;provisioning&#34;</code></p></li>
        <li><p><code>&#34;vmotion&#34;</code></p></li>
        <li><p><code>&#34;vxlan&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-network/type"></div>
      <p style="display: inline;"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network/type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Type of IP assignment.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;static&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;dhcp&#34;</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-portgroup_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-portgroup"></div>
      <p style="display: inline;"><strong>portgroup_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-portgroup_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: portgroup</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the port group for the VMKernel interface.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>If set to <code class='docutils literal notranslate'>present</code>, the VMKernel adapter will be created with the given specifications.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code>, the VMKernel adapter will be removed.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code> and VMKernel adapter exists, the configurations will be updated.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vswitch_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-vswitch"></div>
      <p style="display: inline;"><strong>vswitch_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vswitch_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: vswitch</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the vSwitch where to add the VMKernel interface.</p>
      <p>Required parameter only if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code>.</p>
      <p>Optional parameter from version 2.5 and onwards.</p>
    </td>
  </tr>
  </tbody>
  </table>




Notes
-----

- The option \ :literal:`device`\  need to be used with DHCP because otherwise it's not possible to check if a VMkernel device is already present
- You can only change from DHCP to static, and vSS to vDS, or vice versa, in one step, without creating a new device, with \ :literal:`device`\  specified.
- You can only create the VMKernel adapter on a vDS if authenticated to vCenter and not if authenticated to ESXi.
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    -  name: Add Management vmkernel port using static network type
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0001
          network:
            type: 'static'
            ip_address: 192.168.127.10
            subnet_mask: 255.255.255.0
          state: present
          enable_mgmt: true
       delegate_to: localhost

    -  name: Add Management vmkernel port using DHCP network type
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0002
          state: present
          network:
            type: 'dhcp'
          enable_mgmt: true
       delegate_to: localhost

    -  name: Change IP allocation from static to dhcp
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0002
          state: present
          device: vmk1
          network:
            type: 'dhcp'
          enable_mgmt: true
       delegate_to: localhost

    -  name: Delete VMkernel port
       community.vmware.vmware_vmkernel:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          vswitch_name: vSwitch0
          portgroup_name: PG_0002
          state: absent
       delegate_to: localhost

    -  name: Add Management vmkernel port to Distributed Switch
       community.vmware.vmware_vmkernel:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          dvswitch_name: dvSwitch1
          portgroup_name: dvPG_0001
          network:
            type: 'static'
            ip_address: 192.168.127.10
            subnet_mask: 255.255.255.0
          state: present
          enable_mgmt: true
       delegate_to: localhost

    -  name: Add vMotion vmkernel port with vMotion TCP/IP stack
       community.vmware.vmware_vmkernel:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          esxi_hostname: '{{ esxi_hostname }}'
          dvswitch_name: dvSwitch1
          portgroup_name: dvPG_0001
          network:
            type: 'static'
            ip_address: 192.168.127.10
            subnet_mask: 255.255.255.0
            tcpip_stack: vmotion
          state: present
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
      <div class="ansibleOptionAnchor" id="return-result"></div>
      <p style="display: inline;"><strong>result</strong></p>
      <a class="ansibleOptionLink" href="#return-result" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>metadata about VMKernel name</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;changed&#34;: false, &#34;device&#34;: &#34;vmk1&#34;, &#34;ipv4&#34;: &#34;static&#34;, &#34;ipv4_gw&#34;: &#34;No override&#34;, &#34;ipv4_ip&#34;: &#34;192.168.1.15&#34;, &#34;ipv4_sm&#34;: &#34;255.255.255.0&#34;, &#34;msg&#34;: &#34;VMkernel Adapter already configured properly&#34;, &#34;mtu&#34;: 9000, &#34;services&#34;: &#34;vMotion&#34;, &#34;switch&#34;: &#34;vDS&#34;}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

