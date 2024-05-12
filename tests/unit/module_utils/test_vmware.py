# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest

from unittest import mock

pyvmomi = pytest.importorskip('pyVmomi')

from ansible_collections.community.vmware.plugins.module_utils.vmware import option_diff

import ansible_collections.community.vmware.plugins.module_utils.vmware as vmware_module_utils
import ansible_collections.vmware.vmware.plugins.module_utils.vmware as parent_vmware_module_utils


test_data = [
    (
        dict(
            username='Administrator@vsphere.local',
            password='Esxi@123$%',
            hostname=False,
            validate_certs=False,
        ),
        "Hostname parameter is missing. Please specify this parameter in task or"
        " export environment variable like 'export VMWARE_HOST=ESXI_HOSTNAME'"
    ),
    (
        dict(
            username=False,
            password='Esxi@123$%',
            hostname='esxi1',
            validate_certs=False,
        ),
        "Username parameter is missing. Please specify this parameter in task or"
        " export environment variable like 'export VMWARE_USER=ESXI_USERNAME'"
    ),
    (
        dict(
            username='Administrator@vsphere.local',
            password=False,
            hostname='esxi1',
            validate_certs=False,
        ),
        "Password parameter is missing. Please specify this parameter in task or"
        " export environment variable like 'export VMWARE_PASSWORD=ESXI_PASSWORD'"
    ),
    (
        dict(
            username='Administrator@vsphere.local',
            password='Esxi@123$%',
            hostname='esxi1',
            validate_certs=True,
        ),
        "certificate verify failed"
    ),
    (
        dict(
            username='Administrator@vsphere.local',
            password='Esxi@123$%',
            hostname='esxi1',
            proxy_host='myproxyserver.com',
            proxy_port=80,
            validate_certs=False,
        ),
        " [proxy: myproxyserver.com:80]"
    ),
]

test_ids = [
    'hostname',
    'username',
    'password',
    'validate_certs',
    'valid_http_proxy',
]


class FailJsonException(BaseException):
    pass


@pytest.fixture
def fake_ansible_module():
    ret = mock.Mock()
    ret.params = test_data[3][0]
    ret.tmpdir = None
    ret.fail_json.side_effect = FailJsonException()
    return ret


def fake_connect_to_api(module, return_si=None):
    return None, mock.Mock()


def test_validate_certs(monkeypatch, fake_ansible_module):
    """ Test if SSL is required or not"""
    fake_ansible_module.params = test_data[3][0]

    monkeypatch.setattr(vmware_module_utils, 'ssl', mock.Mock())
    del vmware_module_utils.ssl.SSLContext
    with pytest.raises(FailJsonException):
        vmware_module_utils.PyVmomi(fake_ansible_module)
    msg = 'pyVim does not support changing verification mode with python < 2.7.9.' \
          ' Either update python or use validate_certs=false.'
    fake_ansible_module.fail_json.assert_called_once()
    assert msg == fake_ansible_module.fail_json.call_args[1]['msg']


def test_vmdk_disk_path_split(monkeypatch, fake_ansible_module):
    """ Test vmdk_disk_path_split function"""
    fake_ansible_module.params = test_data[0][0]

    monkeypatch.setattr(parent_vmware_module_utils, 'connect_to_api', fake_connect_to_api)
    pyv = vmware_module_utils.PyVmomi(fake_ansible_module)
    v = pyv.vmdk_disk_path_split('[ds1] VM_0001/VM0001_0.vmdk')
    assert v == ('ds1', 'VM_0001/VM0001_0.vmdk', 'VM0001_0.vmdk', 'VM_0001')


def test_vmdk_disk_path_split_negative(monkeypatch, fake_ansible_module):
    """ Test vmdk_disk_path_split function"""
    fake_ansible_module.params = test_data[0][0]

    monkeypatch.setattr(parent_vmware_module_utils, 'connect_to_api', fake_connect_to_api)
    with pytest.raises(FailJsonException):
        pyv = vmware_module_utils.PyVmomi(fake_ansible_module)
        pyv.vmdk_disk_path_split('[ds1]')
    fake_ansible_module.fail_json.assert_called_once()
    assert 'Bad path' in fake_ansible_module.fail_json.call_args[1]['msg']


@pytest.mark.parametrize("test_options, test_current_options, test_truthy_strings_as_bool", [
    ({"data": True}, [], True),
    ({"data": 1}, [], True),
    ({"data": 1.2}, [], True),
    ({"data": 'string'}, [], True),
    ({"data": True}, [], False),
    ({"data": 1}, [], False),
    ({"data": 1.2}, [], False),
    ({"data": 'string'}, [], False),
])
def test_option_diff(test_options, test_current_options, test_truthy_strings_as_bool):
    assert option_diff(test_options, test_current_options, test_truthy_strings_as_bool)[0].value == test_options["data"]
