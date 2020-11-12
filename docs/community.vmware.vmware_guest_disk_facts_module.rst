.. _community.vmware.vmware_guest_disk_facts_module:


****************************************
community.vmware.vmware_guest_disk_facts
****************************************

**Gather facts about disks of given virtual machine**



.. contents::
   :local:
   :depth: 1

DEPRECATED
----------
:Removed in collection release after 2021-12-01
:Why: Deprecated in favour of :ref:`community.vmware.vmware_guest_disk_info <community.vmware.vmware_guest_disk_info_module>` module.
:Alternative: Use :ref:`community.vmware.vmware_guest_disk_info <community.vmware.vmware_guest_disk_info_module>` instead.



Synopsis
--------
- This module can be used to gather facts about disks belonging to given virtual machine.
- All parameters and VMware object names are case sensitive.



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
                        <div>The datacenter name to which virtual machine belongs to.</div>
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
                        <div>This is required parameter, only if multiple VMs are found with same name.</div>
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
                        <div>Name of the virtual machine.</div>
                        <div>This is required parameter, if parameter <code>uuid</code> or <code>moid</code> is not supplied.</div>
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
                        <div>UUID of the instance to gather facts if known, this is VMware&#x27;s unique identifier.</div>
                        <div>This is required parameter, if parameter <code>name</code> or <code>moid</code> is not supplied.</div>
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
   - Tested on vSphere 6.0 and 6.5.
   - Disk UUID information is added in version 2.8.
   - Additional information about guest disk backings added in version 2.8.



Examples
--------

.. code-block:: yaml

    - name: Gather disk facts from virtual machine using UUID
      community.vmware.vmware_guest_disk_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
      delegate_to: localhost
      register: disk_facts

    - name: Gather disk facts from virtual machine using name
      community.vmware.vmware_guest_disk_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        name: VM_225
      delegate_to: localhost
      register: disk_facts

    - name: Gather disk facts from virtual machine using moid
      community.vmware.vmware_guest_disk_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: ha-datacenter
        moid: vm-42
      delegate_to: localhost
      register: disk_facts



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
                    <b>guest_disk_facts</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>metadata about the virtual machine&#x27;s disks</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;0&#x27;: {&#x27;backing_datastore&#x27;: &#x27;datastore2&#x27;, &#x27;backing_disk_mode&#x27;: &#x27;persistent&#x27;, &#x27;backing_eagerlyscrub&#x27;: False, &#x27;backing_filename&#x27;: &#x27;[datastore2] VM_225/VM_225.vmdk&#x27;, &#x27;backing_thinprovisioned&#x27;: False, &#x27;backing_type&#x27;: &#x27;FlatVer2&#x27;, &#x27;backing_writethrough&#x27;: False, &#x27;backing_uuid&#x27;: &#x27;200C3A00-f82a-97af-02ff-62a595f0020a&#x27;, &#x27;capacity_in_bytes&#x27;: 10485760, &#x27;capacity_in_kb&#x27;: 10240, &#x27;controller_bus_number&#x27;: 0, &#x27;controller_key&#x27;: 1000, &#x27;controller_type&#x27;: &#x27;paravirtual&#x27;, &#x27;key&#x27;: 2000, &#x27;label&#x27;: &#x27;Hard disk 1&#x27;, &#x27;summary&#x27;: &#x27;10,240 KB&#x27;, &#x27;unit_number&#x27;: 0}, &#x27;1&#x27;: {&#x27;backing_datastore&#x27;: &#x27;datastore3&#x27;, &#x27;backing_devicename&#x27;: &#x27;vml.012345678901234567890123456789012345678901234567890123&#x27;, &#x27;backing_disk_mode&#x27;: &#x27;independent_persistent&#x27;, &#x27;backing_filename&#x27;: &#x27;[datastore3] VM_226/VM_226.vmdk&#x27;, &#x27;backing_lunuuid&#x27;: &#x27;012345678901234567890123456789012345678901234567890123&#x27;, &#x27;backing_type&#x27;: &#x27;RawDiskMappingVer1&#x27;, &#x27;backing_uuid&#x27;: None, &#x27;capacity_in_bytes&#x27;: 15728640, &#x27;capacity_in_kb&#x27;: 15360, &#x27;controller_bus_number&#x27;: 0, &#x27;controller_key&#x27;: 1000, &#x27;controller_type&#x27;: &#x27;paravirtual&#x27;, &#x27;key&#x27;: 2001, &#x27;label&#x27;: &#x27;Hard disk 3&#x27;, &#x27;summary&#x27;: &#x27;15,360 KB&#x27;, &#x27;unit_number&#x27;: 1}}</div>
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

- Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>
