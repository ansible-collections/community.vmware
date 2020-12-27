#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# Copyright: (c) 2018, Ansible Project
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_cluster_vsan
short_description: Manages virtual storage area network (vSAN) configuration on VMware vSphere clusters
description:
    - Manages vSAN on VMware vSphere clusters.
    - All values and VMware object names are case sensitive.
author:
- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
- Mario Lenz (@mariolenz)
requirements:
    - Tested on ESXi 6.7.
    - PyVmomi installed.
    - vSAN Management SDK, which needs to be downloaded from VMware and installed manually.
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
    enable_vsan:
      description:
      - Whether to enable vSAN.
      type: bool
      default: false
    vsan_auto_claim_storage:
      description:
      - Whether the VSAN service is configured to automatically claim local storage
        on VSAN-enabled hosts in the cluster.
      type: bool
      default: false
    advanced_options:
      version_added: "1.1.0"
      description:
      - Advanced VSAN Options.
      suboptions:
        automatic_rebalance:
          description:
            - If enabled, vSAN automatically rebalances (moves the data among disks) when a capacity disk fullness hits proactive rebalance threshold.
          type: bool
        disable_site_read_locality:
          description:
            - For vSAN stretched clusters, reads to vSAN objects occur on the site the VM resides on.
            - Setting to C(True) will force reads across all mirrors.
          type: bool
        large_cluster_support:
          description:
            - Allow > 32 VSAN hosts per cluster; if this is changed on an existing vSAN cluster, all hosts are required to reboot to apply this change.
          type: bool
        object_repair_timer:
          description:
            - Delay time in minutes for VSAN to wait for the absent component to come back before starting to repair it.
          type: int
        thin_swap:
          description:
            - When C(enabled), swap objects would not reserve 100% space of their size on vSAN datastore.
          type: bool
      type: dict
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Enable vSAN
  community.vmware.vmware_cluster_vsan:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable_vsan: true
  delegate_to: localhost

- name: Enable vSAN and automatic rebalancing
  community.vmware.vmware_cluster_vsan:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: datacenter
    cluster_name: cluster
    enable_vsan: true
    advanced_options:
      automatic_rebalance: True
  delegate_to: localhost

- name: Enable vSAN and claim storage automatically
  community.vmware.vmware_cluster_vsan:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    datacenter_name: DC0
    cluster_name: "{{ cluster_name }}"
    enable_vsan: True
    vsan_auto_claim_storage: True
  delegate_to: localhost
'''

RETURN = r'''#
'''

import traceback

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

try:
    import vsanapiutils
    HAS_VSANPYTHONSDK = True
except ImportError:
    VSANPYTHONSDK_IMP_ERR = traceback.format_exc()
    HAS_VSANPYTHONSDK = False

from ansible.module_utils.basic import AnsibleModule, missing_required_lib
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    TaskError,
    find_datacenter_by_name,
    vmware_argument_spec,
    wait_for_task)
from ansible.module_utils._text import to_native


class VMwareCluster(PyVmomi):
    def __init__(self, module):
        super(VMwareCluster, self).__init__(module)
        self.cluster_name = module.params['cluster_name']
        self.datacenter_name = module.params['datacenter']
        self.enable_vsan = module.params['enable_vsan']
        self.datacenter = None
        self.cluster = None
        self.advanced_options = None

        self.datacenter = find_datacenter_by_name(self.content, self.datacenter_name)
        if self.datacenter is None:
            self.module.fail_json(msg="Datacenter %s does not exist." % self.datacenter_name)

        self.cluster = self.find_cluster_by_name(cluster_name=self.cluster_name, datacenter_name=self.datacenter)
        if self.cluster is None:
            self.module.fail_json(msg="Cluster %s does not exist." % self.cluster_name)

        if module.params['advanced_options'] is not None:
            self.advanced_options = module.params['advanced_options']
            client_stub = self.si._GetStub()
            ssl_context = client_stub.schemeArgs.get('context')
            apiVersion = vsanapiutils.GetLatestVmodlVersion(module.params['hostname'])
            vcMos = vsanapiutils.GetVsanVcMos(client_stub, context=ssl_context, version=apiVersion)
            self.vsanClusterConfigSystem = vcMos['vsan-cluster-config-system']

    def check_vsan_config_diff(self):
        """
        Check VSAN configuration diff
        Returns: True if there is diff, else False

        """
        vsan_config = self.cluster.configurationEx.vsanConfigInfo

        if vsan_config.enabled != self.enable_vsan or \
                vsan_config.defaultConfig.autoClaimStorage != self.params.get('vsan_auto_claim_storage'):
            return True

        if self.advanced_options is not None:
            vsan_config_info = self.vsanClusterConfigSystem.GetConfigInfoEx(self.cluster).extendedConfig
            if self.advanced_options['automatic_rebalance'] is not None and \
                    self.advanced_options['automatic_rebalance'] != vsan_config_info.proactiveRebalanceInfo.enabled:
                return True
            if self.advanced_options['disable_site_read_locality'] is not None and \
                    self.advanced_options['disable_site_read_locality'] != vsan_config_info.disableSiteReadLocality:
                return True
            if self.advanced_options['large_cluster_support'] is not None and \
                    self.advanced_options['large_cluster_support'] != vsan_config_info.largeScaleClusterSupport:
                return True
            if self.advanced_options['object_repair_timer'] is not None and \
                    self.advanced_options['object_repair_timer'] != vsan_config_info.objectRepairTimer:
                return True
            if self.advanced_options['thin_swap'] is not None and \
                    self.advanced_options['thin_swap'] != vsan_config_info.enableCustomizedSwapObject:
                return True

        return False

    def configure_vsan(self):
        """
        Manage VSAN configuration

        """
        changed, result = False, None

        if self.check_vsan_config_diff():
            if not self.module.check_mode:
                vSanSpec = vim.vsan.ReconfigSpec(
                    modify=True,
                )
                vSanSpec.vsanClusterConfig = vim.vsan.cluster.ConfigInfo(
                    enabled=self.enable_vsan
                )
                vSanSpec.vsanClusterConfig.defaultConfig = vim.vsan.cluster.ConfigInfo.HostDefaultInfo(
                    autoClaimStorage=self.params.get('vsan_auto_claim_storage')
                )
                if self.advanced_options is not None:
                    vSanSpec.extendedConfig = vim.vsan.VsanExtendedConfig()
                    if self.advanced_options['automatic_rebalance'] is not None:
                        vSanSpec.extendedConfig.proactiveRebalanceInfo = vim.vsan.ProactiveRebalanceInfo(
                            enabled=self.advanced_options['automatic_rebalance']
                        )
                    if self.advanced_options['disable_site_read_locality'] is not None:
                        vSanSpec.extendedConfig.disableSiteReadLocality = self.advanced_options['disable_site_read_locality']
                    if self.advanced_options['large_cluster_support'] is not None:
                        vSanSpec.extendedConfig.largeScaleClusterSupport = self.advanced_options['large_cluster_support']
                    if self.advanced_options['object_repair_timer'] is not None:
                        vSanSpec.extendedConfig.objectRepairTimer = self.advanced_options['object_repair_timer']
                    if self.advanced_options['thin_swap'] is not None:
                        vSanSpec.extendedConfig.enableCustomizedSwapObject = self.advanced_options['thin_swap']
                try:
                    task = self.vsanClusterConfigSystem.VsanClusterReconfig(self.cluster, vSanSpec)
                    changed, result = wait_for_task(vim.Task(task._moId, self.si._stub))
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

        self.module.exit_json(changed=changed, result=result)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(dict(
        cluster_name=dict(type='str', required=True),
        datacenter=dict(type='str', required=True, aliases=['datacenter_name']),
        # VSAN
        enable_vsan=dict(type='bool', default=False),
        vsan_auto_claim_storage=dict(type='bool', default=False),
        advanced_options=dict(type='dict', options=dict(
            automatic_rebalance=dict(type='bool', required=False),
            disable_site_read_locality=dict(type='bool', required=False),
            large_cluster_support=dict(type='bool', required=False),
            object_repair_timer=dict(type='int', required=False),
            thin_swap=dict(type='bool', required=False),
        )),
    ))

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if not HAS_VSANPYTHONSDK:
        module.fail_json(msg=missing_required_lib('vSAN Management SDK for Python'), exception=VSANPYTHONSDK_IMP_ERR)

    vmware_cluster_vsan = VMwareCluster(module)
    vmware_cluster_vsan.configure_vsan()


if __name__ == '__main__':
    main()
