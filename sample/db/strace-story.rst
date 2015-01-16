How can we use strace for performance tuning?

Basic strace commands
---------------------

The post `The Magic of Strace`_ has a very good introduction about
the powerful strace.

Trace a process and sand output to a log file::

  $ sudo strace -o /tmp/strace.out.12212 -s 2000 -fp 12212

Trace a process and show up a summary report for each call::

  $ sudo strace -c -fp 21345

Some Examples
-------------

Here is a **strace -c** output for a php-fpm process,
which served a PHP application used both WordPress and MediaWiki.
It traced the process on January 16, 2015 from around
8AM to 12PM::

  % time     seconds  usecs/call     calls    errors syscall
  ------ ----------- ----------- --------- --------- ----------------
   76.29    1.165636           2    632509           read
    4.64    0.070827           0    609271    116099 lstat
    2.61    0.039850           0    186664       117 open
    2.56    0.039188           0     91195     12358 access
    2.28    0.034862           1     53164           poll
    2.00    0.030619           0    114379           munmap
    1.88    0.028732           0    146344     87001 stat
    1.62    0.024710          10      2394           brk
    1.54    0.023526           0    114379           mmap
    1.35    0.020635           1     34096           write
    0.83    0.012756           0    397859           fstat
    0.76    0.011651           0     35074           getdents
    0.59    0.009022           0    187960           close
    0.33    0.004994          12       405           accept
    0.20    0.003116           0     22949           getcwd
    0.18    0.002681           0     10811           recvfrom
    0.09    0.001316           1       968       629 connect
    0.08    0.001179           0     55407           lseek
    0.07    0.001047           1      2030           setsockopt
    0.03    0.000394           0       850           sendto
    0.02    0.000353           0     21463           fcntl
    0.01    0.000198           0      1010           socket
    0.01    0.000149           0       809         1 shutdown
    0.00    0.000075           0      1232           setitimer
    0.00    0.000073           0       809           times
    0.00    0.000073           0      2425           clock_gettime
    0.00    0.000041           0      1415           rt_sigaction
    0.00    0.000035           0      1191           readlink
    0.00    0.000034           0       709       403 ioctl
    0.00    0.000025           0       805           chdir
    0.00    0.000018           0       228           getsockopt
    0.00    0.000000           0       470           rt_sigprocmask
    0.00    0.000000           0        97           mremap
    0.00    0.000000           0       148           alarm
    0.00    0.000000           0        27           recvmsg
    0.00    0.000000           0         9           bind
    0.00    0.000000           0        32           getsockname
    0.00    0.000000           0         8           uname
    0.00    0.000000           0         6           flock
    0.00    0.000000           0         1           unlink
    0.00    0.000000           0        10           getrusage
  ------ ----------- ----------- --------- --------- ----------------
  100.00    1.527815               2731612    216608 total

.. _The Magic of Strace: http://chadfowler.com/blog/2014/01/26/the-magic-of-strace/
