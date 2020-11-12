.. _community.vmware.vmware_dvswitch_info_module:


*************************************
community.vmware.vmware_dvswitch_info
*************************************

**Gathers info dvswitch configurations**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to gather information about dvswitch configurations.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
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
                    <b>folder</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify a folder location of dvswitch to gather information from.</div>
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
                    <b>properties</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify the properties to retrieve.</div>
                        <div>If not specified, all properties are retrieved (deeply).</div>
                        <div>Results are returned in a structure identical to the vsphere API.</div>
                        <div>Example:</div>
                        <div>properties: [</div>
                        <div>&quot;summary.name&quot;,</div>
                        <div>&quot;summary.numPorts&quot;,</div>
                        <div>&quot;config.maxMtu&quot;,</div>
                        <div>&quot;overallStatus&quot;</div>
                        <div>]</div>
                        <div>Only valid when <code>schema</code> is <code>vsphere</code>.</div>
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
                    <b>schema</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>summary</b>&nbsp;&larr;</div></li>
                                    <li>vsphere</li>
                        </ul>
                </td>
                <td>
                        <div>Specify the output schema desired.</div>
                        <div>The &#x27;summary&#x27; output schema is the legacy output from the module</div>
                        <div>The &#x27;vsphere&#x27; output schema is the vSphere API class definition which requires pyvmomi&gt;6.7.1</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>switch_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a dvswitch to look for.</div>
                        <div>If <code>switch_name</code> not specified gather all dvswitch information.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: switch, dvswitch</div>
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
                    <b>distributed_virtual_switches</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>list of dictionary of dvswitch and their information</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;configure&#x27;: {&#x27;folder&#x27;: &#x27;network&#x27;, &#x27;hosts&#x27;: [&#x27;esxi-test-02.local&#x27;, &#x27;esxi-test-01.local&#x27;], &#x27;settings&#x27;: {&#x27;healthCheck&#x27;: {&#x27;TeamingHealthCheckConfig&#x27;: False, &#x27;VlanMtuHealthCheckConfig&#x27;: False}, &#x27;netflow&#x27;: {&#x27;activeFlowTimeout&#x27;: 60, &#x27;collectorIpAddress&#x27;: &#x27;&#x27;, &#x27;collectorPort&#x27;: 0, &#x27;idleFlowTimeout&#x27;: 15, &#x27;internalFlowsOnly&#x27;: False, &#x27;observationDomainId&#x27;: 0, &#x27;samplingRate&#x27;: 0, &#x27;switchIpAddress&#x27;: None}, &#x27;properties&#x27;: {&#x27;administratorContact&#x27;: {&#x27;contact&#x27;: None, &#x27;name&#x27;: None}, &#x27;advanced&#x27;: {&#x27;maxMtu&#x27;: 1500, &#x27;multicastFilteringMode&#x27;: &#x27;legacyFiltering&#x27;}, &#x27;discoveryProtocol&#x27;: {&#x27;operation&#x27;: &#x27;listen&#x27;, &#x27;protocol&#x27;: &#x27;cdp&#x27;}, &#x27;general&#x27;: {&#x27;ioControl&#x27;: True, &#x27;name&#x27;: &#x27;DVSwitch01&#x27;, &#x27;numPorts&#x27;: 10, &#x27;numUplinks&#x27;: 1, &#x27;vendor&#x27;: &#x27;VMware, Inc.&#x27;, &#x27;version&#x27;: &#x27;6.6.0&#x27;}}, &#x27;privateVlan&#x27;: []}}, &#x27;uuid&#x27;: &#x27;50 30 99 9c a7 60 8a 4f-05 9f e7 b5 da df 8f 17&#x27;}]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- sky-joker (@sky-joker)
