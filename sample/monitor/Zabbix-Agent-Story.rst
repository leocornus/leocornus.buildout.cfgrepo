`Build and Config Zabbix Service <How-to-Build-Config-Zabbix.rst>`_
> Zabbix Agent Story

Zabbix Agent Quick Start
------------------------

- `Compile and Build`_ Zabbix Agent
- `Zabbix Agent Configuration File`_
- Run Agent

Compile and Build
-----------------

The base buildout file `<buildout-zabbix-agent.cfg>`_ 
has everything we need to compile and build Zabbix agent.
Create a **buildout.cfg** file and extends it::

  [buildout]
  extends =
      buildout-zabbix-agent.cfg
  
  [zabbix-agentd-conf]
  server-ip = 10.1.1.1
  hostname = myhostname

And then execute the following commands::

  $ python bootstrap.py
  $ mkdir downloads
  $ bin/buildout
