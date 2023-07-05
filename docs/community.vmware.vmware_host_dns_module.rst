

community.vmware.vmware_host_dns module -- Manage DNS configuration of an ESXi host system
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_dns`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure DNS for the default TCP/IP stack on an ESXi host system.








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
      <div class="ansibleOptionAnchor" id="parameter-cluster_name"></div>
      <p style="display: inline;"><strong>cluster_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the cluster from which all host systems will be used.</p>
      <p>This parameter is required if <code class='docutils literal notranslate'>esxi_hostname</code> is not specified and you connect to a vCenter.</p>
      <p>Cannot be used when you connect directly to an ESXi host.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-device"></div>
      <p style="display: inline;"><strong>device</strong></p>
      <a class="ansibleOptionLink" href="#parameter-device" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The VMkernel network adapter to obtain DNS settings from.</p>
      <p>Needs to get its IP through DHCP, a static network configuration combined with a dynamic DNS configuration doesn&#x27;t work.</p>
      <p>The parameter is only required in case of <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>dhcp</code>.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-dns_servers"></div>
      <p style="display: inline;"><strong>dns_servers</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dns_servers" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>A list of DNS servers to be used.</p>
      <p>The order of the DNS servers is important as they are used consecutively in order.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-domain"></div>
      <p style="display: inline;"><strong>domain</strong></p>
      <a class="ansibleOptionLink" href="#parameter-domain" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The domain name to be used for the ESXi host.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the host system to work with.</p>
      <p>This parameter is required if <code class='docutils literal notranslate'>cluster_name</code> is not specified and you connect to a vCenter.</p>
      <p>Cannot be used when you connect directly to an ESXi host.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-host_name"></div>
      <p style="display: inline;"><strong>host_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-host_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The hostname to be used for the ESXi host.</p>
      <p>Cannot be used when configuring a complete cluster.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-search_domains"></div>
      <p style="display: inline;"><strong>search_domains</strong></p>
      <a class="ansibleOptionLink" href="#parameter-search_domains" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>A list of domains to be searched through by the resolver.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-type"></div>
      <p style="display: inline;"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Type of DNS assignment. Either <code class='docutils literal notranslate'>dhcp</code> or <code class='docutils literal notranslate'>static</code>.</p>
      <p>A VMkernel adapter needs to be set to DHCP if <code class='docutils literal notranslate'>type</code> is set to <code class='docutils literal notranslate'>dhcp</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;dhcp&#34;</code></p></li>
        <li><p><code>&#34;static&#34;</code></p></li>
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
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-verbose"></div>
      <p style="display: inline;"><strong>verbose</strong></p>
      <a class="ansibleOptionLink" href="#parameter-verbose" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Verbose output of the DNS server configuration change.</p>
      <p>Explains if an DNS server was added, removed, or if the DNS server sequence was changed.</p>
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

- This module is a replacement for the module \ :literal:`vmware\_dns\_config`\ 
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Configure DNS for an ESXi host
      community.vmware.vmware_host_dns:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        type: static
        host_name: esx01
        domain: example.local
        dns_servers:
          - 192.168.1.10
          - 192.168.1.11
        search_domains:
          - subdomain.example.local
          - example.local
      delegate_to: localhost

    - name: Configure DNS for all ESXi hosts of a cluster
      community.vmware.vmware_host_dns:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: '{{ cluster_name }}'
        type: static
        domain: example.local
        dns_servers:
          - 192.168.1.10
          - 192.168.1.11
        search_domains:
          - subdomain.example.local
          - example.local
      delegate_to: localhost

    - name: Configure DNS via DHCP for an ESXi host
      community.vmware.vmware_host_dns:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
        type: dhcp
        device: vmk0
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
      <div class="ansibleOptionAnchor" id="return-dns_config_result"></div>
      <p style="display: inline;"><strong>dns_config_result</strong></p>
      <a class="ansibleOptionLink" href="#return-dns_config_result" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>metadata about host system&#x27;s DNS configuration</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;esx01.example.local&#34;: {&#34;changed&#34;: true, &#34;dns_servers&#34;: [&#34;192.168.1.10&#34;, &#34;192.168.1.11&#34;], &#34;dns_servers_changed&#34;: [&#34;192.168.1.12&#34;, &#34;192.168.1.13&#34;], &#34;dns_servers_previous&#34;: [&#34;192.168.1.10&#34;, &#34;192.168.1.11&#34;, &#34;192.168.1.12&#34;, &#34;192.168.1.13&#34;], &#34;domain&#34;: &#34;example.local&#34;, &#34;host_name&#34;: &#34;esx01&#34;, &#34;msg&#34;: &#34;DNS servers and Search domains changed&#34;, &#34;search_domains&#34;: [&#34;subdomain.example.local&#34;, &#34;example.local&#34;], &#34;search_domains_changed&#34;: [&#34;subdomain.example.local&#34;], &#34;search_domains_previous&#34;: [&#34;example.local&#34;]}}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Christian Kotte (@ckotte)
- Mario Lenz (@mariolenz)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

