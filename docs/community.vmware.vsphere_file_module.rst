

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

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datacenter:

      **datacenter**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The datacenter on the vCenter server that holds the datastore.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-datastore:

      **datastore**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The datastore on the vCenter server to push files to.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-host:
      .. _parameter-hostname:

      **host**

      aliases: hostname

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The vCenter server on which the datastore is available.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-password:

      **password**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The password to authenticate on the vCenter server.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-dest:
      .. _parameter-path:

      **path**

      aliases: dest

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The file or directory on the datastore on the vCenter server.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The state of or the action on the provided path.

      If \ :literal:`absent`\ , the file will be removed.

      If \ :literal:`directory`\ , the directory will be created.

      If \ :literal:`file`\ , more information of the (existing) file will be returned.

      If \ :literal:`touch`\ , an empty file will be created if the path does not exist.


      Choices:

      - :literal:`"absent"`
      - :literal:`"directory"`
      - :literal:`"file"` ← (default)
      - :literal:`"touch"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-timeout:

      **timeout**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The timeout in seconds for the upload to the datastore.


      Default: :literal:`10`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-username:

      **username**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The user name to authenticate on the vCenter server.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      If \ :literal:`false`\ , SSL certificates will not be validated. This should only be set to \ :literal:`false`\  when no other option exists.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)





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

