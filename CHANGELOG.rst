==============================
community.vmware Release Notes
==============================

.. contents:: Topics


v3.7.0
======

Minor Changes
-------------

- vmware_cluster_drs_recommendations - Add the Module to apply the drs recommendations (https://github.com/ansible-collections/community.vmware/pull/1736)
- vmware_guest_serial_port - add support for proxyURI parameter to enable use of a virtual serial port concentrator (https://github.com/ansible-collections/community.vmware/issues/1742)

Bugfixes
--------

- Add missing modules to runtime.yml (https://github.com/ansible-collections/community.vmware/pull/1764).
- vmware_vm_info - Add missing show_folder parameter (https://github.com/ansible-collections/community.vmware/issues/1709).

New Modules
-----------

- vmware_cluster_drs_recommendations - Apply DRS Recommendations
- vmware_vsan_release_catalog - Uploads the vSAN Release Catalog

v3.6.0
======

Bugfixes
--------

- vmware_guest - Fixed issue where custom attributes were not getting set on VM creation (https://github.com/ansible-collections/community.vmware/pull/1713)
- vmware_vsan_health_info - Fix return value (https://github.com/ansible-collections/community.vmware/pull/1706).

New Modules
-----------

- vsan_health_silent_checks - Silence vSAN health checks

v3.5.0
======

Major Changes
-------------

- Use true/false (lowercase) for boolean values in documentation and examples (https://github.com/ansible-collections/community.vmware/issues/1660).

Minor Changes
-------------

- vmware_migrate_vmk - Improve error handling (https://github.com/ansible-collections/community.vmware/issues/1118).
- vmware_tag - Allow to use category names for tag management (https://github.com/ansible-collections/community.vmware/issues/1614).
- vmware_tag_manager - Improve performance of tag attachments and detachments (https://github.com/ansible-collections/community.vmware/issues/1603).
- vmware_tools - ansible_vmware_guest_uuid added for easier use of vmware_tools connection plugin with vmware_vm_inventory plugin
- vmware_vm_info - Add several parameters to skip discovering some information (https://github.com/ansible-collections/community.vmware/issues/1682)

Bugfixes
--------

- vmware_cross_vc_clone - Fix SSL Thumbprint validation to ignore if destination_vcenter_validate_certs is false (https://github.com/ansible-collections/community.vmware/issues/1433).
- vmware_guest - Fixes adding new NVDIMM device issue by connecting to ESXi host (https://github.com/ansible-collections/community.vmware/issues/1644).
- vmware_guest_cross_vc_clone - Fix vim.fault.NotAuthenticated issue (https://github.com/ansible-collections/community.vmware/issues/1223).
- vmware_guest_cross_vc_clone - New parameter timeout in order to allow clone running longer than 1 hour
- vmware_tag - Fix a performance issue during tag processing (https://github.com/ansible-collections/community.vmware/issues/1603).

New Modules
-----------

- vmware_vsan_hcl_db - Manages the vSAN Hardware Compatibility List (HCL) database

v3.4.0
======

Minor Changes
-------------

- vmware_guest_disk - Add support for IDE disk add, remove or reconfigure, and change to gather same VM disk info as in vmware_guest_disk_info (https://github.com/ansible-collections/community.vmware/issues/1428).
- vmware_guest_disk - Extend return value documentation for vmware_guest_disk (https://github.com/ansible-collections/community.vmware/pull/1641)
- vmware_guest_disk_info - Move gather VM disk info function to vm_device_helper.py (https://github.com/ansible-collections/community.vmware/issues/1617)
- vmware_vmotion - New parameter timeout in order to allow vmotions running longer than 1 hour (https://github.com/ansible-collections/community.vmware/pulls/1629).

Bugfixes
--------

- scenario guides - Fix broken references (https://github.com/ansible-collections/community.vmware/issues/1610).
- various - Fix new pylint issues (https://github.com/ansible-collections/community.vmware/pull/1637).
- vmware_cluster_info - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch_lacp - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_dvswitch_uplink_pg - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_guest_custom_attributes - Fixes assigning attributes to new VMs (https://github.com/ansible-collections/community.vmware/issues/1606).
- vmware_guest_disk - Fix wrong key in the documentation of the return values (https://github.com/ansible-collections/community.vmware/issues/1615)
- vmware_object_rename - Add missing quotation mark to error message (https://github.com/ansible-collections/community.vmware/issues/1633)
- vmware_portgroup - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_vcenter_settings - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).
- vmware_vcenter_statistics - Fix pylint issues (https://github.com/ansible-collections/community.vmware/issues/1618).

v3.3.0
======

Minor Changes
-------------

- vmware_cluster_drs - Add predictive DRS Setting (https://github.com/ansible-collections/community.vmware/pull/1542).
- vmware_guest_network - Add PVRDMA network adapter type (https://github.com/ansible-collections/community.vmware/pull/1579).

Bugfixes
--------

- vmware_cluster_dpm - Fix an issue that the slider and the values of the host_power_action_rate works invertet in the vCenter
- vmware_cluster_drs - Fix drs_vmotion_rate so that the value corresponds to the vCenter UI. Previously, choosing 1 / 2 configured a migration threshold of 5 / 4 and vice versa (https://github.com/ansible-collections/community.vmware/pull/1542).
- vmware_guest - Fix check mode (https://github.com/ansible-collections/community.vmware/issues/1272).
- vmware_host_lockdown_exceptions - Avoid setting exception users to what they already are (https://github.com/ansible-collections/community.vmware/pull/1585).
- vmware_tools - Fix an issue with pyVmomi 8.0.0.1 (https://github.com/ansible-collections/community.vmware/issues/1578).

New Modules
-----------

- vmware_guest_vgpu_info - Gather information about vGPU profiles of the specified virtual machine in the given vCenter infrastructure

v3.2.0
======

Minor Changes
-------------

- vmware_guest - Add sub-option to configure virtual performance counters (https://github.com/ansible-collections/community.vmware/issues/1511).
- vmware_guest - Adding sub-options to configure CPU and memory shares (https://github.com/ansible-collections/community.vmware/issues/356).
- vmware_guest_boot_manager - Add a new parameter boot_hdd_name to specify the boot disk name(https://github.com/ansible-collections/community.vmware/pull/1543).
- vmware_guest_custom_attributes - Improve the code quality and added the return value for diff(https://github.com/ansible-collections/community.vmware/pull/1532).
- vmware_vm_info - Adding resource pool of the VM to result (https://github.com/ansible-collections/community.vmware/pull/1551).

Bugfixes
--------

- vmware_dvs_portgroup - Fix an issue when deleting portgroups (https://github.com/ansible-collections/community.vmware/issues/1522).
- vmware_guest_instant_clone - Fix an issue with pyVmomi 8.0.0.1 (https://github.com/ansible-collections/community.vmware/issues/1555).
- vmware_host_lockdown - Fix issue `'VmwareLockdownManager' object has no attribute 'warn'` (https://github.com/ansible-collections/community.vmware/pull/1540).
- vmware_object_custom_attributes_info - Fixed an issue that has occurred an error if a custom attribute is the global type(https://github.com/ansible-collections/community.vmware/pull/1541).
- vmware_portgroup_info - Fix an issue that can fail the module after manually updating a portgroup through vCenter (https://github.com/ansible-collections/community.vmware/issues/1544).

New Modules
-----------

- vmware_custom_attribute - Manage custom attributes definitions
- vmware_custom_attribute_manager - Manage custom attributes from VMware for the given vSphere object

v3.1.0
======

Minor Changes
-------------

- vmware_dvs_portgroup - Add deprecaded securityPolicyOverrideAllowed because without it make problems if securityPolicyOverrideAllowed and macManagementOverrideAllowed has not the same value (https://github.com/ansible-collections/community.vmware/pull/1508)
- vmware_guest - Adding `script_text` parameter to execute scripts in Linux guests (https://github.com/ansible-collections/community.vmware/pull/1485).
- vmware_host_lockdown - Add the ability to enable ``strict`` lockdown mode (https://github.com/ansible-collections/community.vmware/pull/1514).
- vmware_host_lockdown - Add two new choices for ``state``, ``disabled`` and ``normal``, to replace ``absent`` and ``present``. Please note that ``absent`` and ``present`` will be removed in the next major release (https://github.com/ansible-collections/community.vmware/pull/1514).
- vmware_host_lockdown - Replace deprecated vSphere API calls (https://github.com/ansible-collections/community.vmware/pull/1514).

Bugfixes
--------

- vmware_guest_file_operation - Add a new parameter for timeout(https://github.com/ansible-collections/community.vmware/pull/1513).
- vmware_tag_manager - Fix a performance issue during tag processing (https://github.com/ansible-collections/community.vmware/issues/1503).
- vmware_tag_manager - Fix an issue that causes a failure when changing a single cardinal tag category (https://github.com/ansible-collections/community.vmware/issues/1501).

New Modules
-----------

- vmware_host_lockdown_exceptions - Manage Lockdown Mode Exception Users

v3.0.0
======

Minor Changes
-------------

- vmware_guest_disk - Adding `iolimit` modifications of an existing disk without changing size (https://github.com/ansible-collections/community.vmware/pull/1466).

Breaking Changes / Porting Guide
--------------------------------

- Removed support for ansible-core version < 2.13.0.
- vmware_dvs_portgroup - Add a new sub-option `inherited` to the `in_traffic_shaping` parameter. This means you can keep the setting as-is by not defining the parameter, but also that you have to define the setting as not `inherited` if you want to override it at the PG level (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup - Add a new sub-option `inherited` to the `out_traffic_shaping` parameter. This means you can keep the setting as-is by not defining the parameter, but also that you have to define the setting as not `inherited` if you want to override it at the PG level (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup - Change the type of `net_flow` to string to allow setting it implicitly to inherited or to keep the value as-is. This means you can keep the setting as-is by not defining the parameter, but also that while `true` or `no` still work, `True` or `Off` (uppercase) won't (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup - Remove support for vSphere API less than 6.7.
- vmware_dvs_portgroup - Remove the default for `network_policy` and add a new sub-option `inherited`. This means you can keep the setting as-is by not defining the parameter, but also that you have to define the setting as not `inherited` if you want to override it at the PG level (https://github.com/ansible-collections/community.vmware/pull/1483).
- vmware_dvs_portgroup_info - Remove support for vSphere API less than 6.7.
- vmware_dvswitch - Remove support for vSphere API less than 6.7.
- vmware_dvswitch_uplink_pg - Remove support for vSphere API less than 6.7.
- vmware_guest_boot_manager - Remove default for ``secure_boot_enabled`` parameter (https://github.com/ansible-collections/community.vmware/issues/1461).
- vmware_vm_config_option - Dict item names in result are changed from strings joined with spaces to strings joined with underlines, e.g. `Guest fullname` is changed to `guest_fullname` (https://github.com/ansible-collections/community.vmware/issues/1268).
- vmware_vspan_session - Remove support for vSphere API less than 6.7.

Removed Features (previously deprecated)
----------------------------------------

- vca_fw - The deprecated module ``vca_fw`` has been removed.
- vca_nat - The deprecated module ``vca_nat`` has been removed.
- vca_vapp - The deprecated module ``vca_vapp`` has been removed.
- vmware_dns_config - The deprecated module ``vmware_dns_config`` has been removed, you can use ``vmware_host_dns`` instead.
- vmware_guest_network - The deprecated parameter ``networks`` has been removed, use loops to handle multiple interfaces (https://github.com/ansible-collections/community.vmware/pull/1459).
- vmware_guest_vnc - The deprecated module ``vmware_guest_vnc`` has been removed. The VNC support has been dropped with vSphere 7 and later (https://github.com/ansible-collections/community.vmware/pull/1454).
- vmware_host_firewall_manager - The module doesn't accept a list for ``allowed_hosts`` anymore, use a dict instead. Additionally, ``all_ip`` is now a required sub-option of ``allowed_hosts`` (https://github.com/ansible-collections/community.vmware/pull/1463).
- vsphere_copy - The deprecated parameters ``host`` and ``login`` have been removed. Use ``hostname`` and ``username`` instead (https://github.com/ansible-collections/community.vmware/pull/1456).

Bugfixes
--------

- vmware_dvs_portgroup - Fix update of NetFlow Setting (https://github.com/ansible-collections/community.vmware/pull/1443).
- vmware_tag_manager - Fix idempotency for state `set` (https://github.com/ansible-collections/community.vmware/issues/1265).

New Modules
-----------

- vmware_datastore - Configure Datastores

v2.9.1
======

Bugfixes
--------

- 2.9.0 wasn't released correctly, some changes are missing from the package. Releasing 2.9.1 to fix this.

v2.9.0
======

Minor Changes
-------------

- vmware_cluster_ha - Add APD settings (https://github.com/ansible-collections/community.vmware/pull/1420).
- vmware_content_library_info - Add Subscribed Libraries (https://github.com/ansible-collections/community.vmware/issues/1430).
- vmware_drs_group_manager - Improve error handling (https://github.com/ansible-collections/community.vmware/pull/1448).

Bugfixes
--------

- vmware_cfg_backup - Fix a bug that failed the restore when port 80 is blocked (https://github.com/ansible-collections/community.vmware/issues/1440).
- vmware_vswitch - Fix broken logic of `failback` parameter (https://github.com/ansible-collections/community.vmware/issues/1431).

v2.8.0
======

Minor Changes
-------------

- vmware_cfg_backup - Improve error message (https://github.com/ansible-collections/community.vmware/pull/1388).
- vmware_dvs_portgroup - Fix a `spec.numPorts is None` issue when the `num_ports` parameter isn't set (https://github.com/ansible-collections/community.vmware/pull/1419).
- vmware_guest_sendkey - Add CTRL_X binding support (https://github.com/ansible-collections/community.vmware/pull/1376).
- vmware_host_vmnic_info - add CDP information to output when applicable (https://github.com/ansible-collections/community.vmware/pull/1418).

Bugfixes
--------

- vmware_cfg_backup - Fix a possible urlopen error when connecting directly to an ESXi host (https://github.com/ansible-collections/community.vmware/issues/1383).
- vmware_guest - Fix no fail attribute issue (https://github.com/ansible-collections/community.vmware/issues/1401).
- vmware_vm_info - Fix 'NoneType' object has no attribute 'datastoreUrl' for inaccessible VMs (https://github.com/ansible-collections/community.vmware/issues/1407).

v2.7.0
======

Minor Changes
-------------

- vmware_dvswitch.py - Add Netflow Settings. (https://github.com/ansible-collections/community.vmware/pull/1352)
- vmware_dvswitch_nioc.py - Add backupNfc and nvmetcp to the resources. (https://github.com/ansible-collections/community.vmware/pull/1351)
- vmware_guest_disk - Add a new disk type to support add/reconfigure/remove vPMem disk (https://github.com/ansible-collections/community.vmware/pull/1382).
- vmware_host_passthrough - Support the PCI id in the devices parameter(https://github.com/ansible-collections/community.vmware/pull/1365).
- vmware_object_role_permission.py - Add StoragePod to the list of object_types. (https://github.com/ansible-collections/community.vmware/pull/1338)
- vmware_object_role_permission_info.py - Add StoragePod and DistributedVirtalPortgroup to the list of object_types. (https://github.com/ansible-collections/community.vmware/pull/1338)

Bugfixes
--------

- vmware_content_deploy_ovf_template - Fixed a bug that ignored `resource_pool` in some cases. (https://github.com/ansible-collections/community.vmware/issues/1290).
- vmware_content_deploy_template - Fixed a bug that ignored `resource_pool` in some cases. (https://github.com/ansible-collections/community.vmware/issues/1290).
- vmware_guest_disk - Ignore datastores in maintenance mode (https://github.com/ansible-collections/community.vmware/pull/1321).
- vmware_guest_instant_clone - Support FQPN in the folder parameter.
- vmware_guest_network - Fix a typo in the code for SR-IOV NICs (https://github.com/ansible-collections/community.vmware/issues/1317).
- vmware_guest_network - Fix an `AttributeError` when using SR-IOV NICs (https://github.com/ansible-collections/community.vmware/issues/1318).

v2.6.0
======

Minor Changes
-------------

- vmware_vmotion - Add the feature to use cluster and datastore cluster (storage pods) to define where the vmotion shold go. (https://github.com/ansible-collections/community.vmware/pull/1240)

Bugfixes
--------

- vmware_cfg_backup - Fix a bug that failed the module when port 80 is blocked (https://github.com/ansible-collections/community.vmware/issues/1270).
- vmware_host_facts - Fix a bug that crashes the module when a host is disconnected (https://github.com/ansible-collections/vmware/issues/184).
- vmware_host_vmnic_info - Fix a bug that crashes the module when a host is disconnected (https://github.com/ansible-collections/community.vmware/pull/1337).

v2.5.0
======

Minor Changes
-------------

- vmware_vm_info - Add the feature to get the output of allocated storage, cpu und memory. (https://github.com/ansible-collections/community.vmware/pull/1283)

New Modules
-----------

- vmware_guest_vgpu - Modify vGPU video card profile of the specified virtual machine in the given vCenter infrastructure

v2.4.0
======

Minor Changes
-------------

- vmware_maintenancemode - Add support for check_mode (https://github.com/ansible-collections/community.vmware/pull/1311).
- vmware_migrate_vmk - Add `migrate_vlan_id` to use for the VMK interface when migrating from VDS to VSS (https://github.com/ansible-collections/community.vmware/issues/1297).
- vmware_vswitch - Add support to manage security, teaming and traffic shaping policies on vSwitches. (https://github.com/ansible-collections/community.vmware/pull/1298).
- vmware_vswitch_info - Add support to return security, teaming and traffic shaping policies on vSwitches. (https://github.com/ansible-collections/community.vmware/pull/1309).

v2.3.0
======

Major Changes
-------------

- Drop VCSIM as a test target (https://github.com/ansible-collections/community.vmware/pull/1294).

Minor Changes
-------------

- vmware_dvs_portgroup - Add the feature to configure ingress and egress traffinc shaping and netflow on the dvs portgroup. (https://github.com/ansible-collections/community.vmware/pull/1224)
- vmware_guest_network - Add parameters `physical_function_backing`, `virtual_function_backing` and `allow_guest_os_mtu_change` (https://github.com/ansible-collections/community.vmware/pull/1218)

Bugfixes
--------

- vmware_dvs_portgroup - Fix an idempotency issue when `num_ports` is unset (https://github.com/ansible-collections/community.vmware/pull/1286).
- vmware_guest_powerstate - Ignore trailing `/` in `folder` parameter like other guest modules do (https://github.com/ansible-collections/community.vmware/issues/1238).
- vmware_host_powerstate - Do not execute the powerstate changes in check_mode. (https://github.com/ansible-collections/community.vmware/pull/1299).
- vmware_vmotion - Like already define in the examples, allow Storage vMotion without defining a resource pool. (https://github.com/ansible-collections/community.vmware/pull/1236).

v2.2.0
======

Minor Changes
-------------

- vmware_vm_info - Add the posibility to get the configuration informations of only one vm by name. (https://github.com/ansible-collections/community.vmware/pull/1241)

Bugfixes
--------

- vmware_dvs_host - match the list of the host nics in the correct order based on the uplink port name in vCenter (https://github.com/ansible-collections/community.vmware/issues/1242).
- vmware_guest_powerstate - `shutdownguest` power state is not idempotent (https://github.com/ansible-collections/community.vmware/pull/1227).

v2.1.0
======

Minor Changes
-------------

- Remove `version_added` documentation that pre-dates the collection, that is refers to Ansible < 2.10 (https://github.com/ansible-collections/community.vmware/pull/1215).
- vmware_guest_storage_policy - New parameter `controller_number` to support multiple SCSI controllers (https://github.com/ansible-collections/community.vmware/issues/1203).
- vmware_object_role_permission - added VMware DV portgroup object_type for setting permissions (https://github.com/ansible-collections/community.vmware/pull/1176)
- vmware_vm_config_option - Fix the parameter not correct issue when hostname is set to ESXi host(https://github.com/ansible-collections/community.vmware/pull/1171).
- vmware_vm_info - adding fact about ``datastore_url`` to output (https://github.com/ansible-collections/community.vmware/pull/1143).

New Modules
-----------

- vmware_host_user_manager - Manage users of ESXi

v2.0.0
======

Minor Changes
-------------

- vmware_export_ovf - Add a new parameter 'export_with_extraconfig' to support export extra config options in ovf (https://github.com/ansible-collections/community.vmware/pull/1161).

Breaking Changes / Porting Guide
--------------------------------

- The collection now requires at least ansible-core 2.11.0. Ansible 3 and before, and ansible-base versions are no longer supported.
- vmware_cluster_drs - The default for ``enable`` has been changed from ``false`` to ``true``.
- vmware_cluster_drs - The parameter alias ``enable_drs`` has been removed, use ``enable`` instead.
- vmware_cluster_ha - The default for ``enable`` has been changed from ``false`` to ``true``.
- vmware_cluster_ha - The parameter alias ``enable_ha`` has been removed, use ``enable`` instead.
- vmware_cluster_vsan - The default for ``enable`` has been changed from ``false`` to ``true``.
- vmware_cluster_vsan - The parameter alias ``enable_vsan`` has been removed, use ``enable`` instead.
- vmware_guest - Virtualization Based Security has some requirements (``nested_virt``, ``secure_boot`` and ``iommu``) that the module silently enabled. They have to be enabled explicitly now.

Removed Features (previously deprecated)
----------------------------------------

- vcenter_extension_facts - The deprecated module ``vcenter_extension_facts`` has been removed, use ``vcenter_extension_info`` instead.
- vmware_about_facts - The deprecated module ``vmware_about_facts`` has been removed, use ``vmware_about_info`` instead.
- vmware_category_facts - The deprecated module ``vmware_category_facts`` has been removed, use ``vmware_category_info`` instead.
- vmware_cluster - Remove DRS configuration in favour of module ``vmware_cluster_drs``.
- vmware_cluster - Remove HA configuration in favour of module ``vmware_cluster_ha``.
- vmware_cluster - Remove VSAN configuration in favour of module ``vmware_cluster_vsan``.
- vmware_cluster_facts - The deprecated module ``vmware_cluster_facts`` has been removed, use ``vmware_cluster_info`` instead.
- vmware_datastore_facts - The deprecated module ``vmware_datastore_facts`` has been removed, use ``vmware_datastore_info`` instead.
- vmware_drs_group_facts - The deprecated module ``vmware_drs_group_facts`` has been removed, use ``vmware_drs_group_info`` instead.
- vmware_drs_rule_facts - The deprecated module ``vmware_drs_rule_facts`` has been removed, use ``vmware_drs_rule_info`` instead.
- vmware_dvs_portgroup - The deprecated parameter ``portgroup_type`` has been removed, use ``port_binding`` instead.
- vmware_dvs_portgroup_facts - The deprecated module ``vmware_dvs_portgroup_facts`` has been removed, use ``vmware_dvs_portgroup_info`` instead.
- vmware_guest_boot_facts - The deprecated module ``vmware_guest_boot_facts`` has been removed, use ``vmware_guest_boot_info`` instead.
- vmware_guest_customization_facts - The deprecated module ``vmware_guest_customization_facts`` has been removed, use ``vmware_guest_customization_info`` instead.
- vmware_guest_disk_facts - The deprecated module ``vmware_guest_disk_facts`` has been removed, use ``vmware_guest_disk_info`` instead.
- vmware_guest_facts - The deprecated module ``vmware_guest_facts`` has been removed, use ``vmware_guest_info`` instead.
- vmware_guest_snapshot_facts - The deprecated module ``vmware_guest_snapshot_facts`` has been removed, use ``vmware_guest_snapshot_info`` instead.
- vmware_host_capability_facts - The deprecated module ``vmware_host_capability_facts`` has been removed, use ``vmware_host_capability_info`` instead.
- vmware_host_config_facts - The deprecated module ``vmware_host_config_facts`` has been removed, use ``vmware_host_config_info`` instead.
- vmware_host_dns_facts - The deprecated module ``vmware_host_dns_facts`` has been removed, use ``vmware_host_dns_info`` instead.
- vmware_host_feature_facts - The deprecated module ``vmware_host_feature_facts`` has been removed, use ``vmware_host_feature_info`` instead.
- vmware_host_firewall_facts - The deprecated module ``vmware_host_firewall_facts`` has been removed, use ``vmware_host_firewall_info`` instead.
- vmware_host_ntp_facts - The deprecated module ``vmware_host_ntp_facts`` has been removed, use ``vmware_host_ntp_info`` instead.
- vmware_host_package_facts - The deprecated module ``vmware_host_package_facts`` has been removed, use ``vmware_host_package_info`` instead.
- vmware_host_service_facts - The deprecated module ``vmware_host_service_facts`` has been removed, use ``vmware_host_service_info`` instead.
- vmware_host_ssl_facts - The deprecated module ``vmware_host_ssl_facts`` has been removed, use ``vmware_host_ssl_info`` instead.
- vmware_host_vmhba_facts - The deprecated module ``vmware_host_vmhba_facts`` has been removed, use ``vmware_host_vmhba_info`` instead.
- vmware_host_vmnic_facts - The deprecated module ``vmware_host_vmnic_facts`` has been removed, use ``vmware_host_vmnic_info`` instead.
- vmware_local_role_facts - The deprecated module ``vmware_local_role_facts`` has been removed, use ``vmware_local_role_info`` instead.
- vmware_local_user_facts - The deprecated module ``vmware_local_user_facts`` has been removed, use ``vmware_local_user_info`` instead.
- vmware_portgroup_facts - The deprecated module ``vmware_portgroup_facts`` has been removed, use ``vmware_portgroup_info`` instead.
- vmware_resource_pool_facts - The deprecated module ``vmware_resource_pool_facts`` has been removed, use ``vmware_resource_pool_info`` instead.
- vmware_tag_facts - The deprecated module ``vmware_tag_facts`` has been removed, use ``vmware_tag_info`` instead.
- vmware_target_canonical_facts - The deprecated module ``vmware_target_canonical_facts`` has been removed, use ``vmware_target_canonical_info`` instead.
- vmware_vm_facts - The deprecated module ``vmware_vm_facts`` has been removed, use ``vmware_vm_info`` instead.
- vmware_vmkernel_facts - The deprecated module ``vmware_vmkernel_facts`` has been removed, use ``vmware_vmkernel_info`` instead.
- vmware_vmkernel_ip_config - The deprecated module ``vmware_vmkernel_ip_config`` has been removed, use ``vmware_vmkernel`` instead.
- vmware_vswitch_facts - The deprecated module ``vmware_vswitch_facts`` has been removed, use ``vmware_vswitch_info`` instead.

Bugfixes
--------

- Various modules and plugins - use vendored version of ``distutils.version`` included in ansible-core 2.12 if available. This avoids breakage when ``distutils`` is removed from the standard library of Python 3.12. Note that ansible-core 2.11, ansible-base 2.10 and Ansible 2.9 are right now not compatible with Python 3.12, hence this fix does not target these ansible-core/-base/2.9 versions.
- create_nic - add advanced SR-IOV options from the VMware API (PCI dev PF/VF backing and guest OS MTU change)
- vcenter_folder - fixed folders search collision issue (https://github.com/ansible-collections/community.vmware/issues/1112).
- vmware_guest_network - fix a bug that can crash the module due to an uncaught exception (https://github.com/ansible-collections/community.vmware/issues/25).

v1.17.0
=======

Minor Changes
-------------

- vmware_datastore_info - added show_tag parameters to allow datastore tags to be read in a uniform way across _info modules  (https://github.com/ansible-collections/community.vmware/pull/1085).
- vmware_guest_disk - Added a new key 'cluster_disk' which allows you to use a filename originating from a VM with an RDM.
- vmware_guest_disk - Added bus_sharing as an option for SCSI devices.
- vmware_guest_disk - Enabled the use of up to 64 disks on a paravirtual SCSI controller when the hardware is version 14 or higher.
- vmware_guest_sendkey - added additional USB scan codes for HOME and END.
- vmware_host_scanhba - add rescan_vmfs parameter to allow rescaning for new VMFS volumes. Also add rescan_hba parameter with default true to allow for not rescaning HBAs as this might be very slow. (https://github.com/ansible-collections/community.vmware/issues/479)
- vmware_host_snmp - implement setting syscontact and syslocation (https://github.com/ansible-collections/community.vmware/issues/1044).
- vmware_rest_client module_util - added function get_tags_for_datastore for convenient tag collection (https://github.com/ansible-collections/community.vmware/pull/1085).

Bugfixes
--------

- vmware_guest - when ``customization.password`` is not defined, the Administrator password is made empty instead of setting it to string 'None' (https://github.com/ansible-collections/community.vmware/issues/1017).

v1.16.0
=======

Minor Changes
-------------

- vmware - add vTPM information to default gather information (https://github.com/ansible-collections/community.vmware/pull/1082).
- vmware_guest_cross_vc_clone - Added the is_template option to mark a cloned vm/template as a template (https://github.com/ansible-collections/community.vmware/pull/996).

Bugfixes
--------

- update_vswitch - add the possibility to remove nics from vswitch (https://github.com/ansible-collections/community.vmware/issues/536)
- vmware_guest_serial_port - handle correct serial backing type (https://github.com/ansible-collections/community.vmware/issues/1043).
- vmware_host_lockdown - Fix an issue when enabling or disabling lockdown mode failes (https://github.com/ansible-collections/community.vmware/issues/1083)

New Modules
-----------

- vmware_guest_tpm - Add or remove vTPM device for specified VM.

v1.15.0
=======

Minor Changes
-------------

- vm_device_helper - move NIC device types from vmware_guest module to vm_device_helper (https://github.com/ansible-collections/community.vmware/pull/998).

Deprecated Features
-------------------

- vmware_guest_vnc -  Sphere 7.0 removed the built-in VNC server (https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-vcenter-server-70-release-notes.html#productsupport).

Bugfixes
--------

- Fix a bug that prevented enabling VSAN on more than one vmk, risking splitting the whole cluster during interface migration scenarios (https://github.com/ansible-collections/community.vmware/issues/891)
- vmware_deploy_ovf - Fix deploy ovf issue when there are more than one datacenter in VC (https://github.com/ansible-collections/community.vmware/issues/164).
- vmware_deploy_ovf - fixed to display suitable the error when not exist an ovf file path (https://github.com/ansible-collections/community.vmware/pull/1065).
- vmware_guest_powerstate - handle 'present' state as 'poweredon' (https://github.com/ansible-collections/community.vmware/pull/1033).
- vmware_guest_tools_wait - add documentation about datacenter parameter (https://github.com/ansible-collections/community.vmware/pull/870).
- vmware_object_rename - fixed an issue that an error has occurred when getting than 1,000 objects (https://github.com/ansible-collections/community.vmware/pull/1010).
- vmware_vcenter_settings_info - fix to return all VCSA settings when setting vsphere to the schema and not specifying the properties (https://github.com/ansible-collections/community.vmware/pull/1050).
- vmware_vm_inventory - remove erroneous ``ansible_host`` condition (https://github.com/ansible-collections/community.vmware/issues/975).

New Modules
-----------

- vmware_vm_config_option - Return supported guest ID list and VM recommended config option for specific guest OS

v1.14.0
=======

Minor Changes
-------------

- vmware_host_service_manager - Introducing a new state "unchanged" to allow defining startup policy without defining service state or automatically starting it (https://github.com/ansible-collections/community.vmware/issues/916).

Bugfixes
--------

- vmware_category - fixed some issues that the errors have occurred in executing the module (https://github.com/ansible-collections/community.vmware/pull/990).
- vmware_guest_network - Fix adding more than one NIC to a VM before powering on (https://github.com/ansible-collections/community.vmware/issues/860).

v1.13.0
=======

Minor Changes
-------------

- vm_device_helper - Add new functions for create, remove or reconfigure virutal NVDIMM device (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware - the scenario guides from Ansible repo migrated to collection repo.
- vmware_guest - Add new parameter 'nvdimm' for add, remove or reconfigure virutal NVDIMM device of virtual machine (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware_guest_disk - add the capability to create and remove RDM disks from Virtual Machines.
- vmware_guest_snapshot_info - add quiesced status in VM snapshot info (https://github.com/ansible-collections/community.vmware/pull/978)
- vmware_host_datastore - added a new parameter to expand a datastore capacity (https://github.com/ansible-collections/community.vmware/pull/915).
- vmware_host_inventory - filter hosts before templating hostnames (https://github.com/ansible-collections/community.vmware/issues/850).
- vmware_portgroup - Disable traffic shaping without defining ``traffic_shaping.average_bandwidth``, ``traffic_shaping.burst_size`` and ``traffic_shaping.peak_bandwidth`` (https://github.com/ansible-collections/community.vmware/issues/955).
- vmware_spbm - Add a new function 'find_storage_profile_by_name' (https://github.com/ansible-collections/community.vmware/issues/853).
- vmware_vm_inventory - filter guests before templating hostnames (https://github.com/ansible-collections/community.vmware/issues/850).

Bugfixes
--------

- vmware - changed to use from isinstance to type in the if condition of option_diff method (https://github.com/ansible-collections/community.vmware/pull/983).
- vmware_guest - add message for `deploy_vm` method when it fails with timeout error while customizing the VM (https://github.com/ansible-collections/community.vmware/pull/933).
- vmware_guest_instant_clone - fixed an issue that the module should be required the guestinfo_vars parameter when executing (https://github.com/ansible-collections/community.vmware/pull/962).
- vmware_guest_powerstate - added the datacenter parameter to fix an issue that datacenter key error has been occurring (https://github.com/ansible-collections/community.vmware/pull/924).
- vmware_host_datastore - fixed an issue that the right error message isn't displayed (https://github.com/ansible-collections/community.vmware/pull/976).

v1.12.0
=======

Minor Changes
-------------

- vmware - add processing to answer if the answer question is occurred in starting the vm (https://github.com/ansible-collections/community.vmware/pull/821).
- vmware - find_folder_by_fqpn added to support specifying folders by their fully qualified path name, defined as I(datacenter)/I(folder_type)/subfolder1/subfolder2/.
- vmware - folder field default changed from None to vm.
- vmware_content_deploy_ovf_template - storage_provisioning default changed from None to thin, in keeping with VMware best practices for flash storage.
- vmware_dvs_host - implement adding pNICs to LAGs (https://github.com/ansible-collections/community.vmware/issues/112).
- vmware_guest_instant_clone - added a new option to wait until the vmware tools start (https://github.com/ansible-collections/community.vmware/pull/904).
- vmware_guest_instant_clone - added a reboot processing to reflect the customization parameters to an instant clone vm (https://github.com/ansible-collections/community.vmware/pull/904).
- vmware_guest_powerstate - Add an option that answers whether it was copied or moved the vm if the vm is blocked (https://github.com/ansible-collections/community.vmware/pull/821).
- vmware_host_inventory - support api access via proxy (https://github.com/ansible-collections/community.vmware/pull/817).
- vmware_object_role_permission_info - added principal to provide list of individual permissions on specified entity (https://github.com/ansible-collections/community.vmware/issues/868).
- vmware_rest_client - support proxy feature for module using this API (https://github.com/ansible-collections/community.vmware/pull/848).
- vmware_vm_inventory - support api access via proxy (https://github.com/ansible-collections/community.vmware/pull/817).

Bugfixes
--------

- vmware_content_deploy_ovf_template - no longer requires host, datastore, resource_pool.
- vmware_content_deploy_xxx - deploys to recommended datastore in specified datastore_cluster.
- vmware_content_deploy_xxx - honors folder specified by fully qualified path name.
- vmware_guest - Use hostname parameter in customization only if value is not None (https://github.com/ansible-collections/community.vmware/issues/655)

v1.11.0
=======

Major Changes
-------------

- vmware_object_custom_attributes_info - added a new module to gather custom attributes of an object (https://github.com/ansible-collections/community.vmware/pull/851).

Minor Changes
-------------

- vmware - added a new method to search Managed Object based on moid and object type (https://github.com/ansible-collections/community.vmware/pull/879).
- vmware_dvswitch - Dynamically check the DVS versions vCenter supports (https://github.com/ansible-collections/community.vmware/issues/839).
- vmware_dvswitch - Implement network_policy parameter with suboptions promiscuous, forged_transmits and mac_changes (https://github.com/ansible-collections/community.vmware/issues/833).
- vmware_guest - Make the requirements for Virtualization Based Security explicit (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest - New parameter ``secure_boot`` to manage (U)EFI secure boot on VMs (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest - New parameter ``vvtd`` to manage Intel Virtualization Technology for Directed I/O on VMs (https://github.com/ansible-collections/community.vmware/pull/816).
- vmware_guest_controller - added bus_sharing property to scsi controllers (https://github.com/ansible-collections/community.vmware/pull/878).
- vmware_guest_instant_clone - added the the guestinfo_vars parameter to provide GuestOS Customization functionality in instant cloned VM (https://github.com/ansible-collections/community.vmware/pull/796).
- vmware_host_custom_attributes - new module (https://github.com/ansible-collections/community.vmware/pull/838).
- vmware_host_inventory - added ability for username to be a vault encrypted variable, and updated documentation to reflect ability for username and password to be vaulted. (https://github.com/ansible-collections/community.vmware/issues/854).
- vmware_host_passthrough - added a new module to enable or disable passthrough of PCI devices with ESXi host has (https://github.com/ansible-collections/community.vmware/pull/872).
- vmware_host_tcpip_stacks - added ipv6_gateway parameter and nsx_overlay as an alias of vxlan (https://github.com/ansible-collections/community.vmware/pull/834).
- vmware_host_vmnic_info - add LLDP information to output when applicable (https://github.com/ansible-collections/community.vmware/pull/828).
- vmware_object_custom_attributes_info - added a new parameter to support moid (https://github.com/ansible-collections/community.vmware/pull/879).
- vmware_vcenter_settings.py - Add advanced_settings parameter (https://github.com/ansible-collections/community.vmware/pull/819).
- vmware_vm_inventory - added ability for username to be a vault encrypted variable, and updated documentation to reflect ability for username and password to be vaulted. (https://github.com/ansible-collections/community.vmware/issues/854).

Bugfixes
--------

- vmware - fix that the return value should be returned None if moId doesn't exist of a virtual machine (https://github.com/ansible-collections/community.vmware/pull/867).
- vmware_vmotion - implement new parameter named destination_datacenter to fix failure to move storage when datastores are shared across datacenters (https://github.com/ansible-collections/community.vmware/issues/858)

New Plugins
-----------

Inventory
~~~~~~~~~

- vmware_host_inventory - VMware ESXi hostsystem inventory source

New Modules
-----------

- vmware_host_custom_attributes - Manage custom attributes from VMware for the given ESXi host
- vmware_host_passthrough - Manage PCI device passthrough settings on host
- vmware_object_custom_attributes_info - Gather custom attributes of an object
- vmware_object_role_permission_info - Gather information about object's permissions
- vmware_recommended_datastore - Returns the recommended datastore from a SDRS-enabled datastore cluster

v1.10.0
=======

Minor Changes
-------------

- vmware_cluster_drs - Make enable_drs an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_ha - Make enable_ha an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_cluster_vsan - Make enable_vsan an alias of enable and add a warning that the default will change from false to true in a future version (https://github.com/ansible-collections/community.vmware/pull/766)
- vmware_dvs_portgroup - Implement 'elastic' port group configuration (https://github.com/ansible-collections/community.vmware/issues/410).
- vmware_dvs_portgroup - Implement MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup - Implement configuration of active and standby uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_dvs_portgroup - Remove default for teaming_policy.inbound_policy (https://github.com/ansible-collections/community.vmware/pull/743).
- vmware_dvs_portgroup_info - Return information about MAC learning configuration (https://github.com/ansible-collections/community.vmware/issues/644).
- vmware_dvs_portgroup_info - Return information about uplinks (https://github.com/ansible-collections/community.vmware/issues/709).
- vmware_guest - add more documentation about ``is_template`` (https://github.com/ansible-collections/community.vmware/pull/794).
- vmware_host_iscsi_info - added a list(detected_iscsi_drives) of detected iscsi drives to the return value after set an iscsi config (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_tag - modified the category_id parameter to required (https://github.com/ansible-collections/community.vmware/pull/790).
- vmware_vm_inventory - set default to ``True`` for ``with_nested_properties`` (https://github.com/ansible-collections/community.vmware/issues/712).

Bugfixes
--------

- vmware - fixed a bug that the guest_guestion in the facts doesn't convert to the dictionary (https://github.com/ansible-collections/community.vmware/pull/825).
- vmware - handle exception raised in ``get_all_objs`` and ``find_object_by_name`` which occurs due to multiple parallel operations (https://github.com/ansible-collections/community.vmware/issues/791).
- vmware_cluster_info - Fix a bug that returned enabled_vsan and vsan_auto_claim_storage as lists instead of just true or false (https://github.com/ansible-collections/community.vmware/issues/805).
- vmware_evc_mode - fixed an issue that evc_mode is required when the state parameter set to absent (https://github.com/ansible-collections/community.vmware/pull/764).
- vmware_guest - skip customvalues while deploying VM on a standalone ESXi (https://github.com/ansible-collections/community.vmware/issues/721).
- vmware_host_iscsi_info - fixed an issue that an error occurs gathering iSCSI information against an ESXi Host with iSCSI disabled (https://github.com/ansible-collections/community.vmware/pull/729).
- vmware_vm_info - handle vApp parent logic (https://github.com/ansible-collections/community.vmware/issues/777).
- vmware_vm_shell - handle exception raised while performing the operation (https://github.com/ansible-collections/community.vmware/issues/732).
- vmware_vm_storage_policy_info - fixed an issue that the module can't get storage policy info when the policy has the tag base rules (https://github.com/ansible-collections/community.vmware/pull/788).
- vmware_vmotion - Provide an meaningful error message when providing a bad ESXi node as ``destination_host`` (https://github.com/ansible-collections/vmware/pull/804).

New Modules
-----------

- vmware_host_tcpip_stacks - Manage the TCP/IP Stacks configuration of ESXi host

v1.9.0
======

Minor Changes
-------------

- vmware_guest_instant_clone - supported esxi_hostname parameter as an alias (https://github.com/ansible-collections/community.vmware/pull/745).
- vmware_resource_pool - Add parent_resource_pool parameter which is mutually exclusive with cluster and esxi_hostname (https://github.com/ansible-collections/community.vmware/issues/717)
- vmware_vm_inventory - add an example of FQDN as hostname (https://github.com/ansible-collections/community.vmware/issues/678).
- vmware_vm_inventory - skip disconnected VMs.

Deprecated Features
-------------------

- vmware_vmkernel_ip_config - deprecate in favor of vmware_vmkernel (https://github.com/ansible-collections/community.vmware/pull/667).

Security Fixes
--------------

- vmware_host_iscsi - mark the ``chap_secret`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_host_iscsi - mark the ``mutual_chap_secret`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_vc_infraprofile_info - mark the ``decryption_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).
- vmware_vc_infraprofile_info - mark the ``encryption_key`` parameter as ``no_log`` to avoid accidental leaking of secrets in logs (https://github.com/ansible-collections/community.vmware/pull/715).

Bugfixes
--------

- vmware - add the default value of parameter resource_pool_name in the find_resource_pool_by_name function (https://github.com/ansible-collections/community.vmware/pull/670).
- vmware_cluster_vsan - fixed a bug that made the module fail when advanced_options is not set (https://github.com/ansible-collections/community.vmware/issues/728).
- vmware_deploy_ovf - fixed an issue that a return value hasn't the instance key when the power_on parameter is False (https://github.com/ansible-collections/community.vmware/pull/698).
- vmware_deploy_ovf - fixed an issue that deploy template in datacenter with more than one standalone hosts (https://github.com/ansible-collections/community.vmware/pull/670).
- vmware_guest - fixed a bug that made the module fail when disk.controller_number or disk.unit_number are 0 (https://github.com/ansible-collections/community.vmware/issues/703).
- vmware_local_user_manager - fixed to require local_user_password when the state is present (https://github.com/ansible-collections/community.vmware/pull/724).
- vmware_vm_inventory - Skip over ghost tags attached to virtual machines (https://github.com/ansible-collections/community.vmware/issues/681).

New Modules
-----------

- vmware_guest_instant_clone - Instant Clone VM
- vmware_guest_storage_policy - Set VM Home and disk(s) storage policy profiles.

v1.8.0
======

Minor Changes
-------------

- Define sub-options of disk in argument_spec (https://github.com/ansible-collections/community.vmware/pull/640).
- vmware_guest - Remove unnecessary hardware version check (https://github.com/ansible-collections/community.vmware/issues/636).
- vmware_vcenter_settings - supported the diff mode (https://github.com/ansible-collections/community.vmware/pull/641).

Bugfixes
--------

- vcenter_license - fixed a bug that the license doesn't assign in VCSA 7.0u1c (https://github.com/ansible-collections/community.vmware/pull/643).
- vmware - fixed an issue that a port group name doesn't compare correctly in the find_network_by_name function (https://github.com/ansible-collections/community.vmware/pull/661).
- vmware_category - append namespace to associable types (https://github.com/ansible-collections/community.vmware/issues/579).
- vmware_cluster_ha - fix enabling APD or PDL response (https://github.com/ansible-collections/community.vmware/issues/676).
- vmware_cluster_info - return VSAN status correctly (https://github.com/ansible-collections/community.vmware/issues/673).
- vmware_deploy_ovf - fixed an issue that an error message doesn't show when not finding a port group name (https://github.com/ansible-collections/community.vmware/pull/661).
- vmware_dvs_portgroup - fixed the issue that the VLAN configuration isn't compared correctly in the module (https://github.com/ansible-collections/community.vmware/pull/638).
- vmware_dvs_portgroup_find - fixed to decode the special characters URL-encoded in the dvs port group name (https://github.com/ansible-collections/community.vmware/pull/648).
- vmware_dvs_portgroup_info - fixed to decode the special characters URL-encoded in the dvs port group name (https://github.com/ansible-collections/community.vmware/pull/648).
- vmware_guest - add support for ``advanced settings`` in vmware_guest (https://github.com/ansible-collections/community.vmware/issues/602).
- vmware_guest_register_operation - fixed an issue that an error has been occurring when not specifying a datacenter name (https://github.com/ansible-collections/community.vmware/pull/693).
- vmware_vm_storage_policy - fixed an issue that an error for pyvmomi(SDK) occurred when a tag or category doesn't exist (https://github.com/ansible-collections/community.vmware/pull/682).

v1.7.0
======

Minor Changes
-------------

- vmware_cluster_info - added a parent datacenter name of Cluster to the return value (https://github.com/ansible-collections/community.vmware/pull/591).
- vmware_content_deploy_ovf_template - consistent ``eagerZeroedThick`` value (https://github.com/ansible-collections/community.vmware/issues/618).
- vmware_content_deploy_template - add datastore cluster parameter (https://github.com/ansible-collections/community.vmware/issues/397).
- vmware_content_deploy_template - make resource pool, host, cluster, datastore optional parameter and add check (https://github.com/ansible-collections/community.vmware/issues/397).
- vmware_guest - Define sub-options of hardware and customization in argument_spec (https://github.com/ansible-collections/community.vmware/issues/555).
- vmware_guest_register_operation - supported the check_mode
- vmware_host_iscsi - added a name(iqn) changing option for iSCSI (https://github.com/ansible-collections/community.vmware/pull/617).
- vmware_host_lockdown - Support check mode (https://github.com/ansible-collections/community.vmware/pull/633).

Deprecated Features
-------------------

- vmware_host_firewall_manager - the creation of new rule with no ``allowed_ip`` entry in the ``allowed_hosts`` dictionary won't be allowed after 2.0.0 release.

Bugfixes
--------

- vmware_content_library_manager - added support for subscribed library (https://github.com/ansible-collections/community.vmware/pull/569).
- vmware_datastore_cluster_manager - Fix idempotency in check mode (https://github.com/ansible-collections/community.vmware/issues/623).
- vmware_dvswitch - correctly add contact information (https://github.com/ansible-collections/community.vmware/issues/608).
- vmware_dvswitch_lacp - typecast uplink number in lag_options (https://github.com/ansible-collections/community.vmware/issues/111).
- vmware_guest - handle NoneType values before passing to ``len`` API (https://github.com/ansible-collections/community.vmware/issues/593).

New Modules
-----------

- vmware_drs_group_manager - Manage VMs and Hosts in DRS group.
- vmware_first_class_disk - Manage VMware vSphere First Class Disks

v1.6.0
======

Minor Changes
-------------

- vmware_guest_disk - add new parameters controller_type and controller_number for supporting SATA and NVMe disk (https://github.com/ansible-collections/vmware/issues/196).
- vmware_guest_file_operation - provide useful error message when exception occurs (https://github.com/ansible-collections/community.vmware/issues/485).
- vmware_guest_network - add support for private vlan id (https://github.com/ansible-collections/community.vmware/pull/511).
- vmware_host - added a new state option, the ``disconnected`` (https://github.com/ansible-collections/community.vmware/pull/589).
- vmware_host_facts - Add ESXi host current time info in returned host facts(https://github.com/ansible-collections/community.vmware/issues/527)
- vmware_vsan_health_info - add new parameter to support datacenter.

Bugfixes
--------

- Fix remove hosts from cluster to use cluster name variable
- Fix vSwitch0 default port group removal to run against all hosts
- For vSphere 7.0u1, add steps to tests to remove vCLS VMs before removing datastore
- vmware_cluster - consider datacenter name while creating cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_cluster_drs - consider datacenter name while managing cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_cluster_ha - consider datacenter name while managing cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_cluster_vsan - consider datacenter name while managing cluster (https://github.com/ansible-collections/community.vmware/issues/575).
- vmware_dvswitch - fix an issue with vSphere 7 when no switch_version is defined (https://github.com/ansible-collections/community.vmware/issues/576)
- vmware_guest - fix an issue with vSphere 7 when adding several virtual disks and / or vNICs (https://github.com/ansible-collections/community.vmware/issues/545)
- vmware_guest - handle computer name in existing VM customization (https://github.com/ansible-collections/community.vmware/issues/570).
- vmware_guest_disk - fix an issue with vSphere 7 when adding several virtual disks and (https://github.com/ansible-collections/community.vmware/issues/373)
- vmware_host_logbundle - handle fetch_url status before attempting to read response.
- vmware_host_ntp - fix an issue with disconnected hosts (https://github.com/ansible-collections/community.vmware/issues/539)
- vsphere_copy - handle unboundlocalerror when timeout occurs (https://github.com/ansible-collections/community.vmware/issues/554).

New Modules
-----------

- vcenter_domain_user_group_info - Gather user or group information of a domain

v1.5.1
======

Minor Changes
-------------

- vmware_resource_pool - relabel the change introduced in 1.5.0 as Minor Changes (https://github.com/ansible-collections/community.vmware/issues/540).

v1.5.0
======

Minor Changes
-------------

- vmware_content_deploy_ovf_template - added new parameter "content_library" to get the OVF template from (https://github.com/ansible-collections/community.vmware/issues/514).
- vmware_drs_group - code refactor (https://github.com/ansible-collections/community.vmware/pull/475).
- vmware_guest - add documentation for networks parameters connected and start_connected (https://github.com/ansible-collections/community.vmware/issues/507).
- vmware_guest_controller - error handling in task exception.
- vmware_resource_pool - manage resource pools on ESXi hosts (https://github.com/ansible-collections/community.vmware/issues/492).
- vmware_vm_inventory - skip inaccessible vm configuration.

Bugfixes
--------

- vmware_cluster_ha - added APD and PDL configuration (https://github.com/ansible-collections/community.vmware/issues/451).
- vmware_deploy_ovf - fixed an UnboundLocalError for variable 'name' in check mode (https://github.com/ansible-collections/community.vmware/pull/499).
- vmware_object_role_permission - add support for role name presented in vSphere Web UI (https://github.com/ansible-collections/community.vmware/issues/436).

v1.4.0
======

Minor Changes
-------------

- vmware_category - add additional associable object types (https://github.com/ansible-collections/community.vmware/issues/454).
- vmware_dvswitch - Added support to create vds version 7.0.0.
- vmware_guest - Fixed issue of checking hardware version when set VBS(https://github.com/ansible-collections/community.vmware/issues/351)
- vmware_guest - Fixed issue of comparing latest hardware version str type with int(https://github.com/ansible-collections/community.vmware/issues/381)
- vmware_guest_info - added a new parameter to gather detailed information about tag from the given virtual machine.
- vmware_guest_video - gather facts for video devices even if the virtual machine is poweredoff (https://github.com/ansible-collections/community.vmware/issues/408).
- vmware_object_role_permission - add missing required fields of hostname, username, and password to module examples (https://github.com/ansible-collections/community.vmware/issues/426).
- vmware_resource_pool - add new allocation shares options for cpu and memory(https://github.com/ansible-collections/community.vmware/pull/461).
- vmware_vm_inventory - support for categories and tag, category relation (https://github.com/ansible-collections/community.vmware/issues/350).

Bugfixes
--------

- Fixed the find_obj method in the ``module_utils/vmware.py`` to handle an object name using special characters that URL-decoded(https://github.com/ansible-collections/community.vmware/pull/460).
- vmware_cluster_info - return tag related information (https://github.com/ansible-collections/community.vmware/issues/453).
- vmware_deploy_ovf - fixed network mapping in multi-datacenter environments
- vmware_folder_info - added the flat_folder_info in the return value.
- vmware_guest_sendkey - add sleep_time parameter to add delay in-between keys sent (https://github.com/ansible-collections/community.vmware/issues/404).
- vmware_resource_pool - added a changing feature of resource pool config (https://github.com/ansible-collections/community.vmware/pull/469).
- vmware_resource_pool - fixed that always updates occur bug on vCenter Server even when not changing resource pool config (https://github.com/ansible-collections/community.vmware/pull/482).
- vmware_tag_manager - added new parameter 'moid' to identify VMware object to tag (https://github.com/ansible-collections/community.vmware/issues/430).
- vmware_vm_info - added the moid information in the return value.
- vmware_vm_inventory - ensure self.port is integer (https://github.com/ansible-collections/community.vmware/issues/488).
- vmware_vm_inventory - improve plugin performance (https://github.com/ansible-collections/community.vmware/issues/434).
- vmware_vm_vm_drs_rule - report changes in check mode (https://github.com/ansible-collections/community.vmware/issues/440).

v1.3.0
======

Minor Changes
-------------

- module_utils/vmware - Ignore leading and trailing whitespace when searching for objects (https://github.com/ansible-collections/vmware/issues/335)
- vmware_cluster_info - Fixed issue of a cluster name doesn't URL-decode(https://github.com/ansible-collections/vmware/pull/366)
- vmware_guest - takes now into account the ``esxi_hostname`` argument to create the vm on the right host according to the doc (https://github.com/ansible-collections/vmware/pull/359).
- vmware_guest_custom_attributes - Fixed issue when trying to set a VM custom attribute when there are custom attributes with the same name for other object types (https://github.com/ansible-collections/community.vmware/issues/412).
- vmware_guest_customization_info - Fixed to get values properly for LinuxPrep and SysPrep parameters(https://github.com/ansible-collections/vmware/pull/368)
- vmware_guest_info - Fix get tags API call (https://github.com/ansible-collections/community.vmware/issues/403).
- vmware_guest_network - Fixed to port group changes to work properly and NSX-T port group supported(https://github.com/ansible-collections/community.vmware/pull/401).
- vmware_host_iscsi_info - a new module for the ESXi hosts that is dedicated to gathering information of the iSCSI configuration(https://github.com/ansible-collections/community.vmware/pull/402).
- vmware_vm_inventory - update requirements doc.

Bugfixes
--------

- ``module_utils/vmware.py`` handles an object name using special characters that URL-decoded(https://github.com/ansible-collections/vmware/pull/380).

v1.2.0
======

Minor Changes
-------------

- vmware_cluster_ha - treat truthy advanced options ('true', 'false') as strings instead of booleans (https://github.com/ansible-collections/vmware/issues/286).
- vmware_cluster_vsan - implement advanced VSAN options (https://github.com/ansible-collections/vmware/issues/260).
- vmware_cluster_vsan - requires the vSAN Management SDK, which needs to be downloaded from VMware and installed manually.
- vmware_content_deploy_ovf_template - requires the resource_pool parameter.
- vmware_guest_disk - add backing_uuid value to return (https://github.com/ansible-collections/vmware/pull/348).
- vmware_guest_serial_port - ensure we can run the module two times in a row without unexpected side effect(https://github.com/ansible-collections/vmware/pull/358).

Deprecated Features
-------------------

- vmware_guest - deprecate specifying CDROM configuration as a dict, instead use a list.

Bugfixes
--------

- vmware_content_deploy_ovf_template - fixed issue where wrong resource pool identifier was returned when same resource pool name was used across clusters in the same datacenter (https://github.com/ansible-collections/vmware/pull/363)
- vmware_vmkernel - fixed issue where Repl and ReplNFC services were not being identified as enabled on a vmk interface (https://github.com/ansible-collections/vmware/issues/362).

v1.1.0
======

Minor Changes
-------------

- Added module to be able to create, update, or delete VMware VM storage policies for virtual machines.
- vmware_cluster_info - added ``properties`` and ``schema`` options and supported the getting of clusters resource summary information.
- vmware_content_deploy_ovf_template - handle exception while deploying VM using OVF template.
- vmware_content_deploy_template - handle exception while deploying VM (https://github.com/ansible-collections/vmware/issues/182).
- vmware_dvs_portgroup - Added support for distributed port group with private VLAN.
- vmware_guest_snapshot_info - Document that `folder` is required if the VM `name` is defined (https://github.com/ansible-collections/vmware/issues/243)
- vmware_host_iscsi - a new module for the ESXi hosts that is dedicated to the management of the iSCSI configuration
- vmware_migrate_vmk - allow migration from a VMware vSphere Distrubuted Switch to a ESXi Standard Switch
- vmware_vcenter_settings_info - a new module for gather information about vCenter settings

Breaking Changes / Porting Guide
--------------------------------

- vmware_datastore_maintenancemode - now returns ``datastore_status`` instead of Ansible internal key ``results``.
- vmware_guest_custom_attributes - does not require VM name which was a required parameter for releases prior to Ansible 2.10.
- vmware_guest_find - the ``datacenter`` option has been removed.
- vmware_host_kernel_manager - now returns ``host_kernel_status`` instead of Ansible internal key ``results``.
- vmware_host_ntp - now returns ``host_ntp_status`` instead of Ansible internal key ``results``.
- vmware_host_service_manager - now returns ``host_service_status`` instead of Ansible internal key ``results``.
- vmware_tag - now returns ``tag_status`` instead of Ansible internal key ``results``.
- vmware_vmkernel - the options ``ip_address`` and ``subnet_mask`` have been removed; use the suboptions ``ip_address`` and ``subnet_mask`` of the ``network`` option instead.

Deprecated Features
-------------------

- The vmware_dns_config module has been deprecated and will be removed in a later release; use vmware_host_dns instead.
- vca - vca_fw, vca_nat, vca_app are deprecated since these modules rely on deprecated part of Pyvcloud library.
- vmware_tag_info - in a later release, the module will not return ``tag_facts`` since it does not return multiple tags with the same name and different category id. To maintain the existing behavior use ``tag_info`` which is a list of tag metadata.

Removed Features (previously deprecated)
----------------------------------------

- vmware_portgroup - removed 'inbound_policy', and 'rolling_order' deprecated options.

Bugfixes
--------

- vmware_content_deploy_ovf_template - use datastore_id in deployment_spec (https://github.com/ansible-collections/vmware/pull/287).
- vmware_dvs_portgroup_find - Fix comparison between str and int on method vlan_match (https://github.com/ansible-collections/vmware/pull/52).
- vmware_guest - cdrom.controller_number, cdrom.unit_number are handled as integer. (https://github.com/ansible-collections/vmware/issues/274).
- vmware_vm_inventory - CustomFieldManager is not present in ESXi, handle this condition (https://github.com/ansible-collections/vmware/issues/269).

v1.0.0
======

Minor Changes
-------------

- A `vmware` module_defaults group has been added to simplify parameters for multiple VMware tasks. This group includes all VMware modules.
- Add a flag 'force_upgrade' to force VMware tools upgrade installation (https://github.com/ansible-collections/vmware/issues/75).
- Add powerstates to match vmware_guest_powerstate module with vmware_guest (https://github.com/ansible/ansible/issues/55653).
- Added a timeout parameter `wait_for_ip_address_timeout` for `wait_for_ip_address` for longer-running tasks in vmware_guest.
- Added missing backing_disk_mode information about disk which was removed by mistake in vmware_guest_disk_info.
- Correct datatype for state in vmware_host_lockdown module.
- Correct example from doc of `vmware_local_role_info.py` to match the change of returned structure.
- Correct example from doc of `vmware_local_role_info.py` to match the change of returned structure.
- Handle exceptions raised in connect_to_vsphere_client API.
- Minor typo fixes in vmware_httpapi related modules and module_utils.
- Removed ANSIBLE_METADATA from all the modules.
- Return additional information about hosts inside the cluster using vmware_cluster_info.
- Update Module examples with FQCN.
- Update README.md for installing any third party required Python libraries using pip (https://github.com/ansible-collections/vmware/issues/154).
- add storage_provisioning type into vmware_content_deploy_ovf_template.
- add vmware_content_deploy_ovf_template module for creating VMs from OVF templates
- new code module for new feature for operations of VCenter infra profile config.
- vmware.py - Only add configured network interfaces to facts.
- vmware_cluster_drs - Implemented DRS advanced settings (https://github.com/ansible/ansible/issues/66217)
- vmware_cluster_ha - Implemented HA advanced settings (https://github.com/ansible/ansible/issues/61421)
- vmware_cluster_ha - Remove a wrong parameter from an example in the documentation.
- vmware_content_deploy_template - added new field "content_library" to search template inside the specified content library.
- vmware_datastore_cluster - Added basic SDRS configuration (https://github.com/ansible/ansible/issues/65154).
- vmware_datastore_info - added ``properties`` and ``schema`` options.
- vmware_datastore_maintenancemode now returns datastore_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_dvs_portgroup_info - Include the value of the Portgroup ``key`` in the result
- vmware_dvswitch now returns the UUID of the switch
- vmware_dvswitch_info also returns the switch UUID
- vmware_export_ovf - increase default timeout to 30s
- vmware_export_ovf - timeout value is actually in seconds, not minutes
- vmware_guest - Don't search for VMDK if filename is defined.
- vmware_guest - Extracts repeated code from configure_vapp_properties() to set_vapp_properties() in vmware_guest.py.
- vmware_guest - add support VM creation and reconfiguration with multiple types of disk controllers and disks
- vmware_guest - add support for create and reconfigure CDROMs attaching to SATA (https://github.com/ansible/ansible/issues/42995)
- vmware_guest - add support hardware version 17 for vSphere 7.0
- vmware_guest_custom_attributes does not require VM name (https://github.com/ansible/ansible/issues/63222).
- vmware_guest_disk - Add `destroy` option which allows to remove a disk without deleting the VMDK file.
- vmware_guest_disk - Add `filename` option which allows to create a disk from an existing VMDK.
- vmware_guest_disk - add support for setting the sharing/multi-writer mode of virtual disks (https://github.com/ansible-collections/vmware/issues/212)
- vmware_guest_network - network adapters can be configured without lists
- vmware_guest_network - network_info returns a list of dictionaries for ease of use
- vmware_guest_network - put deprecation warning for the networks parameter
- vmware_guest_tools_wait now exposes a ``timeout`` parameter that allow the user to adjust the timeout (second).
- vmware_host_active_directory - Fail when there are unrecoverable problems with AD membership instead of reporting a change that doesn't take place (https://github.com/ansible-collections/vmware/issues/59).
- vmware_host_dns - New module replacing vmware_dns_config with increased functionality.
- vmware_host_dns can now set the following empty values, ``domain``, ``search_domains`` and ``dns_servers``.
- vmware_host_facts - added ``properties`` and ``schema`` options.
- vmware_host_firewall_manager - ``allowed_hosts`` excpects a dict as parameter, list is deprecated
- vmware_host_kernel_manager now returns host_kernel_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_host_logbundle - new code module for a new feature for ESXi support log bundle download operation
- vmware_host_logbundle_info - new code module for a new feature for getting manifests  for ESXi support log bundle
- vmware_host_ntp now returns host_ntp_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_host_service_manager now returns host_service_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_rest_client - Added a new definition get_library_item_from_content_library_name.
- vmware_tag now returns tag_status instead of Ansible internal key results (https://github.com/ansible/ansible/issues/62083).
- vmware_vm_inventory inventory plugin, raise more descriptive error when all template strings in ``hostnames`` fail.

Deprecated Features
-------------------

- vmware_dns_config - Deprecate in favour of new module vmware_host_dns.

Removed Features (previously deprecated)
----------------------------------------

- vmware_guest_find - Removed deprecated ``datacenter`` option
- vmware_vmkernel - Removed deprecated ``ip_address`` option; use sub-option ip_address in the network option instead
- vmware_vmkernel - Removed deprecated ``subnet_mask`` option; use sub-option subnet_mask in the network option instead

Bugfixes
--------

- Added 'compose' and 'groups' feature in vmware_vm_inventory plugin.
- Added keyed_groups feature in vmware_vm_inventory plugin.
- Added support to vmware_tag_manager module for specifying tag and category as dict if any of the name contains colon (https://github.com/ansible/ansible/issues/65765).
- Check for virtualNicManager in Esxi host system before accessing properties in vmware_vmkernel_info (https://github.com/ansible/ansible/issues/62772).
- Fixed typo in vmware_guest_powerstate module (https://github.com/ansible/ansible/issues/65161).
- Handle Base64 Binary while JSON serialization in vmware_vm_inventory.
- Handle NoneType error when accessing service system info in vmware_host_service_info module (https://github.com/ansible/ansible/issues/67615).
- Handle list items in vSphere schema while handling facts using to_json API (https://github.com/ansible-collections/vmware/issues/33).
- Handle multiple tags name with different category id in vmware_tag module (https://github.com/ansible/ansible/issues/66340).
- Handle slashes in VMware network name (https://github.com/ansible/ansible/issues/64399).
- In inventory plugin, serialize properties user specifies which are objects as dicts (https://github.com/ansible-collections/vmware/pull/58).
- In vmware_guest_network module use appropriate network while creating or reconfiguring (https://github.com/ansible/ansible/issues/65968).
- Made vmnics attributes optional when creating DVS as they are optional on the API and GUI as well.
- VMware Guest Inventory plugin enhancements and features.
- VMware guest inventory plugin support for filters.
- Vmware Fix for Create overwrites a VM of same name even when the folder is different(https://github.com/ansible/ansible/issues/43161)
- `vmware_content_deploy_template`'s `cluster` argument no longer fails with an error message about resource pools.
- return correct datastore cluster placement recommendations during when adding disk using the vmware_guest_disk module
- vmware - Ensure we can use the modules with Python < 2.7.9 or RHEL/CentOS < 7.4, this as soon as ``validate_certs`` is disabled.
- vmware_category - fix associable datatypes (https://github.com/ansible-collections/vmware/issues/197).
- vmware_content_deploy_template - Added param content_library to the main function
- vmware_deploy_ovf - Fixed ova deploy error occur if vm exists
- vmware_dvs_portgroup - Implemented configuration changes on an existing Distributed vSwitch portgroup.
- vmware_dvs_portgroup_find - Cast variable to integer for comparison.
- vmware_guest - Add ability to upgrade the guest hardware version to latest fix issue (https://github.com/ansible/ansible/issues/56273).
- vmware_guest - Allow '-' (Dash) special char in windows DNS name.
- vmware_guest - Exclude dvswitch_name from triggering guest os customization.
- vmware_guest - Updated reference link to vapp_properties property
- vmware_host_capability_facts - Fixed vSphere API legacy version errors occur in pyvmomi 7.0 and later
- vmware_host_capability_info - Fixed vSphere API legacy version errors occur in pyvmomi 7.0 and later
- vmware_host_facts - handle facts when ESXi hostsystem is poweredoff (https://github.com/ansible-collections/vmware/issues/183).
- vmware_host_firewall_manager - Ensure we can set rule with no ``allowed_hosts`` key (https://github.com/ansible/ansible/issues/61332)
- vmware_host_firewall_manager - Fixed creating IP specific firewall rules with Python 2 (https://github.com/ansible/ansible/issues/67303)
- vmware_host_vmhba_info - fixed node_wwn and port_wwn for FC HBA to hexadecimal format(https://github.com/ansible/ansible/issues/63045).
- vmware_vcenter_settings - Fixed when runtime_settings parameters not defined occur error(https://github.com/ansible/ansible/issues/66713)
- vmware_vcenter_statistics - Fix some corner cases like increasing some interval and decreasing another at the same time.
- vmware_vm_inventory inventory plugin, use the port value while connecting to vCenter (https://github.com/ansible/ansible/issues/64096).
- vmware_vmkernel - Remove duplicate checks.
- vmware_vspan_session - Extract repeated code and reduce complexity of function.
