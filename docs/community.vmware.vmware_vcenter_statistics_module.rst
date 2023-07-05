

community.vmware.vmware_vcenter_statistics module -- Configures statistics on a vCenter server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This module is part of the `community.vmware collection <https://galaxy.ansible.com/community/vmware>`_.

To install it, use: :code:`ansible-galaxy collection install community.vmware`.

To use it in a playbook, specify: :code:`community.vmware.vmware_vcenter_statistics`.


.. contents::
   :local:
   :depth: 1


Synopsis
--------

- This module can be used to configure the vCenter server statistics.
- The remaining settings can be configured with the module \ :literal:`vmware\_vcenter\_settings`\ .








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
      <div class="ansibleOptionAnchor" id="parameter-hostname"></div>
      <p style="display: inline;"><strong>hostname</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hostname" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The hostname or IP address of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_HOST</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-interval_past_day"></div>
      <p style="display: inline;"><strong>interval_past_day</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_day" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Settings for vCenter server past day statistic collection.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_day/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_day/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Past day statistics collection enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_day/interval_minutes"></div>
      <p style="display: inline;"><strong>interval_minutes</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_day/interval_minutes" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Interval duration in minutes.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>1</code></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
        <li><p><code>4</code></p></li>
        <li><p><code style="color: blue;"><b>5</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_day/level"></div>
      <p style="display: inline;"><strong>level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_day/level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Statistics level.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
        <li><p><code>4</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_day/save_for_days"></div>
      <p style="display: inline;"><strong>save_for_days</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_day/save_for_days" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Save for value in days.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
        <li><p><code>4</code></p></li>
        <li><p><code>5</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-interval_past_month"></div>
      <p style="display: inline;"><strong>interval_past_month</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_month" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Settings for vCenter server past month statistic collection.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_month/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_month/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Past month statistics collection enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_month/interval_hours"></div>
      <p style="display: inline;"><strong>interval_hours</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_month/interval_hours" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Interval duration in hours.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>2</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_month/level"></div>
      <p style="display: inline;"><strong>level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_month/level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Statistics level.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
        <li><p><code>4</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_month/save_for_months"></div>
      <p style="display: inline;"><strong>save_for_months</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_month/save_for_months" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Save for value in months.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-interval_past_week"></div>
      <p style="display: inline;"><strong>interval_past_week</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_week" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Settings for vCenter server past week statistic collection.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_week/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_week/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Past week statistics collection enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_week/interval_minutes"></div>
      <p style="display: inline;"><strong>interval_minutes</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_week/interval_minutes" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Interval duration in minutes.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>30</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_week/level"></div>
      <p style="display: inline;"><strong>level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_week/level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Statistics level.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
        <li><p><code>4</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_week/save_for_weeks"></div>
      <p style="display: inline;"><strong>save_for_weeks</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_week/save_for_weeks" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Save for value in weeks.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-interval_past_year"></div>
      <p style="display: inline;"><strong>interval_past_year</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_year" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>Settings for vCenter server past month statistic collection.</p>
    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_year/enabled"></div>
      <p style="display: inline;"><strong>enabled</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_year/enabled" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">boolean</span>
      </p>
    </td>
    <td>
      <p>Past month statistics collection enabled.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code>false</code></p></li>
        <li><p><code style="color: blue;"><b>true</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_year/interval_days"></div>
      <p style="display: inline;"><strong>interval_days</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_year/interval_days" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Interval duration in days.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_year/level"></div>
      <p style="display: inline;"><strong>level</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_year/level" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Statistics level.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
        <li><p><code>4</code></p></li>
      </ul>

    </td>
  </tr>
  <tr>
    <td></td>
    <td>
      <div class="ansibleOptionAnchor" id="parameter-interval_past_year/save_for_years"></div>
      <p style="display: inline;"><strong>save_for_years</strong></p>
      <a class="ansibleOptionLink" href="#parameter-interval_past_year/save_for_years" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">integer</span>
      </p>
    </td>
    <td>
      <p>Save for value in years.</p>
      <p style="margin-top: 8px;"><b">Choices:</b></p>
      <ul>
        <li><p><code style="color: blue;"><b>1</b></code> <span style="color: blue;">← (default)</span></p></li>
        <li><p><code>2</code></p></li>
        <li><p><code>3</code></p></li>
        <li><p><code>4</code></p></li>
        <li><p><code>5</code></p></li>
      </ul>

    </td>
  </tr>

  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <div class="ansibleOptionAnchor" id="parameter-pass"></div>
      <div class="ansibleOptionAnchor" id="parameter-pwd"></div>
      <p style="display: inline;"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: pass, pwd</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The password of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PASSWORD</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
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
      <p>The port number of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PORT</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p style="margin-top: 8px;"><b style="color: blue;">Default:</b> <code style="color: blue;">443</code></p>
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
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_HOST</code> will be used instead.</p>
      <p>This feature depends on a version of pyvmomi greater than v6.7.1.2018.12</p>
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
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_PROXY_PORT</code> will be used instead.</p>
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <div class="ansibleOptionAnchor" id="parameter-admin"></div>
      <div class="ansibleOptionAnchor" id="parameter-user"></div>
      <p style="display: inline;"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p style="font-size: small; margin-bottom: 0;"><span style="color: darkgreen; white-space: normal;">aliases: admin, user</span></p>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">string</span>
      </p>
    </td>
    <td>
      <p>The username of the vSphere vCenter or ESXi server.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_USER</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
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
      <p>Allows connection when SSL certificates are not valid. Set to <code class='docutils literal notranslate'>false</code> when certificates are not trusted.</p>
      <p>If the value is not specified in the task, the value of environment variable <code class='docutils literal notranslate'>VMWARE_VALIDATE_CERTS</code> will be used instead.</p>
      <p>Environment variable support added in Ansible 2.6.</p>
      <p>If set to <code class='docutils literal notranslate'>true</code>, please make sure Python &gt;= 2.7.9 is installed on the given machine.</p>
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

- All modules requires API write access and hence is not supported on a free ESXi license.


Examples
--------

.. code-block:: yaml

    
    - name: Configure vCenter statistics
      community.vmware.vmware_vcenter_statistics:
        hostname: '{{ vcenter_hostname }}'
        username: '{{ vcenter_username }}'
        password: '{{ vcenter_password }}'
        interval_past_day:
          enabled: true
          interval_minutes: 5
          save_for_days: 1
          level: 1
        interval_past_week:
          enabled: true
          level: 1
        interval_past_month:
          enabled: true
          level: 1
        interval_past_year:
          enabled: true
          save_for_years: 1
          level: 1
      delegate_to: localhost





Return Values
-------------
The following are the fields unique to this module:

.. raw:: html

  <table style="width: 100%;">
  <thead>
    <tr>
    <th><p>Key</p></th>
    <th><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td>
      <div class="ansibleOptionAnchor" id="return-results"></div>
      <p style="display: inline;"><strong>results</strong></p>
      <a class="ansibleOptionLink" href="#return-results" title="Permalink to this return value"></a>
      <p style="font-size: small; margin-bottom: 0;">
        <span style="color: purple;">dictionary</span>
      </p>
    </td>
    <td>
      <p>metadata about vCenter statistics settings</p>
      <p style="margin-top: 8px;"><b>Returned:</b> always</p>
      <p style="margin-top: 8px; color: blue; word-wrap: break-word; word-break: break-all;"><b style="color: black;">Sample:</b> <code>{&#34;changed&#34;: false, &#34;msg&#34;: &#34;vCenter statistics already configured properly&#34;, &#34;past_day_enabled&#34;: true, &#34;past_day_interval&#34;: 5, &#34;past_day_level&#34;: 1, &#34;past_day_save_for&#34;: 1, &#34;past_month_enabled&#34;: true, &#34;past_month_interval&#34;: 2, &#34;past_month_level&#34;: 1, &#34;past_month_save_for&#34;: 1, &#34;past_week_enabled&#34;: true, &#34;past_week_interval&#34;: 30, &#34;past_week_level&#34;: 1, &#34;past_week_save_for&#34;: 1, &#34;past_year_enabled&#34;: true, &#34;past_year_interval&#34;: 1, &#34;past_year_level&#34;: 1, &#34;past_year_save_for&#34;: 1}</code></p>
    </td>
  </tr>
  </tbody>
  </table>




Authors
~~~~~~~

- Christian Kotte (@ckotte)



Collection links
~~~~~~~~~~~~~~~~

* `Issue Tracker <https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc>`__
* `Homepage <https://github.com/ansible-collections/community.vmware>`__
* `Repository (Sources) <https://github.com/ansible-collections/community.vmware.git>`__

