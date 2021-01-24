#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Mario Lenz <m@riolenz.de>
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: vmware_first_class_disk
short_description: Manage VMware vSphere First Class Disks
version_added: '1.7.0'
description:
    - This module can be used to manage (create, delete, resize) VMware vSphere First Class Disks.
author:
- Mario Lenz (@mariolenz)
notes:
    - Tested on vSphere 7.0
requirements:
    - "python >= 2.6"
    - PyVmomi
options:
    datacenter_name:
      description: The name of the datacenter.
      type: str
    datastore_name:
      description: Name of datastore or datastore cluster to be used for the disk.
      required: True
      type: str
    disk_name:
      description: The name of the disk.
      required: True
      type: str
    size:
      description:
        - Disk storage size, an integer plus a unit.
        - There is no space allowed in between size number and unit.
        - Allowed units are MB, GB and TB.
        - 'Examples:'
        - '   size: 2048MB'
        - '   size: 10GB'
        - '   size: 1TB'
      type: str
    state:
      description: If the disk should be present or absent.
      choices: [ present, absent ]
      default: present
      type: str
extends_documentation_fragment: vmware.documentation
'''

EXAMPLES = r'''
- name: Create Disk
  community.vmware.vmware_first_class_disk:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_name: '{{ datastore_name }}'
    disk_name: '1GBDisk'
    size: '1GB'
    state: present
  delegate_to: localhost

- name: Delete Disk
  community.vmware.vmware_first_class_disk:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datastore_name: '{{ datastore_name }}'
    disk_name: 'FirstClassDisk'
    state: absent
  delegate_to: localhost
'''

RETURN = r'''
first_class_disk:
  description: First-class disk returned when created, deleted or changed
  returned: changed
  type: dict
  sample: >
    {
      "name": "1GBDisk"
      "datastore_name": "DS0"
      "size_mb": "1024"
      "state": "present"
    }
'''

import re
try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, TaskError, vmware_argument_spec, wait_for_task
from ansible.module_utils._text import to_native


class FirstClassDisk(PyVmomi):
    def __init__(self, module):
        super(FirstClassDisk, self).__init__(module)
        self.datacenter_name = self.params['datacenter_name']
        self.datastore_name = self.params['datastore_name']
        self.disk_name = self.params['disk_name']
        self.desired_state = module.params['state']

        self.size_mb = None
        if self.params['size']:
            size_regex = re.compile(r'(\d+)([MGT]B)')
            disk_size_m = size_regex.match(self.params['size'])
            if disk_size_m:
                number = disk_size_m.group(1)
                unit = disk_size_m.group(2)
            else:
                self.module.fail_json(msg="Failed to parse disk size, please review value provided using documentation.")

            number = int(number)
            if unit == "GB":
                self.size_mb = 1024 * number
            elif unit == "TB":
                self.size_mb = 1048576 * number
            else:
                self.size_mb = number

        self.datastore_obj = self.find_datastore_by_name(datastore_name=self.datastore_name, datacenter_name=self.datacenter_name)
        if not self.datastore_obj:
            self.module.fail_json(msg='Failed to find datastore %s.' % self.datastore_name)

        self.disk = self.find_first_class_disk_by_name(self.disk_name, self.datastore_obj)

    def create_fcd_result(self, state):
        result = dict(
            name=self.disk.config.name,
            datastore_name=self.disk.config.backing.datastore.name,
            size_mb=self.disk.config.capacityInMB,
            state=state
        )

        return result

    def create(self):
        result = dict(changed=False)
        if not self.disk:
            result['changed'] = True
            if not self.module.check_mode:
                backing_spec = vim.vslm.CreateSpec.DiskFileBackingSpec()
                backing_spec.datastore = self.datastore_obj

                vslm_create_spec = vim.vslm.CreateSpec()
                vslm_create_spec.backingSpec = backing_spec
                vslm_create_spec.capacityInMB = self.size_mb
                vslm_create_spec.name = self.disk_name

                try:
                    if self.is_vcenter():
                        task = self.content.vStorageObjectManager.CreateDisk_Task(vslm_create_spec)
                    else:
                        task = self.content.vStorageObjectManager.HostCreateDisk_Task(vslm_create_spec)
                    changed, self.disk = wait_for_task(task)
                except vmodl.RuntimeFault as runtime_fault:
                    self.module.fail_json(msg=to_native(runtime_fault.msg))
                except vmodl.MethodFault as method_fault:
                    self.module.fail_json(msg=to_native(method_fault.msg))
                except TaskError as task_e:
                    self.module.fail_json(msg=to_native(task_e))
                except Exception as generic_exc:
                    self.module.fail_json(msg="Failed to create disk"
                                              " due to generic exception %s" % to_native(generic_exc))

                result['diff'] = {'before': {}, 'after': {}}
                result['diff']['before']['first_class_disk'] = self.create_fcd_result('absent')
                result['diff']['after']['first_class_disk'] = self.create_fcd_result('present')
                result['first_class_disk'] = result['diff']['after']['first_class_disk']
        else:
            if self.size_mb < self.disk.config.capacityInMB:
                self.module.fail_json(msg="Given disk size is smaller than current size (%dMB < %dMB). "
                                          "Reducing disks is not allowed."
                                          % (self.size_mb, self.disk.config.capacityInMB))
            elif self.size_mb > self.disk.config.capacityInMB:
                result['changed'] = True
                if not self.module.check_mode:
                    result['diff'] = {'before': {}, 'after': {}}
                    result['diff']['before']['first_class_disk'] = self.create_fcd_result('present')
                    try:
                        if self.is_vcenter():
                            task = self.content.vStorageObjectManager.ExtendDisk_Task(self.disk.config.id,
                                                                                      self.datastore_obj,
                                                                                      self.size_mb)
                        else:
                            task = self.content.vStorageObjectManager.HostExtendDisk_Task(self.disk.config.id,
                                                                                          self.datastore_obj,
                                                                                          self.size_mb)
                        wait_for_task(task)
                    except vmodl.RuntimeFault as runtime_fault:
                        self.module.fail_json(msg=to_native(runtime_fault.msg))
                    except vmodl.MethodFault as method_fault:
                        self.module.fail_json(msg=to_native(method_fault.msg))
                    except TaskError as task_e:
                        self.module.fail_json(msg=to_native(task_e))
                    except Exception as generic_exc:
                        self.module.fail_json(msg="Failed to increase disk size"
                                                  " due to generic exception %s" % to_native(generic_exc))

                    self.disk = self.find_first_class_disk_by_name(self.disk_name, self.datastore_obj)
                    result['diff']['after']['first_class_disk'] = self.create_fcd_result('present')
                    result['first_class_disk'] = result['diff']['after']['first_class_disk']

        self.module.exit_json(**result)

    def delete(self):
        result = dict(changed=False)
        if self.disk:
            result['changed'] = True
            if not self.module.check_mode:
                result['diff'] = {'before': {}, 'after': {}}
                result['diff']['before']['first_class_disk'] = self.create_fcd_result('present')
                result['diff']['after']['first_class_disk'] = self.create_fcd_result('absent')
                result['first_class_disk'] = result['diff']['after']['first_class_disk']

                try:
                    if self.is_vcenter():
                        task = self.content.vStorageObjectManager.DeleteVStorageObject_Task(self.disk.config.id,
                                                                                            self.datastore_obj)
                    else:
                        task = self.content.vStorageObjectManager.HostDeleteVStorageObject_Task(self.disk.config.id,
                                                                                                self.datastore_obj)
                    wait_for_task(task)
                except vmodl.RuntimeFault as runtime_fault:
                    self.module.fail_json(msg=to_native(runtime_fault.msg))
                except vmodl.MethodFault as method_fault:
                    self.module.fail_json(msg=to_native(method_fault.msg))
                except TaskError as task_e:
                    self.module.fail_json(msg=to_native(task_e))
                except Exception as generic_exc:
                    self.module.fail_json(msg="Failed to delete disk"
                                              " due to generic exception %s" % to_native(generic_exc))

        self.module.exit_json(**result)


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update(
        dict(
            datacenter_name=dict(type='str'),
            datastore_name=dict(required=True, type='str'),
            disk_name=dict(required=True, type='str'),
            size=dict(type='str'),
            state=dict(default='present', choices=['present', 'absent'], type='str')
        )
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           required_if=[
                               ['state', 'present', ['size']]
                           ],
                           supports_check_mode=True)

    first_class_disk = FirstClassDisk(module)

    if first_class_disk.desired_state == 'present':
        first_class_disk.create()
    if first_class_disk.desired_state == 'absent':
        first_class_disk.delete()


if __name__ == '__main__':
    main()
