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
