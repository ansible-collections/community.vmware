#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_cluster_vcls
short_description: Override the default vCLS (vSphere Cluster Services) VM disk placement for this cluster.
description:
    - Override the default vCLS VM disk placement for this cluster.
    - Some datastores cannot be selected for vCLS 'Allowed' as they are blocked by solutions as SRM or vSAN maintenance mode where vCLS cannot be configured.
author:
- Joseph Callen (@jcpowermac)
- Nina Loser (@Nina2244)
deprecated:
  removed_in: 6.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.cluster_vcls) instead.
options:
    cluster_name:
      description:
      - The name of the cluster to be managed.
      type: str
      required: true
    datacenter:
      description:
      - The name of the datacenter.
      type: str
      required: true
      aliases: [ datacenter_name ]
    allowed_datastores:
      description:
        - List of the allowed Datastores.
        - If there is one more in the current List it will be removed.
      type: list
      elements: str
      required: true
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Set Allowed vCLS Datastores
  community.vmware.vmware_cluster_vcls:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    allowed_datastores:
      - ds1
      - ds2
  delegate_to: localhost
'''

RETURN = r'''
result:
    description: information about performed operation
    returned: always
    type: str
    sample: {
        "result": null,
        "Added_AllowedDatastores": [ds2],
        "Removed_AllowedDatastores": [ds3]
    }
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    TaskError,
    find_datacenter_by_name,
    find_datastore_by_name,
    wait_for_task,
)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VMwareCluster(PyVmomi):
    def __init__(self, module):
        super(VMwareCluster, self).__init__(module)
        self.cluster_name = module.params['cluster_name']
        self.datacenter_name = module.params['datacenter']
        self.datacenter = None
        self.cluster = None

        self.datacenter = find_datacenter_by_name(self.content, self.datacenter_name)
        if self.datacenter is None:
            self.module.fail_json(msg="Datacenter %s does not exist." % self.datacenter_name)

        self.cluster = self.find_cluster_by_name(cluster_name=self.cluster_name, datacenter_name=self.datacenter)
        if self.cluster is None:
            self.module.fail_json(msg="Cluster %s does not exist." % self.cluster_name)

        self.allowedDatastores_names = module.params['allowed_datastores']

    def check_vCLS_config_diff(self):
        """
        Check vCLS configuration diff
        Returns: True and all to add and to remove allowed and not allowed Datastores if there is diff, else False

        """
        if not hasattr(self.cluster.configurationEx, 'systemVMsConfig'):
            return False, self.allowedDatastores_names, None

        currentAllowedDatastores = []
        changed = False

        # Get List currently of allowed Datastore Names
        vCLS_config = self.cluster.configurationEx.systemVMsConfig
        try:
            for ds in vCLS_config.allowedDatastores:
                currentAllowedDatastores.append(ds.name)
        except AttributeError:
            pass

        # Get the to add and to remove allowed and not allowed Datastores
        toAddAllowedDatastores = list(set(self.allowedDatastores_names) - set(currentAllowedDatastores))
        toRemoveAllowedDatastores = list(set(currentAllowedDatastores) - set(self.allowedDatastores_names))

        if len(toAddAllowedDatastores) != 0 or len(toRemoveAllowedDatastores) != 0:
            changed = True

        return changed, toAddAllowedDatastores, toRemoveAllowedDatastores

    def configure_vCLS(self):
        """
        Manage DRS configuration

        """
        result = None
        changed, toAddAllowedDatastores, toRemoveAllowedDatastores = self.check_vCLS_config_diff()

        if changed:
            if not self.module.check_mode:
                cluster_config_spec = vim.cluster.ConfigSpecEx()
                cluster_config_spec.systemVMsConfig = vim.cluster.SystemVMsConfigSpec()

                cluster_config_spec.systemVMsConfig.allowedDatastores = []

                # Build the Spec
                for ds_name in toAddAllowedDatastores:
                    specSystemVMsConfigAllowedDatastore = vim.cluster.DatastoreUpdateSpec()
                    specSystemVMsConfigAllowedDatastore.datastore = find_datastore_by_name(self.content, ds_name, self.datacenter)
                    specSystemVMsConfigAllowedDatastore.operation = 'add'
                    cluster_config_spec.systemVMsConfig.allowedDatastores.append(specSystemVMsConfigAllowedDatastore)

                for ds_name in toRemoveAllowedDatastores:
                    specSystemVMsConfigAllowedDatastore = vim.cluster.DatastoreUpdateSpec()
                    specSystemVMsConfigAllowedDatastore.removeKey = find_datastore_by_name(self.content, ds_name, self.datacenter)
                    specSystemVMsConfigAllowedDatastore.operation = 'remove'
                    cluster_config_spec.systemVMsConfig.allowedDatastores.append(specSystemVMsConfigAllowedDatastore)

                try:
                    task = self.cluster.ReconfigureComputeResource_Task(cluster_config_spec, True)
                    changed, result = wait_for_task(task)
                except vmodl.RuntimeFault as runtime_fault:
                    self.module.fail_json(msg=to_native(runtime_fault.msg))
                except vmodl.MethodFault as method_fault:
                    self.module.fail_json(msg=to_native(method_fault.msg))
                except TaskError as task_e:
                    self.module.fail_json(msg=to_native(task_e))
                except Exception as generic_exc:
                    self.module.fail_json(msg="Failed to update cluster"
                                              " due to generic exception %s" % to_native(generic_exc))
            else:
                changed = True

        results = dict(changed=changed)
        results['result'] = result
        results['Added_AllowedDatastores'] = toAddAllowedDatastores
        results['Removed_AllowedDatastores'] = toRemoveAllowedDatastores
        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        cluster_name=dict(type='str', required=True),
        datacenter=dict(type='str', required=True, aliases=['datacenter_name']),
        # vCLS
        allowed_datastores=dict(type='list', elements='str', required=True)
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    vmware_cluster_vCLS = VMwareCluster(module)
    vmware_cluster_vCLS.configure_vCLS()


if __name__ == '__main__':
    main()
