

community.vmware.vcenter_standard_key_provider module -- Add, reconfigure or remove Standard Key Provider on vCenter server
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vcenter_standard_key_provider`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is used for adding, reconfiguring or removing Standard Key Provider on vCenter server. Refer to VMware docs for more information: \ `Standard Key Provider <https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-6DB1E745-9624-43EA-847C-DD2F767CB94B.html>`__\ 









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
      <div class="ansibleOptionAnchor" id="parameter-kms_info"></div>
      <p style="display: inline;"><strong>kms_info</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kms_info" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>
    </td>
    <td>
      <p>The information of an external key server (KMS).</p>
      <p><code class='docutils literal notranslate'>kms_name</code>, <code class='docutils literal notranslate'>kms_ip</code> are required when adding a Standard Key Provider.</p>
      <p>If <code class='docutils literal notranslate'>kms_port</code> is not specified, the default port 5696 will be used.</p>
      <p><code class='docutils literal notranslate'>kms_ip</code>, <code class='docutils literal notranslate'>kms_port</code> can be reconfigured for an existing KMS with name <code class='docutils literal notranslate'>kms_name</code>.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-kms_info/kms_ip"></div>
      <p style="display: inline;"><strong>kms_ip</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kms_info/kms_ip" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>IP address of the external KMS.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-kms_info/kms_name"></div>
      <p style="display: inline;"><strong>kms_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kms_info/kms_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the KMS to be configured.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-kms_info/kms_port"></div>
      <p style="display: inline;"><strong>kms_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kms_info/kms_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Port of the external KMS.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-kms_info/remove_kms"></div>
      <p style="display: inline;"><strong>remove_kms</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kms_info/remove_kms" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Remove the configured KMS with name <code class='docutils literal notranslate'>kms_name</code> from the KMIP cluster.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-kms_password"></div>
      <p style="display: inline;"><strong>kms_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kms_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Password to authenticate to the KMS.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-kms_username"></div>
      <p style="display: inline;"><strong>kms_username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-kms_username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Username to authenticate to the KMS.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-make_kms_trust_vc"></div>
      <p style="display: inline;"><strong>make_kms_trust_vc</strong></p>
      <a class="ansibleOptionLink" href="#parameter-make_kms_trust_vc" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>After adding the Standard Key Provider to the vCenter Server, you can establish a trusted connection, the exact process depends on the certificates that the key provider accepts, and on your company policy.</p>
      <p>Three methods implemented here, (1) upload client certificate and private key through <code class='docutils literal notranslate'>upload_client_cert</code> and <code class='docutils literal notranslate'>upload_client_key</code> parameters, (2) generate, update, download vCenter self signed certificate through <code class='docutils literal notranslate'>download_self_signed_cert</code> parameter, (3) download generated Certificate Signing Request(CSR) through <code class='docutils literal notranslate'>download_client_csr</code> parameter, send it to KMS then upload the KMS signed CSR through <code class='docutils literal notranslate'>upload_kms_signed_client_csr</code> parameter.</p>
      <p>This is not set to be mandatory, if not set, please go to vCenter to setup trust connection with KMS manually.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-make_kms_trust_vc/download_client_csr"></div>
      <p style="display: inline;"><strong>download_client_csr</strong></p>
      <a class="ansibleOptionLink" href="#parameter-make_kms_trust_vc/download_client_csr" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">path</span>
      </p>
    </td>
    <td>
      <p>The absolute path on local machine for keeping vCenter generated CSR.</p>
      <p>Then upload the KMS signed CSR using <code class='docutils literal notranslate'>upload_kms_signed_client_csr</code> to vCenter.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-make_kms_trust_vc/download_self_signed_cert"></div>
      <p style="display: inline;"><strong>download_self_signed_cert</strong></p>
      <a class="ansibleOptionLink" href="#parameter-make_kms_trust_vc/download_self_signed_cert" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">path</span>
      </p>
    </td>
    <td>
      <p>The absolute path on local machine for keeping vCenter generated self signed client cert.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-make_kms_trust_vc/upload_client_cert"></div>
      <p style="display: inline;"><strong>upload_client_cert</strong></p>
      <a class="ansibleOptionLink" href="#parameter-make_kms_trust_vc/upload_client_cert" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">path</span>
      </p>
    </td>
    <td>
      <p>The absolute file path of client certificate.</p>
      <p>Request a certificate and private key from the KMS vendor. The files are X509 files in PEM format.</p>
      <p>The certificate might be already trusted by the KMS server.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-make_kms_trust_vc/upload_client_key"></div>
      <p style="display: inline;"><strong>upload_client_key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-make_kms_trust_vc/upload_client_key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">path</span>
      </p>
    </td>
    <td>
      <p>The absolute file path of client private key to be uploaded together with <code class='docutils literal notranslate'>upload_client_cert</code>.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-make_kms_trust_vc/upload_kms_signed_client_csr"></div>
      <p style="display: inline;"><strong>upload_kms_signed_client_csr</strong></p>
      <a class="ansibleOptionLink" href="#parameter-make_kms_trust_vc/upload_kms_signed_client_csr" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">path</span>
      </p>
    </td>
    <td>
      <p>The absolute file path of KMS signed CSR downloaded from <code class='docutils literal notranslate'>download_client_csr</code>.</p>
    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-mark_default"></div>
      <p style="display: inline;"><strong>mark_default</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mark_default" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Set specified Key Provider with name <code class='docutils literal notranslate'>name</code> as the default Key Provider.</p>
      <p>If new added Key Provider is the only key provider in vCenter, then will mark it as default after adding.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Name of the Key Provider to be added, reconfigured or removed from vCenter.</p>
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
      <p>Port of the proxy server.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-proxy_server"></div>
      <p style="display: inline;"><strong>proxy_server</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_server" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Address of the proxy server to connect to KMS.</p>
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
      <p>If set to <code class='docutils literal notranslate'>absent</code>, the named Key Provider will be removed from vCenter.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code>, the named existing Key Provider will be reconfigured or new Key Provider will be added.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

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

    
    - name: Add a new Standard Key Provider with client certificate and private key
      community.vmware.vcenter_standard_key_provider:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: 'test_standard_kp'
        state: 'present'
        mark_default: true
        kms_info:
          - kms_name: test_kms_1
            kms_ip: 192.168.1.10
        make_kms_trust_vc:
          upload_client_cert: "/tmp/test_cert.pem"
          upload_client_key: "/tmp/test_cert_key.pem"
      register: add_skp_result

    - name: Remove the KMS from the key provider cluster
      community.vmware.vcenter_standard_key_provider:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: 'test_standard_kp'
        state: 'present'
        kms_info:
          - kms_name: test_kms_1
            remove_kms: true
      register: remove_kms_result

    - name: Remove the Standard Key Provider
      community.vmware.vcenter_standard_key_provider:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: 'test_standard_kp'
        state: 'absent'
      register: remove_kp_result





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
      <div class="ansibleOptionAnchor" id="return-key_provider_clusters"></div>
      <p style="display: inline;"><strong>key_provider_clusters</strong></p>
      <a class="ansibleOptionLink" href="#return-key_provider_clusters" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>the Key Provider cluster info</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>[{&#34;has_backup&#34;: null, &#34;key_id&#34;: null, &#34;key_provide_id&#34;: &#34;test_standard&#34;, &#34;management_type&#34;: null, &#34;servers&#34;: [{&#34;address&#34;: &#34;192.168.1.10&#34;, &#34;name&#34;: &#34;test_kms&#34;, &#34;port&#34;: 5696, &#34;protocol&#34;: &#34;&#34;, &#34;proxy&#34;: &#34;&#34;, &#34;proxy_port&#34;: null, &#34;user_name&#34;: &#34;&#34;}], &#34;tpm_required&#34;: null, &#34;use_as_default&#34;: true}]</code></p>
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

