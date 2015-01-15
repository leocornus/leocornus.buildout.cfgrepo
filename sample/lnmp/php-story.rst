`LNMP Samples <README.rst>`_ > PHP Story

opcache
-------

OPcache is shipped with PHP version 5.5.0 and higher.
Make sure compile PHP with **--enable-opcace** option.
The OPcache extension will locate in folder
**lib/php/extensions/**.
The php.ini configuration directive **zend_extension** will be used
to load the OPcache_ extension::

  zend_extension = /full/path/to/lib/php/extensions/opcache.so

PHP-FPM need restart after change the php.ini.

Here are some important php.ini configuration directives.

opcache.memory_consumption
  in megabytes, default is 64

.. _OPcache: http://php.net/manual/en/opcache.configuration.php
.. _Some Tools for OPcache: https://rtcamp.com/tutorials/php/zend-opcache/
