#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, sky-joker
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
module: vmware_vcenter_settings_info
short_description: Gather info vCenter settings
description:
  - This module can be used to gather information about vCenter settings.
author:
  - sky-joker (@sky-joker)
requirements:
  - python >= 2.7
  - PyVmomi
extends_documentation_fragment:
  - community.vmware.vmware.documentation
'''

EXAMPLES = r'''
- name: "Gather info about vCenter settings"
  community.vmware.vmware_vcenter_settings_info:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    validate_certs: no
  register: vcenter_settings_info
'''

RETURN = r'''
vcenter_config_info:
  description: dict of vCenter settings
  returned: success
  type: dict
  sample: |
    {
        "db_event_cleanup_previous": true,
        "db_event_retention_previous": 30,
        "db_max_connections_previous": 50,
        "db_task_cleanup_previous": true,
        "db_task_retention_previous": 30,
        "directory_query_limit_previous": true,
        "directory_query_limit_size_previous": 5000,
        "directory_timeout_previous": 60,
        "directory_validation_period_previous": 1440,
        "directory_validation_previous": true,
        "logging_options_previous": "info",
        "mail_sender_previous": "",
        "mail_server_previous": "",
        "runtime_managed_address_previous": "",
        "runtime_server_name_previous": "vcenter.local",
        "runtime_unique_id_previous": 48,
        "snmp_1_community_previous": "public",
        "snmp_1_enabled_previous": true,
        "snmp_1_url_previous": "localhost",
        "snmp_2_community_previous": "",
        "snmp_2_enabled_previous": false,
        "snmp_2_url_previous": "",
        "snmp_3_community_previous": "",
        "snmp_3_enabled_previous": false,
        "snmp_3_url_previous": "",
        "snmp_4_community_previous": "",
        "snmp_4_enabled_previous": false,
        "snmp_4_url_previous": "",
        "snmp_receiver_1_port_previous": 162,
        "snmp_receiver_2_port_previous": 162,
        "snmp_receiver_3_port_previous": 162,
        "snmp_receiver_4_port_previous": 162,
        "timeout_long_operations_previous": 120,
        "timeout_normal_operations_previous": 30
    }
'''

try:
    from pyVmomi import vim
except ImportError:
    pass

from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, vmware_argument_spec
from ansible.module_utils.basic import AnsibleModule


class VmwareVcenterSettingsInfo(PyVmomi):
    def __init__(self, module):
        super(VmwareVcenterSettingsInfo, self).__init__(module)

        if not self.is_vcenter():
            self.module.fail_json(msg="You have to connect to a vCenter server!")

    def ensure(self):
        result = {}
        option_manager = self.content.setting
        for setting in option_manager.setting:
            # Database
            if setting.key == 'VirtualCenter.MaxDBConnection':
                result['db_max_connections_previous'] = setting.value

            if setting.key == 'task.maxAgeEnabled':
                result['db_task_cleanup_previous'] = setting.value

            if setting.key == 'task.maxAge':
                result['db_task_retention_previous'] = setting.value

            if setting.key == 'event.maxAgeEnabled':
                result['db_event_cleanup_previous'] = setting.value

            if setting.key == 'event.maxAge':
                result['db_event_retention_previous'] = setting.value

            # Runtime settings
            if setting.key == 'instance.id':
                result['runtime_unique_id_previous'] = setting.value

            if setting.key == 'VirtualCenter.ManagedIP':
                result['runtime_managed_address_previous'] = setting.value

            if setting.key == 'VirtualCenter.InstanceName':
                result['runtime_server_name_previous'] = setting.value

            # User directory
            if setting.key == 'ads.timeout':
                result['directory_timeout_previous'] = setting.value

            if setting.key == 'ads.maxFetchEnabled':
                result['directory_query_limit_previous'] = setting.value

            if setting.key == 'ads.maxFetch':
                result['directory_query_limit_size_previous'] = setting.value

            if setting.key == 'ads.checkIntervalEnabled':
                result['directory_validation_previous'] = setting.value

            if setting.key == 'ads.checkInterval':
                result['directory_validation_period_previous'] = setting.value

            # Mail
            if setting.key == 'mail.smtp.server':
                result['mail_server_previous'] = setting.value

            if setting.key == 'mail.sender':
                result['mail_sender_previous'] = setting.value

            # SNMP receivers - SNMP receiver #1
            if setting.key == 'snmp.receiver.1.enabled':
                result['snmp_1_enabled_previous'] = setting.value

            if setting.key == 'snmp.receiver.1.name':
                result['snmp_1_url_previous'] = setting.value

            if setting.key == 'snmp.receiver.1.port':
                result['snmp_receiver_1_port_previous'] = setting.value

            if setting.key == 'snmp.receiver.1.community':
                result['snmp_1_community_previous'] = setting.value

            # SNMP receivers - SNMP receiver #2
            if setting.key == 'snmp.receiver.2.enabled':
                result['snmp_2_enabled_previous'] = setting.value

            if setting.key == 'snmp.receiver.2.name':
                result['snmp_2_url_previous'] = setting.value

            if setting.key == 'snmp.receiver.2.port':
                result['snmp_receiver_2_port_previous'] = setting.value

            if setting.key == 'snmp.receiver.2.community':
                result['snmp_2_community_previous'] = setting.value

            # SNMP receivers - SNMP receiver #3
            if setting.key == 'snmp.receiver.3.enabled':
                result['snmp_3_enabled_previous'] = setting.value

            if setting.key == 'snmp.receiver.3.name':
                result['snmp_3_url_previous'] = setting.value

            if setting.key == 'snmp.receiver.3.port':
                result['snmp_receiver_3_port_previous'] = setting.value

            if setting.key == 'snmp.receiver.3.community':
                result['snmp_3_community_previous'] = setting.value

            # SNMP receivers - SNMP receiver #4
            if setting.key == 'snmp.receiver.4.enabled':
                result['snmp_4_enabled_previous'] = setting.value

            if setting.key == 'snmp.receiver.4.name':
                result['snmp_4_url_previous'] = setting.value

            if setting.key == 'snmp.receiver.4.port':
                result['snmp_receiver_4_port_previous'] = setting.value

            if setting.key == 'snmp.receiver.4.community':
                result['snmp_4_community_previous'] = setting.value

            # Timeout settings
            if setting.key == 'client.timeout.normal':
                result['timeout_normal_operations_previous'] = setting.value

            if setting.key == 'client.timeout.long':
                result['timeout_long_operations_previous'] = setting.value

            # Logging settings
            if setting.key == 'log.level':
                result['logging_options_previous'] = setting.value

        self.module.exit_json(changed=False, vcenter_config_info=result)


def main():
    argument_spec = vmware_argument_spec()

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    vmware_vcenter_settings_info = VmwareVcenterSettingsInfo(module)
    vmware_vcenter_settings_info.ensure()


if __name__ == '__main__':
    main()
