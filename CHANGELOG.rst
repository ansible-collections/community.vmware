==============================
community.vmware Release Notes
==============================

.. contents:: Topics

This changelog describes changes after version 5.7.2.

v6.1.0
======

Major Changes
-------------

- Replace ``ansible.module_utils._text`` (https://github.com/ansible-collections/community.vmware/issues/2497).
- Replace ``ansible.module_utils.common._collections_compat`` (https://github.com/ansible-collections/community.vmware/issues/2497).
- Replace ``ansible.module_utils.six`` (https://github.com/ansible-collections/community.vmware/pull/2495).

Minor Changes
-------------

- vmware_dvs_portgroup - add ``portgroup_description`` parameter (https://github.com/ansible-collections/community.vmware/issues/2487).

v6.0.0
======

Major Changes
-------------

- Re-use code from ``vmware.vmware`` (https://github.com/ansible-collections/community.vmware/pull/2459).

Minor Changes
-------------

- vcenter_license - Add support for VCF license keys. (https://github.com/ansible-collections/community.vmware/pull/2451)
- vsphere_file - Remove ``ansible.module_utils.six.PY2`` (https://github.com/ansible-collections/community.vmware/pull/2475).

Breaking Changes / Porting Guide
--------------------------------

- Removed support for ansible-core < 2.19.0.
- Removed support for vmware.vmware < 2.0.0.
- Replace the dependencies on ``pyvmomi``, ``vmware-vcenter`` and ``vmware-vapi-common-client`` with ``vcf-sdk`` (https://github.com/ansible-collections/community.vmware/pull/2457).

Deprecated Features
-------------------

- vmware_guest_snapshot - the module has been deprecated and will be removed in community.vmware 8.0.0 (https://github.com/ansible-collections/community.vmware/pull/2467).

Removed Features (previously deprecated)
----------------------------------------

- vmware_cluster - The deprecated module has been removed. Use ``vmware.vmware.cluster`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_dpm - The deprecated module has been removed. Use ``vmware.vmware.cluster_dpm`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_drs - The deprecated module has been removed. Use ``vmware.vmware.cluster_drs`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_drs_recommendations - The deprecated module has been removed. Use ``vmware.vmware.cluster_drs_recommendations`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).
- vmware_cluster_vcls - The deprecated module has been removed. Use ``vmware.vmware.cluster_vcls`` instead (https://github.com/ansible-collections/community.vmware/pull/2455).

Bugfixes
--------

- vmware_guest_file_operation - fix ``replace() argument 2 must be str, not int`` error (https://github.com/ansible-collections/community.vmware/issues/2447).
- vmware_tools - fix ``replace() argument 2 must be str, not int`` error (https://github.com/ansible-collections/community.vmware/issues/2447).
