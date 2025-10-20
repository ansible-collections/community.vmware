#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Christian Kotte <christian.kotte@gmx.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: vmware_vcenter_settings
short_description: Configures general settings on a vCenter server
description:
- This module can be used to configure the vCenter server general settings (except the statistics).
- The statistics can be configured with the module M(community.vmware.vmware_vcenter_statistics).
author:
- Christian Kotte (@ckotte)
options:
    database:
        description:
            - The database settings for vCenter server.
        suboptions:
            max_connections:
                type: int
                description: Maximum connections.
                default: 50
            task_cleanup:
                type: bool
                description: Task cleanup.
                default: true
            task_retention:
                type: int
                description: Task retention in days.
                default: 30
            event_cleanup:
                type: bool
                description: Event cleanup.
                default: true
            event_retention:
                type: int
                description: Event retention in days.
                default: 30
        type: dict
        default: {
            max_connections: 50,
            task_cleanup: true,
            task_retention: 30,
            event_cleanup: true,
            event_retention: 30,
        }
    runtime_settings:
        description:
            - The unique runtime settings for vCenter server.
        suboptions:
            unique_id:
                type: int
                description: vCenter server unique ID.
            managed_address:
                type: str
                description: vCenter server managed address.
            vcenter_server_name:
                type: str
                description: vCenter server name. Default is FQDN.
        type: dict
    user_directory:
        description:
            - The user directory settings for the vCenter server installation.
        suboptions:
            timeout:
                type: int
                description: User directory timeout.
                default: 60
            query_limit:
                type: bool
                description: Query limit.
                default: true
            query_limit_size:
                type: int
                description: Query limit size.
                default: 5000
            validation:
                type: bool
                description: Mail Validation.
                default: true
            validation_period:
                type: int
                description: Validation period.
                default: 1440
        type: dict
        default: {
            timeout: 60,
            query_limit: true,
            query_limit_size: 5000,
            validation: true,
            validation_period: 1440,
        }
    mail:
        description:
            - The settings vCenter server uses to send email alerts.
        suboptions:
            server:
                type: str
                description: Mail server.
            sender:
                type: str
                description: Mail sender address.
        type: dict
        default: {
            server: '',
            sender: '',
        }
    snmp_receivers:
        description:
            - SNMP trap destinations for vCenter server alerts.
        suboptions:
            snmp_receiver_1_url:
                type: str
                description: Primary Receiver ULR.
                default: "localhost"
            snmp_receiver_1_enabled:
                type: bool
                description: Enable receiver.
                default: true
            snmp_receiver_1_port:
                type: int
                description: Receiver port.
                default: 162
            snmp_receiver_1_community:
                type: str
                description: Community string.
                default: "public"
            snmp_receiver_2_url:
                type: str
                description: Receiver 2 ULR.
                default: ""
            snmp_receiver_2_enabled:
                type: bool
                description: Enable receiver.
                default: false
            snmp_receiver_2_port:
                type: int
                description: Receiver port.
                default: 162
            snmp_receiver_2_community:
                type: str
                description: Community string.
                default: ""
            snmp_receiver_3_url:
                type: str
                description: Receiver 3 ULR.
                default: ""
            snmp_receiver_3_enabled:
                type: bool
                description: Enable receiver.
                default: false
            snmp_receiver_3_port:
                type: int
                description: Receiver port.
                default: 162
            snmp_receiver_3_community:
                type: str
                description: Community string.
                default: ""
            snmp_receiver_4_url:
                type: str
                description: Receiver 4 ULR.
                default: ""
            snmp_receiver_4_enabled:
                type: bool
                description: Enable receiver.
                default: false
            snmp_receiver_4_port:
                type: int
                description: Receiver port.
                default: 162
            snmp_receiver_4_community:
                type: str
                description: Community string.
                default: ""
        type: dict
        default: {
            snmp_receiver_1_url: 'localhost',
            snmp_receiver_1_enabled: true,
            snmp_receiver_1_port: 162,
            snmp_receiver_1_community: 'public',
            snmp_receiver_2_url: '',
            snmp_receiver_2_enabled: false,
            snmp_receiver_2_port: 162,
            snmp_receiver_2_community: '',
            snmp_receiver_3_url: '',
            snmp_receiver_3_enabled: false,
            snmp_receiver_3_port: 162,
            snmp_receiver_3_community: '',
            snmp_receiver_4_url: '',
            snmp_receiver_4_enabled: false,
            snmp_receiver_4_port: 162,
            snmp_receiver_4_community: '',
        }
    timeout_settings:
        description:
            - The vCenter server connection timeout for normal and long operations.
        suboptions:
            normal_operations:
                type: int
                description: Normal operation timeout.
                default: 30
            long_operations:
                type: int
                description: Long operation timeout.
                default: 120
        type: dict
        default: {
            normal_operations: 30,
            long_operations: 120,
        }
    logging_options:
        description:
            - The level of detail that vCenter server usesfor log files.
        type: str
        choices: ['none', 'error', 'warning', 'info', 'verbose', 'trivia']
        default: 'info'
    advanced_settings:
      description:
      - A dictionary of advanced settings.
      default: {}
      type: dict
extends_documentation_fragment:
- vmware.vmware.base_options

'''

EXAMPLES = r'''
- name: Configure vCenter general settings
  community.vmware.vmware_vcenter_settings:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    database:
      max_connections: 50
      task_cleanup: true
      task_retention: 30
      event_cleanup: true
      event_retention: 30
    runtime_settings:
      unique_id: 1
      managed_address: "{{ lookup('dig', inventory_hostname) }}"
      vcenter_server_name: "{{ inventory_hostname }}"
    user_directory:
      timeout: 60
      query_limit: true
      query_limit_size: 5000
      validation: true
      validation_period: 1440
    mail:
      server: mail.example.com
      sender: vcenter@{{ inventory_hostname }}
    snmp_receivers:
      snmp_receiver_1_url: localhost
      snmp_receiver_1_enabled: true
      snmp_receiver_1_port: 162
      snmp_receiver_1_community: public
    timeout_settings:
      normal_operations: 30
      long_operations: 120
    logging_options: info
  delegate_to: localhost

- name: Enable Retreat Mode for cluster with MOID domain-c8 (https://kb.vmware.com/kb/80472)
  community.vmware.vmware_vcenter_settings:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    advanced_settings:
      'config.vcls.clusters.domain-c8.enabled': 'false'
  delegate_to: localhost
'''

RETURN = r'''
results:
    description:
      - metadata about vCenter settings
      - supported diff mode from version 1.8.0
    returned: always
    type: dict
    sample: {
        "changed": false,
        "db_event_cleanup": true,
        "db_event_retention": 30,
        "db_max_connections": 50,
        "db_task_cleanup": true,
        "db_task_retention": 30,
        "directory_query_limit": true,
        "directory_query_limit_size": 5000,
        "directory_timeout": 60,
        "directory_validation": true,
        "directory_validation_period": 1440,
        "logging_options": "info",
        "mail_sender": "vcenter@vcenter01.example.com",
        "mail_server": "mail.example.com",
        "msg": "vCenter settings already configured properly",
        "runtime_managed_address": "192.168.1.10",
        "runtime_server_name": "vcenter01.example.com",
        "runtime_unique_id": 1,
        "timeout_long_operations": 120,
        "timeout_normal_operations": 30,
        "diff": {
           "after": {
               "db_event_cleanup": true,
               "db_event_retention": 30,
               "db_max_connections": 50,
               "db_task_cleanup": true,
               "db_task_retention": 30,
               "directory_query_limit": true,
               "directory_query_limit_size": 5000,
               "directory_timeout": 60,
               "directory_validation": true,
               "directory_validation_period": 1440,
               "logging_options": "info",
               "mail_sender": "vcenter@vcenter01.example.com",
               "mail_server": "mail.example.com",
               "runtime_managed_address": "192.168.1.10",
               "runtime_server_name": "vcenter01.example.com",
               "runtime_unique_id": 1,
               "snmp_receiver_1_community": "public",
               "snmp_receiver_1_enabled": true,
               "snmp_receiver_1_port": 162,
               "snmp_receiver_1_url": "localhost",
               "snmp_receiver_2_community": "",
               "snmp_receiver_2_enabled": false,
               "snmp_receiver_2_port": 162,
               "snmp_receiver_2_url": "",
               "snmp_receiver_3_community": "",
               "snmp_receiver_3_enabled": false,
               "snmp_receiver_3_port": 162,
               "snmp_receiver_3_url": "",
               "snmp_receiver_4_community": "",
               "snmp_receiver_4_enabled": false,
               "snmp_receiver_4_port": 162,
               "snmp_receiver_4_url": "",
               "timeout_long_operations": 120,
               "timeout_normal_operations": 30
           },
           "before": {
               "db_event_cleanup": true,
               "db_event_retention": 30,
               "db_max_connections": 50,
               "db_task_cleanup": true,
               "db_task_retention": 30,
               "directory_query_limit": true,
               "directory_query_limit_size": 5000,
               "directory_timeout": 60,
               "directory_validation": true,
               "directory_validation_period": 1440,
               "logging_options": "info",
               "mail_sender": "vcenter@vcenter01.example.com",
               "mail_server": "mail.example.com",
               "runtime_managed_address": "192.168.1.10",
               "runtime_server_name": "vcenter01.example.com",
               "runtime_unique_id": 1,
               "snmp_receiver_1_community": "public",
               "snmp_receiver_1_enabled": true,
               "snmp_receiver_1_port": 162,
               "snmp_receiver_1_url": "localhost",
               "snmp_receiver_2_community": "",
               "snmp_receiver_2_enabled": false,
               "snmp_receiver_2_port": 162,
               "snmp_receiver_2_url": "",
               "snmp_receiver_3_community": "",
               "snmp_receiver_3_enabled": false,
               "snmp_receiver_3_port": 162,
               "snmp_receiver_3_url": "",
               "snmp_receiver_4_community": "",
               "snmp_receiver_4_enabled": false,
               "snmp_receiver_4_port": 162,
               "snmp_receiver_4_url": "",
               "timeout_long_operations": 120,
               "timeout_normal_operations": 30
           }
        }
    }
'''

try:
    from pyVmomi import vim, vmodl
except ImportError:
    pass

try:
    from collections import OrderedDict
except ImportError:
    try:
        from ordereddict import OrderedDict
    except ImportError:
        pass

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi, option_diff
from ansible_collections.vmware.vmware.plugins.module_utils.argument_spec import base_argument_spec
from ansible.module_utils.common.text.converters import to_native


class VmwareVcenterSettings(PyVmomi):
    """Manage settings for a vCenter server"""

    def __init__(self, module):
        super(VmwareVcenterSettings, self).__init__(module)

        if not self.is_vcenter():
            self.module.fail_json(msg="You have to connect to a vCenter server!")

        self.option_manager = self.content.setting

    def get_default_setting_value(self, setting_key):
        return self.option_manager.QueryOptions(name=setting_key)[0].value

    def ensure(self):
        """Manage settings for a vCenter server"""
        result = dict(changed=False, msg='')
        message = ''

        db_max_connections = self.params['database'].get('max_connections')
        db_task_cleanup = self.params['database'].get('task_cleanup')
        db_task_retention = self.params['database'].get('task_retention')
        db_event_cleanup = self.params['database'].get('event_cleanup')
        db_event_retention = self.params['database'].get('event_retention')

        # runtime default value
        runtime_unique_id = self.get_default_setting_value('instance.id')
        runtime_managed_address = self.get_default_setting_value('VirtualCenter.ManagedIP')
        runtime_server_name = self.get_default_setting_value('VirtualCenter.InstanceName')

        if self.params['runtime_settings']:
            if self.params['runtime_settings'].get('unique_id') is not None:
                runtime_unique_id = self.params['runtime_settings'].get('unique_id')
            if self.params['runtime_settings'].get('managed_address') is not None:
                runtime_managed_address = self.params['runtime_settings'].get('managed_address')
            if self.params['runtime_settings'].get('vcenter_server_name') is not None:
                runtime_server_name = self.params['runtime_settings'].get('vcenter_server_name')

        directory_timeout = self.params['user_directory'].get('timeout')
        directory_query_limit = self.params['user_directory'].get('query_limit')
        directory_query_limit_size = self.params['user_directory'].get('query_limit_size')
        directory_validation = self.params['user_directory'].get('validation')
        directory_validation_period = self.params['user_directory'].get('validation_period')
        mail = self.params.get('mail') or {'mail': {'server': '', 'sender': ''}}
        mail_server = mail.get('server', '')
        mail_sender = mail.get('sender', '')
        snmp_receiver_1_url = self.params['snmp_receivers'].get('snmp_receiver_1_url')
        snmp_receiver_1_enabled = self.params['snmp_receivers'].get('snmp_receiver_1_enabled')
        snmp_receiver_1_port = self.params['snmp_receivers'].get('snmp_receiver_1_port')
        snmp_receiver_1_community = self.params['snmp_receivers'].get('snmp_receiver_1_community')
        snmp_receiver_2_url = self.params['snmp_receivers'].get('snmp_receiver_2_url')
        snmp_receiver_2_enabled = self.params['snmp_receivers'].get('snmp_receiver_2_enabled')
        snmp_receiver_2_port = self.params['snmp_receivers'].get('snmp_receiver_2_port')
        snmp_receiver_2_community = self.params['snmp_receivers'].get('snmp_receiver_2_community')
        snmp_receiver_3_url = self.params['snmp_receivers'].get('snmp_receiver_3_url')
        snmp_receiver_3_enabled = self.params['snmp_receivers'].get('snmp_receiver_3_enabled')
        snmp_receiver_3_port = self.params['snmp_receivers'].get('snmp_receiver_3_port')
        snmp_receiver_3_community = self.params['snmp_receivers'].get('snmp_receiver_3_community')
        snmp_receiver_4_url = self.params['snmp_receivers'].get('snmp_receiver_4_url')
        snmp_receiver_4_enabled = self.params['snmp_receivers'].get('snmp_receiver_4_enabled')
        snmp_receiver_4_port = self.params['snmp_receivers'].get('snmp_receiver_4_port')
        snmp_receiver_4_community = self.params['snmp_receivers'].get('snmp_receiver_4_community')
        timeout_normal_operations = self.params['timeout_settings'].get('normal_operations')
        timeout_long_operations = self.params['timeout_settings'].get('long_operations')
        logging_options = self.params.get('logging_options')

        changed = False
        changed_list = []

        # Check all general settings, except statistics
        result['db_max_connections'] = db_max_connections
        result['db_task_cleanup'] = db_task_cleanup
        result['db_task_retention'] = db_task_retention
        result['db_event_cleanup'] = db_event_cleanup
        result['db_event_retention'] = db_event_retention
        result['runtime_unique_id'] = runtime_unique_id
        result['runtime_managed_address'] = runtime_managed_address
        result['runtime_server_name'] = runtime_server_name
        result['directory_timeout'] = directory_timeout
        result['directory_query_limit'] = directory_query_limit
        result['directory_query_limit_size'] = directory_query_limit_size
        result['directory_validation'] = directory_validation
        result['directory_validation_period'] = directory_validation_period
        result['mail_server'] = mail_server
        result['mail_sender'] = mail_sender
        result['timeout_normal_operations'] = timeout_normal_operations
        result['timeout_long_operations'] = timeout_long_operations
        result['logging_options'] = logging_options
        change_option_list = []

        # Initialize diff_config variable
        diff_config = dict(
            before={},
            after={}
        )
        for key in result.keys():
            if key != 'changed' and key != 'msg':
                diff_config['before'][key] = result[key]
                diff_config['after'][key] = result[key]
        for n in range(1, 5):
            exec("diff_config['before']['snmp_receiver_%s_url'] = snmp_receiver_%s_url" % (n, n))
            exec("diff_config['before']['snmp_receiver_%s_enabled'] = snmp_receiver_%s_enabled" % (n, n))
            exec("diff_config['before']['snmp_receiver_%s_port'] = snmp_receiver_%s_port" % (n, n))
            exec("diff_config['before']['snmp_receiver_%s_community'] = snmp_receiver_%s_community" % (n, n))
            exec("diff_config['after']['snmp_receiver_%s_url'] = snmp_receiver_%s_url" % (n, n))
            exec("diff_config['after']['snmp_receiver_%s_enabled'] = snmp_receiver_%s_enabled" % (n, n))
            exec("diff_config['after']['snmp_receiver_%s_port'] = snmp_receiver_%s_port" % (n, n))
            exec("diff_config['after']['snmp_receiver_%s_community'] = snmp_receiver_%s_community" % (n, n))
        result['diff'] = {}

        advanced_settings = self.params['advanced_settings']
        changed_advanced_settings = option_diff(advanced_settings, self.option_manager.setting, False)

        if changed_advanced_settings:
            changed = True
            change_option_list += changed_advanced_settings

        for advanced_setting in advanced_settings:
            result[advanced_setting] = advanced_settings[advanced_setting]
            diff_config['before'][advanced_setting] = result[advanced_setting]
            diff_config['after'][advanced_setting] = result[advanced_setting]

        for setting in self.option_manager.setting:
            # Database
            if setting.key == 'VirtualCenter.MaxDBConnection' and setting.value != db_max_connections:
                changed = True
                changed_list.append("DB max connections")
                result['db_max_connections_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='VirtualCenter.MaxDBConnection', value=db_max_connections)
                )
                diff_config['before']['db_max_connections'] = setting.value
            if setting.key == 'task.maxAgeEnabled' and setting.value != db_task_cleanup:
                changed = True
                changed_list.append("DB task cleanup")
                result['db_task_cleanup_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='task.maxAgeEnabled', value=db_task_cleanup)
                )
                diff_config['before']['db_task_cleanup'] = setting.value
            if setting.key == 'task.maxAge' and setting.value != db_task_retention:
                changed = True
                changed_list.append("DB task retention")
                result['db_task_retention_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='task.maxAge', value=db_task_retention)
                )
                diff_config['before']['db_task_retention'] = setting.value
            if setting.key == 'event.maxAgeEnabled' and setting.value != db_event_cleanup:
                changed = True
                changed_list.append("DB event cleanup")
                result['db_event_cleanup_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='event.maxAgeEnabled', value=db_event_cleanup)
                )
                diff_config['before']['db_event_cleanup'] = setting.value
            if setting.key == 'event.maxAge' and setting.value != db_event_retention:
                changed = True
                changed_list.append("DB event retention")
                result['db_event_retention_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='event.maxAge', value=db_event_retention)
                )
                diff_config['before']['db_event_retention'] = setting.value
            # Runtime settings
            if setting.key == 'instance.id' and setting.value != runtime_unique_id:
                changed = True
                changed_list.append("Instance ID")
                result['runtime_unique_id_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='instance.id', value=runtime_unique_id)
                )
                diff_config['before']['runtime_unique_id'] = setting.value
            if setting.key == 'VirtualCenter.ManagedIP' and setting.value != runtime_managed_address:
                changed = True
                changed_list.append("Managed IP")
                result['runtime_managed_address_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='VirtualCenter.ManagedIP', value=runtime_managed_address)
                )
                diff_config['before']['runtime_managed_address'] = setting.value
            if setting.key == 'VirtualCenter.InstanceName' and setting.value != runtime_server_name:
                changed = True
                changed_list.append("Server name")
                result['runtime_server_name_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='VirtualCenter.InstanceName', value=runtime_server_name)
                )
                diff_config['before']['runtime_server_name'] = setting.value
            # User directory
            if setting.key == 'ads.timeout' and setting.value != directory_timeout:
                changed = True
                changed_list.append("Directory timeout")
                result['directory_timeout_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='ads.timeout', value=directory_timeout)
                )
                diff_config['before']['directory_timeout'] = setting.value
            if setting.key == 'ads.maxFetchEnabled' and setting.value != directory_query_limit:
                changed = True
                changed_list.append("Query limit")
                result['directory_query_limit_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='ads.maxFetchEnabled', value=directory_query_limit)
                )
                diff_config['before']['directory_query_limit'] = setting.value
            if setting.key == 'ads.maxFetch' and setting.value != directory_query_limit_size:
                changed = True
                changed_list.append("Query limit size")
                result['directory_query_limit_size_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='ads.maxFetch', value=directory_query_limit_size)
                )
                diff_config['before']['directory_query_limit_size'] = setting.value
            if setting.key == 'ads.checkIntervalEnabled' and setting.value != directory_validation:
                changed = True
                changed_list.append("Validation")
                result['directory_validation_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='ads.checkIntervalEnabled', value=directory_validation)
                )
                diff_config['before']['directory_validation'] = setting.value
            if setting.key == 'ads.checkInterval' and setting.value != directory_validation_period:
                changed = True
                changed_list.append("Validation period")
                result['directory_validation_period_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='ads.checkInterval', value=directory_validation_period)
                )
                diff_config['before']['directory_validation_period'] = setting.value
            # Mail
            if setting.key == 'mail.smtp.server' and setting.value != mail_server:
                changed = True
                changed_list.append("Mail server")
                result['mail_server_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='mail.smtp.server', value=mail_server)
                )
                diff_config['before']['mail_server'] = setting.value
            if setting.key == 'mail.sender' and setting.value != mail_sender:
                changed = True
                changed_list.append("Mail sender")
                result['mail_sender_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='mail.sender', value=mail_sender)
                )
                diff_config['before']['mail_sender'] = setting.value
            # SNMP receivers - SNMP receiver #1
            if setting.key == 'snmp.receiver.1.enabled' and setting.value != snmp_receiver_1_enabled:
                changed = True
                changed_list.append("SNMP-1-enabled")
                result['snmp_1_enabled_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.1.enabled', value=snmp_receiver_1_enabled)
                )
                diff_config['before']['snmp_receiver_1_enabled'] = setting.value
            if setting.key == 'snmp.receiver.1.name' and setting.value != snmp_receiver_1_url:
                changed = True
                changed_list.append("SNMP-1-name")
                result['snmp_1_url_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.1.name', value=snmp_receiver_1_url)
                )
                diff_config['before']['snmp_receiver_1_url'] = setting.value
            if setting.key == 'snmp.receiver.1.port' and setting.value != snmp_receiver_1_port:
                changed = True
                changed_list.append("SNMP-1-port")
                result['snmp_receiver_1_port_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.1.port', value=snmp_receiver_1_port)
                )
                diff_config['before']['snmp_receiver_1_port'] = setting.value
            if setting.key == 'snmp.receiver.1.community' and setting.value != snmp_receiver_1_community:
                changed = True
                changed_list.append("SNMP-1-community")
                result['snmp_1_community_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.1.community', value=snmp_receiver_1_community)
                )
                diff_config['before']['snmp_receiver_1_community'] = setting.value
            # SNMP receivers - SNMP receiver #2
            if setting.key == 'snmp.receiver.2.enabled' and setting.value != snmp_receiver_2_enabled:
                changed = True
                changed_list.append("SNMP-2-enabled")
                result['snmp_2_enabled_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.2.enabled', value=snmp_receiver_2_enabled)
                )
                diff_config['before']['snmp_receiver_2_enabled'] = setting.value
            if setting.key == 'snmp.receiver.2.name' and setting.value != snmp_receiver_2_url:
                changed = True
                changed_list.append("SNMP-2-name")
                result['snmp_2_url_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.2.name', value=snmp_receiver_2_url)
                )
                diff_config['before']['snmp_receiver_2_url'] = setting.value
            if setting.key == 'snmp.receiver.2.port' and setting.value != snmp_receiver_2_port:
                changed = True
                changed_list.append("SNMP-2-port")
                result['snmp_receiver_2_port_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.2.port', value=snmp_receiver_2_port)
                )
                diff_config['before']['snmp_receiver_2_port'] = setting.value
            if setting.key == 'snmp.receiver.2.community' and setting.value != snmp_receiver_2_community:
                changed = True
                changed_list.append("SNMP-2-community")
                result['snmp_2_community_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.2.community', value=snmp_receiver_2_community)
                )
                diff_config['before']['snmp_receiver_2_community'] = setting.value
            # SNMP receivers - SNMP receiver #3
            if setting.key == 'snmp.receiver.3.enabled' and setting.value != snmp_receiver_3_enabled:
                changed = True
                changed_list.append("SNMP-3-enabled")
                result['snmp_3_enabled_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.3.enabled', value=snmp_receiver_3_enabled)
                )
                diff_config['before']['snmp_receiver_3_enabled'] = setting.value
            if setting.key == 'snmp.receiver.3.name' and setting.value != snmp_receiver_3_url:
                changed = True
                changed_list.append("SNMP-3-name")
                result['snmp_3_url_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.3.name', value=snmp_receiver_3_url)
                )
                diff_config['before']['snmp_receiver_3_url'] = setting.value
            if setting.key == 'snmp.receiver.3.port' and setting.value != snmp_receiver_3_port:
                changed = True
                changed_list.append("SNMP-3-port")
                result['snmp_receiver_3_port_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.3.port', value=snmp_receiver_3_port)
                )
                diff_config['before']['snmp_receiver_3_port'] = setting.value
            if setting.key == 'snmp.receiver.3.community' and setting.value != snmp_receiver_3_community:
                changed = True
                changed_list.append("SNMP-3-community")
                result['snmp_3_community_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.3.community', value=snmp_receiver_3_community)
                )
                diff_config['before']['snmp_receiver_3_community'] = setting.value
            # SNMP receivers - SNMP receiver #4
            if setting.key == 'snmp.receiver.4.enabled' and setting.value != snmp_receiver_4_enabled:
                changed = True
                changed_list.append("SNMP-4-enabled")
                result['snmp_4_enabled_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.4.enabled', value=snmp_receiver_4_enabled)
                )
                diff_config['before']['snmp_receiver_4_enabled'] = setting.value
            if setting.key == 'snmp.receiver.4.name' and setting.value != snmp_receiver_4_url:
                changed = True
                changed_list.append("SNMP-4-name")
                result['snmp_4_url_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.4.name', value=snmp_receiver_4_url)
                )
                diff_config['before']['snmp_receiver_4_url'] = setting.value
            if setting.key == 'snmp.receiver.4.port' and setting.value != snmp_receiver_4_port:
                changed = True
                changed_list.append("SNMP-4-port")
                result['snmp_receiver_4_port_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.4.port', value=snmp_receiver_4_port)
                )
                diff_config['before']['snmp_receiver_4_port'] = setting.value
            if setting.key == 'snmp.receiver.4.community' and setting.value != snmp_receiver_4_community:
                changed = True
                changed_list.append("SNMP-4-community")
                result['snmp_4_community_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='snmp.receiver.4.community', value=snmp_receiver_4_community)
                )
                diff_config['before']['snmp_receiver_4_community'] = setting.value
            # Timeout settings
            if setting.key == 'client.timeout.normal' and setting.value != timeout_normal_operations:
                changed = True
                changed_list.append("Timeout normal")
                result['timeout_normal_operations_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='client.timeout.normal', value=timeout_normal_operations)
                )
                diff_config['before']['timeout_normal_operations'] = setting.value
            if setting.key == 'client.timeout.long' and setting.value != timeout_long_operations:
                changed = True
                changed_list.append("Timout long")
                result['timeout_long_operations_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='client.timeout.long', value=timeout_long_operations)
                )
                diff_config['before']['timeout_long_operations'] = setting.value
            # Logging settings
            if setting.key == 'log.level' and setting.value != logging_options:
                changed = True
                changed_list.append("Logging")
                result['logging_options_previous'] = setting.value
                change_option_list.append(
                    vim.option.OptionValue(key='log.level', value=logging_options)
                )
                diff_config['before']['logging_options'] = setting.value

            # Advanced settings
            for advanced_setting in changed_advanced_settings:
                if setting.key == advanced_setting.key and setting.value != advanced_setting.value:
                    changed_list.append(advanced_setting.key)
                    result[advanced_setting.key + '_previous'] = advanced_setting.value
                    diff_config['before'][advanced_setting.key] = advanced_setting.value

        for advanced_setting in changed_advanced_settings:
            if advanced_setting.key not in changed_list:
                changed_list.append(advanced_setting.key)
                result[advanced_setting.key + '_previous'] = "N/A"
                diff_config['before'][advanced_setting.key] = "N/A"

        if changed:
            if self.module.check_mode:
                changed_suffix = ' would be changed'
            else:
                changed_suffix = ' changed'
            if len(changed_list) > 2:
                message = ', '.join(changed_list[:-1]) + ', and ' + str(changed_list[-1])
            elif len(changed_list) == 2:
                message = ' and '.join(changed_list)
            elif len(changed_list) == 1:
                message = changed_list[0]
            message += changed_suffix
            if not self.module.check_mode:
                try:
                    self.option_manager.UpdateOptions(changedValue=change_option_list)
                except (vmodl.fault.SystemError, vmodl.fault.InvalidArgument) as invalid_argument:
                    self.module.fail_json(
                        msg="Failed to update option(s) as one or more OptionValue contains an invalid value: %s" %
                        to_native(invalid_argument.msg)
                    )
                except vim.fault.InvalidName as invalid_name:
                    self.module.fail_json(
                        msg="Failed to update option(s) as one or more OptionValue objects refers to a "
                        "non-existent option : %s" % to_native(invalid_name.msg)
                    )
        else:
            message = "vCenter settings already configured properly"
        result['changed'] = changed
        result['msg'] = message

        result['diff']['before'] = OrderedDict(sorted(diff_config['before'].items()))
        result['diff']['after'] = OrderedDict(sorted(diff_config['after'].items()))

        self.module.exit_json(**result)


def main():
    """Main"""
    argument_spec = base_argument_spec()
    argument_spec.update(
        database=dict(
            type='dict',
            options=dict(
                max_connections=dict(type='int', default=50),
                task_cleanup=dict(type='bool', default=True),
                task_retention=dict(type='int', default=30),
                event_cleanup=dict(type='bool', default=True),
                event_retention=dict(type='int', default=30),
            ),
            default=dict(
                max_connections=50,
                task_cleanup=True,
                task_retention=30,
                event_cleanup=True,
                event_retention=30,
            ),
        ),
        runtime_settings=dict(
            type='dict',
            options=dict(
                unique_id=dict(type='int'),
                managed_address=dict(type='str'),
                vcenter_server_name=dict(type='str'),
            ),
        ),
        user_directory=dict(
            type='dict',
            options=dict(
                timeout=dict(type='int', default=60),
                query_limit=dict(type='bool', default=True),
                query_limit_size=dict(type='int', default=5000),
                validation=dict(type='bool', default=True),
                validation_period=dict(type='int', default=1440),
            ),
            default=dict(
                timeout=60,
                query_limit=True,
                query_limit_size=5000,
                validation=True,
                validation_period=1440,
            ),
        ),
        mail=dict(
            type='dict',
            options=dict(
                server=dict(type='str'),
                sender=dict(type='str'),
            ),
            default=dict(
                server='',
                sender='',
            ),
        ),
        snmp_receivers=dict(
            type='dict',
            options=dict(
                snmp_receiver_1_url=dict(type='str', default='localhost'),
                snmp_receiver_1_enabled=dict(type='bool', default=True),
                snmp_receiver_1_port=dict(type='int', default=162),
                snmp_receiver_1_community=dict(type='str', default='public'),
                snmp_receiver_2_url=dict(type='str', default=''),
                snmp_receiver_2_enabled=dict(type='bool', default=False),
                snmp_receiver_2_port=dict(type='int', default=162),
                snmp_receiver_2_community=dict(type='str', default=''),
                snmp_receiver_3_url=dict(type='str', default=''),
                snmp_receiver_3_enabled=dict(type='bool', default=False),
                snmp_receiver_3_port=dict(type='int', default=162),
                snmp_receiver_3_community=dict(type='str', default=''),
                snmp_receiver_4_url=dict(type='str', default=''),
                snmp_receiver_4_enabled=dict(type='bool', default=False),
                snmp_receiver_4_port=dict(type='int', default=162),
                snmp_receiver_4_community=dict(type='str', default=''),
            ),
            default=dict(
                snmp_receiver_1_url='localhost',
                snmp_receiver_1_enabled=True,
                snmp_receiver_1_port=162,
                snmp_receiver_1_community='public',
                snmp_receiver_2_url='',
                snmp_receiver_2_enabled=False,
                snmp_receiver_2_port=162,
                snmp_receiver_2_community='',
                snmp_receiver_3_url='',
                snmp_receiver_3_enabled=False,
                snmp_receiver_3_port=162,
                snmp_receiver_3_community='',
                snmp_receiver_4_url='',
                snmp_receiver_4_enabled=False,
                snmp_receiver_4_port=162,
                snmp_receiver_4_community='',
            ),
        ),
        timeout_settings=dict(
            type='dict',
            options=dict(
                normal_operations=dict(type='int', default=30),
                long_operations=dict(type='int', default=120),
            ),
            default=dict(
                normal_operations=30,
                long_operations=120,
            ),
        ),
        logging_options=dict(default='info', choices=['none', 'error', 'warning', 'info', 'verbose', 'trivia']),
        advanced_settings=dict(type='dict', default=dict(), required=False),
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    host_snmp = VmwareVcenterSettings(module)
    host_snmp.ensure()


if __name__ == '__main__':
    main()
