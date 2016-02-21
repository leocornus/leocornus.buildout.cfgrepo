WordPress and MediaWiki Story
=============================

This story will try to:

- build both WordPress and MediaWiki
- config them so they could work together seamlessly

What we build
-------------

We will build the software infrastructure:

- Nginx
- php-fpm
- MariaDB
- Node.js / Parsoid
- Java / Tomcat / elastic
- supervisord or circus

And install and configure the following frameworks:

- WordPress multi-side mode
- Parsoid service on Node.js
- Elasticsearch
- MediaWiki over WordPress authentication.

Quick start
-----------

simple commans to get started::

  $ python bootstrap.py
  $ bin/buildout -N
  $ bin/supervisord

visit http://localhost

Buildout config
---------------

buildout config for software infrastructure::

  buildout-db.cfg
  buildout-php.cfg
  buildout-nodejs.cfg
  buildout-nginx.cfg
  buildout-java.cfg
  buildout-python.cfg
  buildout-local.cfg
  buildout.cfg

buildout config for applications::

  buildout-php-apps.cfg

Dependences
-----------

MariaDB:

  - cmake
  - libncurses5-dev, libcdk5-dev
