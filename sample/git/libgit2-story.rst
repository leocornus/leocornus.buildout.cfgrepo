`Git Stories <README.rst>`_ >
libgit2 Story

Sample folder to show how to build libgit2_ library and its bindings.

Actions for php-git bindings
----------------------------

Things we need install:

- libgit2_
- PHP php-fpm
- php-git_
- Nginx for testing, optional.

Check file `buildout-php.cfg <buildout-php.cfg>`_ for details.

buildout sample
---------------

Here is a basic and simple buildout.cfg sample::

  [buildout]
  extends = 
      buildout-php.cfg
  
  [users]
  php-fpm = git
  nginx = git
  
  [ports]
  supervisord = 9600
  php-fpm = 9601
  nginx = 80
  
  [hosts]
  frontend-hostname = localhost
  frontend-ip = 127.0.0.1

Create a empty file named **buildout.cfg** and copy source code
to the file. And then run the following commands::

  $ python bootstrap.py
  $ bin/buildout

Start supervisord::

  $ sudo bin/supervisord

Then the sample git php code will ready at page 
http://localhost/phpgit.php.
  
Build Errors
------------

We have problem to build php-git binding mainly because of the 
error to find the header files from libgit2.
All those errors are solved by following the build instruction 
in php-git_ github page.

.. _libgit2: https://github.com/libgit2/libgit2
.. _php-git: https://github.com/libgit2/php-git
