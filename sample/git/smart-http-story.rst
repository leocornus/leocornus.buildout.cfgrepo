Config Git on Smart HTTP
========================

Some facts.

- Git 1.6.6 inroduced the Smart HTTP protocol for Git server.
- http-backend is implemented as a CGI script.
- http-backend could be found in folder **/usr/lib/git-core** 
  or **/usr/libexec/git-core**.

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

Following these commands to create a git bare repository 
on git server::

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

  $ htpasswd -bc git.htpasswd seanchen mygitpassword

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
          auth_basic_user_file /usr/git/http/conf/git.htpasswd; # OR path/to/htpasswd  
  
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

Now we can clone the repo over HTTP and the 
initial commit.::

  $ git clone http://my.git.repo.com:8022/git/first.git
  $ cd first
  $ touch README.rst
  $ git add README.rst
  $ git commit . -m 'first commit'
  $ git push origin master

save password over http
-----------------------

We could save the git password localy to make life easier.
The **credential.helper** config option will be set to store::

  $ git config credential.helper store

There will be a file in user's home folder to store the username
and password.
The file name will be **~\.git-credentials**.

Use PHP to generate the htpasswd file
-------------------------------------

Apache has the tool **htpasswd** to generate passowrd.
By default htpasswd is using CRYPT encryption for password.
PHP has a crypt function to encrypt password.

Apahce `Password Formats <http://httpd.apache.org/docs/2.2/misc/password_encryptions.html>`_
has good documentation.
Here is some samples::

  <?php
  // Password to be used for the user
  $username = 'user1';
  $password = 'password1';
   
  // Encrypt password
  $encrypted_password = crypt($password, base64_encode($password));
