`Sysadmin Samples <../README.rst>`_
Script to capture terminal session.

It is very easy to capture a terminal session by using script_.
Here is example::

  $ script
  Script started, file is typescript
  $ ls -la
  total 36
  drwxrwxr-x  2 egov egov  4096 Apr 22 13:58 .
  drwxrwxr-x 15 egov egov  4096 Apr 22 13:50 ..
  -rw-rw-r--  1 egov egov   101 Mar 13 09:42 cygwin-story.rst
  -rw-rw-r--  1 egov egov   429 Apr 22 13:52 README.rst
  -rw-rw-r--  1 egov egov     0 Apr 22 13:51 script-story.rst
  -rw-r--r--  1 egov egov 12288 Apr 22 13:58 .script-story.rst.swp
  -rw-rw-r--  1 egov egov   107 Mar  9 12:08 sed-story.rst
  -rw-rw-r--  1 egov egov     0 Apr 22 13:58 typescript
  -rw-rw-r--  1 egov egov   118 Mar 16 13:25 vim-story.rst
  $ exit
  exit
  Script done, file is typescript

Here is the content of file **typescript**::

  Script started on Wed 22 Apr 2015 01:58:50 PM EDT
  $ ls -la^M
  total 36^M
  drwxrwxr-x  2 egov egov  4096 Apr 22 13:58 .^M
  drwxrwxr-x 15 egov egov  4096 Apr 22 13:50 ..^M
  -rw-rw-r--  1 egov egov   101 Mar 13 09:42 cygwin-story.rst^M
  -rw-rw-r--  1 egov egov   429 Apr 22 13:52 README.rst^M
  -rw-rw-r--  1 egov egov     0 Apr 22 13:51 script-story.rst^M
  -rw-r--r--  1 egov egov 12288 Apr 22 13:58 .script-story.rst.swp^M
  -rw-rw-r--  1 egov egov   107 Mar  9 12:08 sed-story.rst^M
  -rw-rw-r--  1 egov egov     0 Apr 22 13:58 typescript^M
  -rw-rw-r--  1 egov egov   118 Mar 16 13:25 vim-story.rst^M
  $ exit^M
  exit^M
  
  Script done on Wed 22 Apr 2015 01:59:02 PM EDT

To remove the ending **^M**, we need using the following command::

  $ col -b < typescript > typescript-new

How to set the file name
------------------------

::

  $ script filename.txt

How to append to a existing file
--------------------------------

::

  $ script -a filename.txt

.. _script: http://en.wikipedia.org/wiki/Script_(Unix)
