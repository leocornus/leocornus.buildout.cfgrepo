Zabbix Server Quick Start
-------------------------

Here are the todo checklist:

#. `Compile and Build`_ Zabbix, MariaDB, PHP, Nginx
#. `Init MariaDB Server`_ get ready the MariaDB Server
#. `Init Zabbix Database`_, including dump data
#. `Setup Zabbix Web Interface`_

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
  supervisord = 9500
  mariadb = 9506
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
The **init-mariadb** from file 
`config/db/mariadb-conf.cfg <../../config/db/mariadb-conf.cfg>`_
will install the database server::

  $ bin/buildout -N install init-mariadb

Make sure to read the output information carefully.

Now we can start all apps by using supervisord::

  $ mkdir var/log
  $ sudo bin/supervisord
  $ bin/supervisorctl

The following command will help reset password for **root** db user::

  $ bin/mysqladmin' -u root password 'new-password'
  $ bin/mysqladmin' -u root -h localhost password 'new-password'

Init Zabbix Database
--------------------

now need initialize the database for Zabbix server.

create database and database user::

  create database zabbix character set utf8;
  grant all on zabbix.* to 'zabbix'@'localhost' identified by 'zabbix';
  grant all on zabbix.* to 'zabbix'@'%' identified by 'zabbix';
  flush privileges;

buildout install **zabbix-server-dbinit-mysql**.
If you using Zabbix version 2.0 or higher, you need install
part **zabbix-server-dbinit-mysql-2.0**::

  $ bin/buildout -N install zabbix-server-dbinit-mysql

Setup Zabbix Web Interface
--------------------------

Zabbix come with a simple and easy-to-follow wizard to set up
web interface.
