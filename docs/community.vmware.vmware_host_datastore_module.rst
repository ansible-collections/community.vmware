

community.vmware.vmware_host_datastore module -- Manage a datastore on ESXi host
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_datastore`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to mount/umount datastore on ESXi host.
- This module only supports NFS (NFS v3 or NFS v4.1) and VMFS datastores.
- For VMFS datastore, available device must already be connected on ESXi host.
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
    <td>
      <div class="ansibleOptionAnchor" id="parameter-auto_expand"></div>
      <p style="display: inline;"><strong>auto_expand</strong></p>
      <a class="ansibleOptionLink" href="#parameter-auto_expand" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Expand a datastore capacity to full if it has free capacity.</p>
      <p>This parameter can&#x27;t be extend using another datastore.</p>
      <p>A use case example in <em>auto_expand</em>, it can be used to expand a datastore capacity after increasing LUN volume.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datastore_name"></div>
      <p style="display: inline;"><strong>datastore_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datastore_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Name of the datastore to add/remove.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datastore_type"></div>
      <p style="display: inline;"><strong>datastore_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datastore_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Type of the datastore to configure (nfs/nfs41/vmfs).</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;nfs&#34;</code></p></li>
        <li><p><code>&#34;nfs41&#34;</code></p></li>
        <li><p><code>&#34;vmfs&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-esxi_hostname"></div>
      <p style="display: inline;"><strong>esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>ESXi hostname to manage the datastore.</p>
      <p>Required when used with a vcenter</p>
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
      <div class="ansibleOptionAnchor" id="parameter-nfs_path"></div>
      <p style="display: inline;"><strong>nfs_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nfs_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Resource path on NFS host.</p>
      <p>Required if datastore type is set to <code class='docutils literal notranslate'>nfs</code>/<code class='docutils literal notranslate'>nfs41</code> and state is set to <code class='docutils literal notranslate'>present</code>, else unused.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-nfs_ro"></div>
      <p style="display: inline;"><strong>nfs_ro</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nfs_ro" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>ReadOnly or ReadWrite mount.</p>
      <p>Unused if datastore type is not set to <code class='docutils literal notranslate'>nfs</code>/<code class='docutils literal notranslate'>nfs41</code> and state is not set to <code class='docutils literal notranslate'>present</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-nfs_server"></div>
      <p style="display: inline;"><strong>nfs_server</strong></p>
      <a class="ansibleOptionLink" href="#parameter-nfs_server" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>NFS host serving nfs datastore.</p>
      <p>Required if datastore type is set to <code class='docutils literal notranslate'>nfs</code>/<code class='docutils literal notranslate'>nfs41</code> and state is set to <code class='docutils literal notranslate'>present</code>, else unused.</p>
      <p>Two or more servers can be defined if datastore type is set to <code class='docutils literal notranslate'>nfs41</code></p>
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
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>present: Mount datastore on host if datastore is absent else do nothing.</p>
      <p>absent: Umount datastore if datastore is present else do nothing.</p>
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
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vmfs_device_name"></div>
      <p style="display: inline;"><strong>vmfs_device_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vmfs_device_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the device to be used as VMFS datastore.</p>
      <p>Required for VMFS datastore type and state is set to <code class='docutils literal notranslate'>present</code>, else unused.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vmfs_version"></div>
      <p style="display: inline;"><strong>vmfs_version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vmfs_version" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>VMFS version to use for datastore creation.</p>
      <p>Unused if datastore type is not set to <code class='docutils literal notranslate'>vmfs</code> and state is not set to <code class='docutils literal notranslate'>present</code>.</p>
    </td>
  </tr>
  </tbody>
  </table>




Notes
-----

- Kerberos authentication with NFS v4.1 isn't implemented
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Mount VMFS datastores to ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          datastore_name: '{{ item.name }}'
          datastore_type: '{{ item.type }}'
          vmfs_device_name: 'naa.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
          vmfs_version: 6
          esxi_hostname: '{{ inventory_hostname }}'
          state: present
      delegate_to: localhost

    - name: Mount NFS datastores to ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          datastore_name: '{{ item.name }}'
          datastore_type: '{{ item.type }}'
          nfs_server: '{{ item.server }}'
          nfs_path: '{{ item.path }}'
          nfs_ro: false
          esxi_hostname: '{{ inventory_hostname }}'
          state: present
      delegate_to: localhost
      loop:
          - { 'name': 'NasDS_vol01', 'server': 'nas01', 'path': '/mnt/vol01', 'type': 'nfs'}
          - { 'name': 'NasDS_vol02', 'server': 'nas01', 'path': '/mnt/vol02', 'type': 'nfs'}

    - name: Mount NFS v4.1 datastores to ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ vcenter_hostname }}'
          username: '{{ vcenter_username }}'
          password: '{{ vcenter_password }}'
          datastore_name: '{{ item.name }}'
          datastore_type: '{{ item.type }}'
          nfs_server: '{{ item.server }}'
          nfs_path: '{{ item.path }}'
          nfs_ro: false
          esxi_hostname: '{{ inventory_hostname }}'
          state: present
      delegate_to: localhost
      loop:
          - { 'name': 'NasDS_vol03', 'server': 'nas01,nas02', 'path': '/mnt/vol01', 'type': 'nfs41'}
          - { 'name': 'NasDS_vol04', 'server': 'nas01,nas02', 'path': '/mnt/vol02', 'type': 'nfs41'}

    - name: Remove/Umount Datastores from a ESXi
      community.vmware.vmware_host_datastore:
          hostname: '{{ esxi_hostname }}'
          username: '{{ esxi_username }}'
          password: '{{ esxi_password }}'
          datastore_name: NasDS_vol01
          state: absent
      delegate_to: localhost







Authors
~~~~~~~

- Ludovic Rivallain (@lrivallain) 
- Christian Kotte (@ckotte) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

