.. _community.vmware.vmware_vcenter_settings_info_module:


*********************************************
community.vmware.vmware_vcenter_settings_info
*********************************************

**Gather info vCenter settings**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to gather information about vCenter settings.



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
                        <div>Example:</div>
                        <div>properties: [</div>
                        <div>&quot;config.workflow.port&quot;</div>
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
                        <div>The &#x27;summary&#x27; output schema is the legacy output from the module.</div>
                        <div>The &#x27;vsphere&#x27; output schema is the vSphere API class definition which requires pyvmomi&gt;6.7.1.</div>
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
   - All modules requires API write access and hence is not supported on a free ESXi license.



Examples
--------

.. code-block:: yaml

    - name: "Gather info about vCenter settings"
      community.vmware.vmware_vcenter_settings_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
      register: vcenter_settings_info

    - name: "Gather some info from vCenter using the vSphere API output schema"
      community.vmware.vmware_vcenter_settings_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        schema: vsphere
        properties:
          - config.workflow.port
      register: vcenter_settings_info_vsphere_api



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
                    <b>vcenter_config_info</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>success</td>
                <td>
                            <div>dict of vCenter settings</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{
        &quot;db_event_cleanup_previous&quot;: true,
        &quot;db_event_retention_previous&quot;: 30,
        &quot;db_max_connections_previous&quot;: 50,
        &quot;db_task_cleanup_previous&quot;: true,
        &quot;db_task_retention_previous&quot;: 30,
        &quot;directory_query_limit_previous&quot;: true,
        &quot;directory_query_limit_size_previous&quot;: 5000,
        &quot;directory_timeout_previous&quot;: 60,
        &quot;directory_validation_period_previous&quot;: 1440,
        &quot;directory_validation_previous&quot;: true,
        &quot;logging_options_previous&quot;: &quot;info&quot;,
        &quot;mail_sender_previous&quot;: &quot;&quot;,
        &quot;mail_server_previous&quot;: &quot;&quot;,
        &quot;runtime_managed_address_previous&quot;: &quot;&quot;,
        &quot;runtime_server_name_previous&quot;: &quot;vcenter.local&quot;,
        &quot;runtime_unique_id_previous&quot;: 48,
        &quot;snmp_1_community_previous&quot;: &quot;public&quot;,
        &quot;snmp_1_enabled_previous&quot;: true,
        &quot;snmp_1_url_previous&quot;: &quot;localhost&quot;,
        &quot;snmp_2_community_previous&quot;: &quot;&quot;,
        &quot;snmp_2_enabled_previous&quot;: false,
        &quot;snmp_2_url_previous&quot;: &quot;&quot;,
        &quot;snmp_3_community_previous&quot;: &quot;&quot;,
        &quot;snmp_3_enabled_previous&quot;: false,
        &quot;snmp_3_url_previous&quot;: &quot;&quot;,
        &quot;snmp_4_community_previous&quot;: &quot;&quot;,
        &quot;snmp_4_enabled_previous&quot;: false,
        &quot;snmp_4_url_previous&quot;: &quot;&quot;,
        &quot;snmp_receiver_1_port_previous&quot;: 162,
        &quot;snmp_receiver_2_port_previous&quot;: 162,
        &quot;snmp_receiver_3_port_previous&quot;: 162,
        &quot;snmp_receiver_4_port_previous&quot;: 162,
        &quot;timeout_long_operations_previous&quot;: 120,
        &quot;timeout_normal_operations_previous&quot;: 30
    }</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- sky-joker (@sky-joker)
