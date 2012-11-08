
Quickly set up LNMP as a sample.
It will cover the following components:

* Nginx as Web Server
* MySQL database
* PHP-FPM through FastCGI
* Python through WSGI
* Supervisord

Step by Step
============

1. get the bootstrap.py
   wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py
2. link leocornus cfgrepo
   ln -s /PATH/TO/leocornus.buildout.cfgrepo
3. start buildout.cfg
   vim buildout.cfg

MySQL Dependences
=================

MySQL 5.5 requirs CMake to build from source code.
Make sure the CMake is installed in your system.

* CMake
* curses lib: ncurses-dev,
  
PHP Dependences
===============

We need have the following lib installed in the system.

* libxml2, libxml2-dev
* openssl, openssl-dev
* libbz2, libbz2-dev
* libjpeg, libjpeg-dev
* libpng, libpng-dev
* libgd2, libgd2-dev
* libmcrypt, libmcrypt-dev
* freetype-devel, libfreetype-dev (Ubuntu)
* gettext

For Ubuntu, there is NO openssl-dev package.
We have to install libcurl4-openssl-dev instead.

Nginx Dependences
=================

Nginx depends on the following libs and packages:

* PCRE for re-write module: libpcre3-dev
