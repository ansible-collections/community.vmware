# -*- coding: utf-8 -*-

# Copyright: (c) 2016, Charles Paul <cpaul@ansible.com>
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2019, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class ModuleDocFragment(object):
    # This document fragment serves as a compliment to the vmware.vmware.base documentation fragment for modules
    # that use the REST API SDK. You must include the base fragment in addition to this
    #
    # This vmware.vmware.additional_rest_options fragment will cover any options returned by rest_compatible_argument_spec()
    # that are not included in vmware.vmware.base
    DOCUMENTATION = r'''
options:
  proxy_protocol:
    description:
      - The proxy connection protocol to use.
      - This option is used if the correct proxy protocol cannot be automatically determined.
    type: str
    choices: [ http, https ]
    default: https
    aliases: [protocol]
'''
