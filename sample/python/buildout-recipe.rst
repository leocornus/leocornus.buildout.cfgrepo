`Python Development Samples <README.rst>`_ >
How to Development a Buildout Recipe

Get Started
-----------

Get started the buildout recipe development is very simple.

**Testing**

Testing should always be the first step for any software development.
Python has so many good tools for testing. 
And zc.buildout package provides a set of 
useful funtions for testing.

Methods **constructor, install and update**

Any class could be a zc.buildout recipe, as asson as it has 
3 must-have methods: constructor (__init__), install, and update. 
And then the entry_points named zc.buildout will tell 
zc.buildout to load and execute the recipe.

entry_points sample in setup.py

Execute Test Cases
------------------

Update the **test** part to tell **testrunner** to load your
recipe egg::

  [test]
  eggs += 
      leocornus.recipe.distribute

Once you buildout done, we should have the **test** script in 
**bin** folder. 
The following command will run all test cases and show the
progress in colored output::

  bin/test -cvp

Generate and upload eggs
------------------------

buildout has a built-in command (setup) to generate, register, 
and upload egg distribution.

We are using leocornus.pydev as the base development environment.  
Module leocornus.recipe.wpmw will be a development egg siting 
in folder src::

  $ bin/buildout setup src/leocornus.recipe.wpmw sdist register upload
