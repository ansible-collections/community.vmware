#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_host_capability_info
short_description: Gathers info about an ESXi host's capability information
description:
- This module can be used to gather information about an ESXi host's capability information when ESXi hostname or Cluster name is given.
author:
- Abhijeet Kasurde (@Akasurde)
options:
  cluster_name:
    description:
    - Name of the cluster from all host systems to be used for information gathering.
    - If O(esxi_hostname) is not given, this parameter is required.
    type: str
  esxi_hostname:
    description:
    - ESXi hostname to gather information from.
    - If O(cluster_name) is not given, this parameter is required.
    type: str
extends_documentation_fragment:
- community.vmware.vmware.documentation

'''

EXAMPLES = r'''
- name: Gather capability info about all ESXi Host in given Cluster
  community.vmware.vmware_host_capability_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    cluster_name: cluster_name
  delegate_to: localhost
  register: all_cluster_hosts_info

- name: Gather capability info about ESXi Host
  community.vmware.vmware_host_capability_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    esxi_hostname: '{{ esxi_hostname }}'
  delegate_to: localhost
  register: hosts_info
'''

RETURN = r'''
hosts_capability_info:
    description: metadata about host's capability info
    returned: always
    type: dict
    sample: {
            "esxi_hostname_0001": {
                "accel3dSupported": false,
                "backgroundSnapshotsSupported": false,
                "checkpointFtCompatibilityIssues": [],
                "checkpointFtSupported": false,
                "cloneFromSnapshotSupported": true,
                "cpuHwMmuSupported": true,
            }
    }
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from ansible_collections.community.vmware.plugins.module_utils._argument_spec import base_argument_spec


class CapabilityInfoManager(PyVmomi):
    def __init__(self, module):
        super(CapabilityInfoManager, self).__init__(module)
        cluster_name = self.params.get('cluster_name', None)
        esxi_host_name = self.params.get('esxi_hostname', None)
        self.hosts = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_host_name)

    def gather_host_capability_info(self):
        hosts_capability_info = dict()
        for host in self.hosts:
            hc = host.capability
            hosts_capability_info[host.name] = dict(
                recursiveResourcePoolsSupported=hc.recursiveResourcePoolsSupported,
                cpuMemoryResourceConfigurationSupported=hc.cpuMemoryResourceConfigurationSupported,
                rebootSupported=hc.rebootSupported,
                shutdownSupported=hc.shutdownSupported,
                vmotionSupported=hc.vmotionSupported,
                standbySupported=hc.standbySupported,
                ipmiSupported=hc.ipmiSupported,
                maxSupportedVMs=hc.maxSupportedVMs,
                maxRunningVMs=hc.maxRunningVMs,
                maxSupportedVcpus=hc.maxSupportedVcpus,
                maxRegisteredVMs=hc.maxRegisteredVMs,
                datastorePrincipalSupported=hc.datastorePrincipalSupported,
                sanSupported=hc.sanSupported,
                nfsSupported=hc.nfsSupported,
                iscsiSupported=hc.iscsiSupported,
                vlanTaggingSupported=hc.vlanTaggingSupported,
                nicTeamingSupported=hc.nicTeamingSupported,
                highGuestMemSupported=hc.highGuestMemSupported,
                maintenanceModeSupported=hc.maintenanceModeSupported,
                suspendedRelocateSupported=hc.suspendedRelocateSupported,
                restrictedSnapshotRelocateSupported=hc.restrictedSnapshotRelocateSupported,
                perVmSwapFiles=hc.perVmSwapFiles,
                localSwapDatastoreSupported=hc.localSwapDatastoreSupported,
                unsharedSwapVMotionSupported=hc.unsharedSwapVMotionSupported,
                backgroundSnapshotsSupported=hc.backgroundSnapshotsSupported,
                preAssignedPCIUnitNumbersSupported=hc.preAssignedPCIUnitNumbersSupported,
                screenshotSupported=hc.screenshotSupported,
                scaledScreenshotSupported=hc.scaledScreenshotSupported,
                storageVMotionSupported=hc.storageVMotionSupported,
                vmotionWithStorageVMotionSupported=hc.vmotionWithStorageVMotionSupported,
                vmotionAcrossNetworkSupported=hc.vmotionAcrossNetworkSupported,
                maxNumDisksSVMotion=hc.maxNumDisksSVMotion,
                hbrNicSelectionSupported=hc.hbrNicSelectionSupported,
                vrNfcNicSelectionSupported=hc.vrNfcNicSelectionSupported,
                recordReplaySupported=hc.recordReplaySupported,
                ftSupported=hc.ftSupported,
                replayUnsupportedReason=hc.replayUnsupportedReason,
                smpFtSupported=hc.smpFtSupported,
                maxVcpusPerFtVm=hc.maxVcpusPerFtVm,
                loginBySSLThumbprintSupported=hc.loginBySSLThumbprintSupported,
                cloneFromSnapshotSupported=hc.cloneFromSnapshotSupported,
                deltaDiskBackingsSupported=hc.deltaDiskBackingsSupported,
                perVMNetworkTrafficShapingSupported=hc.perVMNetworkTrafficShapingSupported,
                tpmSupported=hc.tpmSupported,
                virtualExecUsageSupported=hc.virtualExecUsageSupported,
                storageIORMSupported=hc.storageIORMSupported,
                vmDirectPathGen2Supported=hc.vmDirectPathGen2Supported,
                vmDirectPathGen2UnsupportedReasonExtended=hc.vmDirectPathGen2UnsupportedReasonExtended,
                vStorageCapable=hc.vStorageCapable,
                snapshotRelayoutSupported=hc.snapshotRelayoutSupported,
                firewallIpRulesSupported=hc.firewallIpRulesSupported,
                servicePackageInfoSupported=hc.servicePackageInfoSupported,
                maxHostRunningVms=hc.maxHostRunningVms,
                maxHostSupportedVcpus=hc.maxHostSupportedVcpus,
                vmfsDatastoreMountCapable=hc.vmfsDatastoreMountCapable,
                eightPlusHostVmfsSharedAccessSupported=hc.eightPlusHostVmfsSharedAccessSupported,
                nestedHVSupported=hc.nestedHVSupported,
                vPMCSupported=hc.vPMCSupported,
                interVMCommunicationThroughVMCISupported=hc.interVMCommunicationThroughVMCISupported,
                scheduledHardwareUpgradeSupported=hc.scheduledHardwareUpgradeSupported,
                featureCapabilitiesSupported=hc.featureCapabilitiesSupported,
                latencySensitivitySupported=hc.latencySensitivitySupported,
                storagePolicySupported=hc.storagePolicySupported,
                accel3dSupported=hc.accel3dSupported,
                reliableMemoryAware=hc.reliableMemoryAware,
                multipleNetworkStackInstanceSupported=hc.multipleNetworkStackInstanceSupported,
                messageBusProxySupported=hc.messageBusProxySupported,
                vsanSupported=hc.vsanSupported,
                vFlashSupported=hc.vFlashSupported,
                hostAccessManagerSupported=hc.hostAccessManagerSupported,
                provisioningNicSelectionSupported=hc.provisioningNicSelectionSupported,
                nfs41Supported=hc.nfs41Supported,
                nfs41Krb5iSupported=hc.nfs41Krb5iSupported,
                turnDiskLocatorLedSupported=hc.turnDiskLocatorLedSupported,
                virtualVolumeDatastoreSupported=hc.virtualVolumeDatastoreSupported,
                markAsSsdSupported=hc.markAsSsdSupported,
                markAsLocalSupported=hc.markAsLocalSupported,
                smartCardAuthenticationSupported=hc.smartCardAuthenticationSupported,
                cryptoSupported=hc.cryptoSupported,
                oneKVolumeAPIsSupported=hc.oneKVolumeAPIsSupported,
                gatewayOnNicSupported=hc.gatewayOnNicSupported,
                upitSupported=hc.upitSupported,
                cpuHwMmuSupported=hc.cpuHwMmuSupported,
                encryptedVMotionSupported=hc.encryptedVMotionSupported,
                encryptionChangeOnAddRemoveSupported=hc.encryptionChangeOnAddRemoveSupported,
                encryptionHotOperationSupported=hc.encryptionHotOperationSupported,
                encryptionWithSnapshotsSupported=hc.encryptionWithSnapshotsSupported,
                encryptionFaultToleranceSupported=hc.encryptionFaultToleranceSupported,
                encryptionMemorySaveSupported=hc.encryptionMemorySaveSupported,
                encryptionRDMSupported=hc.encryptionRDMSupported,
                encryptionVFlashSupported=hc.encryptionVFlashSupported,
                encryptionCBRCSupported=hc.encryptionCBRCSupported,
                encryptionHBRSupported=hc.encryptionHBRSupported,
                supportedVmfsMajorVersion=list(hc.supportedVmfsMajorVersion),
                vmDirectPathGen2UnsupportedReason=list(hc.vmDirectPathGen2UnsupportedReason),
                ftCompatibilityIssues=list(hc.ftCompatibilityIssues),
                smpFtCompatibilityIssues=list(hc.smpFtCompatibilityIssues),
                replayCompatibilityIssues=list(hc.replayCompatibilityIssues),
            )

            # The `checkpointFtSupported` and `checkpointFtCompatibilityIssues` properties have been removed from pyvmomi 7.0.
            # The parameters can be substituted as follows.
            #   checkpointFtSupported => smpFtSupported
            #   checkpointFtSupported => smpFtCompatibilityIssues.
            # So add `checkpointFtSupported` and `checkpointFtCompatibilityIssues` keys for compatibility with previous versions.
            # https://github.com/ansible-collections/vmware/pull/118
            hosts_capability_info[host.name]['checkpointFtSupported'] = hosts_capability_info[host.name]['smpFtSupported']
            hosts_capability_info[host.name]['checkpointFtCompatibilityIssues'] = hosts_capability_info[host.name]['smpFtCompatibilityIssues']

        return hosts_capability_info


def main():
    argument_spec = base_argument_spec()
    argument_spec.update(
        cluster_name=dict(type='str', required=False),
        esxi_hostname=dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=[
            ['cluster_name', 'esxi_hostname'],
        ],
        supports_check_mode=True,
    )

    host_capability_manager = CapabilityInfoManager(module)
    module.exit_json(changed=False,
                     hosts_capability_info=host_capability_manager.gather_host_capability_info())


if __name__ == "__main__":
    main()
