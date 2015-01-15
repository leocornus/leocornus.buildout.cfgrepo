How can we use strace?

Trace a process and sand output to a log file::

  $ sudo strace -o /tmp/strace.out.12212 -s 2000 -fp 12212

Trace a process and show up a summary report for each call::

  $ sudo strace -c -fp 21345

.. _The Magic of Strace: http://chadfowler.com/blog/2014/01/26/the-magic-of-strace/
