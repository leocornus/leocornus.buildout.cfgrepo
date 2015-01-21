How to Build and Config Zabbix
------------------------------

- Zabbix Overview
- Zabbix Server Requirement and Capacity
- Init Scripts for Zabbix Server
- Init Scripts for Zabbix Agent
- Zabbix Server Web Interface and APIs

Stories
-------

- Zabbix Server Quick Start
- `Zabbix Agent quick Start <Zabbix-Agent-Story.rst>`_
- `Zabbix Server Story Including Web Interface 
  <Zabbix-Server-Story.rst>`_

Special Features
----------------

- Log File Monitoring: Monitoring and analyzing log files.
- Web Monitoring...

Overview
--------

Zabbix_ is the Enterprise-class Monitoring Solution for Everyone.

Requirement and Hardware Configuration
--------------------------------------

Roughly, dual core CPU with 2GB memory could monitor upto 500 hosts.

Init Scripts
------------

Both Zabbix Server and Agent could only run as daemon.
We could NOT manage them through Supervisor_.

.. _Zabbix: http://www.zabbix.com
.. _Supervisor: http://supervisord.org
