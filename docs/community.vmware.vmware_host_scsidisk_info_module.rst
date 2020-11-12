.. _community.vmware.vmware_host_scsidisk_info_module:


******************************************
community.vmware.vmware_host_scsidisk_info
******************************************

**Gather information about SCSI disk attached to the given ESXi**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module can be used to gather information about SCSI disk attached to the given ESXi.



Requirements
------------
The below requirements are needed on the host that executes this module.

- Python >= 2.7
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
                        <div>SCSI disk information about each ESXi server will be returned for the given cluster.</div>
                        <div>This parameter is required if <em>esxi_hostname</em> is not specified.</div>
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
                        <div>SCSI disk information about this ESXi server will be returned.</div>
                        <div>This parameter is required if <em>cluster_name</em> is not specified.</div>
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




Examples
--------

.. code-block:: yaml

    - name: Gather information SCSI disk attached to the given ESXi
      community.vmware.vmware_host_scsidisk_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        esxi_hostname: '{{ esxi_hostname }}'
      delegate_to: localhost

    - name: Gather information of all host systems from the given cluster
      community.vmware.vmware_host_scsidisk_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: '{{ cluster_name }}'
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
                    <b>hosts_scsidisk_info</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>metadata about host system SCSI disk information</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;10.65.201.106&#x27;: [{&#x27;block&#x27;: 41943040, &#x27;block_size&#x27;: 512, &#x27;canonical_name&#x27;: &#x27;t10.ATA_QEMU_HARDDISK_QM00001_&#x27;, &#x27;device_name&#x27;: &#x27;/vmfs/devices/disks/t10.ATA_QEMU_HARDDISK_QM00001_&#x27;, &#x27;device_path&#x27;: &#x27;/vmfs/devices/disks/t10.ATA_QEMU_HARDDISK_QM00001_&#x27;, &#x27;device_type&#x27;: &#x27;disk&#x27;, &#x27;display_name&#x27;: &#x27;Local ATA Disk (t10.ATA_QEMU_HARDDISK_QM00001_)&#x27;, &#x27;key&#x27;: &#x27;key-vim.host.ScsiDisk-0100000000514d30303030312020202020202020202020202051454d552048&#x27;, &#x27;local_disk&#x27;: True, &#x27;lun_type&#x27;: &#x27;disk&#x27;, &#x27;model&#x27;: &#x27;QEMU HARDDISK   &#x27;, &#x27;perenniallyReserved&#x27;: None, &#x27;protocol_endpoint&#x27;: False, &#x27;revision&#x27;: &#x27;1.5.&#x27;, &#x27;scsi_disk_type&#x27;: &#x27;native512&#x27;, &#x27;scsi_level&#x27;: 5, &#x27;serial_number&#x27;: &#x27;unavailable&#x27;, &#x27;ssd&#x27;: False, &#x27;uuid&#x27;: &#x27;0100000000514d30303030312020202020202020202020202051454d552048&#x27;, &#x27;vStorageSupport&#x27;: &#x27;vStorageUnsupported&#x27;, &#x27;vendor&#x27;: &#x27;ATA     &#x27;}]}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
