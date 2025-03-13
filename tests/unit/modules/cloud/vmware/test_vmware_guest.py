# -*- coding: utf-8 -*-
#
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest
import json

pyvmomi = pytest.importorskip('pyVmomi')

from ansible_collections.community.vmware.plugins.modules import vmware_guest


@pytest.mark.parametrize('patch_ansible_module', [{}], indirect=['patch_ansible_module'])
@pytest.mark.usefixtures('patch_ansible_module')
def test_vmware_guest_wo_parameters(capfd):
    with pytest.raises(SystemExit):
        vmware_guest.main()
    out, err = capfd.readouterr()
    results = json.loads(out)
    assert results['failed']
    assert "one of the following is required: name, uuid" in results['msg']
