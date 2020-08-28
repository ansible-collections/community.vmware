.. _community.vmware.vmware_guest_disk_module:


**********************************
community.vmware.vmware_guest_disk
**********************************

**Manage disks related to virtual machine in given vCenter infrastructure**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to add, remove and update disks belonging to given virtual machine.
- All parameters and VMware object names are case sensitive.
- This module is destructive in nature, please read documentation carefully before proceeding.
- Be careful while removing disk specified as this may lead to data loss.



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
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="4">
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
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>disk</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">[]</div>
                </td>
                <td>
                        <div>A list of disks to add.</div>
                        <div>The virtual disk related information is provided using this list.</div>
                        <div>All values and parameters are case sensitive.</div>
                        <div>Valid attributes are:</div>
                        <div>- <code>size[_tb,_gb,_mb,_kb]</code> (integer): Disk storage size in specified unit.</div>
                        <div>If <code>size</code> specified then unit must be specified. There is no space allowed in between size number and unit.</div>
                        <div>Only first occurrence in disk element will be considered, even if there are multiple size* parameters available.</div>
                        <div>- <code>type</code> (string): Valid values are:</div>
                        <div>- <code>thin</code> thin disk</div>
                        <div>- <code>eagerzeroedthick</code> eagerzeroedthick disk</div>
                        <div>- <code>thick</code> thick disk</div>
                        <div>Default: <code>thick</code> thick disk, no eagerzero.</div>
                        <div>- <code>disk_mode</code> (string): Type of disk mode. Valid values are:</div>
                        <div>- <code>persistent</code> Changes are immediately and permanently written to the virtual disk. This is default.</div>
                        <div>- <code>independent_persistent</code> Same as persistent, but not affected by snapshots.</div>
                        <div>- <code>independent_nonpersistent</code> Changes to virtual disk are made to a redo log and discarded at power off, but not affected by snapshots.</div>
                        <div>- <code>sharing</code> (bool): The sharing mode of the virtual disk. The default value is no sharing.</div>
                        <div>Setting <code>sharing</code> means that multiple virtual machines can write to the virtual disk.</div>
                        <div>Sharing can only be set if <code>type</code> is <code>eagerzeroedthick</code>.</div>
                        <div>- <code>datastore</code> (string): Name of datastore or datastore cluster to be used for the disk.</div>
                        <div>- <code>autoselect_datastore</code> (bool): Select the less used datastore. Specify only if <code>datastore</code> is not specified.</div>
                        <div>- <code>scsi_controller</code> (integer): SCSI controller number. Valid value range from 0 to 3.</div>
                        <div>Only 4 SCSI controllers are allowed per VM.</div>
                        <div>Care should be taken while specifying <code>scsi_controller</code> is 0 and <code>unit_number</code> as 0 as this disk may contain OS.</div>
                        <div>- <code>unit_number</code> (integer): Disk Unit Number. Valid value range from 0 to 15. Only 15 disks are allowed per SCSI Controller.</div>
                        <div>- <code>scsi_type</code> (string): Type of SCSI controller. This value is required only for the first occurrence of SCSI Controller.</div>
                        <div>This value is ignored, if SCSI Controller is already present or <code>state</code> is <code>absent</code>.</div>
                        <div>Valid values are <code>buslogic</code>, <code>lsilogic</code>, <code>lsilogicsas</code> and <code>paravirtual</code>.</div>
                        <div><code>paravirtual</code> is default value for this parameter.</div>
                        <div>- <code>destroy</code> (bool): If <code>state</code> is <code>absent</code>, make sure the disk file is deleted from the datastore (default <code>yes</code>).</div>
                        <div>Added in version 2.10.</div>
                        <div>- <code>filename</code> (string): Existing disk image to be used. Filename must already exist on the datastore.</div>
                        <div>Specify filename string in <code>[datastore_name] path/to/file.vmdk</code> format. Added in version 2.10.</div>
                        <div>- <code>state</code> (string): State of disk. This is either &quot;absent&quot; or &quot;present&quot;.</div>
                        <div>If <code>state</code> is set to <code>absent</code>, disk will be removed permanently from virtual machine configuration and from VMware storage.</div>
                        <div>If <code>state</code> is set to <code>present</code>, disk will be added if not present at given SCSI Controller and Unit Number.</div>
                        <div>If <code>state</code> is set to <code>present</code> and disk exists with different size, disk size is increased.</div>
                        <div>Reducing disk size is not allowed.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>iolimit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Section specifies the shares and limit for storage I/O resource.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Section specifies values for limit where the utilization of a virtual machine will not exceed, even if there are available resources.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>shares</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies different types of shares user can add for the given disk.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Specifies different level for the shares section.</div>
                        <div>Valid values are low, normal, high, custom.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level_value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Custom value when <code>level</code> is set as <code>custom</code>.</div>
                </td>
            </tr>


            <tr>
                    <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>shares</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">list</span>
                         / <span style="color: purple">elements=dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>section for iolimit section tells about what are all different types of shares user can add for disk.</div>
                </td>
            </tr>
                                <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>tells about different level for the shares section, valid values are low,normal,high,custom.</div>
                </td>
            </tr>
            <tr>
                    <td class="elbow-placeholder"></td>
                    <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>level_value</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>custom value when level is set as custom.</div>
                </td>
            </tr>


            <tr>
                <td colspan="4">
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
                        <div>This is a required parameter, only if multiple VMs are found with same name.</div>
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
                <td colspan="4">
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
                <td colspan="4">
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
                <td colspan="4">
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
                        <div>This is a required parameter, if parameter <code>uuid</code> or <code>moid</code> is not supplied.</div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
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
                <td colspan="4">
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
                <td colspan="4">
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
                <td colspan="4">
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
                <td colspan="4">
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
                <td colspan="4">
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
                <td colspan="4">
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
                        <div>This is a required parameter, if parameter <code>name</code> or <code>moid</code> is not supplied.</div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
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
   - Tested on vSphere 6.0 and 6.5



Examples
--------

.. code-block:: yaml+jinja

    - name: Add disks to virtual machine using UUID
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: no
        uuid: 421e4592-c069-924d-ce20-7e7533fab926
        disk:
          - size_mb: 10
            type: thin
            datastore: datacluster0
            state: present
            scsi_controller: 1
            unit_number: 1
            scsi_type: 'paravirtual'
            disk_mode: 'persistent'
          - size_gb: 10
            type: eagerzeroedthick
            state: present
            autoselect_datastore: True
            scsi_controller: 2
            scsi_type: 'buslogic'
            unit_number: 12
            disk_mode: 'independent_persistent'
          - size: 10Gb
            type: eagerzeroedthick
            state: present
            autoselect_datastore: True
            scsi_controller: 2
            scsi_type: 'buslogic'
            unit_number: 1
            disk_mode: 'independent_nonpersistent'
          - filename: "[datastore1] path/to/existing/disk.vmdk"
      delegate_to: localhost
      register: disk_facts

    - name: Add disks with specified shares to the virtual machine
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: no
        disk:
          - size_gb: 1
            type: thin
            datastore: datacluster0
            state: present
            scsi_controller: 1
            unit_number: 1
            disk_mode: 'independent_persistent'
            shares:
              level: custom
              level_value: 1300
      delegate_to: localhost
      register: test_custom_shares

    - name: create new disk with custom IO limits and shares in IO Limits
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: no
        disk:
          - size_gb: 1
            type: thin
            datastore: datacluster0
            state: present
            scsi_controller: 1
            unit_number: 1
            disk_mode: 'independent_persistent'
            iolimit:
                limit: 1506
                shares:
                  level: custom
                  level_value: 1305
      delegate_to: localhost
      register: test_custom_IoLimit_shares

    - name: Remove disks from virtual machine using name
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: no
        name: VM_225
        disk:
          - state: absent
            scsi_controller: 1
            unit_number: 1
      delegate_to: localhost
      register: disk_facts

    - name: Remove disk from virtual machine using moid
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: no
        moid: vm-42
        disk:
          - state: absent
            scsi_controller: 1
            unit_number: 1
      delegate_to: localhost
      register: disk_facts

    - name: Remove disk from virtual machine but keep the VMDK file on the datastore
      community.vmware.vmware_guest_disk:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter: "{{ datacenter_name }}"
        validate_certs: no
        name: VM_225
        disk:
          - state: absent
            scsi_controller: 1
            unit_number: 2
            destroy: no
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
                    <b>disk_status</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>metadata about the virtual machine&#x27;s disks after managing them</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;0&#x27;: {&#x27;backing_datastore&#x27;: &#x27;datastore2&#x27;, &#x27;backing_disk_mode&#x27;: &#x27;persistent&#x27;, &#x27;backing_eagerlyscrub&#x27;: False, &#x27;backing_filename&#x27;: &#x27;[datastore2] VM_225/VM_225.vmdk&#x27;, &#x27;backing_thinprovisioned&#x27;: False, &#x27;backing_writethrough&#x27;: False, &#x27;backing_uuid&#x27;: &#x27;421e4592-c069-924d-ce20-7e7533fab926&#x27;, &#x27;capacity_in_bytes&#x27;: 10485760, &#x27;capacity_in_kb&#x27;: 10240, &#x27;controller_key&#x27;: 1000, &#x27;key&#x27;: 2000, &#x27;label&#x27;: &#x27;Hard disk 1&#x27;, &#x27;summary&#x27;: &#x27;10,240 KB&#x27;, &#x27;unit_number&#x27;: 0}}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>
