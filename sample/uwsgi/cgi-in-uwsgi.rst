Running CGI in uWsgi
====================

Quick start to build, config, and run CGI in uWsgi.

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

uwsgi config
------------

uwsgi configuration is very simple::

  # php-cgi.ini
  [uwsgi]
  socket         = 10.0.0.1:8900
  plugin         = cgi
  cgi            = /var/www
  cgi-allowed-ext = .php
  cgi-helper = .php=php-cgi
  
  chdir = %d
  
  post-buffering               = 8192
  
  # start up to 4 but try to stay at 1
  processes                    = 4
  cheaper                      = 1
  
  # lots more customizations possible

Nginx config
------------

Supervisor config
-----------------
