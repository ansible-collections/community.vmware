.. _community.vmware.vmware_dvswitch_lacp_module:


*************************************
community.vmware.vmware_dvswitch_lacp
*************************************

**Manage LACP configuration on a Distributed Switch**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to configure Link Aggregation Control Protocol (LACP) support mode and Link Aggregation Groups (LAGs).



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
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="2">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>link_aggregation_groups</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Can only be used if <code>lacp_support</code> is set to <code>enhanced</code>.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>load_balancing_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"srcDestIpTcpUdpPortVlan"</div>
                </td>
                <td>
                        <div>Load balancing algorithm.</div>
                        <div>Valid values are as follows</div>
                        <div>- srcTcpUdpPort: Source TCP/UDP port number.</div>
                        <div>- srcDestIpTcpUdpPortVlan: Source and destination IP, source and destination TCP/UDP port number and VLAN.</div>
                        <div>- srcIpVlan: Source IP and VLAN.</div>
                        <div>- srcDestTcpUdpPort: Source and destination TCP/UDP port number.</div>
                        <div>- srcMac: Source MAC address.</div>
                        <div>- destIp: Destination IP.</div>
                        <div>- destMac: Destination MAC address.</div>
                        <div>- vlan: VLAN only.</div>
                        <div>- srcDestIp: Source and Destination IP.</div>
                        <div>- srcIpTcpUdpPortVlan: Source IP, TCP/UDP port number and VLAN.</div>
                        <div>- srcDestIpTcpUdpPort: Source and destination IP and TCP/UDP port number.</div>
                        <div>- srcDestMac: Source and destination MAC address.</div>
                        <div>- destIpTcpUdpPort: Destination IP and TCP/UDP port number.</div>
                        <div>- srcPortId: Source Virtual Port Id.</div>
                        <div>- srcIp: Source IP.</div>
                        <div>- srcIpTcpUdpPort: Source IP and TCP/UDP port number.</div>
                        <div>- destIpTcpUdpPortVlan: Destination IP, TCP/UDP port number and VLAN.</div>
                        <div>- destTcpUdpPort: Destination TCP/UDP port number.</div>
                        <div>- destIpVlan: Destination IP and VLAN.</div>
                        <div>- srcDestIpVlan: Source and destination IP and VLAN.</div>
                        <div>Please see examples for more information.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>active</li>
                                    <li>passive</li>
                        </ul>
                </td>
                <td>
                        <div>The negotiating state of the uplinks/ports.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the LAG.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>uplink_number</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Number of uplinks.</div>
                        <div>Can 1 to 30.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
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
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>support_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>basic</b>&nbsp;&larr;</div></li>
                                    <li>enhanced</li>
                        </ul>
                </td>
                <td>
                        <div>The LACP support mode.</div>
                        <div><code>basic</code>: One Link Aggregation Control Protocol group in the switch (singleLag).</div>
                        <div><code>enhanced</code>: Multiple Link Aggregation Control Protocol groups in the switch (multipleLag).</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switch</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The name of the Distributed Switch to manage.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: dvswitch</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
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
                <td colspan="2">
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
    </table>
    <br/>


Notes
-----

.. note::
   - Tested on vSphere 6.7
   - You need to run the task two times if you want to remove all LAGs and change the support mode to 'basic'
   - All modules requires API write access and hence is not supported on a free ESXi license.



Examples
--------

.. code-block:: yaml

    - name: Enable enhanced mode on a Distributed Switch
      community.vmware.vmware_dvswitch_lacp:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        support_mode: enhanced
        validate_certs: "{{ validate_vcenter_certs }}"
      delegate_to: localhost
      loop_control:
        label: "{{ item.name }}"
      with_items: "{{ vcenter_distributed_switches }}"

    - name: Enable enhanced mode and create two LAGs on a Distributed Switch
      community.vmware.vmware_dvswitch_lacp:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        support_mode: enhanced
        link_aggregation_groups:
            - name: lag1
              uplink_number: 2
              mode: active
              load_balancing_mode: srcDestIpTcpUdpPortVlan
            - name: lag2
              uplink_number: 2
              mode: passive
              load_balancing_mode: srcDestIp
        validate_certs: "{{ validate_vcenter_certs }}"
      delegate_to: localhost
      loop_control:
        label: "{{ item.name }}"
      with_items: "{{ vcenter_distributed_switches }}"



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
                      <span style="color: purple">string</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>information about performed operation</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;changed&#x27;: True, &#x27;dvswitch&#x27;: &#x27;dvSwitch&#x27;, &#x27;link_aggregation_groups&#x27;: [{&#x27;load_balancing_mode&#x27;: &#x27;srcDestIpTcpUdpPortVlan&#x27;, &#x27;mode&#x27;: &#x27;active&#x27;, &#x27;name&#x27;: &#x27;lag1&#x27;, &#x27;uplink_number&#x27;: 2}, {&#x27;load_balancing_mode&#x27;: &#x27;srcDestIp&#x27;, &#x27;mode&#x27;: &#x27;active&#x27;, &#x27;name&#x27;: &#x27;lag2&#x27;, &#x27;uplink_number&#x27;: 2}], &#x27;link_aggregation_groups_previous&#x27;: [], &#x27;support_mode&#x27;: &#x27;enhanced&#x27;, &#x27;result&#x27;: &#x27;lacp lags changed&#x27;}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Christian Kotte (@ckotte)
