Nework Configuration Command Line
=================================

Configure Ubuntu network by using command line.
`Networking configuration`_ on Ubuntu official document has all
the details.
We only list some tips for day to day work.

Add/change route
----------------

The ip route could be simply update to fit in your requirment.
For example you have 2 network interface: eth0 and wlan0.
The eth0 will be used for Intranet and
the wlan0 will be used for Extranet.

The following route will help routing::

  $ ip route change default via 192.168.0.1 dev wlan0 proto static
  $ ip addr

.. _Network configuration: https://help.ubuntu.com/community/NetworkConfigurationCommandLine/Automatic
