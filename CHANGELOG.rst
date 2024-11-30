==============================
community.vmware Release Notes
==============================

.. contents:: Topics

This changelog describes changes after version 4.7.0.

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
