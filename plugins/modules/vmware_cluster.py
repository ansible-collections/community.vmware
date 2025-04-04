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
module: vmware_cluster
short_description: Manage VMware vSphere clusters
description:
    - Adds or removes VMware vSphere clusters.
    - To manage DRS, HA and VSAN related configurations, use the modules vmware_cluster_drs, vmware_cluster_ha and vmware_cluster_vsan.
author:
- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
deprecated:
  removed_in: 6.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.cluster) instead.
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
    state:
      description:
      - Create V(present) or remove V(absent) a VMware vSphere cluster.
      choices: [ absent, present ]
      default: present
      type: str
seealso:
- module: community.vmware.vmware_cluster_drs
- module: community.vmware.vmware_cluster_ha
- module: community.vmware.vmware_cluster_vsan
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Create Cluster
  community.vmware.vmware_cluster:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
  delegate_to: localhost

- name: Delete Cluster
  community.vmware.vmware_cluster:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter_name: datacenter
    cluster_name: cluster
    state: absent
  delegate_to: localhost
'''

RETURN = r'''#
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    find_datacenter_by_name,
    wait_for_task)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VMwareCluster(PyVmomi):
    def __init__(self, module):
        super(VMwareCluster, self).__init__(module)
        self.cluster_name = module.params['cluster_name']
        self.datacenter_name = module.params['datacenter']
        self.desired_state = module.params['state']
        self.datacenter = None
        self.cluster = None

    def process_state(self):
        """
        Manage internal states of cluster
        """
        cluster_states = {
            'absent': {
                'present': self.state_destroy_cluster,
                'absent': self.state_exit_unchanged,
            },
            'present': {
                'present': self.state_exit_unchanged,
                'absent': self.state_create_cluster,
            }
        }
        current_state = self.check_cluster_configuration()
        # Based on the desired_state and the current_state call
        # the appropriate method from the dictionary
        cluster_states[self.desired_state][current_state]()

    def state_create_cluster(self):
        """
        Create cluster with given configuration
        """
        try:
            cluster_config_spec = vim.cluster.ConfigSpecEx()
            if not self.module.check_mode:
                self.datacenter.hostFolder.CreateClusterEx(self.cluster_name, cluster_config_spec)
            self.module.exit_json(changed=True)
        except vmodl.fault.InvalidArgument as invalid_args:
            self.module.fail_json(msg="Cluster configuration specification"
                                      " parameter is invalid : %s" % to_native(invalid_args.msg))
        except vim.fault.InvalidName as invalid_name:
            self.module.fail_json(msg="'%s' is an invalid name for a"
                                      " cluster : %s" % (self.cluster_name,
                                                         to_native(invalid_name.msg)))
        except vmodl.fault.NotSupported as not_supported:
            # This should never happen
            self.module.fail_json(msg="Trying to create a cluster on an incorrect"
                                      " folder object : %s" % to_native(not_supported.msg))
        except vmodl.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=to_native(runtime_fault.msg))
        except vmodl.MethodFault as method_fault:
            # This should never happen either
            self.module.fail_json(msg=to_native(method_fault.msg))
        except Exception as generic_exc:
            self.module.fail_json(msg="Failed to create cluster"
                                      " due to generic exception %s" % to_native(generic_exc))

    def state_destroy_cluster(self):
        """
        Destroy cluster
        """
        changed, result = True, None

        try:
            if not self.module.check_mode:
                task = self.cluster.Destroy_Task()
                changed, result = wait_for_task(task)
            self.module.exit_json(changed=changed, result=result)
        except vim.fault.VimFault as vim_fault:
            self.module.fail_json(msg=to_native(vim_fault.msg))
        except vmodl.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=to_native(runtime_fault.msg))
        except vmodl.MethodFault as method_fault:
            self.module.fail_json(msg=to_native(method_fault.msg))
        except Exception as generic_exc:
            self.module.fail_json(msg="Failed to destroy cluster"
                                      " due to generic exception %s" % to_native(generic_exc))

    def state_exit_unchanged(self):
        """
        Exit without any change
        """
        self.module.exit_json(changed=False)

    def check_cluster_configuration(self):
        """
        Check cluster configuration
        Returns: 'Present' if cluster exists, else 'absent'

        """
        try:
            self.datacenter = find_datacenter_by_name(self.content, self.datacenter_name)
            if self.datacenter is None:
                self.module.fail_json(msg="Datacenter %s does not exist." % self.datacenter_name)
            self.cluster = self.find_cluster_by_name(cluster_name=self.cluster_name, datacenter_name=self.datacenter)

            if self.cluster is None:
                return 'absent'

            return 'present'
        except vmodl.RuntimeFault as runtime_fault:
            self.module.fail_json(msg=to_native(runtime_fault.msg))
        except vmodl.MethodFault as method_fault:
            self.module.fail_json(msg=to_native(method_fault.msg))
        except Exception as generic_exc:
            self.module.fail_json(msg="Failed to check configuration"
                                      " due to generic exception %s" % to_native(generic_exc))


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(dict(
        cluster_name=dict(type='str', required=True),
        datacenter=dict(type='str', required=True, aliases=['datacenter_name']),
        state=dict(type='str',
                   default='present',
                   choices=['absent', 'present']),
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    vmware_cluster = VMwareCluster(module)
    vmware_cluster.process_state()


if __name__ == '__main__':
    main()
