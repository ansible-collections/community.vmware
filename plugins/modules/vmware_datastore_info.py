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
module: vmware_datastore_info
short_description: Gather info about datastores available in given vCenter
description:
    - This module can be used to gather information about datastores in VMWare infrastructure.
author:
    - Tim Rightnour (@garbled1)
options:
   name:
     description:
     - Name of the datastore to match.
     - If set, information of specific datastores are returned.
     required: false
     type: str
   datacenter:
     description:
     - Datacenter to search for datastores.
     - This parameter is required, if O(cluster) is not supplied.
     required: false
     aliases: ['datacenter_name']
     type: str
   cluster:
     description:
     - Cluster to search for datastores.
     - If set, information of datastores belonging this clusters will be returned.
     - This parameter is required, if O(datacenter) is not supplied.
     required: false
     type: str
   gather_nfs_mount_info:
    description:
    - Gather mount information of NFS datastores.
    - Disabled per default because this slows down the execution if you have a lot of datastores.
    - Only valid when O(schema=summary).
    type: bool
    default: false
   gather_vmfs_mount_info:
    description:
    - Gather mount information of VMFS datastores.
    - Disabled per default because this slows down the execution if you have a lot of datastores.
    - Only valid when O(schema=summary).
    type: bool
    default: false
   schema:
     description:
     - Specify the output schema desired.
     - The 'summary' output schema is the legacy output from the module
     - The 'vsphere' output schema is the vSphere API class definition
     choices: ['summary', 'vsphere']
     default: 'summary'
     type: str
   show_tag:
     description:
     - Tags related to Datastore are shown if set to V(true).
     default: false
     type: bool
   properties:
     description:
     - Specify the properties to retrieve.
     - If not specified, all properties are retrieved (deeply).
     - Results are returned in a structure identical to the vsphere API.
     - 'Example:'
     - '   properties: ['
     - '      "name",'
     - '      "info.vmfs.ssd",'
     - '      "capability.vsanSparseSupported",'
     - '      "overallStatus"'
     - '   ]'
     - Only valid when O(schema=vsphere).
     type: list
     required: false
     elements: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather info from standalone ESXi server having datacenter as 'ha-datacenter'
  community.vmware.vmware_datastore_info:
    hostname: '{{ esxi_hostname }}'
    username: '{{ esxi_username }}'
    password: '{{ esxi_password }}'
    datacenter_name: "ha-datacenter"
  delegate_to: localhost
  register: info

- name: Gather info from datacenter about specific datastore
  community.vmware.vmware_datastore_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    name: datastore1
  delegate_to: localhost
  register: info

- name: Gather some info from a datastore using the vSphere API output schema
  community.vmware.vmware_datastore_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    schema: vsphere
    properties:
      - name
      - info.vmfs.ssd
      - capability.vsanSparseSupported
      - overallStatus
  delegate_to: localhost
  register: info
'''

RETURN = r'''
datastores:
    description: metadata about the available datastores
    returned: always
    type: list
    sample: [
        {
            "accessible": false,
            "capacity": 42681237504,
            "datastore_cluster": "datacluster0",
            "freeSpace": 39638269952,
            "maintenanceMode": "normal",
            "multipleHostAccess": false,
            "name": "datastore2",
            "provisioned": 12289211488,
            "type": "VMFS",
            "uncommitted": 9246243936,
            "url": "ds:///vmfs/volumes/5a69b18a-c03cd88c-36ae-5254001249ce/",
            "vmfs_blockSize": 1024,
            "vmfs_uuid": "5a69b18a-c03cd88c-36ae-5254001249ce",
            "vmfs_version": "6.81"
        },
        {
            "accessible": true,
            "capacity": 5497558138880,
            "datastore_cluster": "datacluster0",
            "freeSpace": 4279000641536,
            "maintenanceMode": "normal",
            "multipleHostAccess": true,
            "name": "datastore3",
            "nfs_path": "/vol/datastore3",
            "nfs_server": "nfs_server1",
            "provisioned": 1708109410304,
            "type": "NFS",
            "uncommitted": 489551912960,
            "url": "ds:///vmfs/volumes/420b3e73-67070776/"
        },
    ]
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
    get_all_objs,
    find_cluster_by_name,
    get_parent_datacenter)
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec
from ansible_collections.community.vmware.plugins.module_utils.vmware_rest_client import VmwareRestClient


class VMwareHostDatastore(PyVmomi):
    """ This class populates the datastore list """

    def __init__(self, module):
        super(VMwareHostDatastore, self).__init__(module)
        self.gather_nfs_mount_info = self.module.params['gather_nfs_mount_info']
        self.gather_vmfs_mount_info = self.module.params['gather_vmfs_mount_info']
        self.schema = self.module.params['schema']
        self.properties = self.module.params['properties']
        if self.module.params['show_tag']:
            self.vmware_client = VmwareRestClient(self.module)

    def check_datastore_host(self, esxi_host, datastore):
        """ Get all datastores of specified ESXi host """
        esxi = self.find_hostsystem_by_name(esxi_host)
        if esxi is None:
            self.module.fail_json(msg="Failed to find ESXi hostname %s " % esxi_host)
        storage_system = esxi.configManager.storageSystem
        host_file_sys_vol_mount_info = storage_system.fileSystemVolumeInfo.mountInfo
        for host_mount_info in host_file_sys_vol_mount_info:
            if host_mount_info.volume.name == datastore:
                return host_mount_info
        return None

    def build_datastore_list(self, datastore_list):
        """ Build list with datastores """
        datastores = list()
        for datastore in datastore_list:
            if self.schema == 'summary':
                summary = datastore.summary
                datastore_summary = dict()
                datastore_summary['accessible'] = summary.accessible
                datastore_summary['capacity'] = summary.capacity
                datastore_summary['name'] = summary.name
                datastore_summary['freeSpace'] = summary.freeSpace
                datastore_summary['maintenanceMode'] = summary.maintenanceMode
                datastore_summary['multipleHostAccess'] = summary.multipleHostAccess
                datastore_summary['type'] = summary.type
                if self.gather_nfs_mount_info or self.gather_vmfs_mount_info:
                    if self.gather_nfs_mount_info and summary.type.startswith("NFS"):
                        # get mount info from the first ESXi host attached to this NFS datastore
                        host_mount_info = self.check_datastore_host(summary.datastore.host[0].key.name, summary.name)
                        datastore_summary['nfs_server'] = host_mount_info.volume.remoteHost
                        datastore_summary['nfs_path'] = host_mount_info.volume.remotePath
                    if self.gather_vmfs_mount_info and summary.type == "VMFS":
                        # get mount info from the first ESXi host attached to this VMFS datastore
                        host_mount_info = self.check_datastore_host(summary.datastore.host[0].key.name, summary.name)
                        datastore_summary['vmfs_blockSize'] = host_mount_info.volume.blockSize
                        datastore_summary['vmfs_version'] = host_mount_info.volume.version
                        datastore_summary['vmfs_uuid'] = host_mount_info.volume.uuid
                # uncommitted is optional / not always set
                if not summary.uncommitted:
                    summary.uncommitted = 0
                datastore_summary['uncommitted'] = summary.uncommitted
                datastore_summary['url'] = summary.url
                # Calculated values
                datastore_summary['provisioned'] = summary.capacity - summary.freeSpace + summary.uncommitted
                datastore_summary['datastore_cluster'] = 'N/A'
                if isinstance(datastore.parent, vim.StoragePod):
                    datastore_summary['datastore_cluster'] = datastore.parent.name

                if self.module.params['show_tag']:
                    datastore_summary['tags'] = self.vmware_client.get_tags_for_datastore(datastore._moId)

                if self.module.params['name']:
                    if datastore_summary['name'] == self.module.params['name']:
                        datastores.extend([datastore_summary])
                else:
                    datastores.extend([datastore_summary])
            else:
                temp_ds = self.to_json(datastore, self.properties)
                if self.module.params['show_tag']:
                    temp_ds.update({'tags': self.vmware_client.get_tags_for_datastore(datastore._moId)})
                if self.module.params['name']:
                    if datastore.name == self.module.params['name']:
                        datastores.extend(([temp_ds]))
                else:
                    datastores.extend(([temp_ds]))

        return datastores


class PyVmomiCache(object):
    """ This class caches references to objects which are requested multiples times but not modified """

    def __init__(self, content, dc_name=None):
        self.content = content
        self.dc_name = dc_name
        self.clusters = {}
        self.parent_datacenters = {}

    def get_all_objs(self, content, types, confine_to_datacenter=True):
        """ Wrapper around get_all_objs to set datacenter context """
        objects = get_all_objs(content, types)
        if confine_to_datacenter:
            if hasattr(objects, 'items'):
                # resource pools come back as a dictionary
                for k, v in tuple(objects.items()):
                    parent_dc = get_parent_datacenter(k)
                    if parent_dc.name != self.dc_name:
                        del objects[k]
            else:
                # everything else should be a list
                objects = [x for x in objects if get_parent_datacenter(x).name == self.dc_name]

        return objects


class PyVmomiHelper(PyVmomi):
    """ This class gets datastores """

    def __init__(self, module):
        super(PyVmomiHelper, self).__init__(module)
        self.cache = PyVmomiCache(self.content, dc_name=self.params['datacenter'])

    def lookup_datastore(self, confine_to_datacenter):
        """ Get datastore(s) per ESXi host or vCenter server """
        datastores = self.cache.get_all_objs(self.content, [vim.Datastore], confine_to_datacenter)
        return datastores

    def lookup_datastore_by_cluster(self):
        """ Get datastore(s) per cluster """
        cluster = find_cluster_by_name(self.content, self.params['cluster'])
        if not cluster:
            self.module.fail_json(msg='Failed to find cluster "%(cluster)s"' % self.params)
        c_dc = cluster.datastore
        return c_dc


def main():
    """ Main """
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type='str'),
        datacenter=dict(type='str', aliases=['datacenter_name']),
        cluster=dict(type='str'),
        gather_nfs_mount_info=dict(type='bool', default=False),
        gather_vmfs_mount_info=dict(type='bool', default=False),
        schema=dict(type='str', choices=['summary', 'vsphere'], default='summary'),
        properties=dict(type='list', elements='str'),
        show_tag=dict(type='bool', default=False),
    )
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True
                           )

    result = dict(changed=False)

    pyv = PyVmomiHelper(module)

    if module.params['cluster']:
        dxs = pyv.lookup_datastore_by_cluster()
    elif module.params['datacenter']:
        dxs = pyv.lookup_datastore(confine_to_datacenter=True)
    else:
        dxs = pyv.lookup_datastore(confine_to_datacenter=False)

    vmware_host_datastore = VMwareHostDatastore(module)
    datastores = vmware_host_datastore.build_datastore_list(dxs)

    result['datastores'] = datastores

    module.exit_json(**result)


if __name__ == '__main__':
    main()
