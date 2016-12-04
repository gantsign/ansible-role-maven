Ansible Role: Maven
===================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-maven.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-maven)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.maven-blue.svg)](https://galaxy.ansible.com/gantsign/maven)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-maven/master/LICENSE)

Role to install the [Apache Maven](https://maven.apache.org) build tool.

Requirements
------------

* Ansible >= 1.9

* Linux Distribution

    * Debian Family

        * Debian

            * Wheezy (7)
            * Jessie (8)

        * Ubuntu

            * Trusty (14.04)
            * Wily (15.10)
            * Xenial (16.04)

    * RedHat Family

        * CentOS

            * 6
            * 7

        * Fedora

            * 25

    * SUSE Family

        * OpenSUSE

            * 42.2

    * Note: other versions are likely to work but have not been tested.

* Java SE Development Kit (JDK)

    * The required JDK version is dependent on the Apache Maven version

        | Maven Version | Minimum JDK Version |
        | ------------: | ------------------: |
        |         3.3.x |                   7 |
        |         3.2.x |                   6 |
        |         3.1.x |                   5 |

    * Recommendation: use the
      [gantsign.java](https://galaxy.ansible.com/gantsign/java) role if you
      want to install the Oracle JDK rather than OpenJDK.

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
maven_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

### Supported Maven Versions

The following versions of Maven are supported without any additional
configuration (for other versions follow the Advanced Configuration
instructions):

* `3.3.9`
* `3.2.5`
* `3.1.1`

Advanced Configuration
----------------------

The following role variable is dependent on the Maven version; to use a
Maven version **not pre-configured by this role** you must configure the
variable below:

```yaml
# SHA256 sum for the redistributable package (i.e. apache-maven-{{ maven_version }}-bin.tar.gz)
maven_redis_sha256sum: '6e3e9c949ab4695a204f74038717aa7b2689b1be94875899ac1b3fe42800ff82'
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

Related Roles
-------------

You may find the following related roles useful:

* [gantsign.java](https://galaxy.ansible.com/gantsign/java) for installing the
  Oracle JDK.

* [gantsign.maven-color](https://galaxy.ansible.com/gantsign/maven-color) for
  colorizing the Maven console output.

    * Installs the [Maven Color](https://github.com/jcgay/maven-color) extension
      for Maven authored by [Jean-Christophe Gay](https://github.com/jcgay).

* [gantsign.maven-notifier](https://galaxy.ansible.com/gantsign/maven-notifier)
  for providing a GUI notification when a build ends.

    * Installs the [Maven Notifier](https://github.com/jcgay/maven-notifier)
      extension for Maven authored by
      [Jean-Christophe Gay](https://github.com/jcgay).

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

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
