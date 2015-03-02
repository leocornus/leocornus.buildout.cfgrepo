Search and Archive Story
========================

**Purpose**

- Search a folder to identify certain patterns of string, such as 
  plugin name, version, extension name, etc.
- Archive the folder based on name and version, the archive name
  will have pattern name-version.zip

**Preparing Testing Folder**

Get ready a test folder.
All testing activities will happen in this folder.
At the end will remove the whole folder as clean up.

  >>> import os
  >>> homeFolder = os.path.expanduser('~')
  >>> testFolder = os.path.join(homeFolder, 'testfolder')
  >>> os.path.isdir(testFolder)
  False
  >>> os.mkdir(testFolder)
  >>> os.path.isdir(testFolder)
  True

**Preparing Testing Files**

We will need the following files for testing.

**Remove Testing Folder**

remove the whole testing folder.

  >>> import shutil
  >>> shutil.rmtree(testFolder)
  >>> os.path.isdir(testFolder)
  False
