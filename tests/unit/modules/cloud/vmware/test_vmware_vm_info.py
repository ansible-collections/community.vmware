# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from types import SimpleNamespace
from unittest.mock import Mock, call, patch

import pytest
from pyVmomi import vim, vmodl

from ansible_collections.community.vmware.plugins.modules import vmware_vm_info


def make_vm(moid, template=False, fail_property=None, fault=None):
    stub = Mock()
    vm = vim.VirtualMachine(moid, stub)
    properties = {
        'summary': SimpleNamespace(
            guest=SimpleNamespace(ipAddress=None),
            config=SimpleNamespace(name=moid, guestFullName='Linux', uuid='uuid-' + moid, instanceUuid='instance-' + moid),
            runtime=SimpleNamespace(host=None, powerState='poweredOn'),
        ),
        'config': SimpleNamespace(template=template),
    }

    def accessor(obj, prop):
        if prop.name == fail_property:
            raise fault if fault is not None else vmodl.fault.ManagedObjectNotFound(obj=vm)
        return properties[prop.name]

    stub.InvokeAccessor.side_effect = accessor
    return vm


@pytest.fixture
def inventory():
    info = object.__new__(vmware_vm_info.VmwareVmInfo)
    info.module = Mock()
    info.params = info.module.params = {'vm_type': 'vm'}
    info.content = Mock()
    with patch.object(vmware_vm_info, 'get_all_objs') as get_all:
        yield info, get_all


def test_disappeared_vms_are_reported_and_collection_continues(inventory):
    info, get_all = inventory
    get_all.return_value = [
        make_vm('vm-1'),
        make_vm('vm-2', fail_property='summary'),
        make_vm('vm-3', fail_property='config'),
        make_vm('vm-4', template=True),
        make_vm('vm-5'),
    ]

    machines = info.get_virtual_machines()

    assert [(vm['moid'], vm['guest_name']) for vm in machines] == [('vm-1', 'vm-1'), ('vm-5', 'vm-5')]
    assert info.skipped_virtual_machines == ['vm-2', 'vm-3']
    assert info.module.warn.call_args_list == [
        call('Skipping virtual machine vm-2 because it disappeared while gathering information.'),
        call('Skipping virtual machine vm-3 because it disappeared while gathering information.'),
    ]

    info.params['vm_type'] = 'template'
    get_all.return_value = [make_vm('vm-1'), make_vm('vm-4', template=True)]
    assert [vm['moid'] for vm in info.get_virtual_machines()] == ['vm-4']
    assert info.skipped_virtual_machines == []


def test_other_errors_are_not_ignored(inventory):
    info, get_all = inventory
    faults = [
        vmodl.fault.ManagedObjectNotFound(obj=vim.HostSystem('host-1')),
        vmodl.fault.ManagedObjectNotFound(obj=vim.VirtualMachine('vm-other')),
        vim.fault.NoPermission(),
    ]
    for fault in faults:
        get_all.return_value = [make_vm('vm-1', fail_property='summary', fault=fault)]
        with pytest.raises(type(fault)) as error:
            info.get_virtual_machines()
        assert error.value is fault
        assert info.skipped_virtual_machines == []
    info.module.warn.assert_not_called()


def test_main_returns_skipped_vms():
    with patch.object(vmware_vm_info, 'AnsibleModule') as module_class, \
            patch.object(vmware_vm_info, 'VmwareVmInfo') as info_class:
        info_class.return_value.get_virtual_machines.return_value = []
        info_class.return_value.skipped_virtual_machines = ['vm-1']

        vmware_vm_info.main()

    module_class.return_value.exit_json.assert_called_once_with(
        changed=False, virtual_machines=[], skipped_virtual_machines=['vm-1'],
    )
