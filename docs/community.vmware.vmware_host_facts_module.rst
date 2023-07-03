

community.vmware.vmware_host_facts module -- Gathers facts about remote ESXi hostsystem
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_facts`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gathers facts like CPU, memory, datastore, network and system etc. about ESXi host system.
- Please specify hostname or IP address of ESXi host system as \ :literal:`hostname`\ .
- If hostname or IP address of vCenter is provided as \ :literal:`hostname`\  and \ :literal:`esxi\_hostname`\  is not specified, then the module will throw an error.
- VSAN facts added in 2.7 version.
- SYSTEM fact uuid added in 2.10 version.
- Connection state fact added in VMware collection 2.6.0.
- Please note that when ESXi host connection state is not \ :literal:`connected`\ , facts returned from vCenter might be stale. Users are recommended to check connection state value and take appropriate decision in the playbook.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      ESXi hostname.

      Host facts about the specified ESXi server will be returned.

      By specifying this option, you can select which ESXi hostsystem is returned if connecting to a vCenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hostname:

      **hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The hostname or IP address of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_HOST`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-pass:
      .. _parameter-password:
      .. _parameter-pwd:

      **password**

      aliases: pass, pwd

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The password of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PASSWORD`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port:

      **port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The port number of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PORT`\  will be used instead.

      Environment variable support added in Ansible 2.6.


      Default: :literal:`443`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-properties:

      **properties**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      Specify the properties to retrieve.

      If not specified, all properties are retrieved (deeply).

      Results are returned in a structure identical to the vsphere API.

      Example:

         properties: [

            "hardware.memorySize",

            "hardware.cpuInfo.numCpuCores",

            "config.product.apiVersion",

            "overallStatus"

         ]

      Only valid when \ :literal:`schema`\  is \ :literal:`vsphere`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_host:

      **proxy_host**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Address of a proxy that will receive all HTTPS requests and relay them.

      The format is a hostname or a IP.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PROXY\_HOST`\  will be used instead.

      This feature depends on a version of pyvmomi greater than v6.7.1.2018.12



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_port:

      **proxy_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Port of the HTTP proxy that will receive all HTTPS requests and relay them.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PROXY\_PORT`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-schema:

      **schema**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specify the output schema desired.

      The 'summary' output schema is the legacy output from the module

      The 'vsphere' output schema is the vSphere API class definition which requires pyvmomi\>6.7.1


      Choices:

      - :literal:`"summary"` ← (default)
      - :literal:`"vsphere"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-show_tag:

      **show_tag**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Tags related to Host are shown if set to \ :literal:`true`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-admin:
      .. _parameter-user:
      .. _parameter-username:

      **username**

      aliases: admin, user

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The username of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_USER`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allows connection when SSL certificates are not valid. Set to \ :literal:`false`\  when certificates are not trusted.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_VALIDATE\_CERTS`\  will be used instead.

      Environment variable support added in Ansible 2.6.

      If set to \ :literal:`true`\ , please make sure Python \>= 2.7.9 is installed on the given machine.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)





Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Gather vmware host facts
      community.vmware.vmware_host_facts:
        hostname: "{{ esxi_server }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
      register: host_facts
      delegate_to: localhost

    - name: Gather vmware host facts from vCenter
      community.vmware.vmware_host_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
      register: host_facts
      delegate_to: localhost

    - name: Gather vmware host facts from vCenter with tag information
      community.vmware.vmware_host_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        show_tag: true
      register: host_facts_tag
      delegate_to: localhost

    - name: Get VSAN Cluster UUID from host facts
      community.vmware.vmware_host_facts:
        hostname: "{{ esxi_server }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
      register: host_facts
    - set_fact:
        cluster_uuid: "{{ host_facts['ansible_facts']['vsan_cluster_uuid'] }}"

    - name: Gather some info from a host using the vSphere API output schema
      community.vmware.vmware_host_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        schema: vsphere
        properties:
          - hardware.memorySize
          - hardware.cpuInfo.numCpuCores
          - config.product.apiVersion
          - overallStatus
      register: host_facts

    - name: Gather information about powerstate and connection state
      community.vmware.vmware_host_facts:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        schema: vsphere
        properties:
          - runtime.connectionState
          - runtime.powerState

    - name: How to retrieve Product, Version, Build, Update info for ESXi from vCenter
      block:
        - name: Gather product version info for ESXi from vCenter
          community.vmware.vmware_host_facts:
            hostname: "{{ vcenter_hostname }}"
            username: "{{ vcenter_username }}"
            password: "{{ vcenter_password }}"
            esxi_hostname: "{{ esxi_hostname }}"
            schema: vsphere
            properties:
              - config.product
              - config.option
          register: gather_host_facts_result

        - name: Extract update level info from option properties
          set_fact:
            update_level_info: "{{ item.value }}"
          loop: "{{ gather_host_facts_result.ansible_facts.config.option }}"
          when:
            - item.key == 'Misc.HostAgentUpdateLevel'

        - name: The output of Product, Version, Build, Update info for ESXi
          debug:
            msg:
              - "Product : {{ gather_host_facts_result.ansible_facts.config.product.name }}"
              - "Version : {{ gather_host_facts_result.ansible_facts.config.product.version }}"
              - "Build   : {{ gather_host_facts_result.ansible_facts.config.product.build }}"
              - "Update  : {{ update_level_info }}"







Authors
~~~~~~~

- Wei Gao (@woshihaoren)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

