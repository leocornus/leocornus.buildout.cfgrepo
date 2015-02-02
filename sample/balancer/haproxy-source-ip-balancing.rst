`Balancer Stories <README.rst>`_ > HAProxy balancing by source IP

Source IP balancing will make sure same source IP (same client)
sticks to the same server for each request.
This will be different from session or cookie balancing,
which will make sure the same session/cookie stick to the 
same server.

Overview and Algorithm
----------------------

The post `client ip persistence or source ip hash load balancing`_
has a very good overview and explain about the possible algorithm.

The `Load Balancing with HAProxy`_ has the basic ideas about HAProxy.
Including the monitoring web interface.

`An Introduction to HAProxy and Load Balancing Concepts`_ has 
a very good introduction and some samples.

haproxy Source IP hash load-balancing
-------------------------------------


.. _client ip persistence or source ip hash load balancing: http://blog.haproxy.com/2013/04/22/client-ip-persistence-or-source-ip-hash-load-balancing/
.. _Load Balancing with HAProxy: https://serversforhackers.com/haproxy/
.. _An Introduction to HAProxy and Load Balancing Concepts: https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts
.. _Makeing HAProxy High Available for MySQL Cluster: http://www.fromdual.com/making-haproxy-high-available-for-mysql-galera-cluster
