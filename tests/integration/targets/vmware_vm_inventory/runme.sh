#!/usr/bin/env bash
set -eux
export ANSIBLE_CONFIG=ansible.cfg
ansible-playbook prepare_environment.yml $*
ansible-inventory --list -i vmware.yaml
exec ansible-playbook -i vmware.yaml test_inventory.yml $*
