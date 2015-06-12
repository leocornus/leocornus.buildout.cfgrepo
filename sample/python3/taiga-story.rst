Taiga Story
===========

Try to set up development environment for Taiga,
both backend and frontend.

Dependences
-----------

Taiga depends on the following softwares:

- Python >= 3.4
- PostgreSQL >= 9.3
- Django > 1.7
- Circus or Supervisord, circus is better as Supervisord 
  is not working on Python 3 until version 4.0

Setup Steps
-----------

#. create buildout config file by extending `buildout-taiga.cfg
   <buildout-taiga.cfg>`_
#. update users, ports, hosts 
#. install part **init-postgresql** to create database.

Command Memo
------------


