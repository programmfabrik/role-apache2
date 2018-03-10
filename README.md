# Ansible Role apache2

This role installs and configures apache2, a commonly known webserver.


# Example play

```yaml
- hosts: dm.public-debian.vagrant
  become: yes
  vars:
    # role apache2
    apache2_enabled: yes
    apache2_enable_vhosts:
      - default
    apache2_disable_vhosts:
      - default-ssl
    apache_default_vhost_redirect_destination: 'https://www.example.com'
    apache2_module_packages_installed:
      - apache2-utils
      #- libapache2-mpm-event TODO
      - libapache2-modsecurity
      - libapache2-mod-evasive
      - libapache2-mod-fcgid
    apache2_module_packages_removed: []
    apache2_enable_modules:
      - actions
      - expires
      - setenvif
      - rewrite
      - ssl
      - alias
      - authz_core
      - mpm_event
      - security2
      - headers
      - cgid
      - proxy
      - proxy_http
      - proxy_fcgi
      - deflate
    apache2_disable_modules:
      - evasive
      - mpm_prefork
      - autoindex
      - ssl

  roles:
    - blunix.role-apache2

  tasks:

    - name: template the www.example.com Vhost
      template:
        src: "templates/etc/apache2/sites-available/www.example.com.conf.j2"
        dest: "/etc/apache2/sites-available/www.example.com.conf"
        owner: root
        group: root
        mode: 0600
      notify: restart apache2

    - name: enable the www.example.com.conf Vhost
      command: "a2ensite www.example.com"
      args:
        creates: "/etc/apache2/sites-enabled/www.example.com.conf"
      notify: restart apache2

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
