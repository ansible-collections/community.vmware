#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Ansible Project
# Copyright: (c) 2020, Dustin Scott <sdustin@vmware.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_vm_storage_policy
short_description: Create vSphere storage policies
description:
- A vSphere storage policy defines metadata that describes storage requirements
  for virtual machines and storage capabilities of storage providers.
- Currently, only tag-based storage policy creation is supported.
author:
- Dustin Scott (@scottd018)
options:
  name:
    description:
    - Name of the storage policy to create, update, or delete.
    required: True
    type: str
  description:
    description:
    - Description of the storage policy to create or update.
    - This parameter is ignored when C(state=absent).
    type: str
    required: False
  tag_category:
    description:
    - Name of the pre-existing tag category to assign to the storage policy.
    - This parameter is ignored when C(state=absent).
    - This parameter is required when C(state=present).
    required: False
    type: str
  tag_name:
    description:
    - Name of the pre-existing tag to assign to the storage policy.
    - This parameter is ignored when C(state=absent).
    - This parameter is required when C(state=present).
    required: False
    type: str
  tag_affinity:
    description:
    - If set to C(true), the storage policy enforces that virtual machines require the existence of a tag for datastore placement.
    - If set to C(false), the storage policy enforces that virtual machines require the absence of a tag for datastore placement.
    - This parameter is ignored when C(state=absent).
    required: False
    type: bool
    default: True
  state:
    description:
    - State of storage policy.
    - If set to C(present), the storage policy is created.
    - If set to C(absent), the storage policy is deleted.
    default: present
    choices: [ absent, present ]
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Create or update a vSphere tag-based storage policy
  community.vmware.vmware_vm_storage_policy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: "vSphere storage policy"
    description: "vSphere storage performance policy"
    tag_category: "performance_tier"
    tag_name: "gold"
    tag_affinity: true
    state: "present"
  delegate_to: localhost

- name: Remove a vSphere tag-based storage policy
  community.vmware.vmware_vm_storage_policy:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    name: "vSphere storage policy"
    state: "absent"
  delegate_to: localhost
'''

RETURN = r'''
vmware_vm_storage_policy:
  description: dictionary of information for the storage policy
  returned: success
  type: dict
  sample: {
            "vmware_vm_storage_policy": {
                "description": "Storage policy for gold-tier storage",
                "id": "aa6d5a82-1c88-45da-85d3-3d74b91a5bad",
                "name": "gold"
            }
        }
'''

try:
    from pyVmomi import pbm
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_spbm import SPBM
from ansible_collections.community.vmware.plugins.module_utils.vmware import vmware_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient


class VmwareStoragePolicyManager(SPBM):
    def __init__(self, module):
        super(VmwareStoragePolicyManager, self).__init__(module)
        self.rest_client = VmwareRestClient(module)

    #
    # MOB METHODS
    #
    # These will generate the individual items with the following expected structure (see
    # https://github.com/vmware/pyvmomi/blob/master/pyVmomi/PbmObjects.py):
    #
    # PbmProfile: array
    #   - name:        string
    #     description: string
    #     constraints: PbmCapabilityConstraints
    #       subProfiles: ArrayOfPbmCapabilitySubProfile
    #         - name:       string
    #           capability: ArrayOfPbmCapabilityInstance
    #             - constraint: ArrayOfCapabilityConstraintInstance
    #               - id: string
    #                 value: anyType
    #                   values: arrayOfStrings
    #                     - tags
    #
    #
    def create_mob_tag_values(self, tags):
        return pbm.capability.types.DiscreteSet(values=tags)

    def create_mob_capability_property_instance(self, tag_id, tag_operator, tags):
        return pbm.capability.PropertyInstance(
            id=tag_id,
            operator=tag_operator,
            value=self.create_mob_tag_values(tags)
        )

    def create_mob_capability_constraint_instance(self, tag_id, tag_operator, tags):
        return pbm.capability.ConstraintInstance(
            propertyInstance=[self.create_mob_capability_property_instance(tag_id, tag_operator, tags)]
        )

    def create_mob_capability_metadata_uniqueid(self, tag_category):
        return pbm.capability.CapabilityMetadata.UniqueId(
            namespace="http://www.vmware.com/storage/tag",
            id=tag_category
        )

    def create_mob_capability_instance(self, tag_id, tag_operator, tags, tag_category):
        return pbm.capability.CapabilityInstance(
            id=self.create_mob_capability_metadata_uniqueid(tag_category),
            constraint=[self.create_mob_capability_constraint_instance(tag_id, tag_operator, tags)]
        )

    def create_mob_capability_constraints_subprofile(self, tag_id, tag_operator, tags, tag_category):
        return pbm.profile.SubProfileCapabilityConstraints.SubProfile(
            name="Tag based placement",
            capability=[self.create_mob_capability_instance(tag_id, tag_operator, tags, tag_category)]
        )

    def create_mob_capability_subprofile(self, tag_id, tag_operator, tags, tag_category):
        return pbm.profile.SubProfileCapabilityConstraints(
            subProfiles=[self.create_mob_capability_constraints_subprofile(tag_id, tag_operator, tags, tag_category)]
        )

    def create_mob_pbm_update_spec(self, tag_id, tag_operator, tags, tag_category, description):
        return pbm.profile.CapabilityBasedProfileUpdateSpec(
            description=description,
            constraints=self.create_mob_capability_subprofile(tag_id, tag_operator, tags, tag_category)
        )

    def create_mob_pbm_create_spec(self, tag_id, tag_operator, tags, tag_category, description, name):
        return pbm.profile.CapabilityBasedProfileCreateSpec(
            name=name,
            description=description,
            resourceType=pbm.profile.ResourceType(resourceType="STORAGE"),
            category="REQUIREMENT",
            constraints=self.create_mob_capability_subprofile(tag_id, tag_operator, tags, tag_category)
        )

    def get_tag_constraints(self, capabilities):
        """
        Return tag constraints for a profile given its capabilities
        """
        tag_constraints = {}
        for capability in capabilities:
            for constraint in capability.constraint:
                if hasattr(constraint, 'propertyInstance'):
                    for propertyInstance in constraint.propertyInstance:
                        if hasattr(propertyInstance.value, 'values'):
                            tag_constraints['id'] = propertyInstance.id
                            tag_constraints['values'] = propertyInstance.value.values
                            tag_constraints['operator'] = propertyInstance.operator

        return tag_constraints

    def get_profile_manager(self):
        self.get_spbm_connection()

        return self.spbm_content.profileManager

    def get_storage_policies(self, profile_manager):
        profile_ids = profile_manager.PbmQueryProfile(
            resourceType=pbm.profile.ResourceType(resourceType="STORAGE"),
            profileCategory="REQUIREMENT"
        )
        profiles = []
        if profile_ids:
            profiles = profile_manager.PbmRetrieveContent(profileIds=profile_ids)

        return profiles

    def format_profile(self, profile):
        formatted_profile = {
            'name': profile.name,
            'id': profile.profileId.uniqueId,
            'description': profile.description
        }

        return formatted_profile

    def format_tag_mob_id(self, tag_category):
        return "com.vmware.storage.tag." + tag_category + ".property"

    def format_results_and_exit(self, results, policy, changed):
        results['vmware_vm_storage_policy'] = self.format_profile(policy)
        results['changed'] = changed

        self.module.exit_json(**results)

    def update_storage_policy(self, policy, pbm_client, results):
        expected_description = self.params.get('description')
        expected_tags = [self.params.get('tag_name')]
        expected_tag_category = self.params.get('tag_category')
        expected_tag_id = self.format_tag_mob_id(expected_tag_category)
        expected_operator = "NOT"
        if self.params.get('tag_affinity'):
            expected_operator = None

        needs_change = False

        if policy.description != expected_description:
            needs_change = True

        if hasattr(policy.constraints, 'subProfiles'):
            for subprofile in policy.constraints.subProfiles:
                tag_constraints = self.get_tag_constraints(subprofile.capability)
                if tag_constraints['id'] == expected_tag_id:
                    if tag_constraints['values'] != expected_tags:
                        needs_change = True
                else:
                    needs_change = True

                if tag_constraints['operator'] != expected_operator:
                    needs_change = True
        else:
            needs_change = True

        if needs_change:
            pbm_client.PbmUpdate(
                profileId=policy.profileId,
                updateSpec=self.create_mob_pbm_update_spec(expected_tag_id, expected_operator, expected_tags, expected_tag_category, expected_description)
            )

        self.format_results_and_exit(results, policy, needs_change)

    def remove_storage_policy(self, policy, pbm_client, results):
        pbm_client.PbmDelete(profileId=[policy.profileId])

        self.format_results_and_exit(results, policy, True)

    def create_storage_policy(self, policy, pbm_client, results):
        profile_ids = pbm_client.PbmCreate(
            createSpec=self.create_mob_pbm_create_spec(
                self.format_tag_mob_id(self.params.get('tag_category')),
                None,
                [self.params.get('tag_name')],
                self.params.get('tag_category'),
                self.params.get('description'),
                self.params.get('name')
            )
        )

        policy = pbm_client.PbmRetrieveContent(profileIds=[profile_ids])

        self.format_results_and_exit(results, policy[0], True)

    def ensure_state(self):
        client = self.get_profile_manager()
        policies = self.get_storage_policies(client)
        policy_name = self.params.get('name')
        results = dict(changed=False, vmware_vm_storage_policy={})

        if self.params.get('state') == 'present':
            if self.params.get('tag_category') is None:
                self.module.fail_json(msg="tag_category is required when 'state' is 'present'")

            if self.params.get('tag_name') is None:
                self.module.fail_json(msg="tag_name is required when 'state' is 'present'")

            # ensure if the category exists
            category_result = self.rest_client.get_category_by_name(self.params.get('tag_category'))
            if category_result is None:
                self.module.fail_json(msg="%s is not found in vCenter Server tag categories" % self.params.get('tag_category'))

            # ensure if the tag exists
            tag_result = self.rest_client.get_tag_by_category(self.params.get('tag_name'), self.params.get('tag_category'))
            if tag_result is None:
                self.module.fail_json(msg="%s is not found in vCenter Server tags" % self.params.get('tag_name'))

            # loop through and update the first match
            for policy in policies:
                if policy.name == policy_name:
                    self.update_storage_policy(policy, client, results)

            # if we didn't exit by now create the profile
            self.create_storage_policy(policy, client, results)

        if self.params.get('state') == 'absent':
            # loop through and delete the first match
            for policy in policies:
                if policy.name == policy_name:
                    self.remove_storage_policy(policy, client, results)

            # if we didn't exit by now exit without changing anything
            self.module.exit_json(**results)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        name=dict(type='str', required=True),
        description=dict(type='str', required=False),
        tag_name=dict(type='str', required=False),
        tag_category=dict(type='str', required=False),
        tag_affinity=dict(type='bool', default=True),
        state=dict(type='str', choices=['absent', 'present'], default='present')
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)
    manager = VmwareStoragePolicyManager(module)

    manager.ensure_state()


if __name__ == '__main__':
    main()
