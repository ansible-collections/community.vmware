#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, Ansible Project
# Copyright: (c) 2019, Pavan Bidkar <pbidkar@vmware.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_content_deploy_template
deprecated:
  removed_in: 7.0.0
  why: This module has been moved to the L(new vmware.vmware collection,https://forum.ansible.com/t/5880)
  alternative: Use M(vmware.vmware.deploy_content_library_template) instead.
short_description: Deploy Virtual Machine from template stored in content library.
description:
- Module to deploy virtual machine from template in content library.
- Content Library feature is introduced in vSphere 6.0 version.
- vmtx templates feature is introduced in vSphere 67U1 and APIs for clone template from content library in 67U2.
- This module does not work with vSphere version older than 67U2.
author:
- Pavan Bidkar (@pgbidkar)
requirements:
- vSphere Automation SDK
options:
    log_level:
      description:
      - The level of logging desired in this module.
      type: str
      required: false
      default: 'normal'
      choices: [ 'debug', 'info', 'normal' ]
    template:
      description:
      - The name of template from which VM to be deployed.
      type: str
      required: true
      aliases: ['template_src']
    library:
      description:
      - The name of the content library from where the template resides.
      type: str
      required: false
      aliases: ['content_library', 'content_library_src']
    name:
      description:
      - The name of the VM to be deployed.
      type: str
      required: true
      aliases: ['vm_name']
    datacenter:
      description:
      - Name of the datacenter, where VM to be deployed.
      type: str
      required: true
    datastore:
      description:
      - Name of the datastore to store deployed VM and disk.
      - Required if O(datastore_cluster) is not provided.
      type: str
      required: false
    datastore_cluster:
      description:
      - Name of the datastore cluster to store deployed VM and disk.
      - Please make sure Storage DRS is active for recommended datastore from the given datastore cluster.
      - If Storage DRS is not enabled, datastore with largest free storage space is selected.
      - Required if O(datastore) is not provided.
      type: str
      required: false
    folder:
      description:
      - Name of the folder in datacenter in which to place deployed VM.
      type: str
      default: 'vm'
    host:
      description:
      - Name of the ESX Host in datacenter in which to place deployed VM.
      - The host has to be a member of the cluster that contains the resource pool.
      - Required with O(resource_pool) to find resource pool details. This will be used as additional
        information when there are resource pools with same name.
      type: str
      required: false
    resource_pool:
      description:
      - Name of the resource pool in datacenter in which to place deployed VM.
      - Required if O(cluster) is not specified.
      - For default or non-unique resource pool names, specify O(host) and O(cluster).
      - C(Resources) is the default name of resource pool.
      type: str
      required: false
    cluster:
      description:
      - Name of the cluster in datacenter in which to place deployed VM.
      - Required if O(resource_pool) is not specified.
      type: str
      required: false
    state:
      description:
      - The state of Virtual Machine deployed from template in content library.
      - If set to V(present) and VM does not exists, then VM is created.
      - If set to V(present) and VM exists, no action is taken.
      - If set to V(poweredon) and VM does not exists, then VM is created with powered on state.
      - If set to V(poweredon) and VM exists, no action is taken.
      type: str
      required: false
      default: 'present'
      choices: [ 'present', 'poweredon' ]
extends_documentation_fragment:
- vmware.vmware.base_options
- vmware.vmware.additional_rest_options

'''

EXAMPLES = r'''
- name: Deploy Virtual Machine from template in content library
  community.vmware.vmware_content_deploy_template:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    template: rhel_test_template
    datastore: Shared_NFS_Volume
    folder: vm
    datacenter: Sample_DC_1
    name: Sample_VM
    resource_pool: test_rp
    state: present
  delegate_to: localhost

- name: Deploy Virtual Machine from template in content library with PowerON State
  community.vmware.vmware_content_deploy_template:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    template: rhel_test_template
    content_library: test_content_library
    datastore: Shared_NFS_Volume
    folder: vm
    datacenter: Sample_DC_1
    name: Sample_VM
    resource_pool: test_rp
    state: poweredon
  delegate_to: localhost
'''

RETURN = r'''
vm_deploy_info:
  description: Virtual machine deployment message and vm_id
  returned: on success
  type: dict
  sample: {
        "msg": "Deployed Virtual Machine 'Sample_VM'.",
        "vm_id": "vm-1009"
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import rest_compatible_argument_spec
from ansible.module_utils.common.text.converters import to_native

HAS_VAUTOMATION_PYTHON_SDK = False
try:
    from com.vmware.vcenter.vm_template_client import LibraryItems
    from com.vmware.vapi.std.errors_client import Error
    HAS_VAUTOMATION_PYTHON_SDK = True
except ImportError:
    pass


class VmwareContentDeployTemplate(VmwareRestClient):
    def __init__(self, module):
        """Constructor."""
        super(VmwareContentDeployTemplate, self).__init__(module)

        # Initialize member variables
        self.module = module
        self._pyv = PyVmomi(module=module)
        self._template_service = self.api_client.vcenter.vm_template.LibraryItems
        self._datacenter_id = None
        self._datastore_id = None
        self._library_item_id = None
        self._folder_id = None
        self._host_id = None
        self._cluster_id = None
        self._resourcepool_id = None
        self.result = {}

        # Turn on debug if not specified, but ANSIBLE_DEBUG is set
        if self.module._debug:
            self.warn('Enable debug output because ANSIBLE_DEBUG was set.')
            self.params['log_level'] = 'debug'
        self.log_level = self.params['log_level']
        if self.log_level == 'debug':
            # Turn on debugging
            self.result['debug'] = {}

        # Get parameters
        self.template = self.params.get('template')
        self.library = self.params.get('library')
        self.vm_name = self.params.get('name')
        self.datacenter = self.params.get('datacenter')
        self.datastore = self.params.get('datastore')
        self.datastore_cluster = self.params.get('datastore_cluster')
        self.folder = self.params.get('folder')
        self.resourcepool = self.params.get('resource_pool')
        self.cluster = self.params.get('cluster')
        self.host = self.params.get('host')

        vm = self._pyv.get_vm()
        if vm:
            self.result['vm_deploy_info'] = dict(
                msg="Virtual Machine '%s' already Exists." % self.vm_name,
                vm_id=vm._moId,
            )
            self._fail(msg="Virtual Machine deployment failed")

    def deploy_vm_from_template(self, power_on=False):
        # Find the datacenter by the given datacenter name
        self._datacenter_id = self.get_datacenter_by_name(self.datacenter)
        if not self._datacenter_id:
            self._fail(msg="Failed to find the datacenter %s" % self.datacenter)

        # Find the datastore by the given datastore name
        if self.datastore:
            self._datastore_id = self.get_datastore_by_name(self.datacenter, self.datastore)
            if not self._datastore_id:
                self._fail(msg="Failed to find the datastore %s" % self.datastore)

        # Find the datastore by the given datastore cluster name
        if self.datastore_cluster and not self._datastore_id:
            dsc = self._pyv.find_datastore_cluster_by_name(self.datastore_cluster)
            if dsc:
                self.datastore = self._pyv.get_recommended_datastore(dsc)
                self._datastore_id = self.get_datastore_by_name(self.datacenter, self.datastore)
            else:
                self._fail(msg="Failed to find the datastore cluster %s" % self.datastore_cluster)

        if not self._datastore_id:
            self._fail(msg="Failed to find the datastore using either datastore or datastore cluster")

        # Find the LibraryItem (Template) by the given LibraryItem name
        if self.library:
            self._library_item_id = self.get_library_item_from_content_library_name(
                self.template, self.library
            )
            if not self._library_item_id:
                self._fail(msg="Failed to find the library Item %s in content library %s" % (self.template, self.library))
        else:
            self._library_item_id = self.get_library_item_by_name(self.template)
            if not self._library_item_id:
                self._fail(msg="Failed to find the library Item %s" % self.template)

        # Find the folder by the given FQPN folder name
        # The FQPN is I(datacenter)/I(folder type)/folder name/... for
        # example Lab/vm/someparent/myfolder is a vm folder in the Lab datacenter.
        folder_obj = self._pyv.find_folder_by_fqpn(self.folder, self.datacenter, folder_type='vm')
        if folder_obj:
            self._folder_id = folder_obj._moId
        if not self._folder_id:
            self._fail(msg="Failed to find the folder %s" % self.folder)

        # Find the Host by the given name
        if self.host:
            self._host_id = self.get_host_by_name(self.datacenter, self.host)
            if not self._host_id:
                self._fail(msg="Failed to find the Host %s" % self.host)

        # Find the Cluster by the given Cluster name
        if self.cluster:
            self._cluster_id = self.get_cluster_by_name(self.datacenter, self.cluster)
            if not self._cluster_id:
                self._fail(msg="Failed to find the Cluster %s" % self.cluster)
            cluster_obj = self.api_client.vcenter.Cluster.get(self._cluster_id)
            self._resourcepool_id = cluster_obj.resource_pool

        # Find the resourcepool by the given resourcepool name
        if self.resourcepool:
            self._resourcepool_id = self.get_resource_pool_by_name(self.datacenter, self.resourcepool, self.cluster, self.host)
            if not self._resourcepool_id:
                self._fail(msg="Failed to find the resource_pool %s" % self.resourcepool)

        # Create VM placement specs
        self.placement_spec = LibraryItems.DeployPlacementSpec(folder=self._folder_id)
        if self._host_id:
            self.placement_spec.host = self._host_id
        if self._resourcepool_id:
            self.placement_spec.resource_pool = self._resourcepool_id
        if self._cluster_id:
            self.placement_spec.cluster = self._cluster_id
        self.vm_home_storage_spec = LibraryItems.DeploySpecVmHomeStorage(
            datastore=to_native(self._datastore_id)
        )
        self.disk_storage_spec = LibraryItems.DeploySpecDiskStorage(
            datastore=to_native(self._datastore_id)
        )
        self.deploy_spec = LibraryItems.DeploySpec(
            name=self.vm_name,
            placement=self.placement_spec,
            vm_home_storage=self.vm_home_storage_spec,
            disk_storage=self.disk_storage_spec,
            powered_on=power_on
        )
        vm_id = ''
        try:
            vm_id = self._template_service.deploy(self._library_item_id, self.deploy_spec)
        except Error as error:
            self._fail(msg="%s" % self.get_error_message(error))
        except Exception as err:
            self._fail(msg="%s" % to_native(err))

        if not vm_id:
            self.result['vm_deploy_info'] = dict(
                msg="Virtual Machine deployment failed",
                vm_id=''
            )
            self._fail(msg="Virtual Machine deployment failed")
        self.result['changed'] = True
        self.result['vm_deploy_info'] = dict(
            msg="Deployed Virtual Machine '%s'." % self.vm_name,
            vm_id=vm_id,
        )
        self._exit()

    #
    # Wrap AnsibleModule methods
    #

    def _mod_debug(self):
        if self.log_level == 'debug':
            self.result['debug'] = dict(
                datacenter_id=self._datacenter_id,
                datastore_id=self._datastore_id,
                library_item_id=self._library_item_id,
                folder_id=self._folder_id,
                host_id=self._host_id,
                cluster_id=self._cluster_id,
                resourcepool_id=self._resourcepool_id
            )

    def _fail(self, msg):
        self._mod_debug()
        self.module.fail_json(msg=msg, **self.result)

    def _exit(self):
        self._mod_debug()
        self.module.exit_json(**self.result)


def main():
    argument_spec = rest_compatible_argument_spec()
    argument_spec.update(
        log_level=dict(
            type='str',
            choices=[
                'debug',
                'info',
                'normal',
            ],
            default='normal'
        ),
        state=dict(
            type='str',
            choices=[
                'present',
                'poweredon'
            ],
            default='present'
        ),
        template=dict(
            type='str',
            aliases=[
                'template_src'
            ],
            required=True
        ),
        library=dict(
            type='str',
            aliases=[
                'content_library',
                'content_library_src',
            ],
            required=False
        ),
        name=dict(
            type='str',
            aliases=[
                'vm_name'
            ],
            required=True,
        ),
        datacenter=dict(
            type='str',
            required=True
        ),
        datastore=dict(
            type='str',
            required=False
        ),
        datastore_cluster=dict(
            type='str',
            required=False
        ),
        folder=dict(
            type='str',
            default='vm'
        ),
        host=dict(
            type='str',
            required=False
        ),
        resource_pool=dict(
            type='str',
            required=False
        ),
        cluster=dict(
            type='str',
            required=False
        ),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=[
            ['datastore', 'datastore_cluster'],
            ['host', 'cluster'],
        ],
    )

    result = {'failed': False, 'changed': False}
    vmware_contentlib_create = VmwareContentDeployTemplate(module)
    if module.params['state'] == 'present':
        if module.check_mode:
            result.update(
                vm_name=module.params['name'],
                changed=True,
                desired_operation='Create VM with PowerOff State',
            )
            module.exit_json(**result)
        vmware_contentlib_create.deploy_vm_from_template()
    elif module.params['state'] == 'poweredon':
        if module.check_mode:
            result.update(
                vm_name=module.params['name'],
                changed=True,
                desired_operation='Create VM with PowerON State',
            )
            module.exit_json(**result)
        vmware_contentlib_create.deploy_vm_from_template(power_on=True)
    else:
        result.update(
            vm_name=module.params['name'],
            changed=False,
            desired_operation="State '%s' is not implemented" % module.params['state']
        )
        module.fail_json(**result)


if __name__ == '__main__':
    main()
