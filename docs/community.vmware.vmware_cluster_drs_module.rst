

community.vmware.vmware_cluster_drs module -- Manage Distributed Resource Scheduler (DRS) on VMware vSphere clusters
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_cluster_drs`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Manages DRS on VMware vSphere clusters.
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

      .. _parameter-advanced_settings:

      **advanced_settings**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      A dictionary of advanced DRS settings.


      Default: :literal:`{}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cluster_name:

      **cluster_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the cluster to be managed.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:
      .. _parameter-datacenter_name:

      **datacenter**

      aliases: datacenter_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the datacenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-drs_default_vm_behavior:

      **drs_default_vm_behavior**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Specifies the cluster-wide default DRS behavior for virtual machines.

      If set to \ :literal:`partiallyAutomated`\ , vCenter generates recommendations for virtual machine migration and for the placement with a host, then automatically implements placement recommendations at power on.

      If set to \ :literal:`manual`\ , then vCenter generates recommendations for virtual machine migration and for the placement with a host, but does not implement the recommendations automatically.

      If set to \ :literal:`fullyAutomated`\ , then vCenter automates both the migration of virtual machines and their placement with a host at power on.


      Choices:

      - :literal:`"fullyAutomated"` ← (default)
      - :literal:`"manual"`
      - :literal:`"partiallyAutomated"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-drs_enable_vm_behavior_overrides:

      **drs_enable_vm_behavior_overrides**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether DRS Behavior overrides for individual virtual machines are enabled.

      If set to \ :literal:`true`\ , overrides \ :literal:`drs\_default\_vm\_behavior`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-drs_vmotion_rate:

      **drs_vmotion_rate**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Threshold for generated ClusterRecommendations ranging from 1 (lowest) to 5 (highest).


      Choices:

      - :literal:`1`
      - :literal:`2`
      - :literal:`3` ← (default)
      - :literal:`4`
      - :literal:`5`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enable:

      **enable**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to enable DRS.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



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

      .. _parameter-predictive_drs:

      **predictive_drs**

      :literal:`boolean`

      added in community.vmware 3.3.0


      .. raw:: html

        </div></div>

    - 
      In addition to real-time metrics, DRS will respond to forecasted metrics provided by vRealize Operations Manager.

      You must also configure Predictive DRS in a version of vRealize Operations that supports this feature.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



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

    
    - name: Enable DRS
      community.vmware.vmware_cluster_drs:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        enable: true
      delegate_to: localhost
    - name: Enable DRS and distribute a more even number of virtual machines across hosts for availability
      community.vmware.vmware_cluster_drs:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        enable: true
        advanced_settings:
          'TryBalanceVmsPerHost': '1'
      delegate_to: localhost
    - name: Enable DRS and set default VM behavior to partially automated
      community.vmware.vmware_cluster_drs:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter_name: DC0
        cluster_name: "{{ cluster_name }}"
        enable: true
        drs_default_vm_behavior: partiallyAutomated
      delegate_to: localhost







Authors
~~~~~~~

- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

