Try to provide some sample to build and config different kind of
Proxy Servers by using buildout.

Based on Wikipedia `Proxy Server <http://en.wikipedia.org/wiki/Proxy_server>`_
page, there are 3 types of Proxy servers:

- Forward proxy
- Open proxy
- Reverse proxy

**Forward Proxy**

Squid_ is the best choice for Forward proxy server.

**Squid Basic**

Once the buildout execute successfully, 
we could find the squid server in folder **parts/squid-build/sbin**.
Start a squid server by using the following command::

  $ parts/squid-build/sbin/squid

The default port is **3128**.

.. _Squid: http://www.squid-cache.org/
