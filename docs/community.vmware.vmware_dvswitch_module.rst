.. _community.vmware.vmware_dvswitch_module:


********************************
community.vmware.vmware_dvswitch
********************************

**Create or remove a Distributed Switch**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to create, remove a Distributed Switch.



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
                    <b>contact</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Dictionary which configures administrator contact name and description for the Distributed Switch.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description or other details.</div>
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
                        <div>Administrator name.</div>
                </td>
            </tr>

            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datacenter_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The name of the datacenter that will contain the Distributed Switch.</div>
                        <div>This parameter is optional, if <code>folder</code> is provided.</div>
                        <div>Mutually exclusive with <code>folder</code> parameter.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: datacenter</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>description</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Description of the Distributed Switch.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>discovery_operation</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>both</li>
                                    <li>advertise</li>
                                    <li><div style="color: blue"><b>listen</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>Select the discovery operation.</div>
                        <div>Required parameter for <code>state</code> both <code>present</code> and <code>absent</code>, before Ansible 2.6 version.</div>
                        <div>Required only if <code>state</code> is set to <code>present</code>, for Ansible 2.6 and onwards.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>discovery_proto</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>cdp</b>&nbsp;&larr;</div></li>
                                    <li>lldp</li>
                                    <li>disabled</li>
                        </ul>
                </td>
                <td>
                        <div>Link discovery protocol between Cisco and Link Layer discovery.</div>
                        <div>Required parameter for <code>state</code> both <code>present</code> and <code>absent</code>, before Ansible 2.6 version.</div>
                        <div>Required only if <code>state</code> is set to <code>present</code>, for Ansible 2.6 and onwards.</div>
                        <div><code>cdp</code>: Use Cisco Discovery Protocol (CDP).</div>
                        <div><code>lldp</code>: Use Link Layer Discovery Protocol (LLDP).</div>
                        <div><code>disabled</code>: Do not use a discovery protocol.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: discovery_protocol</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>folder</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination folder, absolute path to place dvswitch in.</div>
                        <div>The folder should include the datacenter.</div>
                        <div>This parameter is case sensitive.</div>
                        <div>This parameter is optional, if <code>datacenter</code> is provided.</div>
                        <div>Examples:</div>
                        <div>folder: /datacenter1/network</div>
                        <div>folder: datacenter1/network</div>
                        <div>folder: /datacenter1/network/folder1</div>
                        <div>folder: datacenter1/network/folder1</div>
                        <div>folder: /folder1/datacenter1/network</div>
                        <div>folder: folder1/datacenter1/network</div>
                        <div>folder: /folder1/datacenter1/network/folder2</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>health_check</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">{"teaming_failover": false, "teaming_failover_interval": 0, "vlan_mtu": false, "vlan_mtu_interval": 0}</div>
                </td>
                <td>
                        <div>Dictionary which configures Health Check for the Distributed Switch.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>teaming_failover</b>
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
                        <div>Teaming and failover health check.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>teaming_failover_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">0</div>
                </td>
                <td>
                        <div>Teaming and failover health check interval (minutes).</div>
                        <div>The default value is 1 in the vSphere Client if the Teaming and failover health check is enabled.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_mtu</b>
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
                        <div>VLAN and MTU health check.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vlan_mtu_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">0</div>
                </td>
                <td>
                        <div>VLAN and MTU health check interval (minutes).</div>
                        <div>The default value is 1 in the vSphere Client if the VLAN and MTU health check is enabled.</div>
                </td>
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
                    <b>mtu</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">1500</div>
                </td>
                <td>
                        <div>The switch maximum transmission unit.</div>
                        <div>Required parameter for <code>state</code> both <code>present</code> and <code>absent</code>, before Ansible 2.6 version.</div>
                        <div>Required only if <code>state</code> is set to <code>present</code>, for Ansible 2.6 and onwards.</div>
                        <div>Accepts value between 1280 to 9000 (both inclusive).</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>multicast_filtering_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>basic</b>&nbsp;&larr;</div></li>
                                    <li>snooping</li>
                        </ul>
                </td>
                <td>
                        <div>The multicast filtering mode.</div>
                        <div><code>basic</code> mode: multicast traffic for virtual machines is forwarded according to the destination MAC address of the multicast group.</div>
                        <div><code>snooping</code> mode: the Distributed Switch provides IGMP and MLD snooping according to RFC 4541.</div>
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
                        <div>If set to <code>present</code> and the Distributed Switch does not exist, the Distributed Switch will be created.</div>
                        <div>If set to <code>absent</code> and the Distributed Switch exists, the Distributed Switch will be deleted.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switch_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The name of the distribute vSwitch to create or remove.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: switch, dvswitch</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switch_version</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>5.0.0</li>
                                    <li>5.1.0</li>
                                    <li>5.5.0</li>
                                    <li>6.0.0</li>
                                    <li>6.5.0</li>
                                    <li>6.6.0</li>
                                    <li>7.0.0</li>
                        </ul>
                </td>
                <td>
                        <div>The version of the Distributed Switch to create.</div>
                        <div>Can be 6.0.0, 5.5.0, 5.1.0, 5.0.0 with a vCenter running vSphere 6.0 and 6.5.</div>
                        <div>Can be 6.6.0, 6.5.0, 6.0.0 with a vCenter running vSphere 6.7.</div>
                        <div>Can be 7.0.0, 6.6.0, 6.5.0 with a vCenter running vSphere 7.0.</div>
                        <div>The version must match the version of the ESXi hosts you want to connect.</div>
                        <div>The version of the vCenter server is used if not specified.</div>
                        <div>Required only if <code>state</code> is set to <code>present</code>.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: version</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>uplink_prefix</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"Uplink "</div>
                </td>
                <td>
                        <div>The prefix used for the naming of the uplinks.</div>
                        <div>Only valid if the Distributed Switch will be created. Not used if the Distributed Switch is already present.</div>
                        <div>Uplinks are created as Uplink 1, Uplink 2, etc. pp. by default.</div>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>uplink_quantity</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Quantity of uplink per ESXi host added to the Distributed Switch.</div>
                        <div>The uplink quantity can be increased or decreased, but a decrease will only be successfull if the uplink isn&#x27;t used by a portgroup.</div>
                        <div>Required parameter for <code>state</code> both <code>present</code> and <code>absent</code>, before Ansible 2.6 version.</div>
                        <div>Required only if <code>state</code> is set to <code>present</code>, for Ansible 2.6 and onwards.</div>
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
   - Tested on vSphere 6.5, 6.7 and 7.0



Examples
--------

.. code-block:: yaml

    - name: Create dvSwitch
      community.vmware.vmware_dvswitch:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: '{{ datacenter }}'
        switch: dvSwitch
        version: 6.0.0
        mtu: 9000
        uplink_quantity: 2
        discovery_protocol: lldp
        discovery_operation: both
        state: present
      delegate_to: localhost

    - name: Create dvSwitch with all options
      community.vmware.vmware_dvswitch:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: '{{ datacenter }}'
        switch: dvSwitch
        version: 6.5.0
        mtu: 9000
        uplink_quantity: 2
        uplink_prefix: 'Uplink_'
        discovery_protocol: cdp
        discovery_operation: both
        multicast_filtering_mode: snooping
        health_check:
          vlan_mtu: true
          vlan_mtu_interval: 1
          teaming_failover: true
          teaming_failover_interval: 1
        state: present
      delegate_to: localhost

    - name: Delete dvSwitch
      community.vmware.vmware_dvswitch:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: '{{ datacenter }}'
        switch: dvSwitch
        state: absent
      delegate_to: localhost



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;changed&#x27;: False, &#x27;contact&#x27;: None, &#x27;contact_details&#x27;: None, &#x27;description&#x27;: None, &#x27;discovery_operation&#x27;: &#x27;both&#x27;, &#x27;discovery_protocol&#x27;: &#x27;cdp&#x27;, &#x27;dvswitch&#x27;: &#x27;test&#x27;, &#x27;health_check_teaming&#x27;: False, &#x27;health_check_teaming_interval&#x27;: 0, &#x27;health_check_vlan&#x27;: False, &#x27;health_check_vlan_interval&#x27;: 0, &#x27;mtu&#x27;: 9000, &#x27;multicast_filtering_mode&#x27;: &#x27;basic&#x27;, &#x27;result&#x27;: &#x27;DVS already configured properly&#x27;, &#x27;uplink_quantity&#x27;: 2, &#x27;uplinks&#x27;: [&#x27;Uplink_1&#x27;, &#x27;Uplink_2&#x27;], &#x27;version&#x27;: &#x27;6.6.0&#x27;}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Christian Kotte (@ckotte)
