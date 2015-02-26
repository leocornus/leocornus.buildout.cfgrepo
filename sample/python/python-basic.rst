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
