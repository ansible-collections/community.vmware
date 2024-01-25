==============================
community.vmware Release Notes
==============================

.. contents:: Topics

This changelog describes changes after version 3.9.0.

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
