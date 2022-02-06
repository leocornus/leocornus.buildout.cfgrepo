Build and configure PHP
=======================

The php folder will save all configurations related to a PHP application

Here is a quick list of the things that we covered:

- php-fpm language
- Zend configration
- WordPress configuration
- MediaWiki config

Dependences
-----------

PHP depends on the following libs:

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

Ubuntu story
''''''''''''

sptitude install memo::

  sudo aptitude install libbz2-dev libxml2-dev gettext
  sudo aptitude install libjpeg-dev libpng-dev libgd2-dev 
  sudo aptitude install libmcrypt-dev libfreetype6-dev
  sudo aptitude install libcurl4-openssl-dev libpcre3-dev

Referenc this Dockerfile:
- https://github.com/docker-library/php/blob/master/7.4/buster/fpm/Dockerfile

quick installation::

  sudo apt install libpcre3-dev zlib1g-dev libxml2-dev openssl libcurl4-openssl-dev libssl-dev sqlite3 libsqlite3-dev libbz2-dev lbzip2 pkg-config libonig-dev make autoconf dpkg-dev libc-dev re2c ca-certificates xz-utils
