#!/usr/bin/env bash

TMPDIR=$(mktemp -d)
export ANSIBLE_COLLECTIONS_PATH="$TMPDIR"
ansible-galaxy collection install "$1"
antsibull-docs collection-plugins community.vmware --dest-dir docs/ --use-current --output-format simplified-rst --fqcn-plugin-names
rm -rf "$TMPDIR"
