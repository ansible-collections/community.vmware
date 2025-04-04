#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Alexander Nikitin (ihumster@ihumster.ru)
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_host_graphics
version_added: '3.10.0'
short_description: Manage Host Graphic Settings
description:
- This module can be used to manage Host Graphic Settings
author:
- Alexander Nikitin (@ihumster)
options:
  cluster_name:
    description:
    - Name of cluster.
    - All host system from given cluster used to manage Host Graphic Settings.
    - Required parameter, if O(esxi_hostname) is not set.
    type: str
  esxi_hostname:
    description:
    - List of ESXi hostname to manage Host Graphic Settings.
    - Required parameter, if O(cluster_name) is not set.
    type: list
    elements: str
  graphic_type:
    description:
    - Default graphics type
    default: shared
    choices: [ shared, sharedDirect ]
    type: str
  assigment_policy:
    description:
    - Shared passthrough GPU assignment policy
    default: performance
    choices: [ consolidation, performance ]
    type: str
  restart_xorg:
    description:
    - Restart X.Org Server after change any parameter ( O(graphic_type) or O(assigment_policy) )
    default: False
    type: bool
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Change Host Graphics Settings
  community.vmware.vmware_host_graphics:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
    graphic_type: sharedDirect
    assigment_policy: consolidation
  delegate_to: localhost
'''

RETURN = r'''
results:
  description:
    - data about host system graphics settings.
  returned: always
  type: dict
  sample: {
      "changed": true,
      "esxi01": {
          "changed": false,
          "msg": "All Host Graphics Settings already configured"
      },
      "esxi02": {
          "changed": true,
          "msg": "New host graphics settings changed to: hostDefaultGraphicsType = 'shared', sharedPassthruAssignmentPolicy = 'performance'.X.Org was restarted"
      }
  }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible.module_utils._text import to_native


class VMwareHostGraphicSettings(PyVmomi):
    """ Main class for configuring Host Graphics Settings """
    def __init__(self, module):
        super(VMwareHostGraphicSettings, self).__init__(module)
        self.graphic_type = self.params['graphic_type']
        self.assigment_policy = self.params['assigment_policy']
        self.restart_xorg = self.params['restart_xorg']
        self.results = {"changed": False}
        esxi_hostname = self.params['esxi_hostname']
        cluster_name = self.params['cluster_name']
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_hostname)
        if self.hosts is None:
            self.module.fail_json(msg="Failed to find host system.")

    def ensure(self):
        """
        Function to manage host graphics
        """
        for host in self.hosts:
            self.results[host.name] = dict()
            if host.runtime.connectionState == "connected":
                hgm = host.configManager.graphicsManager
                hsm = host.configManager.serviceSystem
                changed = False
                current_config = hgm.graphicsConfig
                if current_config.hostDefaultGraphicsType != self.graphic_type:
                    changed = True
                    current_config.hostDefaultGraphicsType = self.graphic_type
                if current_config.sharedPassthruAssignmentPolicy != self.assigment_policy:
                    changed = True
                    current_config.sharedPassthruAssignmentPolicy = self.assigment_policy

                if changed:
                    if self.module.check_mode:
                        not_world = '' if self.restart_xorg else 'not '
                        self.results[host.name]['changed'] = False
                        self.results[host.name]['msg'] = f"New host graphics settings will be changed to: hostDefaultGraphicsType = \
                                                            '{current_config.hostDefaultGraphicsType}', sharedPassthruAssignmentPolicy = \
                                                            '{current_config.sharedPassthruAssignmentPolicy}'. \
                                                            X.Org will {not_world}be restarted."
                    else:
                        try:
                            hgm.UpdateGraphicsConfig(current_config)
                            if self.restart_xorg:
                                hsm.RestartService('xorg')
                            xorg_status = 'was restarted' if self.restart_xorg else 'was not restarted.'
                            self.results['changed'] = True
                            self.results[host.name]['changed'] = True
                            self.results[host.name]['msg'] = f"New host graphics settings changed to: hostDefaultGraphicsType = \
                                                                '{current_config.hostDefaultGraphicsType}', sharedPassthruAssignmentPolicy = \
                                                                '{current_config.sharedPassthruAssignmentPolicy}'. \
                                                                X.Org {xorg_status}"
                        except vim.fault.HostConfigFault as config_fault:
                            self.module.fail_json(
                                msg=f"Failed to configure host graphics settings for host {host.name} due to : {to_native(config_fault.msg)}"
                            )
                else:
                    self.results[host.name]['changed'] = False
                    self.results[host.name]['msg'] = 'All Host Graphics Settings have already been configured'
            else:
                self.results[host.name]['changed'] = False
                self.results[host.name]['msg'] = f"Host {host.name} is disconnected and cannot be changed"

        self.module.exit_json(**self.results)


def main():
    """ Main module method"""
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str'),
        esxi_hostname=dict(type='list', elements='str'),
        graphic_type=dict(type='str', default='shared', choices=['shared', 'sharedDirect']),
        assigment_policy=dict(type='str', default='performance', choices=['consolidation', 'performance']),
        restart_xorg=dict(type='bool', default=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
    )

    vmware_host_graphics = VMwareHostGraphicSettings(module)
    vmware_host_graphics.ensure()


if __name__ == "__main__":
    main()
