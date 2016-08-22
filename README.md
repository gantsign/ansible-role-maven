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

# Directory to store files downloaded for Maven installation
maven_download_dir: "{{ x_ansible_download_dir | default('~/.ansible/tmp/downloads') }}"
```

### Supported Maven versions

The following versions of Maven are supported without any additional
configuration (for other versions follow the Advanced Configuration
instructions):

* `3.3.9`

Advanced Configuration
----------------------

The following role variable is dependent on the Maven version; to use a
Maven version **not pre-configured by this role** you must configure the
variable below:

```yaml
# SHA256 sum for the redistributable package (i.e. apache-maven-{{ maven_version }}-bin.tar.gz)
maven_redis_sha256sum: 6e3e9c949ab4695a204f74038717aa7b2689b1be94875899ac1b3fe42800ff82
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gantsign.maven }
```

Role Facts
----------

This role exports the following Ansible facts for use by other roles:

* `ansible_local.maven.general.version`

    * e.g. `3.3.9`

* `ansible_local.maven.general.home`

    * e.g. `/opt/maven/apache-maven-3.3.9`

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
