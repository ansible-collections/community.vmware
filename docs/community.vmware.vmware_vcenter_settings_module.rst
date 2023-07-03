

community.vmware.vmware_vcenter_settings module -- Configures general settings on a vCenter server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vcenter_settings`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure the vCenter server general settings (except the statistics).
- The statistics can be configured with the module \ :literal:`vmware\_vcenter\_statistics`\ .








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
      A dictionary of advanced settings.


      Default: :literal:`{}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-database:

      **database**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The database settings for vCenter server.


      Default: :literal:`{"event\_cleanup": true, "event\_retention": 30, "max\_connections": 50, "task\_cleanup": true, "task\_retention": 30}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-database/event_cleanup:

      **event_cleanup**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Event cleanup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-database/event_retention:

      **event_retention**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Event retention in days.


      Default: :literal:`30`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-database/max_connections:

      **max_connections**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Maximum connections.


      Default: :literal:`50`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-database/task_cleanup:

      **task_cleanup**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Task cleanup.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-database/task_retention:

      **task_retention**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Task retention in days.


      Default: :literal:`30`



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

      .. _parameter-logging_options:

      **logging_options**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The level of detail that vCenter server usesfor log files.


      Choices:

      - :literal:`"none"`
      - :literal:`"error"`
      - :literal:`"warning"`
      - :literal:`"info"` ← (default)
      - :literal:`"verbose"`
      - :literal:`"trivia"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mail:

      **mail**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The settings vCenter server uses to send email alerts.


      Default: :literal:`{"sender": "", "server": ""}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mail/sender:

      **sender**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Mail sender address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mail/server:

      **server**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Mail server.




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

      .. _parameter-runtime_settings:

      **runtime_settings**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The unique runtime settings for vCenter server.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-runtime_settings/managed_address:

      **managed_address**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      vCenter server managed address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-runtime_settings/unique_id:

      **unique_id**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      vCenter server unique ID.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-runtime_settings/vcenter_server_name:

      **vcenter_server_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      vCenter server name. Default is FQDN.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers:

      **snmp_receivers**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      SNMP trap destinations for vCenter server alerts.


      Default: :literal:`{"snmp\_receiver\_1\_community": "public", "snmp\_receiver\_1\_enabled": true, "snmp\_receiver\_1\_port": 162, "snmp\_receiver\_1\_url": "localhost", "snmp\_receiver\_2\_community": "", "snmp\_receiver\_2\_enabled": false, "snmp\_receiver\_2\_port": 162, "snmp\_receiver\_2\_url": "", "snmp\_receiver\_3\_community": "", "snmp\_receiver\_3\_enabled": false, "snmp\_receiver\_3\_port": 162, "snmp\_receiver\_3\_url": "", "snmp\_receiver\_4\_community": "", "snmp\_receiver\_4\_enabled": false, "snmp\_receiver\_4\_port": 162, "snmp\_receiver\_4\_url": ""}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_1_community:

      **snmp_receiver_1_community**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Community string.


      Default: :literal:`"public"`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_1_enabled:

      **snmp_receiver_1_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable receiver.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_1_port:

      **snmp_receiver_1_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Receiver port.


      Default: :literal:`162`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_1_url:

      **snmp_receiver_1_url**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Primary Receiver ULR.


      Default: :literal:`"localhost"`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_2_community:

      **snmp_receiver_2_community**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Community string.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_2_enabled:

      **snmp_receiver_2_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable receiver.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_2_port:

      **snmp_receiver_2_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Receiver port.


      Default: :literal:`162`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_2_url:

      **snmp_receiver_2_url**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Receiver 2 ULR.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_3_community:

      **snmp_receiver_3_community**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Community string.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_3_enabled:

      **snmp_receiver_3_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable receiver.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_3_port:

      **snmp_receiver_3_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Receiver port.


      Default: :literal:`162`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_3_url:

      **snmp_receiver_3_url**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Receiver 3 ULR.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_4_community:

      **snmp_receiver_4_community**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Community string.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_4_enabled:

      **snmp_receiver_4_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable receiver.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_4_port:

      **snmp_receiver_4_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Receiver port.


      Default: :literal:`162`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-snmp_receivers/snmp_receiver_4_url:

      **snmp_receiver_4_url**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Receiver 4 ULR.


      Default: :literal:`""`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-timeout_settings:

      **timeout_settings**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The vCenter server connection timeout for normal and long operations.


      Default: :literal:`{"long\_operations": 120, "normal\_operations": 30}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-timeout_settings/long_operations:

      **long_operations**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Long operation timeout.


      Default: :literal:`120`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-timeout_settings/normal_operations:

      **normal_operations**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Normal operation timeout.


      Default: :literal:`30`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-user_directory:

      **user_directory**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The user directory settings for the vCenter server installation.


      Default: :literal:`{"query\_limit": true, "query\_limit\_size": 5000, "timeout": 60, "validation": true, "validation\_period": 1440}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-user_directory/query_limit:

      **query_limit**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Query limit.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-user_directory/query_limit_size:

      **query_limit_size**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Query limit size.


      Default: :literal:`5000`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-user_directory/timeout:

      **timeout**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      User directory timeout.


      Default: :literal:`60`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-user_directory/validation:

      **validation**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Mail Validation.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-user_directory/validation_period:

      **validation_period**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Validation period.


      Default: :literal:`1440`



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

    
    - name: Configure vCenter general settings
      community.vmware.vmware_vcenter_settings:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        database:
          max_connections: 50
          task_cleanup: true
          task_retention: 30
          event_cleanup: true
          event_retention: 30
        runtime_settings:
          unique_id: 1
          managed_address: "{{ lookup('dig', inventory_hostname) }}"
          vcenter_server_name: "{{ inventory_hostname }}"
        user_directory:
          timeout: 60
          query_limit: true
          query_limit_size: 5000
          validation: true
          validation_period: 1440
        mail:
          server: mail.example.com
          sender: vcenter@{{ inventory_hostname }}
        snmp_receivers:
          snmp_receiver_1_url: localhost
          snmp_receiver_1_enabled: true
          snmp_receiver_1_port: 162
          snmp_receiver_1_community: public
        timeout_settings:
          normal_operations: 30
          long_operations: 120
        logging_options: info
      delegate_to: localhost

    - name: Enable Retreat Mode for cluster with MOID domain-c8 (https://kb.vmware.com/kb/80472)
      community.vmware.vmware_vcenter_settings:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        advanced_settings:
          'config.vcls.clusters.domain-c8.enabled': 'false'
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

      .. _return-results:

      **results**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about vCenter settings

      supported diff mode from version 1.8.0


      Returned: always

      Sample: :literal:`{"changed": false, "db\_event\_cleanup": true, "db\_event\_retention": 30, "db\_max\_connections": 50, "db\_task\_cleanup": true, "db\_task\_retention": 30, "diff": {"after": {"db\_event\_cleanup": true, "db\_event\_retention": 30, "db\_max\_connections": 50, "db\_task\_cleanup": true, "db\_task\_retention": 30, "directory\_query\_limit": true, "directory\_query\_limit\_size": 5000, "directory\_timeout": 60, "directory\_validation": true, "directory\_validation\_period": 1440, "logging\_options": "info", "mail\_sender": "vcenter@vcenter01.example.com", "mail\_server": "mail.example.com", "runtime\_managed\_address": "192.168.1.10", "runtime\_server\_name": "vcenter01.example.com", "runtime\_unique\_id": 1, "snmp\_receiver\_1\_community": "public", "snmp\_receiver\_1\_enabled": true, "snmp\_receiver\_1\_port": 162, "snmp\_receiver\_1\_url": "localhost", "snmp\_receiver\_2\_community": "", "snmp\_receiver\_2\_enabled": false, "snmp\_receiver\_2\_port": 162, "snmp\_receiver\_2\_url": "", "snmp\_receiver\_3\_community": "", "snmp\_receiver\_3\_enabled": false, "snmp\_receiver\_3\_port": 162, "snmp\_receiver\_3\_url": "", "snmp\_receiver\_4\_community": "", "snmp\_receiver\_4\_enabled": false, "snmp\_receiver\_4\_port": 162, "snmp\_receiver\_4\_url": "", "timeout\_long\_operations": 120, "timeout\_normal\_operations": 30}, "before": {"db\_event\_cleanup": true, "db\_event\_retention": 30, "db\_max\_connections": 50, "db\_task\_cleanup": true, "db\_task\_retention": 30, "directory\_query\_limit": true, "directory\_query\_limit\_size": 5000, "directory\_timeout": 60, "directory\_validation": true, "directory\_validation\_period": 1440, "logging\_options": "info", "mail\_sender": "vcenter@vcenter01.example.com", "mail\_server": "mail.example.com", "runtime\_managed\_address": "192.168.1.10", "runtime\_server\_name": "vcenter01.example.com", "runtime\_unique\_id": 1, "snmp\_receiver\_1\_community": "public", "snmp\_receiver\_1\_enabled": true, "snmp\_receiver\_1\_port": 162, "snmp\_receiver\_1\_url": "localhost", "snmp\_receiver\_2\_community": "", "snmp\_receiver\_2\_enabled": false, "snmp\_receiver\_2\_port": 162, "snmp\_receiver\_2\_url": "", "snmp\_receiver\_3\_community": "", "snmp\_receiver\_3\_enabled": false, "snmp\_receiver\_3\_port": 162, "snmp\_receiver\_3\_url": "", "snmp\_receiver\_4\_community": "", "snmp\_receiver\_4\_enabled": false, "snmp\_receiver\_4\_port": 162, "snmp\_receiver\_4\_url": "", "timeout\_long\_operations": 120, "timeout\_normal\_operations": 30}}, "directory\_query\_limit": true, "directory\_query\_limit\_size": 5000, "directory\_timeout": 60, "directory\_validation": true, "directory\_validation\_period": 1440, "logging\_options": "info", "mail\_sender": "vcenter@vcenter01.example.com", "mail\_server": "mail.example.com", "msg": "vCenter settings already configured properly", "runtime\_managed\_address": "192.168.1.10", "runtime\_server\_name": "vcenter01.example.com", "runtime\_unique\_id": 1, "timeout\_long\_operations": 120, "timeout\_normal\_operations": 30}`




Authors
~~~~~~~

- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

