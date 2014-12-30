
Zabbix Server Quick Start
-------------------------

**get ready buildout.cfg**

Most of the details buildout parts are in the base config file
`<buildout-zabbix-server.cfg>`_.
The **buildout.cfg** file will only have the local

  [buildout]
  extends =
      buildout-zabbix-server.cfg

  [users]
  nginx = nginx
  php-fpm = fpm
  mariadb = mariadb

  [ports]
  mariadb = 9500
  nginx = 9580
  php-fpm = 9510
  zabbix-web = 9583

  [hosts]
  zabbix-web-ip = 127.0.0.1
  zabbix-web-host = 127.0.0.1

run the following commands::

  $ python bootstrap.py
  $ mkdir downloads
  $ bin/buildout
