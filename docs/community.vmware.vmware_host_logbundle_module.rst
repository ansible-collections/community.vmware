

community.vmware.vmware_host_logbundle module -- Fetch logbundle file from ESXi
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_logbundle`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to fetch logbundle file from ESXi.








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
      <div class="ansibleOptionAnchor" id="parameter-dest"></div>
      <p style="display: inline;"><strong>dest</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dest" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>file destination on localhost, path must be exist.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Name of the host system to fetch the logbundle.</p>
    </td>
  </tr>
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
      <div class="ansibleOptionAnchor" id="parameter-manifests"></div>
      <p style="display: inline;"><strong>manifests</strong></p>
      <a class="ansibleOptionLink" href="#parameter-manifests" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>Logs to include in the logbundle file.</p>
      <p>Refer to the id key of the <a href='../../community/vmware/vmware_host_logbundle_info_module.html' class='module'>community.vmware.vmware_host_logbundle_info</a> module for values that can be specified in the manifest.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[&#34;System:Base&#34;, &#34;System:CoreDumps&#34;, &#34;System:EsxImage&#34;, &#34;System:IOFilter&#34;, &#34;System:LoadESX&#34;, &#34;System:Modules&#34;, &#34;System:RDMA&#34;, &#34;System:ResourceGroups&#34;, &#34;System:TPM&#34;, &#34;System:VFlash&#34;, &#34;System:VMTools&#34;, &#34;System:VmiofPlugins&#34;, &#34;System:ntp&#34;, &#34;System:uwstats&#34;, &#34;Fcd:Catalog&#34;, &#34;VirtualMachines:CoreDumps&#34;, &#34;VirtualMachines:VirtualMachineStats&#34;, &#34;VirtualMachines:base&#34;, &#34;VirtualMachines:base&#34;, &#34;VirtualMachines:diskinfo&#34;, &#34;VirtualMachines:logs&#34;, &#34;Storage:FCoE&#34;, &#34;Storage:Multipathing&#34;, &#34;Storage:NAS&#34;, &#34;Storage:VSAN&#34;, &#34;Storage:VSANHealth&#34;, &#34;Storage:VSANIscsiTarget&#34;, &#34;Storage:VSANPerfStats&#34;, &#34;Storage:VSANPerfSvc&#34;, &#34;Storage:VSANTraces&#34;, &#34;Storage:VVOL&#34;, &#34;Storage:base&#34;, &#34;Storage:iodm&#34;, &#34;Storage:iscsi&#34;, &#34;FeatureStateSwitch:FeatureStateSwitch&#34;, &#34;Userworld:HostAgent&#34;, &#34;Userworld:ProcessInformation&#34;, &#34;Configuration:System&#34;, &#34;Logs:System&#34;, &#34;hostProfiles:SystemImageCacheHostProfile&#34;, &#34;hostProfiles:hostProfiles&#34;, &#34;FileSystem:VMFSDiskDump&#34;, &#34;FileSystem:base&#34;, &#34;ActiveDirectory:base&#34;, &#34;CIM:base&#34;, &#34;Hardware:base&#34;, &#34;Hardware:usb&#34;, &#34;Installer:base&#34;, &#34;Network:base&#34;, &#34;Network:dvs&#34;, &#34;Network:lacp&#34;, &#34;Network:nscd&#34;, &#34;Network:tcpip&#34;, &#34;IntegrityChecks:md5sums&#34;]</code></p>
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
      <div class="ansibleOptionAnchor" id="parameter-performance_data"></div>
      <p style="display: inline;"><strong>performance_data</strong></p>
      <a class="ansibleOptionLink" href="#parameter-performance_data" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Gather performance data for ESXi.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-performance_data/duration"></div>
      <p style="display: inline;"><strong>duration</strong></p>
      <a class="ansibleOptionLink" href="#parameter-performance_data/duration" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Duration for which performance data is gathered.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">300</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-performance_data/interval"></div>
      <p style="display: inline;"><strong>interval</strong></p>
      <a class="ansibleOptionLink" href="#parameter-performance_data/interval" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Interval for which performance data is gathered.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">5</code></p>
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
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
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

    
    - name: fetch logbundle file from ESXi
      community.vmware.vmware_host_logbundle:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        dest: ./esxi-log.tgz

    - name: fetch logbundle file from ESXi with manifests
      community.vmware.vmware_host_logbundle:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        dest: ./esxi-log.tgz
        manifests:
          - System:Base
          - VirtualMachines:VirtualMachineStats





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
      <div class="ansibleOptionAnchor" id="return-dest"></div>
      <p style="display: inline;"><strong>dest</strong></p>
      <a class="ansibleOptionLink" href="#return-dest" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>saved path of a logbundle file for ESXi</p>
      <p style="margin-top: 8px;"><b>Returned:</b> on success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>&#34;{&#39;changed&#39;: True, &#39;dest&#39;: &#39;./esxi-log.tgz&#39;, &#39;failed&#39;: False, &#39;gid&#39;: 0, &#39;group&#39;: &#39;root&#39;, &#39;mode&#39;: &#39;0644&#39;, &#39;owner&#39;: &#39;root&#39;, &#39;size&#39;: 25783140, &#39;state&#39;: &#39;file&#39;, &#39;uid&#39;: 0}&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

