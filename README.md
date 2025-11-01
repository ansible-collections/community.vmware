# Ansible Collection: community.vmware

This repo hosts the `community.vmware` Ansible Collection.

The collection includes the VMware modules and plugins supported by Ansible VMware community to help the management of VMware infrastructure.

## Releases and maintenance

| Release | Status                      | End of life |
| ------: | --------------------------: | ----------: |
|       6 | Maintained                  |    Nov 2027 |
|       5 | Maintained (bug fixes only) |    Nov 2026 |
|       4 | Unmaintained                |    Nov 2025 |
|       3 | Unmaintained                |    Nov 2024 |
|       2 | Unmaintained                |    Nov 2023 |
|       1 | Unmaintained                |    Nov 2022 |

## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.19.0**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.

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

VMware community collection depends on Python 3.9+ and on following third party libraries:

* [`vcf-sdk`](https://pypi.org/project/vcf-sdk) >=9.0.0.0

### Installing required libraries and SDK

Installing collection does not install any required third party Python libraries or SDKs. You need to install the required Python libraries using following command:

    pip install -r ~/.ansible/collections/ansible_collections/community/vmware/requirements.txt

If you are working on developing and/or testing VMware community collection, you may want to install additional requirements using following command:

    pip install -r ~/.ansible/collections/ansible_collections/community/vmware/test-requirements.txt

## Testing and Development

If you want to develop new content for this collection or improve what is already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

- [Guidelines for VMware module development](https://docs.ansible.com/ansible/latest/collections/community/vmware/docsite/dev_guide.html)

### Testing with `ansible-test`

Refer [testing](testing.md) for more information.

## Publishing New Version

Assuming your (local) repository has set `origin` to your GitHub fork and this repository is added as `upstream`:

Prepare the release:
- Make sure your fork is up to date: `git checkout main && git pull && git fetch upstream && git merge upstream/main`.
- Run `ansible-playbook tools/prepare_release.yml`. The playbook tries to generate the next minor release automatically, but you can also set the version explicitly with `--extra-vars "version=$VERSION"`. You *will* have to set the version explicitly when publishing a new major release.
- Push the created release branch to your GitHub repo (`git push --set-upstream origin prepare_$VERSION_release`) and open a PR for review.

Push the release:
- After the PR has been merged, make sure your fork is up to date: `git checkout main && git pull && git fetch upstream && git merge upstream/main`.
- Tag the release: `git tag -s $VERSION`
- Push the tag: `git push upstream $VERSION`
- Manually `Create release from tag` on GitHub. Copy the changes from the tag instead of generating the release notes.

Revert the version in `galaxy.yml` back to `null`:
- Make sure your fork is up to date: `git checkout main && git pull && git fetch upstream && git merge upstream/main`.
- Run `ansible-playbook tools/unset_version.yml`.
- Push the created branch to your GitHub repo (`git push --set-upstream origin unset_version_$VERSION`) and open a PR for review.

## Communication

* Join the Ansible forum:
    * [Get Help](https://forum.ansible.com/c/help/6): get help or help others.
    * [Posts tagged with 'vmware'](https://forum.ansible.com/tag/vmware): subscribe to participate in VMware-related conversations.
    * [Ansible VMware Automation Working Group](https://forum.ansible.com/g/ansible-vmware): by joining the team you will automatically get subscribed to the posts tagged with ['vmware'](https://forum.ansible.com/tag/vmware).
    * [Social Spaces](https://forum.ansible.com/c/chat/4): gather and interact with fellow enthusiasts.
    * [News & Announcements](https://forum.ansible.com/c/news/5): track project-wide announcements including social events.

* The Ansible [Bullhorn newsletter](https://docs.ansible.com/ansible/devel/community/communication.html#the-bullhorn): used to announce releases and important changes.

For more information about communication, see the [Ansible communication guide](https://docs.ansible.com/ansible/devel/community/communication.html).

## License

GNU General Public License v3.0 or later

See [LICENSE](LICENSE) to see the full text.
