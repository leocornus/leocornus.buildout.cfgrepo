Quickly set up LNMP as a sample.
It will cover the following components:

* Nginx as Web Server
* MariaDB database
* PHP-FPM through FastCGI
* Python through WSGI
* Supervisord

Step by Step
============

0. Make sure all the dependences libs / packages are installed.
   Check the following dependeces section for details.
1. get the bootstrap.py::

   $ wget http://svn.zope.org/*checkout*/zc.buildout/trunk/bootstrap/bootstrap.py

2. link leocornus cfgrepo::

   $ ln -s /PATH/TO/leocornus.buildout.cfgrepo

3. start buildout.cfg::

   $ vim buildout.cfg

4. the buildout.cfg could be as simple as just 2 lines::

   [buildout]
   # extends from the base buildout config.
   extends = buildout-base.cfg
   
   # tweak the setting for different environment, for example:
   # - development server
   # - local desktop
   # - stage server
   # - production server

5. execute the bootstrap.py::

   $ python bootstrap.py

6. execute buildout::

   $ bin/buildout

7. FINGER CROSS...
8. Create the log folder::

   $ mkdir var/log

9. Create the php info page::

   $  mkdir var/www
   $  touch var/www/index.php
   $  vim var/www/index.php

   <?php
   phpinfo();

MariaDB Dependences
===================

MariaDB 5.5 requirs CMake to build from source code.
Make sure the CMake is installed in your system.

* CMake
* curses lib: ncurses, ncurses-dev, cdk, cdk-devel
 
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

Here is yum command for CentOS::

  $ sudo yum install bzip2-devel libjpeg-devel openssl-devel \
  > libxml2-devel libpng-devel libmcrypt-devel freetype-devel gettext

Nginx Dependences
=================

Nginx depends on the following libs and packages:

* PCRE for re-write module: libpcre3-dev
