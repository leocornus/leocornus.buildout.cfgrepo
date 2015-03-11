`Python Development Samples <README.rst>`_ >
How to Set Up Basic Python Development Env

.. contents:: Table of Contents
   :depth: 5

Buildout Config
---------------

The following is the basic buildout configuration, which will
generate the buildout, python, and test for your python project::

  [buildout]
  parts =
      python-bin
      test

  # this part will generate the python interpretor, which
  # will load all eggs.
  [python-bin]
  recipe = zc.recipe.egg
  interpreter = python
  eggs = 
      ${buildout:eggs}

  # This part will generate the bin/test script for unit test.
  [test]
  recipe = zc.recipe.testrunner
  # set the a list of eggs to test.
  eggs = 
      zope.testing
  # set the script name here,
  script = test

After run buildout we should have the following script in **bin**
folder::

   buildout
   python
   test

The **test** script will execute all unit test cases in **src** 
folder.

Test Runner
-----------

Some basic commands::

  bin/test -cvp   # execute tests with colored detail process
  bin/test -cvpD  # -D will load debugger when test failed...

Travis-ci Integration
---------------------

Travis has capability to execute test cases and deploy to PyPI.
And it is all done automatically.

Some travis samples:

- `hexagonit.recipe.download .travis.yml <https://github.com/hexagonit/hexagonit.recipe.download/blob/master/.travis.yml>`_ using setup.py to load test.
- `gp.recipe.node .travis.yml <https://github.com/gawel/gp.recipe.node/blob/master/.travis.yml>`_ using buildout to load test.
- `Travis PyPI deployment <http://docs.travis-ci.com/user/deployment/pypi/>`_

Sphinx Documentation
--------------------

Using Sphinx_ to generate the document automatically.

The collective.recipe.sphinxbuilder_ seems the easy recipe for 
buildout to generate documentation from a package.

PyPI Deployment
---------------

Buildout has built-in the PyPI deployment support.
Here are some general commands and options::

  bin/buildout setup sdist register upload
  bin/buildout setup src/leocornus.py.sandbox sdist register upload

The classifiers have to valid.
Here are full list of `classifiers <https://pypi.python.org/pypi?%3Aaction=list_classifiers>`_

.. _Sphinx: http://sphinx-doc.org/
.. _collective.recipe.sphinxbuilder: https://github.com/sdouche/collective.recipe.sphinxbuilder
