Buildout Story for taiga-back
=============================

taiga-back is mainly a Django application.
Buildout is a very efficient tool to manage a Django application.

.. contents:: Table of Contents
    :depth: 5

Benifit
-------

- Buildout is born for Python app and is good at manage Django apps.
- Buildout will help automate development process the most.
- buildout extension mr.developer_ is the best tool to manage pypi
  packages for a large project. 
  taiga-back depends on a lot packages.

Proposal
--------

As the initiative, we will get started with:

- create **taiga-contrib-buildout** git repo.
- phase by phase roll out features.

Basic features for First Cut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As first cut, we will only have the following on board:

- install dependence eggs
- generate taiga-back script as Django manage script
- install and setup PostgreSQL database.
- create database and user for taiga-back, load sample data.
- generate various scripts: test, PostgreSQL admin, etc.

Frontend development
~~~~~~~~~~~~~~~~~~~~

Possibly automate the frontend development too.

- FRONTEND: install and config Nginx
- FRONTEND: install and config Node.js and npm
- automate frontend test 

Steps to Get Started
--------------------

Steps to get started.

#. create buildout folder::

    $ mkdir taigaio
    $ cd taigaio

#. clone cfgrepo_ repo to cfgrepo folder::

    $ git clone https://github.com/leocornus/leocornus.buildout.cfgrepo.git cfgrepo

#. clone taiga-back_ repo to taiga_back folder::

    $ git clone https://github.com/taigaio/taiga-back.git

#. clone django-pglocks_ repos to src folder, as taiga-back needs
   the master branch::

    $ mkdir src
    $ cd src
    $ git clone  https://github.com/Xof/django-pglocks.git

#. Get ready the bootstrap.py, buildout-taiga.cfg_, and buildout.cfg_::

    $ cd ..    # get back to buildout folder.
    $ cp cfgrepo/sample/python3/bootstrap.py .
    $ cp cfgrepo/sample/python3/buildout-taiga.cfg .
    $ cp cfgrepo/sample/python3/buildout.cfg .

#. Optional: update buildout.cfg for PostgreSQL server's listen IP 
   and port. The whole buildout.cfg looks like this::

    [buildout]
    extends =
        buildout-taiga.cfg

    [users]
    postgresql = ubunbu

    [ports]
    postgresql = 5432

    [hosts]
    postgresql-ip = 127.0.0.1

#. execute the following commands.

:python3.4 bootstrap.py:
    bootstrap buildout.
:bin/buildout:
    execute buildout to compile and install PostgreSQL database
    server and the Django manage script **bin/taiga-back**
:rm var/postgresql/taiga/postgresql.conf:
    Empty the PostgreSQL data directory.
:bin/buildout -N install init-postgresql:
    this will initialize postgreSQL database for taiga-back.
:bin/buildout -N:
    this will update the config file for PostgreSQL
:bin/pg_ctl start -D var/postgresql/taiga:
    Start the PostgreSQL database server
:bin/buildout -N install create-taiga-db:
    create taiga database and database user.
:bin/buildout -N install populate-sample-data:
    populate demo data.
:bin/taiga-back runserver:
    start taiga-back service, to specify ip and port:
    **bin/taiga-back runserver 10.1.1.1:9000**.

What's been built
~~~~~~~~~~~~~~~~~

Here is a list of things built by buildout.

:parts/postgresql-build:
    the PostgreSQL database server
:var/postgresql/taiga:
    PostgreSQL database data directory for taiga-back
:bin/taiga-back:
    The Django manage script for taiga-back

TODO
----

- introduce circus to manage all process for development, including
  PostgreSQL, Nginx, gunicorn, etc.
- introduce mr.developer_ to manage packages.

PostgreSQL admin
----------------

a quick memo for PostgreSQL admin

:Start PostgreSQL Server:
    $ bin/pg_ctl start -D var/postgresql/taiga
:Stop PostgreSQL Server:
    $ bin/pg_ctl stop -D var/postgresql/taiga
:Check PostgreSQL Server:
    $ bin/pg_ctl status -D var/postgresql/taiga
:SQL client:
    $ bin/psql taiga

.. _mr.developer: https://pypi.python.org/pypi/mr.developer
.. _cfgrepo: https://github.com/leocornus/leocornus.buildout.cfgrepo
.. _taiga-back: https://github.com/seanchen/taiga-back
.. _django-pglocks: https://github.com/Xof/django-pglocks
.. _buildout-taiga.cfg: buildout-taiga.cfg
.. _buildout.cfg: buildout.cfg
