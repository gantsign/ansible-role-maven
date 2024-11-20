Ansible Role: Maven
===================

[![Tests](https://github.com/gantsign/ansible-role-maven/workflows/Tests/badge.svg)](https://github.com/gantsign/ansible-role-maven/actions?query=workflow%3ATests)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.maven-blue.svg)](https://galaxy.ansible.com/gantsign/maven)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-maven/master/LICENSE)

Role to install the [Apache Maven](https://maven.apache.org) build tool.

Requirements
------------

* Ansible Core >= 2.16

* Linux Distribution

    * Debian Family

        * Debian

            * Buster (10)
            * Bullseye (11)

        * Ubuntu

            * Focal (20.04)
            * Jammy (22.04)

    * RedHat Family

        * Rocky Linux

            * 8

        * Fedora

            * 34

    * SUSE Family

        * openSUSE

            * Tumbleweed

    * Note: other versions are likely to work but have not been tested.

* Java SE Development Kit (JDK)

    * The required JDK version is dependent on the Apache Maven version

        | Maven Version | Minimum JDK Version |
        | ------------: | ------------------: |
        |         3.9.x |                   8 |
        |         3.8.x |                   7 |
        |         3.6.x |                   7 |
        |         3.5.x |                   7 |
        |         3.3.x |                   7 |
        |         3.2.x |                   6 |
        |         3.1.x |                   5 |

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# Maven version number
maven_version: '3.9.4'

# Mirror to download the Maven redistributable package from
maven_mirror: "http://archive.apache.org/dist/maven/maven-{{ maven_version|regex_replace('\\..*', '') }}/{{ maven_version }}/binaries"

# Base installation directory the Maven distribution
maven_install_dir: /opt/maven

# Directory to store files downloaded for Maven installation
maven_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"

# The number of seconds to wait before the Maven download times-out
maven_download_timeout: 10

# Whether to use the proxy when downloading Maven (if the proxy environment variable is present)
maven_use_proxy: true

# Whether to validate HTTPS certificates when downloading Maven
maven_validate_certs: true

# If this is the default installation, symbolic links to mvn and mvnDebug will
# be created in /usr/local/bin
maven_is_default_installation: true

# Name of the group of Ansible facts relating this Maven installation.
#
# Override if you want use this role more than once to install multiple versions
# of Maven.
#
# e.g. maven_fact_group_name: maven_3_3
# would change the Maven home fact to:
# ansible_local.maven_3_2.general.home
maven_fact_group_name: maven
```

### Supported Maven Versions

The following versions of Maven are supported without any additional
configuration (for other versions follow the Advanced Configuration
instructions):

* `3.9.4`
* `3.9.3`
* `3.9.2`
* `3.9.1`
* `3.9.0`
* `3.8.8`
* `3.8.7`
* `3.8.6`
* `3.8.5`
* `3.8.4`
* `3.8.3`
* `3.8.2`
* `3.8.1`
* `3.6.3`
* `3.6.2`
* `3.6.1`
* `3.6.0`
* `3.5.4`
* `3.5.3`
* `3.5.2`
* `3.5.0`
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

Example Playbooks
-----------------

By default this role will install the latest version of Maven supported by this
role:

```yaml
- hosts: servers
  roles:
    - role: gantsign.maven
```

You can install a specific version of Maven by specifying the `maven_version`
(note: if the version is not currently supported by this role then additional
configuration will be required - see
[Advanced Configuration](#advanced-configuration)):

```yaml
- hosts: servers
  roles:
    - role: gantsign.maven
      maven_version: '3.3.9'
```

You can install the multiple versions of Maven by using this role more than
once:

```yaml
- hosts: servers
  roles:
    - role: gantsign.maven
      maven_version: '3.3.9'
      maven_is_default_installation: true
      maven_fact_group_name: maven

    - role: gantsign.maven
      maven_version: '3.2.5'
      maven_is_default_installation: false
      maven_fact_group_name: maven_3_2
```

Role Facts
----------

This role exports the following Ansible facts for use by other roles:

* `ansible_local.maven.general.version`

    * e.g. `3.3.9`

* `ansible_local.maven.general.home`

    * e.g. `/opt/maven/apache-maven-3.3.9`

Overriding `maven_fact_group_name` will change the names of the facts e.g.:

```yaml
maven_fact_group_name: maven_3_2
```

Would change the name of the facts to:

* `ansible_local.maven_3_2.general.version`
* `ansible_local.maven_3_2.general.home`

Related Roles
-------------

You may find the following related roles useful:

* [gantsign.java](https://galaxy.ansible.com/gantsign/java) for installing the
  JDK.

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

This project uses the following tooling:
* [Molecule](http://molecule.readthedocs.io/) for orchestrating test scenarios
* [Testinfra](http://testinfra.readthedocs.io/) for testing the changes on the
  remote
* [pytest](http://docs.pytest.org/) the testing framework
* [Tox](https://tox.wiki/en/latest/) manages Python virtual
  environments for linting and testing
* [pip-tools](https://github.com/jazzband/pip-tools) for managing dependencies

A Visual Studio Code
[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers) is
provided for developing and testing this role.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
