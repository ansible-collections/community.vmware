#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_logbundle
short_description: Fetch logbundle file from ESXi
description:
    - This module can be used to fetch logbundle file from ESXi.
author:
    - sky-joker (@sky-joker)
options:
    esxi_hostname:
      description:
        - Name of the host system to fetch the logbundle.
      type: str
      required: true
    dest:
      description:
        - file destination on localhost, path must be exist.
      type: str
      required: true
    download_timeout:
      version_added: 4.5.0
      description:
        - The user defined timeout in seconds of exporting the log file.
        - The default of the function this module uses is so low that you have to set this this to a higher value in all probabilty.
      type: int
    manifests:
      description:
        - Logs to include in the logbundle file.
        - Refer to the id key of the M(community.vmware.vmware_host_logbundle_info) module for values that can be specified in the manifest.
      default:
        - System:Base
        - System:CoreDumps
        - System:EsxImage
        - System:IOFilter
        - System:LoadESX
        - System:Modules
        - System:RDMA
        - System:ResourceGroups
        - System:TPM
        - System:VFlash
        - System:VMTools
        - System:VmiofPlugins
        - System:ntp
        - System:uwstats
        - Fcd:Catalog
        - VirtualMachines:CoreDumps
        - VirtualMachines:VirtualMachineStats
        - VirtualMachines:base
        - VirtualMachines:base
        - VirtualMachines:diskinfo
        - VirtualMachines:logs
        - Storage:FCoE
        - Storage:Multipathing
        - Storage:NAS
        - Storage:VSAN
        - Storage:VSANHealth
        - Storage:VSANIscsiTarget
        - Storage:VSANPerfStats
        - Storage:VSANPerfSvc
        - Storage:VSANTraces
        - Storage:VVOL
        - Storage:base
        - Storage:iodm
        - Storage:iscsi
        - FeatureStateSwitch:FeatureStateSwitch
        - Userworld:HostAgent
        - Userworld:ProcessInformation
        - Configuration:System
        - Logs:System
        - hostProfiles:SystemImageCacheHostProfile
        - hostProfiles:hostProfiles
        - FileSystem:VMFSDiskDump
        - FileSystem:base
        - ActiveDirectory:base
        - CIM:base
        - Hardware:base
        - Hardware:usb
        - Installer:base
        - Network:base
        - Network:dvs
        - Network:lacp
        - Network:nscd
        - Network:tcpip
        - IntegrityChecks:md5sums
      type: list
      elements: str
      required: false
    performance_data:
      description:
        - Gather performance data for ESXi.
      type: dict
      required: false
      suboptions:
        duration:
          description:
            - Duration for which performance data is gathered.
          type: int
          default: 300
        interval:
          description:
            - Interval for which performance data is gathered.
          type: int
          default: 5
extends_documentation_fragment:
    - vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: fetch logbundle file from ESXi
  community.vmware.vmware_host_logbundle:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    dest: ./esxi-log.tgz

- name: fetch logbundle file from ESXi with manifests
  community.vmware.vmware_host_logbundle:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    dest: ./esxi-log.tgz
    manifests:
      - System:Base
      - VirtualMachines:VirtualMachineStats
'''

RETURN = r'''
dest:
    description: saved path of a logbundle file for ESXi
    returned: on success
    type: str
    sample:
      {
        "changed": true,
        "dest": "./esxi-log.tgz",
        "failed": false,
        "gid": 0,
        "group": "root",
        "mode": "0644",
        "owner": "root",
        "size": 25783140,
        "state": "file",
        "uid": 0
      }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

import xml.etree.ElementTree as ET

from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url


class VMwareHostLogbundle(PyVmomi):
    def __init__(self, module):
        super(VMwareHostLogbundle, self).__init__(module)
        self.esxi_hostname = self.params['esxi_hostname']
        self.dest = self.params['dest']
        self.manifests = self.params['manifests']
        self.performance_data = self.params['performance_data']
        self.download_timeout = self.params['download_timeout']

        if not self.dest.endswith('.tgz'):
            self.dest = self.dest + '.tgz'

    def generate_req_headers(self, url):
        # get ticket
        req = vim.SessionManager.HttpServiceRequestSpec(method='httpGet', url=url)
        ticket = self.content.sessionManager.AcquireGenericServiceTicket(req)

        headers = {
            'Content-Type': 'application/octet-stream',
            'Cookie': 'vmware_cgi_ticket=%s' % ticket.id
        }

        return headers

    def validate_manifests(self):
        url = 'https://' + self.esxi_hostname + '/cgi-bin/vm-support.cgi?listmanifests=1'
        headers = self.generate_req_headers(url)

        manifests = []
        try:
            resp, info = fetch_url(self.module, method='GET', headers=headers, url=url)
            if info['status'] != 200:
                self.module.fail_json(msg="failed to fetch manifests from %s: %s" % (url, info['msg']))
            manifest_list = ET.fromstring(resp.read())
            for manifest in manifest_list[0]:
                manifests.append(manifest.attrib['id'])

        except Exception as e:
            self.module.fail_json(msg="Failed to fetch manifests from %s: %s" % (url, e))

        for manifest in self.manifests:
            validate_manifest_result = [m for m in manifests if m == manifest]
            if not validate_manifest_result:
                self.module.fail_json(msg="%s is a manifest that cannot be specified." % manifest)

    def get_logbundle(self):
        self.validate_manifests()
        url = 'https://' + self.esxi_hostname + '/cgi-bin/vm-support.cgi?manifests=' + '%20'.join(self.manifests)

        if self.performance_data:
            duration = self.performance_data.get('duration')
            interval = self.performance_data.get('interval')
            url = url + '&performance=true&duration=%s&interval=%s' % (duration, interval)

        headers = self.generate_req_headers(url)

        try:
            if self.download_timeout is not None:
                resp, info = fetch_url(self.module, method='GET', headers=headers, url=url, timeout=self.download_timeout)
            else:
                resp, info = fetch_url(self.module, method='GET', headers=headers, url=url)
            if info['status'] != 200:
                self.module.fail_json(msg="failed to fetch logbundle from %s: %s" % (url, info['msg']))
            with open(self.dest, 'wb') as local_file:
                local_file.write(resp.read())

        except Exception as e:
            self.module.fail_json(msg="Failed to fetch logbundle from %s: %s" % (url, e))

        self.module.exit_json(changed=True, dest=self.dest)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        esxi_hostname=dict(type='str', required=True),
        dest=dict(type='str', required=True),
        download_timeout=dict(type='int'),
        manifests=dict(type='list', elements='str',
                       default=['System:Base', 'System:CoreDumps', 'System:EsxImage', 'System:IOFilter',
                                'System:LoadESX', 'System:Modules', 'System:RDMA', 'System:ResourceGroups',
                                'System:TPM', 'System:VFlash', 'System:VMTools', 'System:VmiofPlugins', 'System:ntp',
                                'System:uwstats', 'Fcd:Catalog', 'VirtualMachines:CoreDumps',
                                'VirtualMachines:VirtualMachineStats', 'VirtualMachines:base', 'VirtualMachines:base',
                                'VirtualMachines:diskinfo', 'VirtualMachines:logs', 'Storage:FCoE',
                                'Storage:Multipathing', 'Storage:NAS', 'Storage:VSAN', 'Storage:VSANHealth',
                                'Storage:VSANIscsiTarget', 'Storage:VSANPerfStats', 'Storage:VSANPerfSvc',
                                'Storage:VSANTraces', 'Storage:VVOL', 'Storage:base', 'Storage:iodm', 'Storage:iscsi',
                                'FeatureStateSwitch:FeatureStateSwitch', 'Userworld:HostAgent',
                                'Userworld:ProcessInformation', 'Configuration:System', 'Logs:System',
                                'hostProfiles:SystemImageCacheHostProfile', 'hostProfiles:hostProfiles',
                                'FileSystem:VMFSDiskDump', 'FileSystem:base', 'ActiveDirectory:base', 'CIM:base',
                                'Hardware:base', 'Hardware:usb', 'Installer:base', 'Network:base', 'Network:dvs',
                                'Network:lacp', 'Network:nscd', 'Network:tcpip', 'IntegrityChecks:md5sums']),
        performance_data=dict(type='dict', required=False,
                              options=dict(
                                  duration=dict(type='int', default=300),
                                  interval=dict(type='int', default=5)
                              ))
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_host_logbundle_mgr = VMwareHostLogbundle(module)
    vmware_host_logbundle_mgr.get_logbundle()


if __name__ == "__main__":
    main()
