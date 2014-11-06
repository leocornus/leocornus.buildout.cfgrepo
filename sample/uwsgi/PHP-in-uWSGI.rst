`Back to README <README.rst>`_ >
Build and Run PHP Scripts in uWSGI

The full details documentation could be found 
`Running PHP scripts in uWSGI <http://uwsgi-docs.readthedocs.org/en/latest/PHP.html>`_.

Building
--------

PHP need enable option **--enable-embed** during compile and build.
Once build success, you should see the following output,
when execute **php-config**::

  $ ${php-build:location}/bin/php-config --php-sapis
  cli embed fpm cgi

build profile for uWSGI

buildout.cfg
------------

It is very easy to create a **buildout.cfg** file by simply extends
the `buildout-php-in-uwsgi.cfg <buildout-php-in-uwsgi.cfg>`_.

We need explore new ways to build uWSGI and its plugins.

References
----------

- `Rumming anything on Nginx with uWSGI <http://metz.gehn.net/2013/02/running-anything-on-nginx-with-uwsgi/>`_ 
