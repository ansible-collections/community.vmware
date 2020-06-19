:orphan:

.. _community.vmware.vmware_portgroup_module:


*********************************
community.vmware.vmware_portgroup
*********************************

**Create a VMware portgroup**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Create a VMware Port Group on a VMware Standard Switch (vSS) for given ESXi host(s) or hosts of given cluster.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.6
- PyVmomi


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
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Name of cluster name for host membership.</div>
                                            <div>Portgroup will be created on all hosts of the given cluster.</div>
                                            <div>This option is required if <code>hosts</code> is not specified.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: cluster</div>
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
                    <b>hosts</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>List of name of host or hosts on which portgroup needs to be added.</div>
                                            <div>This option is required if <code>cluster_name</code> is not specified.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: esxi_hostname</div>
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
                    <b>portgroup</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Portgroup name to add.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: portgroup_name</div>
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
                    <b>security</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Network policy specifies layer 2 security settings for a portgroup such as promiscuous mode, where guest adapter listens to all the packets, MAC address changes and forged transmits.</div>
                                            <div>Dict which configures the different security values for portgroup.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>promiscuous_mode</code> (bool): indicates whether promiscuous mode is allowed. (default: None)</div>
                                            <div>- <code>forged_transmits</code> (bool): indicates whether forged transmits are allowed. (default: None)</div>
                                            <div>- <code>mac_changes</code> (bool): indicates whether mac changes are allowed. (default: None)</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: security_policy, network_policy</div>
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
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>Determines if the portgroup should be present or not.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switch</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>vSwitch to modify.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: switch_name, vswitch</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>teaming</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Dictionary which configures the different teaming values for portgroup.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>load_balancing</code> (string): Network adapter teaming policy. <code>load_balance_policy</code> is also alias to this option. (default: loadbalance_srcid)</div>
                                            <div>- choices: [ loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit ]</div>
                                            <div>- <code>network_failure_detection</code> (string): Network failure detection. (default: link_status_only)</div>
                                            <div>- choices: [ link_status_only, beacon_probing ]</div>
                                            <div>- <code>notify_switches</code> (bool): Indicate whether or not to notify the physical switch if a link fails. (default: None)</div>
                                            <div>- <code>failback</code> (bool): Indicate whether or not to use a failback when restoring links. (default: None)</div>
                                            <div>- <code>active_adapters</code> (list): List of active adapters used for load balancing.</div>
                                            <div>- <code>standby_adapters</code> (list): List of standby adapters used for failover.</div>
                                            <div>- All vmnics are used as active adapters if <code>active_adapters</code> and <code>standby_adapters</code> are not defined.</div>
                                            <div>- <code>inbound_policy</code> (bool): Indicate whether or not the teaming policy is applied to inbound frames as well. Deprecated. (default: False)</div>
                                            <div>- <code>rolling_order</code> (bool): Indicate whether or not to use a rolling policy when restoring links. Deprecated. (default: False)</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: teaming_policy</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>traffic_shaping</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Dictionary which configures traffic shaping for the switch.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>enabled</code> (bool): Status of Traffic Shaping Policy. (default: None)</div>
                                            <div>- <code>average_bandwidth</code> (int): Average bandwidth (kbit/s). (default: None)</div>
                                            <div>- <code>peak_bandwidth</code> (int): Peak bandwidth (kbit/s). (default: None)</div>
                                            <div>- <code>burst_size</code> (int): Burst size (KB). (default: None)</div>
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
                                            <div>If set to <code>yes</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">0</div>
                                    </td>
                                                                <td>
                                            <div>VLAN ID to assign to portgroup.</div>
                                            <div>Set to 0 (no VLAN tagging) by default.</div>
                                                                <div style="font-size: small; color: darkgreen"><br/>aliases: vlan</div>
                                    </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
   - Tested on vSphere 5.5 and 6.5
   - Complete configuration only tested on vSphere 6.5
   - ``inbound_policy`` and ``rolling_order`` are deprecated and will be removed in 2.11
   - Those two options are only used during portgroup creation. Updating isn't supported with those options.



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add Management Network VM Portgroup
      community.vmware.vmware_portgroup:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
      delegate_to: localhost

    - name: Add Portgroup with Promiscuous Mode Enabled
      community.vmware.vmware_portgroup:
        hostname: "{{ esxi_hostname }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        security:
            promiscuous_mode: True
      delegate_to: localhost

    - name: Add Management Network VM Portgroup to specific hosts
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        hosts: [esxi_hostname_one]
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
      delegate_to: localhost

    - name: Add Management Network VM Portgroup to all hosts in a cluster
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        cluster_name: "{{ cluster_name }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
      delegate_to: localhost

    - name: Remove Management Network VM Portgroup to all hosts in a cluster
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        cluster_name: "{{ cluster_name }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: "{{ vlan_id }}"
        state: absent
      delegate_to: localhost

    - name: Add Portgroup with all settings defined
      community.vmware.vmware_portgroup:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ inventory_hostname }}"
        switch: "{{ vswitch_name }}"
        portgroup: "{{ portgroup_name }}"
        vlan_id: 10
        security:
            promiscuous_mode: False
            mac_changes: False
            forged_transmits: False
        traffic_shaping:
            enabled: True
            average_bandwidth: 100000
            peak_bandwidth: 100000
            burst_size: 102400
        teaming:
            load_balancing: failover_explicit
            network_failure_detection: link_status_only
            notify_switches: true
            failback: true
            active_adapters:
                - vmnic0
            standby_adapters:
                - vmnic1
      delegate_to: localhost
      register: teaming_result




Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>result</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                                                        <div>metadata about the portgroup</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;esxi01.example.com&#x27;: {&#x27;changed&#x27;: True, &#x27;failback&#x27;: &#x27;No override&#x27;, &#x27;failover_active&#x27;: &#x27;No override&#x27;, &#x27;failover_standby&#x27;: &#x27;No override&#x27;, &#x27;failure_detection&#x27;: &#x27;No override&#x27;, &#x27;load_balancing&#x27;: &#x27;No override&#x27;, &#x27;msg&#x27;: &#x27;Port Group added&#x27;, &#x27;notify_switches&#x27;: &#x27;No override&#x27;, &#x27;portgroup&#x27;: &#x27;vMotion&#x27;, &#x27;sec_forged_transmits&#x27;: False, &#x27;sec_mac_changes&#x27;: False, &#x27;sec_promiscuous_mode&#x27;: False, &#x27;traffic_shaping&#x27;: &#x27;No override&#x27;, &#x27;vlan_id&#x27;: 33, &#x27;vswitch&#x27;: &#x27;vSwitch1&#x27;}}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Russell Teague (@mtnbikenc)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
