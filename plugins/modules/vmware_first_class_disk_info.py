#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Nina Loser <nina.loser@muenchen.de>
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_first_class_disk_info
short_description: Gather info about VMware vSphere First Class Disks
description:
    - This module can be used to gather information about VMware vSphere First Class Disks.
author:
- Nina Loser (@nina2244)
options:
    datacenter_name:
      description: The name of the datacenter.
      type: str
    datastore_name:
      description: Name of datastore or datastore cluster of the disk.
      required: true
      type: str
    disk_name:
      description: The name of the disk. If not set return all found.
      type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: Gather info of 1GBDisk
  community.vmware.vmware_first_class_disk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_name: '{{ datastore_name }}'
    disk_name: '1GBDisk'
  register: disk_info
  delegate_to: localhost

- debug:
    var: disk_info.first_class_disks

- name: Gather info of all first class disks
  community.vmware.vmware_first_class_disk_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_name: '{{ datastore_name }}'
  register: disk_info
  delegate_to: localhost

- debug:
    var: disk_info.first_class_disks
'''

RETURN = r'''
first_class_disks:
  description: list of dictionary of First-class disk and their information
  returned: success
  type: list
  sample: [
    {
      "name": "1GBDisk",
      "datastore_name": "DS0",
      "size_mb": "1024",
      "consumption_type": "disk",
      "descriptor_version": 0,
      "consumer_ids": []
    }
  ]
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class FirstClassDiskInfo(PyVmomi):
    def __init__(self, module):
        super(FirstClassDiskInfo, self).__init__(module)
        self.datacenter_name = self.params['datacenter_name']
        self.datastore_name = self.params['datastore_name']
        self.disk_name = self.params['disk_name']

    def gather_first_class_disk_info(self):
        self.datastore_obj = self.find_datastore_by_name(datastore_name=self.datastore_name, datacenter_name=self.datacenter_name)
        if not self.datastore_obj:
            self.module.fail_json(msg='Failed to find datastore %s.' % self.datastore_name)

        if self.disk_name:
            self.disk_obj = self.find_first_class_disk_by_name(self.disk_name, self.datastore_obj)
            if not self.disk_obj:
                self.module.fail_json(msg='Failed to find disk %s.' % self.disk_name)

            self.disks = [self.disk_obj]

        else:
            self.disks = self.find_first_class_disks(self.datastore_obj)
            if not self.disks:
                return []

        disk_infos = list()
        for disk in self.disks:
            disk_info = dict(
                name=disk.config.name,
                id=disk.config.id.id,
                datastore_name=disk.config.backing.datastore.name,
                size_mb=disk.config.capacityInMB,
                consumption_type=disk.config.consumptionType,
                descriptor_version=disk.config.descriptorVersion,
                consumer_ids=list(id.id for id in disk.config.consumerId)
            )
            disk_infos.append(disk_info)

        return disk_infos


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        dict(
            datacenter_name=dict(type='str'),
            datastore_name=dict(required=True, type='str'),
            disk_name=dict(type='str')
        )
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    first_class_disk = FirstClassDiskInfo(module)

    _first_class_disks = first_class_disk.gather_first_class_disk_info()

    module.exit_json(changed=False, first_class_disks=_first_class_disks)


if __name__ == '__main__':
    main()
