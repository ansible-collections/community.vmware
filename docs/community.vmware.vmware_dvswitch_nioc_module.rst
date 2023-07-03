

community.vmware.vmware_dvswitch_nioc module -- Manage distributed switch Network IO Control
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_dvswitch_nioc`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to manage distributed switch Network IO Control configurations.








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

      .. _parameter-resources:

      **resources**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      List of dicts containing.


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-resources/limit:

      **limit**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The maximum allowed usage for a traffic class belonging to this resource pool per host physical NIC.


      Default: :literal:`-1`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-resources/name:

      **name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Resource name.


      Choices:

      - :literal:`"faultTolerance"`
      - :literal:`"hbr"`
      - :literal:`"iSCSI"`
      - :literal:`"management"`
      - :literal:`"nfs"`
      - :literal:`"vdp"`
      - :literal:`"virtualMachine"`
      - :literal:`"vmotion"`
      - :literal:`"vsan"`
      - :literal:`"backupNfc"`
      - :literal:`"nvmetcp"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-resources/reservation:

      **reservation**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Ignored if NIOC version is set to version2

      Amount of bandwidth resource that is guaranteed available to the host infrastructure traffic class.

      If the utilization is less than the reservation, the extra bandwidth is used for other host infrastructure traffic class types.

      Reservation is not allowed to exceed the value of limit, if limit is set.

      Unit is Mbits/sec.

      Ignored unless version is "version3".

      Amount of bandwidth resource that is guaranteed available to the host infrastructure traffic class.


      Default: :literal:`0`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-resources/shares:

      **shares**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The number of shares allocated.

      Ignored unless \ :literal:`shares\_level`\  is "custom".



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-resources/shares_level:

      **shares_level**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The allocation level

      The level is a simplified view of shares.

      Levels map to a pre-determined set of numeric values for shares.


      Choices:

      - :literal:`"low"`
      - :literal:`"normal"`
      - :literal:`"high"`
      - :literal:`"custom"`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Enable or disable NIOC on the distributed switch.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`



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
      The name of the distributed switch.



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

      .. _parameter-version:

      **version**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Network IO control version.


      Choices:

      - :literal:`"version2"`
      - :literal:`"version3"`





Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Enable NIOC
      community.vmware.vmware_dvswitch_nioc:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
        version: version3
        resources:
            - name: vmotion
              limit: -1
              reservation: 128
              shares_level: normal
            - name: vsan
              limit: -1
              shares_level: custom
              shares: 99
              reservation: 256
        state: present
      delegate_to: localhost

    - name: Disable NIOC
      community.vmware.vmware_dvswitch_nioc:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch: dvSwitch
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

      .. _return-dvswitch_nioc_status:

      **dvswitch_nioc_status**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      result of the changes


      Returned: success


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _return-resources_changed:

      **resources_changed**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      list of resources which were changed


      Returned: success

      Sample: :literal:`["vmotion", "vsan"]`




Authors
~~~~~~~

- Joseph Andreatta (@vmwjoseph)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

