import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    assert host.package('apache2')


def test_executable(File):
    assert File('/usr/sbin/apache2').exists


def test_enabled_modules(File):
    f = File('/etc/apache2/mods-enabled/ssl.conf')

    assert f.exists
    assert f.is_symlink
    assert f.linked_to == '/etc/apache2/mods-available/ssl.conf'


def test_letsencrypt_global_webroot(File):
    assert File('/etc/apache2/conf-enabled/le.conf').exists
