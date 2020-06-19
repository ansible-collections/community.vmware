:orphan:

.. _community.vmware.vmware_vcenter_statistics_module:


******************************************
community.vmware.vmware_vcenter_statistics
******************************************

**Configures statistics on a vCenter server**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to configure the vCenter server statistics.
- The remaining settings can be configured with the module ``vmware_vcenter_settings``.



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
                    <b>interval_past_day</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Settings for vCenter server past day statistic collection.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>enabled</code> (bool): Past day statistics collection enabled. (default: True)</div>
                                            <div>- <code>interval_minutes</code> (int): Interval duration (minutes). (choices: [1, 2, 3, 4, 5]) (default: 5)</div>
                                            <div>- <code>save_for_days</code> (int): Save for (days). (choices: [1, 2, 3, 4, 5]) (default: 1)</div>
                                            <div>- <code>level</code> (int): Statistics level. (choices: [1, 2, 3, 4]) (default: 1)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval_past_month</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Settings for vCenter server past month statistic collection.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>enabled</code> (bool): Past month statistics collection enabled. (default: True)</div>
                                            <div>- <code>interval_hours</code> (int): Interval duration (hours). (choices: [2]) (default: 2)</div>
                                            <div>- <code>save_for_months</code> (int): Save for (months). (choices: [1]) (default: 1)</div>
                                            <div>- <code>level</code> (int): Statistics level. (choices: [1, 2, 3, 4]) (default: 1)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval_past_week</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Settings for vCenter server past week statistic collection.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>enabled</code> (bool): Past week statistics collection enabled. (default: True)</div>
                                            <div>- <code>interval_minutes</code> (int): Interval duration (minutes). (choices: [30]) (default: 30)</div>
                                            <div>- <code>save_for_weeks</code> (int): Save for (weeks). (choices: [1]) (default: 1)</div>
                                            <div>- <code>level</code> (int): Statistics level. (choices: [1, 2, 3, 4]) (default: 1)</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>interval_past_year</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Settings for vCenter server past month statistic collection.</div>
                                            <div>Valid attributes are:</div>
                                            <div>- <code>enabled</code> (bool): Past month statistics collection enabled. (default: True)</div>
                                            <div>- <code>interval_days</code> (int): Interval duration (days). (choices: [1]) (default: 1)</div>
                                            <div>- <code>save_for_years</code> (int): Save for (years). (choices: [1, 2, 3, 4, 5]) (default: 1)</div>
                                            <div>- <code>level</code> (int): Statistics level. (choices: [1, 2, 3, 4]) (default: 1)</div>
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

    
    - name: Configure vCenter statistics
      community.vmware.vmware_vcenter_statistics:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        interval_past_day:
          enabled: true
          interval_minutes: 5
          save_for_days: 1
          level: 1
        interval_past_week:
          enabled: true
          level: 1
        interval_past_month:
          enabled: true
          level: 1
        interval_past_year:
          enabled: true
          save_for_years: 1
          level: 1
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
                                                                        <div>metadata about vCenter statistics settings</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;changed&#x27;: False, &#x27;msg&#x27;: &#x27;vCenter statistics already configured properly&#x27;, &#x27;past_day_enabled&#x27;: True, &#x27;past_day_interval&#x27;: 5, &#x27;past_day_level&#x27;: 1, &#x27;past_day_save_for&#x27;: 1, &#x27;past_month_enabled&#x27;: True, &#x27;past_month_interval&#x27;: 2, &#x27;past_month_level&#x27;: 1, &#x27;past_month_save_for&#x27;: 1, &#x27;past_week_enabled&#x27;: True, &#x27;past_week_interval&#x27;: 30, &#x27;past_week_level&#x27;: 1, &#x27;past_week_save_for&#x27;: 1, &#x27;past_year_enabled&#x27;: True, &#x27;past_year_interval&#x27;: 1, &#x27;past_year_level&#x27;: 1, &#x27;past_year_save_for&#x27;: 1}</div>
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
