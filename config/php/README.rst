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

  $ sudo aptitude install libbz2-dev libxml2-dev gettext
  $ sudo aptitude install libjpeg-dev libpng-dev libgd2-dev 
  $ sudo aptitude install libmcrypt-dev libfreetype6-dev
  $ sudo aptitude install libcurl4-openssl-dev libpcre3-dev
