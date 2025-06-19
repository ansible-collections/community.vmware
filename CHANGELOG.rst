==============================
community.vmware Release Notes
==============================

.. contents:: Topics

This changelog describes changes after version 3.9.0.

v4.8.5
======

Bugfixes
--------

- Restrict pyvmomi to compatible versions (https://github.com/ansible-collections/community.vmware/pull/2415).
- vmware_vmotion - Fix issue with same resource pool name on different clusters (https://github.com/ansible-collections/community.vmware/issues/1719).

v4.8.4
======

Bugfixes
--------

- vm_device_helper - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_guest_controller - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_guest_disk - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_host_inventory - New option ``enable_backward_compatability`` that can be set to ``false`` to work with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_target_canonical_info - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_vm_inventory - New option ``enable_backward_compatability`` that can be set to ``false`` to work with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).

v4.8.3
======

Deprecated Features
-------------------

- vcenter_folder - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2340).
- vmware_cluster_ha - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2321).
- vmware_content_deploy_ovf_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_deploy_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_library_manager - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2345).
- vmware_host - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2337).
- vmware_host_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).
- vmware_maintenancemode - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2293).
- vmware_vm_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).

Bugfixes
--------

- vmware_guest - setting vApp properties on virtual machines without vApp options raised an AttributeError. Fix now gracefully handles a `None` value for vApp options when retrieving current vApp properties (https://github.com/ansible-collections/community.vmware/pull/2220).
- vmware_object_role_permission - The module ignores changing ``recursive`` (https://github.com/ansible-collections/community.vmware/pull/2350).

v4.8.2
======

Deprecated Features
-------------------

- vmware_cluster_info - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2260).

v4.8.1
======

Bugfixes
--------

- vm_device_helper - Fix 'invalid configuration for device' error caused by missing fileoperation parameter. (https://github.com/ansible-collections/community.vmware/pull/2009).
- vmware_guest - Fix errors occuring during hardware version upgrade not being reported. (https://github.com/ansible-collections/community.vmware/pull/2010).
- vmware_guest - Fix vmware_guest always reporting change when using dvswitch. (https://github.com/ansible-collections/community.vmware/pull/2000).

v4.8.0
======

Minor Changes
-------------

- vmware_vm_info - Improve performance when parsing custom attributes information (https://github.com/ansible-collections/community.vmware/pull/2194)

Deprecated Features
-------------------

- vmware_cluster_dpm - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2217).
- vmware_cluster_drs_recommendations - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2218).

Bugfixes
--------

- vmware_guest - Fix existing disk erroneously being re-created when modifying vm with 8 or more disks. (https://github.com/ansible-collections/community.vmware/pull/2173).
- vmware_vmotion - Fix a `list index out of range` error when vSphere doesn't provide a placement recommendation (https://github.com/ansible-collections/community.vmware/pull/2208).

v4.7.1
======

Bugfixes
--------

- vcenter_standard_key_provider - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_all_snapshots_info - fixed the datacenter parameter was ignored(https://github.com/ansible-collections/community.vmware/pull/2165).
- vmware_dvswitch - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_dvswitch_nioc - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_dvswitch_pvlans - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_guest - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_controller - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_disk - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_serial_port - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_guest_tpm - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_dns - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_inventory - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_host_powerstate - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_tools - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
- vmware_vm_inventory - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).
- vmware_vmotion - Fix Pylint issue (https://github.com/ansible-collections/community.vmware/pull/2186).

v4.7.0
======

Deprecated Features
-------------------

- vmware_cluster - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2143).
- vmware_cluster_vcls - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2156).

v4.6.0
======

Minor Changes
-------------

- vmware_vm_vm_drs_rule - added datacenter argument to correctly deal with multiple clusters with same name(https://github.com/ansible-collections/community.vmware/issues/2101).
- vsphere_file - Fix examples in documentation (https://github.com/ansible-collections/community.vmware/issues/2110).

Deprecated Features
-------------------

- vmware_cluster_drs - the module has been deprecated and will be removed in community.vmware 6.0.0 (https://github.com/ansible-collections/community.vmware/pull/2136).

Bugfixes
--------

- Document dependency on requests (https://github.com/ansible-collections/community.vmware/issues/2127).
- vmware_guest_disk - round size to int, supporting float values properly (https://github.com/ansible-collections/community.vmware/issues/123).
- vmware_guest_snapshot - Update documentation regarding snapshot_id parameter (https://github.com/ansible-collections/community.vmware/issues/2145).

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
