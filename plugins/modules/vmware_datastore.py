#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Tim Rightnour <thegarbledone@gmail.com>
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_datastore
short_description: Configure Datastores
version_added: '3.0.0'
description:
    - Configure Storage I/O Control Settings of a Datastore.
author:
    - Nina Loser (@Nina2244)
options:
   name:
     description: Name of the datastore.
     required: True
     type: str
   datacenter:
     description:
     - Datacenter to search for the datastores.
     aliases: ['datacenter_name']
     type: str
   storage_io_control:
     description:
     - Specify datastore typ.
     type: str
     choices: ['enable_io_statistics', 'enable_statistics', 'disable']
     required: True
   congestion_threshold_percentage:
     description:
     - Storage I/O congestion threshold in percentage of peak throughput.
     - "A value between 50% and 100%."
     - "Recommended: 90%"
     - Only use C(congestion_threshold_percentage) or C(congestion_threshold_manual).
     - Only valid when C(storage_io_control) is C(enable_io_statistics).
     type: int
     default: 90
   congestion_threshold_manual:
     description:
     - Storage I/O congestion threshold in ms.
     - Only use C(congestion_threshold_percentage) or C(congestion_threshold_manual).
     - Only valid when C(storage_io_control) is C(enable_io_statistics).
     type: int
   statistic_collection:
     description:
     - Include I/O statistics for SDRS.
     - Only valid when C(storage_io_control) is C(enable_io_statistics) or C(enable_statistics).
     type: bool
     default: true
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Configure Storage I/O Control of an mounted datastore
  community.vmware.vmware_datastore_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    name: datastore1
    storage_io_control: 'enable_io_statistics'
    congestion_threshold_manual: 30
    statistic_collection: true
  delegate_to: localhost
  register: info

'''

RETURN = r'''
result:
    description: Information about datastore operation.
    returned: always
    type: str
    sample: "Datastore configured successfully."
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    vmware_argument_spec,
    wait_for_task,
    TaskError)


class VMwareDatastore(PyVmomi):
    def __init__(self, module):
        super(VMwareDatastore, self).__init__(module)

        if self.module.params.get('congestion_threshold_percentage') not in range(50, 101):
            self.module.fail_json(msg="Congestion Threshold should be between 50% and 100%.")

        self.datacenter_name = self.module.params.get('datacenter')
        if self.datacenter_name:
            self.datacenter = self.find_datacenter_by_name(self.datacenter_name)
            if self.datacenter is None:
                self.module.fail_json(msg="Datacenter %s does not exist." % self.datacenter_name)
        else:
            self.datacenter = None

        self.datastore_name = self.module.params.get('name')
        self.datastore = self.find_datastore_by_name(self.datastore_name, self.datacenter)
        if self.datastore is None:
            self.module.fail_json(msg="Datastore %s does not exist." % self.name)

        self.storageResourceManager = self.content.storageResourceManager

    def check_config_diff(self):
        """
        Check configuration diff
        Returns: True if there is diff, else False
        """
        iormConfiguration = self.datastore.iormConfiguration

        conf_statsAggregationDisabled = not self.module.params.get('statistic_collection')

        if self.module.params.get('storage_io_control') == "enable_io_statistics":
            if self.module.params.get('congestion_threshold_manual') is not None:
                conf_congestionThresholdMode = 'manual'
                conf_congestionThreshold = self.module.params.get('congestion_threshold_manual')
                conf_percentOfPeakThroughput = iormConfiguration.percentOfPeakThroughput

            else:
                conf_congestionThresholdMode = 'automatic'
                conf_percentOfPeakThroughput = self.module.params.get('congestion_threshold_percentage')
                conf_congestionThreshold = iormConfiguration.congestionThreshold

            if iormConfiguration.enabled and \
                    iormConfiguration.statsCollectionEnabled and \
                    iormConfiguration.statsAggregationDisabled == conf_statsAggregationDisabled and \
                    iormConfiguration.congestionThresholdMode == conf_congestionThresholdMode and \
                    iormConfiguration.congestionThreshold == conf_congestionThreshold and \
                    iormConfiguration.percentOfPeakThroughput == conf_percentOfPeakThroughput:
                return False
            else:
                return True

        elif self.module.params.get('storage_io_control') == "enable_statistics":
            if not iormConfiguration.enabled and \
                    iormConfiguration.statsCollectionEnabled and \
                    iormConfiguration.statsAggregationDisabled == conf_statsAggregationDisabled:
                return False
            else:
                return True

        elif self.module.params.get('storage_io_control') == "disable":
            if not iormConfiguration.enabled and \
                    not iormConfiguration.statsCollectionEnabled:
                return False
            else:
                return True

    def configure(self):
        """
        Manage configuration
        """
        changed = self.check_config_diff()

        if changed:
            if not self.module.check_mode:
                config_spec = vim.StorageResourceManager.IORMConfigSpec()

                iormConfiguration = self.datastore.iormConfiguration

                conf_statsAggregationDisabled = not self.module.params.get('statistic_collection')

                if self.module.params.get('storage_io_control') == "enable_io_statistics":
                    if self.module.params.get('congestion_threshold_manual') is not None:
                        config_spec.congestionThresholdMode = 'manual'
                        config_spec.congestionThreshold = self.module.params.get('congestion_threshold_manual')
                        config_spec.percentOfPeakThroughput = iormConfiguration.percentOfPeakThroughput

                    else:
                        config_spec.congestionThresholdMode = 'automatic'
                        config_spec.percentOfPeakThroughput = self.module.params.get('congestion_threshold_percentage')
                        config_spec.congestionThreshold = iormConfiguration.congestionThreshold

                    config_spec.enabled = True
                    config_spec.statsCollectionEnabled = True
                    config_spec.statsAggregationDisabled = conf_statsAggregationDisabled

                elif self.module.params.get('storage_io_control') == "enable_statistics":
                    config_spec.enabled = False
                    config_spec.statsCollectionEnabled = True
                    config_spec.statsAggregationDisabled = conf_statsAggregationDisabled

                elif self.module.params.get('storage_io_control') == "disable":
                    config_spec.enabled = False
                    config_spec.statsCollectionEnabled = False

                try:
                    task = self.storageResourceManager.ConfigureDatastoreIORM_Task(self.datastore, config_spec)
                    changed, result = wait_for_task(task)
                except TaskError as generic_exc:
                    self.module.fail_json(msg=to_native(generic_exc))
                except Exception as task_e:
                    self.module.fail_json(msg=to_native(task_e))
            else:
                changed = True

        results = dict(changed=changed)
        self.module.exit_json(**results)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        name=dict(type='str', required=True),
        datacenter=dict(type='str', aliases=['datacenter_name']),
        storage_io_control=dict(type='str', choices=['enable_io_statistics', 'enable_statistics', 'disable'], required=True),
        congestion_threshold_percentage=dict(type='int', default=90, required=False),
        congestion_threshold_manual=dict(type='int', required=False),
        statistic_collection=dict(type='bool', default=True, required=False)
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[
            ['congestion_threshold_percentage', 'congestion_threshold_manual'],
        ]
    )

    vmware_datastore = VMwareDatastore(module)
    vmware_datastore.configure()


if __name__ == '__main__':
    main()
