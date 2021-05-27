.. _community.vmware.vmware_host_vmhba_facts_module:


****************************************
community.vmware.vmware_host_vmhba_facts
****************************************

**Gathers facts about vmhbas available on the given ESXi host**



.. contents::
   :local:
   :depth: 1

DEPRECATED
----------
:Removed in collection release after 2021-12-01
:Why: Deprecated in favour of :ref:`community.vmware.vmware_host_vmhba_info <community.vmware.vmware_host_vmhba_info_module>` module.
:Alternative: Use :ref:`community.vmware.vmware_host_vmhba_info <community.vmware.vmware_host_vmhba_info_module>` instead.



Synopsis
--------
- This module can be used to gather facts about vmhbas available on the given ESXi host.
- If ``cluster_name`` is provided, then vmhba facts about all hosts from given cluster will be returned.
- If ``esxi_hostname`` is provided, then vmhba facts about given host system will be returned.



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
                    <b>cluster_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the cluster from which all host systems will be used.</div>
                        <div>Vmhba facts about each ESXi server will be returned for the given cluster.</div>
                        <div>This parameter is required if <code>esxi_hostname</code> is not specified.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>esxi_hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the host system to work with.</div>
                        <div>Vmhba facts about this ESXi server will be returned.</div>
                        <div>This parameter is required if <code>cluster_name</code> is not specified.</div>
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
   - Tested on vSphere 6.5



Examples
--------

.. code-block:: yaml

    - name: Gather facts about vmhbas of all ESXi Host in the given Cluster
      community.vmware.vmware_host_vmhba_facts:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: '{{ cluster_name }}'
      delegate_to: localhost
      register: cluster_host_vmhbas

    - name: Gather facts about vmhbas of an ESXi Host
      community.vmware.vmware_host_vmhba_facts:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
      delegate_to: localhost
      register: host_vmhbas



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
                    <b>hosts_vmhbas_facts</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>hosts_vmhbas_facts</td>
                <td>
                            <div>dict with hostname as key and dict with vmhbas facts as value.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;10.76.33.204&#x27;: {&#x27;vmhba_details&#x27;: [{&#x27;adapter&#x27;: &#x27;HPE Smart Array P440ar&#x27;, &#x27;bus&#x27;: 3, &#x27;device&#x27;: &#x27;vmhba0&#x27;, &#x27;driver&#x27;: &#x27;nhpsa&#x27;, &#x27;location&#x27;: &#x27;0000:03:00.0&#x27;, &#x27;model&#x27;: &#x27;Smart Array P440ar&#x27;, &#x27;node_wwn&#x27;: &#x27;50:01:43:80:37:18:9e:a0&#x27;, &#x27;status&#x27;: &#x27;unknown&#x27;, &#x27;type&#x27;: &#x27;SAS&#x27;}, {&#x27;adapter&#x27;: &#x27;QLogic Corp ISP2532-based 8Gb Fibre Channel to PCI Express HBA&#x27;, &#x27;bus&#x27;: 5, &#x27;device&#x27;: &#x27;vmhba1&#x27;, &#x27;driver&#x27;: &#x27;qlnativefc&#x27;, &#x27;location&#x27;: &#x27;0000:05:00.0&#x27;, &#x27;model&#x27;: &#x27;ISP2532-based 8Gb Fibre Channel to PCI Express HBA&#x27;, &#x27;node_wwn&#x27;: &#x27;57:64:96:32:15:90:23:95:82&#x27;, &#x27;port_type&#x27;: &#x27;unknown&#x27;, &#x27;port_wwn&#x27;: &#x27;57:64:96:32:15:90:23:95:82&#x27;, &#x27;speed&#x27;: 8, &#x27;status&#x27;: &#x27;online&#x27;, &#x27;type&#x27;: &#x27;Fibre Channel&#x27;}, {&#x27;adapter&#x27;: &#x27;QLogic Corp ISP2532-based 8Gb Fibre Channel to PCI Express HBA&#x27;, &#x27;bus&#x27;: 8, &#x27;device&#x27;: &#x27;vmhba2&#x27;, &#x27;driver&#x27;: &#x27;qlnativefc&#x27;, &#x27;location&#x27;: &#x27;0000:08:00.0&#x27;, &#x27;model&#x27;: &#x27;ISP2532-based 8Gb Fibre Channel to PCI Express HBA&#x27;, &#x27;node_wwn&#x27;: &#x27;57:64:96:32:15:90:23:95:21&#x27;, &#x27;port_type&#x27;: &#x27;unknown&#x27;, &#x27;port_wwn&#x27;: &#x27;57:64:96:32:15:90:23:95:21&#x27;, &#x27;speed&#x27;: 8, &#x27;status&#x27;: &#x27;online&#x27;, &#x27;type&#x27;: &#x27;Fibre Channel&#x27;}]}}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


- This module will be removed in version . *[deprecated]*
- For more information see `DEPRECATED`_.


Authors
~~~~~~~

- Christian Kotte (@ckotte)
