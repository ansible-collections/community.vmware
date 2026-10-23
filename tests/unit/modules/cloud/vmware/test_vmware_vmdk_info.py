# Copyright: (c) 2026, Everpure Inc.
# Copyright: (c) 2026, Eugenio Grosso <eugenio.grosso@everpuredata.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from ansible.module_utils import basic
from ansible.module_utils.testing import patch_module_args

from ansible_collections.community.vmware.plugins.modules.vmware_vmdk_info import (
    VmdkInfoModule,
    main as module_main
)
from ansible_collections.community.vmware.plugins.module_utils.vmware_vmdk import (
    VmdkFiles,
    VmdkPath
)
from ansible_collections.vmware.vmware.plugins.module_utils.clients.pyvmomi import (
    PyvmomiClient
)

CONNECTION = dict(hostname='127.0.0.1', username='test', password='test')


class AnsibleExitJson(Exception):
    pass


class AnsibleFailJson(Exception):
    pass


def exit_json(*args, **kwargs):
    kwargs.setdefault('changed', False)
    raise AnsibleExitJson(kwargs)


def fail_json(*args, **kwargs):
    kwargs['failed'] = True
    raise AnsibleFailJson(kwargs)


def run_module(mocker, module_args, expect_success=True):
    """
    Run the module with the given arguments and return what it passed to exit_json or fail_json.
    """
    mocker.patch.multiple(basic.AnsibleModule, exit_json=exit_json, fail_json=fail_json)
    args = dict(CONNECTION, _ansible_remote_tmp='/tmp', _ansible_keep_remote_files=False, **module_args)
    with pytest.raises(AnsibleExitJson if expect_success else AnsibleFailJson) as result, patch_module_args(args):
        module_main()
    return result.value.args[0]


class TestVmdkInfo():

    def __prepare(self, mocker, facts):
        mocker.patch.object(PyvmomiClient, 'connect_to_api', return_value=(mocker.Mock(), mocker.Mock()))
        datastore = mocker.Mock()
        datastore.name = 'ds1'
        self.path = VmdkPath(datastore, mocker.Mock(), '[ds1] vm1/vm1.vmdk')
        self.resolve = mocker.patch.object(VmdkFiles, 'resolve', return_value=self.path)
        self.describe = mocker.patch.object(VmdkFiles, 'describe', return_value=facts)

    def test_existing_disk(self, mocker):
        facts = {'path': '[ds1] vm1/vm1.vmdk', 'exists': True, 'provisioning': 'thin'}
        self.__prepare(mocker, facts)

        result = run_module(mocker, dict(path='/vmfs/volumes/ds1/vm1/vm1.vmdk'))
        assert result['changed'] is False
        assert result['vmdk'] == facts
        self.resolve.assert_called_once_with('/vmfs/volumes/ds1/vm1/vm1.vmdk', 'path')
        self.describe.assert_called_once_with(self.path)

    def test_missing_disk(self, mocker):
        self.__prepare(mocker, {'path': '[ds1] vm1/vm1.vmdk', 'exists': False})

        result = run_module(mocker, dict(path='[ds1] vm1/vm1.vmdk'))
        assert result['changed'] is False
        assert result['vmdk']['exists'] is False

    def test_check_mode(self, mocker):
        self.__prepare(mocker, {'path': '[ds1] vm1/vm1.vmdk', 'exists': True})

        result = run_module(mocker, dict(path='[ds1] vm1/vm1.vmdk', _ansible_check_mode=True))
        assert result['changed'] is False
        assert result['vmdk']['exists'] is True

    def test_path_is_required(self, mocker):
        self.__prepare(mocker, {})

        result = run_module(mocker, dict(), expect_success=False)
        assert 'path' in result['msg']

    def test_gather_info(self, mocker):
        self.__prepare(mocker, {'exists': True})
        params = dict(CONNECTION, port=443, validate_certs=False, proxy_host=None, proxy_port=None, path='[ds1] vm1/vm1.vmdk')
        module = mocker.Mock(params=params)

        assert VmdkInfoModule(module).gather_info() == {'exists': True}
