Pythong Testing Story
=====================

Testing is fun!

Testing using setup.py
----------------------

The **test_suite** is the entry point for setup.py to execute test cases.

Q: how to get ready test_suite?

DocFileSuite
~~~~~~~~~~~~

You could add doctest by using the DocFileSuite.
It will take as simple as one parameter (PATH to the file).
The **path** could be relative or absolute depends on the keyword
argument **module_relative**. The default is **True**.

Some useful doctest directives:

:+ELLIPSIS:
  tells doctest to use Ellipsis (**....**) object to verify the 
  testing result.

:+SKIP:
  tells doctest to skip a test.

Testing using buildout
----------------------

The **zc.recipe.testrunner** recipe will generate the test script and 
execute all test cases.

Q: how testrunner load all test cases?

Testing using travis-ci
-----------------------

Travis-ci is mainly a set of bash shell script to do a set of things 
for testing:

- load a linux vm from a image.
- set up python language
- set up dependences, such as browsers, 3rd party libs, etc.
- clone source code from git repository
- execute pre test script
- execute test script

Travis-ci just provides a convinient way to automatically execute test script.
It does NOT introduce new way to execute test cases.

