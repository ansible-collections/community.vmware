.. _community.vmware.vmware_cluster_module:


*******************************
community.vmware.vmware_cluster
*******************************

**Manage VMware vSphere clusters**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Adds or removes VMware vSphere clusters.
- Although this module can manage DRS, HA and VSAN related configurations, this functionality is deprecated and will be removed in 2.12.
- To manage DRS, HA and VSAN related configurations, use the new modules vmware_cluster_drs, vmware_cluster_ha and vmware_cluster_vsan.
- All values and VMware object names are case sensitive.



Requirements
------------
The below requirements are needed on the host that executes this module.

- Tested on ESXi 5.5 and 6.5.
- PyVmomi installed.


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cluster_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The name of the cluster to be managed.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datacenter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The name of the datacenter.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: datacenter_name</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drs_default_vm_behavior</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>fullyAutomated</b>&nbsp;&larr;</div></li>
                                    <li>manual</li>
                                    <li>partiallyAutomated</li>
                        </ul>
                </td>
                <td>
                        <div>Specifies the cluster-wide default DRS behavior for virtual machines.</div>
                        <div>If set to <code>partiallyAutomated</code>, then vCenter generate recommendations for virtual machine migration and for the placement with a host. vCenter automatically implement placement at power on.</div>
                        <div>If set to <code>manual</code>, then vCenter generate recommendations for virtual machine migration and for the placement with a host. vCenter should not implement the recommendations automatically.</div>
                        <div>If set to <code>fullyAutomated</code>, then vCenter should automate both the migration of virtual machines and their placement with a host at power on.</div>
                        <div>Use <code>drs_default_vm_behavior</code> of <span class='module'>community.vmware.vmware_cluster_drs</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drs_enable_vm_behavior_overrides</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Determines whether DRS Behavior overrides for individual virtual machines are enabled.</div>
                        <div>If set to <code>True</code>, overrides <code>drs_default_vm_behavior</code>.</div>
                        <div>Use <code>drs_enable_vm_behavior_overrides</code> of <span class='module'>community.vmware.vmware_cluster_drs</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>drs_vmotion_rate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>1</li>
                                    <li>2</li>
                                    <li><div style="color: blue"><b>3</b>&nbsp;&larr;</div></li>
                                    <li>4</li>
                                    <li>5</li>
                        </ul>
                </td>
                <td>
                        <div>Threshold for generated ClusterRecommendations.</div>
                        <div>Use <code>drs_vmotion_rate</code> of <span class='module'>community.vmware.vmware_cluster_drs</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable_drs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>True</code>, will enable DRS when the cluster is created.</div>
                        <div>Use <code>enable_drs</code> of <span class='module'>community.vmware.vmware_cluster_drs</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable_ha</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>True</code> will enable HA when the cluster is created.</div>
                        <div>Use <code>enable_ha</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>enable_vsan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>True</code> will enable vSAN when the cluster is created.</div>
                        <div>Use <code>enable_vsan</code> of <span class='module'>community.vmware.vmware_cluster_vsan</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_admission_control_enabled</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Determines if strict admission control is enabled.</div>
                        <div>It is recommended to set this parameter to <code>True</code>, please refer documentation for more details.</div>
                        <div>Use <code>slot_based_admission_control</code>, <code>reservation_based_admission_control</code> or <code>failover_host_admission_control</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_failover_level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">2</div>
                </td>
                <td>
                        <div>Number of host failures that should be tolerated, still guaranteeing sufficient resources to restart virtual machines on available hosts.</div>
                        <div>Accepts integer values only.</div>
                        <div>Use <code>slot_based_admission_control</code>, <code>reservation_based_admission_control</code> or <code>failover_host_admission_control</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_host_monitoring</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>enabled</b>&nbsp;&larr;</div></li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>Indicates whether HA restarts virtual machines after a host fails.</div>
                        <div>If set to <code>enabled</code>, HA restarts virtual machines after a host fails.</div>
                        <div>If set to <code>disabled</code>, HA does not restart virtual machines after a host fails.</div>
                        <div>If <code>enable_ha</code> is set to <code>False</code>, then this value is ignored.</div>
                        <div>Use <code>ha_host_monitoring</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_restart_priority</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>disabled</li>
                                    <li>high</li>
                                    <li>low</li>
                                    <li><div style="color: blue"><b>medium</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Determines the preference that HA gives to a virtual machine if sufficient capacity is not available to power on all failed virtual machines.</div>
                        <div>This setting is only valid if <code>ha_vm_monitoring</code> is set to, either <code>vmAndAppMonitoring</code> or <code>vmMonitoringOnly</code>.</div>
                        <div>If set to <code>disabled</code>, then HA is disabled for this virtual machine.</div>
                        <div>If set to <code>high</code>, then virtual machine with this priority have a higher chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.</div>
                        <div>If set to <code>medium</code>, then virtual machine with this priority have an intermediate chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.</div>
                        <div>If set to <code>low</code>, then virtual machine with this priority have a lower chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.</div>
                        <div>Use <code>ha_restart_priority</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_vm_failure_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">30</div>
                </td>
                <td>
                        <div>The number of seconds after which virtual machine is declared as failed if no heartbeat has been received.</div>
                        <div>This setting is only valid if <code>ha_vm_monitoring</code> is set to, either <code>vmAndAppMonitoring</code> or <code>vmMonitoringOnly</code>.</div>
                        <div>Unit is seconds.</div>
                        <div>Use <code>ha_vm_failure_interval</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_vm_max_failure_window</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">-1</div>
                </td>
                <td>
                        <div>The number of seconds for the window during which up to <code>ha_vm_max_failures</code> resets can occur before automated responses stop.</div>
                        <div>This setting is only valid if <code>ha_vm_monitoring</code> is set to, either <code>vmAndAppMonitoring</code> or <code>vmMonitoringOnly</code>.</div>
                        <div>Unit is seconds.</div>
                        <div>Default specifies no failure window.</div>
                        <div>Use <code>ha_vm_max_failure_window</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_vm_max_failures</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">3</div>
                </td>
                <td>
                        <div>Maximum number of failures and automated resets allowed during the time that <code>ha_vm_max_failure_window</code> specifies.</div>
                        <div>This setting is only valid if <code>ha_vm_monitoring</code> is set to, either <code>vmAndAppMonitoring</code> or <code>vmMonitoringOnly</code>.</div>
                        <div>Use <code>ha_vm_max_failures</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_vm_min_up_time</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">120</div>
                </td>
                <td>
                        <div>The number of seconds for the virtual machine&#x27;s heartbeats to stabilize after the virtual machine has been powered on.</div>
                        <div>This setting is only valid if <code>ha_vm_monitoring</code> is set to, either <code>vmAndAppMonitoring</code> or <code>vmMonitoringOnly</code>.</div>
                        <div>Unit is seconds.</div>
                        <div>Use <code>ha_vm_min_up_time</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ha_vm_monitoring</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>vmAndAppMonitoring</li>
                                    <li>vmMonitoringOnly</li>
                                    <li><div style="color: blue"><b>vmMonitoringDisabled</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Indicates the state of virtual machine health monitoring service.</div>
                        <div>If set to <code>vmAndAppMonitoring</code>, HA response to both virtual machine and application heartbeat failure.</div>
                        <div>If set to <code>vmMonitoringDisabled</code>, virtual machine health monitoring is disabled.</div>
                        <div>If set to <code>vmMonitoringOnly</code>, HA response to virtual machine heartbeat failure.</div>
                        <div>If <code>enable_ha</code> is set to <code>False</code>, then this value is ignored.</div>
                        <div>Use <code>ha_vm_monitoring</code> of <span class='module'>community.vmware.vmware_cluster_ha</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The hostname or IP address of the vSphere vCenter or ESXi server.</div>
                        <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_HOST</code> will be used instead.</div>
                        <div>Environment variable support added in Ansible 2.6.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ignore_drs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>True</code>, DRS will not be configured; all explicit and default DRS related configurations will be ignored.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ignore_ha</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>True</code>, HA will not be configured; all explicit and default HA related configurations will be ignored.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>ignore_vsan</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>True</code>, VSAN will not be configured; all explicit and default VSAN related configurations will be ignored.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The password of the vSphere vCenter or ESXi server.</div>
                        <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PASSWORD</code> will be used instead.</div>
                        <div>Environment variable support added in Ansible 2.6.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: pass, pwd</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">443</div>
                </td>
                <td>
                        <div>The port number of the vSphere vCenter or ESXi server.</div>
                        <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PORT</code> will be used instead.</div>
                        <div>Environment variable support added in Ansible 2.6.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>proxy_host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Address of a proxy that will receive all HTTPS requests and relay them.</div>
                        <div>The format is a hostname or a IP.</div>
                        <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PROXY_HOST</code> will be used instead.</div>
                        <div>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>proxy_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</div>
                        <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_PROXY_PORT</code> will be used instead.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>absent</li>
                                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Create <code>present</code> or remove <code>absent</code> a VMware vSphere cluster.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The username of the vSphere vCenter or ESXi server.</div>
                        <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_USER</code> will be used instead.</div>
                        <div>Environment variable support added in Ansible 2.6.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: admin, user</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Allows connection when SSL certificates are not valid. Set to <code>false</code> when certificates are not trusted.</div>
                        <div>If the value is not specified in the task, the value of environment variable <code>VMWARE_VALIDATE_CERTS</code> will be used instead.</div>
                        <div>Environment variable support added in Ansible 2.6.</div>
                        <div>If set to <code>true</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vsan_auto_claim_storage</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>Determines whether the VSAN service is configured to automatically claim local storage on VSAN-enabled hosts in the cluster.</div>
                        <div>Use <code>vsan_auto_claim_storage</code> of <span class='module'>community.vmware.vmware_cluster_vsan</span> instead.</div>
                        <div>Deprecated option, will be removed in version 2.12.</div>
                </td>
            </tr>
    </table>
    <br/>



See Also
--------

.. seealso::

   :ref:`community.vmware.vmware_cluster_drs_module`
      The official documentation on the **community.vmware.vmware_cluster_drs** module.
   :ref:`community.vmware.vmware_cluster_ha_module`
      The official documentation on the **community.vmware.vmware_cluster_ha** module.
   :ref:`community.vmware.vmware_cluster_vsan_module`
      The official documentation on the **community.vmware.vmware_cluster_vsan** module.


Examples
--------

.. code-block:: yaml

    - name: Create Cluster
      community.vmware.vmware_cluster:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        enable_ha: true
        enable_drs: true
        enable_vsan: true
      delegate_to: localhost

    - name: Create Cluster with additional changes
      community.vmware.vmware_cluster:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter_name: DC0
        cluster_name: "{{ cluster_name }}"
        enable_ha: True
        ha_vm_monitoring: vmMonitoringOnly
        enable_drs: True
        drs_default_vm_behavior: partiallyAutomated
        enable_vsan: True
      register: cl_result
      delegate_to: localhost

    - name: Delete Cluster
      community.vmware.vmware_cluster:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter_name: datacenter
        cluster_name: cluster
        enable_ha: true
        enable_drs: true
        enable_vsan: true
        state: absent
      delegate_to: localhost




Status
------


Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
