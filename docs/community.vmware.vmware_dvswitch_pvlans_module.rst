.. _community.vmware.vmware_dvswitch_pvlans_module:


***************************************
community.vmware.vmware_dvswitch_pvlans
***************************************

**Manage Private VLAN configuration of a Distributed Switch**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to configure Private VLANs (PVLANs) on a Distributed Switch.



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
                    <b>primary_pvlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">[]</div>
                </td>
                <td>
                        <div>A list of VLAN IDs that should be configured as Primary PVLANs.</div>
                        <div>If <code>primary_pvlans</code> isn&#x27;t specified, all PVLANs will be deleted if present.</div>
                        <div>Each member of the list requires primary_pvlan_id (int) set.</div>
                        <div>The secondary promiscuous PVLAN will be created automatically.</div>
                        <div>If <code>secondary_pvlans</code> isn&#x27;t specified, the primary PVLANs and each secondary promiscuous PVLAN will be created.</div>
                        <div>Please see examples for more information.</div>
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
                    <b>secondary_pvlans</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">[]</div>
                </td>
                <td>
                        <div>A list of VLAN IDs that should be configured as Secondary PVLANs.</div>
                        <div><code>primary_pvlans</code> need to be specified to create any Secondary PVLAN.</div>
                        <div>If <code>primary_pvlans</code> isn&#x27;t specified, all PVLANs will be deleted if present.</div>
                        <div>Each member of the list requires primary_pvlan_id (int), secondary_pvlan_id (int), and pvlan_type (str) to be set.</div>
                        <div>The type of the secondary PVLAN can be isolated or community. The secondary promiscuous PVLAN will be created automatically.</div>
                        <div>Please see examples for more information.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
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
                        <div>The name of the Distributed Switch.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: dvswitch</div>
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
    </table>
    <br/>


Notes
-----

.. note::
   - Tested on vSphere 6.5 and 6.7



Examples
--------

.. code-block:: yaml

    - name: Create PVLANs on a Distributed Switch
      community.vmware.vmware_dvswitch_pvlans:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        primary_pvlans:
          - primary_pvlan_id: 1
          - primary_pvlan_id: 4
        secondary_pvlans:
          - primary_pvlan_id: 1
            secondary_pvlan_id: 2
            pvlan_type: isolated
          - primary_pvlan_id: 1
            secondary_pvlan_id: 3
            pvlan_type: community
          - primary_pvlan_id: 4
            secondary_pvlan_id: 5
            pvlan_type: community
      delegate_to: localhost

    - name: Create primary PVLAN and secondary promiscuous PVLAN on a Distributed Switch
      community.vmware.vmware_dvswitch_pvlans:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        primary_pvlans:
          - primary_pvlan_id: 1
      delegate_to: localhost

    - name: Remove all PVLANs from a Distributed Switch
      community.vmware.vmware_dvswitch_pvlans:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        primary_pvlans: []
        secondary_pvlans: []
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;changed&#x27;: True, &#x27;dvswitch&#x27;: &#x27;dvSwitch&#x27;, &#x27;private_vlans&#x27;: [{&#x27;primary_pvlan_id&#x27;: 1, &#x27;pvlan_type&#x27;: &#x27;promiscuous&#x27;, &#x27;secondary_pvlan_id&#x27;: 1}, {&#x27;primary_pvlan_id&#x27;: 1, &#x27;pvlan_type&#x27;: &#x27;isolated&#x27;, &#x27;secondary_pvlan_id&#x27;: 2}, {&#x27;primary_pvlan_id&#x27;: 1, &#x27;pvlan_type&#x27;: &#x27;community&#x27;, &#x27;secondary_pvlan_id&#x27;: 3}], &#x27;private_vlans_previous&#x27;: [], &#x27;result&#x27;: &#x27;All private VLANs added&#x27;}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Christian Kotte (@ckotte)
