

community.vmware.vmware_deploy_ovf module -- Deploys a VMware virtual machine from an OVF or OVA file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_deploy_ovf`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to deploy a VMware VM from an OVF or OVA file








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
      <div class="ansibleOptionAnchor" id="parameter-allow_duplicates"></div>
      <p style="display: inline;"><strong>allow_duplicates</strong></p>
      <a class="ansibleOptionLink" href="#parameter-allow_duplicates" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Whether or not to allow duplicate VM names. ESXi allows duplicates, vCenter may not.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-cluster"></div>
      <p style="display: inline;"><strong>cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Cluster to deploy to.</p>
      <p>This is a required parameter, if <code class='docutils literal notranslate'>esxi_hostname</code> is not set and <code class='docutils literal notranslate'>hostname</code> is set to the vCenter server.</p>
      <p><code class='docutils literal notranslate'>esxi_hostname</code> and <code class='docutils literal notranslate'>cluster</code> are mutually exclusive parameters.</p>
      <p>This parameter is case sensitive.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Datacenter to deploy to.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;ha-datacenter&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-datastore"></div>
      <p style="display: inline;"><strong>datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Datastore to deploy to.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;datastore1&#34;</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-deployment_option"></div>
      <p style="display: inline;"><strong>deployment_option</strong></p>
      <a class="ansibleOptionLink" href="#parameter-deployment_option" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The key of the chosen deployment option.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-disk_provisioning"></div>
      <p style="display: inline;"><strong>disk_provisioning</strong></p>
      <a class="ansibleOptionLink" href="#parameter-disk_provisioning" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Disk provisioning type.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;flat&#34;</code></p></li>
        <li><p><code>&#34;eagerZeroedThick&#34;</code></p></li>
        <li><p><code>&#34;monolithicSparse&#34;</code></p></li>
        <li><p><code>&#34;twoGbMaxExtentSparse&#34;</code></p></li>
        <li><p><code>&#34;twoGbMaxExtentFlat&#34;</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">&#34;thin&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;sparse&#34;</code></p></li>
        <li><p><code>&#34;thick&#34;</code></p></li>
        <li><p><code>&#34;seSparse&#34;</code></p></li>
        <li><p><code>&#34;monolithicFlat&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The ESXi hostname where the virtual machine will run.</p>
      <p>This is a required parameter, if <code class='docutils literal notranslate'>cluster</code> is not set and <code class='docutils literal notranslate'>hostname</code> is set to the vCenter server.</p>
      <p><code class='docutils literal notranslate'>esxi_hostname</code> and <code class='docutils literal notranslate'>cluster</code> are mutually exclusive parameters.</p>
      <p>This parameter is case sensitive.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-fail_on_spec_warnings"></div>
      <p style="display: inline;"><strong>fail_on_spec_warnings</strong></p>
      <a class="ansibleOptionLink" href="#parameter-fail_on_spec_warnings" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Cause the module to treat OVF Import Spec warnings as errors.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Absolute path of folder to place the virtual machine.</p>
      <p>If not specified, defaults to the value of <code class='docutils literal notranslate'>datacenter.vmFolder</code>.</p>
      <p>Examples:</p>
      <p>   folder: /ha-datacenter/vm</p>
      <p>   folder: ha-datacenter/vm</p>
      <p>   folder: /datacenter1/vm</p>
      <p>   folder: datacenter1/vm</p>
      <p>   folder: /datacenter1/vm/folder1</p>
      <p>   folder: datacenter1/vm/folder1</p>
      <p>   folder: /folder1/datacenter1/vm</p>
      <p>   folder: folder1/datacenter1/vm</p>
      <p>   folder: /folder1/datacenter1/vm/folder2</p>
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
      <div class="ansibleOptionAnchor" id="parameter-inject_ovf_env"></div>
      <p style="display: inline;"><strong>inject_ovf_env</strong></p>
      <a class="ansibleOptionLink" href="#parameter-inject_ovf_env" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Force the given properties to be inserted into an OVF Environment and injected through VMware Tools.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code style="color: blue; font-weight: 700;">false</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Name of the VM to work with.</p>
      <p>Virtual machine names in vCenter are not necessarily unique, which may be problematic.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-networks"></div>
      <p style="display: inline;"><strong>networks</strong></p>
      <a class="ansibleOptionLink" href="#parameter-networks" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p><code class='docutils literal notranslate'>key: value</code> mapping of OVF network name, to the vCenter network name.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">{&#34;VM Network&#34;: &#34;VM Network&#34;}</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-ovf"></div>
      <div class="ansibleOptionAnchor" id="parameter-ova"></div>
      <p style="display: inline;"><strong>ovf</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ovf" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: ova</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">path</span>
      </p>
    </div></td>
    <td>
      <p>Path to OVF or OVA file to deploy.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-power_on"></div>
      <p style="display: inline;"><strong>power_on</strong></p>
      <a class="ansibleOptionLink" href="#parameter-power_on" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Whether or not to power on the virtual machine after creation.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-properties"></div>
      <p style="display: inline;"><strong>properties</strong></p>
      <a class="ansibleOptionLink" href="#parameter-properties" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>The assignment of values to the properties found in the OVF as key value pairs.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-resource_pool"></div>
      <p style="display: inline;"><strong>resource_pool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_pool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Resource Pool to deploy to.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">&#34;Resources&#34;</code></p>
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
      <div class="ansibleOptionAnchor" id="parameter-wait"></div>
      <p style="display: inline;"><strong>wait</strong></p>
      <a class="ansibleOptionLink" href="#parameter-wait" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Wait for the host to power on.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-wait_for_ip_address"></div>
      <p style="display: inline;"><strong>wait_for_ip_address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-wait_for_ip_address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Wait until vCenter detects an IP address for the VM.</p>
      <p>This requires vmware-tools (vmtoolsd) to properly work after creation.</p>
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

    
    - community.vmware.vmware_deploy_ovf:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        ovf: /path/to/ubuntu-16.04-amd64.ovf
        wait_for_ip_address: true
      delegate_to: localhost

    # Deploys a new VM named 'NewVM' in specific datacenter/cluster, with network mapping taken from variable and using ova template from an absolute path
    - community.vmware.vmware_deploy_ovf:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: Datacenter1
        cluster: Cluster1
        datastore: vsandatastore
        name: NewVM
        networks: "{u'VM Network':u'{{ ProvisioningNetworkLabel }}'}"
        power_on: false
        ovf: /absolute/path/to/template/mytemplate.ova
      delegate_to: localhost

    - community.vmware.vmware_deploy_ovf:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: Datacenter1
        esxi_hostname: test-server
        datastore: test-datastore
        ovf: /path/to/ubuntu-16.04-amd64.ovf
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
      <div class="ansibleOptionAnchor" id="return-instance"></div>
      <p style="display: inline;"><strong>instance</strong></p>
      <a class="ansibleOptionLink" href="#return-instance" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </div></td>
    <td>
      <p>metadata about the new virtual machine</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Returned:</span> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>&#34;None&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Matt Martz (@sivel)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

