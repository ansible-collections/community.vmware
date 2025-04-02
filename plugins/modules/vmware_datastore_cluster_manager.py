#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Ansible Project
# Copyright (c) 2020, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_datastore_cluster_manager
short_description: Manage VMware vSphere datastore cluster's members
description:
    - This module can be used to add datastore in the datastore cluster.
author:
-  Abhijeet Kasurde (@Akasurde)
options:
    datacenter_name:
      description:
      - The name of the datacenter.
      required: false
      aliases: [ datacenter ]
      type: str
    datastore_cluster_name:
      description:
      - The name of the datastore cluster.
      required: true
      type: str
      aliases: [ datastore_cluster ]
    state:
      description:
      - If set to V(present), datastores specified by O(datastores) will be added to the given datastore cluster.
      - If set to V(absent), datastores specified by O(datastores) will be moved from the given datastore cluster to datstore folder of the parent datacenter.
      choices: [ present, absent ]
      default: present
      type: str
    datastores:
        description:
        - A list of datastores to be manage.
        type: list
        elements: str
        required: true
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Add datastore to the given datastore cluster
  community.vmware.vmware_datastore_cluster_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    datastore_cluster_name: '{{ datastore_cluster_name }}'
    datastores:
    - ds_001
    - ds_002
    - ds_003
    state: present
  delegate_to: localhost

- name: Move datastore from the given datastore cluster
  community.vmware.vmware_datastore_cluster_manager:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    datastore_cluster_name: '{{ datastore_cluster_name }}'
    datastores:
    - ds_001
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
datastore_cluster_info:
    description: information about datastore cluster
    returned: always
    type: str
    sample: {
        "changed_datastores": ["ds_171_1"],
        "current_datastores": [],
        "msg": null,
        "previous_datastores": ["ds_171_1"]
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, wait_for_task, TaskError
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VMwareDatastoreClusterManager(PyVmomi):
    def __init__(self, module):
        """
        Constructor

        """
        super(VMwareDatastoreClusterManager, self).__init__(module)
        datacenter_name = self.params.get('datacenter_name')
        datacenter_obj = self.find_datacenter_by_name(datacenter_name)
        if not datacenter_obj:
            self.module.fail_json(msg="Failed to find datacenter '%s' required"
                                      " for managing datastore cluster." % datacenter_name)
        self.folder_obj = datacenter_obj.datastoreFolder

        self.datastore_cluster_name = self.params.get('datastore_cluster_name')
        self.datastore_cluster_obj = self.find_datastore_cluster_by_name(self.datastore_cluster_name, datacenter=datacenter_obj)
        if not self.datastore_cluster_obj:
            self.module.fail_json(msg="Failed to find the datastore cluster '%s'" % self.datastore_cluster_name)

    def get_datastore_cluster_children(self):
        """
        Return Datastore from the given datastore cluster object

        """
        return [ds for ds in self.datastore_cluster_obj.childEntity if isinstance(ds, vim.Datastore)]

    def ensure(self):
        """
        Manage internal state of datastore cluster

        """
        changed = False
        results = dict(
            changed=changed,
        )
        temp_result = dict(
            previous_datastores=[],
            current_datastores=[],
            msg=""
        )
        state = self.module.params.get('state')
        datastores = self.module.params.get('datastores') or []
        datastore_obj_list = []
        dsc_child_obj = self.get_datastore_cluster_children()

        if state == 'present':
            temp_result['previous_datastores'] = [ds.name for ds in dsc_child_obj]
            for datastore_name in datastores:
                datastore_obj = self.find_datastore_by_name(datastore_name)
                if not datastore_obj:
                    self.module.fail_json(msg="Failed to find datastore '%s'" % datastore_name)
                if datastore_obj not in dsc_child_obj and datastore_obj not in datastore_obj_list:
                    datastore_obj_list.append(datastore_obj)

            if self.module.check_mode:
                changed_list = [ds.name for ds in datastore_obj_list]
                temp_result['current_datastores'] = temp_result['previous_datastores'].extend(changed_list)
                temp_result['changed_datastores'] = changed_list
                results['changed'] = len(datastore_obj_list) > 0
                results['datastore_cluster_info'] = temp_result
                self.module.exit_json(**results)

            try:
                if datastore_obj_list:
                    task = self.datastore_cluster_obj.MoveIntoFolder_Task(list=datastore_obj_list)
                    changed, result = wait_for_task(task)
                    temp_result['msg'] = result
                temp_result['changed_datastores'] = [ds.name for ds in datastore_obj_list]
                temp_result['current_datastores'] = [ds.name for ds in self.get_datastore_cluster_children()]
            except TaskError as generic_exc:
                self.module.fail_json(msg=to_native(generic_exc))
            except Exception as task_e:
                self.module.fail_json(msg=to_native(task_e))
        elif state == 'absent':
            temp_result['previous_datastores'] = [ds.name for ds in dsc_child_obj]
            temp_result['current_datastores'] = [ds.name for ds in dsc_child_obj]
            for datastore_name in datastores:
                datastore_obj = self.find_datastore_by_name(datastore_name)
                if not datastore_obj:
                    self.module.fail_json(msg="Failed to find datastore '%s'" % datastore_name)
                if datastore_obj in dsc_child_obj and datastore_obj not in datastore_obj_list:
                    datastore_obj_list.append(datastore_obj)

            if self.module.check_mode:
                changed_list = [ds.name for ds in datastore_obj_list]
                for ds in changed_list:
                    temp_result['current_datastores'].pop(ds)
                temp_result['changed_datastores'] = changed_list
                results['changed'] = len(datastore_obj_list) > 0
                results['datastore_cluster_info'] = temp_result
                self.module.exit_json(**results)

            try:
                if datastore_obj_list:
                    task = self.folder_obj.MoveIntoFolder_Task(list=datastore_obj_list)
                    changed, result = wait_for_task(task)
                    temp_result['msg'] = result
                temp_result['changed_datastores'] = [ds.name for ds in datastore_obj_list]
                temp_result['current_datastores'] = [ds.name for ds in self.get_datastore_cluster_children()]
            except TaskError as generic_exc:
                self.module.fail_json(msg=to_native(generic_exc))
            except Exception as task_e:
                self.module.fail_json(msg=to_native(task_e))

        results['changed'] = changed
        results['datastore_cluster_info'] = temp_result
        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        dict(
            datacenter_name=dict(type='str', required=False, aliases=['datacenter']),
            datastore_cluster_name=dict(type='str', required=True, aliases=['datastore_cluster']),
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            datastores=dict(type='list', required=True, elements='str'),
        )
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    datastore_cluster_mgr = VMwareDatastoreClusterManager(module)
    datastore_cluster_mgr.ensure()


if __name__ == '__main__':
    main()
