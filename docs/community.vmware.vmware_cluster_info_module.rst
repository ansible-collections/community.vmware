

community.vmware.vmware_cluster_info module -- Gather info about clusters available in given vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_cluster_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about clusters in VMWare infrastructure.
- All values and VMware object names are case sensitive.








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
      <p>Name of the cluster.</p>
      <p>If set, information of this cluster will be returned.</p>
      <p>This parameter is required, if <code class='docutils literal notranslate'>datacenter</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Datacenter to search for cluster/s.</p>
      <p>This parameter is required, if <code class='docutils literal notranslate'>cluster_name</code> is not supplied.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-properties"></div>
      <p style="display: inline;"><strong>properties</strong></p>
      <a class="ansibleOptionLink" href="#parameter-properties" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>Specify the properties to retrieve.</p>
      <p>Example:</p>
      <p>   properties: [</p>
      <p>      "name",</p>
      <p>      "configuration.dasConfig.enabled",</p>
      <p>      "summary.totalCpu"</p>
      <p>   ]</p>
      <p>Only valid when <code class='docutils literal notranslate'>schema</code> is <code class='docutils literal notranslate'>vsphere</code>.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-schema"></div>
      <p style="display: inline;"><strong>schema</strong></p>
      <a class="ansibleOptionLink" href="#parameter-schema" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Specify the output schema desired.</p>
      <p>The &#x27;summary&#x27; output schema is the legacy output from the module.</p>
      <p>The &#x27;vsphere&#x27; output schema is the vSphere API class definition which requires pyvmomi&gt;6.7.1.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;summary&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;vsphere&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_tag"></div>
      <p style="display: inline;"><strong>show_tag</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_tag" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Tags related to cluster are shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
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

    
    - name: Gather cluster info from given datacenter
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: ha-datacenter
      delegate_to: localhost
      register: cluster_info

    - name: Gather info from datacenter about specific cluster
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
      delegate_to: localhost
      register: cluster_info

    - name: Gather info from datacenter about specific cluster with tags
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
        show_tag: true
      delegate_to: localhost
      register: cluster_info

    - name: Gather some info from a cluster using the vSphere API output schema
      vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
        schema: vsphere
        properties:
          - name
          - configuration.dasConfig.enabled
          - summary.totalCpu
      delegate_to: localhost
      register: cluster_info





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
      <div class="ansibleOptionAnchor" id="return-clusters"></div>
      <p style="display: inline;"><strong>clusters</strong></p>
      <a class="ansibleOptionLink" href="#return-clusters" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>metadata about the available clusters</p>
      <p>datacenter added in the return values from version 1.6.0</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;DC0_C0&#34;: {&#34;datacenter&#34;: &#34;DC0&#34;, &#34;drs_default_vm_behavior&#34;: null, &#34;drs_enable_vm_behavior_overrides&#34;: null, &#34;drs_vmotion_rate&#34;: null, &#34;enable_ha&#34;: null, &#34;enabled_drs&#34;: true, &#34;enabled_vsan&#34;: false, &#34;ha_admission_control_enabled&#34;: null, &#34;ha_failover_level&#34;: null, &#34;ha_host_monitoring&#34;: null, &#34;ha_restart_priority&#34;: null, &#34;ha_vm_failure_interval&#34;: null, &#34;ha_vm_max_failure_window&#34;: null, &#34;ha_vm_max_failures&#34;: null, &#34;ha_vm_min_up_time&#34;: null, &#34;ha_vm_monitoring&#34;: null, &#34;ha_vm_tools_monitoring&#34;: null, &#34;hosts&#34;: [{&#34;folder&#34;: &#34;/DC0/host/DC0_C0&#34;, &#34;name&#34;: &#34;esxi01.vsphere.local&#34;}, {&#34;folder&#34;: &#34;/DC0/host/DC0_C0&#34;, &#34;name&#34;: &#34;esxi02.vsphere.local&#34;}, {&#34;folder&#34;: &#34;/DC0/host/DC0_C0&#34;, &#34;name&#34;: &#34;esxi03.vsphere.local&#34;}, {&#34;folder&#34;: &#34;/DC0/host/DC0_C0&#34;, &#34;name&#34;: &#34;esxi04.vsphere.local&#34;}], &#34;moid&#34;: &#34;domain-c9&#34;, &#34;resource_summary&#34;: {&#34;cpuCapacityMHz&#34;: 4224, &#34;cpuUsedMHz&#34;: 87, &#34;memCapacityMB&#34;: 6139, &#34;memUsedMB&#34;: 1254, &#34;pMemAvailableMB&#34;: 0, &#34;pMemCapacityMB&#34;: 0, &#34;storageCapacityMB&#34;: 33280, &#34;storageUsedMB&#34;: 19953}, &#34;tags&#34;: [{&#34;category_id&#34;: &#34;urn:vmomi:InventoryServiceCategory:9fbf83de-7903-442e-8004-70fd3940297c:GLOBAL&#34;, &#34;category_name&#34;: &#34;sample_cluster_cat_0001&#34;, &#34;description&#34;: &#34;&#34;, &#34;id&#34;: &#34;urn:vmomi:InventoryServiceTag:93d680db-b3a6-4834-85ad-3e9516e8fee8:GLOBAL&#34;, &#34;name&#34;: &#34;sample_cluster_tag_0001&#34;}], &#34;vsan_auto_claim_storage&#34;: false}}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Christian Neugum (@digifuchsi)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

