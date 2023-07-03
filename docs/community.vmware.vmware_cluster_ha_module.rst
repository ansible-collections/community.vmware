

community.vmware.vmware_cluster_ha module -- Manage High Availability (HA) on VMware vSphere clusters
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_cluster_ha`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Manages HA configuration on VMware vSphere clusters.
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
      A dictionary of advanced HA settings.


      Default: :literal:`{}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-apd_delay:

      **apd_delay**

      :literal:`integer`

      added in community.vmware 2.9.0


      .. raw:: html

        </div></div>

    - 
      The response recovery delay time in sec for storage failures categorized as All Paths Down (APD).

      Only set if \ :literal:`apd\_response`\  is \ :literal:`restartConservative`\  or \ :literal:`restartAggressive`\ .


      Default: :literal:`180`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-apd_reaction:

      **apd_reaction**

      :literal:`string`

      added in community.vmware 2.9.0


      .. raw:: html

        </div></div>

    - 
      VM response recovery reaction for storage failures categorized as All Paths Down (APD).

      Only set if \ :literal:`apd\_response`\  is \ :literal:`restartConservative`\  or \ :literal:`restartAggressive`\ .


      Choices:

      - :literal:`"reset"` ← (default)
      - :literal:`"none"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-apd_response:

      **apd_response**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      VM storage protection setting for storage failures categorized as All Paths Down (APD).


      Choices:

      - :literal:`"disabled"`
      - :literal:`"warning"` ← (default)
      - :literal:`"restartConservative"`
      - :literal:`"restartAggressive"`



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

      .. _parameter-enable:

      **enable**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to enable HA.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-failover_host_admission_control:

      **failover_host_admission_control**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Configure dedicated failover hosts.

      \ :literal:`slot\_based\_admission\_control`\ , \ :literal:`reservation\_based\_admission\_control`\  and \ :literal:`failover\_host\_admission\_control`\  are mutually exclusive.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-failover_host_admission_control/failover_hosts:

      **failover_hosts**

      :literal:`list` / :literal:`elements=string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      List of dedicated failover hosts.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ha_host_monitoring:

      **ha_host_monitoring**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Whether HA restarts virtual machines after a host fails.

      If set to \ :literal:`enabled`\ , HA restarts virtual machines after a host fails.

      If set to \ :literal:`disabled`\ , HA does not restart virtual machines after a host fails.

      If \ :literal:`enable`\  is set to \ :literal:`false`\ , then this value is ignored.


      Choices:

      - :literal:`"enabled"` ← (default)
      - :literal:`"disabled"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ha_restart_priority:

      **ha_restart_priority**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Priority HA gives to a virtual machine if sufficient capacity is not available to power on all failed virtual machines.

      Valid only if \ :emphasis:`ha\_vm\_monitoring`\  is set to either \ :literal:`vmAndAppMonitoring`\  or \ :literal:`vmMonitoringOnly`\ .

      If set to \ :literal:`disabled`\ , then HA is disabled for this virtual machine.

      If set to \ :literal:`high`\ , then virtual machine with this priority have a higher chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.

      If set to \ :literal:`medium`\ , then virtual machine with this priority have an intermediate chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.

      If set to \ :literal:`low`\ , then virtual machine with this priority have a lower chance of powering on after a failure, when there is insufficient capacity on hosts to meet all virtual machine needs.


      Choices:

      - :literal:`"disabled"`
      - :literal:`"high"`
      - :literal:`"low"`
      - :literal:`"medium"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ha_vm_failure_interval:

      **ha_vm_failure_interval**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of seconds after which virtual machine is declared as failed if no heartbeat has been received.

      This setting is only valid if \ :literal:`ha\_vm\_monitoring`\  is set to, either \ :literal:`vmAndAppMonitoring`\  or \ :literal:`vmMonitoringOnly`\ .

      Unit is seconds.


      Default: :literal:`30`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ha_vm_max_failure_window:

      **ha_vm_max_failure_window**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of seconds for the window during which up to \ :literal:`ha\_vm\_max\_failures`\  resets can occur before automated responses stop.

      Valid only when \ :emphasis:`ha\_vm\_monitoring`\  is set to either \ :literal:`vmAndAppMonitoring`\  or \ :literal:`vmMonitoringOnly`\ .

      Unit is seconds.

      Default specifies no failure window.


      Default: :literal:`-1`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ha_vm_max_failures:

      **ha_vm_max_failures**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Maximum number of failures and automated resets allowed during the time that \ :literal:`ha\_vm\_max\_failure\_window`\  specifies.

      Valid only when \ :emphasis:`ha\_vm\_monitoring`\  is set to either \ :literal:`vmAndAppMonitoring`\  or \ :literal:`vmMonitoringOnly`\ .


      Default: :literal:`3`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ha_vm_min_up_time:

      **ha_vm_min_up_time**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of seconds for the virtual machine's heartbeats to stabilize after the virtual machine has been powered on.

      Valid only when \ :emphasis:`ha\_vm\_monitoring`\  is set to either \ :literal:`vmAndAppMonitoring`\  or \ :literal:`vmMonitoringOnly`\ .

      Unit is seconds.


      Default: :literal:`120`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ha_vm_monitoring:

      **ha_vm_monitoring**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      State of virtual machine health monitoring service.

      If set to \ :literal:`vmAndAppMonitoring`\ , HA response to both virtual machine and application heartbeat failure.

      If set to \ :literal:`vmMonitoringDisabled`\ , virtual machine health monitoring is disabled.

      If set to \ :literal:`vmMonitoringOnly`\ , HA response to virtual machine heartbeat failure.

      If \ :literal:`enable`\  is set to \ :literal:`false`\ , then this value is ignored.


      Choices:

      - :literal:`"vmAndAppMonitoring"`
      - :literal:`"vmMonitoringOnly"`
      - :literal:`"vmMonitoringDisabled"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-host_isolation_response:

      **host_isolation_response**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Indicates whether or VMs should be powered off if a host determines that it is isolated from the rest of the compute resource.

      If set to \ :literal:`none`\ , do not power off VMs in the event of a host network isolation.

      If set to \ :literal:`powerOff`\ , power off VMs in the event of a host network isolation.

      If set to \ :literal:`shutdown`\ , shut down VMs guest operating system in the event of a host network isolation.


      Choices:

      - :literal:`"none"` ← (default)
      - :literal:`"powerOff"`
      - :literal:`"shutdown"`



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

      .. _parameter-pdl_response:

      **pdl_response**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      VM storage protection setting for storage failures categorized as Permenant Device Loss (PDL).


      Choices:

      - :literal:`"disabled"`
      - :literal:`"warning"` ← (default)
      - :literal:`"restartAggressive"`



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

      .. _parameter-reservation_based_admission_control:

      **reservation_based_admission_control**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Configure reservation based admission control policy.

      \ :literal:`slot\_based\_admission\_control`\ , \ :literal:`reservation\_based\_admission\_control`\  and \ :literal:`failover\_host\_admission\_control`\  are mutually exclusive.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-reservation_based_admission_control/auto_compute_percentages:

      **auto_compute_percentages**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      By default, \ :literal:`failover\_level`\  is used to calculate \ :literal:`cpu\_failover\_resources\_percent`\  and \ :literal:`memory\_failover\_resources\_percent`\ . If a user wants to override the percentage values, he has to set this field to false.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-reservation_based_admission_control/cpu_failover_resources_percent:

      **cpu_failover_resources_percent**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Percentage of CPU resources in the cluster to reserve for failover. Ignored if \ :literal:`auto\_compute\_percentages`\  is not set to false.


      Default: :literal:`50`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-reservation_based_admission_control/failover_level:

      **failover_level**

      :literal:`integer` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Number of host failures that should be tolerated.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-reservation_based_admission_control/memory_failover_resources_percent:

      **memory_failover_resources_percent**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Percentage of memory resources in the cluster to reserve for failover. Ignored if \ :literal:`auto\_compute\_percentages`\  is not set to false.


      Default: :literal:`50`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-slot_based_admission_control:

      **slot_based_admission_control**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Configure slot based admission control policy.

      \ :literal:`slot\_based\_admission\_control`\ , \ :literal:`reservation\_based\_admission\_control`\  and \ :literal:`failover\_host\_admission\_control`\  are mutually exclusive.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-slot_based_admission_control/failover_level:

      **failover_level**

      :literal:`integer` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Number of host failures that should be tolerated.




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

    
    - name: Enable HA without admission control
      community.vmware.vmware_cluster_ha:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        enable: true
      delegate_to: localhost

    - name: Enable HA and VM monitoring without admission control
      community.vmware.vmware_cluster_ha:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        datacenter_name: DC0
        cluster_name: "{{ cluster_name }}"
        enable: true
        ha_vm_monitoring: vmMonitoringOnly
      delegate_to: localhost

    - name: Enable HA with admission control reserving 50% of resources for HA
      community.vmware.vmware_cluster_ha:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        datacenter_name: datacenter
        cluster_name: cluster
        enable: true
        reservation_based_admission_control:
          auto_compute_percentages: false
          failover_level: 1
          cpu_failover_resources_percent: 50
          memory_failover_resources_percent: 50
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

