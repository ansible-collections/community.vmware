

community.vmware.vcenter_extension module -- Register/deregister vCenter Extensions
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vcenter_extension`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to register/deregister vCenter Extensions.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-client_type:

      **client_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . Type of client the extension is (win32, .net, linux, etc.).


      Default: :literal:`"vsphere-client-serenity"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-company:

      **company**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . The name of the company that makes the extension.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-description:

      **description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . A short description of the extension.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-email:

      **email**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . Administrator email to use for extension.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-extension_key:

      **extension_key**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The extension key of the extension to install or uninstall.



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

      .. _parameter-name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . The name of the extension you are installing.



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

      .. _parameter-server_type:

      **server_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . Type of server being used to install the extension (SOAP, REST, HTTP, etc.).


      Default: :literal:`"vsphere-client-serenity"`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-ssl_thumbprint:

      **ssl_thumbprint**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . SSL thumbprint of the extension hosting server.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Add or remove vCenter Extension.


      Choices:

      - :literal:`"absent"`
      - :literal:`"present"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-url:

      **url**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Required for \ :literal:`state=present`\ . Link to server hosting extension zip file to install.



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

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The version of the extension you are installing or uninstalling.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-visible:

      **visible**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Show the extension in solution manager inside vCenter.


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

    
        - name: Register vCenter Extension
          community.vmware.vcenter_extension:
             hostname: "{{ groups['vcsa'][0] }}"
             username: "{{ vcenter_username }}"
             password: "{{ site_password }}"
             extension_key: "{{ extension_key }}"
             version: "1.0"
             company: "Acme"
             name: "Acme Extension"
             description: "acme management"
             email: "user@example.com"
             url: "https://10.0.0.1/ACME-vSphere-web-plugin-1.0.zip"
             ssl_thumbprint: "{{ ssl_thumbprint }}"
             state: present
          delegate_to: localhost
          register: register_extension

        - name: Deregister vCenter Extension
          community.vmware.vcenter_extension:
             hostname: "{{ groups['vcsa'][0] }}"
             username: "{{ vcenter_username }}"
             password: "{{ site_password }}"
             extension_key: "{{ extension_key }}"
             version: "1.0"
             state: absent
          delegate_to: localhost
          register: deregister_extension





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

      Sample: :literal:`"'com.acme.Extension' installed."`




Authors
~~~~~~~

- Michael Tipton (@castawayegr)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

