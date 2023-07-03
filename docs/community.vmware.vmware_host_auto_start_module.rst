

community.vmware.vmware_host_auto_start module -- Manage the auto power ON or OFF for vm on ESXi host
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_auto_start`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- In this module, can set up automatic startup and shutdown of virtual machines according to host startup or shutdown.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      ESXi hostname where the VM to set auto power on or off exists.



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

      .. _parameter-moid:

      **moid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Managed Object ID of the instance to manage if known, this is a unique identifier only within a single vCenter instance.

      This is required if \ :literal:`name`\  or \ :literal:`uuid`\  is not supplied.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      VM name to set auto power on or off.

      This is not necessary if change only system default VM settings for autoStart config.



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

      .. _parameter-power_info:

      **power_info**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Startup or shutdown settings of virtual machine.

      This setting will override the system defaults.


      Default: :literal:`{"start\_action": "none", "start\_delay": -1, "start\_order": -1, "stop\_action": "systemDefault", "stop\_delay": -1, "wait\_for\_heartbeat": "systemDefault"}`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-power_info/start_action:

      **start_action**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Whether to start the virtual machine when the host startup.


      Choices:

      - :literal:`"none"` ← (default)
      - :literal:`"powerOn"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-power_info/start_delay:

      **start_delay**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Auto start delay in seconds of virtual machine.


      Default: :literal:`-1`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-power_info/start_order:

      **start_order**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The autostart priority of virtual machine.

      Virtual machines with a lower number are powered on first.

      On host shutdown, the virtual machines are shut down in reverse order, meaning those with a higher number are powered off first.


      Default: :literal:`-1`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-power_info/stop_action:

      **stop_action**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Stop action executed on the virtual machine when the system stops of virtual machine.


      Choices:

      - :literal:`"none"`
      - :literal:`"systemDefault"` ← (default)
      - :literal:`"powerOff"`
      - :literal:`"suspend"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-power_info/stop_delay:

      **stop_delay**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Auto stop delay in seconds of virtual machine.


      Default: :literal:`-1`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-power_info/wait_for_heartbeat:

      **wait_for_heartbeat**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Continue power on processing when VMware Tools started.


      Choices:

      - :literal:`"no"`
      - :literal:`"yes"`
      - :literal:`"systemDefault"` ← (default)




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

      .. _parameter-system_defaults:

      **system_defaults**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      System defaults for auto-start or auto-stop config for virtual machine.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-system_defaults/enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enable automatically start or stop of virtual machines.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-system_defaults/start_delay:

      **start_delay**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Default auto start delay in seconds.


      Default: :literal:`120`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-system_defaults/stop_action:

      **stop_action**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Default stop action executed on the virtual machine when the system stops.


      Choices:

      - :literal:`"none"`
      - :literal:`"guestShutdown"`
      - :literal:`"powerOff"` ← (default)
      - :literal:`"suspend"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-system_defaults/stop_delay:

      **stop_delay**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Default auto stop delay in seconds.


      Default: :literal:`120`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-system_defaults/wait_for_heartbeat:

      **wait_for_heartbeat**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Continue power on processing when VMware Tools started.

      If this parameter is enabled to powers on the next virtual machine without waiting for the delay to pass.

      However, the virtual machine must have VMware Tools installed.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-use_instance_uuid:

      **use_instance_uuid**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to use the VMware instance UUID rather than the BIOS UUID.


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

      .. _parameter-uuid:

      **uuid**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      VM uuid to set auto power on or off, this is VMware's unique identifier.

      This is required if \ :literal:`name`\  is not supplied.

      This is not necessary if change only system default VM settings for autoStart config.



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

    
    ---
    - name: Update for system defaults config.
      community.vmware.vmware_host_auto_start:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        system_defaults:
          enabled: true
          start_delay: 100
          stop_action: guestShutdown

    - name: Update for powerInfo config of virtual machine.
      community.vmware.vmware_host_auto_start:
        hostname: "{{ hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        name: "{{ vm_name }}"
        power_info:
          start_action: powerOn
          start_delay: 10
          start_order: 1
          stop_action: powerOff
          wait_for_heartbeat: true





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

      .. _return-power_info_config:

      **power_info_config**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      Parameter return when virtual machine power info config is changed.


      Returned: changed

      Sample: :literal:`{"start\_action": "powerOn", "start\_delay": -1, "start\_order": -1, "stop\_action": "systemDefault", "stop\_delay": -1, "wait\_for\_heartbeat": "systemDefault"}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-system_defaults_config:

      **system_defaults_config**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      Parameter return when system defaults config is changed.


      Returned: changed

      Sample: :literal:`{"enabled": true, "start\_delay": 120, "stop\_action": "powerOff", "stop\_delay": 120, "wait\_for\_heartbeat": false}`




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

