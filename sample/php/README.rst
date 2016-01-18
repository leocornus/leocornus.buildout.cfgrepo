Build the Application Server for PHP
====================================

Basically, this is a CGI to run PHP.
Mostly it is the PHP-FPM at this days.

What will be build?
-------------------

We will build the following things:

- mariadb client
- php-fpm
- php configuration
- php-fpm configuration
- supervisord to manage php-fpm

We will also build a WebServer (Nginx) to testing.
It will have the following functions:

- demostration how the using the php-fpm in Nginx
- show the php info
- test the php-fpm is working fine.
- show stastics  info for php-fpm

How to use it?
--------------

Build Stories
-------------

- build stroy on ubuntu

