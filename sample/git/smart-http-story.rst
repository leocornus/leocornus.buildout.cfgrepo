Config Git on Smart HTTP
========================

Some facts.

- Git 1.6.6 inroduced the Smart HTTP protocol for Git server.
- http-backend is implemented as a CGI script.
- http-backend could be found in folder /usr/lib/git-core 
  or /usr/libexec/git-core

Basic Auth
----------

ngx_postgres module: https://github.com/FRiCKLE/ngx_postgres

options
-------

#. using Nginx default auth-basic, generate the htpasswd by using
   the current FTP credential.
#. using the ngx_postgres module for Nginx

Set up Git over Nginx
---------------------

Specs:

- http port 8022
- htpasswd
- multiple git repos

Dependence:

we need a fastcgi to execute the **git-http-backend** script.
the simple choice will be **fcgiwrap**.

Create Git Repo
'''''''''''''''

Following these commands to create a git bare repository on git server::

  $ git init --bare /usr/rd/git-repos/first.git
  $ cd /usr/rd/git-repos/first.git
  $ git config core.sharedrepository true
  $ git config http.receivepack true

we need configure the repo to receive pack.

fcgiwrap
''''''''

install fcgiwrap and run it as service.
Once installed, we could run it using the following command::

  $ fcgiwrap -s tcp:10.1.1.111:9022

Create htpasswd
'''''''''''''''

using apache htpasswd to create user name and password::

  $ htpass -bc test.pass seanchen mygitpassword

Nginx Config
''''''''''''

Here is the config file for Nginx server::

  server {
  
      listen 8022;
      server_name my.git.repo.com:8022;
  
      error_log /usr/git/http/log/frontend-error.log debug;
      access_log /usr/git/http/log/frontend-access.log;
  
      #root /usr/git/repos/www;
      #index index.php;
  
      location ~ /git(/.)* {
  
          client_max_body_size 0;
  
          auth_basic "git anonymous read-only, authenticated write";  
          auth_basic_user_file /usr/git/http/conf/htpasswd; # OR path/to/htpasswd  
  
          fastcgi_split_path_info ^(.*/git)(/.*)$;
  
          fastcgi_param DOCUMENT_ROOT /usr/lib/git-core/;
          fastcgi_param PATH_INFO $fastcgi_path_info;
          fastcgi_param SCRIPT_FILENAME /usr/lib/git-core/git-http-backend;
          fastcgi_param GIT_HTTP_EXPORT_ALL "";
          fastcgi_param GIT_PROJECT_ROOT /usr/rd/git-repos/;
          #include /etc/nginx/fastcgi_params;
  
          #fastcgi_pass unix:/var/run/fcgiwrap.socket;
          #fastcgi_pass phpfpm56;
          fastcgi_pass 10.1.1.111:9022;
      }
  }

clone over http
---------------

Now we can clone the repo over HTTP::

  $ git clone http://my.git.repo.com:8022/git/first.git
  $ cd first
  $ touch README.rst
  $ git add README.rst
  $ git commit . -m 'first commit'
  $ git push origin master

