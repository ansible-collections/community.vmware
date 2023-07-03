

community.vmware.vmware_host_sriov module -- Manage SR-IOV settings on host
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_sriov`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure, enable or disable SR-IOV functions on ESXi host.
- Module does not reboot the host after changes, but puts it in output "rebootRequired" state.
- User can specify an ESXi hostname or Cluster name. In case of cluster name, all ESXi hosts are updated.








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
      Name of the cluster from which all host systems will be used.

      This parameter is required if \ :literal:`esxi\_hostname`\  is not specified.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the host system to work with.

      This parameter is required if \ :literal:`cluster\_name`\  is not specified.

      User can specify specific host from the cluster.



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

      .. _parameter-num_virt_func:

      **num_virt_func**

      :literal:`integer` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      number of functions to activate on interface.

      0 means SR-IOV disabled.

      number greater than 0 means SR-IOV enabled.



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

      .. _parameter-sriov_on:

      **sriov_on**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      optional parameter, related to \ :literal:`num\_virt\_func`\ .

      SR-IOV can be enabled only if \ :literal:`num\_virt\_func`\  \> 0.


      Choices:

      - :literal:`false`
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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmnic:

      **vmnic**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Interface name, like vmnic0.





Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: enable SR-IOV on vmnic0 with 8 functions
      community.vmware.vmware_host_sriov:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi1 }}"
        vmnic: vmnic0
        sriov_on: true
        num_virt_func: 8

    - name: enable SR-IOV on already enabled interface vmnic0
      community.vmware.vmware_host_sriov:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi1 }}"
        vmnic: vmnic0
        sriov_on: true
        num_virt_func: 8

    - name: enable SR-IOV on vmnic0 with big number of functions
      community.vmware.vmware_host_sriov:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi1 }}"
        vmnic: vmnic0
        sriov_on: true
        num_virt_func: 100
      ignore_errors: true

    - name: disable SR-IOV on vmnic0
      community.vmware.vmware_host_sriov:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi1 }}"
        vmnic: vmnic0
        sriov_on: false
        num_virt_func: 0





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

      .. _return-host_sriov_diff:

      **host_sriov_diff**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      contains info about SR-IOV status on vmnic before, after and requested changes

      sometimes vCenter slowly update info, as result "after" contains same info as "before" need to run again in check\_mode or reboot host, as ESXi requested


      Returned: always

      Sample: :literal:`{"changed": true, "diff": {"after": {"host\_test": {"maxVirtualFunctionSupported": 63, "numVirtualFunction": 0, "numVirtualFunctionRequested": 8, "rebootRequired": true, "sriovActive": false, "sriovCapable": true, "sriovEnabled": true}}, "before": {"host\_test": {"maxVirtualFunctionSupported": 63, "numVirtualFunction": 0, "numVirtualFunctionRequested": 0, "rebootRequired": false, "sriovActive": false, "sriovCapable": true, "sriovEnabled": false}}, "changes": {"host\_test": {"numVirtualFunction": 8, "rebootRequired": true, "sriovEnabled": true}}}}`




Authors
~~~~~~~

- Viktor Tsymbalyuk (@victron)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

