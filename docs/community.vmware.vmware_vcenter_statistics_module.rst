

community.vmware.vmware_vcenter_statistics module -- Configures statistics on a vCenter server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vcenter_statistics`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure the vCenter server statistics.
- The remaining settings can be configured with the module \ :literal:`vmware\_vcenter\_settings`\ .








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

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

      .. _parameter-interval_past_day:

      **interval_past_day**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Settings for vCenter server past day statistic collection.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_day/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Past day statistics collection enabled.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_day/interval_minutes:

      **interval_minutes**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Interval duration in minutes.


      Choices:

      - :literal:`1`
      - :literal:`2`
      - :literal:`3`
      - :literal:`4`
      - :literal:`5` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_day/level:

      **level**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Statistics level.


      Choices:

      - :literal:`1` ← (default)
      - :literal:`2`
      - :literal:`3`
      - :literal:`4`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_day/save_for_days:

      **save_for_days**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Save for value in days.


      Choices:

      - :literal:`1` ← (default)
      - :literal:`2`
      - :literal:`3`
      - :literal:`4`
      - :literal:`5`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_month:

      **interval_past_month**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Settings for vCenter server past month statistic collection.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_month/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Past month statistics collection enabled.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_month/interval_hours:

      **interval_hours**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Interval duration in hours.


      Choices:

      - :literal:`2` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_month/level:

      **level**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Statistics level.


      Choices:

      - :literal:`1` ← (default)
      - :literal:`2`
      - :literal:`3`
      - :literal:`4`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_month/save_for_months:

      **save_for_months**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Save for value in months.


      Choices:

      - :literal:`1` ← (default)




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_week:

      **interval_past_week**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Settings for vCenter server past week statistic collection.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_week/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Past week statistics collection enabled.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_week/interval_minutes:

      **interval_minutes**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Interval duration in minutes.


      Choices:

      - :literal:`30` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_week/level:

      **level**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Statistics level.


      Choices:

      - :literal:`1` ← (default)
      - :literal:`2`
      - :literal:`3`
      - :literal:`4`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_week/save_for_weeks:

      **save_for_weeks**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Save for value in weeks.


      Choices:

      - :literal:`1` ← (default)




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_year:

      **interval_past_year**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Settings for vCenter server past month statistic collection.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_year/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Past month statistics collection enabled.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_year/interval_days:

      **interval_days**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Interval duration in days.


      Choices:

      - :literal:`1` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_year/level:

      **level**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Statistics level.


      Choices:

      - :literal:`1` ← (default)
      - :literal:`2`
      - :literal:`3`
      - :literal:`4`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-interval_past_year/save_for_years:

      **save_for_years**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Save for value in years.


      Choices:

      - :literal:`1` ← (default)
      - :literal:`2`
      - :literal:`3`
      - :literal:`4`
      - :literal:`5`




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

    
    - name: Configure vCenter statistics
      community.vmware.vmware_vcenter_statistics:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        interval_past_day:
          enabled: true
          interval_minutes: 5
          save_for_days: 1
          level: 1
        interval_past_week:
          enabled: true
          level: 1
        interval_past_month:
          enabled: true
          level: 1
        interval_past_year:
          enabled: true
          save_for_years: 1
          level: 1
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
      metadata about vCenter statistics settings


      Returned: always

      Sample: :literal:`{"changed": false, "msg": "vCenter statistics already configured properly", "past\_day\_enabled": true, "past\_day\_interval": 5, "past\_day\_level": 1, "past\_day\_save\_for": 1, "past\_month\_enabled": true, "past\_month\_interval": 2, "past\_month\_level": 1, "past\_month\_save\_for": 1, "past\_week\_enabled": true, "past\_week\_interval": 30, "past\_week\_level": 1, "past\_week\_save\_for": 1, "past\_year\_enabled": true, "past\_year\_interval": 1, "past\_year\_level": 1, "past\_year\_save\_for": 1}`




Authors
~~~~~~~

- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

