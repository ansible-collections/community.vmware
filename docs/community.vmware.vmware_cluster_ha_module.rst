
.. Created with antsibull-docs 2.5.0

community.vmware.vmware_cluster_ha module -- Manage High Availability (HA) on VMware vSphere clusters
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/ui/repo/published/community/vmware/>`_ (version 3.10.0).

It is not included in ``ansible-core``.
To check whether it is installed, run ``ansible-galaxy collection list``.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: ``community.vmware.vmware_cluster_ha``.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Manages HA configuration on VMware vSphere clusters.
- All values and VMware object names are case sensitive.








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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-advanced_settings"></div>
      <p style="display: inline;"><strong>advanced_settings</strong></p>
      <a class="ansibleOptionLink" href="#parameter-advanced_settings" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>A dictionary of advanced HA settings.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">{}</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-apd_delay"></div>
      <p style="display: inline;"><strong>apd_delay</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apd_delay" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.9.0</i></p>
    </td>
    <td valign="top">
      <p>The response recovery delay time in sec for storage failures categorized as All Paths Down (APD).</p>
      <p>Only set if <code class='docutils literal notranslate'>apd_response</code> is <code class='docutils literal notranslate'>restartConservative</code> or <code class='docutils literal notranslate'>restartAggressive</code>.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">180</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-apd_reaction"></div>
      <p style="display: inline;"><strong>apd_reaction</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apd_reaction" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.9.0</i></p>
    </td>
    <td valign="top">
      <p>VM response recovery reaction for storage failures categorized as All Paths Down (APD).</p>
      <p>Only set if <code class='docutils literal notranslate'>apd_response</code> is <code class='docutils literal notranslate'>restartConservative</code> or <code class='docutils literal notranslate'>restartAggressive</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;reset&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;none&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-apd_response"></div>
      <p style="display: inline;"><strong>apd_response</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apd_response" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>VM storage protection setting for storage failures categorized as All Paths Down (APD).</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;disabled&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;warning&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;restartConservative&#34;</code></p></li>
        <li><p><code>&#34;restartAggressive&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-cluster_name"></div>
      <p style="display: inline;"><strong>cluster_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the cluster to be managed.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <div class="ansibleOptionAnchor" id="parameter-datacenter_name"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: datacenter_name</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>The name of the datacenter.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-enable"></div>
      <p style="display: inline;"><strong>enable</strong></p>
      <a class="ansibleOptionLink" href="#parameter-enable" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Whether to enable HA.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-failover_host_admission_control"></div>
      <p style="display: inline;"><strong>failover_host_admission_control</strong></p>
      <a class="ansibleOptionLink" href="#parameter-failover_host_admission_control" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Configure dedicated failover hosts.</p>
      <p><code class='docutils literal notranslate'>slot_based_admission_control</code>, <code class='docutils literal notranslate'>reservation_based_admission_control</code> and <code class='docutils literal notranslate'>failover_host_admission_control</code> are mutually exclusive.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-failover_host_admission_control/failover_hosts"></div>
      <p style="display: inline;"><strong>failover_hosts</strong></p>
      <a class="ansibleOptionLink" href="#parameter-failover_host_admission_control/failover_hosts" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>List of dedicated failover hosts.</p>
    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ha_host_monitoring"></div>
      <p style="display: inline;"><strong>ha_host_monitoring</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ha_host_monitoring" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Whether HA restarts virtual machines after a host fails.</p>
      <p>If set to <code class='docutils literal notranslate'>enabled</code>, HA restarts virtual machines after a host fails.</p>
      <p>If set to <code class='docutils literal notranslate'>disabled</code>, HA does not restart virtual machines after a host fails.</p>
      <p>If <code class='docutils literal notranslate'>enable</code> is set to <code class='docutils literal notranslate'>false</code>, then this value is ignored.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;enabled&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;disabled&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ha_restart_priority"></div>
      <p style="display: inline;"><strong>ha_restart_priority</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ha_restart_priority" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Priority HA gives to a virtual machine if sufficient capacity is not available to power on all failed virtual machines.</p>
      <p>Valid only if <em>ha_vm_monitoring</em> is set to either <code class='docutils literal notranslate'>vmAndAppMonitoring</code> or <code class='docutils literal notranslate'>vmMonitoringOnly</code>.</p>
      <p>If set to <code class='docutils literal notranslate'>disabled</code>, then HA is disabled for this virtual machine.</p>
      <p>If set to <code class='docutils literal notranslate'>high</code>, then virtual machine with this priority have a higher chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.</p>
      <p>If set to <code class='docutils literal notranslate'>medium</code>, then virtual machine with this priority have an intermediate chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.</p>
      <p>If set to <code class='docutils literal notranslate'>low</code>, then virtual machine with this priority have a lower chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;disabled&#34;</code></p></li>
        <li><p><code>&#34;high&#34;</code></p></li>
        <li><p><code>&#34;low&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;medium&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ha_vm_failure_interval"></div>
      <p style="display: inline;"><strong>ha_vm_failure_interval</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ha_vm_failure_interval" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The number of seconds after which virtual machine is declared as failed if no heartbeat has been received.</p>
      <p>This setting is only valid if <code class='docutils literal notranslate'>ha_vm_monitoring</code> is set to, either <code class='docutils literal notranslate'>vmAndAppMonitoring</code> or <code class='docutils literal notranslate'>vmMonitoringOnly</code>.</p>
      <p>Unit is seconds.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">30</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ha_vm_max_failure_window"></div>
      <p style="display: inline;"><strong>ha_vm_max_failure_window</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ha_vm_max_failure_window" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The number of seconds for the window during which up to <code class='docutils literal notranslate'>ha_vm_max_failures</code> resets can occur before automated responses stop.</p>
      <p>Valid only when <em>ha_vm_monitoring</em> is set to either <code class='docutils literal notranslate'>vmAndAppMonitoring</code> or <code class='docutils literal notranslate'>vmMonitoringOnly</code>.</p>
      <p>Unit is seconds.</p>
      <p>Default specifies no failure window.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">-1</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ha_vm_max_failures"></div>
      <p style="display: inline;"><strong>ha_vm_max_failures</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ha_vm_max_failures" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Maximum number of failures and automated resets allowed during the time that <code class='docutils literal notranslate'>ha_vm_max_failure_window</code> specifies.</p>
      <p>Valid only when <em>ha_vm_monitoring</em> is set to either <code class='docutils literal notranslate'>vmAndAppMonitoring</code> or <code class='docutils literal notranslate'>vmMonitoringOnly</code>.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">3</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ha_vm_min_up_time"></div>
      <p style="display: inline;"><strong>ha_vm_min_up_time</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ha_vm_min_up_time" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The number of seconds for the virtual machine&#x27;s heartbeats to stabilize after the virtual machine has been powered on.</p>
      <p>Valid only when <em>ha_vm_monitoring</em> is set to either <code class='docutils literal notranslate'>vmAndAppMonitoring</code> or <code class='docutils literal notranslate'>vmMonitoringOnly</code>.</p>
      <p>Unit is seconds.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">120</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-ha_vm_monitoring"></div>
      <p style="display: inline;"><strong>ha_vm_monitoring</strong></p>
      <a class="ansibleOptionLink" href="#parameter-ha_vm_monitoring" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>State of virtual machine health monitoring service.</p>
      <p>If set to <code class='docutils literal notranslate'>vmAndAppMonitoring</code>, HA response to both virtual machine and application heartbeat failure.</p>
      <p>If set to <code class='docutils literal notranslate'>vmMonitoringDisabled</code>, virtual machine health monitoring is disabled.</p>
      <p>If set to <code class='docutils literal notranslate'>vmMonitoringOnly</code>, HA response to virtual machine heartbeat failure.</p>
      <p>If <code class='docutils literal notranslate'>enable</code> is set to <code class='docutils literal notranslate'>false</code>, then this value is ignored.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;vmAndAppMonitoring&#34;</code></p></li>
        <li><p><code>&#34;vmMonitoringOnly&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;vmMonitoringDisabled&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-host_isolation_response"></div>
      <p style="display: inline;"><strong>host_isolation_response</strong></p>
      <a class="ansibleOptionLink" href="#parameter-host_isolation_response" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Indicates whether or VMs should be powered off if a host determines that it is isolated from the rest of the compute resource.</p>
      <p>If set to <code class='docutils literal notranslate'>none</code>, do not power off VMs in the event of a host network isolation.</p>
      <p>If set to <code class='docutils literal notranslate'>powerOff</code>, power off VMs in the event of a host network isolation.</p>
      <p>If set to <code class='docutils literal notranslate'>shutdown</code>, shut down VMs guest operating system in the event of a host network isolation.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;none&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;powerOff&#34;</code></p></li>
        <li><p><code>&#34;shutdown&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-pdl_response"></div>
      <p style="display: inline;"><strong>pdl_response</strong></p>
      <a class="ansibleOptionLink" href="#parameter-pdl_response" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>VM storage protection setting for storage failures categorized as Permenant Device Loss (PDL).</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;disabled&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;warning&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;restartAggressive&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-reservation_based_admission_control"></div>
      <p style="display: inline;"><strong>reservation_based_admission_control</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reservation_based_admission_control" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Configure reservation based admission control policy.</p>
      <p><code class='docutils literal notranslate'>slot_based_admission_control</code>, <code class='docutils literal notranslate'>reservation_based_admission_control</code> and <code class='docutils literal notranslate'>failover_host_admission_control</code> are mutually exclusive.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-reservation_based_admission_control/auto_compute_percentages"></div>
      <p style="display: inline;"><strong>auto_compute_percentages</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reservation_based_admission_control/auto_compute_percentages" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>By default, <code class='docutils literal notranslate'>failover_level</code> is used to calculate <code class='docutils literal notranslate'>cpu_failover_resources_percent</code> and <code class='docutils literal notranslate'>memory_failover_resources_percent</code>. If a user wants to override the percentage values, he has to set this field to false.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-reservation_based_admission_control/cpu_failover_resources_percent"></div>
      <p style="display: inline;"><strong>cpu_failover_resources_percent</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reservation_based_admission_control/cpu_failover_resources_percent" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Percentage of CPU resources in the cluster to reserve for failover. Ignored if <code class='docutils literal notranslate'>auto_compute_percentages</code> is not set to false.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">50</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-reservation_based_admission_control/failover_level"></div>
      <p style="display: inline;"><strong>failover_level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reservation_based_admission_control/failover_level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Number of host failures that should be tolerated.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-reservation_based_admission_control/memory_failover_resources_percent"></div>
      <p style="display: inline;"><strong>memory_failover_resources_percent</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reservation_based_admission_control/memory_failover_resources_percent" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Percentage of memory resources in the cluster to reserve for failover. Ignored if <code class='docutils literal notranslate'>auto_compute_percentages</code> is not set to false.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">50</code></p>
    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
      <div class="ansibleOptionAnchor" id="parameter-slot_based_admission_control"></div>
      <p style="display: inline;"><strong>slot_based_admission_control</strong></p>
      <a class="ansibleOptionLink" href="#parameter-slot_based_admission_control" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>Configure slot based admission control policy.</p>
      <p><code class='docutils literal notranslate'>slot_based_admission_control</code>, <code class='docutils literal notranslate'>reservation_based_admission_control</code> and <code class='docutils literal notranslate'>failover_host_admission_control</code> are mutually exclusive.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-slot_based_admission_control/failover_level"></div>
      <p style="display: inline;"><strong>failover_level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-slot_based_admission_control/failover_level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Number of host failures that should be tolerated.</p>
    </td>
  </tr>

  <tr>
    <td colspan="2" valign="top">
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
    <td colspan="2" valign="top">
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
  </tbody>
  </table>




Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Enable HA without admission control
      community.vmware.vmware_cluster_ha:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        enable: true
      delegate_to: localhost

    - name: Enable HA and VM monitoring without admission control
      community.vmware.vmware_cluster_ha:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter_name: DC0
        cluster_name: "{{ cluster_name }}"
        enable: true
        ha_vm_monitoring: vmMonitoringOnly
      delegate_to: localhost

    - name: Enable HA with admission control reserving 50% of resources for HA
      community.vmware.vmware_cluster_ha:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        enable: true
        reservation_based_admission_control:
          auto_compute_percentages: false
          failover_level: 1
          cpu_failover_resources_percent: 50
          memory_failover_resources_percent: 50
      delegate_to: localhost







Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

