
Zabbix Server Quick Start
-------------------------

Here are the todo checklist:

#. `Compile and Build`_ Zabbix, MariaDB, PHP, Nginx
#. `Init MariaDB Server`_ get ready the MariaDB Server
#. `Init Zabbix Database`_, including dump data
#. configuration tweak for the Zabbix Web Interface.

Compile and Build
-----------------

**get ready buildout.cfg**

Most of the details buildout parts are in the base config file
`<buildout-zabbix-server.cfg>`_.
The **buildout.cfg** file will only have the params for your
local environment.
Here is a sample buildout.cfg::

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
  zabbix-server = 10051
  zabbix-web = 9583

  [hosts]
  zabbix-server-ip = 0.0.0.0
  zabbix-web-ip = 127.0.0.1
  zabbix-web-host = 127.0.0.1
  mariadb-ip = 127.0.0.1

run the following commands to compile and build::

  $ python bootstrap.py
  $ mkdir downloads
  $ bin/buildout

Init MariaDB Server
-------------------

MariaDB buildout config has a set of parts to initialize a 
MariaDB Server. 

Init Zabbix Database
--------------------

now need initialize the database for Zabbix server::
