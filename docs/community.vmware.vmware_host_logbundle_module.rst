

community.vmware.vmware_host_logbundle module -- Fetch logbundle file from ESXi
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_logbundle`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to fetch logbundle file from ESXi.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-dest:

      **dest**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      file destination on localhost, path must be exist.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-esxi_hostname:

      **esxi_hostname**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the host system to fetch the logbundle.



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

      .. _parameter-manifests:

      **manifests**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      Logs to include in the logbundle file.

      Refer to the id key of the \ `community.vmware.vmware\_host\_logbundle\_info <vmware_host_logbundle_info_module.rst>`__\  module for values that can be specified in the manifest.


      Default: :literal:`["System:Base", "System:CoreDumps", "System:EsxImage", "System:IOFilter", "System:LoadESX", "System:Modules", "System:RDMA", "System:ResourceGroups", "System:TPM", "System:VFlash", "System:VMTools", "System:VmiofPlugins", "System:ntp", "System:uwstats", "Fcd:Catalog", "VirtualMachines:CoreDumps", "VirtualMachines:VirtualMachineStats", "VirtualMachines:base", "VirtualMachines:base", "VirtualMachines:diskinfo", "VirtualMachines:logs", "Storage:FCoE", "Storage:Multipathing", "Storage:NAS", "Storage:VSAN", "Storage:VSANHealth", "Storage:VSANIscsiTarget", "Storage:VSANPerfStats", "Storage:VSANPerfSvc", "Storage:VSANTraces", "Storage:VVOL", "Storage:base", "Storage:iodm", "Storage:iscsi", "FeatureStateSwitch:FeatureStateSwitch", "Userworld:HostAgent", "Userworld:ProcessInformation", "Configuration:System", "Logs:System", "hostProfiles:SystemImageCacheHostProfile", "hostProfiles:hostProfiles", "FileSystem:VMFSDiskDump", "FileSystem:base", "ActiveDirectory:base", "CIM:base", "Hardware:base", "Hardware:usb", "Installer:base", "Network:base", "Network:dvs", "Network:lacp", "Network:nscd", "Network:tcpip", "IntegrityChecks:md5sums"]`


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

      .. _parameter-performance_data:

      **performance_data**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      Gather performance data for ESXi.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-performance_data/duration:

      **duration**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Duration for which performance data is gathered.


      Default: :literal:`300`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-performance_data/interval:

      **interval**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Interval for which performance data is gathered.


      Default: :literal:`5`



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

    
    - name: fetch logbundle file from ESXi
      community.vmware.vmware_host_logbundle:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        dest: ./esxi-log.tgz

    - name: fetch logbundle file from ESXi with manifests
      community.vmware.vmware_host_logbundle:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        dest: ./esxi-log.tgz
        manifests:
          - System:Base
          - VirtualMachines:VirtualMachineStats





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

      .. _return-dest:

      **dest**

      :literal:`string`

      .. raw:: html

        </div></div>
    - 
      saved path of a logbundle file for ESXi


      Returned: on success

      Sample: :literal:`"{'changed': True, 'dest': './esxi-log.tgz', 'failed': False, 'gid': 0, 'group': 'root', 'mode': '0644', 'owner': 'root', 'size': 25783140, 'state': 'file', 'uid': 0}"`




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

