

community.vmware.vmware_dvswitch_pvlans module -- Manage Private VLAN configuration of a Distributed Switch
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_dvswitch_pvlans`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure Private VLANs (PVLANs) on a Distributed Switch.








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

      .. _parameter-primary_pvlans:

      **primary_pvlans**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of VLAN IDs that should be configured as Primary PVLANs.

      If \ :literal:`primary\_pvlans`\  isn't specified, all PVLANs will be deleted if present.

      Each member of the list requires primary\_pvlan\_id (int) set.

      The secondary promiscuous PVLAN will be created automatically.

      If \ :literal:`secondary\_pvlans`\  isn't specified, the primary PVLANs and each secondary promiscuous PVLAN will be created.

      Please see examples for more information.


      Default: :literal:`[]`


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

      .. _parameter-secondary_pvlans:

      **secondary_pvlans**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      A list of VLAN IDs that should be configured as Secondary PVLANs.

      \ :literal:`primary\_pvlans`\  need to be specified to create any Secondary PVLAN.

      If \ :literal:`primary\_pvlans`\  isn't specified, all PVLANs will be deleted if present.

      Each member of the list requires primary\_pvlan\_id (int), secondary\_pvlan\_id (int), and pvlan\_type (str) to be set.

      The type of the secondary PVLAN can be isolated or community. The secondary promiscuous PVLAN will be created automatically.

      Please see examples for more information.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-dvswitch:
      .. _parameter-switch:

      **switch**

      aliases: dvswitch

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the Distributed Switch.



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

    
    - name: Create PVLANs on a Distributed Switch
      community.vmware.vmware_dvswitch_pvlans:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        primary_pvlans:
          - primary_pvlan_id: 1
          - primary_pvlan_id: 4
        secondary_pvlans:
          - primary_pvlan_id: 1
            secondary_pvlan_id: 2
            pvlan_type: isolated
          - primary_pvlan_id: 1
            secondary_pvlan_id: 3
            pvlan_type: community
          - primary_pvlan_id: 4
            secondary_pvlan_id: 5
            pvlan_type: community
      delegate_to: localhost

    - name: Create primary PVLAN and secondary promiscuous PVLAN on a Distributed Switch
      community.vmware.vmware_dvswitch_pvlans:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        primary_pvlans:
          - primary_pvlan_id: 1
      delegate_to: localhost

    - name: Remove all PVLANs from a Distributed Switch
      community.vmware.vmware_dvswitch_pvlans:
        hostname: '{{ inventory_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        primary_pvlans: []
        secondary_pvlans: []
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

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      information about performed operation


      Returned: always

      Sample: :literal:`"{'changed': True, 'dvswitch': 'dvSwitch', 'private\_vlans': [{'primary\_pvlan\_id': 1, 'pvlan\_type': 'promiscuous', 'secondary\_pvlan\_id': 1}, {'primary\_pvlan\_id': 1, 'pvlan\_type': 'isolated', 'secondary\_pvlan\_id': 2}, {'primary\_pvlan\_id': 1, 'pvlan\_type': 'community', 'secondary\_pvlan\_id': 3}], 'private\_vlans\_previous': [], 'result': 'All private VLANs added'}"`




Authors
~~~~~~~

- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

