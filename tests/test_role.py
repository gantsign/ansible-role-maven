from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_mvn_color(Command):
    assert '3.3.9' in Command.check_output('mvn --version')


def test_mvn_debug(Command):
    assert Command('which mvnDebug').rc == 0
