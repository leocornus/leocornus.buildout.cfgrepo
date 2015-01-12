`Cache Samples <README.rst>`_ > Memcached Story

Memcached_ has been widely used in many high profile websites,
including Facebook, YouTube, Wikipedia, etc.
`Memcached on Wikipedia`_ has many details.

The `Hardware Considerations`_ has many good practice about
how to deploy your Memcached_ services.

Some Tools
----------

**telnet**

Using telnet is the simplest way to 
check your Memcached_ installation.
Here is a quick sample::

  $ telnet 127.0.0.1 11211
  stats  -- to show the statistic info

Here are the `Memcached commands`_ you can use.

.. _Memcached: http://memcached.org
.. _Memcached on Wikipedia: http://en.wikipedia.org/wiki/Memcachedk
.. _Hardware Consideration: http://code.google.com/p/memcached/wiki/NewHardware
.. _Memcached commands: https://code.google.com/p/memcached/wiki/NewCommands
