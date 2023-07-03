

community.vmware.vmware_host_iscsi module -- Manage the iSCSI configuration of ESXi host
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_iscsi`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- In this module, can manage the iSCSI configuration of ESXi host








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
      The ESXi hostname on which to change iSCSI settings.



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

      .. _parameter-iscsi_config:

      **iscsi_config**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The iSCSI configs.

      This parameter is required if \ :emphasis:`state=present`\  or \ :emphasis:`state=absent`\ .


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/alias:

      **alias**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The new value for the alias of the adapter.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication:

      **authentication**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      CHAP authentication parent settings for iSCSI.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication/chap_auth_enabled:

      **chap_auth_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to enable CHAP authentication.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication/chap_authentication_type:

      **chap_authentication_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.


      Choices:

      - :literal:`"chapDiscouraged"`
      - :literal:`"chapPreferred"`
      - :literal:`"chapRequired"`
      - :literal:`"chapProhibited"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication/chap_name:

      **chap_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      CHAP user name if CHAP is enabled.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication/chap_secret:

      **chap_secret**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The secret password of CHAP if CHAP is enabled.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication/mutual_chap_authentication_type:

      **mutual_chap_authentication_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.


      Choices:

      - :literal:`"chapProhibited"` ← (default)
      - :literal:`"chapRequired"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication/mutual_chap_name:

      **mutual_chap_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/authentication/mutual_chap_secret:

      **mutual_chap_secret**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The secret password of mutual CHAP if Mutual-CHAP is enabled.




  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/force:

      **force**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Force port bind VMkernels to be removed.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/initiator_iqn:
      .. _parameter-iscsi_config/iscsi_name:

      **iscsi_name**

      aliases: initiator_iqn

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The name for the iSCSI HBA adapter.

      This is iSCSI qualified name.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/port_bind:

      **port_bind**

      :literal:`list` / :literal:`elements=string`

      .. raw:: html

        </div></div>

    - 
      The list of the VMkernels if use port bindings.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target:

      **send_target**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The iSCSI dynamic target settings.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/address:

      **address**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The IP address or hostname of the storage device.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication:

      **authentication**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      CHAP authentication settings of a dynamic target for iSCSI.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/chap_auth_enabled:

      **chap_auth_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to enable CHAP authentication.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/chap_authentication_type:

      **chap_authentication_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.


      Choices:

      - :literal:`"chapDiscouraged"`
      - :literal:`"chapPreferred"`
      - :literal:`"chapRequired"`
      - :literal:`"chapProhibited"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/chap_inherited:

      **chap_inherited**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether or not to inherit CHAP settings from the parent settings.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/chap_name:

      **chap_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      CHAP user name if CHAP is enabled.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/chap_secret:

      **chap_secret**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The secret password of CHAP if CHAP is enabled.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/mutual_chap_authentication_type:

      **mutual_chap_authentication_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.


      Choices:

      - :literal:`"chapProhibited"` ← (default)
      - :literal:`"chapRequired"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/mutual_chap_inherited:

      **mutual_chap_inherited**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether or not to inherit Mutual-CHAP settings from the parent settings.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/mutual_chap_name:

      **mutual_chap_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/authentication/mutual_chap_secret:

      **mutual_chap_secret**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The secret password of mutual CHAP if Mutual-CHAP is enabled.




  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/send_target/port:

      **port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The TCP port of the storage device.

      If not specified, the standard default of 3260 is used.


      Default: :literal:`3260`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target:

      **static_target**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      The iSCSI static target settings.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/address:

      **address**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The IP address or hostname of the storage device.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication:

      **authentication**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      CHAP authentication settings of a static target for iSCSI.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/chap_auth_enabled:

      **chap_auth_enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to enable CHAP authentication.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/chap_authentication_type:

      **chap_authentication_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.


      Choices:

      - :literal:`"chapDiscouraged"`
      - :literal:`"chapPreferred"`
      - :literal:`"chapRequired"`
      - :literal:`"chapProhibited"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/chap_inherited:

      **chap_inherited**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether or not to inherit CHAP settings from the parent settings.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/chap_name:

      **chap_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      CHAP user name if CHAP is enabled.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/chap_secret:

      **chap_secret**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The secret password of CHAP if CHAP is enabled.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/mutual_chap_authentication_type:

      **mutual_chap_authentication_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.


      Choices:

      - :literal:`"chapProhibited"` ← (default)
      - :literal:`"chapRequired"`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/mutual_chap_inherited:

      **mutual_chap_inherited**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether or not to inherit Mutual-CHAP settings from the parent settings.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/mutual_chap_name:

      **mutual_chap_name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/authentication/mutual_chap_secret:

      **mutual_chap_secret**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The secret password of mutual CHAP if Mutual-CHAP is enabled.




  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/iscsi_name:

      **iscsi_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the iSCSI target to connect to.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/static_target/port:

      **port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The TCP port of the storage device.

      If not specified, the standard default of 3260 is used.


      Default: :literal:`3260`



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-iscsi_config/vmhba_name:

      **vmhba_name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The iSCSI adapter name.




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
      If set to \ :literal:`present`\ , add the iSCSI target or the bind ports if they are not existing.

      If set to \ :literal:`present`\ , update the iSCSI settings if they already exist and occur change.

      If set to \ :literal:`absent`\ , remove the iSCSI target or the bind ports if they are existing.

      If set to (enabled), enable the iSCSI of ESXi if the iSCSI is disabled.

      If set to (disabled), disable the iSCSI of ESXi if the iSCSI is enabled.


      Choices:

      - :literal:`"present"` ← (default)
      - :literal:`"absent"`
      - :literal:`"enabled"`
      - :literal:`"disabled"`



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

    
    - name: Enable iSCSI of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        state: enabled

    - name: Add a dynamic target to iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          send_target:
            address: "{{ send_target_address }}"
        state: present

    - name: Add a static target to iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          static_target:
            iscsi_name: iqn.2011-08.com.xxxxxxx:as6104t-8c3e9d.target001
            address: "{{ send_target_address }}"
        state: present

    - name: Add VMKernels to iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          port_bind:
            - vmk0
            - vmk1
        state: present

    - name: Use CHAP authentication
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          authentication:
            chap_auth_enabled: true
            chap_authentication_type: chapPreferred
            chap_name: chap_user_name
            chap_secret: secret
        state: present

    - name: Remove a dynamic target from iSCSI config of ESXi
      community.vmware.vmware_host_iscsi:
        hostname: "{{ vcenter_hostname }}"
        username: "{{ vcenter_username }}"
        password: "{{ vcenter_password }}"
        esxi_hostname: "{{ esxi_hostname }}"
        iscsi_config:
          vmhba_name: vmhba65
          send_target:
            address: "{{ send_target_address }}"
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

      .. _return-iscsi_properties:

      **iscsi_properties**

      :literal:`dictionary`

      .. raw:: html

        </div></div>
    - 
      Parameter return when system defaults config is changed.


      Returned: changed

      Sample: :literal:`{"iscsi\_alias": "", "iscsi\_authentication\_properties": {"\_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties", "chapAuthEnabled": false, "chapAuthenticationType": "chapProhibited", "chapInherited": null, "chapName": "", "chapSecret": "XXXXXXXXXXXXXXXXXXXXX", "mutualChapAuthenticationType": "chapProhibited", "mutualChapInherited": null, "mutualChapName": "XXXXXXXXXXXXXXXXXXXXX", "mutualChapSecret": ""}, "iscsi\_enabled": true, "iscsi\_name": "", "iscsi\_send\_targets": [], "iscsi\_static\_targets": [], "port\_bind": [], "vmhba\_name": "vmhba65"}`




Authors
~~~~~~~

- sky-joker (@sky-joker)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

