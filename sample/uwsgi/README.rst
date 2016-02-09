Buildout samples to build, deploy, and manage applications
running on uWSGI.

- `Build, Deploy, Init and Run Trac Projects`_
- `Simple Python WSGI Application`_
- `Trac on PostgreSQL on uWSGI <Trac-on-PostgreSQL-in-uWSGI.rst>`_
- `CGI on uWSGI <cgi-in-uwsgi.rst>`_
- `PHP on uWSGI <PHP-in-uWSGI.rst>`_

Build, Deploy, Init and Run Trac Projects
-----------------------------------------

Following the simple steps, 
you will have a Trac project up and running in minutes.

#. create **buildout.cfg** by extends from the 
   **buildout-trac.cfg**::

     [buildout]
     extends = 
         buildout-trac.cfg

     [trac-wsgi-bin]
     trac-project-dir = ${buildout:directory}/var/trac-projects

     [users]
     uwsgi = your_local_account

     [ports]
     supervisord = 8909
     uwsgi = 8910

     [hosts]
     uwsgi = 10.10.10.1

#. Bootstrap the buildout and execute it::

     $ python bootstrap.py
     $ bin/buildout

#. Now you can create you first Trac project using the following 
   command::

     $ bin/trac-admin var/trac-projects/traconuwsgi initenv \
     > 'Trac on uWSGI' sqlite:db/trac.db

#. Start supervisord::

     $ bin/supervisord
     $ bin/supervisorctl
     trac-on-uwsgi        RUNNING    pid 14940, uptime 0:11:45
     supervisor>

Simple Python WSGI Application
------------------------------

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
---------

- `uWSGI Homepage <http://projects.unbit.it/uwsgi/>`_
- `Supervisord Homepage <http://supervisord.org/>`_
- `You Should Be Using Nginx + UWSGI <http://cramer.io/2013/06/27/serving-python-web-applications/>`_
