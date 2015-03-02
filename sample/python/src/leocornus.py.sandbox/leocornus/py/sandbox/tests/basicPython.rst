Python Basic
============

Get to know Python language in basic.

    >>> 1 + 3
    4

Basic os module.

    >>> import os
    >>> homeFolder = os.path.expanduser('~')
    >>> testFolder = os.path.join(homeFolder, 'testfolder')
    >>> os.mkdir(testFolder)

Basic shutil module

    >>> import shutil
    >>> shutil.rmtree(testFolder)

Basic String Operator
---------------------

Try the splitlines:

  >>> lines = """line one
  ... line two
  ... line three
  ... """
  >>> lines.splitlines()
  ['line one', 'line two', 'line three']
