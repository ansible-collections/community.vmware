

community.vmware.vmware_guest_network module -- Manage network adapters of specified virtual machine in given vCenter infrastructure
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_network`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is used to add, reconfigure, remove network adapter of given virtual machine.








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
      <div class="ansibleOptionAnchor" id="parameter-allow_guest_os_mtu_change"></div>
      <p style="display: inline;"><strong>allow_guest_os_mtu_change</strong></p>
      <a class="ansibleOptionLink" href="#parameter-allow_guest_os_mtu_change" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.3.0</i></p>
    </td>
    <td valign="top">
      <p>Allows the guest OS to change the MTU on a SR-IOV network adapter.</p>
      <p>This option is only compatible for SR-IOV network adapters.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-cluster"></div>
      <p style="display: inline;"><strong>cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of cluster where VM belongs to.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-connected"></div>
      <p style="display: inline;"><strong>connected</strong></p>
      <a class="ansibleOptionLink" href="#parameter-connected" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If NIC should be connected to the network.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
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
      <p>Datacenter the VM belongs to.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;ha-datacenter&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-device_type"></div>
      <p style="display: inline;"><strong>device_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-device_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Type of virtual network device.</p>
      <p>Valid choices are - <code class='docutils literal notranslate'>e1000</code>, <code class='docutils literal notranslate'>e1000e</code>, <code class='docutils literal notranslate'>pcnet32</code>, <code class='docutils literal notranslate'>vmxnet2</code>, <code class='docutils literal notranslate'>vmxnet3</code> (default), <code class='docutils literal notranslate'>sriov</code>, <code class='docutils literal notranslate'>pvrdma</code>.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;vmxnet3&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-directpath_io"></div>
      <p style="display: inline;"><strong>directpath_io</strong></p>
      <a class="ansibleOptionLink" href="#parameter-directpath_io" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable Universal Pass-through (UPT).</p>
      <p>Only compatible with the <code class='docutils literal notranslate'>vmxnet3</code> device type.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

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
      <p>The hostname of the ESXi host where the VM belongs to.</p>
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
      <p>Folder location of given VM, this is only required when there&#x27;s multiple VM&#x27;s with the same name.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-force"></div>
      <p style="display: inline;"><strong>force</strong></p>
      <a class="ansibleOptionLink" href="#parameter-force" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Force adapter creation even if an existing adapter is attached to the same network.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-gather_network_info"></div>
      <div class="ansibleOptionAnchor" id="parameter-gather_network_facts"></div>
      <p style="display: inline;"><strong>gather_network_info</strong></p>
      <a class="ansibleOptionLink" href="#parameter-gather_network_info" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: gather_network_facts</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Return information about current guest network adapters.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-guest_control"></div>
      <p style="display: inline;"><strong>guest_control</strong></p>
      <a class="ansibleOptionLink" href="#parameter-guest_control" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enables guest control over whether the connectable device is connected.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

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
      <div class="ansibleOptionAnchor" id="parameter-label"></div>
      <p style="display: inline;"><strong>label</strong></p>
      <a class="ansibleOptionLink" href="#parameter-label" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Label of the NIC that should be altered. <code class='docutils literal notranslate'>mac_address</code> or <code class='docutils literal notranslate'>label</code> should be set to get the corresponding device to reconfigure.</p>
      <p>Alter the name of the network adapter.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-mac_address"></div>
      <p style="display: inline;"><strong>mac_address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mac_address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>MAC address of the NIC that should be altered, if a MAC address is not supplied a new nic will be created.</p>
      <p>Required when <em>state=absent</em>.</p>
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
      <p>Required if <code class='docutils literal notranslate'>uuid</code> or <code class='docutils literal notranslate'>name</code> is not supplied.</p>
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
      <p>Name of virtual machine</p>
      <p>Required if <code class='docutils literal notranslate'>uuid</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-network_name"></div>
      <p style="display: inline;"><strong>network_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-network_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of network in vSphere.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-physical_function_backing"></div>
      <p style="display: inline;"><strong>physical_function_backing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-physical_function_backing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.3.0</i></p>
    </td>
    <td valign="top">
      <p>If set, specifies the PCI ID of the physical function to use as backing for a SR-IOV network adapter.</p>
      <p>This option is only compatible for SR-IOV network adapters.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-pvrdma_device_protocol"></div>
      <p style="display: inline;"><strong>pvrdma_device_protocol</strong></p>
      <a class="ansibleOptionLink" href="#parameter-pvrdma_device_protocol" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.3.0</i></p>
    </td>
    <td valign="top">
      <p>The PVRDMA device protocol used. Valid choices are - <code class='docutils literal notranslate'>rocev1</code>, <code class='docutils literal notranslate'>rocev2</code>.</p>
      <p>This parameter is only used on the VM with hardware version &gt;=14 and &lt;= 19.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-start_connected"></div>
      <p style="display: inline;"><strong>start_connected</strong></p>
      <a class="ansibleOptionLink" href="#parameter-start_connected" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If NIC should be connected to network on startup.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>NIC state.</p>
      <p>When <code class='docutils literal notranslate'>state=present</code>, a nic will be added if a mac address or label does not previously exists or is unset.</p>
      <p>When <code class='docutils literal notranslate'>state=absent</code>, the <em>mac_address</em> parameter has to be set.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-switch"></div>
      <p style="display: inline;"><strong>switch</strong></p>
      <a class="ansibleOptionLink" href="#parameter-switch" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the (dv)switch for destination network, this is only required for dvswitches.</p>
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
      <p>vm uuid</p>
      <p>Required if <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
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
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-virtual_function_backing"></div>
      <p style="display: inline;"><strong>virtual_function_backing</strong></p>
      <a class="ansibleOptionLink" href="#parameter-virtual_function_backing" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.3.0</i></p>
    </td>
    <td valign="top">
      <p>If set, specifies the PCI ID of the physical function to use as backing for a SR-IOV network adapter.</p>
      <p>This option is only compatible for SR-IOV network adapters.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vlan_id"></div>
      <p style="display: inline;"><strong>vlan_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vlan_id" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>VLAN id associated with the network.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-wake_onlan"></div>
      <p style="display: inline;"><strong>wake_onlan</strong></p>
      <a class="ansibleOptionLink" href="#parameter-wake_onlan" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Enable wake on LAN.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>




Notes
-----

- For backwards compatibility network\_data is returned when using the gather\_network\_info parameter
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: change network for 00:50:56:11:22:33 on vm01.domain.fake
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: vm01.domain.fake
        mac_address: 00:50:56:11:22:33
        network_name: admin-network
        state: present

    - name: add a nic on network with vlan id 2001 for 422d000d-2000-ffff-0000-b00000000000
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        uuid: 422d000d-2000-ffff-0000-b00000000000
        vlan_id: 2001

    - name: remove nic with mac 00:50:56:11:22:33 from vm01.domain.fake
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        mac_address: 00:50:56:11:22:33
        name: vm01.domain.fake
        state: absent

    - name: add multiple nics to vm01.domain.fake
      community.vmware.vmware_guest_network:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: vm01.domain.fake
        state: present
        vlan_id: "{{ item.vlan_id | default(omit) }}"
        network_name: "{{ item.network_name | default(omit) }}"
        connected: "{{ item.connected | default(omit) }}"
      loop:
        - vlan_id: 2000
          connected: false
        - network_name: guest-net
          connected: true





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
      <div class="ansibleOptionAnchor" id="return-network_data"></div>
      <p style="display: inline;"><strong>network_data</strong></p>
      <a class="ansibleOptionLink" href="#return-network_data" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>For backwards compatibility, metadata about the virtual machine network adapters</p>
      <p style="margin-top: 8px;"><b>Returned:</b> when using gather_network_info parameter</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;network_data&#34;: {&#34;0&#34;: {&#34;allow_guest_ctl&#34;: true, &#34;connected&#34;: true, &#34;device_type&#34;: &#34;vmxnet3&#34;, &#34;label&#34;: &#34;Network adapter 2&#34;, &#34;mac_addr&#34;: &#34;00:50:56:AA:AA:AA&#34;, &#34;mac_address&#34;: &#34;00:50:56:AA:AA:AA&#34;, &#34;name&#34;: &#34;admin-net&#34;, &#34;network_name&#34;: &#34;admin-net&#34;, &#34;start_connected&#34;: true, &#34;switch&#34;: &#34;vSwitch0&#34;, &#34;unit_number&#34;: 8, &#34;vlan_id&#34;: 10, &#34;wake_onlan&#34;: false}, &#34;1&#34;: {&#34;allow_guest_ctl&#34;: true, &#34;connected&#34;: true, &#34;device_type&#34;: &#34;vmxnet3&#34;, &#34;label&#34;: &#34;Network adapter 1&#34;, &#34;mac_addr&#34;: &#34;00:50:56:BB:BB:BB&#34;, &#34;mac_address&#34;: &#34;00:50:56:BB:BB:BB&#34;, &#34;name&#34;: &#34;guest-net&#34;, &#34;network_name&#34;: &#34;guest-net&#34;, &#34;start_connected&#34;: true, &#34;switch&#34;: &#34;vSwitch0&#34;, &#34;unit_number&#34;: 7, &#34;vlan_id&#34;: 10, &#34;wake_onlan&#34;: true}}}</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-network_info"></div>
      <p style="display: inline;"><strong>network_info</strong></p>
      <a class="ansibleOptionLink" href="#return-network_info" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td valign="top">
      <p>metadata about the virtual machine network adapters</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;network_info&#34;: [{&#34;allow_guest_ctl&#34;: true, &#34;connected&#34;: true, &#34;device_type&#34;: &#34;vmxnet3&#34;, &#34;label&#34;: &#34;Network adapter 2&#34;, &#34;mac_address&#34;: &#34;00:50:56:AA:AA:AA&#34;, &#34;network_name&#34;: &#34;admin-net&#34;, &#34;start_connected&#34;: true, &#34;switch&#34;: &#34;vSwitch0&#34;, &#34;unit_number&#34;: 8, &#34;vlan_id&#34;: 10, &#34;wake_onlan&#34;: false}, {&#34;allow_guest_ctl&#34;: true, &#34;connected&#34;: true, &#34;device_type&#34;: &#34;vmxnet3&#34;, &#34;label&#34;: &#34;Network adapter 1&#34;, &#34;mac_address&#34;: &#34;00:50:56:BB:BB:BB&#34;, &#34;network_name&#34;: &#34;guest-net&#34;, &#34;start_connected&#34;: true, &#34;switch&#34;: &#34;vSwitch0&#34;, &#34;unit_number&#34;: 7, &#34;vlan_id&#34;: 10, &#34;wake_onlan&#34;: true}]}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Diane Wang (@Tomorrow9) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

