

community.vmware.vcenter_standard_key_provider module -- Add, reconfigure or remove Standard Key Provider on vCenter server
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vcenter_standard_key_provider`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module is used for adding, reconfiguring or removing Standard Key Provider on vCenter server. Refer to VMware docs for more information: \ `Standard Key Provider <https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-6DB1E745-9624-43EA-847C-DD2F767CB94B.html>`__\ 









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

      .. _parameter-kms_info:

      **kms_info**

      :literal:`list` / :literal:`elements=dictionary`

      .. raw:: html

        </div></div>

    - 
      The information of an external key server (KMS).

      \ :literal:`kms\_name`\ , \ :literal:`kms\_ip`\  are required when adding a Standard Key Provider.

      If \ :literal:`kms\_port`\  is not specified, the default port 5696 will be used.

      \ :literal:`kms\_ip`\ , \ :literal:`kms\_port`\  can be reconfigured for an existing KMS with name \ :literal:`kms\_name`\ .


      Default: :literal:`[]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-kms_info/kms_ip:

      **kms_ip**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      IP address of the external KMS.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-kms_info/kms_name:

      **kms_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the KMS to be configured.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-kms_info/kms_port:

      **kms_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Port of the external KMS.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-kms_info/remove_kms:

      **remove_kms**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Remove the configured KMS with name \ :literal:`kms\_name`\  from the KMIP cluster.


      Choices:

      - :literal:`false`
      - :literal:`true`




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-kms_password:

      **kms_password**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Password to authenticate to the KMS.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-kms_username:

      **kms_username**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Username to authenticate to the KMS.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-make_kms_trust_vc:

      **make_kms_trust_vc**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      After adding the Standard Key Provider to the vCenter Server, you can establish a trusted connection, the exact process depends on the certificates that the key provider accepts, and on your company policy.

      Three methods implemented here, (1) upload client certificate and private key through \ :literal:`upload\_client\_cert`\  and \ :literal:`upload\_client\_key`\  parameters, (2) generate, update, download vCenter self signed certificate through \ :literal:`download\_self\_signed\_cert`\  parameter, (3) download generated Certificate Signing Request(CSR) through \ :literal:`download\_client\_csr`\  parameter, send it to KMS then upload the KMS signed CSR through \ :literal:`upload\_kms\_signed\_client\_csr`\  parameter.

      This is not set to be mandatory, if not set, please go to vCenter to setup trust connection with KMS manually.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-make_kms_trust_vc/download_client_csr:

      **download_client_csr**

      :literal:`path`

      .. raw:: html

        </div></div>

    - 
      The absolute path on local machine for keeping vCenter generated CSR.

      Then upload the KMS signed CSR using \ :literal:`upload\_kms\_signed\_client\_csr`\  to vCenter.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-make_kms_trust_vc/download_self_signed_cert:

      **download_self_signed_cert**

      :literal:`path`

      .. raw:: html

        </div></div>

    - 
      The absolute path on local machine for keeping vCenter generated self signed client cert.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-make_kms_trust_vc/upload_client_cert:

      **upload_client_cert**

      :literal:`path`

      .. raw:: html

        </div></div>

    - 
      The absolute file path of client certificate.

      Request a certificate and private key from the KMS vendor. The files are X509 files in PEM format.

      The certificate might be already trusted by the KMS server.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-make_kms_trust_vc/upload_client_key:

      **upload_client_key**

      :literal:`path`

      .. raw:: html

        </div></div>

    - 
      The absolute file path of client private key to be uploaded together with \ :literal:`upload\_client\_cert`\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-make_kms_trust_vc/upload_kms_signed_client_csr:

      **upload_kms_signed_client_csr**

      :literal:`path`

      .. raw:: html

        </div></div>

    - 
      The absolute file path of KMS signed CSR downloaded from \ :literal:`download\_client\_csr`\ .




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mark_default:

      **mark_default**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Set specified Key Provider with name \ :literal:`name`\  as the default Key Provider.

      If new added Key Provider is the only key provider in vCenter, then will mark it as default after adding.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the Key Provider to be added, reconfigured or removed from vCenter.



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
      Port of the proxy server.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_server:

      **proxy_server**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Address of the proxy server to connect to KMS.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      If set to \ :literal:`absent`\ , the named Key Provider will be removed from vCenter.

      If set to \ :literal:`present`\ , the named existing Key Provider will be reconfigured or new Key Provider will be added.


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
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add a new Standard Key Provider with client certificate and private key
      community.vmware.vcenter_standard_key_provider:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: 'test_standard_kp'
        state: 'present'
        mark_default: true
        kms_info:
          - kms_name: test_kms_1
            kms_ip: 192.168.1.10
        make_kms_trust_vc:
          upload_client_cert: "/tmp/test_cert.pem"
          upload_client_key: "/tmp/test_cert_key.pem"
      register: add_skp_result

    - name: Remove the KMS from the key provider cluster
      community.vmware.vcenter_standard_key_provider:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: 'test_standard_kp'
        state: 'present'
        kms_info:
          - kms_name: test_kms_1
            remove_kms: true
      register: remove_kms_result

    - name: Remove the Standard Key Provider
      community.vmware.vcenter_standard_key_provider:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        name: 'test_standard_kp'
        state: 'absent'
      register: remove_kp_result





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

      .. _return-key_provider_clusters:

      **key_provider_clusters**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>
    - 
      the Key Provider cluster info


      Returned: always

      Sample: :literal:`[{"has\_backup": null, "key\_id": null, "key\_provide\_id": "test\_standard", "management\_type": null, "servers": [{"address": "192.168.1.10", "name": "test\_kms", "port": 5696, "protocol": "", "proxy": "", "proxy\_port": null, "user\_name": ""}], "tpm\_required": null, "use\_as\_default": true}]`




Authors
~~~~~~~

- Diane Wang (@Tomorrow9) 



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

