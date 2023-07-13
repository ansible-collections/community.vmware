

community.vmware.vmware_vmotion module -- Move a virtual machine using vMotion, and/or its vmdks using storage vMotion.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vmotion`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Using VMware vCenter, move a virtual machine using vMotion to a different host, and/or its vmdks to another datastore using storage vMotion.








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
      <div class="ansibleOptionAnchor" id="parameter-destination_cluster"></div>
      <p style="display: inline;"><strong>destination_cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.5.0</i></p>
    </td>
    <td valign="top">
      <p>Name of the destination cluster the virtual machine should be running on.</p>
      <p>Only works if drs is enabled for this cluster.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_datacenter"></div>
      <p style="display: inline;"><strong>destination_datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the destination datacenter the datastore is located on.</p>
      <p>Optional, required only when datastores are shared across datacenters.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_datastore"></div>
      <div class="ansibleOptionAnchor" id="parameter-datastore"></div>
      <p style="display: inline;"><strong>destination_datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: datastore</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the destination datastore the virtual machine&#x27;s vmdk should be moved on.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_datastore_cluster"></div>
      <p style="display: inline;"><strong>destination_datastore_cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_datastore_cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.5.0</i></p>
    </td>
    <td valign="top">
      <p>Name of the destination datastore cluster (storage pod) the virtual machine&#x27;s vmdk should be moved on.</p>
      <p>Only works if drs is enabled for the cluster the vm is running / should run.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_host"></div>
      <div class="ansibleOptionAnchor" id="parameter-destination"></div>
      <p style="display: inline;"><strong>destination_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: destination</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the destination host the virtual machine should be running on.</p>
      <p>Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-destination_resourcepool"></div>
      <div class="ansibleOptionAnchor" id="parameter-resource_pool"></div>
      <p style="display: inline;"><strong>destination_resourcepool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destination_resourcepool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: resource_pool</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the destination resource pool where the virtual machine should be running.</p>
      <p>Resource pool is required if vmotion is done between hosts which are part of different clusters or datacenters.</p>
      <p>if not passed, resource_pool object will be retrived from host_obj parent.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-moid"></div>
      <p style="display: inline;"><strong>moid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-moid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.</p>
      <p>This is required if <code class='docutils literal notranslate'>vm_name</code> or <code class='docutils literal notranslate'>vm_uuid</code> is not supplied.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
      <p style="display: inline;"><strong>timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.4.0</i></p>
    </td>
    <td valign="top">
      <p>The timeout in seconds. When the timeout is reached, the module will fail.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">3600</code></p>
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
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vm_name"></div>
      <div class="ansibleOptionAnchor" id="parameter-vm"></div>
      <p style="display: inline;"><strong>vm_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: vm</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>Name of the VM to perform a vMotion on.</p>
      <p>This is required parameter, if <code class='docutils literal notranslate'>vm_uuid</code> is not set.</p>
      <p>Version 2.6 onwards, this parameter is not a required parameter, unlike the previous versions.</p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="parameter-vm_uuid"></div>
      <div class="ansibleOptionAnchor" id="parameter-uuid"></div>
      <p style="display: inline;"><strong>vm_uuid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_uuid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: uuid</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>UUID of the virtual machine to perform a vMotion operation on.</p>
      <p>This is a required parameter, if <code class='docutils literal notranslate'>vm_name</code> or <code class='docutils literal notranslate'>moid</code> is not set.</p>
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

    
    - name: Perform vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_host: 'destination_host_as_per_vcenter'
      delegate_to: localhost

    - name: Perform vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        moid: vm-42
        destination_host: 'destination_host_as_per_vcenter'
      delegate_to: localhost

    - name: Perform vMotion of virtual machine to resource_pool
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        moid: vm-42
        destination_host: 'destination_host_as_per_vcenter'
        destination_resourcepool: 'destination_resourcepool_as_per_vcenter'
      delegate_to: localhost

    - name: Perform storage vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_datastore: 'destination_datastore_as_per_vcenter'
      delegate_to: localhost

    - name: Perform storage vMotion and host vMotion of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_host: 'destination_host_as_per_vcenter'
        destination_datastore: 'destination_datastore_as_per_vcenter'
      delegate_to: localhost

    - name: Perform storage vMotion to a Storage Cluster and vMotion to a Cluster of virtual machine
      community.vmware.vmware_vmotion:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
        destination_cluster: 'destination_cluster_as_per_vcenter'
        destination_datastore_cluster: 'destination_datastore_cluster_as_per_vcenter'
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
      <div class="ansibleOptionAnchor" id="return-datastore"></div>
      <p style="display: inline;"><strong>datastore</strong></p>
      <a class="ansibleOptionLink" href="#return-datastore" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List the datastore the virtual machine is on.</p>
      <p>Only returned if there is asked for a Storage vMotion (Datastore or Datastore Cluster).</p>
      <p style="margin-top: 8px;"><b>Returned:</b> changed or success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>&#34;datastore1&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td valign="top">
      <div class="ansibleOptionAnchor" id="return-running_host"></div>
      <p style="display: inline;"><strong>running_host</strong></p>
      <a class="ansibleOptionLink" href="#return-running_host" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td valign="top">
      <p>List the host the virtual machine is registered to.</p>
      <p>Only returned if there is asked for a vMotion (Cluster or Host).</p>
      <p style="margin-top: 8px;"><b>Returned:</b> changed or success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>&#34;host1.example.com&#34;</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Bede Carroll (@bedecarroll)
- Olivier Boukili (@oboukili)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

