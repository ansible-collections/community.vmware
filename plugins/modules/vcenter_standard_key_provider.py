#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2021, Ansible Project
# Copyright: (c) 2021, VMware, Inc. All Rights Reserved
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vcenter_standard_key_provider
short_description: Add, reconfigure or remove Standard Key Provider on vCenter server
description: >
  This module is used for adding, reconfiguring or removing Standard Key Provider on vCenter server.
  Refer to VMware docs for more information: L(Standard Key Provider,
  https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-6DB1E745-9624-43EA-847C-DD2F767CB94B.html)
author:
  - Diane Wang (@Tomorrow9) <dianew@vmware.com>
options:
  name:
    description: Name of the Key Provider to be added, reconfigured or removed from vCenter.
    type: str
    required: true
  mark_default:
    description:
      - Set specified Key Provider with name O(name) as the default Key Provider.
      - If new added Key Provider is the only key provider in vCenter, then will mark it as default after adding.
    type: bool
    default: false
  state:
    description:
      - If set to V(absent), the named Key Provider will be removed from vCenter.
      - If set to V(present), the named existing Key Provider will be reconfigured or new Key Provider will be added.
    type: str
    choices:
      - present
      - absent
    default: present
  kms_info:
    description:
      - The information of an external key server (KMS).
      - O(kms_info[].kms_name), O(kms_info[].kms_ip) are required when adding a Standard Key Provider.
      - If O(kms_info[].kms_port) is not specified, the default port 5696 will be used.
      - O(kms_info[].kms_ip), O(kms_info[].kms_port) can be reconfigured for an existing KMS with name O(kms_info[].kms_name).
    type: list
    default: []
    elements: dict
    suboptions:
      kms_name:
        description: Name of the KMS to be configured.
        type: str
      kms_ip:
        description: IP address of the external KMS.
        type: str
      kms_port:
        description: Port of the external KMS.
        type: int
      remove_kms:
        description: Remove the configured KMS with name O(kms_info[].kms_name) from the KMIP cluster.
        type: bool
  proxy_server:
    description: Address of the proxy server to connect to KMS.
    type: str
  proxy_port:
    description: Port of the proxy server.
    type: int
  kms_username:
    description: Username to authenticate to the KMS.
    type: str
  kms_password:
    description: Password to authenticate to the KMS.
    type: str
  make_kms_trust_vc:
    description:
      - After adding the Standard Key Provider to the vCenter Server, you can establish a trusted connection, the
        exact process depends on the certificates that the key provider accepts, and on your company policy.
      - Three methods implemented here,
        (1) upload client certificate and private key through O(make_kms_trust_vc.upload_client_cert) and O(make_kms_trust_vc.upload_client_key) parameters,
        (2) generate, update, download vCenter self signed certificate through O(make_kms_trust_vc.download_self_signed_cert) parameter,
        (3) download generated Certificate Signing Request(CSR) through O(make_kms_trust_vc.download_client_csr) parameter, send it to
        KMS then upload the KMS signed CSR through O(make_kms_trust_vc.upload_kms_signed_client_csr) parameter.
      - This is not set to be mandatory, if not set, please go to vCenter to setup trust connection with KMS manually.
    type: dict
    suboptions:
      upload_client_cert:
        description:
          - The absolute file path of client certificate.
          - Request a certificate and private key from the KMS vendor. The files are X509 files in PEM format.
          - The certificate might be already trusted by the KMS server.
        type: path
      upload_client_key:
        description: The absolute file path of client private key to be uploaded together with O(make_kms_trust_vc.upload_client_cert).
        type: path
      download_self_signed_cert:
        description: The absolute path on local machine for keeping vCenter generated self signed client cert.
        type: path
      download_client_csr:
        description:
          - The absolute path on local machine for keeping vCenter generated CSR.
          - Then upload the KMS signed CSR using O(make_kms_trust_vc.upload_kms_signed_client_csr) to vCenter.
        type: path
      upload_kms_signed_client_csr:
        description: The absolute file path of KMS signed CSR downloaded from O(make_kms_trust_vc.download_client_csr).
        type: path
extends_documentation_fragment:
- vmware.vmware.base_options
'''

EXAMPLES = r'''
- name: Add a new Standard Key Provider with client certificate and private key
  community.vmware.vcenter_standard_key_provider:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: 'test_standard_kp'
    state: 'present'
    mark_default: true
    kms_info:
      - kms_name: test_kms_1
        kms_ip: 192.168.1.10
    make_kms_trust_vc:
      upload_client_cert: "/tmp/test_cert.pem"
      upload_client_key: "/tmp/test_cert_key.pem"
  register: add_skp_result

- name: Remove the KMS from the key provider cluster
  community.vmware.vcenter_standard_key_provider:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: 'test_standard_kp'
    state: 'present'
    kms_info:
      - kms_name: test_kms_1
        remove_kms: true
  register: remove_kms_result

- name: Remove the Standard Key Provider
  community.vmware.vcenter_standard_key_provider:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    name: 'test_standard_kp'
    state: 'absent'
  register: remove_kp_result
'''

RETURN = r'''
key_provider_clusters:
    description: the Key Provider cluster info
    returned: always
    type: list
    sample:
        [
            {
                "has_backup": null,
                "key_id": null,
                "key_provide_id": "test_standard",
                "management_type": null,
                "servers": [
                    {
                        "address": "192.168.1.10",
                        "name": "test_kms",
                        "port": 5696,
                        "protocol": "",
                        "proxy": "",
                        "proxy_port": null,
                        "user_name": ""
                    }
                ],
                "tpm_required": null,
                "use_as_default": true
            }
        ]
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

import os
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec


class PyVmomiHelper(PyVmomi):
    def __init__(self, module):
        super(PyVmomiHelper, self).__init__(module)
        self.crypto_mgr = self.content.cryptoManager
        self.key_provider_id = None

    def get_key_provider_clusters(self):
        key_provider_clusters = None
        try:
            if self.vcenter_version_at_least(version=(7, 0, 0)):
                key_provider_clusters = self.crypto_mgr.ListKmsClusters(includeKmsServers=True)
            else:
                key_provider_clusters = self.crypto_mgr.ListKmipServers()
        except Exception as e:
            self.module.fail_json(msg="Failed to get key provider clusters info with exception: %s" % to_native(e))

        return key_provider_clusters

    @staticmethod
    def get_key_provider_by_name(key_provider_clusters, name):
        key_provider_cluster = None
        if not name or not key_provider_clusters:
            return key_provider_cluster
        for kp_cluster in key_provider_clusters:
            if kp_cluster.clusterId.id == name:
                key_provider_cluster = kp_cluster

        return key_provider_cluster

    @staticmethod
    def gather_key_provider_cluster_info(key_provider_clusters):
        key_provider_cluster_facts = []
        if not key_provider_clusters:
            return key_provider_cluster_facts
        for kp_item in key_provider_clusters:
            kp_info = dict(
                key_provide_id=kp_item.clusterId.id,
                use_as_default=kp_item.useAsDefault,
                management_type=kp_item.managementType,
                has_backup=kp_item.hasBackup,
                tpm_required=kp_item.tpmRequired,
                key_id=kp_item.keyId
            )
            kmip_servers = []
            if hasattr(kp_item, 'servers') and len(kp_item.servers) != 0:
                for kmip_item in kp_item.servers:
                    kmip_info = dict(
                        name=kmip_item.name,
                        address=kmip_item.address,
                        port=kmip_item.port,
                        protocol=kmip_item.protocol,
                        proxy=kmip_item.proxyAddress,
                        proxy_port=kmip_item.proxyPort,
                        user_name=kmip_item.userName
                    )
                    kmip_servers.append(kmip_info)
            kp_info.update(servers=kmip_servers)
            key_provider_cluster_facts.append(kp_info)

        return key_provider_cluster_facts

    def set_default_key_provider(self):
        # Since vSphere API 6.5
        try:
            self.crypto_mgr.MarkDefault(self.key_provider_id)
        except Exception as e:
            self.module.fail_json(msg="Failed to mark default key provider to '%s' with exception: %s"
                                      % (self.key_provider_id.id, to_native(e)))

    @staticmethod
    def create_key_provider_id(key_provider_name):
        key_provider_id = None
        if key_provider_name:
            key_provider_id = vim.encryption.KeyProviderId()
            key_provider_id.id = key_provider_name

        return key_provider_id

    @staticmethod
    def create_kmip_server_info(kms_info, proxy_user_info):
        kmip_server_info = None
        if kms_info:
            kmip_server_info = vim.encryption.KmipServerInfo()
            kmip_server_info.name = kms_info.get('kms_name')
            kmip_server_info.address = kms_info.get('kms_ip')
            if kms_info.get('kms_port') is None:
                kmip_server_info.port = 5696
            else:
                kmip_server_info.port = kms_info.get('kms_port')
            if proxy_user_info:
                if proxy_user_info.get('proxy_server'):
                    kmip_server_info.proxyAddress = proxy_user_info['proxy_server']
                if proxy_user_info.get('proxy_port'):
                    kmip_server_info.proxyPort = proxy_user_info['proxy_port']
                if proxy_user_info.get('kms_username'):
                    kmip_server_info.userName = proxy_user_info['kms_username']

        return kmip_server_info

    @staticmethod
    def create_kmip_server_spec(key_provider_id, kms_server_info, kms_password=None):
        kmip_server_spec = None
        if key_provider_id and kms_server_info:
            kmip_server_spec = vim.encryption.KmipServerSpec()
            kmip_server_spec.clusterId = key_provider_id
            kmip_server_spec.info = kms_server_info
            if kms_password:
                kmip_server_spec.password = kms_password

        return kmip_server_spec

    def setup_standard_kp(self, kp_name, kms_info_list, proxy_user_config_dict):
        kp_id = self.create_key_provider_id(kp_name)
        for kms_info in kms_info_list:
            server_cert = None
            kms_server = self.create_kmip_server_info(kms_info, proxy_user_config_dict)
            kms_spec = self.create_kmip_server_spec(kp_id, kms_server, proxy_user_config_dict.get('kms_password'))
            try:
                self.crypto_mgr.RegisterKmipServer(server=kms_spec)
            except Exception as e:
                self.module.fail_json(msg="Failed to add Standard Key Provider '%s' with exception: %s"
                                          % (kp_name, to_native(e)))
            try:
                server_cert = self.crypto_mgr.RetrieveKmipServerCert(keyProvider=kp_id, server=kms_server).certificate
            except Exception as e:
                self.module.fail_json(msg="Failed to retrieve KMS server certificate with exception: %s" % to_native(e))
            if not server_cert:
                self.module.fail_json(msg="Got empty KMS server certificate: '%s'" % server_cert)
            try:
                self.crypto_mgr.UploadKmipServerCert(cluster=kp_id, certificate=server_cert)
            except Exception as e:
                self.module.fail_json(msg="Failed to upload KMS server certificate for key provider '%s' with"
                                          " exception: %s" % (kp_name, to_native(e)))

        return kp_id

    def add_kmip_to_standard_kp(self, kms_info, proxy_user_config_dict):
        kmip_server_info = self.create_kmip_server_info(kms_info, proxy_user_config_dict)
        kmip_server_spec = self.create_kmip_server_spec(self.key_provider_id, kmip_server_info,
                                                        proxy_user_config_dict.get('kms_password'))
        try:
            self.crypto_mgr.RegisterKmipServer(server=kmip_server_spec)
        except Exception as e:
            self.module.fail_json(msg="Failed to add the KMIP server to Key Provider cluster with exception: %s"
                                      % to_native(e))

    def change_kmip_in_standard_kp(self, existing_kmip_info, kms_info, proxy_user_config_dict):
        changed = False
        if kms_info:
            if kms_info.get('kms_ip') and existing_kmip_info.address != kms_info['kms_ip']:
                existing_kmip_info.address = kms_info['kms_ip']
                changed = True
            if kms_info.get('kms_port') and existing_kmip_info.port != kms_info['kms_port']:
                existing_kmip_info.port = kms_info['kms_port']
                changed = True
        if proxy_user_config_dict:
            if proxy_user_config_dict.get('proxy_server') and \
                    existing_kmip_info.proxyAddress != proxy_user_config_dict['proxy_server']:
                existing_kmip_info.proxyAddress = proxy_user_config_dict['proxy_server']
                changed = True
            if proxy_user_config_dict.get('proxy_port') and \
                    existing_kmip_info.proxyPort != proxy_user_config_dict['proxy_port']:
                existing_kmip_info.proxyPort = proxy_user_config_dict['proxy_port']
                changed = True
            if proxy_user_config_dict.get('kms_username') and \
                    existing_kmip_info.userName != proxy_user_config_dict['kms_username']:
                existing_kmip_info.userName = proxy_user_config_dict['kms_username']
                changed = True
        if changed:
            kmip_server_spec = self.create_kmip_server_spec(self.key_provider_id, existing_kmip_info,
                                                            proxy_user_config_dict.get('kms_password'))
            try:
                # Since vSphere API 6.5
                self.crypto_mgr.UpdateKmipServer(server=kmip_server_spec)
            except Exception as e:
                self.module.fail_json(msg="Failed to update KMIP server info with exception: %s" % to_native(e))

        return changed

    def reconfig_kmip_standard_kp(self, kmip_cluster_servers, kms_info_list, proxy_user_config_dict):
        changed = False
        # kms server reconfigure
        if len(kms_info_list) != 0:
            for kms_info in kms_info_list:
                existing_kmip = None
                for kmip_server in kmip_cluster_servers:
                    if kmip_server.name == kms_info.get('kms_name'):
                        existing_kmip = kmip_server
                # reconfigure existing kms server
                if existing_kmip is not None:
                    if kms_info.get('remove_kms'):
                        self.remove_kms_server(self.key_provider_id, kms_info.get('kms_name'))
                        kms_changed = True
                    else:
                        kms_changed = self.change_kmip_in_standard_kp(existing_kmip, kms_info, proxy_user_config_dict)
                # no kms server with specified name
                else:
                    if kms_info.get('remove_kms'):
                        self.module.fail_json(msg="Not find named KMS server to remove in the key provider cluster '%s'"
                                                  % self.key_provider_id.id)
                    self.add_kmip_to_standard_kp(kms_info, proxy_user_config_dict)
                    kms_changed = True
                if kms_changed:
                    changed = True
        # no kms specified in kms_info, then only update proxy or user info
        for kmip_server in kmip_cluster_servers:
            kms_changed = self.change_kmip_in_standard_kp(kmip_server, kms_info=None,
                                                          proxy_user_config_dict=proxy_user_config_dict)
            if kms_changed:
                changed = True

        return changed

    def update_self_signed_client_cert(self, dest_path):
        if not os.path.exists(dest_path):
            try:
                os.makedirs(dest_path)
            except OSError as e:
                self.module.fail_json(msg="Specified destination path '%s' not exist, but failed to create it with"
                                          " exception: %s" % (dest_path, to_native(e)))
        client_cert_file_path = os.path.join(dest_path, self.key_provider_id.id + '_self_signed_cert.pem')
        client_cert = self.crypto_mgr.RetrieveSelfSignedClientCert(self.key_provider_id)
        if not client_cert:
            try:
                client_cert = self.crypto_mgr.GenerateSelfSignedClientCert(self.key_provider_id)
            except Exception as e:
                self.module.fail_json(msg="Generate self signed client certificate failed with exception: %s"
                                          % to_native(e))
        if not client_cert:
            self.module.fail_json(msg="Generated self signed client certificate is empty '%s'" % client_cert)
        try:
            self.crypto_mgr.UpdateSelfSignedClientCert(self.key_provider_id, client_cert)
        except Exception as e:
            self.module.fail_json(msg="Update self signed client cert failed with exception: %s" % to_native(e))
        client_cert_file = open(client_cert_file_path, 'w')
        client_cert_file.write(client_cert)
        client_cert_file.close()

        return client_cert_file_path

    def download_client_csr_file(self, dest_path):
        if not os.path.exists(dest_path):
            try:
                os.makedirs(dest_path)
            except OSError as e:
                self.module.fail_json(msg="Specified destination path '%s' not exist, but failed to create it with"
                                          " exception: %s" % (dest_path, to_native(e)))
        client_csr_file_path = os.path.join(dest_path, self.key_provider_id.id + '_client_csr.pem')
        client_csr = self.crypto_mgr.RetrieveClientCsr(self.key_provider_id)
        if not client_csr:
            try:
                client_csr = self.crypto_mgr.GenerateClientCsr(self.key_provider_id)
            except Exception as e:
                self.module.fail_json(msg="Generate client CSR failed with exception: %s" % to_native(e))
        if not client_csr:
            self.module.fail_json(msg="Generated client CSR is empty '%s'" % client_csr)
        else:
            client_csr_file = open(client_csr_file_path, 'w')
            client_csr_file.write(client_csr)
            client_csr_file.close()

        return client_csr_file_path

    def upload_kms_signed_csr(self, kms_signed_csr):
        kms_signed_csr_file = open(kms_signed_csr)
        kms_signed_csr_content = kms_signed_csr_file.read()
        kms_signed_csr_file.close()
        try:
            self.crypto_mgr.UpdateKmsSignedCsrClientCert(self.key_provider_id, kms_signed_csr_content)
        except Exception as e:
            self.module.fail_json(msg="Update KMS signed client CSR cert failed with exception: '%s'" % to_native(e))

    def upload_client_cert_key(self, client_cert, client_key):
        client_cert_file = open(client_cert)
        private_key_file = open(client_key)
        client_cert_content = client_cert_file.read()
        private_key_content = private_key_file.read()
        client_cert_file.close()
        private_key_file.close()
        try:
            self.crypto_mgr.UploadClientCert(cluster=self.key_provider_id, certificate=client_cert_content,
                                             privateKey=private_key_content)
        except Exception as e:
            self.module.fail_json(msg="Failed to upload client certificate and private key for key provider '%s'"
                                      " with exception: %s" % (self.key_provider_id.id, to_native(e)))

    def download_upload_cert_for_trust(self, kms_trust_vc_config):
        changed = False
        cert_info = ''
        client_cert = kms_trust_vc_config.get('upload_client_cert')
        client_key = kms_trust_vc_config.get('upload_client_key')
        kms_signed_csr = kms_trust_vc_config.get('upload_kms_signed_client_csr')
        self_signed_cert_path = kms_trust_vc_config.get('download_self_signed_cert')
        client_csr_path = kms_trust_vc_config.get('download_client_csr')

        if client_cert and client_key:
            if not os.path.exists(client_cert) or not os.path.exists(client_key):
                self.module.fail_json(msg="Configured 'upload_client_cert' file: '%s', or 'upload_client_key' file:"
                                          " '%s' does not exist." % (client_cert, client_key))
            self.upload_client_cert_key(client_cert, client_key)
            cert_info = "Client cert file '%s', key file '%s' uploaded for key provider '%s'" \
                        % (client_cert, client_key, self.key_provider_id.id)
            changed = True
        elif kms_signed_csr:
            if not os.path.exists(kms_signed_csr):
                self.module.fail_json(msg="Configured 'upload_kms_signed_client_csr' file: '%s' does not exist."
                                          % kms_signed_csr)
            self.upload_kms_signed_csr(kms_signed_csr)
            cert_info = "KMS signed client CSR '%s' uploaded for key provider '%s'" % (kms_signed_csr,
                                                                                       self.key_provider_id.id)
            changed = True
        elif self_signed_cert_path:
            cert_file_path = self.update_self_signed_client_cert(self_signed_cert_path)
            cert_info = "Client self signed certificate file '%s' for key provider '%s' updated and downloaded" \
                        % (cert_file_path, self.key_provider_id.id)
            changed = True
        elif client_csr_path:
            cert_file_path = self.download_client_csr_file(client_csr_path)
            cert_info = "Client certificate signing request file '%s' for key provider '%s' downloaded" \
                        % (cert_file_path, self.key_provider_id.id)

        return changed, cert_info

    def remove_kms_server(self, key_provider_id, kms_server):
        # Since vSphere API 6.5
        try:
            self.crypto_mgr.RemoveKmipServer(clusterId=key_provider_id, serverName=kms_server)
        except Exception as e:
            self.module.fail_json(msg="Failed to remove KMIP server '%s' from key provider '%s' with exception: %s"
                                      % (kms_server, key_provider_id.id, to_native(e)))

    def remove_kms_cluster(self, kp_cluster):
        for kms in kp_cluster.servers:
            self.remove_kms_server(kp_cluster.clusterId, kms.name)

    def get_key_provider_type(self, kmip_cluster_info):
        key_provider_type = ''
        if kmip_cluster_info is None:
            return key_provider_type
        # Native Key Provider is supported from vSphere 7.0.2
        if not self.vcenter_version_at_least(version=(7, 0, 2)):
            key_provider_type = 'standard'
        else:
            if kmip_cluster_info.managementType == 'vCenter':
                key_provider_type = 'standard'
            elif kmip_cluster_info.managementType == 'nativeProvider':
                key_provider_type = 'native'
            else:
                key_provider_type = kmip_cluster_info.managementType

        return key_provider_type

    def key_provider_operation(self):
        results = {'failed': False, 'changed': False}
        kp_name = self.params['name']
        if not kp_name:
            self.module.fail_json(msg="Please set a valid name of key provider via 'name' parameter, now it's '%s',"
                                      % kp_name)
        key_provider_clusters = self.get_key_provider_clusters()
        # Find if there is existing Key Provider with the specified name
        existing_kp_cluster = self.get_key_provider_by_name(key_provider_clusters, kp_name)
        existing_kp_type = self.get_key_provider_type(existing_kp_cluster)
        if existing_kp_cluster is not None:
            if existing_kp_type and existing_kp_type == 'native':
                self.module.fail_json(msg="Native Key Provider with name '%s' already exist, please change to another"
                                          " name for Standard Key Provider operation using this module." % kp_name)
            self.key_provider_id = existing_kp_cluster.clusterId

        # Add a new Key Provider or reconfigure the existing Key Provider
        if self.params['state'] == 'present':
            is_default_kp = False
            proxy_user_config = dict()
            proxy_user_config.update(
                proxy_server=self.params.get('proxy_server'),
                proxy_port=self.params.get('proxy_port'),
                kms_username=self.params.get('kms_username'),
                kms_password=self.params.get('kms_password')
            )
            if existing_kp_cluster is not None:
                is_default_kp = existing_kp_cluster.useAsDefault
                # For existing Standard Key Provider, KMS servers can be reconfigured
                if self.module.check_mode:
                    results['desired_operation'] = "reconfig standard key provider"
                    results['target_key_provider'] = kp_name
                    self.module.exit_json(**results)
                else:
                    results['operation'] = "reconfig standard key provider"
                    results['changed'] = self.reconfig_kmip_standard_kp(existing_kp_cluster.servers,
                                                                        self.params['kms_info'], proxy_user_config)
            # Named Key Provider not exist
            else:
                # Add a Standard Key Provider, KMS name, IP are required
                if len(self.params['kms_info']) == 0:
                    self.module.fail_json(msg="Please set 'kms_info' when add new standard key provider")
                for configured_kms_info in self.params['kms_info']:
                    if configured_kms_info.get('remove_kms'):
                        self.module.fail_json(msg="Specified key provider '%s' not exist, so no KMS server to be"
                                              " removed." % kp_name)
                if self.module.check_mode:
                    results['desired_operation'] = "add standard key provider"
                    self.module.exit_json(**results)
                else:
                    results['operation'] = "add standard key provider"
                    new_key_provider_id = self.setup_standard_kp(kp_name, self.params['kms_info'], proxy_user_config)
                    if new_key_provider_id:
                        self.key_provider_id = new_key_provider_id
                        # If this new added key provider is the only key provider, then mark it default
                        if len(key_provider_clusters) == 0:
                            self.params['mark_default'] = True
                        results['changed'] = True

            if self.key_provider_id and self.params['mark_default'] and not is_default_kp:
                self.set_default_key_provider()
                results['changed'] = True
            if self.key_provider_id and self.params.get('make_kms_trust_vc'):
                results['changed'], cert_info = self.download_upload_cert_for_trust(self.params['make_kms_trust_vc'])
                results['msg'] = cert_info
        # Remove Key Provider
        else:
            if self.module.check_mode:
                results['desired_operation'] = "remove standard key provider"
            else:
                results['operation'] = "remove standard key provider"
            # Named Key Provider not found
            if existing_kp_cluster is None:
                output_msg = "Key Provider with name '%s' is not found." % kp_name
                if self.module.check_mode:
                    results['msg'] = output_msg
                    self.module.exit_json(**results)
                else:
                    self.module.fail_json(msg=output_msg)
            else:
                if self.module.check_mode:
                    results['target_key_provider'] = kp_name
                    self.module.exit_json(**results)
                else:
                    self.remove_kms_cluster(existing_kp_cluster)
                    results['changed'] = True

        if results['changed']:
            key_provider_clusters = self.get_key_provider_clusters()
        results['key_provider_clusters'] = self.gather_key_provider_cluster_info(key_provider_clusters)
        self.module.exit_json(**results)


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        name=dict(type='str', required=True),
        kms_info=dict(
            type='list',
            default=[],
            elements='dict',
            options=dict(
                kms_name=dict(type='str'),
                kms_ip=dict(type='str'),
                kms_port=dict(type='int'),
                remove_kms=dict(type='bool')
            )
        ),
        proxy_server=dict(type='str'),
        proxy_port=dict(type='int'),
        kms_username=dict(type='str'),
        kms_password=dict(type='str', no_log=True),
        make_kms_trust_vc=dict(
            type='dict',
            options=dict(
                upload_client_cert=dict(type='path'),
                upload_client_key=dict(type='path'),
                download_self_signed_cert=dict(type='path'),
                download_client_csr=dict(type='path'),
                upload_kms_signed_client_csr=dict(type='path')
            )
        ),
        mark_default=dict(type='bool', default=False),
        state=dict(type='str', default='present', choices=['present', 'absent'])
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    config_key_provider = PyVmomiHelper(module)
    if not config_key_provider.is_vcenter():
        module.fail_json(msg="hostname '%s' is not set to the vCenter server, please connect to vCenter for key"
                             " provider operations." % module.params.get('hostname'))
    if not config_key_provider.vcenter_version_at_least(version=(6, 5, 0)):
        module.fail_json(msg="vCenter server '%s' version is not >= 6.5.0, key provider is supported from vSphere 6.5."
                             % module.params.get('hostname'))
    try:
        config_key_provider.key_provider_operation()
    except Exception as e:
        module.fail_json(msg="Failed to configure key provider on vCenter with exception : %s" % to_native(e))


if __name__ == "__main__":
    main()
