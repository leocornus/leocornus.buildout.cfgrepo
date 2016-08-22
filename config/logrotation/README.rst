Log Rotation Strategy
=====================

Different application (program) have different way for log rotation.
We have to look at the specific applications that we are using.

Sysmtem logrotate
-----------------

Linux system lorotate will have the following configurations:

- /etc/logrotate.conf file
- /etc/logrotate.d folder

Nginx
-----

By default Nginx server rely on the system **logrotate** to do
log rotation.
NGINX will re-open its logs in response to the USR1 signal.::

  $ mv access.log access.log.0
  $ kill -USR1 `cat master.nginx.pid`
  $ sleep 1
  $ gzip access.log.0    # do something with access.log.0

Java Application
----------------

Most of the Java application will rotate log files by default.
For example elasticsearch.
