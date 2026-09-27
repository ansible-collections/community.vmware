==============================
community.vmware Release Notes
==============================

.. contents:: Topics

This changelog describes changes after version 6.5.0.

v7.0.0
======

Breaking Changes / Porting Guide
--------------------------------

- Removed support for ansible-core < 2.21.0.

Removed Features (previously deprecated)
----------------------------------------

- module_utils.vm_device_helper - The deprecated ``PyVmomiDeviceHelper.is_nvdimm_controller`` method has been removed (https://github.com/ansible-collections/community.vmware/pull/2314).
- module_utils.vm_device_helper - The deprecated ``PyVmomiDeviceHelper.is_nvdimm_device`` method has been removed (https://github.com/ansible-collections/community.vmware/pull/2314).
- module_utils.vmware - The deprecated ``PyVmomi.find_vmdk_file`` method has been removed (https://github.com/ansible-collections/community.vmware/pull/2314).
- module_utils.vmware - The deprecated ``PyVmomi.host_version_at_least`` method has been removed (https://github.com/ansible-collections/community.vmware/issues/2309).
- module_utils.vmware - The deprecated ``PyVmomi.network_exists_by_name`` method has been removed (https://github.com/ansible-collections/community.vmware/pull/2314).
- module_utils.vmware - The deprecated ``PyVmomi.vmdk_disk_path_split`` method has been removed (https://github.com/ansible-collections/community.vmware/pull/2314).
- module_utils.vmware - The deprecated ``connect_to_api`` function has been removed. (https://github.com/ansible-collections/community.vmware/issues/2465).
- module_utils.vmware - The deprecated ``find_host_portgroup_by_name`` function and ``PyVmomi.find_host_portgroup_by_name`` method have been removed (https://github.com/ansible-collections/community.vmware/pull/2314).
- module_utils.vmware_rest_client - The deprecated ``VmwareRestClient.get_folder_by_name`` method has been removed (https://github.com/ansible-collections/community.vmware/pull/2314).
- plugin_utils.inventory - The deprecated plugin util has been removed (https://github.com/ansible-collections/community.vmware/issues/2292).
- plugins.httpapi - The deprecated ``plugins.httpapi`` has been removed (https://github.com/ansible-collections/community.vmware/issues/2310).
- vcenter_folder - The deprecated module has been removed. Use ``vmware.vmware.folder`` instead (https://github.com/ansible-collections/community.vmware/issues/2358).
- vmware_cluster_ha - The deprecated module has been removed. Use ``vmware.vmware.cluster_ha`` instead (https://github.com/ansible-collections/community.vmware/issues/2333).
- vmware_cluster_info - The deprecated module has been removed. Use ``vmware.vmware.cluster_info`` instead (https://github.com/ansible-collections/community.vmware/issues/2261).
- vmware_content_deploy_ovf_template - The deprecated module has been removed. Use ``vmware.vmware.deploy_content_library_ovf`` instead (https://github.com/ansible-collections/community.vmware/issues/2334).
- vmware_content_deploy_template - The deprecated module has been removed. Use ``vmware.vmware.deploy_content_library_template`` instead (https://github.com/ansible-collections/community.vmware/issues/2334).
- vmware_content_library_manager - The deprecated module has been removed. Use ``vmware.vmware.local_content_library`` and ``vmware.vmware.subscribed_content_library`` instead (https://github.com/ansible-collections/community.vmware/issues/2359).
- vmware_dvs_portgroup - The deprecated option ``mac_learning`` has been removed. Use ``network_policy.mac_learning`` instead (https://github.com/ansible-collections/community.vmware/issues/2466).
- vmware_guest_powerstate - The deprecated module has been removed. Use ``vmware.vmware.vm_powerstate`` instead (https://github.com/ansible-collections/community.vmware/issues/2440).
- vmware_host - The deprecated module has been removed. Use ``vmware.vmware.esxi_host`` and ``vmware.vmware.esxi_connection`` instead (https://github.com/ansible-collections/community.vmware/issues/2341).
- vmware_host_inventory - The deprecated inventory plugin has been removed. Use ``vmware.vmware.esxi_hosts`` instead (https://github.com/ansible-collections/community.vmware/issues/2292).
- vmware_maintenancemode - The deprecated module has been removed. Use ``vmware.vmware.esxi_maintenance_mode`` instead (https://github.com/ansible-collections/community.vmware/issues/2299).
- vmware_vm_inventory - The deprecated inventory plugin has been removed. Use ``vmware.vmware.vms`` instead (https://github.com/ansible-collections/community.vmware/issues/2292).
