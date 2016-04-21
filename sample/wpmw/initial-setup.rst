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
- set up Nginx config
- set up wordpress config file.
- TODO: set up mediawiki config file.
- TODO: set up Solr or elasticsearch

plugins and extensions
----------------------

How to effectively and efficiently manage plugins and extensions.

Themes and skins
----------------

Same question, how to manage themes and skins.

libs and web components
-----------------------

- php libs
- java libs
- javascript libs
- css libs
- fonts

TODOs
-----

application upgrade process:

- backup, pending the backup list!
- update buildout part **src-versions**
- execute bin/buildout -N
