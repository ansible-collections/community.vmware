.. _community.vmware.vmware_vm_info_module:


*******************************
community.vmware.vmware_vm_info
*******************************

**Return basic info pertaining to a VMware machine guest**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Return basic information pertaining to a vSphere or ESXi virtual machine guest.
- Cluster name as fact is added in version 2.7.
- This module was called ``vmware_vm_facts`` before Ansible 2.9. The usage did not change.



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
                    <b>folder</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specify a folder location of VMs to gather information from.</div>
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
                    <b>show_attribute</b>
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
                        <div>Attributes related to VM guest shown in information only when this is set <code>true</code>.</div>
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
                        <div>Tags related to virtual machine are shown if set to <code>True</code>.</div>
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
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vm_type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>all</b>&nbsp;&larr;</div></li>
                                    <li>vm</li>
                                    <li>template</li>
                        </ul>
                </td>
                <td>
                        <div>If set to <code>vm</code>, then information are gathered for virtual machines only.</div>
                        <div>If set to <code>template</code>, then information are gathered for virtual machine templates only.</div>
                        <div>If set to <code>all</code>, then information are gathered for all virtual machines and virtual machine templates.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Tested on ESXi 6.7, vSphere 5.5 and vSphere 6.5
   - From 2.8 and onwards, information are returned as list of dict instead of dict.
   - Fact about ``moid`` added in VMware collection 1.4.0.



Examples
--------

.. code-block:: yaml

    - name: Gather all registered virtual machines
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost
      register: vminfo

    - debug:
        var: vminfo.virtual_machines

    - name: Gather only registered virtual machine templates
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_type: template
      delegate_to: localhost
      register: template_info

    - debug:
        var: template_info.virtual_machines

    - name: Gather only registered virtual machines
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_type: vm
      delegate_to: localhost
      register: vm_info

    - debug:
        var: vm_info.virtual_machines

    - name: Get UUID from given VM Name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
            folder: "/datacenter/vm/folder"
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.uuid }}"
          with_items:
            - "{{ vm_info.virtual_machines | json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"

    - name: Get Tags from given VM Name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
            folder: "/datacenter/vm/folder"
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.tags }}"
          with_items:
            - "{{ vm_info.virtual_machines | json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"

    - name: Gather all VMs from a specific folder
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        folder: "/Asia-Datacenter1/vm/prod"
      delegate_to: localhost
      register: vm_info



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
                    <b>virtual_machines</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>success</td>
                <td>
                            <div>list of dictionary of virtual machines and their information</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;guest_name&#x27;: &#x27;ubuntu_t&#x27;, &#x27;datacenter&#x27;: &#x27;Datacenter-1&#x27;, &#x27;cluster&#x27;: None, &#x27;esxi_hostname&#x27;: &#x27;10.76.33.226&#x27;, &#x27;folder&#x27;: &#x27;/Datacenter-1/vm&#x27;, &#x27;guest_fullname&#x27;: &#x27;Ubuntu Linux (64-bit)&#x27;, &#x27;ip_address&#x27;: &#x27;&#x27;, &#x27;mac_address&#x27;: [&#x27;00:50:56:87:a5:9a&#x27;], &#x27;power_state&#x27;: &#x27;poweredOff&#x27;, &#x27;uuid&#x27;: &#x27;4207072c-edd8-3bd5-64dc-903fd3a0db04&#x27;, &#x27;vm_network&#x27;: {&#x27;00:50:56:87:a5:9a&#x27;: {&#x27;ipv4&#x27;: [&#x27;10.76.33.228&#x27;], &#x27;ipv6&#x27;: []}}, &#x27;attributes&#x27;: {&#x27;job&#x27;: &#x27;backup-prepare&#x27;}, &#x27;tags&#x27;: [{&#x27;category_id&#x27;: &#x27;urn:vmomi:InventoryServiceCategory:b316cc45-f1a9-4277-811d-56c7e7975203:GLOBAL&#x27;, &#x27;category_name&#x27;: &#x27;cat_0001&#x27;, &#x27;description&#x27;: &#x27;&#x27;, &#x27;id&#x27;: &#x27;urn:vmomi:InventoryServiceTag:43737ec0-b832-4abf-abb1-fd2448ce3b26:GLOBAL&#x27;, &#x27;name&#x27;: &#x27;tag_0001&#x27;}], &#x27;moid&#x27;: &#x27;vm-24&#x27;}]</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Fedor Vompe (@sumkincpp)
