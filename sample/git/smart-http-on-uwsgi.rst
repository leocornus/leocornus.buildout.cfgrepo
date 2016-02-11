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

Quick start
-----------

simple commands::

  $ python bootstrap.py
  $ bin/buildout -N
  $ bin/supervisord

then we could clode git repos on url http://10.160.192.88:8980/git.

buildout config
---------------

the base buildout config file is in file `buildout-git-on-uwsgi.cfg
<buildout-git-on-uwsgi.cfg>`_.
The following the buildout.cfg to set running users, ips, and ports::

  ####################
  # buildout config file to set
  #  - running user
  #  - ips, ports
  #
  [buildout]
  extends =
      buildout-git-on-uwsgi.cfg
  
  [users]
  nginx = ubuntu
  uwsgi = ubuntu
  
  [ports]
  supervisord = 8909
  nginx = 8980
  uwsgi = 8900
  uwsgi-stats = 8901
  
  [hosts]
  uwsgi = 10.160.192.88
  frontend-ip = 10.160.192.88
  frontend-hostname = 10.160.192.88

Nginx config
------------

this example is config git repository in **/git** uri::

  location ~ /git(/.*) {

      client_max_body_size 0;

      #limit_except GET HEAD {
      #    # authenticate for post (write) only.
      #    auth_basic "authenticated write";
      #    auth_basic_user_file /path/to/htpasswd;
      #}

      #fastcgi_split_path_info ^(.*/git)(/.*)$;

      # load uwsgi params first
      include ${nginx-build:location}/conf/uwsgi_params;
      #uwsgi_param DOCUMENT_ROOT /usr/libexe/git-core/;
      # overwrite the path info.
      uwsgi_param PATH_INFO $1;
      uwsgi_param GIT_HTTP_EXPORT_ALL "";
      uwsgi_param REMOTE_USER $remote_user;
      uwsgi_param GIT_PROJECT_ROOT ${:git-project-root};

      # has to set to 9
      uwsgi_modifier1 9;
      uwsgi_pass ${hosts:uwsgi}:${ports:uwsgi};
  }

uWSGI config
------------

The simple uWSGI config to have up to 4 processes and keep 1 stay
alive::

  # uwsgi-git.ini
  [uwsgi]
  socket = ${hosts:uwsgi}:${ports:uwsgi}
  plugin = cgi
  cgi = ${:git-http-backend-path}
  chdir = %d
  # in what? MB, KB?
  post-buffering = 8192
  # start up to 4 but try to stay at 1
  processes = 4
  cheaper = 1

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

  $ aptitude install libpcre3-dev libssl-dev python-dev

This post tells every thing: https://www.burgundywall.com/post/nginx-uwsgi-supervisord-git
