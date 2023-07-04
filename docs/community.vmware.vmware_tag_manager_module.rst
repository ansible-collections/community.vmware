

community.vmware.vmware_tag_manager module -- Manage association of VMware tags with VMware objects
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this module,
see `Requirements <ansible_collections.community.vmware.vmware_tag_manager_module_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_tag_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to assign / remove VMware tags from the given VMware objects.
- Tag feature is introduced in vSphere 6 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.



.. _ansible_collections.community.vmware.vmware_tag_manager_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- vSphere Automation SDK






Parameters
----------

.. raw:: html

  <table style="width: 100%; height: 1px;">
  <thead>
  <tr>
    <th><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The hostname or IP address of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-moid"></div>
      <p style="display: inline;"><strong>moid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-moid" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Managed object ID for the given object.</p>
      <p>Required if <code class='docutils literal notranslate'>object_name</code> is not set.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-object_name"></div>
      <p style="display: inline;"><strong>object_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-object_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Name of the object to work with.</p>
      <p>For DistributedVirtualPortgroups the format should be "switch_name:portgroup_name"</p>
      <p>Required if <code class='docutils literal notranslate'>moid</code> is not set.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-object_type"></div>
      <p style="display: inline;"><strong>object_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-object_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>Type of object to work with.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;VirtualMachine&#34;</code></p></li>
        <li><p><code>&#34;Datacenter&#34;</code></p></li>
        <li><p><code>&#34;ClusterComputeResource&#34;</code></p></li>
        <li><p><code>&#34;HostSystem&#34;</code></p></li>
        <li><p><code>&#34;DistributedVirtualSwitch&#34;</code></p></li>
        <li><p><code>&#34;DistributedVirtualPortgroup&#34;</code></p></li>
        <li><p><code>&#34;Datastore&#34;</code></p></li>
        <li><p><code>&#34;DatastoreCluster&#34;</code></p></li>
        <li><p><code>&#34;ResourcePool&#34;</code></p></li>
        <li><p><code>&#34;Folder&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <div class="ansibleOptionAnchor" id="parameter-pass"></div>
      <div class="ansibleOptionAnchor" id="parameter-pwd"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: pass, pwd</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The password of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>The port number of the vSphere vCenter.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p style="margin-top: 8px;"><span style="color: blue; font-weight: 700;">Default:</span> <code style="color: blue;">443</code></p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-protocol"></div>
      <p style="display: inline;"><strong>protocol</strong></p>
      <a class="ansibleOptionLink" href="#parameter-protocol" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The connection to protocol.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;http&#34;</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">&#34;https&#34;</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>Address of a proxy that will receive all HTTPS requests and relay them.</p>
      <p>The format is a hostname or a IP.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_HOST</code> will be used instead.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </div></td>
    <td>
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>add</code> or <code class='docutils literal notranslate'>present</code> will add the tags to the existing tag list of the given object.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>remove</code> or <code class='docutils literal notranslate'>absent</code> will remove the tags from the existing tag list of the given object.</p>
      <p>If <code class='docutils literal notranslate'>state</code> is set to <code class='docutils literal notranslate'>set</code> will replace the tags of the given objects with the user defined list of tags.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>&#34;present&#34;</code></p></li>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">&#34;add&#34;</code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;remove&#34;</code></p></li>
        <li><p><code>&#34;set&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-tag_names"></div>
      <p style="display: inline;"><strong>tag_names</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tag_names" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=any</span>
        / <span style="color: red;">required</span>
      </p>
    </div></td>
    <td>
      <p>List of tag(s) to be managed.</p>
      <p>User can also specify category name by specifying colon separated value. For example, "category_name:tag_name".</p>
      <p>User can also specify tag and category as dict, when tag or category contains colon. See example for more information. Added in version 2.10.</p>
      <p>User can skip category name if you have unique tag names.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <div class="ansibleOptionAnchor" id="parameter-admin"></div>
      <div class="ansibleOptionAnchor" id="parameter-user"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: admin, user</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </div></td>
    <td>
      <p>The username of the vSphere vCenter server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
    </td>
  </tr>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </div></td>
    <td>
      <p>Allows connection when SSL certificates are not valid.</p>
      <p>Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_VALIDATE_CERTS</code> will be used instead.</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Choices:</span></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue; font-weight: 700;">true</code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    - name: Add tags to a virtual machine
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0002
          - Category_0001:Sample_Tag_0003
        object_name: Fedora_VM
        object_type: VirtualMachine
        state: add
      delegate_to: localhost

    - name: Specify tag and category as dict
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - tag: tag_0001
            category: cat_0001
          - tag: tag_0002
            category: cat_0002
        object_name: Fedora_VM
        object_type: VirtualMachine
        state: add
      delegate_to: localhost

    - name: Remove a tag from a virtual machine
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0002
        object_name: Fedora_VM
        object_type: VirtualMachine
        state: remove
      delegate_to: localhost

    - name: Add tags to a distributed virtual switch
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0003
        object_name: Switch_0001
        object_type: DistributedVirtualSwitch
        state: add
      delegate_to: localhost

    - name: Add tags to a distributed virtual portgroup
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Tag_0004
        object_name: Switch_0001:Portgroup_0001
        object_type: DistributedVirtualPortgroup
        state: add
      delegate_to: localhost


    - name: Get information about folders
      community.vmware.vmware_folder_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: 'Asia-Datacenter1'
      delegate_to: localhost
      register: r
    - name: Set Managed object ID for the given folder
      ansible.builtin.set_fact:
        folder_mo_id: "{{ (r.flat_folder_info | selectattr('path', 'equalto', '/Asia-Datacenter1/vm/tier1/tier2') | map(attribute='moid'))[0] }}"
    - name: Add tags to a Folder using managed object id
      community.vmware.vmware_tag_manager:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        tag_names:
          - Sample_Cat_0004:Sample_Tag_0004
        object_type: Folder
        moid: "{{ folder_mo_id }}"
        state: add
      delegate_to: localhost






Return Values
-------------
The following are the fields unique to this module:

.. raw:: html

  <table style="width: 100%; height: 1px;">
  <thead>
  <tr>
    <th><p>Key</p></th>
    <th><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr style="height: 100%;">
    <td style="height: inherit; display: flex; flex-direction: row;"><div style="padding: 8px 16px; border-top: 1px solid #000000; height: inherit; flex: 1 0 auto; white-space: nowrap; max-width: 100%;">
      <div class="ansibleOptionAnchor" id="return-tag_status"></div>
      <p style="display: inline;"><strong>tag_status</strong></p>
      <a class="ansibleOptionLink" href="#return-tag_status" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </div></td>
    <td>
      <p>metadata about tags related to object configuration</p>
      <p style="margin-top: 8px;"><span style="font-weight: 700;">Returned:</span> on success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><span style="color: black; font-weight: 700;">Sample:</span> <code>{&#34;attached_tags&#34;: [&#34;urn:vmomi:InventoryServiceCategory:76f69e84-f6b9-4e64-954c-fac545d2c0ba:GLOBAL:security&#34;], &#34;current_tags&#34;: [&#34;urn:vmomi:InventoryServiceCategory:927f5ff8-62e6-4364-bc94-23e3bfd7dee7:GLOBAL:backup&#34;, &#34;urn:vmomi:InventoryServiceCategory:76f69e84-f6b9-4e64-954c-fac545d2c0ba:GLOBAL:security&#34;], &#34;detached_tags&#34;: [], &#34;previous_tags&#34;: [&#34;urn:vmomi:InventoryServiceCategory:927f5ff8-62e6-4364-bc94-23e3bfd7dee7:GLOBAL:backup&#34;]}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Frederic Van Reet (@GBrawl)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

