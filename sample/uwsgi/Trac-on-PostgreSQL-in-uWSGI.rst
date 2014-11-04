`Back to README <README.rst>`_ >
Running Trac on PostgreSQL in uWSGI

Steps
-----

#. create build by extending `buildout-trac-postgres.cfg <buildout-trac-postgres.cfg>`_
#. update users, ports, hosts
#. bootstrap buildout execute buildout
#. set datadir for postgresql
#. buildout install init-postgresql
#. execute buildout again to regenerate the postgresql.conf
#. start database server by using supervisord
#. create user for trac
#. create database fro trac
#. grant privileges
#. adding python binding for PostgreSQL database
#. trac-admin initenv

ceate-user-sql:: 

  create user trac with password 'tracpassword';
  create database trac;
  grant all privileges on database trac to trac;

this simple way to connect from remote client
new line in file pg_hba.conf
need restart postgresql after added this line::

  host trac trac 0.0.0.0/0 password


buildout config
---------------

Here is the complete **buildout.cfg** file::

  ####################
  # focus on what we need for build Trac on PostgreSQL
  #
  [buildout]
  extends = 
      buildout-trac-postgres.cfg

  parts += 
      python-interpreter

  [users]
  uwsgi = uwsgi 
  postgresql = uwsgi 
  
  [python-interpreter]
  recipe = zc.recipe.egg
  interpreter = python
  eggs = ${buildout:eggs}
  
  [ports]
  supervisord = 8909
  postgresql = 5432
  
  [hosts]
  uwsgi = 10.10.10.10
  postgresql-ip = 10.10.10.10
  
  [init-postgresql]
  datadir = ${buildout:directory}/var/postgresql/trac
  
  [postgresql-conf]
  datadir = ${buildout:directory}/var/postgresql/trac

Reference
---------

- `comprehensive buildout sample <http://svn.zope.org/zodbshootout/trunk/buildout.cfg?view=markup&pathrev=105749>`_
