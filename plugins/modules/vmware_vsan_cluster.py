#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Russell Teague <rteague2 () csc.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vsan_cluster
short_description: Configure VSAN clustering on an ESXi host
description:
    - This module can be used to configure VSAN clustering on an ESXi host
author:
- Russell Teague (@mtnbikenc)
options:
    cluster_uuid:
        description:
            - Desired cluster UUID
        required: false
        type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Configure VMware VSAN Cluster
  hosts: deploy_node
  tags:
    - vsan
  tasks:
    - name: Configure VSAN on first host
      community.vmware.vmware_vsan_cluster:
         hostname: "{{ groups['esxi'][0] }}"
         username: "{{ esxi_username }}"
         password: "{{ site_password }}"
      delegate_to: localhost
      register: vsan_cluster

    - name: Configure VSAN on remaining hosts
      community.vmware.vmware_vsan_cluster:
         hostname: "{{ item }}"
         username: "{{ esxi_username }}"
         password: "{{ site_password }}"
         cluster_uuid: "{{ vsan_cluster.cluster_uuid }}"
      delegate_to: localhost
      loop: "{{ groups['esxi'][1:] }}"
'''

try:
    from pyVmomi import vim, vmodl
    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (get_all_objs, wait_for_task)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.clients._vmware import PyvmomiClient


def create_vsan_cluster(host_system, new_cluster_uuid):
    host_config_manager = host_system.configManager
    vsan_system = host_config_manager.vsanSystem

    vsan_config = vim.vsan.host.ConfigInfo()
    vsan_config.enabled = True

    if new_cluster_uuid is not None:
        vsan_config.clusterInfo = vim.vsan.host.ConfigInfo.ClusterInfo()
        vsan_config.clusterInfo.uuid = new_cluster_uuid

    vsan_config.storageInfo = vim.vsan.host.ConfigInfo.StorageInfo()
    vsan_config.storageInfo.autoClaimStorage = True

    task = vsan_system.UpdateVsan_Task(vsan_config)
    changed, result = wait_for_task(task)

    host_status = vsan_system.QueryHostStatus()
    cluster_uuid = host_status.uuid

    return changed, result, cluster_uuid


def main():

    argument_spec = base_argument_spec()
    argument_spec.update(dict(cluster_uuid=dict(required=False, type='str')))

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    if not HAS_PYVMOMI:
        module.fail_json(msg='pyvmomi is required for this module')

    new_cluster_uuid = module.params['cluster_uuid']

    try:
        pyvmomi_client = PyvmomiClient(
            hostname=module.params.get('hostname'),
            username=module.params.get('username'),
            password=module.params.get('password'),
            port=module.params.get('port'),
            validate_certs=module.params.get('validate_certs')
        )
        content = pyvmomi_client.content
        host = get_all_objs(content, [vim.HostSystem])
        if not host:
            module.fail_json(msg="Unable to locate Physical Host.")
        host_system = list(host)[0]
        changed, result, cluster_uuid = create_vsan_cluster(host_system, new_cluster_uuid)
        module.exit_json(changed=changed, result=result, cluster_uuid=cluster_uuid)

    except vmodl.RuntimeFault as runtime_fault:
        module.fail_json(msg=runtime_fault.msg)
    except vmodl.MethodFault as method_fault:
        module.fail_json(msg=method_fault.msg)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
