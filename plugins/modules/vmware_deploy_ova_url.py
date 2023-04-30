#!/usr/bin/python
# -*- coding: utf-8 -*-

# based on code vmware_deploy_ovf from Matt Martz <matt@sivel.net>
# Copyright: (c) 2023, Alexander Nikitin <alexander@ihumster.ru>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
author: 'Alexander Nikitin (@ihumster)'
short_description: 'Deploys a VMware virtual machine from an OVA file placed on HTTP server'
description:
- 'This module can be used to deploy a VMware VM from an OVA file placed on HTTP server'
module: vmware_deploy_ova_url
notes: []
options:
    allow_duplicates:
        default: "True"
        description:
          - Whether or not to allow duplicate VM names. ESXi allows duplicates, vCenter may not.
        type: bool
    datacenter:
        default: ha-datacenter
        description:
        - Datacenter to deploy to.
        type: str
    cluster:
        description:
        - Cluster to deploy to.
        - This is a required parameter, if C(esxi_hostname) is not set and C(hostname) is set to the vCenter server.
        - C(esxi_hostname) and C(cluster) are mutually exclusive parameters.
        - This parameter is case sensitive.
        type: str
    esxi_hostname:
        description:
        - The ESXi hostname where the virtual machine will run.
        - This is a required parameter, if C(cluster) is not set and C(hostname) is set to the vCenter server.
        - C(esxi_hostname) and C(cluster) are mutually exclusive parameters.
        - This parameter is case sensitive.
        type: str
    datastore:
        default: datastore1
        description:
        - Datastore to deploy to.
        type: str
    deployment_option:
        description:
        - The key of the chosen deployment option.
        type: str
    disk_provisioning:
        choices:
        - flat
        - eagerZeroedThick
        - monolithicSparse
        - twoGbMaxExtentSparse
        - twoGbMaxExtentFlat
        - thin
        - sparse
        - thick
        - seSparse
        - monolithicFlat
        default: thin
        description:
        - Disk provisioning type.
        type: str
    fail_on_spec_warnings:
        description:
        - Cause the module to treat OVF Import Spec warnings as errors.
        default: false
        type: bool
    folder:
        description:
        - Absolute path of folder to place the virtual machine.
        - If not specified, defaults to the value of C(datacenter.vmFolder).
        - 'Examples:'
        - '   folder: /ha-datacenter/vm'
        - '   folder: ha-datacenter/vm'
        - '   folder: /datacenter1/vm'
        - '   folder: datacenter1/vm'
        - '   folder: /datacenter1/vm/folder1'
        - '   folder: datacenter1/vm/folder1'
        - '   folder: /folder1/datacenter1/vm'
        - '   folder: folder1/datacenter1/vm'
        - '   folder: /folder1/datacenter1/vm/folder2'
        type: str
    inject_ovf_env:
        description:
        - Force the given properties to be inserted into an OVF Environment and injected through VMware Tools.
        type: bool
        default: False
    name:
        description:
        - Name of the VM to work with.
        - Virtual machine names in vCenter are not necessarily unique, which may be problematic.
        type: str
    networks:
        default:
            VM Network: VM Network
        description:
        - 'C(key: value) mapping of OVF network name, to the vCenter network name.'
        type: dict
    ova:
        description:
        - 'URL for OVA file to deploy.'
        type: str
    power_on:
        default: true
        description:
        - 'Whether or not to power on the virtual machine after creation.'
        type: bool
    properties:
        description:
        - The assignment of values to the properties found in the OVF as key value pairs.
        type: dict
    resource_pool:
        default: Resources
        description:
        - Resource Pool to deploy to.
        type: str
    wait:
        default: true
        description:
        - 'Wait for the host to power on.'
        type: bool
    wait_for_ip_address:
        default: false
        description:
        - Wait until vCenter detects an IP address for the VM.
        - This requires vmware-tools (vmtoolsd) to properly work after creation.
        type: bool
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- community.vmware.vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    ova: https://cloud-images.ubuntu.com/releases/xenial/release/ubuntu-16.04-server-cloudimg-amd64.ova
    wait_for_ip_address: true
  delegate_to: localhost

# Deploys a new VM named 'NewVM' in specific datacenter/cluster, with network mapping taken from variable and using ova template from URL
- community.vmware.vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: Datacenter1
    cluster: Cluster1
    datastore: vsandatastore
    name: NewVM
    networks: "{u'VM Network':u'{{ ProvisioningNetworkLabel }}'}"
    power_on: no
    ova: http://youserver.com/mytemplate.ova
  delegate_to: localhost

- community.vmware.vmware_deploy_ovf:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter: Datacenter1
    esxi_hostname: test-server
    datastore: test-datastore
    ova: https://cloud-images.ubuntu.com/releases/xenial/release/ubuntu-16.04-server-cloudimg-amd64.ova
  delegate_to: localhost
'''


RETURN = r'''
instance:
    description: metadata about the new virtual machine
    returned: always
    type: dict
    sample: None
'''

from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    find_network_by_name,
    find_vm_by_name,
    PyVmomi,
    gather_vm_facts,
    vmware_argument_spec,
    wait_for_task,
    wait_for_vm_ip,
    set_vm_power_state)
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ansible.module_utils.six.moves.urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import re
import hashlib
import ssl
import time
import tarfile


try:
    from ansible_collections.community.vmware.plugins.module_utils.vmware import vim
    from pyVmomi import vmodl
except ImportError:
    pass


class WebHandle(object):
    def __init__(self, url):
        self.url = url
        self.thumbprint = None
        self.ssl_context = None

        self.parsed_url = self._parse_url(url)

        self.https = self.parsed_url.group('scheme') == 'https://'

        if self.https:
            self.ssl_context = ssl._create_default_https_context()
            self.ssl_context.check_hostname = False
            self.ssl_context.verify_mode = ssl.CERT_NONE

            self.thumbprint = self._get_thumbprint(
                self.parsed_url.group('hostname'))
            r = urlopen(url=url, context=self.ssl_context)
        else:
            r = urlopen(url)
        if r.code != 200:
            raise FileNotFoundError(url)
        self.headers = self._headers_to_dict(r)
        if 'accept-ranges' not in self.headers:
            raise Exception("Site does not accept ranges")
        self.st_size = int(self.headers['content-length'])
        self.offset = 0

    def _parse_url(self, url):
        exp = r"(?P<url>(?:(?P<scheme>[a-zA-Z]+:\/\/)?(?P<hostname>(?:[-a-zA-Z0-9@%_\+~#=]{1,256}\.){1,256}(?:[-a-zA-Z0-9@%_\+~#=]{1,256})))(?::(?P<port>[[:digit:]]+))?(?P<path>(?:\/[-a-zA-Z0-9!$&'()*+,\\\/:;=@\[\]._~%]*)*)(?P<query>(?:(?:\#|\?)[-a-zA-Z0-9!$&'()*+,\\\/:;=@\[\]._~]*)*))"
        return re.match(exp, url)

    def _get_thumbprint(self, hostname):
        pem = ssl.get_server_certificate((hostname, 443))
        sha1 = hashlib.sha1(
            ssl.PEM_cert_to_DER_cert(pem)).hexdigest().upper()
        colon_notion = ':'.join(sha1[i:i + 2] for i in range(0, len(sha1), 2))

        return None if sha1 is None else colon_notion

    def _headers_to_dict(self, r):
        result = {}
        if hasattr(r, 'getheaders'):
            for n, v in r.getheaders():
                result[n.lower()] = v.strip()
        else:
            for line in r.info().headers:
                if line.find(':') != -1:
                    n, v = line.split(': ', 1)
                    result[n.lower()] = v.strip()
        return result

    def tell(self):
        return self.offset

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = self.st_size - offset
        return self.offset

    def seekable(self):
        return True

    def read(self, amount):
        start = self.offset
        end = self.offset + amount - 1
        req = Request(self.url,
                      headers={'Range': 'bytes=%d-%d' % (start, end)})
        r = urlopen(req) if not self.ssl_context else urlopen(
            req, context=self.ssl_context)
        self.offset += amount
        result = r.read(amount)
        r.close()
        return result

    # A slightly more accurate percentage
    def progress(self):
        return int(100.0 * self.offset / self.st_size)


class OVAUploader(PyVmomi):
    def __init__(self, module):
        super(OVAUploader, self).__init__(module)

        self.module = module
        self.params = module.params

        self.handle = None
        self.datastore = None
        self.datacenter = None
        self.resource_pool = None
        self.network_mappings = []

        self.ovf_descriptor = None
        self.tar = None

        self.lease = None
        self.import_spec = None
        self.entity = None

    def get_objects(self):
        # Get datacenter firstly
        self.datacenter = self.find_datacenter_by_name(
            self.params['datacenter'])
        if self.datacenter is None:
            self.module.fail_json(
                msg=f"Datacenter '{self.params['datacenter']}' could not be located")

        # Get cluster in datacenter if cluster configured
        if self.params['cluster']:
            cluster = self.find_cluster_by_name(
                self.params['cluster'], datacenter_name=self.datacenter)
            if cluster is None:
                self.module.fail_json(
                    msg=f"Unable to find cluster '{self.params['cluster']}'")
            self.resource_pool = self.find_resource_pool_by_cluster(
                self.params['resource_pool'], cluster=cluster)
        # Or get ESXi host in datacenter if ESXi host configured
        elif self.params['esxi_hostname']:
            host = self.find_hostsystem_by_name(
                self.params['esxi_hostname'], datacenter=self.datacenter)
            if host is None:
                self.module.fail_json(
                    msg=f"Unable to find host '{self.params['esxi_hostname']}' in datacenter"
                        " '{self.params['datacenter']}'")
            self.resource_pool = self.find_resource_pool_by_name(
                self.params['resource_pool'], folder=host.parent)
        else:
            # For more than one datacenter env, specify 'folder' to datacenter hostFolder
            self.resource_pool = self.find_resource_pool_by_name(
                self.params['resource_pool'], folder=self.datacenter.hostFolder)

        if not self.resource_pool:
            self.module.fail_json(
                msg=f"Resource pool '{self.params['resource_pool']}' could not be located")

        self.datastore = None
        datastore_cluster_obj = self.find_datastore_cluster_by_name(
            self.params['datastore'], datacenter=self.datacenter)
        if datastore_cluster_obj:
            datastore = None
            datastore_freespace = 0
            for dstore in datastore_cluster_obj.childEntity:
                if isinstance(dstore, vim.Datastore) and dstore.summary.freeSpace > datastore_freespace:
                    # If datastore field is provided, filter destination datastores
                    if dstore.summary.maintenanceMode != 'normal' or not dstore.summary.accessible:
                        continue
                    datastore = dstore
                    datastore_freespace = dstore.summary.freeSpace
            if datastore:
                self.datastore = datastore
        else:
            self.datastore = self.find_datastore_by_name(
                self.params['datastore'], datacenter_name=self.datacenter)

        if self.datastore is None:
            self.module.fail_json(msg=f"Datastore '{self.params['datastore']}' could not be located on specified ESXi host or"
                                  " datacenter")

        for key, value in self.params['networks'].items():
            network = find_network_by_name(
                self.content, value, datacenter_name=self.datacenter)
            if not network:
                self.module.fail_json(
                    msg='%(networks)s could not be located' % self.params)
            network_mapping = vim.OvfManager.NetworkMapping()
            network_mapping.name = key
            network_mapping.network = network
            self.network_mappings.append(network_mapping)

        return self.datastore, self.datacenter, self.resource_pool, self.network_mappings

    def get_ovf_descriptor(self):
        self.handle = WebHandle(self.params['ova'])
        self.tar = tarfile.open(fileobj=self.handle)
        ovffilename = list(
            filter(lambda x: x.endswith('.ovf'), self.tar.getnames()))[0]
        ovffile = self.tar.extractfile(ovffilename)
        self.ovf_descriptor = ovffile.read().decode()

        if self.ovf_descriptor:
            return self.ovf_descriptor
        else:
            self.module.fail_json(
                msg='Could not locate OVF file in %(ovf)s' % self.params)

    def get_lease(self):
        datastore, datacenter, resource_pool, network_mappings = self.get_objects()

        params = {
            'diskProvisioning': self.params['disk_provisioning'],
        }
        if self.params['name']:
            params['entityName'] = self.params['name']
        if network_mappings:
            params['networkMapping'] = network_mappings
        if self.params['deployment_option']:
            params['deploymentOption'] = self.params['deployment_option']
        if self.params['properties']:
            params['propertyMapping'] = []
            for key, value in self.params['properties'].items():
                property_mapping = vim.KeyValue()
                property_mapping.key = key
                property_mapping.value = str(
                    value) if isinstance(value, bool) else value
                params['propertyMapping'].append(property_mapping)

        if self.params['folder']:
            folder = self.content.searchIndex.FindByInventoryPath(
                self.params['folder'])
            if not folder:
                self.module.fail_json(
                    msg=f"Unable to find the specified folder {self.params['folder']}")
        else:
            folder = datacenter.vmFolder

        spec_params = vim.OvfManager.CreateImportSpecParams(**params)

        ovf_descriptor = self.get_ovf_descriptor()

        self.import_spec = self.content.ovfManager.CreateImportSpec(
            ovf_descriptor,
            resource_pool,
            datastore,
            spec_params
        )

        errors = [to_native(e.msg)
                  for e in getattr(self.import_spec, 'error', [])]
        if self.params['fail_on_spec_warnings']:
            errors.extend(
                (to_native(w.msg)
                 for w in getattr(self.import_spec, 'warning', []))
            )
        if errors:
            self.module.fail_json(
                msg=f"Failure validating OVF import spec: {'. '.join(errors)}"
            )

        for warning in getattr(self.import_spec, 'warning', []):
            self.module.warn(
                f"Problem validating OVF import spec: {to_native(warning.msg)}")

        name = self.params.get('name')
        if not self.params['allow_duplicates']:
            name = self.import_spec.importSpec.configSpec.name
            match = find_vm_by_name(self.content, name, folder=folder)
            if match:
                self.module.exit_json(instance=gather_vm_facts(
                    self.content, match), changed=False)

        if self.module.check_mode:
            self.module.exit_json(changed=True, instance={'hw_name': name})

        try:
            self.lease = resource_pool.ImportVApp(
                self.import_spec.importSpec,
                folder
            )
        except vmodl.fault.SystemError as err:
            self.module.fail_json(
                msg=f"Failed to start import: {to_native(err.msg)}")

        while self.lease.state != vim.HttpNfcLease.State.ready:
            time.sleep(0.1)

        self.entity = self.lease.info.entity

        return self.lease, self.import_spec

    def vm_existence_check(self):
        vm_obj = self.get_vm()
        if vm_obj:
            self.entity = vm_obj
            facts = self.deploy()
            self.module.exit_json(**facts)

    def upload(self):
        if self.params['ova'] is None:
            self.module.fail_json(
                msg="OVF path is required for upload operation.")

        lease, import_spec = self.get_lease()

        ssl_thumbprint = self.handle.thumbprint if self.handle.thumbprint else None
        source_files = []
        for file_item in import_spec.fileItem:
            source_file = vim.HttpNfcLease.SourceFile(
                url=self.handle.url,
                targetDeviceId=file_item.deviceId,
                create=file_item.create,
                size=file_item.size,
                sslThumbprint=ssl_thumbprint,
                memberName=file_item.path
            )
            source_files.append(source_file)

        wait_for_task(lease.HttpNfcLeasePullFromUrls_Task(source_files))

    def complete(self):
        self.lease.HttpNfcLeaseComplete()

    def inject_ovf_env(self):
        attrib = {
            'xmlns': 'http://schemas.dmtf.org/ovf/environment/1',
            'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xmlns:oe': 'http://schemas.dmtf.org/ovf/environment/1',
            'xmlns:ve': 'http://www.vmware.com/schema/ovfenv',
            'oe:id': '',
            've:esxId': self.entity._moId
        }
        env = ET.Element('Environment', **attrib)

        platform = ET.SubElement(env, 'PlatformSection')
        ET.SubElement(platform, 'Kind').text = self.content.about.name
        ET.SubElement(platform, 'Version').text = self.content.about.version
        ET.SubElement(platform, 'Vendor').text = self.content.about.vendor
        ET.SubElement(platform, 'Locale').text = 'US'

        prop_section = ET.SubElement(env, 'PropertySection')
        for key, value in self.params['properties'].items():
            params = {
                'oe:key': key,
                'oe:value': str(value) if isinstance(value, bool) else value
            }
            ET.SubElement(prop_section, 'Property', **params)

        opt = vim.option.OptionValue()
        opt.key = 'guestinfo.ovfEnv'
        opt.value = '<?xml version="1.0" encoding="UTF-8"?>' + \
            to_native(ET.tostring(env))

        config_spec = vim.vm.ConfigSpec()
        config_spec.extraConfig = [opt]

        task = self.entity.ReconfigVM_Task(config_spec)
        wait_for_task(task)

    def deploy(self):
        facts = {}

        if self.params['power_on']:
            facts = set_vm_power_state(
                self.content, self.entity, 'poweredon', force=False)
            if self.params['wait_for_ip_address']:
                _facts = wait_for_vm_ip(self.content, self.entity)
                if not _facts:
                    self.module.fail_json(
                        msg='Waiting for IP address timed out')

        if not facts:
            facts.update(
                dict(instance=gather_vm_facts(self.content, self.entity)))

        return facts


def main():
    argument_spec = vmware_argument_spec()
    argument_spec.update({
        'name': {},
        'datastore': {
            'default': 'datastore1',
        },
        'datacenter': {
            'default': 'ha-datacenter',
        },
        'cluster': {
            'default': None,
        },
        'esxi_hostname': {
            'default': None,
        },
        'deployment_option': {
            'default': None,
        },
        'folder': {
            'default': None,
        },
        'inject_ovf_env': {
            'default': False,
            'type': 'bool',
        },
        'resource_pool': {
            'default': 'Resources',
        },
        'networks': {
            'default': {
                'VM Network': 'VM Network',
            },
            'type': 'dict',
        },
        'ova': {
            'type': 'str',
        },
        'disk_provisioning': {
            'choices': [
                'flat',
                'eagerZeroedThick',
                'monolithicSparse',
                'twoGbMaxExtentSparse',
                'twoGbMaxExtentFlat',
                'thin',
                'sparse',
                'thick',
                'seSparse',
                'monolithicFlat'
            ],
            'default': 'thin',
        },
        'power_on': {
            'type': 'bool',
            'default': True,
        },
        'properties': {
            'type': 'dict',
        },
        'wait': {
            'type': 'bool',
            'default': True,
        },
        'wait_for_ip_address': {
            'type': 'bool',
            'default': False,
        },
        'allow_duplicates': {
            'type': 'bool',
            'default': True,
        },
        'fail_on_spec_warnings': {
            'type': 'bool',
            'default': False,
        },
    })
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[
            ['cluster', 'esxi_hostname'],
        ],
    )

    deploy_ova = OVAUploader(module)

    deploy_ova.vm_existence_check()
    deploy_ova.upload()
    deploy_ova.complete()

    if module.params['inject_ovf_env']:
        deploy_ova.inject_ovf_env()

    facts = deploy_ova.deploy()
    facts.update(changed=True)

    module.exit_json(**facts)


if __name__ == '__main__':
    main()
