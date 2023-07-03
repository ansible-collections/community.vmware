

community.vmware.vmware_guest_serial_port module -- Manage serial ports on an existing VM
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_guest_serial_port`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage serial ports on an existing VM








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings:

      **backings**

      :literal:`list` / :literal:`elements=dictionary` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      A list of backings for serial ports.

      \ :literal:`backing\_type`\  (str): is required to add or reconfigure or remove an existing serial port.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/backing_type:
      .. _parameter-backings/type:

      **backing_type**

      aliases: type

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Backing type is required for the serial ports to be added or reconfigured or removed.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/device_name:

      **device_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Serial device absolutely path.

      Required when \ :emphasis:`backing\_type=device`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/direction:

      **direction**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The direction of the connection.

      Required when \ :emphasis:`backing\_type=network`\ .


      Choices:

      - :literal:`"client"` ← (default)
      - :literal:`"server"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/endpoint:

      **endpoint**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      When you use serial port pipe backing to connect a virtual machine to another process, you must define the endpoints.

      Required when \ :emphasis:`backing\_type=pipe`\ .


      Choices:

      - :literal:`"client"` ← (default)
      - :literal:`"server"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/file_path:

      **file_path**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      File path for the host file used in this backing. Fully qualified path is required, like \<datastore\_name\>/\<file\_name\>.

      Required when \ :emphasis:`backing\_type=file`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/no_rx_loss:

      **no_rx_loss**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enables optimized data transfer over the pipe.

      Required when \ :emphasis:`backing\_type=pipe`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/pipe_name:

      **pipe_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Pipe name for the host pipe.

      Required when \ :emphasis:`backing\_type=pipe`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/proxy_uri:

      **proxy_uri**

      :literal:`string`

      added in community.vmware 3.7.0


      .. raw:: html

        </div></div>

    - 
      Identifies a vSPC proxy service that provides network access to the \ :emphasis:`service\_uri`\ .

      If you specify a proxy URI, the virtual machine initiates a connection with the proxy service and forwards the serviceURI and direction to the proxy.

      The \ :literal:`Use Virtual Serial Port Concentrator`\  option is automatically enabled when \ :emphasis:`proxy\_uri`\  is set.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/service_uri:

      **service_uri**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Identifies the local host or a system on the network, depending on the value of \ :emphasis:`direction`\ .

      If you use the virtual machine as a server, the URI identifies the host on which the virtual machine runs.

      In this case, the host name part of the URI should be empty, or it should specify the address of the local host.

      If you use the virtual machine as a client, the URI identifies the remote system on the network.

      Required when \ :emphasis:`backing\_type=network`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      \ :literal:`state`\  is required to identify whether we are adding, modifying or removing the serial port.

      If \ :literal:`state`\  is set to \ :literal:`present`\ , a serial port will be added or modified.

      If \ :literal:`state`\  is set to \ :literal:`absent`\ , an existing serial port will be removed.

      If an existing serial port to modify or remove, \ :literal:`backing\_type`\  and either of \ :literal:`service\_uri`\  or \ :literal:`pipe\_name`\  or \ :literal:`device\_name`\  or \ :literal:`file\_path`\  are required.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-backings/yield_on_poll:

      **yield_on_poll**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Enables CPU yield behavior.


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
      Name of the virtual machine.

      This is a required parameter, if parameter \ :literal:`uuid`\  or \ :literal:`moid`\  is not supplied.



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
      UUID of the instance to manage the serial ports, this is VMware's unique identifier.

      This is a required parameter, if parameter \ :literal:`name`\  or \ :literal:`moid`\  is not supplied.



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

    
    # Create serial ports
    - name: Create multiple serial ports with Backing type - network, pipe, device and file
      community.vmware.vmware_guest_serial_port:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: "test_vm1"
        backings:
        - type: 'network'
          direction: 'client'
          service_uri: 'tcp://6000'
          yield_on_poll: true
        - type: 'pipe'
          pipe_name: 'serial_pipe'
          endpoint: 'client'
        - type: 'device'
          device_name: '/dev/char/serial/uart0'
        - type: 'file'
          file_path: '[datastore1]/file1'
          yield_on_poll:  true
        register: create_multiple_ports

    # Create vSPC port
    - name: Create network serial port with vSPC
      community.vmware.vmware_guest_serial_port:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: "test_vm1"
        backings:
        - type: 'network'
          direction: 'server'
          service_uri: 'vSPC.py'
          proxy_uri: 'telnets://<host>:<port>'
          yield_on_poll: true

    # Modify existing serial port
    - name: Modify Network backing type
      community.vmware.vmware_guest_serial_port:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        name: '{{ name }}'
        backings:
        - type: 'network'
          state: 'present'
          direction: 'server'
          service_uri: 'tcp://6000'
      delegate_to: localhost

    # Remove serial port
    - name: Remove pipe backing type
      community.vmware.vmware_guest_serial_port:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        name: '{{ name }}'
        backings:
        - type: 'pipe'
          state: 'absent'
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

      .. _return-serial_port_data:

      **serial_port_data**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      metadata about the virtual machine's serial ports after managing them


      Returned: always

      Sample: :literal:`[{"backing\_type": "network", "direction": "client", "service\_uri": "tcp://6000"}, {"backing\_type": "pipe", "direction": "server", "pipe\_name": "serial pipe"}]`




Authors
~~~~~~~

- Anusha Hegde (@anusha94)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

