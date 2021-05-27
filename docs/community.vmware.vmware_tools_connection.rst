.. _community.vmware.vmware_tools_connection:


*****************************
community.vmware.vmware_tools
*****************************

**Execute tasks inside a VM via VMware Tools**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Use VMware tools to run tasks in, or put/fetch files to guest operating systems running in VMware infrastructure.
- In case of Windows VMs, set ``ansible_shell_type`` to ``powershell``.
- Does not work with 'become'.



Requirements
------------
The below requirements are needed on the local Ansible controller node that executes this connection.

- pyvmomi (Python library)
- requests (Python library)


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                <th>Configuration</th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>exec_command_sleep_interval</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">float</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">0.5</div>
                </td>
                    <td>
                                <div>var: ansible_vmware_tools_exec_command_sleep_interval</div>
                    </td>
                <td>
                        <div>Time in seconds to sleep between execution of command.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>executable</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"/bin/sh"</div>
                </td>
                    <td>
                            <div> ini entries:
                                    <p>[defaults]<br>executable = /bin/sh</p>
                            </div>
                                <div>env:ANSIBLE_EXECUTABLE</div>
                                <div>var: ansible_executable</div>
                                <div>var: ansible_vmware_tools_executable</div>
                    </td>
                <td>
                        <div>shell to use for execution inside container</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>file_chunk_size</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">128</div>
                </td>
                    <td>
                                <div>var: ansible_vmware_tools_file_chunk_size</div>
                    </td>
                <td>
                        <div>File chunk size.</div>
                        <div>(Applicable when writing a file to disk, example: using the <code>fetch</code> module.)</div>
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
                                <div>env:VMWARE_VALIDATE_CERTS</div>
                                <div>var: ansible_vmware_validate_certs</div>
                    </td>
                <td>
                        <div>Verify SSL for the connection.</div>
                        <div>Note: This will validate certs for both <code>vmware_host</code> and the ESXi host running the VM.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vm_password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>var: ansible_password</div>
                                <div>var: ansible_vmware_tools_password</div>
                    </td>
                <td>
                        <div>Password for the user in guest operating system.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vm_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>var: ansible_vmware_guest_path</div>
                    </td>
                <td>
                        <div>VM path absolute to the connection.</div>
                        <div>vCenter Example: <code>Datacenter/vm/Discovered virtual machine/testVM</code>.</div>
                        <div>ESXi Host Example: <code>ha-datacenter/vm/testVM</code>.</div>
                        <div>Must include VM name, appended to &#x27;folder&#x27; as would be passed to <span class='module'>community.vmware.vmware_guest</span>.</div>
                        <div>Needs to include <em>vm</em> between the Datacenter and the rest of the VM path.</div>
                        <div>Datacenter default value for ESXi server is <code>ha-datacenter</code>.</div>
                        <div>Folder <em>vm</em> is not visible in the vSphere Web Client but necessary for VMware API to work.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vm_user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>var: ansible_user</div>
                                <div>var: ansible_vmware_tools_user</div>
                    </td>
                <td>
                        <div>VM username.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vmware_host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>env:VI_SERVER</div>
                                <div>env:VMWARE_HOST</div>
                                <div>var: ansible_host</div>
                                <div>var: ansible_vmware_host</div>
                    </td>
                <td>
                        <div>FQDN or IP Address for the connection (vCenter or ESXi Host).</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vmware_password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>env:VI_PASSWORD</div>
                                <div>env:VMWARE_PASSWORD</div>
                                <div>var: ansible_vmware_password</div>
                    </td>
                <td>
                        <div>Password for the connection.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vmware_port</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">443</div>
                </td>
                    <td>
                                <div>env:VI_PORTNUMBER</div>
                                <div>env:VMWARE_PORT</div>
                                <div>var: ansible_port</div>
                                <div>var: ansible_vmware_port</div>
                    </td>
                <td>
                        <div>Port for the connection.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>vmware_user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                    <td>
                                <div>env:VI_USERNAME</div>
                                <div>env:VMWARE_USER</div>
                                <div>var: ansible_vmware_user</div>
                    </td>
                <td>
                        <div>Username for the connection.</div>
                        <div>Requires the following permissions on the VM: - VirtualMachine.GuestOperations.Execute - VirtualMachine.GuestOperations.Modify - VirtualMachine.GuestOperations.Query</div>
                </td>
            </tr>
    </table>
    <br/>








Status
------


Authors
~~~~~~~

- Deric Crago <deric.crago@gmail.com>


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
