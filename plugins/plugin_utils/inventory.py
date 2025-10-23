# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2020, dacrystal
# Copyright: (c) 2021, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later


from __future__ import absolute_import, division, print_function

__metaclass__ = type

import ssl
import atexit
import base64

try:
    # requests is required for exception handling of the ConnectionError
    import requests

    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

try:
    from pyVim import connect
    from pyVmomi import vim, vmodl
    from pyVmomi.VmomiSupport import DataObject
    from pyVmomi import Iso8601

    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False

try:
    from vmware.vapi.vsphere.client import create_vsphere_client

    HAS_VSPHERE = True
except ImportError:
    HAS_VSPHERE = False

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.common.dict_transformations import _snake_to_camel
from ansible.module_utils.common.text.converters import to_text, to_native


class BaseVMwareInventory:
    def __init__(
        self, hostname, username, password, port, validate_certs, with_tags, display
    ):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.with_tags = with_tags
        self.validate_certs = validate_certs
        self.content = None
        self.rest_content = None
        self.display = display

    def do_login(self):
        """
        Check requirements and do login
        """
        self.check_requirements()
        self.si, self.content = self._login()
        if self.with_tags:
            self.rest_content = self._login_vapi()

    def _login_vapi(self):
        """
        Login to vCenter API using REST call
        Returns: connection object

        """
        session = requests.Session()
        session.verify = self.validate_certs
        if not self.validate_certs:
            # Disable warning shown at stdout
            requests.packages.urllib3.disable_warnings()

        server = self.hostname
        if self.port:
            server += ":" + str(self.port)

        client, err = None, None
        try:
            client = create_vsphere_client(
                server=server,
                username=self.username,
                password=self.password,
                session=session,
            )
        except Exception as error:
            err = error

        if client is None:
            msg = "Failed to login to %s using %s" % (server, self.username)
            if err:
                msg += " due to : %s" % to_native(err)
            raise AnsibleError(msg)
        return client

    def _login(self):
        """
        Login to vCenter or ESXi server
        Returns: connection object

        """
        if self.validate_certs and not hasattr(ssl, "SSLContext"):
            raise AnsibleError(
                "pyVim does not support changing verification mode with python < 2.7.9. Either update "
                "python or set validate_certs to false in configuration YAML file."
            )

        ssl_context = None
        if not self.validate_certs and hasattr(ssl, "SSLContext"):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
            ssl_context.verify_mode = ssl.CERT_NONE

        service_instance = None
        try:
            service_instance = connect.SmartConnect(
                host=self.hostname,
                user=self.username,
                pwd=self.password,
                sslContext=ssl_context,
                port=self.port,
            )

        except vim.fault.InvalidLogin as e:
            raise AnsibleParserError(
                "Unable to log on to vCenter or ESXi API at %s:%s as %s: %s"
                % (self.hostname, self.port, self.username, e.msg)
            )
        except vim.fault.NoPermission as e:
            raise AnsibleParserError(
                "User %s does not have required permission"
                " to log on to vCenter or ESXi API at %s:%s : %s"
                % (self.username, self.hostname, self.port, e.msg)
            )
        except (requests.ConnectionError, ssl.SSLError) as e:
            raise AnsibleParserError(
                "Unable to connect to vCenter or ESXi API at %s on TCP/%s: %s"
                % (self.hostname, self.port, e)
            )
        except vmodl.fault.InvalidRequest as e:
            # Request is malformed
            raise AnsibleParserError(
                "Failed to get a response from server %s:%s as "
                "request is malformed: %s" % (self.hostname, self.port, e.msg)
            )
        except Exception as e:
            raise AnsibleParserError(
                "Unknown error while connecting to vCenter or ESXi API at %s:%s : %s"
                % (self.hostname, self.port, e)
            )

        if service_instance is None:
            raise AnsibleParserError(
                "Unknown error while connecting to vCenter or ESXi API at %s:%s"
                % (self.hostname, self.port)
            )

        atexit.register(connect.Disconnect, service_instance)
        return service_instance, service_instance.RetrieveContent()

    def check_requirements(self):
        """ Check all requirements for this inventory are satisfied"""
        if not HAS_REQUESTS:
            raise AnsibleParserError(
                'Please install "requests" Python module as this is required'
                " for VMware Guest dynamic inventory plugin."
            )
        if not HAS_PYVMOMI:
            raise AnsibleParserError(
                'Please install "PyVmomi" Python module as this is required'
                " for VMware Guest dynamic inventory plugin."
            )
        if HAS_REQUESTS:
            # Pyvmomi 5.5 and onwards requires requests 2.3
            # https://github.com/vmware/pyvmomi/blob/master/requirements.txt
            required_version = (2, 3)
            requests_version = requests.__version__.split(".")[:2]
            try:
                requests_major_minor = tuple(map(int, requests_version))
            except ValueError:
                raise AnsibleParserError("Failed to parse 'requests' library version.")

            if requests_major_minor < required_version:
                raise AnsibleParserError(
                    "'requests' library version should"
                    " be >= %s, found: %s."
                    % (
                        ".".join([str(w) for w in required_version]),
                        requests.__version__,
                    )
                )

        if not HAS_VSPHERE and self.with_tags:
            raise AnsibleError(
                "Unable to find 'vSphere Automation SDK' Python library which is required."
                " Please refer this URL for installation steps"
                " - https://code.vmware.com/web/sdk/7.0/vsphere-automation-python"
            )

        if not all([self.hostname, self.username, self.password]):
            raise AnsibleError(
                "Missing one of the following : hostname, username, password. Please read "
                "the documentation for more information."
            )

    def get_managed_objects_properties(
        self, vim_type, properties=None, resources=None, strict=False
    ):
        """
        Look up a Managed Object Reference in vCenter / ESXi Environment
        :param vim_type: Type of vim object e.g, for datacenter - vim.Datacenter
        :param properties: List of properties related to vim object e.g. Name
        :param resources: List of resources to limit search scope
        :param strict: Dictates if plugin raises error or just warns
        :return: local content object
        """
        traversal_spec = vmodl.query.PropertyCollector.TraversalSpec
        filter_spec = vmodl.query.PropertyCollector.FilterSpec
        object_spec = vmodl.query.PropertyCollector.ObjectSpec
        property_spec = vmodl.query.PropertyCollector.PropertySpec

        resource_filters = resources or []
        type_to_name_map = {}

        def _handle_error(message):
            if strict:
                raise AnsibleError(message)
            self.display.warning(message)

        def get_contents(container, vim_types):
            return self.content.propertyCollector.RetrieveContents(
                [
                    filter_spec(
                        objectSet=[
                            object_spec(
                                obj=self.content.viewManager.CreateContainerView(
                                    container, vim_types, True
                                ),
                                skip=False,
                                selectSet=[
                                    traversal_spec(
                                        type=vim.view.ContainerView,
                                        path="view",
                                        skip=False,
                                    )
                                ],
                            )
                        ],
                        propSet=[
                            property_spec(type=t, all=False, pathSet=["name"])
                            for t in vim_types
                        ],
                    )
                ]
            )

        def filter_containers(containers, typ, filter_list):
            if len(filter_list) > 0:
                objs = []
                results = []
                found_filters = {}

                for container in containers:
                    results.extend(get_contents(container, [typ]))

                for res in results:
                    if res.propSet[0].val in filter_list:
                        objs.append(res.obj)
                        found_filters[res.propSet[0].val] = True

                for fil in filter_list:
                    if fil not in found_filters:
                        _handle_error(
                            "Unable to find %s %s" % (type_to_name_map[typ], fil)
                        )

                return objs
            return containers

        def build_containers(containers, vim_type, names, filters):
            filters = filters or []
            if vim_type:
                containers = filter_containers(containers, vim_type, names)

            new_containers = []
            for fil in filters:
                new_filters = None
                for k, v in fil.items():
                    if k == "resources":
                        new_filters = v
                    else:
                        vim_type = getattr(vim, _snake_to_camel(k, True))
                        names = v
                        type_to_name_map[vim_type] = k.replace("_", " ")

                new_containers.extend(
                    build_containers(containers, vim_type, names, new_filters)
                )

            if len(filters) > 0:
                return new_containers
            return containers

        containers = build_containers(
            [self.content.rootFolder], None, None, resource_filters
        )
        if len(containers) == 0:
            return []

        objs_list = [
            object_spec(
                obj=self.content.viewManager.CreateContainerView(r, [vim_type], True),
                selectSet=[
                    traversal_spec(path="view", skip=False, type=vim.view.ContainerView)
                ],
            )
            for r in containers
        ]

        is_all = not properties

        # Create Property Spec
        property_spec = property_spec(
            type=vim_type, all=is_all, pathSet=properties  # Type of object to retrieved
        )

        # Create Filter Spec
        filter_spec = filter_spec(
            objectSet=objs_list,
            propSet=[property_spec],
            reportMissingObjectsInResults=False,
        )

        try:
            return self.content.propertyCollector.RetrieveContents([filter_spec])
        except vmodl.query.InvalidProperty as err:
            _handle_error("Invalid property name: %s" % err.name)
        except Exception as err:  # pylint: disable=broad-except
            _handle_error("Couldn't retrieve contents from host: %s" % to_native(err))
        return []


def in_place_merge(a, b):
    """
    Recursively merges second dict into the first.

    """
    if not isinstance(b, dict):
        return b
    for k, v in b.items():
        if k in a and isinstance(a[k], dict):
            a[k] = in_place_merge(a[k], v)
        else:
            a[k] = v
    return a


def to_nested_dict(vm_properties):
    """
    Parse properties from dot notation to dict

    """

    host_properties = {}

    for vm_prop_name, vm_prop_val in vm_properties.items():
        prop_parents = reversed(vm_prop_name.split("."))
        prop_dict = parse_vim_property(vm_prop_val)

        for k in prop_parents:
            prop_dict = {k: prop_dict}
        host_properties = in_place_merge(host_properties, prop_dict)

    return host_properties


def to_flatten_dict(d, parent_key="", sep="."):
    """
    Parse properties dict to dot notation

    """
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if v and isinstance(v, dict):
            items.extend(to_flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def parse_vim_property(vim_prop):
    """
    Helper method to parse VIM properties of virtual machine
    """
    prop_type = type(vim_prop).__name__
    if prop_type.startswith(("vim", "vmodl", "Link")):
        if isinstance(vim_prop, DataObject):
            r = {}
            for prop in vim_prop._GetPropertyList():  # pylint: disable=protected-access
                if prop.name not in [
                    "dynamicProperty",
                    "dynamicType",
                    "managedObjectType",
                ]:
                    sub_prop = getattr(vim_prop, prop.name)
                    r[prop.name] = parse_vim_property(sub_prop)
            return r

        if isinstance(vim_prop, list):
            r = []
            for prop in vim_prop:
                r.append(parse_vim_property(prop))
            return r
        return vim_prop.__str__()

    elif prop_type == "datetime":
        return Iso8601.ISO8601Format(vim_prop)

    elif prop_type == "long":
        return int(vim_prop)
    elif prop_type == "long[]":
        return [int(x) for x in vim_prop]

    elif isinstance(vim_prop, list):
        return [parse_vim_property(x) for x in vim_prop]

    elif prop_type in ["bool", "int", "NoneType", "dict"]:
        return vim_prop

    elif prop_type in ["binary"]:
        return to_text(base64.b64encode(vim_prop))

    return to_text(vim_prop)
