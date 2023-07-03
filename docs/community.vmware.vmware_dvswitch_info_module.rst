

community.vmware.vmware_dvswitch_info module -- Gathers info dvswitch configurations
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_dvswitch_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about dvswitch configurations.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specify a folder location of dvswitch to gather information from.

      Examples:

         folder: /datacenter1/network

         folder: datacenter1/network

         folder: /datacenter1/network/folder1

         folder: datacenter1/network/folder1

         folder: /folder1/datacenter1/network

         folder: folder1/datacenter1/network

         folder: /folder1/datacenter1/network/folder2



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

            "summary.name",

            "summary.numPorts",

            "config.maxMtu",

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

      .. _parameter-dvswitch:
      .. _parameter-switch:
      .. _parameter-switch_name:

      **switch_name**

      aliases: switch, dvswitch

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of a dvswitch to look for.

      If \ :literal:`switch\_name`\  not specified gather all dvswitch information.



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

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Gather all registered dvswitch
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
      delegate_to: localhost
      register: dvswitch_info

    - name: Gather info about specific dvswitch
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        switch_name: DVSwitch01
      delegate_to: localhost
      register: dvswitch_info

    - name: Gather info from folder about specific dvswitch
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        folder: /datacenter1/network/F01
        switch_name: DVSwitch02
      delegate_to: localhost
      register: dvswitch_info

    - name: Gather some info from a dvswitch using the vSphere API output schema
      community.vmware.vmware_dvswitch_info:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        schema: vsphere
        properties:
          - summary.name
          - summary.numPorts
          - config.maxMtu
          - overallStatus
        switch_name: DVSwitch01
      register: dvswitch_info





Return Values
-------------
The following are the fields unique to this module:

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-distributed_virtual_switches:

      **distributed_virtual_switches**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      list of dictionary of dvswitch and their information


      Returned: always

      Sample: :literal:`[{"configure": {"folder": "network", "hosts": ["esxi-test-02.local", "esxi-test-01.local"], "settings": {"healthCheck": {"TeamingHealthCheckConfig": false, "VlanMtuHealthCheckConfig": false}, "netflow": {"activeFlowTimeout": 60, "collectorIpAddress": "", "collectorPort": 0, "idleFlowTimeout": 15, "internalFlowsOnly": false, "observationDomainId": 0, "samplingRate": 0, "switchIpAddress": null}, "privateVlan": [], "properties": {"administratorContact": {"contact": null, "name": null}, "advanced": {"maxMtu": 1500, "multicastFilteringMode": "legacyFiltering"}, "discoveryProtocol": {"operation": "listen", "protocol": "cdp"}, "general": {"ioControl": true, "name": "DVSwitch01", "numPorts": 10, "numUplinks": 1, "vendor": "VMware, Inc.", "version": "6.6.0"}}}}, "uuid": "50 30 99 9c a7 60 8a 4f-05 9f e7 b5 da df 8f 17"}]`




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

