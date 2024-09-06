==============================
community.vmware Release Notes
==============================

.. contents:: Topics

This changelog describes changes after version 3.9.0.

v4.5.0
======

Minor Changes
-------------

- vmware_host_logbundle - Add timeout parameter (https://github.com/ansible-collections/community.vmware/pull/2092).

Bugfixes
--------

- vcenter_folder - removed documentation that incorrectly said `folder_type` had no effect when `parent_folder` was set
- vmware_cluster_vcls - fixed bug caused by pyvmomi >=7.0.3 returning the vlcs cluster config attribute as None when it was previously undefined. Now if the vCLS config is not initialized on the cluster, the module will initialize it using the user's desired state.
- vmware_host_logbundle - Manifests previously was separared by "&", thus selecting first manifest. Fix now separates manifests with URL encoded space, thus correctly supplying the manifests.  (https://github.com/ansible-collections/community.vmware/pull/2090).

v4.4.0
======

Minor Changes
-------------

- vmware_dvs_portgroup - Make `state` default to `present` instead of having it as a required parameter (https://github.com/ansible-collections/community.vmware/pull/2055).

Bugfixes
--------

- Clarify pyVmomi requirement (https://github.com/ansible-collections/community.vmware/pull/2071).
- vmware_cluster_dpm - Handle case where DPM config has not been initialized yet and is None (https://github.com/ansible-collections/community.vmware/pull/2057).
- vmware_dvs_portgroup - Fix erroneously reporting a change when `port_binding` is static and `num_ports` not specified (https://github.com/ansible-collections/community.vmware/pull/2053).

v4.3.0
======

Minor Changes
-------------

- Document that all parameters and VMware object names are case sensitive (https://github.com/ansible-collections/community.vmware/issues/2019).
- Drop the outdated (and actually unmaintained) scenario guides (https://github.com/ansible-collections/community.vmware/pull/2022).
- vmware_dvswitch - Add switchIpAddress/switch_ip parameter for netflow config
- vmware_guest_tools_info - Use `toolsVersionStatus2` instead of `toolsVersionStatus` (https://github.com/ansible-collections/community.vmware/issues/2033).

Deprecated Features
-------------------

- vmware_guest_tools_info - `vm_tools_install_status` will be removed from next major version (5.0.0) of the collection since the API call that provides this information has been deprecated by VMware. Use `vm_tools_running_status` / `vm_tools_version_status` instead (https://github.com/ansible-collections/community.vmware/issues/2033).

Bugfixes
--------

- Use `isinstance()` instead of `type()` for a typecheck (https://github.com/ansible-collections/community.vmware/pull/2011).
- vmware_guest - Fix a error while updating the VM by adding a new disk. While adding a disk to an  existing VM, it leaves it in invalid state. (https://github.com/ansible-collections/community.vmware/pull/2044).
- vmware_guest - Fix a missing error message while setting a template parameter with inconsistency guest_os ID (https://github.com/ansible-collections/community.vmware/pull/2036).

v4.2.0
======

Minor Changes
-------------

- Add standard function vmware_argument_spec() from module_utils for using default env fallback function. https://github.com/ansible-collections/community.vmware/issues/1977
- vmware_first_class_disk_info - Add a module to gather informations about first class disks. (https://github.com/ansible-collections/community.vmware/pull/1996). (https://github.com/ansible-collections/community.vmware/issues/1988).
- vmware_host_facts - Add the possibility to get the related datacenter. (https://github.com/ansible-collections/community.vmware/pull/1994).
- vmware_vm_inventory - Add parameter `subproperties` (https://github.com/ansible-collections/community.vmware/pull/1972).
- vmware_vmkernel - Add the function to set the enable_backup_nfc setting (https://github.com/ansible-collections/community.vmware/pull/1978)
- vsphere_copy - Add parameter to tell vsphere_copy which diskformat is being uploaded (https://github.com/ansible-collections/community.vmware/pull/1995).

v4.1.0
======

Minor Changes
-------------

- vmware_guest - Add IPv6 support for VM network interfaces (https://github.com/ansible-collections/community.vmware/pull/1937).
- vmware_guest_sendkey - Add Windows key (https://github.com/ansible-collections/community.vmware/issues/1959).
- vmware_guest_tools_upgrade - Add parameter `installer_options` to pass command line options to the installer to modify the installation procedure for tools (https://github.com/ansible-collections/community.vmware/pull/1059).

Bugfixes
--------

- Fix InsecureRequestWarning for modules based on the VmwareRestClient module util when setting ``validate_certs`` to ``False`` (https://github.com/ansible-collections/community.vmware/pull/1969).
- module_utils/vmware.py - remove ssl.wrap_socet() function. Replaced for code based on ssl.get_server_certificate (https://github.com/ansible-collections/community.vmware/issues/1930).
- vmware_guest - Fix failure of vm reconfiguration with enabled virt_based_security (https://github.com/ansible-collections/community.vmware/pull/1848).

v4.0.1
======

Bugfixes
--------

- vmware_vm_info - Fix an AttributeError when gathering network information (https://github.com/ansible-collections/community.vmware/pull/1919).

v4.0.0
======

Minor Changes
-------------

- Removed module / plugin documentation RST files from the repository (https://github.com/ansible-collections/community.vmware/pull/1897).
- Using semantic markup in documentation (https://github.com/ansible-collections/community.vmware/issues/1771).
- vmware_deploy_ovf - New parameter enable_hidden_properties to force OVF properties marked as `ovf:userConfigurable=false` to become user configurable (https://github.com/ansible-collections/community.vmware/issues/802).
- vmware_dvs_portgroup_info - add moid property in the return value for the module (https://github.com/ansible-collections/community.vmware/issues/1849).
- vmware_guest_snapshot - add new snapshot_id option (https://github.com/ansible-collections/community.vmware/pull/1847).
- vmware_host_snmp module now can configure SNMP agent on set of hosts (list in esxi_hostname parameter or as cluster in cluster_name parameter). The ability to configure the host directly remains (https://github.com/ansible-collections/community.vmware/issues/1799).

Breaking Changes / Porting Guide
--------------------------------

- Removed support for ansible-core version < 2.15.0.
- vmware_dvs_host - removed defaults for `vmnics` and `lag_uplinks` (https://github.com/ansible-collections/community.vmware/issues/1516).
- vmware_host_acceptance - removed `acceptance_level` and used its options in `state`. This also means there will be no state `list` anymore. In order to get information about the current acceptance level, use the new module `vmware_host_acceptance_info` (https://github.com/ansible-collections/community.vmware/issues/1872).
- vmware_vm_info - added prefix length to IP addresses in vm_network, so they now show up as for example 10.76.33.228/24 instead of just 10.76.33.228 (https://github.com/ansible-collections/community.vmware/issues/1761).

Removed Features (previously deprecated)
----------------------------------------

- Removed module util `version` (https://github.com/ansible-collections/community.vmware/issues/1639).
- vmware_guest - removed specifying CDROM configuration as a dict, instead use a list (https://github.com/ansible-collections/community.vmware/issues/1472).
- vmware_host_lockdown - removed deprecated states `absent` and `present` (https://github.com/ansible-collections/community.vmware/issues/1517).
- vmware_rest_client - removed deprecated method `get_tag_by_category()` (https://github.com/ansible-collections/community.vmware/issues/1898).

Bugfixes
--------

- vmware_deploy_ovf - fix error in finding networks part of code (https://github.com/ansible-collections/community.vmware/issues/1853).
- vmware_guest_custom_attributes - fix problem when module try apply non global or non VM type custom attribute to VM object (https://github.com/ansible-collections/community.vmware/issues/1772).
