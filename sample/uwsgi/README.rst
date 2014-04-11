Buildout samples to build, deploy, and manage applications
running on uWSGI.

Simple Python WSGI Application
==============================

How to build and run a very simple Python WSGI application on uWSGI.

#. create **buildout.cfg** by extends from the 
   **buildout-quickstar.cfg**::

     [buildout]
     extends = 
         buildout-quickstart.cfg
     
     [users]
     uwsgi = youusername
     
     [ports]
     supervisord = 9000
     uwsgi = 9001

     [hosts]
     uwsgi = 127.0.0.1

#. Bootstrap the buildout and execute it::

     $ python bootstrap.py
     $ bin/buildout

#. Start your Python WSGI App by using supervisord::

     $ bin/supervisord
     $ bin/supervisorctl

Reference
=========

- `uWSGI Homepage <http://projects.unbit.it/uwsgi/>`_
- `Supervisord Homepage <http://supervisord.org/>`_
