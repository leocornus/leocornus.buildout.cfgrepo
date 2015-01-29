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

haproxy Source IP hash load-balancing
-------------------------------------


.. _client ip persistence or source ip hash load balancing: http://blog.haproxy.com/2013/04/22/client-ip-persistence-or-source-ip-hash-load-balancing/
