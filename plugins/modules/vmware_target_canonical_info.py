#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_target_canonical_info
short_description: Return canonical (NAA) from an ESXi host system
description:
    - This module can be used to gather information about canonical (NAA) from an ESXi host based on SCSI target ID.
author:
- Joseph Callen (@jcpowermac)
- Abhijeet Kasurde (@Akasurde)
options:
  target_id:
    description:
    - The target id based on order of scsi device.
    - version 2.6 onwards, this parameter is optional.
    required: false
    type: int
  cluster_name:
    description:
    - Name of the cluster.
    - Info about all SCSI devices for all host system in the given cluster is returned.
    - This parameter is required, if O(esxi_hostname) is not provided.
    type: str
  esxi_hostname:
    description:
    - Name of the ESXi host system.
    - Info about all SCSI devices for the given ESXi host system is returned.
    - This parameter is required, if O(cluster_name) is not provided.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Get Canonical name of particular target on particular ESXi host system
  community.vmware.vmware_target_canonical_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    target_id: 7
    esxi_hostname: esxi_hostname
  delegate_to: localhost

- name: Get Canonical name of all target on particular ESXi host system
  community.vmware.vmware_target_canonical_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost

- name: Get Canonical name of all ESXi hostname on particular Cluster
  community.vmware.vmware_target_canonical_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: '{{ cluster_name }}'
  delegate_to: localhost
'''

RETURN = r'''
canonical:
    description: metadata about SCSI Target device
    returned: if host system and target id is given
    type: str
    sample: "mpx.vmhba0:C0:T0:L0"

scsi_tgt_info:
    description: metadata about all SCSI Target devices
    returned: if host system or cluster is given
    type: dict
    sample: {
        "DC0_C0_H0": {
            "scsilun_canonical": {
                "key-vim.host.ScsiDisk-0000000000766d686261303a303a30": "mpx.vmhba0:C0:T0:L0",
                "key-vim.host.ScsiLun-0005000000766d686261313a303a30": "mpx.vmhba1:C0:T0:L0"
            },
            "target_lun_uuid": {
                "0": "key-vim.host.ScsiDisk-0000000000766d686261303a303a30"
            }
        },
        "DC0_C0_H1": {
            "scsilun_canonical": {
                "key-vim.host.ScsiDisk-0000000000766d686261303a303a30": "mpx.vmhba0:C0:T0:L0",
                "key-vim.host.ScsiLun-0005000000766d686261313a303a30": "mpx.vmhba1:C0:T0:L0"
            },
            "target_lun_uuid": {
                "0": "key-vim.host.ScsiDisk-0000000000766d686261303a303a30"
            }
        },
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class ScsiTargetInfoManager(PyVmomi):
    def __init__(self, module):
        super(ScsiTargetInfoManager, self).__init__(module)
        cluster_name = self.module.params.get('cluster_name')
        self.esxi_hostname = self.module.params.get('esxi_hostname')
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=self.esxi_hostname)

    def gather_scsi_device_info(self):
        """
        Function to gather information about SCSI target devices

        """
        scsi_tgt_info = {}
        target_lun_uuid = {}
        scsilun_canonical = {}
        target_id = self.module.params['target_id']

        for host in self.hosts:
            # Associate the scsiLun key with the canonicalName (NAA)
            for scsilun in host.config.storageDevice.scsiLun:
                scsilun_canonical[scsilun.key] = scsilun.canonicalName

            # Associate target number with LUN uuid
            for target in host.config.storageDevice.scsiTopology.adapter[0].target:
                for lun in target.lun:
                    target_lun_uuid[target.target] = lun.scsiLun

            scsi_tgt_info[host.name] = dict(
                scsilun_canonical=scsilun_canonical,
                target_lun_uuid=target_lun_uuid)

        if target_id is not None and self.esxi_hostname is not None:
            canonical = ''
            temp_lun_data = scsi_tgt_info[self.esxi_hostname]['target_lun_uuid']
            if self.esxi_hostname in scsi_tgt_info and \
                    target_id in temp_lun_data:
                temp_scsi_data = scsi_tgt_info[self.esxi_hostname]['scsilun_canonical']
                temp_target = temp_lun_data[target_id]
                canonical = temp_scsi_data[temp_target]
            self.module.exit_json(changed=False, canonical=canonical)

        self.module.exit_json(changed=False, scsi_tgt_info=scsi_tgt_info)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        dict(
            target_id=dict(required=False, type='int'),
            cluster_name=dict(type='str', required=False),
            esxi_hostname=dict(type='str', required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True,
    )

    scsi_tgt_manager = ScsiTargetInfoManager(module)
    scsi_tgt_manager.gather_scsi_device_info()


if __name__ == '__main__':
    main()
