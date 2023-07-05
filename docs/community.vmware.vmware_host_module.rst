

community.vmware.vmware_host module -- Add, remove, or move an ESXi host to, from, or within vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add, reconnect, or remove an ESXi host to or from vCenter.
- This module can also be used to move an ESXi host to a cluster or folder, or vice versa, within the same datacenter.








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
    <td>
      <div class="ansibleOptionAnchor" id="parameter-add_connected"></div>
      <p style="display: inline;"><strong>add_connected</strong></p>
      <a class="ansibleOptionLink" href="#parameter-add_connected" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>If set to <code class='docutils literal notranslate'>true</code>, then the host should be connected as soon as it is added.</p>
      <p>This parameter is ignored if state is set to a value other than <code class='docutils literal notranslate'>present</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-cluster_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-cluster"></div>
      <p style="display: inline;"><strong>cluster_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: cluster</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the cluster to add the host.</p>
      <p>If <code class='docutils literal notranslate'>folder</code> is not set, then this parameter is required.</p>
      <p>Aliases added in version 2.6.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datacenter_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: datacenter</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Name of the datacenter to add the host.</p>
      <p>Aliases added in version 2.6.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>ESXi hostname to manage.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-esxi_password"></div>
      <p style="display: inline;"><strong>esxi_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>ESXi password.</p>
      <p>Required for adding a host.</p>
      <p>Optional for reconnect.</p>
      <p>Unused for removing.</p>
      <p>No longer a required parameter from version 2.5.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-esxi_ssl_thumbprint"></div>
      <div class="ansibleOptionAnchor" id="parameter-ssl_thumbprint"></div>
      <p style="display: inline;"><strong>esxi_ssl_thumbprint</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_ssl_thumbprint" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: ssl_thumbprint</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Specifying the hostsystem certificate&#x27;s thumbprint.</p>
      <p>Use following command to get hostsystem certificate&#x27;s thumbprint - </p>
      <p># openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha1 -noout</p>
      <p>Only used if <code class='docutils literal notranslate'>fetch_thumbprint</code> isn&#x27;t set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-esxi_username"></div>
      <p style="display: inline;"><strong>esxi_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>ESXi username.</p>
      <p>Required for adding a host.</p>
      <p>Optional for reconnect. If both <code class='docutils literal notranslate'>esxi_username</code> and <code class='docutils literal notranslate'>esxi_password</code> are used</p>
      <p>Unused for removing.</p>
      <p>No longer a required parameter from version 2.5.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-fetch_ssl_thumbprint"></div>
      <p style="display: inline;"><strong>fetch_ssl_thumbprint</strong></p>
      <a class="ansibleOptionLink" href="#parameter-fetch_ssl_thumbprint" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Fetch the thumbprint of the host&#x27;s SSL certificate.</p>
      <p>This basically disables the host certificate verification (check if it was signed by a recognized CA).</p>
      <p>Disable this option if you want to allow only hosts with valid certificates to be added to vCenter.</p>
      <p>If this option is set to <code class='docutils literal notranslate'>false</code> and the certificate can&#x27;t be verified, an add or reconnect will fail.</p>
      <p>Unused when <code class='docutils literal notranslate'>esxi_ssl_thumbprint</code> is set.</p>
      <p>Optional for reconnect, but only used if <code class='docutils literal notranslate'>esxi_username</code> and <code class='docutils literal notranslate'>esxi_password</code> are used.</p>
      <p>Unused for removing.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <div class="ansibleOptionAnchor" id="parameter-folder_name"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: folder_name</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the folder under which host to add.</p>
      <p>If <code class='docutils literal notranslate'>cluster_name</code> is not set, then this parameter is required.</p>
      <p>For example, if there is a datacenter &#x27;dc1&#x27; under folder called &#x27;Site1&#x27; then, this value will be &#x27;/Site1/dc1/host&#x27;.</p>
      <p>Here &#x27;host&#x27; is an invisible folder under VMware Web Client.</p>
      <p>Another example, if there is a nested folder structure like &#x27;/myhosts/india/pune&#x27; under datacenter &#x27;dc2&#x27;, then <code class='docutils literal notranslate'>folder</code> value will be &#x27;/dc2/host/myhosts/india/pune&#x27;.</p>
      <p>Other Examples: &#x27;/Site2/dc2/Asia-Cluster/host&#x27; or &#x27;/dc3/Asia-Cluster/host&#x27;</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-force_connection"></div>
      <p style="display: inline;"><strong>force_connection</strong></p>
      <a class="ansibleOptionLink" href="#parameter-force_connection" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Force the connection if the host is already being managed by another vCenter server.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
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
    <td>
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
    <td>
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
    <td>
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
    <td>
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
    <td>
      <div class="ansibleOptionAnchor" id="parameter-reconnect_disconnected"></div>
      <p style="display: inline;"><strong>reconnect_disconnected</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reconnect_disconnected" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Reconnect disconnected hosts.</p>
      <p>This is only used if <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>present</code> and if the host already exists.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>If set to <code class='docutils literal notranslate'>present</code>, add the host if host is absent.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code>, update the location of the host if host already exists.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code>, remove the host if host is present.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code>, do nothing if host already does not exists.</p>
      <p>If set to <code class='docutils literal notranslate'>add_or_reconnect</code>, add the host if it&#x27;s absent else reconnect it and update the location.</p>
      <p>If set to <code class='docutils literal notranslate'>reconnect</code>, then reconnect the host if it&#x27;s present and update the location.</p>
      <p>If set to <code class='docutils literal notranslate'>disconnected</code>, disconnect the host if the host already exists.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code>&#34;add_or_reconnect&#34;</code></p></li>
        <li><p><code>&#34;reconnect&#34;</code></p></li>
        <li><p><code>&#34;disconnected&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
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
    <td>
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

    
    - name: Add ESXi Host to vCenter
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: present
      delegate_to: localhost

    - name: Add ESXi Host to vCenter under a specific folder
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        folder: '/Site2/Asia-Cluster/host'
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: present
        add_connected: true
      delegate_to: localhost

    - name: Reconnect ESXi Host (with username/password set)
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: reconnect
      delegate_to: localhost

    - name: Reconnect ESXi Host (with default username/password)
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        state: reconnect
      delegate_to: localhost

    - name: Add ESXi Host with SSL Thumbprint to vCenter
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        esxi_ssl_thumbprint: "3C:A5:60:6F:7A:B7:C4:6C:48:28:3D:2F:A5:EC:A3:58:13:88:F6:DD"
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
    <td>
      <div class="ansibleOptionAnchor" id="return-result"></div>
      <p style="display: inline;"><strong>result</strong></p>
      <a class="ansibleOptionLink" href="#return-result" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>metadata about the new host system added</p>
      <p style="margin-top: 8px;"><b>Returned:</b> on successful addition</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>&#34;Host already connected to vCenter &#39;vcenter01&#39; in cluster &#39;cluster01&#39;&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Maxime de Roucy (@tchernomax)
- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

