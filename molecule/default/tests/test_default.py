import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_env_vars_added(host):
    f = host.file('/etc/environment')

    assert f.exists
    assert f.contains("VARIABLE='variable value'")


def test_pam_env_vars_added(host):
    f = host.file('/home/vagrant/.pam_environment')

    assert f.exists
