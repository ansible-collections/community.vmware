.. _community.vmware.vmware_httpapi:


***********************
community.vmware.vmware
***********************

**HttpApi Plugin for VMware REST API**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This HttpApi plugin provides methods to connect to VMware vCenter over a HTTP(S)-based APIs.


Examples:
---------

Using the 'appliance' API:

- hosts: all
  connection: httpapi
  gather_facts: false
  vars:
    ansible_network_os: vmware
    ansible_host: vcenter.my.domain
    ansible_user: administrator@vsphere.local
    ansible_httpapi_password: "SomePassword"
    ansbile_httpapi_use_ssl: yes
    ansible_httpapi_validate_certs: false
  tasks:

  - name: Get all access modes information
    vmware_appliance_access_info:

  - name: Get ssh access mode information
    vmware_appliance_access_info:
      access_mode: ssh
      
Using the 'vcenter' API:

- hosts: all
  connection: httpapi
  gather_facts: false
  vars:
    ansible_network_os: vmware
    ansible_host: vcenter.my.domain
    ansible_user: some.user
    ansible_httpapi_password: "SomePassword"
    ansible_httpapi_use_ssl: yes
    ansible_httpapi_validate_certs: false
  tasks:

  - name: get vm information
    vmware_core_info:
      object_type: vm
      filters:
        - names: "some_vm"


Status
------


Authors
~~~~~~~

- Abhijeet Kasurde (Akasurde)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.
