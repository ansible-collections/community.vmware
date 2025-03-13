# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import sys
import pytest

from unittest import mock

pyvmomi = pytest.importorskip('pyVmomi')

from ansible_collections.community.vmware.plugins.module_utils.vmware import option_diff

import ansible_collections.community.vmware.plugins.module_utils.vmware as vmware_module_utils


test_data = [
    (
        dict(
            username='Administrator@vsphere.local',
            password='Esxi@123$%',
            hostname=False,
            port=443,
            validate_certs=False,
            proxy_host=None,
            proxy_port=None,
        ),
        "Hostname parameter is missing. Please specify this parameter in task or"
        " export environment variable like 'export VMWARE_HOST=ESXI_HOSTNAME'"
    ),
    (
        dict(
            username=False,
            password='Esxi@123$%',
            hostname='esxi1',
            port=443,
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
            port=443,
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
            port=443,
            proxy_host=None,
            proxy_port=None,
            validate_certs=True,
        ),
        "certificate verify failed"
    ),
    (
        dict(
            username='Administrator@vsphere.local',
            password='Esxi@123$%',
            hostname='esxi1',
            port=443,
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


testdata = [
    ('HAS_PYVMOMI', 'PyVmomi'),
    ('HAS_REQUESTS', 'requests'),
]


@pytest.mark.parametrize("key,libname", testdata)
def test_lib_loading_failure(monkeypatch, fake_ansible_module, key, libname):
    """ Test if Pyvmomi is present or not"""
    monkeypatch.setattr(vmware_module_utils, key, False)
    with pytest.raises(FailJsonException):
        vmware_module_utils.PyVmomi(fake_ansible_module)
    error_str = 'Failed to import the required Python library (%s)' % libname
    fake_ansible_module.fail_json.assert_called_once()
    assert error_str in fake_ansible_module.fail_json.call_args[1]['msg']


@pytest.mark.skipif(sys.version_info < (2, 7), reason="requires python2.7 and greater")
@pytest.mark.parametrize("params, msg", test_data, ids=test_ids)
def test_required_params(request, params, msg, fake_ansible_module):
    """ Test if required params are correct or not"""
    fake_ansible_module.params = params
    with pytest.raises(FailJsonException):
        vmware_module_utils.connect_to_api(fake_ansible_module)
    fake_ansible_module.fail_json.assert_called_once()
    # TODO: assert msg in fake_ansible_module.fail_json.call_args[1]['msg']


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
