leocornus.buildout.cfgrepo
==========================

Create this repository to save some buildout configuration files
to make my daily development work easier.

What's in
=========

I will try to include the following utilities:

* MySQL/MariaDB database compile and build
* MySQL/MariaDB database server setup utilities
* MySQL/MariaDB configuration
* SQLite3 compile and build
* Nginx compile and build
* Nginx configuration for all kind of applications, 
  including WordPress, MediaWiki, Django, etc.
* PHP-FPM compile and build
* PHP-FPM configuration

How to use
==========

cfgrepo is very easy to use.  You could try the following methods:

* hard copy, download from GitHub and copy to your buildout facility.
* symlink, clone from GitHub and symlink to your buildout folder.
* submodule, adding cfgrepo as a submodule of your project.

git submodule and tag
=====================

Add cfgrepo as a submodule::

  $ cd myproject
  $ git submodule add git://github.com/leocornus/leocornus.buildout.cfgrepo.git buildout/cfgrepo
  $ git commit -m "add cfgrepo as submodule" .

Update to use a certain tag::

  $ cd buildout/cfgrepo
  $ git checkout v0.1
  $ cd ../..
  $ git add buildout/cfgrepo
  $ git commit -m "update to cfgrepo v0.1" buildout/cfgrepo
  $ git push

Register and update submodule in your project::

  $ cd myproject
  $ git submodule init
  $ git submodule update

License
=======

GNU General Public License Version 2

Change Log
==========

- `cfgrepo releae 0.5 <docs/cdgrepo-0.5.rst>`_

cfgrepo-0.4 (2014-04-03)
-----------------------

 - adding cfg to build node.js and MediaWiki Parsoid Service
 - install Java
 - install and config Tomcat
 - install and config Trac

0.3 (2013-10-31)
----------------

 - Alternative way to setup supervisor by using
   collective.recipe.template and zc.recipe.egg.

0.2 (2012-05-08)
----------------

 - Add config profile to build legacy MySQL database server 
   up to version 5.1.x 

0.1 (2012-04-27)
----------------

 - initial release, taged as v0.1
