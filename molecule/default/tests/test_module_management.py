import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_enabled_modules(host):
    f = host.file('/etc/apache2/mods-enabled/security2.conf')
    assert f.exists
    assert f.is_symlink
    assert f.linked_to == '/etc/apache2/mods-available/security2.conf'

def test_disabled_modules(host):
    f = host.file('/etc/apache2/mods-enabled/auth_basic.conf')
    assert not f.exists
