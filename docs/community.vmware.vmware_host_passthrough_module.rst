

community.vmware.vmware_host_passthrough module -- Manage PCI device passthrough settings on host
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_passthrough`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be managed PCI device passthrough settings on host.








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

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the cluster from which all host systems will be used.

      This parameter is required if \ :literal:`esxi\_hostname`\  is not specified.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-devices:

      **devices**

      :literal:`list` / :literal:`elements=dictionary` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      List of PCI device name or id.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-devices/device:
      .. _parameter-devices/device_name:
      .. _parameter-devices/name:

      **device**

      aliases: name, device_name

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of PCI device to enable passthrough.




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
      If \ :emphasis:`state=present`\ , passthrough of PCI device will be enabled.

      If \ :emphasis:`state=absent`\ , passthrough of PCI device will be disabled.


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

.. note::
   - Supports \ :literal:`check\_mode`\ .
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Enable PCI device passthrough against the whole ESXi in a cluster
      community.vmware.vmware_host_passthrough:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        cluster: "{{ ccr1 }}"
        devices:
          - device_name: "Dual Band Wireless AC 3165"
        state: present

    - name: Enable PCI device passthrough against one ESXi
      community.vmware.vmware_host_passthrough:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        esxi_hostname: "{{ esxi1 }}"
        devices:
          - device_name: "Dual Band Wireless AC 3165"
        state: present

    - name: Enable PCI device passthrough with PCI ids
      community.vmware.vmware_host_passthrough:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        esxi_hostname: "{{ esxi1 }}"
        devices:
          - device: '0000:03:00.0'
          - device: '0000:00:02.0'
        state: present

    - name: Disable PCI device passthrough against the whole ESXi in a cluster
      community.vmware.vmware_host_passthrough:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        cluster: "{{ ccr1 }}"
        devices:
          - device_name: "Dual Band Wireless AC 3165"
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

      .. _return-passthrough_configs:

      **passthrough_configs**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>
    - 
      list of that PCI devices have been enabled passthrough for each host system.


      Returned: changed

      Sample: :literal:`"[\\n    {\\n        \\"esxi-01.example.com\\": [\\n            {\\n                \\"device\_id\\": \\"0000:03:00.0\\",\\n                \\"device\_name\\": \\"Dual Band Wireless AC 3165\\",\\n                \\"passthruEnabled\\": true\\n            }\\n        ]\\n    },\\n    {\\n        \\"esxi-02.example.com\\": [\\n            {\\n                \\"device\_id\\": \\"0000:03:00.0\\",\\n                \\"device\_name\\": \\"Dual Band Wireless AC 3165\\",\\n                \\"passthruEnabled\\": true\\n            }\\n        ]\\n    }\\n]"`




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

