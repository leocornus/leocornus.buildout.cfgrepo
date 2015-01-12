`Cache Samples <README.rst>`_ > Varnish Story

Main facts:

- Varnish ONLY caching for anonymous users
- logged-in users may use Memcached_

Varnish Basic
-------------

Basic things from Varnish_

- VCL configuration file
- varnishadm, the admin console, which read secret from 
  /etc/varnish/secret
- varnishlog, it will stream the logging message in memory 
- varnishstat, statistics about varnish, `Varnishstat for dummies`_
  is a good start.

**hashing**

- varnish is using hash key for each page.
- hash key is generated based on URL and Host or IP.

`Varnish for High Availability Web Servers`_

How to decide the cache size?
-----------------------------

How to deploy multiple Varnish instances
----------------------------------------

the case is multiple backend web servers and multiple Varnish_
instances.


Questions
---------

- How to calculate the cache size for my website
- how to deploy multiple Varnish_ instances?


.. _Memcaches: http://memcached.org
.. _Varnish: https://www.varnish-cache.org/
.. _Varnishstat for dummies: http://kly.no/posts/2009_12_08__Varnishstat_for_dummies__.html
.. _Varnish for High Availability Web Servers: https://www.lullabot.com/blog/article/configuring-varnish-high-availability-multiple-web-servers
