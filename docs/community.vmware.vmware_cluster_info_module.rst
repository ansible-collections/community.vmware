

community.vmware.vmware_cluster_info module -- Gather info about clusters available in given vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_cluster_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about clusters in VMWare infrastructure.
- All values and VMware object names are case sensitive.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster_name:

      **cluster_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the cluster.

      If set, information of this cluster will be returned.

      This parameter is required, if \ :literal:`datacenter`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Datacenter to search for cluster/s.

      This parameter is required, if \ :literal:`cluster\_name`\  is not supplied.



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

      Example:

         properties: [

            "name",

            "configuration.dasConfig.enabled",

            "summary.totalCpu"

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

      The 'summary' output schema is the legacy output from the module.

      The 'vsphere' output schema is the vSphere API class definition which requires pyvmomi\>6.7.1.


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
      Tags related to cluster are shown if set to \ :literal:`true`\ .


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

    
    - name: Gather cluster info from given datacenter
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: ha-datacenter
      delegate_to: localhost
      register: cluster_info

    - name: Gather info from datacenter about specific cluster
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
      delegate_to: localhost
      register: cluster_info

    - name: Gather info from datacenter about specific cluster with tags
      community.vmware.vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
        show_tag: true
      delegate_to: localhost
      register: cluster_info

    - name: Gather some info from a cluster using the vSphere API output schema
      vmware_cluster_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        cluster_name: DC0_C0
        schema: vsphere
        properties:
          - name
          - configuration.dasConfig.enabled
          - summary.totalCpu
      delegate_to: localhost
      register: cluster_info





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

      .. _return-clusters:

      **clusters**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the available clusters

      datacenter added in the return values from version 1.6.0


      Returned: always

      Sample: :literal:`{"DC0\_C0": {"datacenter": "DC0", "drs\_default\_vm\_behavior": null, "drs\_enable\_vm\_behavior\_overrides": null, "drs\_vmotion\_rate": null, "enable\_ha": null, "enabled\_drs": true, "enabled\_vsan": false, "ha\_admission\_control\_enabled": null, "ha\_failover\_level": null, "ha\_host\_monitoring": null, "ha\_restart\_priority": null, "ha\_vm\_failure\_interval": null, "ha\_vm\_max\_failure\_window": null, "ha\_vm\_max\_failures": null, "ha\_vm\_min\_up\_time": null, "ha\_vm\_monitoring": null, "ha\_vm\_tools\_monitoring": null, "hosts": [{"folder": "/DC0/host/DC0\_C0", "name": "esxi01.vsphere.local"}, {"folder": "/DC0/host/DC0\_C0", "name": "esxi02.vsphere.local"}, {"folder": "/DC0/host/DC0\_C0", "name": "esxi03.vsphere.local"}, {"folder": "/DC0/host/DC0\_C0", "name": "esxi04.vsphere.local"}], "moid": "domain-c9", "resource\_summary": {"cpuCapacityMHz": 4224, "cpuUsedMHz": 87, "memCapacityMB": 6139, "memUsedMB": 1254, "pMemAvailableMB": 0, "pMemCapacityMB": 0, "storageCapacityMB": 33280, "storageUsedMB": 19953}, "tags": [{"category\_id": "urn:vmomi:InventoryServiceCategory:9fbf83de-7903-442e-8004-70fd3940297c:GLOBAL", "category\_name": "sample\_cluster\_cat\_0001", "description": "", "id": "urn:vmomi:InventoryServiceTag:93d680db-b3a6-4834-85ad-3e9516e8fee8:GLOBAL", "name": "sample\_cluster\_tag\_0001"}], "vsan\_auto\_claim\_storage": false}}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)
- Christian Neugum (@digifuchsi)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

