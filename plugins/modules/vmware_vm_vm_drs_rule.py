#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vm_vm_drs_rule
short_description: Configure VMware DRS Affinity rule for virtual machines in the given cluster
description:
- This module can be used to configure VMware DRS Affinity rule for virtual machines in the given cluster.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  datacenter:
    version_added: '4.6.0'
    description:
      - "Datacenter to search for given cluster. If not set, we use first cluster we encounter with O(cluster_name)."
    required: false
    type: str
  cluster_name:
    description:
    - Desired cluster name where virtual machines are present for the DRS rule.
    required: true
    type: str
  vms:
    description:
    - List of virtual machines name for which DRS rule needs to be applied.
    - Required if O(state=present).
    type: list
    elements: str
  drs_rule_name:
    description:
    - The name of the DRS rule to manage.
    required: true
    type: str
  enabled:
    description:
    - If set to V(true), the DRS rule will be enabled.
    - Effective only if O(state=present).
    default: false
    type: bool
  mandatory:
    description:
    - If set to V(true), the DRS rule will be mandatory.
    - Effective only if O(state=present).
    default: false
    type: bool
  affinity_rule:
    description:
    - If set to V(true), the DRS rule will be an Affinity rule.
    - If set to V(false), the DRS rule will be an Anti-Affinity rule.
    - Effective only if O(state=present).
    default: true
    type: bool
  state:
    description:
    - If set to V(present), then the DRS rule is created if not present.
    - If set to V(present), then the DRS rule is already present, it updates to the given configurations.
    - If set to V(absent), then the DRS rule is deleted if present.
    required: false
    default: present
    choices: [ present, absent ]
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Create DRS Affinity Rule for VM-VM
  community.vmware.vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    datacenter: "{{ datacenter }}"
    cluster_name: "{{ cluster_name }}"
    vms:
        - vm1
        - vm2
    drs_rule_name: vm1-vm2-affinity-rule-001
    enabled: true
    mandatory: true
    affinity_rule: true
  delegate_to: localhost

- name: Create DRS Anti-Affinity Rule for VM-VM
  community.vmware.vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    datacenter: "{{ datacenter }}"
    cluster_name: "{{ cluster_name }}"
    enabled: true
    vms:
        - vm1
        - vm2
    drs_rule_name: vm1-vm2-affinity-rule-001
    mandatory: true
    affinity_rule: false
  delegate_to: localhost

- name: Delete DRS Affinity Rule for VM-VM
  community.vmware.vmware_vm_vm_drs_rule:
    hostname: "{{ esxi_server }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    datacenter: "{{ datacenter }}"
    cluster_name: "{{ cluster_name }}"
    drs_rule_name: vm1-vm2-affinity-rule-001
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
result:
    description: metadata about DRS VM and VM rule
    returned: when state is present
    type: dict
    sample: {
            "rule_enabled": false,
            "rule_key": 20,
            "rule_mandatory": true,
            "rule_name": "drs_rule_0014",
            "rule_uuid": "525f3bc0-253f-825a-418e-2ec93bffc9ae",
            "rule_vms": [
                "VM_65",
                "VM_146"
            ]
        }
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi, wait_for_task,
    find_vm_by_id, find_cluster_by_name, find_datacenter_by_name)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class VmwareDrs(PyVmomi):
    def __init__(self, module):
        super(VmwareDrs, self).__init__(module)
        self.vm_list = module.params['vms']
        self.__datacenter_name = module.params.get('datacenter', None)
        self.__datacenter_obj = None
        self.cluster_name = module.params['cluster_name']
        self.rule_name = module.params['drs_rule_name']
        self.enabled = module.params['enabled']
        self.mandatory = module.params['mandatory']
        self.affinity_rule = module.params['affinity_rule']
        self.state = module.params['state']

        if self.__datacenter_name is not None:
            self.__datacenter_obj = find_datacenter_by_name(self.content, self.__datacenter_name)
            if self.__datacenter_obj is None and module.check_mode is False:
                raise Exception("Datacenter '%s' not found" % self.__datacenter_name)
        # Sanity check for cluster
        self.cluster_obj = find_cluster_by_name(content=self.content, datacenter=self.__datacenter_obj,
                                                cluster_name=self.cluster_name)
        if self.cluster_obj is None:
            self.module.fail_json(msg="Failed to find the cluster %s" % self.cluster_name)
        # Sanity check for virtual machines
        self.vm_obj_list = []
        if self.state == 'present':
            # Get list of VMs only if state is present
            self.vm_obj_list = self.get_all_vms_info()

    # Getter
    def get_all_vms_info(self, vms_list=None):
        """
        Get all VM objects using name from given cluster
        Args:
            vms_list: List of VM names

        Returns: List of VM managed objects

        """
        vm_obj_list = []
        if vms_list is None:
            vms_list = self.vm_list

        for vm_name in vms_list:
            vm_obj = find_vm_by_id(content=self.content, vm_id=vm_name,
                                   vm_id_type='vm_name', cluster=self.cluster_obj)
            if vm_obj is None:
                self.module.fail_json(msg="Failed to find the virtual machine %s "
                                          "in the given cluster %s" % (vm_name,
                                                                       self.cluster_name))
            vm_obj_list.append(vm_obj)
        return vm_obj_list

    def get_rule_key_by_name(self, cluster_obj=None, rule_name=None):
        """
        Get a specific DRS rule key by name
        Args:
            rule_name: Name of rule
            cluster_obj: Cluster managed object

        Returns: Rule Object if found or None

        """
        if cluster_obj is None:
            cluster_obj = self.cluster_obj

        if rule_name:
            rules_list = [rule for rule in cluster_obj.configuration.rule if rule.name == rule_name]
            if rules_list:
                return rules_list[0]
        # No rule found
        return None

    @staticmethod
    def normalize_rule_spec(rule_obj=None):
        """
        Return human readable rule spec
        Args:
            rule_obj: Rule managed object

        Returns: Dictionary with Rule info

        """
        if rule_obj is None:
            return {}
        return dict(rule_key=rule_obj.key,
                    rule_enabled=rule_obj.enabled,
                    rule_name=rule_obj.name,
                    rule_mandatory=rule_obj.mandatory,
                    rule_uuid=rule_obj.ruleUuid,
                    rule_vms=[vm.name for vm in rule_obj.vm],
                    rule_affinity=True if isinstance(rule_obj, vim.cluster.AffinityRuleSpec) else False,
                    )

    # Create
    def create(self):
        """
        Create a DRS rule if rule does not exist
        """
        rule_obj = self.get_rule_key_by_name(rule_name=self.rule_name)
        if rule_obj is not None:
            existing_rule = self.normalize_rule_spec(rule_obj=rule_obj)
            if ((sorted(existing_rule['rule_vms']) == sorted(self.vm_list))
                    and (existing_rule['rule_enabled'] == self.enabled)
                    and (existing_rule['rule_mandatory'] == self.mandatory)
                    and (existing_rule['rule_affinity'] == self.affinity_rule)):
                self.module.exit_json(changed=False, result=existing_rule, msg="Rule already exists with the same configuration")
            return self.update_rule_spec(rule_obj)
        return self.create_rule_spec()

    def create_rule_spec(self):
        """
        Create DRS rule
        """
        changed = False
        result = None
        if self.affinity_rule:
            rule = vim.cluster.AffinityRuleSpec()
        else:
            rule = vim.cluster.AntiAffinityRuleSpec()

        rule.vm = self.vm_obj_list
        rule.enabled = self.enabled
        rule.mandatory = self.mandatory
        rule.name = self.rule_name

        rule_spec = vim.cluster.RuleSpec(info=rule, operation='add')
        config_spec = vim.cluster.ConfigSpecEx(rulesSpec=[rule_spec])

        try:
            if not self.module.check_mode:
                task = self.cluster_obj.ReconfigureEx(config_spec, modify=True)
                changed, result = wait_for_task(task)
        except vmodl.fault.InvalidRequest as e:
            result = to_native(e.msg)
        except Exception as e:
            result = to_native(e)

        if changed:
            rule_obj = self.get_rule_key_by_name(rule_name=self.rule_name)
            result = self.normalize_rule_spec(rule_obj)

        if self.module.check_mode:
            changed = True
            result = dict(
                rule_key='',
                rule_enabled=rule.enabled,
                rule_name=self.rule_name,
                rule_mandatory=rule.mandatory,
                rule_uuid='',
                rule_vms=[vm.name for vm in rule.vm],
                rule_affinity=self.affinity_rule,
            )
        return changed, result

    def update_rule_spec(self, rule_obj=None):
        """
        Update DRS rule
        """
        changed = False
        result = None
        rule_obj.vm = self.vm_obj_list

        if (rule_obj.mandatory != self.mandatory):
            rule_obj.mandatory = self.mandatory

        if (rule_obj.enabled != self.enabled):
            rule_obj.enabled = self.enabled

        rule_spec = vim.cluster.RuleSpec(info=rule_obj, operation='edit')
        config_spec = vim.cluster.ConfigSpec(rulesSpec=[rule_spec])

        try:
            if not self.module.check_mode:
                task = self.cluster_obj.ReconfigureCluster_Task(config_spec, modify=True)
                changed, result = wait_for_task(task)
            else:
                changed = True
        except vmodl.fault.InvalidRequest as e:
            result = to_native(e.msg)
        except Exception as e:
            result = to_native(e)

        if changed:
            rule_obj = self.get_rule_key_by_name(rule_name=self.rule_name)
            result = self.normalize_rule_spec(rule_obj)

        return changed, result

    # Delete
    def delete(self, rule_name=None):
        """
        Delete DRS rule using name
        """
        changed = False
        if rule_name is None:
            rule_name = self.rule_name

        rule = self.get_rule_key_by_name(rule_name=rule_name)
        if rule is not None:
            rule_key = int(rule.key)
            rule_spec = vim.cluster.RuleSpec(removeKey=rule_key, operation='remove')
            config_spec = vim.cluster.ConfigSpecEx(rulesSpec=[rule_spec])
            try:
                if not self.module.check_mode:
                    task = self.cluster_obj.ReconfigureEx(config_spec, modify=True)
                    changed, result = wait_for_task(task)
                else:
                    changed = True
                    result = 'Rule %s will be deleted' % self.rule_name
            except vmodl.fault.InvalidRequest as e:
                result = to_native(e.msg)
            except Exception as e:
                result = to_native(e)
        else:
            result = 'No rule named %s exists' % self.rule_name
        return changed, result


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        state=dict(type='str', default='present', choices=['absent', 'present']),
        vms=dict(type='list', elements='str'),
        cluster_name=dict(type='str', required=True),
        datacenter=dict(type='str', required=False),
        drs_rule_name=dict(type='str', required=True),
        enabled=dict(type='bool', default=False),
        mandatory=dict(type='bool', default=False),
        affinity_rule=dict(type='bool', default=True),
    )
    )

    required_if = [
        ['state', 'present', ['vms']]
    ]
    module = AnsibleModule(argument_spec=argument_spec,
                           required_if=required_if,
                           supports_check_mode=True)

    results = dict(failed=False, changed=False)
    state = module.params['state']
    vm_drs = VmwareDrs(module)

    if state == 'present':
        # Add Rule
        changed, result = vm_drs.create()
        if changed:
            results['changed'] = changed
        else:
            results['failed'] = True
            results['msg'] = "Failed to create DRS rule %s" % vm_drs.rule_name
        results['result'] = result
    elif state == 'absent':
        # Delete Rule
        changed, result = vm_drs.delete()
        if changed:
            results['changed'] = changed
            results['msg'] = "DRS rule %s deleted successfully." % vm_drs.rule_name
        else:
            if "No rule named" in result:
                results['msg'] = result
                module.exit_json(**results)

            results['failed'] = True
            results['msg'] = "Failed to delete DRS rule %s" % vm_drs.rule_name
        results['result'] = result

    if results['changed']:
        module.exit_json(**results)
    if results['failed']:
        module.fail_json(**results)


if __name__ == '__main__':
    main()
