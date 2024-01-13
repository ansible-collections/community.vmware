# Testing Ansible Collection: community.vmware

### Testing with `ansible-test`

Clone the collection and install it manually:

```
$ mkdir -p  ~/.ansible/collections/ansible_collections/community
$ git clone https://github.com/ansible-collections/community.vmware ~/.ansible/collections/ansible_collections/community/vmware
$ cd ~/.ansible/collections/ansible_collections/community/vmware
```

If you want to test a PR, you can get it after cloning like this:

```
$ git fetch origin pull/ID/head:BRANCHNAME
$ git checkout BRANCHNAME
```

Prepare VMware configuration file:

```
$ cat tests/integration/cloud-config-vcenter.ini
[DEFAULT]
vcenter_username: administrator@vsphere.local
vcenter_password: mySuperSecretPassw0rd!
vcenter_hostname: vcenter.test
vmware_validate_certs: false
esxi1_username: zuul
esxi1_hostname: esxi1.test
esxi1_password: myEsxiSuperSecretPassw0rd!
```

Run `ansible-test`:

```
$ VMWARE_TEST_PLATFORM=static ansible-test integration --diff --no-temp-workdir --python 3.7 -vvvv --requirements --allow-disabled vmware_guest_network
```


## More Information

* [Developer guide for testing](https://docs.ansible.com/ansible/latest/collections/community/vmware/docsite/dev_guide.html#testing-with-your-own-infrastructure)
