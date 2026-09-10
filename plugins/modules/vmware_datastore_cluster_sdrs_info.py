#!/usr/bin/python

DOCUMENTATION = r"""
---
module: vmware_datastore_cluster_sdrs_info
short_description: Get SDRS information from VMware vSphere datastore clusters
description:
    - This module can be used to gather SDRS information from a datastore cluster in given VMware environment.
author:
-  Thomas Sjögren (@konstruktoid)
options:
    datacenter_name:
      description:
      - The name of the datacenter.
      required: true
      aliases: [ datacenter ]
      type: str
    datastore_cluster_name:
      description:
      - The name of the datastore cluster.
      required: true
      type: str
extends_documentation_fragment:
- vmware.vmware.base_options

"""

EXAMPLES = r"""
- name: Get SDRS information from a datastore cluster
  community.vmware.vmware_datastore_cluster_sdrs_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    datacenter_name: '{{ datacenter_name }}'
    datastore_cluster_name: '{{ datastore_cluster_name }}'
  delegate_to: localhost
"""

RETURN = r"""
sdrs:
    description: Datastore cluster SDRS information
    returned: always
    type: list
    sample: [
        "sdrs": {
            "_vimtype": "vim.storageDrs.PodConfigInfo",
            "automationOverrides": {
                "_vimtype": "vim.storageDrs.AutomationConfig",
                "ioLoadBalanceAutomationMode": null,
                "policyEnforcementAutomationMode": null,
                "ruleEnforcementAutomationMode": null,
                "spaceLoadBalanceAutomationMode": null,
                "vmEvacuationAutomationMode": null
            },
            "defaultIntraVmAffinity": true,
            "defaultVmBehavior": "manual",
            "enabled": false,
            "ioLoadBalanceConfig": {
                "_vimtype": "vim.storageDrs.IoLoadBalanceConfig",
                "ioLatencyThreshold": 15,
                "ioLoadImbalanceThreshold": null,
                "reservableIopsThreshold": null,
                "reservablePercentThreshold": 60,
                "reservableThresholdMode": "automated"
            },
            "ioLoadBalanceEnabled": true,
            "loadBalanceInterval": 480,
            "option": [],
            "rule": [],
            "spaceLoadBalanceConfig": {
                "_vimtype": "vim.storageDrs.SpaceLoadBalanceConfig",
                "freeSpaceThresholdGB": null,
                "minSpaceUtilizationDifference": null,
                "spaceThresholdMode": "utilization",
                "spaceUtilizationThreshold": 80
            }
        },
    ]
"""

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    PyVmomi,
)
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import (
    base_argument_spec,
)


class VMwareDatastoreClusterSdrsInfo(PyVmomi):
    """A class that provides functionality to fetch datastore cluster SDRS configuration details."""

    def __init__(self, module):
        """Initialize the VMwareDatastoreClusterSdrsInfo class."""
        super(VMwareDatastoreClusterSdrsInfo, self).__init__(module)
        datacenter_name = self.params.get("datacenter_name")
        datacenter_obj = self.find_datacenter_by_name(datacenter_name)
        if not datacenter_obj:
            self.module.fail_json(
                msg="Failed to find datacenter '%s'." % datacenter_name,
            )
        self.folder_obj = datacenter_obj.datastoreFolder

        self.datastore_cluster_name = self.params.get("datastore_cluster_name")
        self.datastore_cluster_obj = self.find_datastore_cluster_by_name(
            self.datastore_cluster_name,
        )

    def sdrs(self) -> None:
        """Retrieve Storage Distributed Resource Scheduler (SDRS) configuration."""
        datastore_cluster = self.to_json(
            self.datastore_cluster_obj.podStorageDrsEntry.storageDrsConfig.podConfig,
        )

        results = {}
        results["sdrs"] = {}
        for key, value in datastore_cluster.items():
            results["sdrs"][key] = value

        self.module.exit_json(**results)


def main() -> None:
    """Execute the VMware Datastore Cluster Info module."""
    argument_spec = base_argument_spec()
    argument_spec.update(
        dict(
            datacenter_name=dict(type="str", required=True, aliases=["datacenter"]),
            datastore_cluster_name=dict(type="str", required=True),
        ),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    datastore_cluster_sdrs_info = VMwareDatastoreClusterSdrsInfo(module)
    datastore_cluster_sdrs_info.sdrs()


if __name__ == "__main__":
    main()
