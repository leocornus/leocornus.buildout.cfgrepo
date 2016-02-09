buildout repository for some basic libraries.

Why we need this?
-----------------

for some legacy OS.

Here is a list

- libxml
- libxslt
- autoconfig

libxml2 on 64 bit
-----------------

The **CC** option will tell this is a 64 bit machine.
::

  $ ./configure CC='cc -m64' --prefix=/usr/local
  $ ./configure CC='cc -m64' --prefix=/usr 
    --libdir=/usr/lib64


