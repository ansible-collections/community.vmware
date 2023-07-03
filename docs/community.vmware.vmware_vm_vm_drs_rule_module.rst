

community.vmware.vmware_vm_vm_drs_rule module -- Configure VMware DRS Affinity rule for virtual machines in the given cluster
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_vm_vm_drs_rule`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure VMware DRS Affinity rule for virtual machines in the given cluster.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-affinity_rule:

      **affinity_rule**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , the DRS rule will be an Affinity rule.

      If set to \ :literal:`false`\ , the DRS rule will be an Anti-Affinity rule.

      Effective only if \ :literal:`state`\  is set to \ :literal:`present`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster_name:

      **cluster_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Desired cluster name where virtual machines are present for the DRS rule.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-drs_rule_name:

      **drs_rule_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the DRS rule to manage.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , the DRS rule will be enabled.

      Effective only if \ :literal:`state`\  is set to \ :literal:`present`\ .


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

      .. _parameter-mandatory:

      **mandatory**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`true`\ , the DRS rule will be mandatory.

      Effective only if \ :literal:`state`\  is set to \ :literal:`present`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



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
      If set to \ :literal:`present`\ , then the DRS rule is created if not present.

      If set to \ :literal:`present`\ , then the DRS rule is already present, it updates to the given configurations.

      If set to \ :literal:`absent`\ , then the DRS rule is deleted if present.


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
      List of virtual machines name for which DRS rule needs to be applied.

      Required if \ :literal:`state`\  is set to \ :literal:`present`\ .





Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create DRS Affinity Rule for VM-VM
      community.vmware.vmware_vm_vm_drs_rule:
        hostname: "{{ esxi_server }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        cluster_name: "{{ cluster_name }}"
        vms:
            - vm1
            - vm2
        drs_rule_name: vm1-vm2-affinity-rule-001
        enabled: true
        mandatory: true
        affinity_rule: true
      delegate_to: localhost

    - name: Create DRS Anti-Affinity Rule for VM-VM
      community.vmware.vmware_vm_vm_drs_rule:
        hostname: "{{ esxi_server }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        cluster_name: "{{ cluster_name }}"
        enabled: true
        vms:
            - vm1
            - vm2
        drs_rule_name: vm1-vm2-affinity-rule-001
        mandatory: true
        affinity_rule: false
      delegate_to: localhost

    - name: Delete DRS Affinity Rule for VM-VM
      community.vmware.vmware_vm_vm_drs_rule:
        hostname: "{{ esxi_server }}"
        username: "{{ esxi_username }}"
        password: "{{ esxi_password }}"
        cluster_name: "{{ cluster_name }}"
        drs_rule_name: vm1-vm2-affinity-rule-001
        state: absent
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

      .. _return-result:

      **result**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about DRS VM and VM rule


      Returned: when state is present

      Sample: :literal:`{"rule\_enabled": false, "rule\_key": 20, "rule\_mandatory": true, "rule\_name": "drs\_rule\_0014", "rule\_uuid": "525f3bc0-253f-825a-418e-2ec93bffc9ae", "rule\_vms": ["VM\_65", "VM\_146"]}`




Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

