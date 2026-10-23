# Copyright: (c) 2026, Everpure Inc.
# Copyright: (c) 2026, Eugenio Grosso <eugenio.grosso@everpuredata.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from pyVmomi import vim

from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    TaskError
)
from ansible_collections.community.vmware.plugins.module_utils.vmware_vmdk import (
    VmdkFiles,
    VmdkPath,
    is_file_not_found,
    parse_vmdk_path,
    provisioning_of,
    split_ds_path,
    type_short_name,
)


class FailJson(Exception):
    pass


def fail_json(**kwargs):
    raise FailJson(kwargs['msg'])


def vsphere_object(mocker, name='test', moid='1'):
    obj = mocker.Mock()
    obj.name = name
    obj._GetMoId.return_value = moid
    return obj


def task_error(message, fault):
    """
    A TaskError as raised by wait_for_task, with the vSphere fault as its cause.
    """
    error = TaskError(message)
    error.__cause__ = fault
    return error


@pytest.fixture
def files(mocker):
    client = mocker.Mock()
    client.module.fail_json.side_effect = fail_json
    client.module.params = {'datacenter': None}
    return VmdkFiles(client)


@pytest.fixture
def path(mocker):
    return VmdkPath(vsphere_object(mocker, name='ds1', moid='datastore-1'), vim.Datacenter('datacenter-1'), '[ds1] vm1/vm1.vmdk')


def flat_disk(file_name, eagerly_scrub=False):
    backing = vim.vm.device.VirtualDisk.FlatVer2BackingInfo(fileName=file_name, diskMode='persistent', eagerlyScrub=eagerly_scrub)
    return vim.vm.device.VirtualDisk(backing=backing, deviceInfo=vim.Description(label='Hard disk 1', summary=''))


def disk_info(mocker, disk_type=vim.vm.device.VirtualDisk.FlatVer2BackingInfo, thin=True, extents=None):
    return mocker.Mock(
        path='vm1.vmdk', diskType=disk_type, capacityKb=1024, thin=thin, fileSize=2048, hardwareVersion=14,
        controllerType=vim.vm.device.VirtualLsiLogicController, diskExtents=extents or ['[ds1] vm1/vm1-flat.vmdk'],
        modification=None)


@pytest.mark.parametrize('value, expected', [
    ('[ds1] vm1/vm1.vmdk', ('ds1', 'vm1/vm1.vmdk')),
    ('[ds 1]  a/b/disk.VMDK', ('ds 1', 'a/b/disk.VMDK')),
    ('[ds1] disk.vmdk', ('ds1', 'disk.vmdk')),
    ('/vmfs/volumes/ds1/vm1/vm1.vmdk', ('ds1', 'vm1/vm1.vmdk')),
    ('/vmfs/volumes/61faa211-2857d4e6-1f86-34800d10ce12//vm1.vmdk', ('61faa211-2857d4e6-1f86-34800d10ce12', 'vm1.vmdk')),
])
def test_parse_vmdk_path(value, expected):
    assert parse_vmdk_path(value) == expected


@pytest.mark.parametrize('value', ['vm1/vm1.vmdk', '[ds1] vm1/vm1.txt', '[ds1] ', '/vmfs/volumes/ds1', '', None])
def test_parse_vmdk_path_rejects(value):
    with pytest.raises(ValueError):
        parse_vmdk_path(value)


@pytest.mark.parametrize('value, expected', [
    ('[ds1] vm1/vm1.vmdk', ('[ds1] vm1', 'vm1.vmdk')),
    ('[ds1] a/b/disk.vmdk', ('[ds1] a/b', 'disk.vmdk')),
    ('[ds1] disk.vmdk', ('[ds1]', 'disk.vmdk')),
])
def test_split_ds_path(value, expected):
    assert split_ds_path(value) == expected


def test_type_short_name():
    assert type_short_name(vim.vm.device.VirtualDisk.FlatVer2BackingInfo) == 'FlatVer2BackingInfo'
    assert type_short_name(None) is None


@pytest.mark.parametrize('args, expected', [
    (('RawDiskMappingVer1BackingInfo', False, ['[ds1] vm1/d-rdmp.vmdk']), 'rdmp'),
    (('RawDiskMappingVer1BackingInfo', False, ['[ds1] vm1/d-rdm.vmdk']), 'rdm'),
    (('RawDiskMappingVer1BackingInfo', False, ['[ds1] vm1/d-rdm.vmdk'], 'physicalMode'), 'rdmp'),
    (('RawDiskMappingVer1BackingInfo', False, ['[ds1] vm1/d-rdmp.vmdk'], 'virtualMode'), 'rdm'),
    (('FlatVer2BackingInfo', True, []), 'thin'),
    (('SparseVer2BackingInfo', False, []), 'sparse'),
    (('FlatVer2BackingInfo', False, [], None, True), 'eagerzeroedthick'),
    (('FlatVer2BackingInfo', False, [], None, False), 'zeroedthick'),
    (('FlatVer2BackingInfo', False, []), 'thick'),
    ((None, None, []), None),
])
def test_provisioning_of(args, expected):
    assert provisioning_of(*args) == expected


def test_is_file_not_found():
    assert is_file_not_found(task_error('not found', vim.fault.FileNotFound()))
    assert not is_file_not_found(task_error('denied', vim.fault.NoPermission()))
    assert not is_file_not_found(TaskError('timeout'))


def test_wait_returns_task_result(mocker):
    task = mocker.Mock()
    task.info.state = vim.TaskInfo.State.success
    task.info.result = 'result'
    assert VmdkFiles.wait(task) == 'result'


def test_wait_keeps_the_fault(mocker):
    task = mocker.Mock()
    task.info.state = vim.TaskInfo.State.error
    task.info.error = vim.fault.FileNotFound(msg='not found')
    with pytest.raises(TaskError) as error:
        VmdkFiles.wait(task)
    assert is_file_not_found(error.value)


def test_resolve(files, mocker):
    datastore = vsphere_object(mocker, name='ds1')
    datacenter = vim.Datacenter('datacenter-1')
    mocker.patch.object(files, 'find_datastore', return_value=datastore)
    mocker.patch.object(VmdkFiles, 'datacenter_of', return_value=datacenter)

    resolved = files.resolve('/vmfs/volumes/ds1/vm1/vm1.vmdk', 'path')
    assert resolved == VmdkPath(datastore, datacenter, '[ds1] vm1/vm1.vmdk')


def test_resolve_bad_path(files):
    with pytest.raises(FailJson, match='path: '):
        files.resolve('vm1.vmdk', 'path')


def test_find_datastore_by_name(files, mocker):
    datastore = vsphere_object(mocker, name='ds1')
    files.client.get_objs_by_name_or_moid.return_value = [datastore]
    assert files.find_datastore('ds1') is datastore


def test_find_datastore_in_datacenter(files, mocker):
    datacenter = mocker.Mock()
    datastore = vsphere_object(mocker, name='ds1')
    files.module.params['datacenter'] = 'dc1'
    files.client.is_vcenter.return_value = True
    files.client.get_objs_by_name_or_moid.side_effect = lambda vimtype, name, **kwargs: (
        [datacenter] if vimtype == [vim.Datacenter] else [datastore])

    assert files.find_datastore('ds1') is datastore
    assert files.client.get_objs_by_name_or_moid.call_args.kwargs['search_root_folder'] is datacenter.datastoreFolder


def test_find_datastore_missing_datacenter(files):
    files.module.params['datacenter'] = 'dc1'
    files.client.is_vcenter.return_value = True
    files.client.get_objs_by_name_or_moid.return_value = []
    with pytest.raises(FailJson, match='Unable to find datacenter'):
        files.find_datastore('ds1')


def test_find_datastore_ignores_datacenter_on_esxi(files, mocker):
    files.module.params['datacenter'] = 'dc1'
    files.client.is_vcenter.return_value = False
    files.client.get_objs_by_name_or_moid.return_value = [vsphere_object(mocker, name='ds1')]
    files.find_datastore('ds1')
    assert files.client.get_objs_by_name_or_moid.call_count == 1
    assert files.client.get_objs_by_name_or_moid.call_args.kwargs['search_root_folder'] is None


def test_find_datastore_by_vmfs_uuid(files, mocker):
    datastore = vsphere_object(mocker, name='ds1')
    datastore.info.vmfs.uuid = '61faa211-2857d4e6-1f86-34800d10ce12'
    datastore.summary.url = 'ds:///vmfs/volumes/61faa211-2857d4e6-1f86-34800d10ce12/'
    other = vsphere_object(mocker, name='other')
    other.info.vmfs.uuid = '5f3c2a10-8e5b7c3a-1d2e-0050568a1b2c'
    other.summary.url = 'ds:///vmfs/volumes/5f3c2a10-8e5b7c3a-1d2e-0050568a1b2c/'
    files.client.get_objs_by_name_or_moid.return_value = []
    files.client.get_all_objs_by_type.return_value = [other, datastore]
    assert files.find_datastore('61faa211-2857d4e6-1f86-34800d10ce12') is datastore


def test_find_datastore_missing(files):
    files.client.get_objs_by_name_or_moid.return_value = []
    files.client.get_all_objs_by_type.return_value = []
    with pytest.raises(FailJson, match='Unable to find datastore'):
        files.find_datastore('ds1')


def test_find_datastore_ambiguous(files, mocker):
    files.client.get_objs_by_name_or_moid.return_value = [vsphere_object(mocker), vsphere_object(mocker)]
    with pytest.raises(FailJson, match='set datacenter'):
        files.find_datastore('ds1')


def test_datacenter_of(mocker):
    datacenter = vim.Datacenter('datacenter-1')
    # 'parent' is a reserved argument of the Mock constructor, so set the attribute afterwards
    folder, datastore = mocker.Mock(), mocker.Mock()
    folder.parent, datastore.parent = datacenter, folder
    assert VmdkFiles.datacenter_of(datastore) is datacenter


def test_file_info(files, path, mocker):
    info = disk_info(mocker)
    mocker.patch.object(VmdkFiles, 'wait', return_value=mocker.Mock(file=[info]))
    assert files.file_info(path) is info
    search = path.datastore.browser.SearchDatastore_Task.call_args.kwargs
    assert search['datastorePath'] == '[ds1] vm1'
    assert search['searchSpec'].matchPattern == ['vm1.vmdk']


def test_file_info_missing_file(files, path, mocker):
    mocker.patch.object(VmdkFiles, 'wait', return_value=mocker.Mock(file=[]))
    assert files.file_info(path) is None


def test_file_info_missing_folder(files, path, mocker):
    mocker.patch.object(VmdkFiles, 'wait', side_effect=task_error('not found', vim.fault.FileNotFound()))
    assert files.file_info(path) is None


def test_file_info_error(files, path, mocker):
    mocker.patch.object(VmdkFiles, 'wait', side_effect=task_error('denied', vim.fault.NoPermission()))
    with pytest.raises(FailJson, match='Unable to read'):
        files.file_info(path)


def test_users(files, path, mocker):
    snapshot_backing = vim.vm.device.VirtualDisk.FlatVer2BackingInfo(
        fileName='[ds1] vm2/vm2-000001.vmdk',
        parent=vim.vm.device.VirtualDisk.FlatVer2BackingInfo(fileName='[ds1]  vm1/vm1.vmdk'))
    vm1 = vsphere_object(mocker, name='vm1')
    vm1.config.hardware.device = [flat_disk('[ds1] vm1/vm1.vmdk'), vim.vm.device.VirtualCdrom()]
    vm2 = vsphere_object(mocker, name='vm2')
    vm2.config.hardware.device = [vim.vm.device.VirtualDisk(backing=snapshot_backing)]
    vm3 = mocker.Mock(config=None)
    path.datastore.vm = [vm1, vm2, vm3]

    users = files.users(path)
    assert [(vm.name, is_parent) for vm, dummy, is_parent in users] == [('vm1', False), ('vm2', True)]


def test_facts_missing_disk(files, path):
    assert files.facts(path, None) == {
        'path': '[ds1] vm1/vm1.vmdk', 'exists': False, 'datastore': {'name': 'ds1', 'moid': 'datastore-1'}}


def test_facts(files, path, mocker):
    vm = vsphere_object(mocker, name='vm1', moid='vm-1')
    mocker.patch.object(files, 'users', return_value=[(vm, flat_disk('[ds1] vm1/vm1.vmdk', eagerly_scrub=True), False)])
    files.content.virtualDiskManager.QueryVirtualDiskUuid.return_value = '60 00 c2 9a'
    files.content.virtualDiskManager.QueryVirtualDiskGeometry.return_value = mocker.Mock(cylinder=1, head=2, sector=3)

    facts = files.facts(path, disk_info(mocker, thin=False))
    assert facts['provisioning'] == 'eagerzeroedthick'
    assert facts['capacity_bytes'] == 1024 * 1024
    assert facts['controller_type'] == 'VirtualLsiLogicController'
    assert facts['uuid'] == '60 00 c2 9a'
    assert facts['geometry'] == {'cylinders': 1, 'heads': 2, 'sectors': 3}
    assert facts['attached_to'] == [{
        'vm': {'name': 'vm1', 'moid': 'vm-1'}, 'label': 'Hard disk 1', 'disk_mode': 'persistent', 'snapshot_base': False}]


def test_facts_attached_rdm(files, path, mocker):
    backing = vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo(
        fileName='[ds1] vm1/vm1.vmdk', compatibilityMode='physicalMode', deviceName='/vmfs/devices/disks/naa.1', lunUuid='0200')
    vm = vsphere_object(mocker, name='vm1', moid='vm-1')
    mocker.patch.object(files, 'users', return_value=[(vm, vim.vm.device.VirtualDisk(backing=backing), False)])

    facts = files.facts(path, disk_info(mocker, disk_type=vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo, thin=False,
                                        extents=['[ds1] vm1/vm1-rdm.vmdk']))
    assert facts['provisioning'] == 'rdmp'
    assert facts['attached_to'][0]['rdm'] == {
        'compatibility_mode': 'physicalMode', 'device': '/vmfs/devices/disks/naa.1', 'lun_uuid': '0200'}


def test_facts_warns_on_unreadable_uuid(files, path, mocker):
    mocker.patch.object(files, 'users', return_value=[])
    files.content.virtualDiskManager.QueryVirtualDiskUuid.side_effect = vim.fault.FileFault(msg='locked')
    files.content.virtualDiskManager.QueryVirtualDiskGeometry.side_effect = vim.fault.FileFault(msg='locked')

    facts = files.facts(path, disk_info(mocker))
    assert facts['uuid'] is None
    assert facts['geometry'] is None
    assert files.module.warn.call_count == 2


def test_describe(files, path, mocker):
    info = disk_info(mocker)
    mocker.patch.object(files, 'file_info', return_value=info)
    facts = mocker.patch.object(files, 'facts', return_value={'exists': True})
    assert files.describe(path) == {'exists': True}
    facts.assert_called_once_with(path, info)
