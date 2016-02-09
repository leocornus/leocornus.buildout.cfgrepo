`Back to README <README.rst>`_ >
Running CGI on uWSGI

Quick start to build, config, and run CGI in uWSGI
Mainly reference to `Running CGI scripts on uWSGI <http://uwsgi-docs.readthedocs.org/en/latest/CGI.html>`_.

What we build
-------------

this quick start will build the following things:

- build uwsgi
- build uwsgi cgi plugin
- php cgi to test the uwsgi cgi plugin
- uwsgi configuration
- build nginx web server
- generate config for nginx virtual host server
- build supervisord
- generate supversor config file to manage Nginx and uWsgi cgi

buildout config
---------------

It is very easy to create a **buildout.cfg** file by simply extends
the `buildout-quickstart-cgi.cfg <buildout-quickstart-cgi.cfg>`_.

Here is the buildout file::

  ####################
  # buildout config file to set
  #  - running user
  #  - ips, ports
  #
  [buildout]
  extends = 
      buildout-quickstart-cgi.cfg
  
  [users]
  nginx = nginx
  uwsgi = nginx
  
  [ports]
  supervisord = 8909
  nginx = 8980
  uwsgi = 8900
  uwsgi-stats = 8901
  
  [hosts]
  uwsgi = 10.1.1.111
  frontend-ip = 10.1.1.111
  frontend-hostname = 10.1.1.111

uwsgi config
------------

Minium uwsgi configuration is very simple::

  # php-cgi.ini
  [uwsgi]
  socket         = 10.0.0.1:8900
  plugin         = cgi
  cgi            = /var/www
  cgi-allowed-ext = .php
  cgi-helper = .php=php-cgi
  
Nginx config
------------

configuration for Nginx web server.::

  location ~ \.php$ {
      root ${:document-root};
      include ${nginx-build:location}/conf/uwsgi_params;
      # uwsgi cgi using modifier1 as 9
      uwsgi_modifier1 9;
      uwsgi_pass ${hosts:uwsgi}:${ports:uwsgi};
  }

Supervisor config
-----------------

Supervisor program for uwsgi-cgi is as simple as following::

  [program:uwsgi-cgi]
  command = /path/to/bin/uwsgi --ini /path/to/uwsgi-cgi.ini
  process_name = uwsgi-cgi
  user = uwsgi
