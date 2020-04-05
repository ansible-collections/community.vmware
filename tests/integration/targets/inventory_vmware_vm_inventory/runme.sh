#!/usr/bin/env bash

[[ -n "$DEBUG" || -n "$ANSIBLE_DEBUG" ]] && set -x

set -euxo pipefail

# Required to differentiate between Python 2 and 3 environ
export ANSIBLE_PYTHON_INTERPRETER=${ANSIBLE_TEST_PYTHON_INTERPRETER:-$(which python)}
export PYTHON=${ANSIBLE_PYTHON_INTERPRETER}
export ANSIBLE_INVENTORY_ENABLED="community.vmware.vmware_vm_inventory,host_list,ini"

# Cache setting
export ANSIBLE_CACHE_PLUGIN_CONNECTION="${PWD}/inventory_cache"
export ANSIBLE_CACHE_PLUGIN="community.general.jsonfile"

INVENTORY_DIR="${PWD}/_test/hosts"
mkdir -p "${INVENTORY_DIR}" 2>/dev/null
touch "${INVENTORY_DIR}/empty.yml"

cleanup() {
    ec=$?
    echo "Cleanup"
    if [ -d "${ANSIBLE_CACHE_PLUGIN_CONNECTION}" ]; then
        echo "Removing ${ANSIBLE_CACHE_PLUGIN_CONNECTION}"
        rm -rf "${ANSIBLE_CACHE_PLUGIN_CONNECTION}"
    fi
    
    if [ -d "${INVENTORY_DIR}" ]; then
        echo "Removing ${INVENTORY_DIR}"
        rm -rf "${INVENTORY_DIR}"
    fi

    echo "Done"
    exit $ec
}
trap cleanup INT TERM EXIT

set_inventory(){
    export ANSIBLE_INVENTORY="${1}"
    echo "INVENTORY '${1}' is active" 
}


# Prepare tests
ansible-playbook -i 'localhost,' playbook/prepare_vmware.yml "$@"

# Set inventory path
set_inventory "${INVENTORY_DIR}"

# Test Cache
ansible-playbook -i 'localhost,' playbook/build_inventory_with_cache.yml "$@"
ansible-inventory --list 1>/dev/null
ansible-playbook playbook/test_inventory_cache.yml -e inventory_cache="${ANSIBLE_CACHE_PLUGIN_CONNECTION}" "$@"

# Test YAML and TOME
ansible-playbook -i 'localhost,' playbook/build_inventory_without_cache.yml "$@"
ansible-inventory --list --yaml 1>/dev/null
if ${PYTHON} -m pip list 2>/dev/null | grep toml >/dev/null 2>&1; then
    ansible-inventory --list --toml 1>/dev/null
fi

# # Test playbook with given inventory
ansible-playbook playbook/test_vmware_vm_inventory.yml "$@"

# Test options
ansible-playbook playbook/test_options.yml "$@"