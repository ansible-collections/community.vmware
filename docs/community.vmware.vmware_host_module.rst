.. _community.vmware.vmware_host_module:


****************************
community.vmware.vmware_host
****************************

**Add, remove, or move an ESXi host to, from, or within vCenter**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to add, reconnect, or remove an ESXi host to or from vCenter.
- This module can also be used to move an ESXi host to a cluster or folder, or vice versa, within the same datacenter.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.6
- PyVmomi
- ssl
- socket
- hashlib


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
                    <b>add_connected</b>
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
                        <div>If set to <code>True</code>, then the host should be connected as soon as it is added.</div>
                        <div>This parameter is ignored if state is set to a value other than <code>present</code>.</div>
                </td>
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
                        <div>Name of the cluster to add the host.</div>
                        <div>If <code>folder</code> is not set, then this parameter is required.</div>
                        <div>Aliases added in version 2.6.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: cluster</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datacenter_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the datacenter to add the host.</div>
                        <div>Aliases added in version 2.6.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: datacenter</div>
                </td>
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
                        <div>ESXi hostname to manage.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esxi_password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ESXi password.</div>
                        <div>Required for adding a host.</div>
                        <div>Optional for reconnect.</div>
                        <div>Unused for removing.</div>
                        <div>No longer a required parameter from version 2.5.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esxi_ssl_thumbprint</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">""</div>
                </td>
                <td>
                        <div>Specifying the hostsystem certificate&#x27;s thumbprint.</div>
                        <div>Use following command to get hostsystem certificate&#x27;s thumbprint -</div>
                        <div># openssl x509 -in /etc/vmware/ssl/rui.crt -fingerprint -sha1 -noout</div>
                        <div>Only used if <code>fetch_thumbprint</code> isn&#x27;t set to <code>true</code>.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: ssl_thumbprint</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esxi_username</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>ESXi username.</div>
                        <div>Required for adding a host.</div>
                        <div>Optional for reconnect. If both <code>esxi_username</code> and <code>esxi_password</code> are used</div>
                        <div>Unused for removing.</div>
                        <div>No longer a required parameter from version 2.5.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fetch_ssl_thumbprint</b>
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
                        <div>Fetch the thumbprint of the host&#x27;s SSL certificate.</div>
                        <div>This basically disables the host certificate verification (check if it was signed by a recognized CA).</div>
                        <div>Disable this option if you want to allow only hosts with valid certificates to be added to vCenter.</div>
                        <div>If this option is set to <code>false</code> and the certificate can&#x27;t be verified, an add or reconnect will fail.</div>
                        <div>Unused when <code>esxi_ssl_thumbprint</code> is set.</div>
                        <div>Optional for reconnect, but only used if <code>esxi_username</code> and <code>esxi_password</code> are used.</div>
                        <div>Unused for removing.</div>
                </td>
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
                        <div>Name of the folder under which host to add.</div>
                        <div>If <code>cluster_name</code> is not set, then this parameter is required.</div>
                        <div>For example, if there is a datacenter &#x27;dc1&#x27; under folder called &#x27;Site1&#x27; then, this value will be &#x27;/Site1/dc1/host&#x27;.</div>
                        <div>Here &#x27;host&#x27; is an invisible folder under VMware Web Client.</div>
                        <div>Another example, if there is a nested folder structure like &#x27;/myhosts/india/pune&#x27; under datacenter &#x27;dc2&#x27;, then <code>folder</code> value will be &#x27;/dc2/host/myhosts/india/pune&#x27;.</div>
                        <div>Other Examples: &#x27;/Site2/dc2/Asia-Cluster/host&#x27; or &#x27;/dc3/Asia-Cluster/host&#x27;</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: folder_name</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>force_connection</b>
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
                        <div>Force the connection if the host is already being managed by another vCenter server.</div>
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
                    <b>reconnect_disconnected</b>
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
                        <div>Reconnect disconnected hosts.</div>
                        <div>This is only used if <code>state</code> is set to <code>present</code> and if the host already exists.</div>
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
                                    <li>add_or_reconnect</li>
                                    <li>reconnect</li>
                                    <li>disconnected</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>present</code>, add the host if host is absent.</div>
                        <div>If set to <code>present</code>, update the location of the host if host already exists.</div>
                        <div>If set to <code>absent</code>, remove the host if host is present.</div>
                        <div>If set to <code>absent</code>, do nothing if host already does not exists.</div>
                        <div>If set to <code>add_or_reconnect</code>, add the host if it&#x27;s absent else reconnect it and update the location.</div>
                        <div>If set to <code>reconnect</code>, then reconnect the host if it&#x27;s present and update the location.</div>
                        <div>If set to <code>disconnected</code>, disconnect the host if the host already exists.</div>
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
   - Tested on vSphere 5.5, 6.0, 6.5 and 6.7
   - All modules requires API write access and hence is not supported on a free ESXi license.



Examples
--------

.. code-block:: yaml

    - name: Add ESXi Host to vCenter
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: present
      delegate_to: localhost

    - name: Add ESXi Host to vCenter under a specific folder
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        folder: '/Site2/Asia-Cluster/host'
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: present
        add_connected: True
      delegate_to: localhost

    - name: Reconnect ESXi Host (with username/password set)
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        state: reconnect
      delegate_to: localhost

    - name: Reconnect ESXi Host (with default username/password)
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        state: reconnect
      delegate_to: localhost

    - name: Add ESXi Host with SSL Thumbprint to vCenter
      community.vmware.vmware_host:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: datacenter_name
        cluster: cluster_name
        esxi_hostname: '{{ esxi_hostname }}'
        esxi_username: '{{ esxi_username }}'
        esxi_password: '{{ esxi_password }}'
        esxi_ssl_thumbprint: "3C:A5:60:6F:7A:B7:C4:6C:48:28:3D:2F:A5:EC:A3:58:13:88:F6:DD"
        state: present
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
                <td>on successful addition</td>
                <td>
                            <div>metadata about the new host system added</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Host already connected to vCenter &#x27;vcenter01&#x27; in cluster &#x27;cluster01&#x27;</div>
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
- Maxime de Roucy (@tchernomax)
- Christian Kotte (@ckotte)
