Initial Setup Guide
===================

Simple and easy guide to build up things from scratch.

.. contents:: Table of Contents
   :depth: 5

Dependences or Pre-requirement
------------------------------

We assume the following libs are installed in your system:

**MariaDB**

- cmake
- libncurses5-dev libcdk5-dev

Buildout bootstrap
------------------

TODO: we need an instructure for the buildout config files

Steps:

- download cfgrepo
- cd sample/wpmw
- sys link cfgrepo
- vim buildout-local.cfg to change 
- buildout bootstrap
- bin/buildout
- bin/supervisourd

Application initialize
----------------------

configuring applications at first time, Nginx, WordPress, 
MediaWiki, Solr or elasticsearch, etc.

- initilize MariaDB server
- create database and its users
- set up Nginx config for WordPress
- set up wordpress config file.
- TODO: set up mediawiki config file.
- TODO: set up Solr or elasticsearch

**How to make WordPress private**

the my private site plugin: jonradio-private-site

**How to make MediaWiki Private**

The `Preventing_access <https://www.mediawiki.org/wiki/Manual:Preventing_access>`_
page.

Composer to automate
--------------------

How to effectively and efficiently manage plugins and extensions.

We will use composer to manage WordPress plugins and themes.
The buildout config file **php/php-wp-composer.cfg** 
will have details.

How to use composer for MediaWiki extensions and skins.

libs and web components
-----------------------

- php libs
- java libs
- javascript libs
- css libs
- fonts

AJAX Frontend
-------------

- wp-calypso: https://github.com/Automattic/wp-calypso

TODOs
-----

application upgrade process:

- backup, pending the backup list!
- update buildout part **src-versions**
- execute bin/buildout -N
