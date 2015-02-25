The **src** folder is the place for Python source code.
You could sym link your Python app's source folder to here 
or clone your source code here directly.

for example::

  $ cd src
  $ ln -s /path/to/python/module/my.package my.package

Then in the **buildout.cfg** file, adding the following to
**buildout** part::

  ...
  develop =
      src/my.package
  ...
