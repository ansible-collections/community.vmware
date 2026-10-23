# -*- coding: utf-8 -*-

# Copyright: (c) 2026, Everpure Inc.
# Copyright: (c) 2026, Eugenio Grosso <eugenio.grosso@everpuredata.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import re
from collections import namedtuple

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass
    # handled in PyVmomi

from ansible.module_utils.common.text.converters import to_native

from ansible_collections.community.vmware.plugins.module_utils.vmware import (
    TaskError,
    wait_for_task
)


DS_PATH_RE = re.compile(r'^\[(?P<ds>[^\]]+)\]\s*(?P<rel>.*)$')
VOLUMES_PREFIX = '/vmfs/volumes/'

VmdkPath = namedtuple('VmdkPath', ['datastore', 'datacenter', 'ds_path'])


def parse_vmdk_path(value):
    """
    Split a virtual disk path into the datastore identifier and the path inside the datastore.
    Args:
        value: str, '[datastore] dir/disk.vmdk' or '/vmfs/volumes/<datastore name or uuid>/dir/disk.vmdk'
    Returns:
        (str, str), the datastore identifier and the relative path
    Raises:
        ValueError if the value is not a datastore path to a .vmdk file
    """
    value = (value or '').strip()
    match = DS_PATH_RE.match(value)
    if match:
        datastore, relative = match.group('ds'), match.group('rel')
    elif value.startswith(VOLUMES_PREFIX):
        parts = value[len(VOLUMES_PREFIX):].split('/', 1)
        datastore, relative = parts[0], parts[1] if len(parts) > 1 else ''
    else:
        raise ValueError("'%s' must be a datastore path like '[datastore] dir/disk.vmdk' or start with %s" % (value, VOLUMES_PREFIX))

    relative = relative.strip().lstrip('/')
    if not datastore or not relative.lower().endswith('.vmdk'):
        raise ValueError("'%s' must point to a .vmdk descriptor" % value)
    return datastore, relative


def split_ds_path(ds_path):
    """
    Split '[ds] dir/sub/disk.vmdk' into ('[ds] dir/sub', 'disk.vmdk').
    """
    match = DS_PATH_RE.match(ds_path)
    relative = match.group('rel')
    if '/' in relative:
        folder, name = relative.rsplit('/', 1)
        return '[%s] %s' % (match.group('ds'), folder), name
    return '[%s]' % match.group('ds'), relative


def type_short_name(vim_type):
    """
    Return the short class name of a type reported by the API, for example FlatVer2BackingInfo.
    """
    if vim_type is None:
        return None
    name = getattr(vim_type, '__name__', str(vim_type))
    return name.rsplit('.', 1)[-1]


def provisioning_of(backing_type, thin, extents, compatibility_mode=None, eagerly_scrub=None):
    """
    Derive the vmkfstools style disk format from what the datastore browser and attached VMs report.
    Args:
        backing_type: str, short backing type name, for example FlatVer2BackingInfo
        thin: bool or None, the thin flag reported by the datastore browser
        extents: list(str), the disk extents; ESXi names the mapping file of a physical RDM <disk>-rdmp.vmdk
        compatibility_mode: str or None, physicalMode or virtualMode when a VM uses the RDM
        eagerly_scrub: bool or None, the eager zeroing flag when a VM uses the disk
    Returns:
        str or None, one of thin, zeroedthick, eagerzeroedthick, thick, sparse, rdm, rdmp
    """
    if backing_type and 'RawDiskMapping' in backing_type:
        if compatibility_mode:
            return 'rdmp' if compatibility_mode == 'physicalMode' else 'rdm'
        return 'rdmp' if any(extent.endswith('-rdmp.vmdk') for extent in extents) else 'rdm'
    if thin:
        return 'thin'
    if backing_type and 'Sparse' in backing_type:
        return 'sparse'
    if eagerly_scrub is not None:
        return 'eagerzeroedthick' if eagerly_scrub else 'zeroedthick'
    if thin is False:
        # the datastore browser does not report eager zeroing for detached disks
        return 'thick'
    return None


def is_file_not_found(error):
    """
    Return True if a TaskError raised by wait_for_task comes from a FileNotFound fault.
    """
    return isinstance(getattr(error, '__cause__', None), vim.fault.FileNotFound)


class VmdkFiles():
    """
    Virtual disk file operations shared by the vmware_vmdk_* modules. Wraps a PyVmomi instance.
    """
    def __init__(self, client):
        self.client = client
        self.module = client.module
        self.content = client.content

    @staticmethod
    def wait(task, timeout=3600):
        """
        Wait for a vSphere task and return its result. Raises TaskError on failure, with the fault as __cause__.
        """
        return wait_for_task(task, timeout=timeout)[1]

    def resolve(self, value, option):
        """
        Resolve a user provided disk path.
        Args:
            value: str, the disk path
            option: str, the option name, used in error messages
        Returns:
            VmdkPath with the datastore object, its datacenter object and the normalized '[datastore] path'
        """
        try:
            datastore_id, relative = parse_vmdk_path(value)
        except ValueError as e:
            self.module.fail_json(msg='%s: %s' % (option, to_native(e)))
        datastore = self.find_datastore(datastore_id)
        return VmdkPath(datastore, self.datacenter_of(datastore), '[%s] %s' % (datastore.name, relative))

    def find_datastore(self, identifier):
        """
        Find a datastore by name, MOID, VMFS UUID or the last element of its URL. On vCenter the search can be limited
        to the datacenter given in the datacenter parameter, which is ignored on an ESXi host.
        """
        search_folder = None
        datacenter_name = self.module.params.get('datacenter')
        if datacenter_name and self.client.is_vcenter():
            datacenters = self.client.get_objs_by_name_or_moid([vim.Datacenter], datacenter_name)
            if not datacenters:
                self.module.fail_json(msg="Unable to find datacenter with name or MOID %s" % datacenter_name)
            search_folder = datacenters[0].datastoreFolder

        matches = self.client.get_objs_by_name_or_moid([vim.Datastore], identifier, return_all=True, search_root_folder=search_folder)
        if not matches:
            for datastore in self.client.get_all_objs_by_type([vim.Datastore], folder=search_folder):
                vmfs = getattr(datastore.info, 'vmfs', None)
                url = (datastore.summary.url or '').rstrip('/')
                if (vmfs is not None and vmfs.uuid == identifier) or url.endswith('/' + identifier):
                    matches.append(datastore)
        if not matches:
            self.module.fail_json(msg="Unable to find datastore with name, MOID or UUID %s" % identifier)
        if len(matches) > 1:
            self.module.fail_json(msg="Several datastores match %s; set datacenter to choose one" % identifier)
        return matches[0]

    @staticmethod
    def datacenter_of(managed_object):
        """
        Return the datacenter that contains a managed object.
        """
        parent = managed_object.parent
        while parent is not None and not isinstance(parent, vim.Datacenter):
            parent = parent.parent
        return parent

    def file_info(self, path):
        """
        Return the VmDiskInfo of a descriptor, or None if it does not exist.
        Args:
            path: VmdkPath
        """
        folder, name = split_ds_path(path.ds_path)
        details = vim.host.DatastoreBrowser.VmDiskQuery.Details(
            diskType=True, capacityKb=True, hardwareVersion=True, controllerType=True, diskExtents=True, thin=True)
        spec = vim.host.DatastoreBrowser.SearchSpec(
            query=[vim.host.DatastoreBrowser.VmDiskQuery(details=details)],
            matchPattern=[name],
            details=vim.host.DatastoreBrowser.FileInfo.Details(fileType=True, fileSize=True, modification=True))
        try:
            result = self.wait(path.datastore.browser.SearchDatastore_Task(datastorePath=folder, searchSpec=spec))
        except TaskError as e:
            if is_file_not_found(e):
                return None
            self.module.fail_json(msg='Unable to read %s: %s' % (path.ds_path, to_native(e)))
        for item in getattr(result, 'file', None) or []:
            if item.path == name:
                return item
        return None

    def users(self, path):
        """
        Return [(vm, VirtualDisk, is_snapshot_parent)] for the VMs whose disks use the descriptor.
        """
        users = []
        wanted = re.sub(r'\s+', ' ', path.ds_path)
        for vm in path.datastore.vm:
            try:
                devices = vm.config.hardware.device
            except AttributeError:
                continue
            for device in devices:
                if not isinstance(device, vim.vm.device.VirtualDisk):
                    continue
                backing, depth = device.backing, 0
                while backing is not None:
                    if re.sub(r'\s+', ' ', getattr(backing, 'fileName', '') or '') == wanted:
                        users.append((vm, device, depth > 0))
                        break
                    backing, depth = getattr(backing, 'parent', None), depth + 1
        return users

    def facts(self, path, info):
        """
        Describe a disk.
        Args:
            path: VmdkPath
            info: VmDiskInfo from file_info, or None if the disk does not exist
        Returns:
            dict
        """
        facts = {
            'path': path.ds_path,
            'exists': info is not None,
            'datastore': {'name': path.datastore.name, 'moid': path.datastore._GetMoId()},
        }
        if info is None:
            return facts

        extents = list(info.diskExtents or [])
        attached, compatibility_mode, eagerly_scrub = [], None, None
        for vm, device, is_parent in self.users(path):
            backing = device.backing
            entry = {
                'vm': {'name': vm.name, 'moid': vm._GetMoId()},
                'label': device.deviceInfo.label if device.deviceInfo else None,
                'disk_mode': getattr(backing, 'diskMode', None),
                'snapshot_base': is_parent,
            }
            if isinstance(backing, vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo):
                compatibility_mode = backing.compatibilityMode
                entry['rdm'] = {
                    'compatibility_mode': backing.compatibilityMode,
                    'device': backing.deviceName,
                    'lun_uuid': backing.lunUuid,
                }
            elif not is_parent and getattr(backing, 'eagerlyScrub', None) is not None:
                eagerly_scrub = bool(backing.eagerlyScrub) or bool(eagerly_scrub)
            attached.append(entry)

        backing_type = type_short_name(info.diskType)
        facts.update({
            'backing_type': backing_type,
            'provisioning': provisioning_of(backing_type, info.thin, extents, compatibility_mode, eagerly_scrub),
            'capacity_bytes': info.capacityKb * 1024 if info.capacityKb is not None else None,
            'file_size_bytes': info.fileSize,
            'thin': info.thin,
            'controller_type': type_short_name(info.controllerType),
            'hardware_version': info.hardwareVersion,
            'extents': extents,
            'modification_time': info.modification.isoformat() if info.modification else None,
            'attached_to': attached,
        })

        manager = self.content.virtualDiskManager
        try:
            facts['uuid'] = manager.QueryVirtualDiskUuid(name=path.ds_path, datacenter=path.datacenter)
        except vmodl.MethodFault as e:
            facts['uuid'] = None
            self.module.warn('Unable to read the UUID of %s: %s' % (path.ds_path, to_native(e.msg)))
        try:
            geometry = manager.QueryVirtualDiskGeometry(name=path.ds_path, datacenter=path.datacenter)
            facts['geometry'] = {'cylinders': geometry.cylinder, 'heads': geometry.head, 'sectors': geometry.sector}
        except vmodl.MethodFault as e:
            facts['geometry'] = None
            self.module.warn('Unable to read the geometry of %s: %s' % (path.ds_path, to_native(e.msg)))
        return facts

    def describe(self, path):
        """
        Look up a disk and describe it.
        """
        return self.facts(path, self.file_info(path))
