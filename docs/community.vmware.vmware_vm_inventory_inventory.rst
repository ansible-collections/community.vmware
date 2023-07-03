

community.vmware.vmware_vm_inventory inventory -- VMware Guest inventory source
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This inventory plugin is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this inventory plugin,
see `Requirements <ansible_collections.community.vmware.vmware_vm_inventory_inventory_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_vm_inventory`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Get virtual machines as inventory hosts from VMware environment.
- Uses any file which ends with vmware.yml, vmware.yaml, vmware\_vm\_inventory.yml, or vmware\_vm\_inventory.yaml as a YAML configuration file.



.. _ansible_collections.community.vmware.vmware_vm_inventory_inventory_requirements:

Requirements
------------
The below requirements are needed on the local controller node that executes this inventory.

- requests \>= 2.3
- vSphere Automation SDK - For tag feature






Parameters
----------

.. list-table::
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cache:

      **cache**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`


      Configuration:

      - INI entry:

        .. code-block::

          [inventory]
          cache = false


      - Environment variable: :literal:`ANSIBLE\_INVENTORY\_CACHE`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cache_connection:

      **cache_connection**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      Cache connection data or path, read cache plugin documentation for specifics.


      Configuration:

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching_connection = VALUE



        .. code-block::

          [inventory]
          cache_connection = VALUE


      - Environment variable: :literal:`ANSIBLE\_CACHE\_PLUGIN\_CONNECTION`

      - Environment variable: :literal:`ANSIBLE\_INVENTORY\_CACHE\_CONNECTION`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cache_plugin:

      **cache_plugin**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      Cache plugin to use for the inventory's source data.


      Default: :literal:`"memory"`

      Configuration:

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching = memory



        .. code-block::

          [inventory]
          cache_plugin = memory


      - Environment variable: :literal:`ANSIBLE\_CACHE\_PLUGIN`

      - Environment variable: :literal:`ANSIBLE\_INVENTORY\_CACHE\_PLUGIN`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cache_prefix:

      **cache_prefix**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      Prefix to use for cache plugin files/tables


      Default: :literal:`"ansible\_inventory\_"`

      Configuration:

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching_prefix = ansible_inventory_



        .. code-block::

          [inventory]
          cache_prefix = ansible_inventory_


      - Environment variable: :literal:`ANSIBLE\_CACHE\_PLUGIN\_PREFIX`

      - Environment variable: :literal:`ANSIBLE\_INVENTORY\_CACHE\_PLUGIN\_PREFIX`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-cache_timeout:

      **cache_timeout**

      :literal:`integer`




      .. raw:: html

        </div></div>

    - 
      Cache duration in seconds


      Default: :literal:`3600`

      Configuration:

      - INI entries:

        .. code-block::

          [defaults]
          fact_caching_timeout = 3600



        .. code-block::

          [inventory]
          cache_timeout = 3600


      - Environment variable: :literal:`ANSIBLE\_CACHE\_PLUGIN\_TIMEOUT`

      - Environment variable: :literal:`ANSIBLE\_INVENTORY\_CACHE\_TIMEOUT`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-compose:

      **compose**

      :literal:`dictionary`




      .. raw:: html

        </div></div>

    - 
      Create vars from jinja2 expressions.


      Default: :literal:`{}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-filters:

      **filters**

      :literal:`list` / :literal:`elements=string`




      .. raw:: html

        </div></div>

    - 
      This option allows client-side filtering hosts with jinja templating.

      When server-side filtering is introduced, it should be preferred over this.


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-groups:

      **groups**

      :literal:`dictionary`




      .. raw:: html

        </div></div>

    - 
      Add hosts to group based on Jinja2 conditionals.


      Default: :literal:`{}`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hostname:

      **hostname**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      Name of vCenter or ESXi server.


      Configuration:

      - Environment variable: :literal:`VMWARE\_HOST`

      - Environment variable: :literal:`VMWARE\_SERVER`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-hostnames:

      **hostnames**

      :literal:`list` / :literal:`elements=string`




      .. raw:: html

        </div></div>

    - 
      A list of templates in order of precedence to compose inventory\_hostname.

      Ignores template if resulted in an empty string or None value.

      You can use property specified in \ :emphasis:`properties`\  as variables in the template.


      Default: :literal:`["config.name + \\"\_\\" + config.uuid"]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-keyed_groups:

      **keyed_groups**

      :literal:`list` / :literal:`elements=dictionary`




      .. raw:: html

        </div></div>

    - 
      Add hosts to group based on the values of a variable.


      Default: :literal:`[{"key": "config.guestId", "separator": ""}, {"key": "summary.runtime.powerState", "separator": ""}]`

    
  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-keyed_groups/default_value:

      **default_value**

      :literal:`string`

      added in ansible-core 2.12





      .. raw:: html

        </div></div>

    - 
      The default value when the host variable's value is an empty string.

      This option is mutually exclusive with \ :literal:`keyed\_groups[].trailing\_separator` (`link <parameter-keyed_groups/trailing_separator_>`_)\ .



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-keyed_groups/key:

      **key**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      The key from input dictionary used to generate groups



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-keyed_groups/parent_group:

      **parent_group**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      parent group for keyed group



  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-keyed_groups/prefix:

      **prefix**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      A keyed group name will start with this prefix


      Default: :literal:`""`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-keyed_groups/separator:

      **separator**

      :literal:`string`




      .. raw:: html

        </div></div>

    - 
      separator used to build the keyed group name


      Default: :literal:`"\_"`


  * - .. raw:: html

        <div style="display: flex;"><div style="margin-left: 2em; border-right: 1px solid #000000;"></div><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-keyed_groups/trailing_separator:

      **trailing_separator**

      :literal:`boolean`

      added in ansible-core 2.12





      .. raw:: html

        </div></div>

    - 
      Set this option to \ :literal:`false`\  to omit the \ :literal:`keyed\_groups[].separator` (`link <parameter-keyed_groups/separator_>`_)\  after the host variable when the value is an empty string.

      This option is mutually exclusive with \ :literal:`keyed\_groups[].default\_value` (`link <parameter-keyed_groups/default_value_>`_)\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)




  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-leading_separator:

      **leading_separator**

      :literal:`boolean`

      added in ansible-core 2.11





      .. raw:: html

        </div></div>

    - 
      Use in conjunction with keyed\_groups.

      By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.

      This is because the default prefix is "" and the default separator is "\_".

      Set this option to False to omit the leading underscore (or other separator) if no prefix is given.

      If the group name is derived from a mapping the separator is still used to concatenate the items.

      To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-password:

      **password**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      Password of vSphere user.

      Accepts vault encrypted variable.


      Configuration:

      - Environment variable: :literal:`VMWARE\_PASSWORD`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-port:

      **port**

      :literal:`integer`




      .. raw:: html

        </div></div>

    - 
      Port number used to connect to vCenter or ESXi Server.


      Default: :literal:`443`

      Configuration:

      - Environment variable: :literal:`VMWARE\_PORT`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-properties:

      **properties**

      :literal:`list` / :literal:`elements=string`




      .. raw:: html

        </div></div>

    - 
      Specify the list of VMware schema properties associated with the VM.

      These properties will be populated in hostvars of the given VM.

      Each value in the list can be a path to a specific property in VM object or a path to a collection of VM objects.

      \ :literal:`config.name`\ , \ :literal:`config.uuid`\  are required properties if \ :literal:`hostnames`\  is set to default.

      \ :literal:`config.guestId`\ , \ :literal:`summary.runtime.powerState`\  are required if \ :literal:`keyed\_groups`\  is set to default.

      Please make sure that all the properties that are used in other parameters are included in this options.

      In addition to VM properties, the following are special values

      Use \ :literal:`customValue`\  to populate virtual machine's custom attributes. \ :literal:`customValue`\  is only supported by vCenter and not by ESXi.

      Use \ :literal:`all`\  to populate all the properties of the virtual machine. The value \ :literal:`all`\  is time consuming operation, do not use unless required absolutely.

      Please refer more VMware guest attributes which can be used as properties \ https://docs.ansible.com/ansible/latest/collections/community/vmware/docsite/vmware_scenarios/vmware_inventory_vm_attributes.html\ 


      Default: :literal:`["name", "config.cpuHotAddEnabled", "config.cpuHotRemoveEnabled", "config.instanceUuid", "config.hardware.numCPU", "config.template", "config.name", "config.uuid", "guest.hostName", "guest.ipAddress", "guest.guestId", "guest.guestState", "runtime.maxMemoryUsage", "customValue", "summary.runtime.powerState", "config.guestId"]`


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

      This feature depends on a version of pyvmomi\>=v6.7.1.2018.12.


      Configuration:

      - Environment variable: :literal:`VMWARE\_PROXY\_HOST`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-proxy_port:

      **proxy_port**

      :literal:`integer`




      .. raw:: html

        </div></div>

    - 
      Port of the HTTP proxy that will receive all HTTPS requests and relay them.


      Configuration:

      - Environment variable: :literal:`VMWARE\_PROXY\_PORT`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-resources:

      **resources**

      :literal:`list` / :literal:`elements=dictionary`




      .. raw:: html

        </div></div>

    - 
      A list of resources to limit search scope.

      Each resource item is represented by exactly one \ :literal:`'vim\_type\_snake\_case`\ :\ :literal:`list of resource names`\  pair and optional nested \ :emphasis:`resources`\ 

      Key name is based on snake case of a vim type name; e.g \ :literal:`host\_system`\  correspond to \ :literal:`vim.HostSystem`\ 

      See  \ `VIM Types <https://pubs.vmware.com/vi-sdk/visdk250/ReferenceGuide/index-mo_types.html>`__\ 


      Default: :literal:`[]`


  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-strict:

      **strict**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      If \ :literal:`true`\  make invalid entries a fatal error, otherwise skip and continue.

      Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-use_extra_vars:

      **use_extra_vars**

      :literal:`boolean`

      added in ansible-core 2.11





      .. raw:: html

        </div></div>

    - 
      Merge extra vars into the available variables for composition (highest precedence).


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`


      Configuration:

      - INI entry:

        .. code-block::

          [inventory_plugins]
          use_extra_vars = false


      - Environment variable: :literal:`ANSIBLE\_INVENTORY\_USE\_EXTRA\_VARS`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-username:

      **username**

      :literal:`string` / :strong:`required`




      .. raw:: html

        </div></div>

    - 
      Name of vSphere user.

      Accepts vault encrypted variable.


      Configuration:

      - Environment variable: :literal:`VMWARE\_USER`

      - Environment variable: :literal:`VMWARE\_USERNAME`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-validate_certs:

      **validate_certs**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      Allows connection when SSL certificates are not valid.

      Set to \ :literal:`false`\  when certificates are not trusted.


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)


      Configuration:

      - Environment variable: :literal:`VMWARE\_VALIDATE\_CERTS`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-with_nested_properties:

      **with_nested_properties**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      This option transform flatten properties name to nested dictionary.

      From 1.10.0 and onwards, default value is set to \ :literal:`true`\ .


      Choices:

      - :literal:`false`
      - :literal:`true` ← (default)



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-with_path:

      **with_path**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      Include virtual machines path.

      Set this option to a string value to replace root name from \ :emphasis:`'Datacenters'`\ .


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-with_sanitized_property_name:

      **with_sanitized_property_name**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      This option allows property name sanitization to create safe property names for use in Ansible.

      Also, transforms property name to snake case.


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`



  * - .. raw:: html

        <div style="display: flex;"><div style="flex: 1 0 auto; white-space: nowrap; margin-left: 0.25em;">

      .. _parameter-with_tags:

      **with_tags**

      :literal:`boolean`




      .. raw:: html

        </div></div>

    - 
      Include tags and associated virtual machines.

      Requires 'vSphere Automation SDK' library to be installed on the given controller machine.

      Please refer following URLs for installation steps

      \ https://code.vmware.com/web/sdk/7.0/vsphere-automation-python\ 


      Choices:

      - :literal:`false` ← (default)
      - :literal:`true`







Examples
--------

.. code-block:: yaml

    
    # Sample configuration file for VMware Guest dynamic inventory
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        with_tags: true

    # Gather minimum set of properties for VMware guest
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        properties:
        - 'name'
        - 'guest.ipAddress'
        - 'config.name'
        - 'config.uuid'

    # Create Groups based upon VMware Tools status
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        properties:
        - 'name'
        - 'config.name'
        - 'guest.toolsStatus'
        - 'guest.toolsRunningStatus'
        hostnames:
        - config.name
        keyed_groups:
        - key: guest.toolsStatus
          separator: ''
        - key: guest.toolsRunningStatus
          separator: ''

    # Filter VMs based upon condition
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        properties:
        - 'runtime.powerState'
        - 'config.name'
        filters:
        - runtime.powerState == "poweredOn"
        hostnames:
        - config.name

    # Filter VM's based on OR conditions
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        properties:
        - 'name'
        - 'config.name'
        - 'guest.ipAddress'
        - 'guest.toolsStatus'
        - 'guest.toolsRunningStatus'
        - 'config.guestFullName'
        - 'config.guestId'
        hostnames:
        - 'config.name'
        filters:
        - config.guestId == "rhel7_64Guest" or config.name == "rhel_20_04_empty"

    # Filter VM's based on regex conditions
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        properties:
        - 'config.name'
        - 'config.guestId'
        - 'guest.ipAddress'
        - 'summary.runtime.powerState'
        filters:
        - guest.ipAddress is defined and (guest.ipAddress is match('192.168.*') or guest.ipAddress is match('192.169.*'))

    # Using compose and groups
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        properties:
        - 'name'
        - 'config.name'
        - 'guest.ipAddress'
        compose:
          # This will populate the IP address of virtual machine if available
          # and will be used while communicating to the given virtual machine
          ansible_host: 'guest.ipAddress'
          composed_var: 'config.name'
          # This will populate a host variable with a string value
          ansible_user: "'admin'"
          ansible_connection: "'ssh'"
        groups:
          VMs: true
        hostnames:
        - config.name

    # Use Datacenter, Cluster and Folder value to list VMs
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.200.241
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        with_tags: true
        resources:
          - datacenter:
            - Asia-Datacenter1
            - Asia-Datacenter2
            resources:
            - compute_resource:
              - Asia-Cluster1
              resources:
              - host_system:
                - Asia-ESXI4
            - folder:
              - dev
              - prod

    # Use Category and it's relation with Tag
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.201.128
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        hostnames:
        - 'config.name'
        properties:
        - 'config.name'
        - 'config.guestId'
        - 'guest.ipAddress'
        - 'summary.runtime.powerState'
        with_tags: true
        keyed_groups:
        - key: tag_category.OS
          prefix: "vmware_tag_os_category_"
          separator: ""
        with_nested_properties: true
        filters:
        - "tag_category.OS is defined and 'Linux' in tag_category.OS"

    # customizing hostnames based on VM's FQDN. The second hostnames template acts as a fallback mechanism.
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        hostnames:
         - 'config.name+"."+guest.ipStack.0.dnsConfig.domainName'
         - 'config.name'
        properties:
          - 'config.name'
          - 'config.guestId'
          - 'guest.hostName'
          - 'guest.ipAddress'
          - 'guest.guestFamily'
          - 'guest.ipStack'

    # Select a specific IP address for use by ansible when multiple NICs are present on the VM
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        compose:
          # Set the IP address used by ansible to one that starts by 10.42. or 10.43.
          ansible_host: >-
            guest.net
            | selectattr('ipAddress')
            | map(attribute='ipAddress')
            | flatten
            | select('match', '^10.42.*|^10.43.*')
            | list
            | first
        properties:
          - guest.net

    # Group hosts using Jinja2 conditionals
        plugin: community.vmware.vmware_vm_inventory
        strict: false
        hostname: 10.65.13.37
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        hostnames:
        - config.name
        properties:
        - 'name'
        - 'config.name'
        - 'config.datastoreUrl'
        groups:
          slow_storage: "'Nas01' in config.datastoreUrl[0].name"
          fast_storage: "'SSD' in config.datastoreUrl[0].name"







Authors
~~~~~~~

- Abhijeet Kasurde (@Akasurde)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

