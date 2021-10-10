#!/usr/bin/env bash
set -eux

# Envs
export ANSIBLE_PYTHON_INTERPRETER=${ANSIBLE_TEST_PYTHON_INTERPRETER:-$(command -v python)}
export ANSIBLE_INVENTORY_ENABLED="community.vmware.vmware_vm_inventory,host_list,ini"
export ANSIBLE_CACHE_PLUGIN_CONNECTION="${PWD}/inventory_cache"
export ANSIBLE_CACHE_PLUGIN="community.general.jsonfile"

export INVENTORY_DIR="${PWD}/_test/hosts"
mkdir -p "${INVENTORY_DIR}" 2>/dev/null
touch "${INVENTORY_DIR}/empty.vmware.yml"

cleanup() {
    echo "Cleanup"
    if [ -d "${ANSIBLE_CACHE_PLUGIN_CONNECTION}" ]; then
        echo "Removing ${ANSIBLE_CACHE_PLUGIN_CONNECTION}"
        rm -rf "${ANSIBLE_CACHE_PLUGIN_CONNECTION}"
    fi

    if [ -d "${INVENTORY_DIR}" ]; then
        echo "Removing ${INVENTORY_DIR}"
        rm -rf "${INVENTORY_DIR}"
    fi

    unset ANSIBLE_INVENTORY_ENABLED
    unset ANSIBLE_CACHE_PLUGIN ANSIBLE_CACHE_PLUGIN_CONNECTION
    unset INVENTORY_DIR

    echo "Done"
}

trap cleanup INT TERM EXIT

# Prepare tests
ansible-playbook playbook/prepare_vmware.yml "$@"

# Test Cache
# Cache requires community.general.jsonfile
ansible-playbook playbook/build_inventory_with_cache.yml "$@"
ansible-inventory -i "${INVENTORY_DIR}" --list 1>/dev/null
ansible-playbook -i "${INVENTORY_DIR}" playbook/test_inventory_cache.yml "$@"

# Test YAML and TOML
ansible-playbook playbook/build_inventory_without_cache.yml "$@"
ansible-inventory -i "${INVENTORY_DIR}" --list --yaml 1>/dev/null
if ${ANSIBLE_PYTHON_INTERPRETER} -m pip list 2>/dev/null | grep toml >/dev/null 2>&1; then
    ansible-inventory -i "${INVENTORY_DIR}" --list --toml 1>/dev/null
fi

# # Test playbook with the given inventory
ansible-playbook -i "${INVENTORY_DIR}" playbook/test_vmware_vm_inventory.yml "$@"

# Test options
ansible-playbook -i "${INVENTORY_DIR}" playbook/test_options.yml "$@"
