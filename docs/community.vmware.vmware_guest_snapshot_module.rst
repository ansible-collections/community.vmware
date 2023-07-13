

community.vmware.vmware_guest_snapshot module -- Manages virtual machines snapshots in vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_snapshot`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to create, delete and update snapshot(s) of the given virtual machine.
- All parameters and VMware object names are case sensitive.








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
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td valign="top">
      <p>Destination datacenter for the deploy operation.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p style="display: inline;"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Define an arbitrary description to attach to snapshot.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Destination folder, absolute or relative path to find an existing guest.</p>
      <p>This is required parameter, if <code class='docutils literal notranslate'>name</code> is supplied.</p>
      <p>The folder should include the datacenter. ESX&#x27;s datacenter is ha-datacenter.</p>
      <p>Examples:</p>
      <p>   folder: /ha-datacenter/vm</p>
      <p>   folder: ha-datacenter/vm</p>
      <p>   folder: /datacenter1/vm</p>
      <p>   folder: datacenter1/vm</p>
      <p>   folder: /datacenter1/vm/folder1</p>
      <p>   folder: datacenter1/vm/folder1</p>
      <p>   folder: /folder1/datacenter1/vm</p>
      <p>   folder: folder1/datacenter1/vm</p>
      <p>   folder: /folder1/datacenter1/vm/folder2</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The hostname or IP address of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-memory_dump"></div>
      <p style="display: inline;"><strong>memory_dump</strong></p>
      <a class="ansibleOptionLink" href="#parameter-memory_dump" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If set to <code class='docutils literal notranslate'>true</code>, memory dump of virtual machine is also included in snapshot.</p>
      <p>Note that memory snapshots take time and resources, this will take longer time to create.</p>
      <p>If virtual machine does not provide capability to take memory snapshot, then this flag is set to <code class='docutils literal notranslate'>false</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-moid"></div>
      <p style="display: inline;"><strong>moid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-moid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.</p>
      <p>This is required if <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>uuid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the virtual machine to work with.</p>
      <p>This is required parameter, if <code class='docutils literal notranslate'>uuid</code> or <code class='docutils literal notranslate'>moid</code> is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-name_match"></div>
      <p style="display: inline;"><strong>name_match</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name_match" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>If multiple VMs matching the name, use the first or last found.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;first&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;last&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-new_description"></div>
      <p style="display: inline;"><strong>new_description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-new_description" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Value to change the description of an existing snapshot to.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-new_snapshot_name"></div>
      <p style="display: inline;"><strong>new_snapshot_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-new_snapshot_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Value to rename the existing snapshot to.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <div class="ansibleOptionAnchor" id="parameter-pass"></div>
      <div class="ansibleOptionAnchor" id="parameter-pwd"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: pass, pwd</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The password of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>The port number of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Address of a proxy that will receive all HTTPS requests and relay them.</p>
      <p>The format is a hostname or a IP.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_HOST</code> will be used instead.</p>
      <p>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td valign="top">
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-quiesce"></div>
      <p style="display: inline;"><strong>quiesce</strong></p>
      <a class="ansibleOptionLink" href="#parameter-quiesce" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If set to <code class='docutils literal notranslate'>true</code> and virtual machine is powered on, it will quiesce the file system in virtual machine.</p>
      <p>Note that VMware Tools are required for this flag.</p>
      <p>If virtual machine is powered off or VMware Tools are not available, then this flag is set to <code class='docutils literal notranslate'>false</code>.</p>
      <p>If virtual machine does not provide capability to take quiesce snapshot, then this flag is set to <code class='docutils literal notranslate'>false</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-remove_children"></div>
      <p style="display: inline;"><strong>remove_children</strong></p>
      <a class="ansibleOptionLink" href="#parameter-remove_children" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>If set to <code class='docutils literal notranslate'>true</code> and state is set to <code class='docutils literal notranslate'>absent</code>, then entire snapshot subtree is set for removal.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-snapshot_name"></div>
      <p style="display: inline;"><strong>snapshot_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-snapshot_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Sets the snapshot name to manage.</p>
      <p>This param is required only if state is not <code class='docutils literal notranslate'>remove_all</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Manage snapshot(s) attached to a specific virtual machine.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code> and snapshot absent, then will create a new snapshot with the given name.</p>
      <p>If set to <code class='docutils literal notranslate'>present</code> and snapshot present, then no changes are made.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code> and snapshot present, then snapshot with the given name is removed.</p>
      <p>If set to <code class='docutils literal notranslate'>absent</code> and snapshot absent, then no changes are made.</p>
      <p>If set to <code class='docutils literal notranslate'>revert</code> and snapshot present, then virtual machine state is reverted to the given snapshot.</p>
      <p>If set to <code class='docutils literal notranslate'>revert</code> and snapshot absent, then no changes are made.</p>
      <p>If set to <code class='docutils literal notranslate'>remove_all</code> and snapshot(s) present, then all snapshot(s) will be removed.</p>
      <p>If set to <code class='docutils literal notranslate'>remove_all</code> and snapshot(s) absent, then no changes are made.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code>&#34;revert&#34;</code></p></li>
        <li><p><code>&#34;remove_all&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-use_instance_uuid"></div>
      <p style="display: inline;"><strong>use_instance_uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-use_instance_uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Whether to use the VMware instance UUID rather than the BIOS UUID.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <div class="ansibleOptionAnchor" id="parameter-admin"></div>
      <div class="ansibleOptionAnchor" id="parameter-user"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: admin, user</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>The username of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-uuid"></div>
      <p style="display: inline;"><strong>uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>UUID of the instance to manage if known, this is VMware&#x27;s BIOS UUID by default.</p>
      <p>This is required if <code class='docutils literal notranslate'>name</code> or <code class='docutils literal notranslate'>moid</code> parameter is not supplied.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td valign="top">
      <p>Allows connection when SSL certificates are not valid. Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_VALIDATE_CERTS</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p>If set to <code class='docutils literal notranslate'>true</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>




Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
      - name: Create a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: present
          snapshot_name: snap1
          description: snap1_description
        delegate_to: localhost

      - name: Remove a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: absent
          snapshot_name: snap1
        delegate_to: localhost

      - name: Revert to a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: revert
          snapshot_name: snap1
        delegate_to: localhost

      - name: Remove all snapshots of a VM
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: remove_all
        delegate_to: localhost

      - name: Remove all snapshots of a VM using MoID
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          moid: vm-42
          state: remove_all
        delegate_to: localhost

      - name: Take snapshot of a VM using quiesce and memory flag on
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: present
          snapshot_name: dummy_vm_snap_0001
          quiesce: true
          memory_dump: true
        delegate_to: localhost

      - name: Remove a snapshot and snapshot subtree
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: absent
          remove_children: true
          snapshot_name: snap1
        delegate_to: localhost

      - name: Rename a snapshot
        community.vmware.vmware_guest_snapshot:
          hostname: "{{ vcenter_hostname }}"
          username: "{{ vcenter_username }}"
          password: "{{ vcenter_password }}"
          datacenter: "{{ datacenter_name }}"
          folder: "/{{ datacenter_name }}/vm/"
          name: "{{ guest_name }}"
          state: present
          snapshot_name: current_snap_name
          new_snapshot_name: im_renamed
          new_description: "{{ new_snapshot_description }}"
        delegate_to: localhost





Return Values
-------------
The following are the fields unique to this module:

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Key</p></th>
    <th><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-snapshot_results"></div>
      <p style="display: inline;"><strong>snapshot_results</strong></p>
      <a class="ansibleOptionLink" href="#return-snapshot_results" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td valign="top">
      <p>metadata about the virtual machine snapshots</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;current_snapshot&#34;: {&#34;creation_time&#34;: &#34;2019-04-09T14:40:26.617427+00:00&#34;, &#34;description&#34;: &#34;Snapshot 4 example&#34;, &#34;id&#34;: 4, &#34;name&#34;: &#34;snapshot4&#34;, &#34;state&#34;: &#34;poweredOff&#34;}, &#34;snapshots&#34;: [{&#34;creation_time&#34;: &#34;2019-04-09T14:38:24.667543+00:00&#34;, &#34;description&#34;: &#34;Snapshot 3 example&#34;, &#34;id&#34;: 3, &#34;name&#34;: &#34;snapshot3&#34;, &#34;state&#34;: &#34;poweredOff&#34;}, {&#34;creation_time&#34;: &#34;2019-04-09T14:40:26.617427+00:00&#34;, &#34;description&#34;: &#34;Snapshot 4 example&#34;, &#34;id&#34;: 4, &#34;name&#34;: &#34;snapshot4&#34;, &#34;state&#34;: &#34;poweredOff&#34;}]}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Loic Blot (@nerzhul) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

