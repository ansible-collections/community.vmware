==============================
community.vmware Release Notes
==============================

.. contents:: Topics


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
