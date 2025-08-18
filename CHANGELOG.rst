==============================
community.vmware Release Notes
==============================

.. contents:: Topics

This changelog describes changes after version 4.7.0.

v5.7.2
======

Bugfixes
--------

- vmware_deploy_ovf - Fix detection of HTTP range support in `WebHandle` to support HTTP/2 endpoints like Nexus that do not return `accept-ranges` header (https://github.com/ansible-collections/community.vmware/pull/2399).
- vmware_guest_file_operation - Fix to use custom port provided to the module (https://github.com/ansible-collections/community.vmware/pull/2397).
- vmware_vm_config_option - change to use 'disk_ctl_device_type' defined in 'device_helper' and add 'support_cpu_hotadd', 'support_memory_hotadd', 'support_for_create' in output. (https://github.com/ansible-collections/community.vmware/pull/2428)

v5.7.1
======

Bugfixes
--------

- Fix issues with pyvmomi 9.0.0.0 (https://github.com/ansible-collections/community.vmware/issues/2414).
- vmware_vmotion - Fix issue with same resource pool name on different clusters (https://github.com/ansible-collections/community.vmware/issues/1719).

v5.7.0
======

Minor Changes
-------------

- vcenter_extension - Stop using ``connect_to_api`` (https://github.com/ansible-collections/community.vmware/pull/2372).
- vmware_guest_cross_vc_clone - Stop using ``connect_to_api`` (https://github.com/ansible-collections/community.vmware/pull/2372).
- vmware_guest_instant_clone - Stop using ``connect_to_api`` (https://github.com/ansible-collections/community.vmware/pull/2372).
- vmware_vm_inventory - Stop using ``connect_to_api`` (https://github.com/ansible-collections/community.vmware/pull/2372).
- vmware_vsan_cluster - Stop using ``connect_to_api`` (https://github.com/ansible-collections/community.vmware/pull/2372).

Deprecated Features
-------------------

- module_utils.vmware - Deprecate ``connect_to_api`` (https://github.com/ansible-collections/community.vmware/pull/2372).
- vmware_guest_powerstate - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2398).

Bugfixes
--------

- vm_device_helper - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_guest_controller - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_guest_disk - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_host_inventory - New option ``enable_backward_compatability`` that can be set to ``false`` to work with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_target_canonical_info - Fix an issue with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).
- vmware_vm_inventory - New option ``enable_backward_compatability`` that can be set to ``false`` to work with ansible-core 2.19 (https://github.com/ansible-collections/community.vmware/pull/2391).

v5.6.0
======

Minor Changes
-------------

- module_utils.vmware - Move ``vmware_argument_spec`` to a dedicated file (https://github.com/ansible-collections/community.vmware/pull/2370).
- module_utils.vmware_rest_client - Move ``vmware_client_argument_spec`` to a dedicated file (https://github.com/ansible-collections/community.vmware/pull/2370).
- vmware_dvs_portgroup - New option ``network_policy.mac_learning`` to replace ``mac_learning`` (https://github.com/ansible-collections/community.vmware/pull/2360).
- vmware_object_role_permission - Document setting permissions on vCenter level (https://github.com/ansible-collections/community.vmware/pull/2374).

Deprecated Features
-------------------

- vmware_dvs_portgroup - ``mac_learning`` is deprecated in favour of ``network_policy.mac_learning`` (https://github.com/ansible-collections/community.vmware/pull/2360).

Bugfixes
--------

- vmware_dvs_portgroup - Fix idempotency issue with ``mac_learning`` (https://github.com/ansible-collections/community.vmware/issues/1873).

v5.5.0
======

Minor Changes
-------------

- vcenter_standard_key_provider - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_category - Don't test for vSphere < 7 anymore (https://github.com/ansible-collections/community.vmware/pull/2326).
- vmware_guest - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_guest_storage_policy - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_guest_tpm - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_host_graphics - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_host_lockdown - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_host_lockdown_exceptions - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_host_snmp - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_migrate_vmk - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_migrate_vmk - Inherit from / sub-class PyVmomi (https://github.com/ansible-collections/community.vmware/pull/2324).
- vmware_resource_pool - Drop unnecessary HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2328).
- vmware_vc_infraprofile_info - Don't test for vSphere < 7 anymore (https://github.com/ansible-collections/community.vmware/pull/2326).
- vmware_vm_config_option - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).
- vmware_vm_vss_dvs_migrate - Inherit from / sub-class PyVmomi (https://github.com/ansible-collections/community.vmware/pull/2325).
- vmware_vsan_health_info - Drop unused HAS_PYVMOMI (https://github.com/ansible-collections/community.vmware/pull/2327).

Deprecated Features
-------------------

- vcenter_folder - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2340).
- vmware_cluster_ha - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2321).
- vmware_content_deploy_ovf_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_deploy_template - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2332).
- vmware_content_library_manager - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2345).
- vmware_host - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2337).

Bugfixes
--------

- vmware_object_role_permission - The module ignores changing ``recursive`` (https://github.com/ansible-collections/community.vmware/pull/2350).

v5.4.0
======

Minor Changes
-------------

- vmware_guest - Print details about the error message when the returned task result contains (https://github.com/ansible-collections/community.vmware/pull/2301).

Deprecated Features
-------------------

- module_utils.vmware - host_version_at_least is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2303).
- plugin_utils.inventory - this plugin util is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2304).
- plugins.httpapi - this is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2306).
- vm_device_helper.py - is_nvdimm_controller is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vm_device_helper.py - is_nvdimm_device is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - find_host_portgroup_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - find_vmdk_file is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - network_exists_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware - vmdk_disk_path_split is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware_host_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).
- vmware_maintenancemode - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2293).
- vmware_rest_client - get_folder_by_name is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2311).
- vmware_vm_inventory - the inventory plugin is deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2283).

v5.3.0
======

Major Changes
-------------

- vmware_dvswitch_pvlans - The VLAN ID type has been updated to be handled as an integer (https://github.com/ansible-collections/community.vmware/pull/2267).

Minor Changes
-------------

- vmware_guest - Add new cutomization spec param `domainOU`. (https://github.com/ansible-collections/community.vmware/issues/2275)
- vmware_guest - Speedup network search (https://github.com/ansible-collections/community.vmware/pull/2278).
- vmware_guest_network - Speedup network search (https://github.com/ansible-collections/community.vmware/pull/2277).

Deprecated Features
-------------------

- vmware_cluster_info - the module has been deprecated and will be removed in community.vmware 7.0.0 (https://github.com/ansible-collections/community.vmware/pull/2260).

Bugfixes
--------

- vmware_guest - setting vApp properties on virtual machines without vApp options raised an AttributeError. Fix now gracefully handles a `None` value for vApp options when retrieving current vApp properties (https://github.com/ansible-collections/community.vmware/pull/2220).

v5.2.0
======

Minor Changes
-------------

- vmware.py - Add logic for handling the case where the `datacenter` property is not provided.
- vmware_guest_info - `datacenter` property is now optional as it only required in cases where the VM is not uniquely identified by `name`.

Bugfixes
--------

- vm_device_helper - Fix 'invalid configuration for device' error caused by missing fileoperation parameter. (https://github.com/ansible-collections/community.vmware/pull/2009).
- vmware_guest - Fix errors occuring during hardware version upgrade not being reported. (https://github.com/ansible-collections/community.vmware/pull/2010).
- vmware_guest - Fix vmware_guest always reporting change when using dvswitch. (https://github.com/ansible-collections/community.vmware/pull/2000).
- vmware_guest_tools_upgrade - Account for all possible tools status (https://github.com/ansible-collections/community.vmware/issues/2237).

New Modules
-----------

- vmware_drs_override - Configure DRS behavior for a specific VM in vSphere

v5.1.0
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

v5.0.1
======

Bugfixes
--------

- vcenter_standard_key_provider - Fix documentation (https://github.com/ansible-collections/community.vmware/pull/2192).
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

v5.0.0
======

Major Changes
-------------

- vmware_guest_tools_upgrade - Subsitute the deprecated ``guest.toolsStatus`` (https://github.com/ansible-collections/community.vmware/pull/2174).
- vmware_vm_shell - Subsitute the deprecated ``guest.toolsStatus`` (https://github.com/ansible-collections/community.vmware/pull/2174).

Breaking Changes / Porting Guide
--------------------------------

- Adding a dependency on the ``vmware.vmware`` collection (https://github.com/ansible-collections/community.vmware/pull/2159).
- Depending on ``vmware-vcenter`` and ``vmware-vapi-common-client`` instead of ``https://github.com/vmware/vsphere-automation-sdk-python.git`` (https://github.com/ansible-collections/community.vmware/pull/2163).
- Dropping support for pyVmomi < 8.0.3.0.1 (https://github.com/ansible-collections/community.vmware/pull/2163).
- Module utils - Removed ``vmware.run_command_in_guest()`` (https://github.com/ansible-collections/community.vmware/pull/2175).
- Removed support for ansible-core version < 2.17.0.
- vmware_dvs_portgroup - Removed ``security_override`` alias for ``mac_management_override`` and support for ``securityPolicyOverrideAllowed`` which has been deprected in the vSphere API (https://github.com/ansible-collections/community.vmware/issues/1998).
- vmware_dvs_portgroup_info - Removed ``security_override`` because it's deprecated in the vSphere API (https://github.com/ansible-collections/community.vmware/issues/1998).
- vmware_guest_tools_info - Removed deprecated ``vm_tools_install_status`` from the result (https://github.com/ansible-collections/community.vmware/issues/2078).

Bugfixes
--------

- vmware_all_snapshots_info - fixed the datacenter parameter was ignored(https://github.com/ansible-collections/community.vmware/pull/2165).
