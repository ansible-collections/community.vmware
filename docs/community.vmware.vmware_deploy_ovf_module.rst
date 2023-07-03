

community.vmware.vmware_deploy_ovf module -- Deploys a VMware virtual machine from an OVF or OVA file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_deploy_ovf`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to deploy a VMware VM from an OVF or OVA file








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-allow_duplicates:

      **allow_duplicates**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether or not to allow duplicate VM names. ESXi allows duplicates, vCenter may not.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster:

      **cluster**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Cluster to deploy to.

      This is a required parameter, if \ :literal:`esxi\_hostname`\  is not set and \ :literal:`hostname`\  is set to the vCenter server.

      \ :literal:`esxi\_hostname`\  and \ :literal:`cluster`\  are mutually exclusive parameters.

      This parameter is case sensitive.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Datacenter to deploy to.


      Default: :literal:`"ha-datacenter"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore:

      **datastore**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Datastore to deploy to.


      Default: :literal:`"datastore1"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-deployment_option:

      **deployment_option**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The key of the chosen deployment option.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-disk_provisioning:

      **disk_provisioning**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Disk provisioning type.


      Choices:

      - :literal:`"flat"`
      - :literal:`"eagerZeroedThick"`
      - :literal:`"monolithicSparse"`
      - :literal:`"twoGbMaxExtentSparse"`
      - :literal:`"twoGbMaxExtentFlat"`
      - :literal:`"thin"` ← (default)
      - :literal:`"sparse"`
      - :literal:`"thick"`
      - :literal:`"seSparse"`
      - :literal:`"monolithicFlat"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ESXi hostname where the virtual machine will run.

      This is a required parameter, if \ :literal:`cluster`\  is not set and \ :literal:`hostname`\  is set to the vCenter server.

      \ :literal:`esxi\_hostname`\  and \ :literal:`cluster`\  are mutually exclusive parameters.

      This parameter is case sensitive.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-fail_on_spec_warnings:

      **fail_on_spec_warnings**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Cause the module to treat OVF Import Spec warnings as errors.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-folder:

      **folder**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Absolute path of folder to place the virtual machine.

      If not specified, defaults to the value of \ :literal:`datacenter.vmFolder`\ .

      Examples:

         folder: /ha-datacenter/vm

         folder: ha-datacenter/vm

         folder: /datacenter1/vm

         folder: datacenter1/vm

         folder: /datacenter1/vm/folder1

         folder: datacenter1/vm/folder1

         folder: /folder1/datacenter1/vm

         folder: folder1/datacenter1/vm

         folder: /folder1/datacenter1/vm/folder2



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

      .. _parameter-inject_ovf_env:

      **inject_ovf_env**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Force the given properties to be inserted into an OVF Environment and injected through VMware Tools.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the VM to work with.

      Virtual machine names in vCenter are not necessarily unique, which may be problematic.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-networks:

      **networks**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      \ :literal:`key: value`\  mapping of OVF network name, to the vCenter network name.


      Default: :literal:`{"VM Network": "VM Network"}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ova:
      .. _parameter-ovf:

      **ovf**

      aliases: ova

      :literal:`path`

      .. raw:: html

        </div></div>

    - 
      Path to OVF or OVA file to deploy.



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

      .. _parameter-power_on:

      **power_on**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether or not to power on the virtual machine after creation.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-properties:

      **properties**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The assignment of values to the properties found in the OVF as key value pairs.



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

      .. _parameter-resource_pool:

      **resource_pool**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Resource Pool to deploy to.


      Default: :literal:`"Resources"`


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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait:

      **wait**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Wait for the host to power on.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-wait_for_ip_address:

      **wait_for_ip_address**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Wait until vCenter detects an IP address for the VM.

      This requires vmware-tools (vmtoolsd) to properly work after creation.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`





Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - community.vmware.vmware_deploy_ovf:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        ovf: /path/to/ubuntu-16.04-amd64.ovf
        wait_for_ip_address: true
      delegate_to: localhost

    # Deploys a new VM named 'NewVM' in specific datacenter/cluster, with network mapping taken from variable and using ova template from an absolute path
    - community.vmware.vmware_deploy_ovf:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: Datacenter1
        cluster: Cluster1
        datastore: vsandatastore
        name: NewVM
        networks: "{u'VM Network':u'{{ ProvisioningNetworkLabel }}'}"
        power_on: false
        ovf: /absolute/path/to/template/mytemplate.ova
      delegate_to: localhost

    - community.vmware.vmware_deploy_ovf:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: Datacenter1
        esxi_hostname: test-server
        datastore: test-datastore
        ovf: /path/to/ubuntu-16.04-amd64.ovf
      delegate_to: localhost





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

      .. _return-instance:

      **instance**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the new virtual machine


      Returned: always

      Sample: :literal:`"None"`




Authors
~~~~~~~

- Matt Martz (@sivel)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

