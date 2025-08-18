# Copyright: (c) 2018, Deric Crago <deric.crago@gmail.com>
# Copyright: (c) 2018, Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
    author:
    - Deric Crago (@dericcrago) <deric.crago@gmail.com>
    name: vmware_tools
    short_description: Execute tasks inside a VM via VMware Tools
    description:
      - Use VMware tools to run tasks in, or put/fetch files to guest operating systems running in VMware infrastructure.
      - In case of Windows VMs, set C(ansible_shell_type) to C(powershell).
      - Does not work with C(become).
    requirements:
      - requests (Python library)
    options:
      vmware_host:
        description:
          - FQDN or IP Address for the connection (vCenter or ESXi Host).
        env:
          - name: VI_SERVER
          - name: VMWARE_HOST
        vars:
          - name: ansible_host
          - name: ansible_vmware_host
        required: true
      vmware_user:
        description:
          - Username for the connection.
          - "Requires the following permissions on the VM:
               - VirtualMachine.GuestOperations.Execute
               - VirtualMachine.GuestOperations.Modify
               - VirtualMachine.GuestOperations.Query"
        env:
          - name: VI_USERNAME
          - name: VMWARE_USER
        vars:
          - name: ansible_vmware_user
        required: true
      vmware_password:
        description:
          - Password for the connection.
        env:
          - name: VI_PASSWORD
          - name: VMWARE_PASSWORD
        vars:
          - name: ansible_vmware_password
        required: true
      vmware_port:
        description:
          - Port for the connection.
        env:
          - name: VI_PORTNUMBER
          - name: VMWARE_PORT
        vars:
          - name: ansible_port
          - name: ansible_vmware_port
        required: false
        default: 443
      validate_certs:
        description:
          - Verify SSL for the connection.
          - "Note: This will validate certs for both O(vmware_host) and the ESXi host running the VM."
        env:
          - name: VMWARE_VALIDATE_CERTS
        vars:
          - name: ansible_vmware_validate_certs
        default: true
        type: bool
      vm_path:
        description:
          - Mutually exclusive with O(vm_uuid)
          - VM path absolute to the connection.
          - "vCenter Example: V(Datacenter/vm/Discovered virtual machine/testVM)."
          - "ESXi Host Example: V(ha-datacenter/vm/testVM)."
          - Must include VM name, appended to 'folder' as would be passed to M(community.vmware.vmware_guest).
          - Needs to include I(vm) between the Datacenter and the rest of the VM path.
          - Datacenter default value for ESXi server is C(ha-datacenter).
          - Folder I(vm) is not visible in the vSphere Web Client but necessary for VMware API to work.
        vars:
          - name: ansible_vmware_guest_path
        required: false
      vm_uuid:
        description:
          - UUID of the virtual machine
          - Mutually exclusive with O(vm_path)
        vars:
          - name: ansible_vmware_guest_uuid
        required: false
      vm_user:
        description:
          - VM username.
          - C(ansible_vmware_tools_user) is used for connecting to the VM.
          - C(ansible_user) is used by Ansible on the VM.
        vars:
          - name: ansible_user
          - name: ansible_vmware_tools_user
        required: true
      vm_password:
        description:
          - Password for the user in guest operating system.
        vars:
          - name: ansible_password
          - name: ansible_vmware_tools_password
        required: true
      exec_command_sleep_interval:
        description:
          - Time in seconds to sleep between execution of command.
        vars:
          - name: ansible_vmware_tools_exec_command_sleep_interval
        default: 0.5
        type: float
      file_chunk_size:
        description:
          - File chunk size.
          - "(Applicable when writing a file to disk, example: using the M(ansible.builtin.fetch) module.)"
        vars:
          - name: ansible_vmware_tools_file_chunk_size
        default: 128
        type: integer
      executable:
        description:
            - shell to use for execution inside container
        default: /bin/sh
        ini:
          - section: defaults
            key: executable
        env:
          - name: ANSIBLE_EXECUTABLE
        vars:
            - name: ansible_executable
            - name: ansible_vmware_tools_executable
'''

example = r'''
# example vars.yml
---
ansible_connection: vmware_tools
ansible_user: "{{ ansible_vmware_tools_user }}"

ansible_vmware_host: vcenter.example.com
ansible_vmware_user: administrator@vsphere.local
ansible_vmware_password: Secr3tP4ssw0rd!12
ansible_vmware_validate_certs: false  # default is true

# vCenter Connection VM Path Example
ansible_vmware_guest_path: DATACENTER/vm/FOLDER/{{ inventory_hostname }}
# ESXi Connection VM Path Example
ansible_vmware_guest_path: ha-datacenter/vm/{{ inventory_hostname }}

ansible_vmware_tools_user: root
ansible_vmware_tools_password: MyR00tPassw0rD

# if the target VM guest is Windows set the 'ansible_shell_type' to 'powershell'
ansible_shell_type: powershell


# example playbook_linux.yml
---
- name: Test VMware Tools Connection Plugin for Linux
  hosts: linux
  tasks:
    - command: whoami

    - ping:

    - copy:
        src: foo
        dest: /home/user/foo

    - fetch:
        src: /home/user/foo
        dest: linux-foo
        flat: true

    - file:
        path: /home/user/foo
        state: absent


# example playbook_windows.yml
---
- name: Test VMware Tools Connection Plugin for Windows
  hosts: windows
  tasks:
    - win_command: whoami

    - win_ping:

    - win_copy:
        src: foo
        dest: C:\Users\user\foo

    - fetch:
        src: C:\Users\user\foo
        dest: windows-foo
        flat: true

    - win_file:
        path: C:\Users\user\foo
        state: absent
'''

import re
from os.path import exists, getsize
from socket import gaierror
from ssl import SSLError
from time import sleep
import traceback

REQUESTS_IMP_ERR = None
PYVMOMI_IMP_ERR = None
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    REQUESTS_IMP_ERR = traceback.format_exc()
    HAS_REQUESTS = False

try:
    from requests.packages import urllib3
    HAS_URLLIB3 = True
except ImportError:
    try:
        import urllib3
        HAS_URLLIB3 = True
    except ImportError:
        HAS_URLLIB3 = False

from ansible.errors import AnsibleError, AnsibleFileNotFound, AnsibleConnectionFailure
from ansible.module_utils._text import to_bytes, to_native
from ansible.plugins.connection import ConnectionBase
from ansible.module_utils.basic import missing_required_lib

try:
    from pyVim.connect import Disconnect, SmartConnect
    from pyVmomi import vim, vmodl

    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False
    PYVMOMI_IMP_ERR = traceback.format_exc()


class Connection(ConnectionBase):
    """VMware Tools Connection."""

    transport = 'community.vmware.vmware_tools'

    @property
    def vmware_host(self):
        """Read-only property holding the connection address."""
        return self.get_option("vmware_host")

    @property
    def validate_certs(self):
        """Read-only property holding whether the connection should validate certs."""
        return self.get_option("validate_certs")

    @property
    def authManager(self):
        """Guest Authentication Manager."""
        return self._si.content.guestOperationsManager.authManager

    @property
    def fileManager(self):
        """Guest File Manager."""
        return self._si.content.guestOperationsManager.fileManager

    @property
    def processManager(self):
        """Guest Process Manager."""
        return self._si.content.guestOperationsManager.processManager

    @property
    def windowsGuest(self):
        """Return if VM guest family is windows."""
        return self.vm.guest.guestFamily == "windowsGuest"

    def __init__(self, *args, **kwargs):
        """init."""
        super(Connection, self).__init__(*args, **kwargs)
        if hasattr(self, "_shell") and self._shell.SHELL_FAMILY == "powershell":
            self.module_implementation_preferences = (".ps1", ".exe", "")
            self.become_methods = ["runas"]
            self.allow_executable = False
            self.has_pipelining = False
            self.allow_extras = True
        self._si = None

    def _establish_connection(self):
        connection_kwargs = {
            "host": self.vmware_host,
            "user": self.get_option("vmware_user"),
            "pwd": self.get_option("vmware_password"),
            "port": self.get_option("vmware_port"),
        }

        if not self.validate_certs:
            if HAS_URLLIB3:
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            connection_kwargs['disableSslCertValidation'] = True

        try:
            self._si = SmartConnect(**connection_kwargs)
        except SSLError:
            raise AnsibleError("SSL Error: Certificate verification failed.")
        except (gaierror):
            raise AnsibleError("Connection Error: Unable to connect to '%s'." % to_native(connection_kwargs["host"]))
        except vim.fault.InvalidLogin as e:
            raise AnsibleError("Connection Login Error: %s" % to_native(e.msg))

    def _establish_vm(self, check_vm_credentials=True):
        searchIndex = self._si.content.searchIndex
        self.vm = None
        if self.get_option("vm_path") is not None:
            self.vm = searchIndex.FindByInventoryPath(self.get_option("vm_path"))
            if self.vm is None:
                raise AnsibleError("Unable to find VM by path '%s'" % to_native(self.get_option("vm_path")))
        elif self.get_option("vm_uuid") is not None:
            self.vm = searchIndex.FindByUuid(None, self.get_option("vm_uuid"), True)
            if self.vm is None:
                raise AnsibleError("Unable to find VM by uuid '%s'" % to_native(self.get_option("vm_uuid")))

        self.vm_auth = vim.NamePasswordAuthentication(
            username=self.get_option("vm_user"), password=self.get_option("vm_password"), interactiveSession=False
        )

        try:
            if check_vm_credentials:
                self.authManager.ValidateCredentialsInGuest(vm=self.vm, auth=self.vm_auth)
        except vim.fault.InvalidPowerState as e:
            raise AnsibleError("VM Power State Error: %s" % to_native(e.msg))
        except vim.fault.RestrictedVersion as e:
            raise AnsibleError("Restricted Version Error: %s" % to_native(e.msg))
        except vim.fault.GuestOperationsUnavailable as e:
            raise AnsibleError("VM Guest Operations (VMware Tools) Error: %s" % to_native(e.msg))
        except vim.fault.InvalidGuestLogin as e:
            raise AnsibleError("VM Login Error: %s" % to_native(e.msg))
        except vim.fault.NoPermission as e:
            raise AnsibleConnectionFailure("No Permission Error: %s %s" % (to_native(e.msg), to_native(e.privilegeId)))
        except vmodl.fault.SystemError as e:
            if e.reason == 'vix error codes = (3016, 0).\n':
                raise AnsibleConnectionFailure(
                    "Connection failed, is the vm currently rebooting? Reason: %s" % (
                        to_native(e.reason)
                    )
                )
            else:
                raise AnsibleConnectionFailure("Connection failed. Reason %s" % (to_native(e.reason)))
        except vim.fault.GuestOperationsUnavailable:
            raise AnsibleConnectionFailure("Cannot connect to guest. Native error: GuestOperationsUnavailable")

    def _connect(self, check_vm_credentials=True):
        if not HAS_REQUESTS:
            raise AnsibleError("%s : %s" % (missing_required_lib('requests'), REQUESTS_IMP_ERR))

        if not HAS_PYVMOMI:
            raise AnsibleError("%s : %s" % (missing_required_lib('PyVmomi'), PYVMOMI_IMP_ERR))

        super(Connection, self)._connect()

        if not self.connected:
            self._establish_connection()
            self._establish_vm(check_vm_credentials=check_vm_credentials)
            self._connected = True

    def close(self):
        """Close connection."""
        super(Connection, self).close()

        Disconnect(self._si)
        self._connected = False

    def reset(self):
        """Reset the connection to vcenter."""
        # TODO: Fix persistent connection implementation currently ansible creates new connections to vcenter for each task
        # therefore we're currently closing a non existing connection here and establish a connection just for being thrown away
        # right afterwards.
        self.close()
        self._connect(check_vm_credentials=False)

    def create_temporary_file_in_guest(self, prefix="", suffix=""):
        """Create a temporary file in the VM."""
        try:
            return self.fileManager.CreateTemporaryFileInGuest(vm=self.vm, auth=self.vm_auth, prefix=prefix, suffix=suffix)
        except vim.fault.NoPermission as e:
            raise AnsibleError("No Permission Error: %s %s" % (to_native(e.msg), to_native(e.privilegeId)))
        except vmodl.fault.SystemError as e:
            if e.reason == 'vix error codes = (3016, 0).\n':
                raise AnsibleConnectionFailure(
                    "Connection failed, is the vm currently rebooting? Reason: %s" % (
                        to_native(e.reason)
                    )
                )
            else:
                raise AnsibleConnectionFailure("Connection failed. Reason %s" % (to_native(e.reason)))
        except vim.fault.GuestOperationsUnavailable:
            raise AnsibleConnectionFailure("Cannot connect to guest. Native error: GuestOperationsUnavailable")

    def _get_program_spec_program_path_and_arguments(self, cmd):
        if self.windowsGuest:
            '''
            we need to warp the execution of powershell into a cmd /c because
            the call otherwise fails with "Authentication or permission failure"
            #FIXME: Fix the unecessary invocation of cmd and run the command directly
            '''
            program_path = "cmd.exe"
            arguments = "/c %s" % cmd
        else:
            program_path = self.get_option("executable")
            arguments = re.sub(r"^%s\s*" % program_path, "", cmd)

        return program_path, arguments

    def _get_guest_program_spec(self, cmd, stdout, stderr):
        guest_program_spec = vim.GuestProgramSpec()

        program_path, arguments = self._get_program_spec_program_path_and_arguments(cmd)

        arguments += " 1> %s 2> %s" % (stdout, stderr)

        guest_program_spec.programPath = program_path
        guest_program_spec.arguments = arguments

        return guest_program_spec

    def _get_pid_info(self, pid):
        try:
            processes = self.processManager.ListProcessesInGuest(vm=self.vm, auth=self.vm_auth, pids=[pid])
        except vim.fault.NoPermission as e:
            raise AnsibleError("No Permission Error: %s %s" % (to_native(e.msg), to_native(e.privilegeId)))
        except vmodl.fault.SystemError as e:
            # https://pubs.vmware.com/vsphere-6-5/index.jsp?topic=%2Fcom.vmware.wssdk.smssdk.doc%2Fvmodl.fault.SystemError.html
            # https://github.com/ansible/ansible/issues/57607
            if e.reason == 'vix error codes = (1, 0).\n':
                raise AnsibleConnectionFailure(
                    "Connection failed, Netlogon service stopped or dcpromo in progress. Reason: %s" % (
                        to_native(e.reason)
                    )
                )
            else:
                raise AnsibleConnectionFailure("Connection plugin failed. Reason: %s" % (to_native(e.reason)))
        except vim.fault.GuestOperationsUnavailable:
            raise AnsibleConnectionFailure("Cannot connect to guest. Native error: GuestOperationsUnavailable")
        except vim.fault.InvalidGuestLogin:
            raise AnsibleConnectionFailure("Guest login failed. Native error: InvalidGuestLogin")

        return processes[0]

    def _fix_url_for_hosts(self, url):
        """
        Fix url if connection is a host.

        The host part of the URL is returned as '*' if the hostname to be used is the name of the server to which the call was made. For example, if the call is
        made to esx-svr-1.domain1.com and port 443, and the file is available for download from http://esx-svr-1.domain1.com:443/guestFile?id=1&token=1234,
        the URL returned may be http://*:443/guestFile?id=1&token=1234.
        The client replaces the asterisk with the server name on which it invoked the call and 443 with the port number.

        https://code.vmware.com/apis/358/vsphere#/doc/vim.vm.guest.FileManager.FileTransferInformation.html
        """
        return url.replace("*", self.vmware_host).replace("443", self.get_option("vmware_port"))

    def _fetch_file_from_vm(self, guestFilePath):
        try:
            fileTransferInformation = self.fileManager.InitiateFileTransferFromGuest(vm=self.vm, auth=self.vm_auth, guestFilePath=guestFilePath)
        except vim.fault.NoPermission as e:
            raise AnsibleError("No Permission Error: %s %s" % (to_native(e.msg), to_native(e.privilegeId)))
        except vmodl.fault.SystemError as e:
            if e.reason == 'vix error codes = (3016, 0).\n':
                raise AnsibleConnectionFailure(
                    "Connection failed, is the vm currently rebooting? Reason: %s" % (
                        to_native(e.reason)
                    )
                )
            else:
                raise AnsibleConnectionFailure("Connection failed. Reason %s" % (to_native(e.reason)))
        except vim.fault.GuestOperationsUnavailable:
            raise AnsibleConnectionFailure("Cannot connect to guest. Native error: GuestOperationsUnavailable")

        url = self._fix_url_for_hosts(fileTransferInformation.url)
        response = requests.get(url, verify=self.validate_certs, stream=True)

        if response.status_code != 200:
            raise AnsibleError("Failed to fetch file")

        return response

    def delete_file_in_guest(self, filePath):
        """Delete file from VM."""
        try:
            self.fileManager.DeleteFileInGuest(vm=self.vm, auth=self.vm_auth, filePath=filePath)
        except vim.fault.NoPermission as e:
            raise AnsibleError("No Permission Error: %s %s" % (to_native(e.msg), to_native(e.privilegeId)))
        except vmodl.fault.SystemError as e:
            if e.reason == 'vix error codes = (3016, 0).\n':
                raise AnsibleConnectionFailure(
                    "Connection failed, is the vm currently rebooting? Reason: %s" % (
                        to_native(e.reason)
                    )
                )
            else:
                raise AnsibleConnectionFailure("Connection failed. Reason %s" % (to_native(e.reason)))
        except vim.fault.GuestOperationsUnavailable:
            raise AnsibleConnectionFailure("Cannot connect to guest. Native error: GuestOperationsUnavailable")

    def exec_command(self, cmd, in_data=None, sudoable=True):
        """Execute command."""
        super(Connection, self).exec_command(cmd, in_data=in_data, sudoable=sudoable)

        stdout = self.create_temporary_file_in_guest(suffix=".stdout")
        stderr = self.create_temporary_file_in_guest(suffix=".stderr")

        guest_program_spec = self._get_guest_program_spec(cmd, stdout, stderr)

        try:
            pid = self.processManager.StartProgramInGuest(vm=self.vm, auth=self.vm_auth, spec=guest_program_spec)
        except vim.fault.NoPermission as e:
            raise AnsibleError("No Permission Error: %s %s" % (to_native(e.msg), to_native(e.privilegeId)))
        except vim.fault.FileNotFound as e:
            raise AnsibleError("StartProgramInGuest Error: %s" % to_native(e.msg))
        except vmodl.fault.SystemError as e:
            if e.reason == 'vix error codes = (3016, 0).\n':
                raise AnsibleConnectionFailure(
                    "Connection failed, is the vm currently rebooting? Reason: %s" % (
                        to_native(e.reason)
                    )
                )
            else:
                raise AnsibleConnectionFailure("Connection failed. Reason %s" % (to_native(e.reason)))
        except vim.fault.GuestOperationsUnavailable:
            raise AnsibleConnectionFailure("Cannot connect to guest. Native error: GuestOperationsUnavailable")

        pid_info = self._get_pid_info(pid)

        while pid_info.endTime is None:
            sleep(self.get_option("exec_command_sleep_interval"))
            pid_info = self._get_pid_info(pid)

        stdout_response = self._fetch_file_from_vm(stdout)
        self.delete_file_in_guest(stdout)

        stderr_response = self._fetch_file_from_vm(stderr)
        self.delete_file_in_guest(stderr)

        return pid_info.exitCode, stdout_response.text, stderr_response.text

    def fetch_file(self, in_path, out_path):
        """Fetch file."""
        super(Connection, self).fetch_file(in_path, out_path)

        in_path_response = self._fetch_file_from_vm(in_path)

        with open(out_path, "wb") as fd:
            for chunk in in_path_response.iter_content(chunk_size=self.get_option("file_chunk_size")):
                fd.write(chunk)

    def put_file(self, in_path, out_path):
        """Put file."""
        super(Connection, self).put_file(in_path, out_path)

        if not exists(to_bytes(in_path, errors="surrogate_or_strict")):
            raise AnsibleFileNotFound("file or module does not exist: '%s'" % to_native(in_path))

        try:
            put_url = self.fileManager.InitiateFileTransferToGuest(
                vm=self.vm, auth=self.vm_auth, guestFilePath=out_path, fileAttributes=vim.GuestFileAttributes(), fileSize=getsize(in_path), overwrite=True
            )
        except vim.fault.NoPermission as e:
            raise AnsibleError("No Permission Error: %s %s" % (to_native(e.msg), to_native(e.privilegeId)))
        except vmodl.fault.SystemError as e:
            if e.reason == 'vix error codes = (3016, 0).\n':
                raise AnsibleConnectionFailure(
                    "Connection failed, is the vm currently rebooting? Reason: %s" % (
                        to_native(e.reason)
                    )
                )
            else:
                raise AnsibleConnectionFailure("Connection failed. Reason %s" % (to_native(e.reason)))
        except vim.fault.GuestOperationsUnavailable:
            raise AnsibleConnectionFailure("Cannot connect to guest. Native error: GuestOperationsUnavailable")

        url = self._fix_url_for_hosts(put_url)

        # file size of 'in_path' must be greater than 0
        with open(in_path, "rb") as fd:
            response = requests.put(url, verify=self.validate_certs, data=fd)

        if response.status_code != 200:
            raise AnsibleError("File transfer failed")
