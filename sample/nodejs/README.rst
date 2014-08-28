This project is try to provide a sample buildout config to set up
nodejs_ services, specifically MediaWiki Parsoid_ service.

The main parts including:

- nodejs_ build
- nodejs_ configuration
- forever_ configuration
- Parsoid_ configruation
- supervisor_ configuration to manage nodejs_ and Parsoid_.
- npm_ installation and bash script
- bower_ installation and bash script

How to Get Started
------------------

Create a new **buildout.cfg** file with the following content::

  [buildout]
  extends = 
      buildout-base.cfg

Then execute the following commands::

  $ cd sample/nodejs
  $ python bootstrap.py
  $ bin/buildout

After the buildout executed successfully, you could find 
the following bash scripts in bin folder::

  bin/
    - node
    - npm
    - bower

How to use bower?
-----------------

For example using bower_ to install bootstrap_ framework::

  $ cd sample/nodejs
  $ bin/bower install bootstrap

We can specify which version we want for a module::

  $ bin/bower install bootstrap#2.x

.. _nodejs: http://nodejs.org
.. _Parsoid: http://www.mediawiki.org/wiki/Parsoid
.. _forever: https://github.com/nodejitsu/forever
.. _supervisor: http://supervisord.org/
.. _npm: https://www.npmjs.org/
.. _bower: http://bower.io
.. _bootstrap: http://getbootstrap.com/
