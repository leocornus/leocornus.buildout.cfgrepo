`Back to README <README.rst>`_ >
Build and Run PHP Scripts on uWSGI

The full details documentation could be found 
`Running PHP scripts in uWSGI <http://uwsgi-docs.readthedocs.org/en/latest/PHP.html>`_.

What we build?
--------------

Here are things we are building:

- builc embed enabled php
- build uwsgi
- build uwsgi php plugin
- uwsgi configuration for php plugin
- build Nginx web server
- generate config for nginx virtual host server
- build supervisord
- generate supversor config file to manage Nginx and uWsgi php

embed php
---------

PHP need enable option **--enable-embed** during compile and build.
Once build success, you should see the following output,
when execute **php-config**::

  $ ${php-build:location}/bin/php-config --php-sapis
  cli embed fpm cgi

buildout.cfg
------------

It is very easy to create a **buildout.cfg** file by simply extends
the `buildout-php-in-uwsgi.cfg <buildout-php-in-uwsgi.cfg>`_.

Here is the whole buildout config file::

  ####################
  # buildout config file to set
  #  - running user
  #  - ips, ports
  #
  [buildout]
  extends = 
      buildout-php-in-uwsgi.cfg
  
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

Nginx Config
------------

configuration for Nginx web server.::

  location ~ \.php$ {
      root ${:document-root};
      include ${nginx-build:location}/conf/uwsgi_params;
      # uwsgi php plugin using modifier1 as 14 
      uwsgi_modifier1 14;
      uwsgi_pass ${hosts:uwsgi}:${ports:uwsgi};
  }

uWSGI config
------------

Here is he config to run uwsgi-php from comamnd line::

  [program:uwsgi-php]
  command = /path/to/bin/uwsgi --plugin php --socket 10.1.1.2:8900 --master --processes 4 --cheaper 2

Here is a ini config file for uwsgi php plugin::

  # uwsgi-php.ini
  [uwsgi]
  socket = 10.1.1.2:8900
  plugin = php
  # using master process.
  master = true
  # max 4 threads / processes
  processes = 4
  # keep 2 processes live
  cheaper = 2
  # turn on the stats.
  stats = 10.1.1.2:8901

Challenges
----------

We need explore new ways to build uWSGI and its plugins.

The simple way to build php_plugin.
::

  $ python uwsgiconfig.py --plugin plugins/php

- `Rumming anything on Nginx with uWSGI <http://metz.gehn.net/2013/02/running-anything-on-nginx-with-uwsgi/>`_ 
