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

How about private npm repo?
---------------------------

The npm_ repository is very good repository.
Still, there are many benefits to create a private npm repo:

- When npm_ is down or outage.
- When you are working behind a firewall.

Here are some good post talking about this topic.

- `How to create a private npmjs repository`_
- sinopia_ is a private npm repository server.

.. _nodejs: http://nodejs.org
.. _Parsoid: http://www.mediawiki.org/wiki/Parsoid
.. _forever: https://github.com/nodejitsu/forever
.. _supervisor: http://supervisord.org/
.. _npm: https://www.npmjs.org/
.. _bower: http://bower.io
.. _bootstrap: http://getbootstrap.com/
.. _How to create a private npmjs repository: http://www.clock.co.uk/blog/how-to-create-a-private-npmjs-repository
.. _sinopia: https://www.npmjs.org/package/sinopia
