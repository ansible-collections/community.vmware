

community.vmware.vmware_tools connection -- Execute tasks inside a VM via VMware Tools
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This connection plugin is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this connection plugin,
see `Requirements <ansible_collections.community.vmware.vmware_tools_connection_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_tools`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Use VMware tools to run tasks in, or put/fetch files to guest operating systems running in VMware infrastructure.
- In case of Windows VMs, set \ :literal:`ansible\_shell\_type`\  to \ :literal:`powershell`\ .
- Does not work with 'become'.



.. _ansible_collections.community.vmware.vmware_tools_connection_requirements:

Requirements
------------
The below requirements are needed on the local controller node that executes this connection.

- requests (Python library)






Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-exec_command_sleep_interval"></div>
      <p style="display: inline;"><strong>exec_command_sleep_interval</strong></p>
      <a class="ansibleOptionLink" href="#parameter-exec_command_sleep_interval" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">float</span>
      </p>

    </td>
    <td>
      <p>Time in seconds to sleep between execution of command.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">0.5</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: ansible_vmware_tools_exec_command_sleep_interval</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-executable"></div>
      <p style="display: inline;"><strong>executable</strong></p>
      <a class="ansibleOptionLink" href="#parameter-executable" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>shell to use for execution inside container</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;/bin/sh&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[defaults]
  executable = /bin/sh</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_EXECUTABLE</code></p>

      </li>
      <li>
        <p>Variable: ansible_executable</p>

      </li>
      <li>
        <p>Variable: ansible_vmware_tools_executable</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-file_chunk_size"></div>
      <p style="display: inline;"><strong>file_chunk_size</strong></p>
      <a class="ansibleOptionLink" href="#parameter-file_chunk_size" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td>
      <p>File chunk size.</p>
      <p>(Applicable when writing a file to disk, example: using the <code class='docutils literal notranslate'>fetch</code> module.)</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">128</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: ansible_vmware_tools_file_chunk_size</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>Verify SSL for the connection.</p>
      <p>Note: This will validate certs for both <code class='docutils literal notranslate'>vmware_host</code> and the ESXi host running the VM.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_VALIDATE_CERTS</code></p>

      </li>
      <li>
        <p>Variable: ansible_vmware_validate_certs</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vm_password"></div>
      <p style="display: inline;"><strong>vm_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>Password for the user in guest operating system.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: ansible_password</p>

      </li>
      <li>
        <p>Variable: ansible_vmware_tools_password</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vm_path"></div>
      <p style="display: inline;"><strong>vm_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>Mutually exclusive with vm_uuid</p>
      <p>VM path absolute to the connection.</p>
      <p>vCenter Example: <code class='docutils literal notranslate'>Datacenter/vm/Discovered virtual machine/testVM</code>.</p>
      <p>ESXi Host Example: <code class='docutils literal notranslate'>ha-datacenter/vm/testVM</code>.</p>
      <p>Must include VM name, appended to &#x27;folder&#x27; as would be passed to <a href='../../community/vmware/vmware_guest_module.html' class='module'>community.vmware.vmware_guest</a>.</p>
      <p>Needs to include <em>vm</em> between the Datacenter and the rest of the VM path.</p>
      <p>Datacenter default value for ESXi server is <code class='docutils literal notranslate'>ha-datacenter</code>.</p>
      <p>Folder <em>vm</em> is not visible in the vSphere Web Client but necessary for VMware API to work.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: ansible_vmware_guest_path</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vm_user"></div>
      <p style="display: inline;"><strong>vm_user</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_user" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>VM username.</p>
      <p><code class='docutils literal notranslate'>ansible_vmware_tools_user</code> is used for connecting to the VM.</p>
      <p><code class='docutils literal notranslate'>ansible_user</code> is used by Ansible on the VM.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: ansible_user</p>

      </li>
      <li>
        <p>Variable: ansible_vmware_tools_user</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vm_uuid"></div>
      <p style="display: inline;"><strong>vm_uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>Mutually exclusive with vm_path</p>
      <p>VM UUID to the connection.</p>
      <p>UUID of the virtual machine from property config.uuid of vmware_vm_inventory plugin</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Variable: ansible_vmware_guest_uuid</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vmware_host"></div>
      <p style="display: inline;"><strong>vmware_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vmware_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>FQDN or IP Address for the connection (vCenter or ESXi Host).</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VI_SERVER</code></p>

      </li>
      <li>
        <p>Environment variable: <code>VMWARE_HOST</code></p>

      </li>
      <li>
        <p>Variable: ansible_host</p>

      </li>
      <li>
        <p>Variable: ansible_vmware_host</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vmware_password"></div>
      <p style="display: inline;"><strong>vmware_password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vmware_password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>Password for the connection.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VI_PASSWORD</code></p>

      </li>
      <li>
        <p>Environment variable: <code>VMWARE_PASSWORD</code></p>

      </li>
      <li>
        <p>Variable: ansible_vmware_password</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vmware_port"></div>
      <p style="display: inline;"><strong>vmware_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vmware_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>Port for the connection.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VI_PORTNUMBER</code></p>

      </li>
      <li>
        <p>Environment variable: <code>VMWARE_PORT</code></p>

      </li>
      <li>
        <p>Variable: ansible_port</p>

      </li>
      <li>
        <p>Variable: ansible_vmware_port</p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vmware_user"></div>
      <p style="display: inline;"><strong>vmware_user</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vmware_user" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>Username for the connection.</p>
      <p>Requires the following permissions on the VM: - VirtualMachine.GuestOperations.Execute - VirtualMachine.GuestOperations.Modify - VirtualMachine.GuestOperations.Query</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VI_USERNAME</code></p>

      </li>
      <li>
        <p>Environment variable: <code>VMWARE_USER</code></p>

      </li>
      <li>
        <p>Variable: ansible_vmware_user</p>

      </li>
      </ul>
    </td>
  </tr>
  </tbody>
  </table>











Authors
~~~~~~~

- Deric Crago (@dericcrago) 


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

