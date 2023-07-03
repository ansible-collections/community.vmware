

community.vmware.vmware_resource_pool module -- Add/remove resource pools to/from vCenter
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_resource_pool`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to add/remove a resource pool to/from vCenter








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
      Name of the cluster to configure the resource pool.

      This parameter is required if \ :literal:`esxi\_hostname`\  or \ :literal:`parent\_resource\_pool`\  is not specified.

      The \ :literal:`cluster`\ , \ :literal:`esxi\_hostname`\  and \ :literal:`parent\_resource\_pool`\  parameters are mutually exclusive.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cpu_allocation_shares:

      **cpu_allocation_shares**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of cpu shares allocated.

      This value is only set if \ :emphasis:`cpu\_shares`\  is set to \ :literal:`custom`\ .


      Default: :literal:`4000`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cpu_expandable_reservations:

      **cpu_expandable_reservations**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cpu_limit:

      **cpu_limit**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.

      The default value -1 indicates no limit.


      Default: :literal:`-1`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cpu_reservation:

      **cpu_reservation**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Amount of resource that is guaranteed available to the virtual machine or resource pool.


      Default: :literal:`0`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cpu_shares:

      **cpu_shares**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Memory shares are used in case of resource contention.


      Choices:

      - :literal:`"high"`
      - :literal:`"custom"`
      - :literal:`"low"`
      - :literal:`"normal"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the datacenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the host to configure the resource pool.

      The host must not be member of a cluster.

      This parameter is required if \ :literal:`cluster`\  or \ :literal:`parent\_resource\_pool`\  is not specified.

      The \ :literal:`cluster`\ , \ :literal:`esxi\_hostname`\  and \ :literal:`parent\_resource\_pool`\  parameters are mutually exclusive.



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

      .. _parameter-mem_allocation_shares:

      **mem_allocation_shares**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of memory shares allocated.

      This value is only set if \ :emphasis:`mem\_shares`\  is set to \ :literal:`custom`\ .


      Default: :literal:`163840`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mem_expandable_reservations:

      **mem_expandable_reservations**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      In a resource pool with an expandable reservation, the reservation on a resource pool can grow beyond the specified value.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mem_limit:

      **mem_limit**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The utilization of a virtual machine/resource pool will not exceed this limit, even if there are available resources.

      The default value -1 indicates no limit.


      Default: :literal:`-1`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mem_reservation:

      **mem_reservation**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Amount of resource that is guaranteed available to the virtual machine or resource pool.


      Default: :literal:`0`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mem_shares:

      **mem_shares**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Memory shares are used in case of resource contention.


      Choices:

      - :literal:`"high"`
      - :literal:`"custom"`
      - :literal:`"low"`
      - :literal:`"normal"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-parent_resource_pool:

      **parent_resource_pool**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the parent resource pool.

      This parameter is required if \ :literal:`cluster`\  or \ :literal:`esxi\_hostname`\  is not specified.

      The \ :literal:`cluster`\ , \ :literal:`esxi\_hostname`\  and \ :literal:`parent\_resource\_pool`\  parameters are mutually exclusive.



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

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Resource pool name to manage.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Add or remove the resource pool


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



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

    
    - name: Add resource pool to vCenter
      community.vmware.vmware_resource_pool:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter: '{{ datacenter_name }}'
        cluster: '{{ cluster_name }}'
        resource_pool: '{{ resource_pool_name }}'
        mem_shares: normal
        mem_limit: -1
        mem_reservation: 0
        mem_expandable_reservations: true
        cpu_shares: normal
        cpu_limit: -1
        cpu_reservation: 0
        cpu_expandable_reservations: true
        state: present
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
      metadata about the new resource pool


      Returned: always

      Sample: :literal:`"None"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-resource_pool_config:

      **resource_pool_config**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      config data about the resource pool, version added 1.4.0


      Returned: always

      Sample: :literal:`{"\_vimtype": "vim.ResourceConfigSpec", "changeVersion": null, "cpuAllocation": {"\_vimtype": "vim.ResourceAllocationInfo", "expandableReservation": true, "limit": -1, "overheadLimit": null, "reservation": 0, "shares": {"\_vimtype": "vim.SharesInfo", "level": "normal", "shares": 4000}}, "entity": "vim.ResourcePool:resgroup-1108", "lastModified": null, "memoryAllocation": {"\_vimtype": "vim.ResourceAllocationInfo", "expandableReservation": true, "limit": -1, "overheadLimit": null, "reservation": 0, "shares": {"\_vimtype": "vim.SharesInfo", "level": "high", "shares": 327680}}, "name": "test\_pr1", "scaleDescendantsShares": null}`




Authors
~~~~~~~

- Davis Phillips (@dav1x)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

