.. _community.vmware.vsphere_file_module:


*****************************
community.vmware.vsphere_file
*****************************

**Manage files on a vCenter datastore**



.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage files on a vCenter datastore.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datacenter</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The datacenter on the vCenter server that holds the datastore.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>datastore</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The datastore on the vCenter server to push files to.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>host</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The vCenter server on which the datastore is available.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: hostname</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The password to authenticate on the vCenter server.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The file or directory on the datastore on the vCenter server.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: dest</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>state</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>absent</li>
                                    <li>directory</li>
                                    <li><div style="color: blue"><b>file</b>&nbsp;&larr;</div></li>
                                    <li>touch</li>
                        </ul>
                </td>
                <td>
                        <div>The state of or the action on the provided path.</div>
                        <div>If <code>absent</code>, the file will be removed.</div>
                        <div>If <code>directory</code>, the directory will be created.</div>
                        <div>If <code>file</code>, more information of the (existing) file will be returned.</div>
                        <div>If <code>touch</code>, an empty file will be created if the path does not exist.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>timeout</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">10</div>
                </td>
                <td>
                        <div>The timeout in seconds for the upload to the datastore.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>username</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The user name to authenticate on the vCenter server.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>no</li>
                                    <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                        </ul>
                </td>
                <td>
                        <div>If <code>false</code>, SSL certificates will not be validated. This should only be set to <code>false</code> when no other option exists.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - The vSphere folder API does not allow to remove directory objects.



Examples
--------

.. code-block:: yaml

    - name: Create an empty file on a datastore
      community.vmware.vsphere_file:
        host: '{{ vhost }}'
        username: '{{ vuser }}'
        password: '{{ vpass }}'
        datacenter: DC1 Someplace
        datastore: datastore1
        path: some/remote/file
        state: touch
      delegate_to: localhost

    - name: Create a directory on a datastore
      community.vmware.vsphere_file:
        host: '{{ vhost }}'
        username: '{{ vuser }}'
        password: '{{ vpass }}'
        datacenter: DC2 Someplace
        datastore: datastore2
        path: other/remote/file
        state: directory
      delegate_to: localhost

    - name: Query a file on a datastore
      community.vmware.vsphere_file:
        host: '{{ vhost }}'
        username: '{{ vuser }}'
        password: '{{ vpass }}'
        datacenter: DC1 Someplace
        datastore: datastore1
        path: some/remote/file
        state: file
      delegate_to: localhost
      ignore_errors: true

    - name: Delete a file on a datastore
      community.vmware.vsphere_file:
        host: '{{ vhost }}'
        username: '{{ vuser }}'
        password: '{{ vpass }}'
        datacenter: DC2 Someplace
        datastore: datastore2
        path: other/remote/file
        state: absent
      delegate_to: localhost




Status
------


Authors
~~~~~~~

- Dag Wieers (@dagwieers)
