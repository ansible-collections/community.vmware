

community.vmware.vmware_content_deploy_ovf_template module -- Deploy Virtual Machine from ovf template stored in content library.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this module,
see `Requirements <ansible_collections.community.vmware.vmware_content_deploy_ovf_template_module_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_content_deploy_ovf_template`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Module to deploy virtual machine from ovf template in content library.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_content_deploy_ovf_template_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- vSphere Automation SDK






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
      <div class="ansibleOptionAnchor" id="parameter-cluster"></div>
      <p style="display: inline;"><strong>cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the cluster in datacenter in which to place deployed VM.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>Name of the datacenter, where VM to be deployed.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datastore"></div>
      <p style="display: inline;"><strong>datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the datastore to store deployed VM and disk.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datastore_cluster"></div>
      <p style="display: inline;"><strong>datastore_cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datastore_cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the datastore cluster housing a datastore to store deployed VM and disk.</p>
      <p>If datastore is not specified, the recommended datastore from this cluster will be used.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the folder in datacenter in which to place deployed VM.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;vm&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-host"></div>
      <p style="display: inline;"><strong>host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the ESX Host in datacenter in which to place deployed VM. The host has to be a member of the cluster that contains the resource pool.</p>
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
      <p>The hostname or IP address of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-library"></div>
      <div class="ansibleOptionAnchor" id="parameter-content_library"></div>
      <div class="ansibleOptionAnchor" id="parameter-content_library_src"></div>
      <p style="display: inline;"><strong>library</strong></p>
      <a class="ansibleOptionLink" href="#parameter-library" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: content_library, content_library_src</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The name of the content library from where the template resides.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-log_level"></div>
      <p style="display: inline;"><strong>log_level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-log_level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The level of logging desired in this module.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;debug&#34;</code></p></li>
        <li><p><code>&#34;info&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;normal&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <div class="ansibleOptionAnchor" id="parameter-vm_name"></div>
      <p style="display: inline;"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: vm_name</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The name of the VM to be deployed.</p>
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
      <p>The password of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
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
      <p>The port number of the vSphere vCenter.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-protocol"></div>
      <p style="display: inline;"><strong>protocol</strong></p>
      <a class="ansibleOptionLink" href="#parameter-protocol" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The connection to protocol.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;http&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;https&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

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
      <div class="ansibleOptionAnchor" id="parameter-resource_pool"></div>
      <p style="display: inline;"><strong>resource_pool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_pool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the resourcepool in datacenter in which to place deployed VM.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-storage_provisioning"></div>
      <p style="display: inline;"><strong>storage_provisioning</strong></p>
      <a class="ansibleOptionLink" href="#parameter-storage_provisioning" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Default storage provisioning type to use for all sections of type vmw:StorageSection in the OVF descriptor.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;thin&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;thick&#34;</code></p></li>
        <li><p><code>&#34;eagerZeroedThick&#34;</code></p></li>
        <li><p><code>&#34;eagerzeroedthick&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-template"></div>
      <div class="ansibleOptionAnchor" id="parameter-ovf"></div>
      <div class="ansibleOptionAnchor" id="parameter-ovf_template"></div>
      <div class="ansibleOptionAnchor" id="parameter-template_src"></div>
      <p style="display: inline;"><strong>template</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: ovf, ovf_template, template_src</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The name of OVF template from which VM to be deployed.</p>
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
      <p>The username of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
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
      <p>Allows connection when SSL certificates are not valid.</p>
      <p>Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_VALIDATE_CERTS</code> will be used instead.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Deploy Virtual Machine from OVF template in content library
      community.vmware.vmware_content_deploy_ovf_template:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        ovf_template: rhel_test_template
        datastore: Shared_NFS_Volume
        folder: vm
        datacenter: Sample_DC_1
        name: Sample_VM
        resource_pool: test_rp
      delegate_to: localhost

    - name: Deploy Virtual Machine from OVF template in content library with eagerZeroedThick storage
      vmware_content_deploy_ovf_template:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        ovf_template: rhel_test_template
        datastore: Shared_NFS_Volume
        folder: vm
        datacenter: Sample_DC_1
        name: Sample_VM
        resource_pool: test_rp
        storage_provisioning: eagerZeroedThick
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
      <div class="ansibleOptionAnchor" id="return-vm_deploy_info"></div>
      <p style="display: inline;"><strong>vm_deploy_info</strong></p>
      <a class="ansibleOptionLink" href="#return-vm_deploy_info" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Virtual machine deployment message and vm_id</p>
      <p style="margin-top: 8px;"><b>Returned:</b> on success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;msg&#34;: &#34;Deployed Virtual Machine &#39;Sample_VM&#39;.&#34;, &#34;vm_id&#34;: &#34;vm-1009&#34;}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Lev Goncharv (@ultral)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

