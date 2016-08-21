Ansible Role: Maven
===================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-maven.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-maven)

Role to install the [Apache Maven](https://maven.apache.org) build tool.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Maven version number
maven_version: '3.3.9'

# Mirror to download the Maven redistributable package from
maven_mirror: "http://archive.apache.org/dist/maven/maven-{{ maven_version|regex_replace('\\..*', '') }}/{{ maven_version }}/binaries"

# Base installation directory the Maven distribution
maven_install_dir: /opt/maven

# Path for Ansible to store downloaded files
local_ansible_data_path: /tmp/ansible/data
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gantsign.maven }
```

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:
* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To run the role (i.e. the `tests/test.yml` playbook), and test the results
(`tests/test_role.py`), execute the following command from the project root
(i.e. the directory with `molecule.yml` in it):

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
