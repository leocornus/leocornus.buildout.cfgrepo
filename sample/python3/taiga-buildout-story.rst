Buildout Story for taiga-back
==========================================================

taiga-back is maily a Django application.
Buildout is a very efficient tool to manage a Django application.

Benifit
-------

- automated development process the most.
- buildout is born for Python app,
- 

proposal
--------

- create **buildout** folder.
- phase by phase roll out features.

Basic features
--------------

- install dependence eggs
- generate taiga-back script as Django manage script
- install and setup PostgreSQL database.
- load testing data.
- generate various scripts: test, 
- install and config circus

Frontend development
--------------------

Possibly automate the frontend development.

- FRONTEND: install and config Nginx
- FRONTEND: install and config Node.js and npm
- 

First Cut
---------

As to now, supervisor doesn't support Python 3.
So we have to use circus to manage processes.

As cut, we will only have the following on board:

- install PostgreSQL database
- setup PostgreSQL database for taiga-back: create database and 
  user
- create easier Django manage scripts.

PostgreSQL admin
----------------

:Start PostgreSQL Server:
    $ parts/postgresql-build/bin/pg_ctl start -D var/postgresql/taiga
:Stop PostgreSQL Server:
    $ parts/postgresql-build/bin/pg_ctl stop -D var/postgresql/taiga
:SQL client:
    $ parts/postgresql-build/bin/psql taiga

Steps
-----

Steps to get started.
get ready the buildout.cfg

:python3.4 bootstrap.py:
    bootstrap buildout.
:bin/buildout:
    execute buildout to compile and install PostgreSQL database
    server and the Django manage script **bin/taiga-back**
:bin/buildout -N install init-postgresql:
    this will initialize postgreSQL database for taiga-back.
:bin/buildout -N:
    this will update the config file for PostgreSQL
:bin/buildout -N install generat-scripts:
    generate scripts for PostgreSQL admin.
:bin/start-postmaster:
    Start the PostgreSQL database server
:bin/buildout -N install create-taiga-db:
    create taiga database and database user.
:bin/buildout -N install pop-demo-data:
    populate demo data.
:bin/taiga-back runserver:
    start taiga-back service, to specify ip and port:
    **bin/taiga-back runserver 10.1.1.1:9000**.

**TODO**

- generate script for all those
