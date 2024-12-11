from ansible.module_utils.basic import env_fallback


def rest_compatible_argument_spec():
    """
    This returns a dictionary that can be used as the baseline for all REST module specs.
    If your module uses the REST API SDK, you should use this instead of the base_argument_spec.
    If your module uses both the REST API SDK and the pyvmomi SDK, you should still use this spec.
    """
    return {
        **base_argument_spec(),
        **dict(
            proxy_protocol=dict(
                type='str',
                default='https',
                choices=['https', 'http'],
                aliases=['protocol']
            ),
        )
    }


def base_argument_spec():
    """
    This returns a dictionary that can be used as the baseline for all VMware module specs. Any arguments
    common to both the REST API SDK and pyvmomi SDK should be placed here.
    If your module uses the REST API, you should use the rest_compatible_argument_spec since that
    includes additional arguments specific to that SDK.
    """
    return dict(
        hostname=dict(
            type='str',
            required=False,
            fallback=(env_fallback, ['VMWARE_HOST']),
        ),
        username=dict(
            type='str',
            aliases=['user', 'admin'],
            required=False,
            fallback=(env_fallback, ['VMWARE_USER'])
        ),
        password=dict(
            type='str',
            aliases=['pass', 'pwd'],
            required=False,
            no_log=True,
            fallback=(env_fallback, ['VMWARE_PASSWORD'])
        ),
        port=dict(
            type='int',
            default=443,
            fallback=(env_fallback, ['VMWARE_PORT'])
        ),
        validate_certs=dict(
            type='bool',
            required=False,
            default=True,
            fallback=(env_fallback, ['VMWARE_VALIDATE_CERTS'])
        ),
        proxy_host=dict(
            type='str',
            required=False,
            default=None,
            fallback=(env_fallback, ['VMWARE_PROXY_HOST'])
        ),
        proxy_port=dict(
            type='int',
            required=False,
            default=None,
            fallback=(env_fallback, ['VMWARE_PROXY_PORT'])
        ),
    )
