Setup Git Smart Http on uwsgi
=============================

what we build
-------------

we assume git is install properly.

- uwsgi
- uwsgi cgi plugin
- Nginx
- Nginx config for uwsgi cgi plugin
- Supervisord to manage Nginx and uWSGI cgi plugin

buildout config
---------------

Nginx config
------------

uWSGI config
------------

supervisor config
-----------------

commands memo
-------------

::

  $ bin/buildout -N
  $ sudo bin/supervisord
  $ bin/supervisorctl

location of http-backend
------------------------

- centos: **/usr/libexe/git-core/git-http-backend**
- ubuntu: **/usr/lib/git-core/git-http-backend**

ubuntu memo
-----------

need pcre and ssl library::

  $ aptitude install libpcre3-dev libssl-dev

This post tells every thing: https://www.burgundywall.com/post/nginx-uwsgi-supervisord-git
