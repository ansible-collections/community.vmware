.. _community.vmware.vmware_guest_info_module:


**********************************
community.vmware.vmware_guest_info
**********************************

**Gather info about a single VM**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Gather information about a single VM on a VMware ESX cluster.
- This module was called ``vmware_guest_facts`` before Ansible 2.9. The usage did not change.



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
                    <b>datacenter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Destination datacenter for the deploy operation</div>
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
                        <div>Destination folder, absolute or relative path to find an existing guest.</div>
                        <div>This is required if name is supplied.</div>
                        <div>The folder should include the datacenter. ESX&#x27;s datacenter is ha-datacenter</div>
                        <div>Examples:</div>
                        <div>folder: /ha-datacenter/vm</div>
                        <div>folder: ha-datacenter/vm</div>
                        <div>folder: /datacenter1/vm</div>
                        <div>folder: datacenter1/vm</div>
                        <div>folder: /datacenter1/vm/folder1</div>
                        <div>folder: datacenter1/vm/folder1</div>
                        <div>folder: /folder1/datacenter1/vm</div>
                        <div>folder: folder1/datacenter1/vm</div>
                        <div>folder: /folder1/datacenter1/vm/folder2</div>
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
                    <b>moid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.</div>
                        <div>This is required if <code>name</code> or <code>uuid</code> is not supplied.</div>
                </td>
            </tr>
            <tr>
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
                        <div>Name of the VM to work with</div>
                        <div>This is required if <code>uuid</code> or <code>moid</code> is not supplied.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name_match</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>first</b>&nbsp;&larr;</div></li>
                                    <li>last</li>
                        </ul>
                </td>
                <td>
                        <div>If multiple VMs matching the name, use the first or last found</div>
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
                        <div>&quot;config.hardware.memoryMB&quot;,</div>
                        <div>&quot;config.hardware.numCPU&quot;,</div>
                        <div>&quot;guest.disk&quot;,</div>
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
                    <b>tag_details</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                    <div style="font-style: italic; font-size: small; color: darkgreen">added in 1.4.0</div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                    <li>yes</li>
                        </ul>
                </td>
                <td>
                        <div>If set <code>True</code>, detail information about &#x27;tags&#x27; returned.</div>
                        <div>Without this flag, the &#x27;tags&#x27; returns a list of tag names.</div>
                        <div>With this flag, the &#x27;tags&#x27; returns a list of dict about tag information with additional details like category name, category id, and tag id.</div>
                        <div>This parameter is added to maintain backward compatability.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tags</b>
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
                        <div>Whether to show tags or not.</div>
                        <div>If set <code>True</code>, shows tags information. Returns a list of tag names.</div>
                        <div>If set <code>False</code>, hides tags information.</div>
                        <div>vSphere Automation SDK is required.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>use_instance_uuid</b>
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
                        <div>Whether to use the VMware instance UUID rather than the BIOS UUID.</div>
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
                    <b>uuid</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>UUID of the instance to manage if known, this is VMware&#x27;s unique identifier.</div>
                        <div>This is required if <code>name</code> or <code>moid</code> is not supplied.</div>
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
   - Tested on vSphere 5.5, 6.7
   - All modules requires API write access and hence is not supported on a free ESXi license.



Examples
--------

.. code-block:: yaml

    - name: Gather info from standalone ESXi server having datacenter as 'ha-datacenter'
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
      delegate_to: localhost
      register: info

    - name: Gather some info from a guest using the vSphere API output schema
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: "{{ vm_name }}"
        schema: "vsphere"
        properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
      delegate_to: localhost
      register: info

    - name: Gather some information about a guest using MoID
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        moid: vm-42
        schema: "vsphere"
        properties: ["config.hardware.memoryMB", "guest.disk", "overallStatus"]
      delegate_to: localhost
      register: vm_moid_info

    - name: Gather Managed object ID (moid) from a guest using the vSphere API output schema for REST Calls
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: "{{ vm_name }}"
        schema: "vsphere"
        properties:
          - _moId
      delegate_to: localhost
      register: moid_info

    - name: Gather detailed information about tags and category associated with the given VM
      community.vmware.vmware_guest_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        name: "{{ vm_name }}"
        tags: True
        tag_details: True
      register: detailed_tag_info



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
                    <b>instance</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>metadata about the virtual machine</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;advanced_settings&#x27;: {}, &#x27;annotation&#x27;: &#x27;&#x27;, &#x27;current_snapshot&#x27;: None, &#x27;customvalues&#x27;: {}, &#x27;guest_consolidation_needed&#x27;: False, &#x27;guest_question&#x27;: None, &#x27;guest_tools_status&#x27;: &#x27;guestToolsNotRunning&#x27;, &#x27;guest_tools_version&#x27;: &#x27;10247&#x27;, &#x27;hw_cores_per_socket&#x27;: 1, &#x27;hw_datastores&#x27;: [&#x27;ds_226_3&#x27;], &#x27;hw_esxi_host&#x27;: &#x27;10.76.33.226&#x27;, &#x27;hw_eth0&#x27;: {&#x27;addresstype&#x27;: &#x27;assigned&#x27;, &#x27;ipaddresses&#x27;: None, &#x27;label&#x27;: &#x27;Network adapter 1&#x27;, &#x27;macaddress&#x27;: &#x27;00:50:56:87:a5:9a&#x27;, &#x27;macaddress_dash&#x27;: &#x27;00-50-56-87-a5-9a&#x27;, &#x27;portgroup_key&#x27;: None, &#x27;portgroup_portkey&#x27;: None, &#x27;summary&#x27;: &#x27;VM Network&#x27;}, &#x27;hw_files&#x27;: [&#x27;[ds_226_3] ubuntu_t/ubuntu_t.vmx&#x27;, &#x27;[ds_226_3] ubuntu_t/ubuntu_t.nvram&#x27;, &#x27;[ds_226_3] ubuntu_t/ubuntu_t.vmsd&#x27;, &#x27;[ds_226_3] ubuntu_t/vmware.log&#x27;, &#x27;[ds_226_3] u0001/u0001.vmdk&#x27;], &#x27;hw_folder&#x27;: &#x27;/DC0/vm/Discovered virtual machine&#x27;, &#x27;hw_guest_full_name&#x27;: None, &#x27;hw_guest_ha_state&#x27;: None, &#x27;hw_guest_id&#x27;: None, &#x27;hw_interfaces&#x27;: [&#x27;eth0&#x27;], &#x27;hw_is_template&#x27;: False, &#x27;hw_memtotal_mb&#x27;: 1024, &#x27;hw_name&#x27;: &#x27;ubuntu_t&#x27;, &#x27;hw_power_status&#x27;: &#x27;poweredOff&#x27;, &#x27;hw_processor_count&#x27;: 1, &#x27;hw_product_uuid&#x27;: &#x27;4207072c-edd8-3bd5-64dc-903fd3a0db04&#x27;, &#x27;hw_version&#x27;: &#x27;vmx-13&#x27;, &#x27;instance_uuid&#x27;: &#x27;5007769d-add3-1e12-f1fe-225ae2a07caf&#x27;, &#x27;ipv4&#x27;: None, &#x27;ipv6&#x27;: None, &#x27;module_hw&#x27;: True, &#x27;snapshots&#x27;: [], &#x27;tags&#x27;: [&#x27;backup&#x27;], &#x27;vnc&#x27;: {}, &#x27;moid&#x27;: &#x27;vm-42&#x27;, &#x27;vimref&#x27;: &#x27;vim.VirtualMachine:vm-42&#x27;}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Loic Blot (@nerzhul) <loic.blot@unix-experience.fr>
