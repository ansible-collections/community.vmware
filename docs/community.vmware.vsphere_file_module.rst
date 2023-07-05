

community.vmware.vsphere_file module -- Manage files on a vCenter datastore
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vsphere_file`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Manage files on a vCenter datastore.








Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datacenter"></div>
      <p style="display: inline;"><strong>datacenter</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datacenter" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The datacenter on the vCenter server that holds the datastore.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-datastore"></div>
      <p style="display: inline;"><strong>datastore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-datastore" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The datastore on the vCenter server to push files to.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-host"></div>
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: hostname</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The vCenter server on which the datastore is available.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The password to authenticate on the vCenter server.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-path"></div>
      <div class="ansibleOptionAnchor" id="parameter-dest"></div>
      <p style="display: inline;"><strong>path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: dest</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The file or directory on the datastore on the vCenter server.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p style="display: inline;"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The state of or the action on the provided path.</p>
      <p>If <code class='docutils literal notranslate'>absent</code>, the file will be removed.</p>
      <p>If <code class='docutils literal notranslate'>directory</code>, the directory will be created.</p>
      <p>If <code class='docutils literal notranslate'>file</code>, more information of the (existing) file will be returned.</p>
      <p>If <code class='docutils literal notranslate'>touch</code>, an empty file will be created if the path does not exist.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>&#34;absent&#34;</code></p></li>
        <li><p><code>&#34;directory&#34;</code></p></li>
        <li><p><code style="color: blue;"><b>&#34;file&#34;</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>&#34;touch&#34;</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-timeout"></div>
      <p style="display: inline;"><strong>timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>The timeout in seconds for the upload to the datastore.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">10</code></p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>
    </td>
    <td>
      <p>The user name to authenticate on the vCenter server.</p>
    </td>
  </tr>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>If <code class='docutils literal notranslate'>false</code>, SSL certificates will not be validated. This should only be set to <code class='docutils literal notranslate'>false</code> when no other option exists.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>




Notes
-----

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







Authors
~~~~~~~

- Dag Wieers (@dagwieers)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

