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

## Testing and Development

If you want to develop new content for this collection or improve what is already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

- [Guidelines for VMware module development](https://docs.ansible.com/ansible/latest/dev_guide/platforms/vmware_guidelines.html)

### Testing with `ansible-test`

First, Git clone collection and install it manually:

```
$ mkdir -p  ~/.ansible/collections/ansible_collections/community
# fetch the source tree:
$ git clone https://github.com/ansible-collections/vmware ~/.ansible/collections/ansible_collections/community/vmware
$ cd ~/.ansible/collections/ansible_collections/community/vmware
```

Prepare your configuration file:

```
$ cat tests/integration/cloud-config-vcenter.ini
[DEFAULT]
vcenter_username: administrator@vsphere.local
vcenter_password: \Q5_o\ve#}51QJ$C*(Ch
vcenter_hostname: vcenter.test
vmware_validate_certs: false
esxi1_username: zuul
esxi1_hostname: esxi1.test
esxi1_password: vp21EQRoPO83b8t56
```

Finally, you can run `ansible-test`:

```
$ VMWARE_TEST_PLATFORM=static ansible-test integration --diff --no-temp-workdir --python 3.7 -vvvv --requirements --allow-disabled vmware_guest_network
```


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
