#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2019, David Hewitt <davidmhewitt@gmail.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_folder_info
short_description: Provides information about folders in a datacenter
description:
- The module can be used to gather a hierarchical view of the folders that exist within a datacenter
author:
- David Hewitt (@davidmhewitt)
options:
  datacenter:
    description:
    - Name of the datacenter.
    required: true
    type: str
    aliases: ['datacenter_name']
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Provide information about vCenter folders
  community.vmware.vmware_folder_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: datacenter_name
  delegate_to: localhost
  register: vcenter_folder_info

- name: Get information about folders
  community.vmware.vmware_folder_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: 'Asia-Datacenter1'
  register: r

- name: Set Managed object ID for the given folder
  ansible.builtin.set_fact:
    folder_mo_id: "{{ (r.flat_folder_info | selectattr('path', 'equalto', '/Asia-Datacenter1/vm/tier1/tier2') | map(attribute='moid'))[0] }}"
'''

RETURN = r'''
flat_folder_info:
    description:
    - list of dict about folders in flat structure
    returned: success
    type: list
    sample:
        [
            {
                "moid": "group-v3",
                "path": "/Asia-Datacenter1/vm"
            },
            {
                "moid": "group-v44",
                "path": "/Asia-Datacenter1/vm/tier1"
            },
            {
                "moid": "group-v45",
                "path": "/Asia-Datacenter1/vm/tier1/tier2"
            }
        ]
folder_info:
    description:
    - dict about folders
    returned: success
    type: dict
    sample:
        {
            "datastoreFolders": {
                "moid": "group-v10",
                "path": "/DC01/datastore",
                "subfolders": {
                    "Local Datastores": {
                        "path": "/DC01/datastore/Local Datastores",
                        "subfolders": {}
                    }
                }
            },
            "hostFolders": {
                "moid": "group-v21",
                "path": "/DC01/host",
                "subfolders": {}
            },
            "networkFolders": {
                "moid": "group-v31",
                "path": "/DC01/network",
                "subfolders": {}
            },
            "vmFolders": {
                "moid": "group-v41",
                "path": "/DC01/vm",
                "subfolders": {
                    "Core Infrastructure Servers": {
                        "moid": "group-v42",
                        "path": "/DC01/vm/Core Infrastructure Servers",
                        "subfolders": {
                            "Staging Network Services": {
                                "moid": "group-v43",
                                "path": "/DC01/vm/Core Infrastructure Servers/Staging Network Services",
                                "subfolders": {}
                            },
                            "VMware": {
                                "moid": "group-v44",
                                "path": "/DC01/vm/Core Infrastructure Servers/VMware",
                                "subfolders": {}
                            }
                        }
                    }
                }
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


class VmwareFolderInfoManager(PyVmomi):
    def __init__(self, module):
        super(VmwareFolderInfoManager, self).__init__(module)
        self.dc_name = self.params['datacenter']

    def gather_folder_info(self):
        datacenter = self.find_datacenter_by_name(self.dc_name)
        if datacenter is None:
            self.module.fail_json(msg="Failed to find the datacenter %s" % self.dc_name)

        folder_trees = {}
        folder_trees['vmFolders'] = self.build_folder_tree(datacenter.vmFolder, "/%s/vm" % self.dc_name)
        folder_trees['hostFolders'] = self.build_folder_tree(datacenter.hostFolder, "/%s/host" % self.dc_name)
        folder_trees['networkFolders'] = self.build_folder_tree(datacenter.networkFolder, "/%s/network" % self.dc_name)
        folder_trees['datastoreFolders'] = self.build_folder_tree(datacenter.datastoreFolder, "/%s/datastore" % self.dc_name)

        flat_folder_info = self.build_flat_folder_tree(datacenter.vmFolder, '/%s/vm' % self.dc_name)
        flat_folder_info.extend(self.build_flat_folder_tree(datacenter.hostFolder, "/%s/host" % self.dc_name))
        flat_folder_info.extend(self.build_flat_folder_tree(datacenter.networkFolder, "/%s/network" % self.dc_name))
        flat_folder_info.extend(self.build_flat_folder_tree(datacenter.datastoreFolder, "/%s/datastore" % self.dc_name))

        self.module.exit_json(
            changed=False,
            folder_info=folder_trees,
            flat_folder_info=flat_folder_info,
        )

    def build_flat_folder_tree(self, folder, path):
        ret = []
        tree = {
            'path': path,
            'moid': folder._moId,
        }

        ret.append(tree)

        children = None
        if hasattr(folder, 'childEntity'):
            children = folder.childEntity

        if children:
            for child in children:
                if child == folder:
                    continue
                if isinstance(child, vim.Folder):
                    ret.extend(self.build_flat_folder_tree(child, "%s/%s" % (path, child.name)))
        return ret

    def build_folder_tree(self, folder, path):
        tree = {
            'path': path,
            'subfolders': {},
            'moid': folder._moId,
        }

        children = None
        if hasattr(folder, 'childEntity'):
            children = folder.childEntity

        if children:
            for child in children:
                if child == folder:
                    continue
                if isinstance(child, vim.Folder):
                    ctree = self.build_folder_tree(child, "%s/%s" % (path, child.name))
                    tree['subfolders'][child.name] = dict.copy(ctree)
        return tree


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        datacenter=dict(type='str', required=True, aliases=['datacenter_name'])
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    vmware_folder_info_mgr = VmwareFolderInfoManager(module)
    vmware_folder_info_mgr.gather_folder_info()


if __name__ == "__main__":
    main()
