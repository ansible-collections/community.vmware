.. _community.vmware.vmware_host_iscsi_info_module:


***************************************
community.vmware.vmware_host_iscsi_info
***************************************

**Gather iSCSI configuration information of ESXi host**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to gather information about the iSCSI configuration of the ESXi host.



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
                    <b>esxi_hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The ESXi hostname on which to gather iSCSI settings.</div>
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

    - name: Gather iSCSI configuration information of ESXi host
      community.vmware.vmware_host_iscsi_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
      register: iscsi_info



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
                    <b>detected_iscsi_drives</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>list of detected iSCSI drive</div>
                            <div>added from version 1.9.0</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[
        {
            &quot;address&quot;: [
                &quot;192.168.0.57:3260&quot;
            ],
            &quot;canonical_name&quot;: &quot;naa.60014055f198fb3d0cb4bd7ae1f802e1&quot;,
            &quot;iscsi_name&quot;: &quot;iqn.2021-03.local.iscsi-target:iscsi-storage.target0&quot;
        }
    ]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>iscsi_properties</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>dictionary of current iSCSI information</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{
      &quot;iscsi_alias&quot;: &quot;&quot;,
      &quot;iscsi_authentication_properties&quot;: {
        &quot;_vimtype&quot;: &quot;vim.host.InternetScsiHba.AuthenticationProperties&quot;,
        &quot;chapAuthEnabled&quot;: false,
        &quot;chapAuthenticationType&quot;: &quot;chapProhibited&quot;,
        &quot;chapInherited&quot;: null,
        &quot;chapName&quot;: &quot;&quot;,
        &quot;chapSecret&quot;: &quot;XXXXXXXXX&quot;,
        &quot;mutualChapAuthenticationType&quot;: &quot;chapProhibited&quot;,
        &quot;mutualChapInherited&quot;: null,
        &quot;mutualChapName&quot;: &quot;&quot;,
        &quot;mutualChapSecret&quot;: &quot;XXXXXXXXX&quot;
      },
      &quot;iscsi_enabled&quot;: true,
      &quot;iscsi_name&quot;: &quot;iqn.1998-01.com.vmware:esxi-033f58ee&quot;,
      &quot;iscsi_send_targets&quot;: [
        {
          &quot;address&quot;: &quot;192.168.0.1&quot;,
          &quot;authenticationProperties&quot;: {
            &quot;_vimtype&quot;: &quot;vim.host.InternetScsiHba.AuthenticationProperties&quot;,
            &quot;chapAuthEnabled&quot;: false,
            &quot;chapAuthenticationType&quot;: &quot;chapProhibited&quot;,
            &quot;chapInherited&quot;: true,
            &quot;chapName&quot;: &quot;&quot;,
            &quot;chapSecret&quot;: &quot;XXXXXXXXX&quot;,
            &quot;mutualChapAuthenticationType&quot;: &quot;chapProhibited&quot;,
            &quot;mutualChapInherited&quot;: true,
            &quot;mutualChapName&quot;: &quot;&quot;,
            &quot;mutualChapSecret&quot;: &quot;XXXXXXXXX&quot;
          },
          &quot;port&quot;: 3260
        }
      ],
      &quot;iscsi_static_targets&quot;: [
        {
          &quot;address&quot;: &quot;192.168.0.1&quot;,
          &quot;authenticationProperties&quot;: {
            &quot;_vimtype&quot;: &quot;vim.host.InternetScsiHba.AuthenticationProperties&quot;,
            &quot;chapAuthEnabled&quot;: false,
            &quot;chapAuthenticationType&quot;: &quot;chapProhibited&quot;,
            &quot;chapInherited&quot;: true,
            &quot;chapName&quot;: &quot;&quot;,
            &quot;chapSecret&quot;: &quot;XXXXXXXXX&quot;,
            &quot;mutualChapAuthenticationType&quot;: &quot;chapProhibited&quot;,
            &quot;mutualChapInherited&quot;: true,
            &quot;mutualChapName&quot;: &quot;&quot;,
            &quot;mutualChapSecret&quot;: &quot;XXXXXXXXX&quot;
          },
          &quot;iscsi_name&quot;: &quot;iqn.2004-04.com.qnap:tvs-673:iscsi.vm3.2c580e&quot;,
          &quot;port&quot;: 3260
        }
      ],
      &quot;port_bind&quot;: [],
      &quot;vmhba_name&quot;: &quot;vmhba65&quot;
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
