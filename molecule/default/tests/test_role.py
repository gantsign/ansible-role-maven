import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mvn(Command):
    assert '3.5.3' in Command.check_output('mvn --version')


def test_mvn_debug(Command):
    assert Command('which mvnDebug').rc == 0


@pytest.mark.parametrize('command,version_dir_pattern', [
    ('mvn', 'apache-maven-3\\.5\\.[0-9]+$'),
    ('mvnDebug', 'apache-maven-3\\.5\\.[0-9]+$'),
    ('mvn', 'apache-maven-3\\.3\\.[0-9]+$'),
    ('mvnDebug', 'apache-maven-3\\.3\\.[0-9]+$')
])
def test_commands_installed(Command, File, command, version_dir_pattern):

    maven_home = Command.check_output('find %s | grep --color=never -E %s',
                                      '/opt/maven',
                                      version_dir_pattern)

    command_file = File(maven_home + '/bin/' + command)

    assert command_file.exists
    assert command_file.is_file
    assert command_file.user == 'root'
    assert command_file.group == 'root'
    assert oct(command_file.mode) == '0755'


@pytest.mark.parametrize('fact_group_name', [
    'maven',
    'maven_3_3'
])
def test_facts_installed(File, fact_group_name):
    fact_file = File('/etc/ansible/facts.d/' + fact_group_name + '.fact')

    assert fact_file.exists
    assert fact_file.is_file
    assert fact_file.user == 'root'
    assert fact_file.group == 'root'
    assert oct(fact_file.mode) == '0644'
