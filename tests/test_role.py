import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_mvn(Command):
    assert '3.3.9' in Command.check_output('mvn --version')


def test_mvn_debug(Command):
    assert Command('which mvnDebug').rc == 0


@pytest.mark.parametrize('command', [
    'mvn',
    'mvnDebug'
])
def test_commands_installed(Command, File, command):

    maven_home = Command.check_output('find %s | grep --color=never -E %s',
                                      '/opt/maven',
                                      'apache-maven-3\\.3\\.[0-9]+$')

    command_file = File(maven_home + '/bin/' + command)

    assert command_file.exists
    assert command_file.is_file
    assert command_file.user == 'root'
    assert command_file.group == 'root'
    assert oct(command_file.mode) == '0755'


def test_facts_installed(File):
    fact_file = File('/etc/ansible/facts.d/maven.fact')

    assert fact_file.exists
    assert fact_file.is_file
    assert fact_file.user == 'root'
    assert fact_file.group == 'root'
    assert oct(fact_file.mode) == '0644'
