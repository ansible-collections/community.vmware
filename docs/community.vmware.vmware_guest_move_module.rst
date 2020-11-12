.. _community.vmware.vmware_guest_move_module:


**********************************
community.vmware.vmware_guest_move
**********************************

**Moves virtual machines in vCenter**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to move virtual machines between folders.



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
                        <div>Destination datacenter for the move operation</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>dest_folder</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Absolute path to move an existing guest</div>
                        <div>The dest_folder should include the datacenter. ESX&#x27;s datacenter is ha-datacenter.</div>
                        <div>This parameter is case sensitive.</div>
                        <div>Examples:</div>
                        <div>dest_folder: /ha-datacenter/vm</div>
                        <div>dest_folder: ha-datacenter/vm</div>
                        <div>dest_folder: /datacenter1/vm</div>
                        <div>dest_folder: datacenter1/vm</div>
                        <div>dest_folder: /datacenter1/vm/folder1</div>
                        <div>dest_folder: datacenter1/vm/folder1</div>
                        <div>dest_folder: /folder1/datacenter1/vm</div>
                        <div>dest_folder: folder1/datacenter1/vm</div>
                        <div>dest_folder: /folder1/datacenter1/vm/folder2</div>
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
                        <div>Name of the existing virtual machine to move.</div>
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
                        <div>If multiple virtual machines matching the name, use the first or last found.</div>
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
                        <div>UUID of the virtual machine to manage if known, this is VMware&#x27;s unique identifier.</div>
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
   - Tested on vSphere 5.5 and vSphere 6.5



Examples
--------

.. code-block:: yaml

    - name: Move Virtual Machine
      community.vmware.vmware_guest_move:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: datacenter
        name: testvm-1
        dest_folder: "/{{ datacenter }}/vm"
      delegate_to: localhost

    - name: Move Virtual Machine using MoID
      community.vmware.vmware_guest_move:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: datacenter
        moid: vm-42
        dest_folder: "/{{ datacenter }}/vm"
      delegate_to: localhost

    - name: Get VM UUID
      vmware_guest_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        folder: "/{{ datacenter }}/vm"
        name: "{{ vm_name }}"
      delegate_to: localhost
      register: vm_facts

    - name: Get UUID from previous task and pass it to this task
      community.vmware.vmware_guest_move:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter }}"
        uuid: "{{ vm_facts.instance.hw_product_uuid }}"
        dest_folder: "/DataCenter/vm/path/to/new/folder/where/we/want"
      delegate_to: localhost
      register: facts



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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;annotation&#x27;: None, &#x27;current_snapshot&#x27;: None, &#x27;customvalues&#x27;: {}, &#x27;guest_consolidation_needed&#x27;: False, &#x27;guest_question&#x27;: None, &#x27;guest_tools_status&#x27;: None, &#x27;guest_tools_version&#x27;: &#x27;0&#x27;, &#x27;hw_cores_per_socket&#x27;: 1, &#x27;hw_datastores&#x27;: [&#x27;LocalDS_0&#x27;], &#x27;hw_esxi_host&#x27;: &#x27;DC0_H0&#x27;, &#x27;hw_eth0&#x27;: {&#x27;addresstype&#x27;: &#x27;generated&#x27;, &#x27;ipaddresses&#x27;: None, &#x27;label&#x27;: &#x27;ethernet-0&#x27;, &#x27;macaddress&#x27;: &#x27;00:0c:29:6b:34:2c&#x27;, &#x27;macaddress_dash&#x27;: &#x27;00-0c-29-6b-34-2c&#x27;, &#x27;summary&#x27;: &#x27;DVSwitch: 43cdd1db-1ef7-4016-9bbe-d96395616199&#x27;}, &#x27;hw_files&#x27;: [&#x27;[LocalDS_0] DC0_H0_VM0/DC0_H0_VM0.vmx&#x27;], &#x27;hw_folder&#x27;: &#x27;/F0/DC0/vm/F0&#x27;, &#x27;hw_guest_full_name&#x27;: None, &#x27;hw_guest_ha_state&#x27;: None, &#x27;hw_guest_id&#x27;: &#x27;otherGuest&#x27;, &#x27;hw_interfaces&#x27;: [&#x27;eth0&#x27;], &#x27;hw_is_template&#x27;: False, &#x27;hw_memtotal_mb&#x27;: 32, &#x27;hw_name&#x27;: &#x27;DC0_H0_VM0&#x27;, &#x27;hw_power_status&#x27;: &#x27;poweredOn&#x27;, &#x27;hw_processor_count&#x27;: 1, &#x27;hw_product_uuid&#x27;: &#x27;581c2808-64fb-45ee-871f-6a745525cb29&#x27;, &#x27;instance_uuid&#x27;: &#x27;8bcb0b6e-3a7d-4513-bf6a-051d15344352&#x27;, &#x27;ipv4&#x27;: None, &#x27;ipv6&#x27;: None, &#x27;module_hw&#x27;: True, &#x27;snapshots&#x27;: []}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Jose Angel Munoz (@imjoseangel)
