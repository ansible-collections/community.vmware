# Ansible Collection: community.vmware

This repo hosts the `community.vmware` Ansible Collection.

The collection includes the VMware modules and plugins supported by Ansible VMware community to help the management of VMware infrastructure.


## Installation and Usage

### Installing the Collection from Ansible Galaxy

Before using the VMware community collection, you need to install the collection with the `ansible-galaxy` CLI:

    ansible-galaxy collection install community.vmware

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: community.vmware
```

### Required Python libraries

VMware community collection depends upon following third party libraries:

* [`Pyvmomi`](https://github.com/vmware/pyvmomi)
* [`vSphere Automation SDK for Python`](https://github.com/vmware/vsphere-automation-sdk-python/)

### Installing required libraries and SDK

Installing collection does not install any required third party Python libraries or SDKs. You need to install the required Python libraries using following command:

    pip install -r ~/.ansible/collections/ansible_collections/community/vmware/requirements.txt

If you are working on developing and/or testing VMware community collection, you may want to install additional requirements using following command:

    pip install -r ~/.ansible/collections/ansible_collections/community/vmware/test-requirements.txt

## Testing and Development

If you want to develop new content for this collection or improve what is already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

- [Guidelines for VMware module development](https://docs.ansible.com/ansible/latest/dev_guide/platforms/vmware_guidelines.html)

### Testing with `ansible-test`

TBD

## Publishing New Version

TBD

## More Information

TBD

## Communication

We have a dedicated Working Group for VMware.
You can find other people interested in this in `#ansible-vmware` on Freenode IRC.
For more information about communities, meetings and agendas see https://github.com/ansible/community/wiki/VMware.

## License

GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.
