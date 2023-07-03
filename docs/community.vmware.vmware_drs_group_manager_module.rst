

community.vmware.vmware_drs_group_manager module -- Manage VMs and Hosts in DRS group.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_drs_group_manager`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- The module can be used to add VMs / Hosts to or remove them from a DRS group.








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
      .. _parameter-cluster_name:

      **cluster**

      aliases: cluster_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Cluster to which DRS group associated with.



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
      Name of the datacenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-group_name:

      **group_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the group to manage.



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

      .. _parameter-hosts:

      **hosts**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      A List of hosts to add / remove in the group.

      Required only if \ :emphasis:`vms`\  is not set.



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

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`present`\ , VMs/hosts will be added to the given DRS group.

      If set to \ :literal:`absent`\ , VMs/hosts will be removed from the given DRS group.


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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vms:

      **vms**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      A List of vms to add / remove in the group.

      Required only if \ :emphasis:`hosts`\  is not set.





Notes
-----

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    ---
    - name: Add VMs in an existing DRS VM group
      delegate_to: localhost
      community.vmware.vmware_drs_group_manager:
        hostname: "{{ vcenter_hostname }}"
        password: "{{ vcenter_password }}"
        username: "{{ vcenter_username }}"
        cluster: DC0_C0
        datacenter: DC0
        group_name: TEST_VM_01
        vms:
          - DC0_C0_RP0_VM0
          - DC0_C0_RP0_VM1
        state: present

    - name: Add Hosts in an existing DRS Host group
      delegate_to: localhost
      community.vmware.vmware_drs_group_manager:
        hostname: "{{ vcenter_hostname }}"
        password: "{{ vcenter_password }}"
        username: "{{ vcenter_username }}"
        cluster: DC0_C0
        datacenter: DC0
        group_name: TEST_HOST_01
        hosts:
          - DC0_C0_H0
          - DC0_C0_H1
          - DC0_C0_H2
        state: present

    - name: Remove VM from an existing DRS VM group
      delegate_to: localhost
      community.vmware.vmware_drs_group_manager:
        hostname: "{{ vcenter_hostname }}"
        password: "{{ vcenter_password }}"
        username: "{{ vcenter_username }}"
        cluster: DC0_C0
        datacenter: DC0
        group_name: TEST_VM_01
        vms:
          - DC0_C0_RP0_VM0
        state: absent

    - name: Remove host from an existing DRS Host group
      delegate_to: localhost
      community.vmware.vmware_drs_group_manager:
        hostname: "{{ vcenter_hostname }}"
        password: "{{ vcenter_password }}"
        username: "{{ vcenter_username }}"
        cluster: DC0_C0
        datacenter: DC0
        group_name: TEST_HOST_01
        hosts:
          - DC0_C0_H0
        state: absent






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

      .. _return-drs_group_member_info:

      **drs_group_member_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      Metadata about DRS group


      Returned: always

      Sample: :literal:`{"Asia-Cluster1": [{"group\_name": "vm\_group\_002", "type": "vm", "vms": ["dev-1"]}]}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-msg:

      **msg**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      Info message


      Returned: always

      Sample: :literal:`"Updated host group TEST\_HOST\_01 successfully"`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

