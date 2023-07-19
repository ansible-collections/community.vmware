# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Ansible Project
# Copyright: (c) 2023, Pure Storage, Inc.

from __future__ import absolute_import, division, print_function
__metaclass__ = type

try:
    from pyVmomi import sms
    from pyVim.connect import SoapStubAdapter
except ImportError:
    pass

from ansible_collections.community.vmware.plugins.module_utils.vmware import PyVmomi
from random import randint
import time


class TaskError(Exception):
    def __init__(self, *args, **kwargs):
        super(TaskError, self).__init__(*args, **kwargs)


class SMS(PyVmomi):
    def __init__(self, module):
        super(SMS, self).__init__(module)
        self.sms_si = None
        self.version = "sms.version.v7_0_0_1"

    def get_sms_connection(self):
        """
        Creates a Service instance for VMware SMS
        """
        client_stub = self.si._GetStub()
        try:
            session_cookie = client_stub.cookie.split('"')[1]
        except IndexError:
            self.module.fail_json(msg="Failed to get session cookie")
        ssl_context = client_stub.schemeArgs.get('context')
        additional_headers = {'vcSessionCookie': session_cookie}
        hostname = self.module.params['hostname']
        if not hostname:
            self.module.fail_json(msg="Please specify required parameter - hostname")
        stub = SoapStubAdapter(host=hostname, path="/sms/sdk", version=self.version,
                               sslContext=ssl_context, requestContext=additional_headers)

        self.sms_si = sms.ServiceInstance("ServiceInstance", stub)


def wait_for_sms_task(task, max_backoff=64, timeout=3600):
    """Wait for given task using exponential back-off algorithm.

    Args:
        task: VMware SMS task object
        max_backoff: Maximum amount of sleep time in seconds
        timeout: Timeout for the given task in seconds

    Returns: Tuple with True and result for successful task
    Raises: TaskError on failure
    """
    failure_counter = 0
    start_time = time.time()

    while True:
        task_info = task.QuerySmsTaskInfo()
        if time.time() - start_time >= timeout:
            raise TaskError("Timeout")
        if task_info.state == sms.TaskInfo.State.success:
            return True, task_info.result
        if task_info.state == sms.TaskInfo.State.error:
            return False, task_info.error
        if task_info.state in [sms.TaskInfo.State.running, sms.TaskInfo.State.queued]:
            sleep_time = min(2 ** failure_counter + randint(1, 1000) / 1000, max_backoff)
            time.sleep(sleep_time)
            failure_counter += 1
