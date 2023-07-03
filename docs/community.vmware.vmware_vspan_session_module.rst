

community.vmware.vmware_vspan_session module -- Create or remove a Port Mirroring session.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note::
    This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

    To install it, use: :code:`ansible-galaxy collection install community.vmware`.

    To use it in a playbook, specify: :code:`community.vmware.vmware_vspan_session`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to create, delete or edit different kind of port mirroring sessions.








Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-description:

      **description**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The description for the session.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_port:

      **destination_port**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Destination port that received the mirrored packets.

      Also any port designated in the value of this property can not match the source port in any of the Distributed Port Mirroring session.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vm:

      **destination_vm**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      With this parameter it is possible, to add a NIC of a VM to a port mirroring session.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vm/name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the VM.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-destination_vm/nic_label:

      **nic_label**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Label of the network interface card to use.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-enabled:

      **enabled**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether the session is enabled.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-encapsulation_vlan_id:

      **encapsulation_vlan_id**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      VLAN ID used to encapsulate the mirrored traffic.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hostname:

      **hostname**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The hostname or IP address of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_HOST`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-mirrored_packet_length:

      **mirrored_packet_length**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      An integer that describes how much of each frame to mirror.

      If unset, all of the frame would be mirrored.

      Setting this property to a smaller value is useful when the consumer will look only at the headers.

      The value cannot be less than 60.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-name:

      **name**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Name of the session.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-normal_traffic_allowed:

      **normal_traffic_allowed**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether or not destination ports can send and receive "normal" traffic.

      Setting this to false will make mirror ports be used solely for mirroring and not double as normal access ports.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-pass:
      .. _parameter-password:
      .. _parameter-pwd:

      **password**

      aliases: pass, pwd

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The password of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PASSWORD`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port:

      **port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      The port number of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PORT`\  will be used instead.

      Environment variable support added in Ansible 2.6.


      Default: :literal:`443`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_host:

      **proxy_host**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Address of a proxy that will receive all HTTPS requests and relay them.

      The format is a hostname or a IP.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PROXY\_HOST`\  will be used instead.

      This feature depends on a version of pyvmomi greater than v6.7.1.2018.12



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_port:

      **proxy_port**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Port of the HTTP proxy that will receive all HTTPS requests and relay them.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_PROXY\_PORT`\  will be used instead.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-sampling_rate:

      **sampling_rate**

      :literal:`integer`

      .. raw:: html

        </div></div>

    - 
      Sampling rate of the session.

      If its value is n, one of every n packets is mirrored.

      Valid values are between 1 to 65535.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-session_type:

      **session_type**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Select the mirroring type.

      In \ :literal:`encapsulatedRemoteMirrorSource`\  session, Distributed Ports can be used as source entities, and IP address can be used as destination entities.

      In \ :literal:`remoteMirrorDest`\  session, VLAN IDs can be used as source entities, and Distributed Ports can be used as destination entities.

      In \ :literal:`remoteMirrorSource`\  session, Distributed Ports can be used as source entities, and uplink ports name can be used as destination entities.

      In \ :literal:`dvPortMirror`\  session, Distributed Ports can be used as both source and destination entities.


      Choices:

      - :literal:`"encapsulatedRemoteMirrorSource"`
      - :literal:`"remoteMirrorDest"`
      - :literal:`"remoteMirrorSource"`
      - :literal:`"dvPortMirror"` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_port_received:

      **source_port_received**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Source port for which received packets are mirrored.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_port_transmitted:

      **source_port_transmitted**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Source port for which transmitted packets are mirrored.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_vm_received:

      **source_vm_received**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      With this parameter it is possible, to add a NIC of a VM to a port mirroring session.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_vm_received/name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the VM.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_vm_received/nic_label:

      **nic_label**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Label of the network interface card to use.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_vm_transmitted:

      **source_vm_transmitted**

      :literal:`dictionary`

      .. raw:: html

        </div></div>

    - 
      With this parameter it is possible, to add a NIC of a VM to a port mirroring session.


    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_vm_transmitted/name:

      **name**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Name of the VM.



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-source_vm_transmitted/nic_label:

      **nic_label**

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      Label of the network interface card to use.




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-state:

      **state**

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      Create or remove the session.


      Choices:

      - :literal:`"present"`
      - :literal:`"absent"`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-strip_original_vlan:

      **strip_original_vlan**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Whether to strip the original VLAN tag.

      If false, the original VLAN tag will be preserved on the mirrored traffic.

      If \ :literal:`encapsulationVlanId`\  has been set and this property is false, the frames will be double tagged with the original VLAN ID as the inner tag.


      Choices:

      - :literal:`false`
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-switch:
      .. _parameter-switch_name:

      **switch**

      aliases: switch_name

      :literal:`string` / :strong:`required`

      .. raw:: html

        </div></div>

    - 
      The name of the distributed vSwitch on which to add or remove the mirroring session.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-admin:
      .. _parameter-user:
      .. _parameter-username:

      **username**

      aliases: admin, user

      :literal:`string`

      .. raw:: html

        </div></div>

    - 
      The username of the vSphere vCenter or ESXi server.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_USER`\  will be used instead.

      Environment variable support added in Ansible 2.6.



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`

      .. raw:: html

        </div></div>

    - 
      Allows connection when SSL certificates are not valid. Set to \ :literal:`false`\  when certificates are not trusted.

      If the value is not specified in the task, the value of environment variable \ :literal:`VMWARE\_VALIDATE\_CERTS`\  will be used instead.

      Environment variable support added in Ansible 2.6.

      If set to \ :literal:`true`\ , please make sure Python \>= 2.7.9 is installed on the given machine.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)





Notes
-----

.. note::
   - All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create distributed mirroring session.
      community.vmware.vmware_vspan_session:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch_name: dvSwitch
        state: present
        name: Basic Session
        enabled: true
        description: "Example description"
        source_port_transmitted: 817
        source_port_received: 817
        destination_port: 815
      delegate_to: localhost

    - name: Create remote destination mirroring session.
      community.vmware.vmware_vspan_session:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch_name: dvSwitch
        state: present
        name: Remote Session
        enabled: true
        description: "Example description"
        source_port_received: 105
        destination_port: 815
        session_type: "remoteMirrorDest"
      delegate_to: localhost

    - name: Delete remote destination mirroring session.
      community.vmware.vmware_vspan_session:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        switch_name: dvSwitch
        state: absent
        name: Remote Session
      delegate_to: localhost







Authors
~~~~~~~

- Peter Gyorgy (@gyorgypeter)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

