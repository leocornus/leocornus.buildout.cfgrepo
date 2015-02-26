`Python Development Samples <README.rst>`_ >
How to Set Up Basic Python Development Env

buildout config
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
