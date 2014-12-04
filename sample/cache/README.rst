Some buildout samples around cache servers.

Lists of cases
--------------

- `buildout-base.cfg <buildout-base.cfg>`_ provides the very basic
  buildout parts to build the redis_ server, generate the server
  config file, and manage the server under supervisor_.

- `buildout-memcached-base.cfg <buildout-memcached-base.cfg>`_ 
  provides the very basic config file for memcached_.

- `buildout-php.cfg <buildout-php.cfg>`_ build the redis_ ready PHP
  on Nginx and managed by supervisor_.

Stories
-------

- `memcached story <memcached-story.rst>`_

References
----------

- `How to use memcached in MediaWiki 
  <https://www.mediawiki.org/wiki/Memcached>`_

.. _redis: http://redis.io
.. _memcached: http://memcached.org/
.. _supervisor: https://github.com/Supervisor/supervisor
