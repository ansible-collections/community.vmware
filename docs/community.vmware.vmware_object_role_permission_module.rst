

community.vmware.vmware_object_role_permission module -- Manage local roles on an ESXi host or vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_object_role_permission`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage object permissions on the given host or vCenter.








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
      <div class="ansibleOptionAnchor" id="parameter-group"></div>
      <p style="display: inline;"><strong>group</strong></p>
      <a class="ansibleOptionLink" href="#parameter-group" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The group to be assigned permission.</p>
      <p>Required if <code class='docutils literal notranslate'>principal</code> is not specified.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The hostname or IP address of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-object_name"></div>
      <p style="display: inline;"><strong>object_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-object_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The object name to assigned permission.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-object_type"></div>
      <p style="display: inline;"><strong>object_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-object_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The object type being targeted.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;Folder&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;VirtualMachine&#34;</code></p></li>
        <li><p><code>&#34;Datacenter&#34;</code></p></li>
        <li><p><code>&#34;ResourcePool&#34;</code></p></li>
        <li><p><code>&#34;Datastore&#34;</code></p></li>
        <li><p><code>&#34;Network&#34;</code></p></li>
        <li><p><code>&#34;HostSystem&#34;</code></p></li>
        <li><p><code>&#34;ComputeResource&#34;</code></p></li>
        <li><p><code>&#34;ClusterComputeResource&#34;</code></p></li>
        <li><p><code>&#34;DistributedVirtualSwitch&#34;</code></p></li>
        <li><p><code>&#34;DistributedVirtualPortgroup&#34;</code></p></li>
        <li><p><code>&#34;StoragePod&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
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
    <td>
      <p>The password of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The port number of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-principal"></div>
      <p style="display: inline;"><strong>principal</strong></p>
      <a class="ansibleOptionLink" href="#parameter-principal" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The user to be assigned permission.</p>
      <p>Required if <code class='docutils literal notranslate'>group</code> is not specified.</p>
      <p>If specifying domain user, required separator of domain uses backslash.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Address of a proxy that will receive all HTTPS requests and relay them.</p>
      <p>The format is a hostname or a IP.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_HOST</code> will be used instead.</p>
      <p>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-recursive"></div>
      <p style="display: inline;"><strong>recursive</strong></p>
      <a class="ansibleOptionLink" href="#parameter-recursive" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Should the permissions be recursively applied.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-role"></div>
      <p style="display: inline;"><strong>role</strong></p>
      <a class="ansibleOptionLink" href="#parameter-role" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The role to be assigned permission.</p>
      <p>User can also specify role name presented in Web UI. Supported added in 1.5.0.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Indicate desired state of the object&#x27;s permission.</p>
      <p>When <code class='docutils literal notranslate'>state=present</code>, the permission will be added if it doesn&#x27;t already exist.</p>
      <p>When <code class='docutils literal notranslate'>state=absent</code>, the permission is removed if it exists.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;present&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
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
    <td>
      <p>The username of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
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

- The login user must have the appropriate rights to administer permissions.
- Permissions for a distributed switch must be defined and managed on either the datacenter or a folder containing the switch.
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Assign user to VM folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        role: Admin
        principal: user_bob
        object_name: services
        state: present
      delegate_to: localhost

    - name: Remove user from VM folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        role: Admin
        principal: user_bob
        object_name: services
        state: absent
      delegate_to: localhost

    - name: Assign finance group to VM folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        role: Limited Users
        group: finance
        object_name: Accounts
        state: present
      delegate_to: localhost

    - name: Assign view_user Read Only permission at root folder
      community.vmware.vmware_object_role_permission:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        role: ReadOnly
        principal: view_user
        object_name: rootFolder
        state: present
      delegate_to: localhost

    - name: Assign domain user to VM folder
      community.vmware.vmware_object_role_permission:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        role: Admin
        principal: "vsphere.local\\domainuser"
        object_name: services
        state: present
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
    <td>
      <div class="ansibleOptionAnchor" id="return-changed"></div>
      <p style="display: inline;"><strong>changed</strong></p>
      <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>whether or not a change was made to the object&#x27;s role</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Derek Rushing (@kryptsi)
- Joseph Andreatta (@vmwjoseph)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

