Build Story on Ubuntu
=====================

The stories to build php-fpm on a Unbuntu box.

Dependences
-----------

Confirming the following dependences before build 
will save a lot time.
All of them could be install by using **aptitude**.

Essential build tools:

- build-essential - essential build tools.

MariaDB dependences:

- cmake - mariadb is uing cmake for building.
- ncurses, ncurses-dev - mariadb dependence

PHP dependences or extensions:

- libxml2, libxml2-dev
- openssl
- libcurl4-openssl-dev - OpenSSL dev package is in this package.
- libbz2, libbz2-dev
- libjpeg, libjpeg-dev
- libpng, libpng-dev
- libgd2, libgd2-dev
- libmcrypt, libmcrypt-dev
- freetype-devel, libfreetype-dev (Ubuntu)
- gettext

command line sample::

  $ sudo aptitude install libbz2-dev libxml2-dev gettext
  $ sudo aptitude install libjpeg-dev libpng-dev libgd2-dev 
  $ sudo aptitude install libmcrypt-dev libfreetype6-dev
  $ sudo aptitude install libcurl4-openssl-dev
