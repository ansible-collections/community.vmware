

community.vmware.vmware_host_tcpip_stacks module -- Manage the TCP/IP Stacks configuration of ESXi host
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_host_tcpip_stacks`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to modify the TCP/IP stacks configuration.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default:

      **default**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The TCP/IP stacks configuration of the \ :emphasis:`default`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/alternate_dns:

      **alternate_dns**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The IP address of the alternate dns server.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/congestion_algorithm:

      **congestion_algorithm**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The TCP congest control algorithm.


      Choices:

      - :literal:`"newreno"` ← (default)
      - :literal:`"cubic"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/domain:

      **domain**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The domain name portion of the DNS name.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/gateway:

      **gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv4 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/hostname:

      **hostname**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The host name of the ESXi host.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/ipv6_gateway:

      **ipv6_gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv6 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/max_num_connections:

      **max_num_connections**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of socket connection that are requested.


      Default: :literal:`11000`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/preferred_dns:

      **preferred_dns**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The IP address of the preferred dns server.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-default/search_domains:

      **search_domains**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      The domain in which to search for hosts, placed in order of preference.


      Default: :literal:`[]`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the ESXi host.



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

      .. _parameter-provisioning:

      **provisioning**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The TCP/IP stacks configuration of the \ :emphasis:`provisioning`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-provisioning/congestion_algorithm:

      **congestion_algorithm**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The TCP congest control algorithm.


      Choices:

      - :literal:`"newreno"` ← (default)
      - :literal:`"cubic"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-provisioning/gateway:

      **gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv4 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-provisioning/ipv6_gateway:

      **ipv6_gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv6 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-provisioning/max_num_connections:

      **max_num_connections**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of socket connection that are requested.


      Default: :literal:`11000`



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



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmotion:

      **vmotion**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The TCP/IP stacks configuration of the \ :emphasis:`vmotion`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmotion/congestion_algorithm:

      **congestion_algorithm**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The TCP congest control algorithm.


      Choices:

      - :literal:`"newreno"` ← (default)
      - :literal:`"cubic"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmotion/gateway:

      **gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv4 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmotion/ipv6_gateway:

      **ipv6_gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv6 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-vmotion/max_num_connections:

      **max_num_connections**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of socket connection that are requested.


      Default: :literal:`11000`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nsx_overlay:
      .. _parameter-vxlan:

      **vxlan**

      aliases: nsx_overlay

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The TCP/IP stacks configuration of the \ :emphasis:`vxlan`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nsx_overlay/congestion_algorithm:
      .. _parameter-vxlan/congestion_algorithm:

      **congestion_algorithm**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The TCP congest control algorithm.


      Choices:

      - :literal:`"newreno"` ← (default)
      - :literal:`"cubic"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nsx_overlay/gateway:
      .. _parameter-vxlan/gateway:

      **gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv4 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nsx_overlay/ipv6_gateway:
      .. _parameter-vxlan/ipv6_gateway:

      **ipv6_gateway**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The ipv6 gateway address.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-nsx_overlay/max_num_connections:
      .. _parameter-vxlan/max_num_connections:

      **max_num_connections**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum number of socket connection that are requested.


      Default: :literal:`11000`





Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Update the TCP/IP stack configuration of the default
      community.vmware.vmware_host_tcpip_stacks:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        esxi_hostname: "{{ esxi_hostname }}"
        default:
          hostname: "{{ esxi_hostname }}"
          domain: example.com
          preferred_dns: 192.168.10.1
          alternate_dns: 192.168.20.1
          search_domains:
            - hoge.com
            - fuga.com
          gateway: 192.168.10.1
          congestion_algorithm: cubic
          max_num_connections: 12000

    - name: Update the TCP/IP stack configuration of the provisioning
      community.vmware.vmware_host_tcpip_stacks:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        esxi_hostname: "{{ esxi_hostname }}"
        provisioning:
          congestion_algorithm: newreno
          max_num_connections: 12000
          gateway: 10.10.10.254

    - name: Update the TCP/IP stack configuration of the default and provisioning
      community.vmware.vmware_host_tcpip_stacks:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        esxi_hostname: "{{ esxi_hostname }}"
        default:
          hostname: "{{ esxi_hostname }}"
          domain: example.com
          preferred_dns: 192.168.10.1
          alternate_dns: 192.168.20.1
          search_domains:
            - hoge.com
            - fuga.com
          gateway: 192.168.10.1
          congestion_algorithm: cubic
          max_num_connections: 12000
        provisioning:
          congestion_algorithm: newreno
          max_num_connections: 12000
          gateway: 10.10.10.254

    - name: Update the ipv6 gateway of the provisioning TCP/IP stack
      community.vmware.vmware_host_tcpip_stacks:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        validate_certs: false
        esxi_hostname: "{{ esxi_hostname }}"
        provisioning:
          ipv6_gateway: ::ffff:6440:301





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

      .. _return-default:

      **default**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dict of the TCP/IP stack configuration of the default.


      Returned: always

      Sample: :literal:`"{\\n    \\"alternate\_dns\\": \\"192.168.20.1\\",\\n    \\"congestion\_algorithm\\": \\"cubic\\",\\n    \\"domain\\": \\"example.com\\",\\n    \\"gateway\\": \\"192.168.10.1\\",\\n    \\"ipv6\_gateway\\", null,\\n    \\"hostname\\": \\"esxi-test03\\",\\n    \\"max\_num\_connections\\": 12000,\\n    \\"preferred\_dns\\": \\"192.168.10.1\\",\\n    \\"search\_domains\\": [\\n        \\"hoge.com\\",\\n        \\"fuga.com\\"\\n    ]\\n}"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-provisioning:

      **provisioning**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dict of the TCP/IP stack configuration of the provisioning.


      Returned: always

      Sample: :literal:`{"congestion\_algorithm": "newreno", "gateway": "10.10.10.254", "ipv6\_gateway": null, "max\_num\_connections": 12000}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-vmotion:

      **vmotion**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dict of the TCP/IP stack configuration of the vmotion.


      Returned: always

      Sample: :literal:`{"congestion\_algorithm": "newreno", "gateway": null, "ipv6\_gateway": null, "max\_num\_connections": 11000}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-vxlan:

      **vxlan**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      dict of the TCP/IP stack configuration of the vxlan.


      Returned: always

      Sample: :literal:`{"congestion\_algorithm": "newreno", "gateway": null, "ipv6\_gateway": null, "max\_num\_connections": 11000}`




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

