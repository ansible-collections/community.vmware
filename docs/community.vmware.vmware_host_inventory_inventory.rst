

community.vmware.vmware_host_inventory inventory -- VMware ESXi hostsystem inventory source
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This inventory plugin is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.
You need further requirements to be able to use this inventory plugin,
see `Requirements <ansible_collections.community.vmware.vmware_host_inventory_inventory_requirements_>`_ for details.

To use it in a playbook, specify: :code:`community.vmware.vmware_host_inventory`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- Get VMware ESXi hostsystem as inventory hosts from VMware environment.
- Uses any file which ends with vmware.yml, vmware.yaml, vmware\_host\_inventory.yml, or vmware\_host\_inventory.yaml as a YAML configuration file.



.. _ansible_collections.community.vmware.vmware_host_inventory_inventory_requirements:

Requirements
------------
The below requirements are needed on the local controller node that executes this inventory.

- vSphere Automation SDK - For tag feature






Parameters
----------

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th colspan="2"><p>Parameter</p></th>
    <th><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-cache"></div>
      <p style="display: inline;"><strong>cache</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cache" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>Toggle to enable/disable the caching of the inventory&#x27;s source data, requires a cache plugin setup to work.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[inventory]
  cache = false</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_INVENTORY_CACHE</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-cache_connection"></div>
      <p style="display: inline;"><strong>cache_connection</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cache_connection" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>Cache connection data or path, read cache plugin documentation for specifics.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[defaults]
  fact_caching_connection = VALUE</pre>

        <pre>[inventory]
  cache_connection = VALUE</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_CACHE_PLUGIN_CONNECTION</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_INVENTORY_CACHE_CONNECTION</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-cache_plugin"></div>
      <p style="display: inline;"><strong>cache_plugin</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cache_plugin" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>Cache plugin to use for the inventory&#x27;s source data.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;memory&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[defaults]
  fact_caching = memory</pre>

        <pre>[inventory]
  cache_plugin = memory</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_CACHE_PLUGIN</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_INVENTORY_CACHE_PLUGIN</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-cache_prefix"></div>
      <p style="display: inline;"><strong>cache_prefix</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cache_prefix" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>Prefix to use for cache plugin files/tables</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;ansible_inventory_&#34;</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[defaults]
  fact_caching_prefix = ansible_inventory_</pre>

        <pre>[inventory]
  cache_prefix = ansible_inventory_</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_CACHE_PLUGIN_PREFIX</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-cache_timeout"></div>
      <p style="display: inline;"><strong>cache_timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-cache_timeout" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td>
      <p>Cache duration in seconds</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">3600</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entries</p>
        <pre>[defaults]
  fact_caching_timeout = 3600</pre>

        <pre>[inventory]
  cache_timeout = 3600</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_CACHE_PLUGIN_TIMEOUT</code></p>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_INVENTORY_CACHE_TIMEOUT</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-compose"></div>
      <p style="display: inline;"><strong>compose</strong></p>
      <a class="ansibleOptionLink" href="#parameter-compose" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>

    </td>
    <td>
      <p>Create vars from jinja2 expressions.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">{}</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-filters"></div>
      <p style="display: inline;"><strong>filters</strong></p>
      <a class="ansibleOptionLink" href="#parameter-filters" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>

    </td>
    <td>
      <p>This option allows client-side filtering hosts with jinja templating.</p>
      <p>When server-side filtering is introduced, it should be preferred over this.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-groups"></div>
      <p style="display: inline;"><strong>groups</strong></p>
      <a class="ansibleOptionLink" href="#parameter-groups" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>

    </td>
    <td>
      <p>Add hosts to group based on Jinja2 conditionals.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">{}</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>Name of vCenter or ESXi server.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_HOST</code></p>

      </li>
      <li>
        <p>Environment variable: <code>VMWARE_SERVER</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-hostnames"></div>
      <p style="display: inline;"><strong>hostnames</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostnames" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>

    </td>
    <td>
      <p>A list of templates in order of precedence to compose inventory_hostname.</p>
      <p>Ignores template if resulted in an empty string or None value.</p>
      <p>You can use property specified in <em>properties</em> as variables in the template.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[&#34;name&#34;]</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-keyed_groups"></div>
      <p style="display: inline;"><strong>keyed_groups</strong></p>
      <a class="ansibleOptionLink" href="#parameter-keyed_groups" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>

    </td>
    <td>
      <p>Add hosts to group based on the values of a variable.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[{&#34;key&#34;: &#34;summary.runtime.powerState&#34;, &#34;separator&#34;: &#34;&#34;}]</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-keyed_groups/default_value"></div>
      <p style="display: inline;"><strong>default_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-keyed_groups/default_value" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible-core 2.12</i></p>

    </td>
    <td>
      <p>The default value when the host variable&#x27;s value is an empty string.</p>
      <p>This option is mutually exclusive with <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-keyed_groups/trailing_separator"><span class="std std-ref"><span class="pre">keyed_groups[].trailing_separator</span></span></a></strong></code>.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-keyed_groups/key"></div>
      <p style="display: inline;"><strong>key</strong></p>
      <a class="ansibleOptionLink" href="#parameter-keyed_groups/key" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>The key from input dictionary used to generate groups</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-keyed_groups/parent_group"></div>
      <p style="display: inline;"><strong>parent_group</strong></p>
      <a class="ansibleOptionLink" href="#parameter-keyed_groups/parent_group" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>parent group for keyed group</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-keyed_groups/prefix"></div>
      <p style="display: inline;"><strong>prefix</strong></p>
      <a class="ansibleOptionLink" href="#parameter-keyed_groups/prefix" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>A keyed group name will start with this prefix</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-keyed_groups/separator"></div>
      <p style="display: inline;"><strong>separator</strong></p>
      <a class="ansibleOptionLink" href="#parameter-keyed_groups/separator" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>separator used to build the keyed group name</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">&#34;_&#34;</code></p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-keyed_groups/trailing_separator"></div>
      <p style="display: inline;"><strong>trailing_separator</strong></p>
      <a class="ansibleOptionLink" href="#parameter-keyed_groups/trailing_separator" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible-core 2.12</i></p>

    </td>
    <td>
      <p>Set this option to <code class="ansible-value literal notranslate">False</code> to omit the <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-keyed_groups/separator"><span class="std std-ref"><span class="pre">keyed_groups[].separator</span></span></a></strong></code> after the host variable when the value is an empty string.</p>
      <p>This option is mutually exclusive with <code class="ansible-option literal notranslate"><strong><a class="reference internal" href="#parameter-keyed_groups/default_value"><span class="std std-ref"><span class="pre">keyed_groups[].default_value</span></span></a></strong></code>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-leading_separator"></div>
      <p style="display: inline;"><strong>leading_separator</strong></p>
      <a class="ansibleOptionLink" href="#parameter-leading_separator" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible-core 2.11</i></p>

    </td>
    <td>
      <p>Use in conjunction with keyed_groups.</p>
      <p>By default, a keyed group that does not have a prefix or a separator provided will have a name that starts with an underscore.</p>
      <p>This is because the default prefix is "" and the default separator is "_".</p>
      <p>Set this option to False to omit the leading underscore (or other separator) if no prefix is given.</p>
      <p>If the group name is derived from a mapping the separator is still used to concatenate the items.</p>
      <p>To not use a separator in the group name at all, set the separator for the keyed group to an empty string instead.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>Password of vSphere user.</p>
      <p>Accepts vault encrypted variable.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_PASSWORD</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-port"></div>
      <p style="display: inline;"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td>
      <p>Port number used to connect to vCenter or ESXi Server.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_PORT</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-properties"></div>
      <p style="display: inline;"><strong>properties</strong></p>
      <a class="ansibleOptionLink" href="#parameter-properties" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=string</span>
      </p>

    </td>
    <td>
      <p>Specify the list of VMware schema properties associated with the ESXi hostsystem.</p>
      <p>These properties will be populated in hostvars of the given ESXi hostsystem.</p>
      <p>Each value in the list can be a path to a specific property in hostsystem object or a path to a collection of hostsystem objects.</p>
      <p><code class='docutils literal notranslate'>summary.runtime.powerState</code> are required if <code class='docutils literal notranslate'>keyed_groups</code> is set to default.</p>
      <p>Please make sure that all the properties that are used in other parameters are included in this options.</p>
      <p>In addition to ESXi hostsystem&#x27;s properties, the following are special values</p>
      <p>Use <code class='docutils literal notranslate'>customValue</code> to populate ESXi hostsystem&#x27;s custom attributes. <code class='docutils literal notranslate'>customValue</code> is only supported by vCenter and not by ESXi.</p>
      <p>Use <code class='docutils literal notranslate'>all</code> to populate all the properties of the virtual machine. The value <code class='docutils literal notranslate'>all</code> is time consuming operation, do not use unless required absolutely.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[&#34;name&#34;, &#34;customValue&#34;, &#34;summary.runtime.powerState&#34;]</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-proxy_host"></div>
      <p style="display: inline;"><strong>proxy_host</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_host" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>

    </td>
    <td>
      <p>Address of a proxy that will receive all HTTPS requests and relay them.</p>
      <p>The format is a hostname or a IP.</p>
      <p>This feature depends on a version of pyvmomi&gt;=v6.7.1.2018.12.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_PROXY_HOST</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-proxy_port"></div>
      <p style="display: inline;"><strong>proxy_port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-proxy_port" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>

    </td>
    <td>
      <p>Port of the HTTP proxy that will receive all HTTPS requests and relay them.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_PROXY_PORT</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-resources"></div>
      <p style="display: inline;"><strong>resources</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resources" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">list</span>
        / <span style="color: purple;">elements=dictionary</span>
      </p>

    </td>
    <td>
      <p>A list of resources to limit search scope.</p>
      <p>Each resource item is represented by exactly one <code class='docutils literal notranslate'>&#x27;vim_type_snake_case</code>:<code class='docutils literal notranslate'>list of resource names</code> pair and optional nested <em>resources</em></p>
      <p>Key name is based on snake case of a vim type name; e.g <code class='docutils literal notranslate'>host_system</code> correspond to <code class='docutils literal notranslate'>vim.HostSystem</code></p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">[]</code></p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-strict"></div>
      <p style="display: inline;"><strong>strict</strong></p>
      <a class="ansibleOptionLink" href="#parameter-strict" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>If <code class="ansible-value literal notranslate">yes</code> make invalid entries a fatal error, otherwise skip and continue.</p>
      <p>Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-use_extra_vars"></div>
      <p style="display: inline;"><strong>use_extra_vars</strong></p>
      <a class="ansibleOptionLink" href="#parameter-use_extra_vars" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
      <p><i style="font-size: small; color: darkgreen;">added in ansible-core 2.11</i></p>

    </td>
    <td>
      <p>Merge extra vars into the available variables for composition (highest precedence).</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>INI entry</p>
        <pre>[inventory_plugins]
  use_extra_vars = false</pre>

      </li>
      <li>
        <p>Environment variable: <code>ANSIBLE_INVENTORY_USE_EXTRA_VARS</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
        / <span style="color: red;">required</span>
      </p>

    </td>
    <td>
      <p>Name of vSphere user.</p>
      <p>Accepts vault encrypted variable.</p>
      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_USER</code></p>

      </li>
      <li>
        <p>Environment variable: <code>VMWARE_USERNAME</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-validate_certs"></div>
      <p style="display: inline;"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-validate_certs" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>Allows connection when SSL certificates are not valid.</p>
      <p>Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

      <p style="margin-top: 8px;"><b>Configuration:</b></p>
      <ul>
      <li>
        <p>Environment variable: <code>VMWARE_VALIDATE_CERTS</code></p>

      </li>
      </ul>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-with_nested_properties"></div>
      <p style="display: inline;"><strong>with_nested_properties</strong></p>
      <a class="ansibleOptionLink" href="#parameter-with_nested_properties" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>This option transform flatten properties name to nested dictionary.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-with_path"></div>
      <p style="display: inline;"><strong>with_path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-with_path" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>Include ESXi hostsystem&#x27;s path.</p>
      <p>Set this option to a string value to replace root name from <em>&#x27;Datacenters&#x27;</em>.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-with_sanitized_property_name"></div>
      <p style="display: inline;"><strong>with_sanitized_property_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-with_sanitized_property_name" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>This option allows property name sanitization to create safe property names for use in Ansible.</p>
      <p>Also, transforms property name to snake case.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-with_tags"></div>
      <p style="display: inline;"><strong>with_tags</strong></p>
      <a class="ansibleOptionLink" href="#parameter-with_tags" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>

    </td>
    <td>
      <p>Include tags and associated hosts.</p>
      <p>Requires &#x27;vSphere Automation SDK&#x27; library to be installed on the given controller machine.</p>
      <p>Please refer following URLs for installation steps</p>
      <p><a href='https://code.vmware.com/web/sdk/7.0/vsphere-automation-python'>https://code.vmware.com/web/sdk/7.0/vsphere-automation-python</a></p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>false</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>true</code></p></li>
      </ul>

    </td>
  </tr>
  </tbody>
  </table>






Examples
--------

.. code-block:: yaml

    
    # Sample configuration file for VMware Host dynamic inventory
        plugin: community.vmware.vmware_host_inventory
        strict: false
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        with_tags: true

    # Using compose
        plugin: community.vmware.vmware_host_inventory
        hostname: 10.65.223.31
        username: administrator@vsphere.local
        password: Esxi@123$%
        validate_certs: false
        properties:
        - name
        - summary
        - config.lockdownMode
        compose:
            ansible_user: "'root'"
            ansible_connection: "'ssh'"







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

