

community.vmware.vmware_cluster_vcls module -- Override the default vCLS (vSphere Cluster Services) VM disk placement for this cluster.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_cluster_vcls`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Override the default vCLS VM disk placement for this cluster.
- Some datastores cannot be selected for vCLS 'Allowed' as they are blocked by solutions as SRM or vSAN maintenance mode where vCLS cannot be configured.
- All values and VMware object names are case sensitive.








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
      <div class="ansibleOptionAnchor" id="parameter-allowed_datastores"></div>
      <p style="display: inline;"><strong>allowed_datastores</strong></p>
      <a class="ansibleOptionLink" href="#parameter-allowed_datastores" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>List of the allowed Datastores.</p>
      <p>If there is one more in the current List it will be removed.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cluster_name"></div>
      <p style="display: inline;"><strong>cluster_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The name of the cluster to be managed.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <div class="ansibleOptionAnchor" id="parameter-datacenter_name"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: datacenter_name</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>The name of the datacenter.</p>
    </td>
  </tr>
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

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Set Allowed vCLS Datastores
      community.vmware.vmware_cluster_vcls:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        allowed_datastores:
          - ds1
          - ds2
      delegate_to: localhost





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
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>&#34;{&#39;Added_AllowedDatastores&#39;: [&#39;ds2&#39;], &#39;Removed_AllowedDatastores&#39;: [&#39;ds3&#39;], &#39;result&#39;: None}&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Nina Loser (@Nina2244)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

