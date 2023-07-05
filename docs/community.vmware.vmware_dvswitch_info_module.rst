

community.vmware.vmware_dvswitch_info module -- Gathers info dvswitch configurations
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_dvswitch_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about dvswitch configurations.








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
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Specify a folder location of dvswitch to gather information from.</p>
      <p>Examples:</p>
      <p>   folder: /datacenter1/network</p>
      <p>   folder: datacenter1/network</p>
      <p>   folder: /datacenter1/network/folder1</p>
      <p>   folder: datacenter1/network/folder1</p>
      <p>   folder: /folder1/datacenter1/network</p>
      <p>   folder: folder1/datacenter1/network</p>
      <p>   folder: /folder1/datacenter1/network/folder2</p>
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
      <p>If not specified, all properties are retrieved (deeply).</p>
      <p>Results are returned in a structure identical to the vsphere API.</p>
      <p>Example:</p>
      <p>   properties: [</p>
      <p>      "summary.name",</p>
      <p>      "summary.numPorts",</p>
      <p>      "config.maxMtu",</p>
      <p>      "overallStatus"</p>
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
      <p>The &#x27;summary&#x27; output schema is the legacy output from the module</p>
      <p>The &#x27;vsphere&#x27; output schema is the vSphere API class definition which requires pyvmomi&gt;6.7.1</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;summary&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;vsphere&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-switch_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-switch"></div>
      <div class="ansibleOptionAnchor" id="parameter-dvswitch"></div>
      <p style="display: inline;"><strong>switch_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-switch_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: switch, dvswitch</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of a dvswitch to look for.</p>
      <p>If <code class='docutils literal notranslate'>switch_name</code> not specified gather all dvswitch information.</p>
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

    
    - name: Gather all registered dvswitch
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
      delegate_to: localhost
      register: dvswitch_info

    - name: Gather info about specific dvswitch
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        switch_name: DVSwitch01
      delegate_to: localhost
      register: dvswitch_info

    - name: Gather info from folder about specific dvswitch
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: /datacenter1/network/F01
        switch_name: DVSwitch02
      delegate_to: localhost
      register: dvswitch_info

    - name: Gather some info from a dvswitch using the vSphere API output schema
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        schema: vsphere
        properties:
          - summary.name
          - summary.numPorts
          - config.maxMtu
          - overallStatus
        switch_name: DVSwitch01
      register: dvswitch_info





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
      <div class="ansibleOptionAnchor" id="return-distributed_virtual_switches"></div>
      <p style="display: inline;"><strong>distributed_virtual_switches</strong></p>
      <a class="ansibleOptionLink" href="#return-distributed_virtual_switches" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>list of dictionary of dvswitch and their information</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>[{&#34;configure&#34;: {&#34;folder&#34;: &#34;network&#34;, &#34;hosts&#34;: [&#34;esxi-test-02.local&#34;, &#34;esxi-test-01.local&#34;], &#34;settings&#34;: {&#34;healthCheck&#34;: {&#34;TeamingHealthCheckConfig&#34;: false, &#34;VlanMtuHealthCheckConfig&#34;: false}, &#34;netflow&#34;: {&#34;activeFlowTimeout&#34;: 60, &#34;collectorIpAddress&#34;: &#34;&#34;, &#34;collectorPort&#34;: 0, &#34;idleFlowTimeout&#34;: 15, &#34;internalFlowsOnly&#34;: false, &#34;observationDomainId&#34;: 0, &#34;samplingRate&#34;: 0, &#34;switchIpAddress&#34;: null}, &#34;privateVlan&#34;: [], &#34;properties&#34;: {&#34;administratorContact&#34;: {&#34;contact&#34;: null, &#34;name&#34;: null}, &#34;advanced&#34;: {&#34;maxMtu&#34;: 1500, &#34;multicastFilteringMode&#34;: &#34;legacyFiltering&#34;}, &#34;discoveryProtocol&#34;: {&#34;operation&#34;: &#34;listen&#34;, &#34;protocol&#34;: &#34;cdp&#34;}, &#34;general&#34;: {&#34;ioControl&#34;: true, &#34;name&#34;: &#34;DVSwitch01&#34;, &#34;numPorts&#34;: 10, &#34;numUplinks&#34;: 1, &#34;vendor&#34;: &#34;VMware, Inc.&#34;, &#34;version&#34;: &#34;6.6.0&#34;}}}}, &#34;uuid&#34;: &#34;50 30 99 9c a7 60 8a 4f-05 9f e7 b5 da df 8f 17&#34;}]</code></p>
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

