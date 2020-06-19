:orphan:

.. _community.vmware.vmware_dvs_portgroup_module:


*************************************
community.vmware.vmware_dvs_portgroup
*************************************

**Create or remove a Distributed vSwitch portgroup.**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Create or remove a Distributed vSwitch portgroup.



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
                    <b>network_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"forged_transmits": false, "mac_changes": false, "promiscuous": false}</div>
                                    </td>
                                                                <td>
                                            <div>Dictionary which configures the different security values for portgroup.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>promiscuous</code> (bool): indicates whether promiscuous mode is allowed. (default: false)</div>
                                            <div>- <code>forged_transmits</code> (bool): indicates whether forged transmits are allowed. (default: false)</div>
                                            <div>- <code>mac_changes</code> (bool): indicates whether mac changes are allowed. (default: false)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>num_ports</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The number of ports the portgroup should contain.</div>
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
                    <b>port_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"block_override": true, "ipfix_override": false, "live_port_move": false, "network_rp_override": false, "port_config_reset_at_disconnect": true, "security_override": false, "shaping_override": false, "traffic_filter_override": false, "uplink_teaming_override": false, "vendor_config_override": false, "vlan_override": false}</div>
                                    </td>
                                                                <td>
                                            <div>Dictionary which configures the advanced policy settings for the portgroup.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>block_override</code> (bool): indicates if the block policy can be changed per port. (default: true)</div>
                                            <div>- <code>ipfix_override</code> (bool): indicates if the ipfix policy can be changed per port. (default: false)</div>
                                            <div>- <code>live_port_move</code> (bool): indicates if a live port can be moved in or out of the portgroup. (default: false)</div>
                                            <div>- <code>network_rp_override</code> (bool): indicates if the network resource pool can be changed per port. (default: false)</div>
                                            <div>- <code>port_config_reset_at_disconnect</code> (bool): indicates if the configuration of a port is reset automatically after disconnect. (default: true)</div>
                                            <div>- <code>security_override</code> (bool): indicates if the security policy can be changed per port. (default: false)</div>
                                            <div>- <code>shaping_override</code> (bool): indicates if the shaping policy can be changed per port. (default: false)</div>
                                            <div>- <code>traffic_filter_override</code> (bool): indicates if the traffic filter can be changed per port. (default: false)</div>
                                            <div>- <code>uplink_teaming_override</code> (bool): indicates if the uplink teaming policy can be changed per port. (default: false)</div>
                                            <div>- <code>vendor_config_override</code> (bool): indicates if the vendor config can be changed per port. (default: false)</div>
                                            <div>- <code>vlan_override</code> (bool): indicates if the vlan can be changed per port. (default: false)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>portgroup_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the portgroup that is to be created or deleted.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>portgroup_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>earlyBinding</li>
                                                                                                                                                                                                <li>lateBinding</li>
                                                                                                                                                                                                <li>ephemeral</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>See VMware KB 1022312 regarding portgroup types.</div>
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
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>present</li>
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
                    <b>switch_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The name of the distributed vSwitch the port group should be created on.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>teaming_policy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"inbound_policy": false, "load_balance_policy": "loadbalance_srcid", "notify_switches": true, "rolling_order": false}</div>
                                    </td>
                                                                <td>
                                            <div>Dictionary which configures the different teaming values for portgroup.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>load_balance_policy</code> (string): Network adapter teaming policy. (default: loadbalance_srcid)</div>
                                            <div>- choices: [ loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, loadbalance_loadbased, failover_explicit]</div>
                                            <div>- &quot;loadbalance_loadbased&quot; is available from version 2.6 and onwards</div>
                                            <div>- <code>inbound_policy</code> (bool): Indicate whether or not the teaming policy is applied to inbound frames as well. (default: False)</div>
                                            <div>- <code>notify_switches</code> (bool): Indicate whether or not to notify the physical switch if a link fails. (default: True)</div>
                                            <div>- <code>rolling_order</code> (bool): Indicate whether or not to use a rolling policy when restoring links. (default: False)</div>
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
                        <span style="color: purple">string</span>
                                                 / <span style="color: red">required</span>                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The VLAN ID that should be configured with the portgroup, use 0 for no VLAN.</div>
                                            <div>If <code>vlan_trunk</code> is configured to be <em>true</em>, this can be a combination of multiple ranges and numbers, example: 1-200, 205, 400-4094.</div>
                                            <div>The valid <code>vlan_id</code> range is from 0 to 4094. Overlapping ranges are allowed.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_trunk</b>
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
                                            <div>Indicates whether this is a VLAN trunk or not.</div>
                                                        </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
   - Tested on vSphere 5.5
   - Tested on vSphere 6.5



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create vlan portgroup
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: vlan-123-portrgoup
        switch_name: dvSwitch
        vlan_id: 123
        num_ports: 120
        portgroup_type: earlyBinding
        state: present
      delegate_to: localhost

    - name: Create vlan trunk portgroup
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: vlan-trunk-portrgoup
        switch_name: dvSwitch
        vlan_id: 1-1000, 1005, 1100-1200
        vlan_trunk: True
        num_ports: 120
        portgroup_type: earlyBinding
        state: present
      delegate_to: localhost

    - name: Create no-vlan portgroup
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: no-vlan-portrgoup
        switch_name: dvSwitch
        vlan_id: 0
        num_ports: 120
        portgroup_type: earlyBinding
        state: present
      delegate_to: localhost

    - name: Create vlan portgroup with all security and port policies
      community.vmware.vmware_dvs_portgroup:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        portgroup_name: vlan-123-portrgoup
        switch_name: dvSwitch
        vlan_id: 123
        num_ports: 120
        portgroup_type: earlyBinding
        state: present
        network_policy:
          promiscuous: yes
          forged_transmits: yes
          mac_changes: yes
        port_policy:
          block_override: yes
          ipfix_override: yes
          live_port_move: yes
          network_rp_override: yes
          port_config_reset_at_disconnect: yes
          security_override: yes
          shaping_override: yes
          traffic_filter_override: yes
          uplink_teaming_override: yes
          vendor_config_override: yes
          vlan_override: yes
      delegate_to: localhost





Status
------


Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Philippe Dellaert (@pdellaert) <philippe@dellaert.org>


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
