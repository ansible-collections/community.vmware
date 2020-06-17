:orphan:

.. _community.vmware.vmware_cluster_info_module:


************************************
community.vmware.vmware_cluster_info
************************************

**Gather info about clusters available in given vCenter**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to gather information about clusters in VMWare infrastructure.
- All values and VMware object names are case sensitive.
- This module was called ``vmware_cluster_facts`` before Ansible 2.9. The usage did not change.



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
                                            <div>Name of the cluster.</div>
                                            <div>If set, information of this cluster will be returned.</div>
                                            <div>This parameter is required, if <code>datacenter</code> is not supplied.</div>
                                                        </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datacenter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                                                                    </div>
                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                            <div>Datacenter to search for cluster/s.</div>
                                            <div>This parameter is required, if <code>cluster_name</code> is not supplied.</div>
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
                    <b>show_tag</b>
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
                                            <div>Tags related to cluster are shown if set to <code>True</code>.</div>
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
   - Tested on vSphere 6.5, 6.7



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Gather cluster info from given datacenter
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: ha-datacenter
        validate_certs: no
      delegate_to: localhost
      register: cluster_info

    - name: Gather info from datacenter about specific cluster
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
      delegate_to: localhost
      register: cluster_info

    - name: Gather info from datacenter about specific cluster with tags
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
        show_tag: True
      delegate_to: localhost
      register: cluster_info




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
                    <b>clusters</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                                          </div>
                                    </td>
                <td>always</td>
                <td>
                                                                        <div>metadata about the available clusters</div>
                                                                <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;DC0_C0&#x27;: {&#x27;drs_default_vm_behavior&#x27;: None, &#x27;drs_enable_vm_behavior_overrides&#x27;: None, &#x27;drs_vmotion_rate&#x27;: None, &#x27;enable_ha&#x27;: None, &#x27;enabled_drs&#x27;: True, &#x27;enabled_vsan&#x27;: False, &#x27;ha_admission_control_enabled&#x27;: None, &#x27;ha_failover_level&#x27;: None, &#x27;ha_host_monitoring&#x27;: None, &#x27;ha_restart_priority&#x27;: None, &#x27;ha_vm_failure_interval&#x27;: None, &#x27;ha_vm_max_failure_window&#x27;: None, &#x27;ha_vm_max_failures&#x27;: None, &#x27;ha_vm_min_up_time&#x27;: None, &#x27;ha_vm_monitoring&#x27;: None, &#x27;ha_vm_tools_monitoring&#x27;: None, &#x27;vsan_auto_claim_storage&#x27;: False, &#x27;hosts&#x27;: [{&#x27;name&#x27;: &#x27;esxi01.vsphere.local&#x27;, &#x27;folder&#x27;: &#x27;/DC0/host/DC0_C0&#x27;}, {&#x27;name&#x27;: &#x27;esxi02.vsphere.local&#x27;, &#x27;folder&#x27;: &#x27;/DC0/host/DC0_C0&#x27;}, {&#x27;name&#x27;: &#x27;esxi03.vsphere.local&#x27;, &#x27;folder&#x27;: &#x27;/DC0/host/DC0_C0&#x27;}, {&#x27;name&#x27;: &#x27;esxi04.vsphere.local&#x27;, &#x27;folder&#x27;: &#x27;/DC0/host/DC0_C0&#x27;}], &#x27;tags&#x27;: [{&#x27;category_id&#x27;: &#x27;urn:vmomi:InventoryServiceCategory:9fbf83de-7903-442e-8004-70fd3940297c:GLOBAL&#x27;, &#x27;category_name&#x27;: &#x27;sample_cluster_cat_0001&#x27;, &#x27;description&#x27;: &#x27;&#x27;, &#x27;id&#x27;: &#x27;urn:vmomi:InventoryServiceTag:93d680db-b3a6-4834-85ad-3e9516e8fee8:GLOBAL&#x27;, &#x27;name&#x27;: &#x27;sample_cluster_tag_0001&#x27;}]}}</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Christian Neugum (@digifuchsi)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
