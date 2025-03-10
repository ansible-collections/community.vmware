# -*- coding: utf-8 -*-

# Copyright: (c) 2015, Joseph Callen <jcallen () csc.com>
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, James E. King III (@jeking3) <jking@apache.org>
# Copyright: (c) 2025, Mario Lenz (@mariolenz) <m@riolenz.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

__metaclass__ = type

import atexit
import ssl
import traceback

from ansible.module_utils.basic import missing_required_lib

REQUESTS_IMP_ERR = None
try:
    # requests is required for exception handling of the ConnectionError
    import requests
except ImportError:
    REQUESTS_IMP_ERR = traceback.format_exc()

PYVMOMI_IMP_ERR = None
try:
    from pyVim import connect
    from pyVmomi import vim, vmodl
except ImportError:
    PYVMOMI_IMP_ERR = traceback.format_exc()


class MissingLibError(Exception):
    def __init__(self, library, exception, url=None):
        self.exception = exception
        self.library = library
        self.url = url
        super().__init__(missing_required_lib(self.library, url=self.url))


class ApiAccessError(Exception):
    def __init__(self, *args, **kwargs):
        super(ApiAccessError, self).__init__(*args, **kwargs)


class PyvmomiClient(object):
    def __init__(self, hostname, username, password, port=443, validate_certs=True, http_proxy_host=None, http_proxy_port=None):
        if REQUESTS_IMP_ERR:
            raise MissingLibError('requests', REQUESTS_IMP_ERR)

        if PYVMOMI_IMP_ERR:
            raise MissingLibError('pyvmomi', PYVMOMI_IMP_ERR)

        self.si, self.content = self._connect_to_api(hostname, username, password, port, validate_certs, http_proxy_host, http_proxy_port)

    def _connect_to_api(self, hostname, username, password, port, validate_certs, http_proxy_host, http_proxy_port):
        if not hostname:
            raise ApiAccessError("Hostname parameter is missing.")

        if not username:
            raise ApiAccessError("Username parameter is missing.")

        if not password:
            raise ApiAccessError("Password parameter is missing.")

        if validate_certs and not hasattr(ssl, 'SSLContext'):
            raise ApiAccessError('pyVim does not support changing verification mode with python < 2.7.9. Either update '
                                 'python or use validate_certs=false.')
        elif validate_certs:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            ssl_context.verify_mode = ssl.CERT_REQUIRED
            ssl_context.check_hostname = True
            ssl_context.load_default_certs()
        elif hasattr(ssl, 'SSLContext'):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            ssl_context.verify_mode = ssl.CERT_NONE
            ssl_context.check_hostname = False

        service_instance = None

        connect_args = dict(
            host=hostname,
            port=port,
        )
        if ssl_context:
            connect_args.update(sslContext=ssl_context)

        msg_suffix = ''
        try:
            if http_proxy_host:
                msg_suffix = " [proxy: %s:%d]" % (http_proxy_host, http_proxy_port)
                connect_args.update(httpProxyHost=http_proxy_host, httpProxyPort=http_proxy_port)
                smart_stub = connect.SmartStubAdapter(**connect_args)
                session_stub = connect.VimSessionOrientedStub(smart_stub, connect.VimSessionOrientedStub.makeUserLoginMethod(username, password))
                service_instance = vim.ServiceInstance('ServiceInstance', session_stub)
            else:
                connect_args.update(user=username, pwd=password)
                service_instance = connect.SmartConnect(**connect_args)
        except vim.fault.InvalidLogin as invalid_login:
            msg = "Unable to log on to vCenter or ESXi API at %s:%s " % (hostname, port)
            raise ApiAccessError("%s as %s: %s" % (msg, username, invalid_login.msg) + msg_suffix)
        except vim.fault.NoPermission as no_permission:
            raise ApiAccessError("User %s does not have required permission"
                                 " to log on to vCenter or ESXi API at %s:%s : %s" % (username, hostname, port, no_permission.msg))
        except (requests.ConnectionError, ssl.SSLError) as generic_req_exc:
            raise ApiAccessError("Unable to connect to vCenter or ESXi API at %s on TCP/%s: %s" % (hostname, port, generic_req_exc))
        except vmodl.fault.InvalidRequest as invalid_request:
            # Request is malformed
            msg = "Failed to get a response from server %s:%s " % (hostname, port)
            raise ApiAccessError("%s as request is malformed: %s" % (msg, invalid_request.msg) + msg_suffix)
        except Exception as generic_exc:
            msg = "Unknown error while connecting to vCenter or ESXi API at %s:%s" % (hostname, port) + msg_suffix
            raise ApiAccessError("%s : %s" % (msg, generic_exc))

        if service_instance is None:
            msg = "Unknown error while connecting to vCenter or ESXi API at %s:%s" % (hostname, port)
            raise ApiAccessError(msg + msg_suffix)

        atexit.register(connect.Disconnect, service_instance)

        return service_instance, service_instance.RetrieveContent()
