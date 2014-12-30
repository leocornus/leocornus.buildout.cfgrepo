Samples for build and config monitoring services
------------------------------------------------

Here are list of monitoring applications:

- Zabbix_

Zabbix Monitoring
-----------------

We need the following components for Zabbix monitoring service:

- MariaDB
- Nginx_ as the Web Server for Zabbix_ web interface
- PHP for Zabbix_ web interface, which also provides RESTful APIs.
- Supervisord to manage Nginx_, php-fpm, and MariaDB

Check the `Zabbix Quick Start Guide<How-to-Build-Config-Zabbix.rst>`_
to build Zabbix_ server in half hour.

.. _Zabbix: http://zabbix.com
.. _Nginx: http://nginx.org
