#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Karsten Kaj Jakobsen <kj@patientsky.com>
# Copyright: (c) 2020, Ansible Project
# Copyright: (c) 2020, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_drs_group_manager
author:
  - Abhijeet Kasurde (@Akasurde)
short_description: Manage VMs and Hosts in DRS group.
description:
  - The module can be used to add VMs / Hosts to or remove them from a DRS group.
extends_documentation_fragment:
- community.vmware.vmware.documentation
notes:
  - Tested on vSphere 6.5, and 6.7.
options:
  cluster:
    description:
      - Cluster to which DRS group associated with.
    required: true
    type: str
    aliases:
      - cluster_name
  datacenter:
    aliases:
      - datacenter_name
    description:
      - Name of the datacenter.
    required: false
    type: str
  group_name:
    description:
      - The name of the group to manage.
    required: true
    type: str
  hosts:
    description:
      - A List of hosts to add / remove in the group.
      - Required only if I(vms) is not set.
    required: false
    type: list
    elements: str
  vms:
    description:
      - A List of vms to add / remove in the group.
      - Required only if I(hosts) is not set.
    required: false
    type: list
    elements: str
  state:
    choices: [ present, absent ]
    default: present
    description:
      - If set to C(present), VMs/hosts will be added to the given DRS group.
      - If set to C(absent), VMs/hosts will be removed from the given DRS group.
    type: str
requirements:
  - "python >= 2.7"
  - PyVmomi
version_added: '1.7.0'
'''

EXAMPLES = r'''
---
- name: Add VMs in an existing DRS VM group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_VM_01
    vms:
      - DC0_C0_RP0_VM0
      - DC0_C0_RP0_VM1
    state: present

- name: Add Hosts in an existing DRS Host group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_HOST_01
    hosts:
      - DC0_C0_H0
      - DC0_C0_H1
      - DC0_C0_H2
    state: present

- name: Remove VM from an existing DRS VM group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_VM_01
    vms:
      - DC0_C0_RP0_VM0
    state: absent

- name: Remove host from an existing DRS Host group
  delegate_to: localhost
  community.vmware.vmware_drs_group_manager:
    hostname: "{{ vcenter_hostname }}"
    password: "{{ vcenter_password }}"
    username: "{{ vcenter_username }}"
    cluster: DC0_C0
    datacenter: DC0
    group_name: TEST_HOST_01
    hosts:
      - DC0_C0_H0
    state: absent

'''

RETURN = r'''
drs_group_member_info:
    description: Metadata about DRS group
    returned: always
    type: dict
    sample: {
        "Asia-Cluster1": [
            {
                "group_name": "vm_group_002",
                "type": "vm",
                "vms": [
                    "dev-1"
                ]
            }
        ]
    }
msg:
    description: Info message
    returned: always
    type: str
    sample: "Updated host group TEST_HOST_01 successfully"
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    vmware_argument_spec,
    wait_for_task,
    find_vm_by_id)


class VmwareDrsGroupMemberManager(PyVmomi):
    """
    Class to manage DRS group members
    """

    def __init__(self, module):
        """
        Init
        """

        super(VmwareDrsGroupMemberManager, self).__init__(module)

        self._datacenter_name = module.params.get('datacenter')
        self._datacenter_obj = None
        self._cluster_name = module.params.get('cluster')
        self._cluster_obj = None
        self._group_name = module.params.get('group_name')
        self._group_obj = None
        self._operation = None
        self._vm_list = module.params.get('vms')
        self._vm_obj_list = []
        self._host_list = module.params.get('hosts')
        self._host_obj_list = []
        self.message = 'Nothing to see here...'
        self.result = dict()
        self.changed = False
        self._state = module.params.get('state')

        if self._datacenter_name is not None:
            self._datacenter_obj = self.find_datacenter_by_name(self._datacenter_name)

            if self._datacenter_obj is None:
                raise Exception("Datacenter '%s' not found" % self._datacenter_name)

        self._cluster_obj = self.find_cluster_by_name(self._cluster_name, self._datacenter_obj)

        # Throw error if cluster does not exist
        if self._cluster_obj is None:
            raise Exception("Cluster '%s' not found" % self._cluster_name)

        # get group
        self._group_obj = self._get_group_by_name()
        # Set result here. If nothing is to be updated, result is already set
        self._set_result(self._group_obj)

        self._operation = 'edit' if self._state == 'present' else 'remove'

        if self._vm_list is not None:
            self._set_vm_obj_list(vm_list=self._vm_list)

        if self._host_list is not None:
            self._set_host_obj_list(host_list=self._host_list)

    def _set_result(self, group_obj):
        """
        Creates result for successful run
        Args:
            group_obj: group object

        Returns: None

        """
        self.result = dict()

        if self._cluster_obj is not None and group_obj is not None:
            self.result[self._cluster_obj.name] = []
            self.result[self._cluster_obj.name].append(self._normalize_group_data(group_obj))

    def _set_vm_obj_list(self, vm_list=None, cluster_obj=None):
        """
        Populate vm object list from list of vms
        Args:
            vm_list: List of vm names

        Returns: None

        """

        if vm_list is None:
            vm_list = self._vm_list

        if cluster_obj is None:
            cluster_obj = self._cluster_obj

        if vm_list is not None:
            for vm in vm_list:
                if self.module.check_mode is False:
                    # Get host data
                    vm_obj = find_vm_by_id(content=self.content, vm_id=vm,
                                           vm_id_type='vm_name', cluster=cluster_obj)
                    if vm_obj is None:
                        raise Exception("VM %s does not exist in cluster %s" % (vm,
                                                                                self._cluster_name))
                    self._vm_obj_list.append(vm_obj)

    def _set_host_obj_list(self, host_list=None):
        """
        Populate host object list from list of hostnames
        Args:
            host_list: List of host names

        Returns: None

        """

        if host_list is None:
            host_list = self._host_list

        if host_list is not None:
            for host in host_list:
                if self.module.check_mode is False:
                    # Get host data
                    host_obj = self.find_hostsystem_by_name(host)
                    if host_obj is None and self.module.check_mode is False:
                        raise Exception("ESXi host %s does not exist in cluster %s" % (host, self._cluster_name))
                    self._host_obj_list.append(host_obj)

    def _get_group_by_name(self, group_name=None, cluster_obj=None):
        """
        Get group by name
        Args:
            group_name: Name of group
            cluster_obj: vim Cluster object

        Returns: Group Object if found or None

        """

        if group_name is None:
            group_name = self._group_name

        if cluster_obj is None:
            cluster_obj = self._cluster_obj

        # Allow for group check even if dry run
        if self.module.check_mode and cluster_obj is None:
            return None

        for group in cluster_obj.configurationEx.group:
            if group.name == group_name:
                return group

        # No group found
        return None

    def _populate_vm_host_list(self, group_name=None, cluster_obj=None, host_group=False):
        """
        Return all VMs/Hosts names using given group name
        Args:
            group_name: group name
            cluster_obj: Cluster managed object
            host_group: True if we want only host name from group

        Returns: List of VMs/Hosts names belonging to given group object

        """
        obj_name_list = []

        if group_name is None:
            group_name = self._group_name

        if cluster_obj is None:
            cluster_obj = self._cluster_obj

        if not all([group_name, cluster_obj]):
            return obj_name_list

        group = self._group_obj

        if not host_group and isinstance(group, vim.cluster.VmGroup):
            obj_name_list = [vm.name for vm in group.vm]

        elif host_group and isinstance(group, vim.cluster.HostGroup):
            obj_name_list = [host.name for host in group.host]

        return obj_name_list

    def _check_if_vms_hosts_changed(self, group_name=None, cluster_obj=None, host_group=False):
        """
        Check if VMs/Hosts changed
        Args:
            group_name: Name of group
            cluster_obj: vim Cluster object
            host_group: True if we want to check hosts, else check vms

        Returns: Bool

        """

        if group_name is None:
            group_name = self._group_name

        if cluster_obj is None:
            cluster_obj = self._cluster_obj

        list_a = self._host_list if host_group else self._vm_list
        list_b = self._populate_vm_host_list(host_group=host_group)

        # By casting lists as a set, you remove duplicates and order doesn't count. Comparing sets is also much faster and more efficient than comparing lists.
        if set(list_a) == set(list_b):
            if self._operation != 'remove':
                return False
        return True

    def _manage_host_group(self):
        # Check if anything has changed when editing
        if self._check_if_vms_hosts_changed(host_group=True):

            need_reconfigure = False
            group = vim.cluster.HostGroup()
            group.name = self._group_name
            group.host = self._group_obj.host or []

            # Modify existing hosts
            for host in self._host_obj_list:
                if self._operation == 'edit' and host not in group.host:
                    group.host.append(host)
                    need_reconfigure = True
                if self._operation == 'remove' and host in group.host:
                    group.host.remove(host)
                    need_reconfigure = True

            group_spec = vim.cluster.GroupSpec(info=group, operation='edit')
            config_spec = vim.cluster.ConfigSpecEx(groupSpec=[group_spec])

            if not self.module.check_mode and need_reconfigure:
                task = self._cluster_obj.ReconfigureEx(config_spec, modify=True)
                self.changed, dummy = wait_for_task(task)

            # Set new result since something changed
            self._set_result(group)
            if self.changed:
                self.message = "Updated host group %s successfully" % self._group_name
            else:
                self.message = "No update to host group %s" % self._group_name
        else:
            self.changed = False
            self.message = "No update to host group %s" % self._group_name

    def _manage_vm_group(self):

        # Check if anything has changed when editing
        if self._check_if_vms_hosts_changed():
            need_reconfigure = False
            group = vim.cluster.VmGroup()
            group.name = self._group_name
            group.vm = self._group_obj.vm or []

            # Modify existing VMs
            for vm in self._vm_obj_list:
                if self._operation == 'edit' and vm not in group.vm:
                    group.vm.append(vm)
                    need_reconfigure = True
                if self._operation == 'remove' and vm in group.vm:
                    group.vm.remove(vm)
                    need_reconfigure = True

            group_spec = vim.cluster.GroupSpec(info=group, operation='edit')
            config_spec = vim.cluster.ConfigSpecEx(groupSpec=[group_spec])

            # Check if dry run
            if not self.module.check_mode and need_reconfigure:
                task = self._cluster_obj.ReconfigureEx(config_spec, modify=True)
                self.changed, dummy = wait_for_task(task)

            self._set_result(group)
            if self.changed:
                self.message = "Updated vm group %s successfully" % self._group_name
            else:
                self.message = "No update to vm group %s" % self._group_name
        else:
            self.changed = False
            self.message = "No update to vm group %s" % self._group_name

    def _normalize_group_data(self, group_obj):
        """
        Return human readable group spec
        Args:
            group_obj: Group object

        Returns: DRS group object fact

        """
        if not all([group_obj]):
            return {}

        # Check if group is a host group
        if hasattr(group_obj, 'host'):
            return dict(
                group_name=group_obj.name,
                hosts=self._host_list,
                type="host"
            )
        return dict(
            group_name=group_obj.name,
            vms=self._vm_list,
            type="vm"
        )

    def manage_drs_group_members(self):
        """
        Add a DRS host/vm group members
        """

        if self._vm_list is None:
            self._manage_host_group()
        elif self._host_list is None:
            self._manage_vm_group()
        else:
            raise Exception('Failed, no hosts or vms defined')


def main():
    """
    Main function
    """

    argument_spec = vmware_argument_spec()
    argument_spec.update(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        datacenter=dict(type='str', required=False, aliases=['datacenter_name']),
        cluster=dict(type='str', required=True, aliases=['cluster_name']),
        group_name=dict(type='str', required=True),
        vms=dict(type='list', elements='str'),
        hosts=dict(type='list', elements='str')
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[['vms', 'hosts']],
        required_one_of=[['vms', 'hosts']]
    )

    try:
        # Create instance of VmwareDrsGroupMemberManager
        vmware_drs_group = VmwareDrsGroupMemberManager(module=module)
        vmware_drs_group.manage_drs_group_members()

        # Set results
        results = dict(msg=vmware_drs_group.message,
                       failed=False,
                       changed=vmware_drs_group.changed,
                       drs_group_member_info=vmware_drs_group.result)

    except Exception as error:
        results = dict(failed=True, msg="Error: %s" % error)

    if results['failed']:
        module.fail_json(**results)
    module.exit_json(**results)


if __name__ == "__main__":
    main()
