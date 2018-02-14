# Ansible Role apache2

This role installs and configures apache2, a commonly known webserver.


# Example play

```yaml
- hosts: dm.public-debian.vagrant
  vars:
    apache2_enabled: yes
    apache2_enable_modules:
      - rewrite
      - ssl
  roles:
    - blunix.role-apache2
```

# License

Apache-2.0

# Author Information

Service and support for orchestrated hosting environments,
continuous integration/deployment/delivery and various Linux
and open-source technology stacks are available from:

```
Blunix GmbH - Consulting for Linux Hosting 24/7
Glogauer Straße 21
10999 Berlin - Germany

Web: www.blunix.org
Email: service[at]blunix.org
Phone: (+49) 30 / 12 08 39 90
```
