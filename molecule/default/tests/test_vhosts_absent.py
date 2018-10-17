import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_absent_vhost(host):
    assert not host.file('/etc/apache2/sites-enabled/000-default.conf').exists
