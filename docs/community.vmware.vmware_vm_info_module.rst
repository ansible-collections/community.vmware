

community.vmware.vmware_vm_info module -- Return basic info pertaining to a VMware machine guest
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vm_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Return basic information pertaining to a vSphere or ESXi virtual machine guest.
- Cluster name as fact is added in version 2.7.








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
      <div class="ansibleOptionAnchor" id="parameter-folder"></div>
      <p style="display: inline;"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Specify a folder location of VMs to gather information from.</p>
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
      <div class="ansibleOptionAnchor" id="parameter-show_allocated"></div>
      <p style="display: inline;"><strong>show_allocated</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_allocated" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 2.5.0</i></p>
    </td>
    <td>
      <p>Allocated storage in byte and memory in MB are shown if it set to True.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_attribute"></div>
      <p style="display: inline;"><strong>show_attribute</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_attribute" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Attributes related to VM guest shown in information only when this is set <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_cluster"></div>
      <p style="display: inline;"><strong>show_cluster</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_cluster" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td>
      <p>Tags virtual machine&#x27;s cluster is shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_datacenter"></div>
      <p style="display: inline;"><strong>show_datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td>
      <p>Tags virtual machine&#x27;s datacenter is shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_datastore"></div>
      <p style="display: inline;"><strong>show_datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td>
      <p>Tags virtual machine&#x27;s datastore is shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_esxi_hostname"></div>
      <p style="display: inline;"><strong>show_esxi_hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_esxi_hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td>
      <p>Tags virtual machine&#x27;s ESXi host is shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_folder"></div>
      <p style="display: inline;"><strong>show_folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_folder" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.7.0</i></p>
    </td>
    <td>
      <p>Show folders</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_mac_address"></div>
      <p style="display: inline;"><strong>show_mac_address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_mac_address" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td>
      <p>Tags virtual machine&#x27;s mac address is shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_net"></div>
      <p style="display: inline;"><strong>show_net</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_net" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td>
      <p>Tags virtual machine&#x27;s network is shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_resource_pool"></div>
      <p style="display: inline;"><strong>show_resource_pool</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_resource_pool" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in community.vmware 3.5.0</i></p>
    </td>
    <td>
      <p>Tags virtual machine&#x27;s resource pool is shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-show_tag"></div>
      <p style="display: inline;"><strong>show_tag</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_tag" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Tags related to virtual machine are shown if set to <code class='docutils literal notranslate'>true</code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
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
      <div class="ansibleOptionAnchor" id="parameter-vm_name"></div>
      <p style="display: inline;"><strong>vm_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>Name of the virtual machine to get related configurations information from.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-vm_type"></div>
      <p style="display: inline;"><strong>vm_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-vm_type" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>If set to <code class='docutils literal notranslate'>vm</code>, then information are gathered for virtual machines only.</p>
      <p>If set to <code class='docutils literal notranslate'>template</code>, then information are gathered for virtual machine templates only.</p>
      <p>If set to <code class='docutils literal notranslate'>all</code>, then information are gathered for all virtual machines and virtual machine templates.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>&#34;all&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;vm&#34;</code></p></li>
        <li><p><code>&#34;template&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>




Notes
-----

- Fact about \ :literal:`moid`\  added in VMware collection 1.4.0.
- Fact about \ :literal:`datastore\_url`\  is added in VMware collection 1.18.0.
- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Gather all registered virtual machines
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
      delegate_to: localhost
      register: vminfo

    - debug:
        var: vminfo.virtual_machines

    - name: Gather one specific VM
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_name: 'vm_name_as_per_vcenter'
      delegate_to: localhost
      register: vm_info

    - debug:
        var: vminfo.virtual_machines

    - name: Gather only registered virtual machine templates
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_type: template
      delegate_to: localhost
      register: template_info

    - debug:
        var: template_info.virtual_machines

    - name: Gather only registered virtual machines
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        vm_type: vm
      delegate_to: localhost
      register: vm_info

    - debug:
        var: vm_info.virtual_machines

    - name: Get UUID from given VM Name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
            folder: "/datacenter/vm/folder"
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.uuid }}"
          with_items:
            - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"

    - name: Get Tags from given VM Name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
            folder: "/datacenter/vm/folder"
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.tags }}"
          with_items:
            - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"

    - name: Gather all VMs from a specific folder
      community.vmware.vmware_vm_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        folder: "/Asia-Datacenter1/vm/prod"
      delegate_to: localhost
      register: vm_info

    - name: Get datastore_url from given VM name
      block:
        - name: Get virtual machine info
          community.vmware.vmware_vm_info:
            hostname: '{{ vcenter_hostname }}'
            username: '{{ vcenter_username }}'
            password: '{{ vcenter_password }}'
          delegate_to: localhost
          register: vm_info

        - debug:
            msg: "{{ item.datastore_url }}"
          with_items:
            - "{{ vm_info.virtual_machines | community.general.json_query(query) }}"
          vars:
            query: "[?guest_name=='DC0_H0_VM0']"





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
      <div class="ansibleOptionAnchor" id="return-virtual_machines"></div>
      <p style="display: inline;"><strong>virtual_machines</strong></p>
      <a class="ansibleOptionLink" href="#return-virtual_machines" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>
    </td>
    <td>
      <p>list of dictionary of virtual machines and their information</p>
      <p style="margin-top: 8px;"><b>Returned:</b> success</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>[{&#34;allocated&#34;: {&#34;cpu&#34;: 2, &#34;memory&#34;: 16, &#34;storage&#34;: 500000000}, &#34;attributes&#34;: {&#34;job&#34;: &#34;backup-prepare&#34;}, &#34;cluster&#34;: null, &#34;datacenter&#34;: &#34;Datacenter-1&#34;, &#34;datastore_url&#34;: [{&#34;name&#34;: &#34;t880-o2g&#34;, &#34;url&#34;: &#34;/vmfs/volumes/e074264a-e5c82a58&#34;}], &#34;esxi_hostname&#34;: &#34;10.76.33.226&#34;, &#34;folder&#34;: &#34;/Datacenter-1/vm&#34;, &#34;guest_fullname&#34;: &#34;Ubuntu Linux (64-bit)&#34;, &#34;guest_name&#34;: &#34;ubuntu_t&#34;, &#34;ip_address&#34;: &#34;&#34;, &#34;mac_address&#34;: [&#34;00:50:56:87:a5:9a&#34;], &#34;moid&#34;: &#34;vm-24&#34;, &#34;power_state&#34;: &#34;poweredOff&#34;, &#34;tags&#34;: [{&#34;category_id&#34;: &#34;urn:vmomi:InventoryServiceCategory:b316cc45-f1a9-4277-811d-56c7e7975203:GLOBAL&#34;, &#34;category_name&#34;: &#34;cat_0001&#34;, &#34;description&#34;: &#34;&#34;, &#34;id&#34;: &#34;urn:vmomi:InventoryServiceTag:43737ec0-b832-4abf-abb1-fd2448ce3b26:GLOBAL&#34;, &#34;name&#34;: &#34;tag_0001&#34;}], &#34;uuid&#34;: &#34;4207072c-edd8-3bd5-64dc-903fd3a0db04&#34;, &#34;vm_network&#34;: {&#34;00:50:56:87:a5:9a&#34;: {&#34;ipv4&#34;: [&#34;10.76.33.228&#34;], &#34;ipv6&#34;: []}}}]</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Fedor Vompe (@sumkincpp)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

