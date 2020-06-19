# Ansible Collection: community.vmware

This repo hosts the `community.vmware` Ansible Collection.

The collection includes the VMware modules and plugins supported by Ansible VMware community to help the management of VMware infrastructure.


## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using the VMware community collection, you need to install the collection with the `ansible-galaxy` CLI:

    ansible-galaxy collection install community.vmware

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: community.vmware
```

### Required Python libraries

VMware community collection depends upon following third party libraries:

* [`Pyvmomi`](https://github.com/vmware/pyvmomi)
* [`vSphere Automation SDK for Python`](https://github.com/vmware/vsphere-automation-sdk-python/)

### Installing required libraries and SDK

Installing collection does not install any required third party Python libraries or SDKs. You need to install the required Python libraries using following command:

    pip install -r ~/.ansible/collections/ansible_collections/community/vmware/requirements.txt

If you are working on developing and/or testing VMware community collection, you may want to install additional requirements using following command:

    pip install -r ~/.ansible/collections/ansible_collections/community/vmware/test-requirements.txt


## Included content
<!--start collection content-->
### Connection plugins
Name | Description
--- | ---
[community.vmware.vmware_tools](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_tools.rst)|Execute tasks inside a VM via VMware Tools
### Httpapi plugins
Name | Description
--- | ---
[community.vmware.vmware](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware.rst)|HttpApi Plugin for VMware REST API
### Modules
Name | Description
--- | ---
[community.vmware.vca_fw](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vca_fw.rst)|add remove firewall rules in a gateway  in a vca
[community.vmware.vca_nat](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vca_nat.rst)|add remove nat rules in a gateway  in a vca
[community.vmware.vca_vapp](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vca_vapp.rst)|Manages vCloud Air vApp instances.
[community.vmware.vcenter_extension](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vcenter_extension.rst)|Register/deregister vCenter Extensions
[community.vmware.vcenter_extension_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vcenter_extension_facts.rst)|Gather facts vCenter extensions
[community.vmware.vcenter_extension_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vcenter_extension_info.rst)|Gather info vCenter extensions
[community.vmware.vcenter_folder](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vcenter_folder.rst)|Manage folders on given datacenter
[community.vmware.vcenter_license](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vcenter_license.rst)|Manage VMware vCenter license keys
[community.vmware.vmware_about_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_about_facts.rst)|Provides information about VMware server to which user is connecting to
[community.vmware.vmware_about_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_about_info.rst)|Provides information about VMware server to which user is connecting to
[community.vmware.vmware_category](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_category.rst)|Manage VMware categories
[community.vmware.vmware_category_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_category_facts.rst)|Gather facts about VMware tag categories
[community.vmware.vmware_category_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_category_info.rst)|Gather info about VMware tag categories
[community.vmware.vmware_cfg_backup](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_cfg_backup.rst)|Backup / Restore / Reset ESXi host configuration
[community.vmware.vmware_cluster](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_cluster.rst)|Manage VMware vSphere clusters
[community.vmware.vmware_cluster_drs](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_cluster_drs.rst)|Manage Distributed Resource Scheduler (DRS) on VMware vSphere clusters
[community.vmware.vmware_cluster_ha](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_cluster_ha.rst)|Manage High Availability (HA) on VMware vSphere clusters
[community.vmware.vmware_cluster_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_cluster_info.rst)|Gather info about clusters available in given vCenter
[community.vmware.vmware_cluster_vsan](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_cluster_vsan.rst)|Manages virtual storage area network (vSAN) configuration on VMware vSphere clusters
[community.vmware.vmware_content_deploy_ovf_template](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_content_deploy_ovf_template.rst)|Deploy Virtual Machine from ovf template stored in content library.
[community.vmware.vmware_content_deploy_template](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_content_deploy_template.rst)|Deploy Virtual Machine from template stored in content library.
[community.vmware.vmware_content_library_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_content_library_info.rst)|Gather information about VMWare Content Library
[community.vmware.vmware_content_library_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_content_library_manager.rst)|Create, update and delete VMware content library
[community.vmware.vmware_datacenter](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_datacenter.rst)|Manage VMware vSphere Datacenters
[community.vmware.vmware_datacenter_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_datacenter_info.rst)|Gather information about VMware vSphere Datacenters
[community.vmware.vmware_datastore_cluster](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_datastore_cluster.rst)|Manage VMware vSphere datastore clusters
[community.vmware.vmware_datastore_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_datastore_info.rst)|Gather info about datastores available in given vCenter
[community.vmware.vmware_datastore_maintenancemode](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_datastore_maintenancemode.rst)|Place a datastore into maintenance mode
[community.vmware.vmware_deploy_ovf](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_deploy_ovf.rst)|Deploys a VMware virtual machine from an OVF or OVA file
[community.vmware.vmware_dns_config](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dns_config.rst)|Manage VMware ESXi DNS Configuration
[community.vmware.vmware_drs_group](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_drs_group.rst)|Creates vm/host group in a given cluster.
[community.vmware.vmware_drs_group_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_drs_group_facts.rst)|Gathers facts about DRS VM/Host groups on the given cluster
[community.vmware.vmware_drs_group_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_drs_group_info.rst)|Gathers info about DRS VM/Host groups on the given cluster
[community.vmware.vmware_drs_rule_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_drs_rule_facts.rst)|Gathers facts about DRS rule on the given cluster
[community.vmware.vmware_drs_rule_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_drs_rule_info.rst)|Gathers info about DRS rule on the given cluster
[community.vmware.vmware_dvs_host](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvs_host.rst)|Add or remove a host from distributed virtual switch
[community.vmware.vmware_dvs_portgroup](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvs_portgroup.rst)|Create or remove a Distributed vSwitch portgroup.
[community.vmware.vmware_dvs_portgroup_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvs_portgroup_facts.rst)|Gathers facts DVS portgroup configurations
[community.vmware.vmware_dvs_portgroup_find](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvs_portgroup_find.rst)|Find portgroup(s) in a VMware environment
[community.vmware.vmware_dvs_portgroup_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvs_portgroup_info.rst)|Gathers info DVS portgroup configurations
[community.vmware.vmware_dvswitch](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvswitch.rst)|Create or remove a Distributed Switch
[community.vmware.vmware_dvswitch_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvswitch_info.rst)|Gathers info dvswitch configurations
[community.vmware.vmware_dvswitch_lacp](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvswitch_lacp.rst)|Manage LACP configuration on a Distributed Switch
[community.vmware.vmware_dvswitch_nioc](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvswitch_nioc.rst)|Manage distributed switch Network IO Control
[community.vmware.vmware_dvswitch_pvlans](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvswitch_pvlans.rst)|Manage Private VLAN configuration of a Distributed Switch
[community.vmware.vmware_dvswitch_uplink_pg](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_dvswitch_uplink_pg.rst)|Manage uplink portproup configuration of a Distributed Switch
[community.vmware.vmware_evc_mode](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_evc_mode.rst)|Enable/Disable EVC mode on vCenter
[community.vmware.vmware_export_ovf](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_export_ovf.rst)|Exports a VMware virtual machine to an OVF file, device files and a manifest file
[community.vmware.vmware_folder_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_folder_info.rst)|Provides information about folders in a datacenter
[community.vmware.vmware_guest](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest.rst)|Manages virtual machines in vCenter
[community.vmware.vmware_guest_boot_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_boot_facts.rst)|Gather facts about boot options for the given virtual machine
[community.vmware.vmware_guest_boot_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_boot_info.rst)|Gather info about boot options for the given virtual machine
[community.vmware.vmware_guest_boot_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_boot_manager.rst)|Manage boot options for the given virtual machine
[community.vmware.vmware_guest_controller](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_controller.rst)|Manage disk or USB controllers related to virtual machine in given vCenter infrastructure
[community.vmware.vmware_guest_cross_vc_clone](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_cross_vc_clone.rst)|Cross-vCenter VM/template clone
[community.vmware.vmware_guest_custom_attribute_defs](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_custom_attribute_defs.rst)|Manage custom attributes definitions for virtual machine from VMware
[community.vmware.vmware_guest_custom_attributes](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_custom_attributes.rst)|Manage custom attributes from VMware for the given virtual machine
[community.vmware.vmware_guest_customization_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_customization_facts.rst)|Gather facts about VM customization specifications
[community.vmware.vmware_guest_customization_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_customization_info.rst)|Gather info about VM customization specifications
[community.vmware.vmware_guest_disk](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_disk.rst)|Manage disks related to virtual machine in given vCenter infrastructure
[community.vmware.vmware_guest_disk_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_disk_facts.rst)|Gather facts about disks of given virtual machine
[community.vmware.vmware_guest_disk_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_disk_info.rst)|Gather info about disks of given virtual machine
[community.vmware.vmware_guest_file_operation](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_file_operation.rst)|Files operation in a VMware guest operating system without network
[community.vmware.vmware_guest_find](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_find.rst)|Find the folder path(s) for a virtual machine by name or UUID
[community.vmware.vmware_guest_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_info.rst)|Gather info about a single VM
[community.vmware.vmware_guest_move](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_move.rst)|Moves virtual machines in vCenter
[community.vmware.vmware_guest_network](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_network.rst)|Manage network adapters of specified virtual machine in given vCenter infrastructure
[community.vmware.vmware_guest_powerstate](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_powerstate.rst)|Manages power states of virtual machines in vCenter
[community.vmware.vmware_guest_register_operation](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_register_operation.rst)|VM inventory registration operation
[community.vmware.vmware_guest_screenshot](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_screenshot.rst)|Create a screenshot of the Virtual Machine console.
[community.vmware.vmware_guest_sendkey](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_sendkey.rst)|Send USB HID codes to the Virtual Machine's keyboard.
[community.vmware.vmware_guest_serial_port](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_serial_port.rst)|Manage serial ports on an existing VM
[community.vmware.vmware_guest_snapshot](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_snapshot.rst)|Manages virtual machines snapshots in vCenter
[community.vmware.vmware_guest_snapshot_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_snapshot_info.rst)|Gather info about virtual machine's snapshots in vCenter
[community.vmware.vmware_guest_tools_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_tools_info.rst)|Gather info about VMware tools installed in VM
[community.vmware.vmware_guest_tools_upgrade](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_tools_upgrade.rst)|Module to upgrade VMTools
[community.vmware.vmware_guest_tools_wait](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_tools_wait.rst)|Wait for VMware tools to become available
[community.vmware.vmware_guest_video](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_video.rst)|Modify video card configurations of specified virtual machine in given vCenter infrastructure
[community.vmware.vmware_guest_vnc](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_guest_vnc.rst)|Manages VNC remote display on virtual machines in vCenter
[community.vmware.vmware_host](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host.rst)|Add, remove, or move an ESXi host to, from, or within vCenter
[community.vmware.vmware_host_acceptance](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_acceptance.rst)|Manage the host acceptance level of an ESXi host
[community.vmware.vmware_host_active_directory](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_active_directory.rst)|Joins an ESXi host system to an Active Directory domain or leaves it
[community.vmware.vmware_host_auto_start](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_auto_start.rst)|Manage the auto power ON or OFF for vm on ESXi host
[community.vmware.vmware_host_capability_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_capability_facts.rst)|Gathers facts about an ESXi host's capability information
[community.vmware.vmware_host_capability_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_capability_info.rst)|Gathers info about an ESXi host's capability information
[community.vmware.vmware_host_config_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_config_facts.rst)|Gathers facts about an ESXi host's advance configuration information
[community.vmware.vmware_host_config_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_config_info.rst)|Gathers info about an ESXi host's advance configuration information
[community.vmware.vmware_host_config_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_config_manager.rst)|Manage advanced system settings of an ESXi host
[community.vmware.vmware_host_datastore](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_datastore.rst)|Manage a datastore on ESXi host
[community.vmware.vmware_host_dns](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_dns.rst)|Manage DNS configuration of an ESXi host system
[community.vmware.vmware_host_dns_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_dns_facts.rst)|Gathers facts about an ESXi host's DNS configuration information
[community.vmware.vmware_host_dns_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_dns_info.rst)|Gathers info about an ESXi host's DNS configuration information
[community.vmware.vmware_host_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_facts.rst)|Gathers facts about remote ESXi hostsystem
[community.vmware.vmware_host_feature_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_feature_facts.rst)|Gathers facts about an ESXi host's feature capability information
[community.vmware.vmware_host_feature_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_feature_info.rst)|Gathers info about an ESXi host's feature capability information
[community.vmware.vmware_host_firewall_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_firewall_facts.rst)|Gathers facts about an ESXi host's firewall configuration information
[community.vmware.vmware_host_firewall_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_firewall_info.rst)|Gathers info about an ESXi host's firewall configuration information
[community.vmware.vmware_host_firewall_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_firewall_manager.rst)|Manage firewall configurations about an ESXi host
[community.vmware.vmware_host_hyperthreading](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_hyperthreading.rst)|Enables/Disables Hyperthreading optimization for an ESXi host system
[community.vmware.vmware_host_ipv6](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_ipv6.rst)|Enables/Disables IPv6 support for an ESXi host system
[community.vmware.vmware_host_kernel_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_kernel_manager.rst)|Manage kernel module options on ESXi hosts
[community.vmware.vmware_host_lockdown](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_lockdown.rst)|Manage administrator permission for the local administrative account for the ESXi host
[community.vmware.vmware_host_logbundle](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_logbundle.rst)|Fetch logbundle file from ESXi
[community.vmware.vmware_host_logbundle_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_logbundle_info.rst)|Gathers manifest info for logbundle
[community.vmware.vmware_host_ntp](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_ntp.rst)|Manage NTP server configuration of an ESXi host
[community.vmware.vmware_host_ntp_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_ntp_facts.rst)|Gathers facts about NTP configuration on an ESXi host
[community.vmware.vmware_host_ntp_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_ntp_info.rst)|Gathers info about NTP configuration on an ESXi host
[community.vmware.vmware_host_package_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_package_facts.rst)|Gathers facts about available packages on an ESXi host
[community.vmware.vmware_host_package_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_package_info.rst)|Gathers info about available packages on an ESXi host
[community.vmware.vmware_host_powermgmt_policy](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_powermgmt_policy.rst)|Manages the Power Management Policy of an ESXI host system
[community.vmware.vmware_host_powerstate](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_powerstate.rst)|Manages power states of host systems in vCenter
[community.vmware.vmware_host_scanhba](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_scanhba.rst)|Rescan host HBA's and optionally refresh the storage system
[community.vmware.vmware_host_service_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_service_facts.rst)|Gathers facts about an ESXi host's services
[community.vmware.vmware_host_service_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_service_info.rst)|Gathers info about an ESXi host's services
[community.vmware.vmware_host_service_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_service_manager.rst)|Manage services on a given ESXi host
[community.vmware.vmware_host_snmp](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_snmp.rst)|Configures SNMP on an ESXi host system
[community.vmware.vmware_host_ssl_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_ssl_facts.rst)|Gather facts of ESXi host system about SSL
[community.vmware.vmware_host_ssl_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_ssl_info.rst)|Gather info of ESXi host system about SSL
[community.vmware.vmware_host_vmhba_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_vmhba_facts.rst)|Gathers facts about vmhbas available on the given ESXi host
[community.vmware.vmware_host_vmhba_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_vmhba_info.rst)|Gathers info about vmhbas available on the given ESXi host
[community.vmware.vmware_host_vmnic_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_vmnic_facts.rst)|Gathers facts about vmnics available on the given ESXi host
[community.vmware.vmware_host_vmnic_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_host_vmnic_info.rst)|Gathers info about vmnics available on the given ESXi host
[community.vmware.vmware_local_role_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_local_role_facts.rst)|Gather facts about local roles on an ESXi host
[community.vmware.vmware_local_role_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_local_role_info.rst)|Gather info about local roles on an ESXi host
[community.vmware.vmware_local_role_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_local_role_manager.rst)|Manage local roles on an ESXi host
[community.vmware.vmware_local_user_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_local_user_facts.rst)|Gather facts about users on the given ESXi host
[community.vmware.vmware_local_user_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_local_user_info.rst)|Gather info about users on the given ESXi host
[community.vmware.vmware_local_user_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_local_user_manager.rst)|Manage local users on an ESXi host
[community.vmware.vmware_maintenancemode](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_maintenancemode.rst)|Place a host into maintenance mode
[community.vmware.vmware_migrate_vmk](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_migrate_vmk.rst)|Migrate a VMK interface from VSS to VDS
[community.vmware.vmware_object_role_permission](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_object_role_permission.rst)|Manage local roles on an ESXi host
[community.vmware.vmware_portgroup](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_portgroup.rst)|Create a VMware portgroup
[community.vmware.vmware_portgroup_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_portgroup_facts.rst)|Gathers facts about an ESXi host's Port Group configuration
[community.vmware.vmware_portgroup_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_portgroup_info.rst)|Gathers info about an ESXi host's Port Group configuration
[community.vmware.vmware_resource_pool](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_resource_pool.rst)|Add/remove resource pools to/from vCenter
[community.vmware.vmware_resource_pool_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_resource_pool_facts.rst)|Gathers facts about resource pool information
[community.vmware.vmware_resource_pool_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_resource_pool_info.rst)|Gathers info about resource pool information
[community.vmware.vmware_tag](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_tag.rst)|Manage VMware tags
[community.vmware.vmware_tag_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_tag_info.rst)|Manage VMware tag info
[community.vmware.vmware_tag_manager](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_tag_manager.rst)|Manage association of VMware tags with VMware objects
[community.vmware.vmware_target_canonical_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_target_canonical_facts.rst)|Return canonical (NAA) from an ESXi host system
[community.vmware.vmware_target_canonical_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_target_canonical_info.rst)|Return canonical (NAA) from an ESXi host system
[community.vmware.vmware_vc_infraprofile_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vc_infraprofile_info.rst)|List and Export VMware Vcenter infra profile configs.
[community.vmware.vmware_vcenter_settings](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vcenter_settings.rst)|Configures general settings on a vCenter server
[community.vmware.vmware_vcenter_statistics](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vcenter_statistics.rst)|Configures statistics on a vCenter server
[community.vmware.vmware_vm_host_drs_rule](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vm_host_drs_rule.rst)|Creates vm/host group in a given cluster
[community.vmware.vmware_vm_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vm_info.rst)|Return basic info pertaining to a VMware machine guest
[community.vmware.vmware_vm_shell](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vm_shell.rst)|Run commands in a VMware guest operating system
[community.vmware.vmware_vm_storage_policy_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vm_storage_policy_info.rst)|Gather information about vSphere storage profile defined storage policy information.
[community.vmware.vmware_vm_vm_drs_rule](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vm_vm_drs_rule.rst)|Configure VMware DRS Affinity rule for virtual machine in given cluster
[community.vmware.vmware_vm_vss_dvs_migrate](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vm_vss_dvs_migrate.rst)|Migrates a virtual machine from a standard vswitch to distributed
[community.vmware.vmware_vmkernel](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vmkernel.rst)|Manages a VMware VMkernel Adapter of an ESXi host.
[community.vmware.vmware_vmkernel_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vmkernel_facts.rst)|Gathers VMKernel facts about an ESXi host
[community.vmware.vmware_vmkernel_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vmkernel_info.rst)|Gathers VMKernel info about an ESXi host
[community.vmware.vmware_vmkernel_ip_config](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vmkernel_ip_config.rst)|Configure the VMkernel IP Address
[community.vmware.vmware_vmotion](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vmotion.rst)|Move a virtual machine using vMotion, and/or its vmdks using storage vMotion.
[community.vmware.vmware_vsan_cluster](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vsan_cluster.rst)|Configure VSAN clustering on an ESXi host
[community.vmware.vmware_vsan_health_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vsan_health_info.rst)|Gather information about a VMware vSAN cluster's health
[community.vmware.vmware_vspan_session](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vspan_session.rst)|Create or remove a Port Mirroring session.
[community.vmware.vmware_vswitch](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vswitch.rst)|Manage a VMware Standard Switch to an ESXi host.
[community.vmware.vmware_vswitch_facts](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vswitch_facts.rst)|Gathers facts about an ESXi host's vswitch configurations
[community.vmware.vmware_vswitch_info](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vmware_vswitch_info.rst)|Gathers info about an ESXi host's vswitch configurations
[community.vmware.vsphere_copy](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vsphere_copy.rst)|Copy a file to a VMware datastore
[community.vmware.vsphere_file](https://github.com/ansible-collections/vmware/blob/master/docs/community.vmware.vsphere_file.rst)|Manage files on a vCenter datastore
<!--end collection content-->

## Testing and Development

If you want to develop new content for this collection or improve what is already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

- [Guidelines for VMware module development](https://docs.ansible.com/ansible/latest/dev_guide/platforms/vmware_guidelines.html)

### Testing with `ansible-test`

TBD

## Publishing New Version

TBD

## More Information

TBD

## Communication

We have a dedicated Working Group for VMware.
You can find other people interested in this in `#ansible-vmware` on Freenode IRC.
For more information about communities, meetings and agendas see https://github.com/ansible/community/wiki/VMware.

## License

GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.
