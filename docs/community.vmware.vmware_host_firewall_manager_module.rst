

community.vmware.vmware_host_firewall_manager module -- Manage firewall configurations about an ESXi host
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_firewall_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage firewall configurations about an ESXi host when ESXi hostname or Cluster name is given.








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th colspan="3"><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-cluster_name"></div>
      <p style="display: inline;"><strong>cluster_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the cluster.</p>
      <p>Firewall settings are applied to every ESXi host system in given cluster.</p>
      <p>If <code class='docutils literal notranslate'>esxi_hostname</code> is not given, this parameter is required.</p>
    </td>
  </tr>
  <tr>
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>ESXi hostname.</p>
      <p>Firewall settings are applied to this ESXi host system.</p>
      <p>If <code class='docutils literal notranslate'>cluster_name</code> is not given, this parameter is required.</p>
    </td>
  </tr>
  <tr>
    <td colspan="3">
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
    <td colspan="3">
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
    <td colspan="3">
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
    <td colspan="3">
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
    <td colspan="3">
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
    <td colspan="3">
      <div class="ansibleOptionAnchor" id="parameter-rules"></div>
      <p style="display: inline;"><strong>rules</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rules" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td>
      <p>A list of Rule set which needs to be managed.</p>
      <p>Each member of list is rule set name and state to be set the rule.</p>
      <p>Both rule name and rule state are required parameters.</p>
      <p>Additional IPs and networks can also be specified</p>
      <p>Please see examples for more information.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-rules/allowed_hosts"></div>
      <p style="display: inline;"><strong>allowed_hosts</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rules/allowed_hosts" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Define the allowed hosts for this rule set.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-rules/allowed_hosts/all_ip"></div>
      <p style="display: inline;"><strong>all_ip</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rules/allowed_hosts/all_ip" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Whether all hosts should be allowed or not.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-rules/allowed_hosts/ip_address"></div>
      <p style="display: inline;"><strong>ip_address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rules/allowed_hosts/ip_address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>List of allowed IP addresses.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-rules/allowed_hosts/ip_network"></div>
      <p style="display: inline;"><strong>ip_network</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rules/allowed_hosts/ip_network" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>List of allowed IP networks.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>

  <tr>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-rules/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rules/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Whether the rule set is enabled or not.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-rules/name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rules/name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Rule set name.</p>
    </td>
  </tr>

  <tr>
    <td colspan="3">
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
    <td colspan="3">
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

    
    - name: Enable vvold rule set for all ESXi Host in given Cluster
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: cluster_name
        rules:
            - name: vvold
              enabled: true
              allowed_hosts:
                all_ip: true
      delegate_to: localhost

    - name: Enable vvold rule set for an ESXi Host
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        rules:
            - name: vvold
              enabled: true
              allowed_hosts:
                all_ip: true
      delegate_to: localhost

    - name: Manage multiple rule set for an ESXi Host
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        rules:
            - name: vvold
              enabled: true
              allowed_hosts:
                all_ip: true
            - name: CIMHttpServer
              enabled: false
      delegate_to: localhost

    - name: Manage IP and network based firewall permissions for ESXi
      community.vmware.vmware_host_firewall_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        rules:
            - name: gdbserver
              enabled: true
              allowed_hosts:
                all_ip: false
                ip_address:
                  - 192.168.20.10
                  - 192.168.20.11
            - name: CIMHttpServer
              enabled: true
              allowed_hosts:
                all_ip: false
                ip_network:
                  - 192.168.100.0/24
            - name: remoteSerialPort
              enabled: true
              allowed_hosts:
                all_ip: false
                ip_address:
                  - 192.168.100.11
                ip_network:
                  - 192.168.200.0/24
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
      <div class="ansibleOptionAnchor" id="return-rule_set_state"></div>
      <p style="display: inline;"><strong>rule_set_state</strong></p>
      <a class="ansibleOptionLink" href="#return-rule_set_state" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>dict with hostname as key and dict with firewall rule set facts as value</p>
      <p style="margin-top: 8px;"><b>Returned:</b> success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;rule_set_state&#34;: {&#34;localhost.localdomain&#34;: {&#34;CIMHttpServer&#34;: {&#34;allowed_hosts&#34;: {&#34;current_allowed_all&#34;: true, &#34;current_allowed_ip&#34;: [], &#34;current_allowed_networks&#34;: [], &#34;desired_allowed_all&#34;: true, &#34;desired_allowed_ip&#34;: [], &#34;desired_allowed_networks&#34;: [], &#34;previous_allowed_all&#34;: true, &#34;previous_allowed_ip&#34;: [], &#34;previous_allowed_networks&#34;: []}, &#34;current_state&#34;: false, &#34;desired_state&#34;: false, &#34;previous_state&#34;: true}, &#34;remoteSerialPort&#34;: {&#34;allowed_hosts&#34;: {&#34;current_allowed_all&#34;: false, &#34;current_allowed_ip&#34;: [&#34;192.168.100.11&#34;], &#34;current_allowed_networks&#34;: [&#34;192.168.200.0/24&#34;], &#34;desired_allowed_all&#34;: false, &#34;desired_allowed_ip&#34;: [&#34;192.168.100.11&#34;], &#34;desired_allowed_networks&#34;: [&#34;192.168.200.0/24&#34;], &#34;previous_allowed_all&#34;: true, &#34;previous_allowed_ip&#34;: [], &#34;previous_allowed_networks&#34;: []}, &#34;current_state&#34;: true, &#34;desired_state&#34;: true, &#34;previous_state&#34;: true}}}}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Aaron Longchamps (@alongchamps)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

