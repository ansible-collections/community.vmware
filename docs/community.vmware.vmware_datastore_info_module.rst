

community.vmware.vmware_datastore_info module -- Gather info about datastores available in given vCenter
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_datastore_info`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to gather information about datastores in VMWare infrastructure.
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

      .. _parameter-cluster:

      **cluster**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Cluster to search for datastores.

      If set, information of datastores belonging this clusters will be returned.

      This parameter is required, if \ :literal:`datacenter`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:
      .. _parameter-datacenter_name:

      **datacenter**

      aliases: datacenter_name

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Datacenter to search for datastores.

      This parameter is required, if \ :literal:`cluster`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-gather_nfs_mount_info:

      **gather_nfs_mount_info**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Gather mount information of NFS datastores.

      Disabled per default because this slows down the execution if you have a lot of datastores.

      Only valid when \ :literal:`schema`\  is \ :literal:`summary`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-gather_vmfs_mount_info:

      **gather_vmfs_mount_info**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Gather mount information of VMFS datastores.

      Disabled per default because this slows down the execution if you have a lot of datastores.

      Only valid when \ :literal:`schema`\  is \ :literal:`summary`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



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

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the datastore to match.

      If set, information of specific datastores are returned.



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

            "name",

            "info.vmfs.ssd",

            "capability.vsanSparseSupported",

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
      Tags related to Datastore are shown if set to \ :literal:`true`\ .


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

    
    - name: Gather info from standalone ESXi server having datacenter as 'ha-datacenter'
      community.vmware.vmware_datastore_info:
        hostname: '{{ esxi_hostname }}'
        username: '{{ esxi_username }}'
        password: '{{ esxi_password }}'
        datacenter_name: "ha-datacenter"
      delegate_to: localhost
      register: info

    - name: Gather info from datacenter about specific datastore
      community.vmware.vmware_datastore_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: '{{ datacenter_name }}'
        name: datastore1
      delegate_to: localhost
      register: info

    - name: Gather some info from a datastore using the vSphere API output schema
      community.vmware.vmware_datastore_info:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: '{{ datacenter_name }}'
        schema: vsphere
        properties:
          - name
          - info.vmfs.ssd
          - capability.vsanSparseSupported
          - overallStatus
      delegate_to: localhost
      register: info





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

      .. _return-datastores:

      **datastores**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      metadata about the available datastores


      Returned: always

      Sample: :literal:`[{"accessible": false, "capacity": 42681237504, "datastore\_cluster": "datacluster0", "freeSpace": 39638269952, "maintenanceMode": "normal", "multipleHostAccess": false, "name": "datastore2", "provisioned": 12289211488, "type": "VMFS", "uncommitted": 9246243936, "url": "ds:///vmfs/volumes/5a69b18a-c03cd88c-36ae-5254001249ce/", "vmfs\_blockSize": 1024, "vmfs\_uuid": "5a69b18a-c03cd88c-36ae-5254001249ce", "vmfs\_version": "6.81"}, {"accessible": true, "capacity": 5497558138880, "datastore\_cluster": "datacluster0", "freeSpace": 4279000641536, "maintenanceMode": "normal", "multipleHostAccess": true, "name": "datastore3", "nfs\_path": "/vol/datastore3", "nfs\_server": "nfs\_server1", "provisioned": 1708109410304, "type": "NFS", "uncommitted": 489551912960, "url": "ds:///vmfs/volumes/420b3e73-67070776/"}]`




Authors
~~~~~~~

- Tim Rightnour (@garbled1)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

