:orphan:

.. _community.vmware.vmware_vcenter_settings_module:


****************************************
community.vmware.vmware_vcenter_settings
****************************************

**Configures general settings on a vCenter server**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to configure the vCenter server general settings (except the statistics).
- The statistics can be configured with the module ``vmware_vcenter_statistics``.



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
                    <b>database</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"event_cleanup": true, "event_retention": 30, "max_connections": 50, "task_cleanup": true, "task_retention": 30}</div>
                                    </td>
                                                                <td>
                                            <div>The database settings for vCenter server.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>max_connections</code> (int): Maximum connections. (default: 50)</div>
                                            <div>- <code>task_cleanup</code> (bool): Task cleanup. (default: true)</div>
                                            <div>- <code>task_retention</code> (int): Task retention (days). (default: 30)</div>
                                            <div>- <code>event_cleanup</code> (bool): Event cleanup. (default: true)</div>
                                            <div>- <code>event_retention</code> (int): Event retention (days). (default: 30)</div>
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
                    <b>logging_options</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                            <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                                                                                                                                                <li>none</li>
                                                                                                                                                                                                <li>error</li>
                                                                                                                                                                                                <li>warning</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>info</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>verbose</li>
                                                                                                                                                                                                <li>trivia</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                            <div>The level of detail that vCenter server usesfor log files.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>mail</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"sender": "", "server": ""}</div>
                                    </td>
                                                                <td>
                                            <div>The settings vCenter server uses to send email alerts.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>server</code> (str): Mail server</div>
                                            <div>- <code>sender</code> (str): Mail sender address</div>
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
                    <b>runtime_settings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>The unique runtime settings for vCenter server.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>unique_id</code> (int): vCenter server unique ID.</div>
                                            <div>- <code>managed_address</code> (str): vCenter server managed address.</div>
                                            <div>- <code>vcenter_server_name</code> (str): vCenter server name. (default: FQDN)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>snmp_receivers</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"snmp_receiver_1_community": "public", "snmp_receiver_1_enabled": true, "snmp_receiver_1_port": 162, "snmp_receiver_1_url": "localhost", "snmp_receiver_2_community": "", "snmp_receiver_2_enabled": false, "snmp_receiver_2_port": 162, "snmp_receiver_2_url": "", "snmp_receiver_3_community": "", "snmp_receiver_3_enabled": false, "snmp_receiver_3_port": 162, "snmp_receiver_3_url": "", "snmp_receiver_4_community": "", "snmp_receiver_4_enabled": false, "snmp_receiver_4_port": 162, "snmp_receiver_4_url": ""}</div>
                                    </td>
                                                                <td>
                                            <div>SNMP trap destinations for vCenter server alerts.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>snmp_receiver_1_url</code> (str): Primary Receiver ULR. (default: &quot;localhost&quot;)</div>
                                            <div>- <code>snmp_receiver_1_enabled</code> (bool): Enable receiver. (default: True)</div>
                                            <div>- <code>snmp_receiver_1_port</code> (int): Receiver port. (default: 162)</div>
                                            <div>- <code>snmp_receiver_1_community</code> (str): Community string. (default: &quot;public&quot;)</div>
                                            <div>- <code>snmp_receiver_2_url</code> (str): Receiver 2 ULR. (default: &quot;&quot;)</div>
                                            <div>- <code>snmp_receiver_2_enabled</code> (bool): Enable receiver. (default: False)</div>
                                            <div>- <code>snmp_receiver_2_port</code> (int): Receiver port. (default: 162)</div>
                                            <div>- <code>snmp_receiver_2_community</code> (str): Community string. (default: &quot;&quot;)</div>
                                            <div>- <code>snmp_receiver_3_url</code> (str): Receiver 3 ULR. (default: &quot;&quot;)</div>
                                            <div>- <code>snmp_receiver_3_enabled</code> (bool): Enable receiver. (default: False)</div>
                                            <div>- <code>snmp_receiver_3_port</code> (int): Receiver port. (default: 162)</div>
                                            <div>- <code>snmp_receiver_3_community</code> (str): Community string. (default: &quot;&quot;)</div>
                                            <div>- <code>snmp_receiver_4_url</code> (str): Receiver 4 ULR. (default: &quot;&quot;)</div>
                                            <div>- <code>snmp_receiver_4_enabled</code> (bool): Enable receiver. (default: False)</div>
                                            <div>- <code>snmp_receiver_4_port</code> (int): Receiver port. (default: 162)</div>
                                            <div>- <code>snmp_receiver_4_community</code> (str): Community string. (default: &quot;&quot;)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout_settings</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"long_operations": 120, "normal_operations": 30}</div>
                                    </td>
                                                                <td>
                                            <div>The vCenter server connection timeout for normal and long operations.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>normal_operations</code> (int) (default: 30)</div>
                                            <div>- <code>long_operations</code> (int) (default: 120)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>user_directory</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{"query_limit": true, "query_limit_size": 5000, "timeout": 60, "validation": true, "validation_period": 1440}</div>
                                    </td>
                                                                <td>
                                            <div>The user directory settings for the vCenter server installation.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>timeout</code> (int): User directory timeout. (default: 60)</div>
                                            <div>- <code>query_limit</code> (bool): Query limit. (default: true)</div>
                                            <div>- <code>query_limit_size</code> (int): Query limit size. (default: 5000)</div>
                                            <div>- <code>validation</code> (bool): Mail Validation. (default: true)</div>
                                            <div>- <code>validation_period</code> (int): Validation period. (default: 1440)</div>
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
                        </table>
    <br/>


Notes
-----

.. note::
   - Tested with vCenter Server Appliance (vCSA) 6.5 and 6.7



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Configure vCenter general settings
      community.vmware.vmware_vcenter_settings:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        database:
          max_connections: 50
          task_cleanup: true
          task_retention: 30
          event_cleanup: true
          event_retention: 30
        runtime_settings:
          unique_id: 1
          managed_address: "{{ lookup('dig', inventory_hostname) }}"
          vcenter_server_name: "{{ inventory_hostname }}"
        user_directory:
          timeout: 60
          query_limit: true
          query_limit_size: 5000
          validation: true
          validation_period: 1440
        mail:
          server: mail.example.com
          sender: vcenter@{{ inventory_hostname }}
        snmp_receivers:
          snmp_receiver_1_url: localhost
          snmp_receiver_1_enabled: true
          snmp_receiver_1_port: 162
          snmp_receiver_1_community: public
        timeout_settings:
          normal_operations: 30
          long_operations: 120
        logging_options: info
        validate_certs: no
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
                    <b>results</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                                                        <div>metadata about vCenter settings</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;changed&#x27;: False, &#x27;db_event_cleanup&#x27;: True, &#x27;db_event_retention&#x27;: 30, &#x27;db_max_connections&#x27;: 50, &#x27;db_task_cleanup&#x27;: True, &#x27;db_task_retention&#x27;: 30, &#x27;directory_query_limit&#x27;: True, &#x27;directory_query_limit_size&#x27;: 5000, &#x27;directory_timeout&#x27;: 60, &#x27;directory_validation&#x27;: True, &#x27;directory_validation_period&#x27;: 1440, &#x27;logging_options&#x27;: &#x27;info&#x27;, &#x27;mail_sender&#x27;: &#x27;vcenter@vcenter01.example.com&#x27;, &#x27;mail_server&#x27;: &#x27;mail.example.com&#x27;, &#x27;msg&#x27;: &#x27;vCenter settings already configured properly&#x27;, &#x27;runtime_managed_address&#x27;: &#x27;192.168.1.10&#x27;, &#x27;runtime_server_name&#x27;: &#x27;vcenter01.example.com&#x27;, &#x27;runtime_unique_id&#x27;: 1, &#x27;timeout_long_operations&#x27;: 120, &#x27;timeout_normal_operations&#x27;: 30}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Christian Kotte (@ckotte)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
