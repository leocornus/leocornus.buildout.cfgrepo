Search and Archive Story
========================

Purpose
-------

- Search a folder to identify certain patterns of string, such as 
  plugin name, version, extension name, etc.
- Archive the folder based on name and version, the archive name
  will have pattern name-version.zip

Preparing Testing Folder
------------------------

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

General Functions
-----------------

We will define some general functions for re-use.
Here are some ideas:

- function to prepare testing folder and files.
- function to archive a file in zip format.
- utility function to print out some information for verifying.

utility function to create a file in a folder.

  >>> def createFile(folder, filename, content):
  ...     fullName = os.path.join(folder, filename)
  ...     os.system("touch " + fullName)
  ...     f = open(fullName, 'r+')
  ...     f.write(content)
  ...     f.close()

utility function to archive a folder

Preparing Testing Files
-----------------------

We will need the following files for testing.

- WordPress Plugins
- WordPress Themes

**WordPress Plugin**

The following WordPress file header identified as 
a WordPress Plugin::

  Plugin Name: name of plugin
  Version:  2.1.1

Here we will get ready some files for testing...

  >>> pluginOne = os.path.join(testFolder, 'pluginone')
  >>> os.mkdir(pluginOne)
  >>> createFile(pluginOne, 'pfileone.php', 
  ... """/**
  ...  * Plugin Name: Plugin One
  ...  * Version:  1.0.1
  ...  */
  ...  # *comments**
  ... <?php
  ... phpinfo()""")

Add more files here for testing.

  >>> createFile(pluginOne, 'pfile2.php', 'some testing code')
  >>> createFile(pluginOne, 'pfile3.php', 'some testing code 3')
  >>> pluginOneCss = os.path.join(pluginOne, 'css')
  >>> os.mkdir(pluginOneCss)
  >>> createFile(pluginOneCss, 'styles.css', 'styles')
  >>> createFile(pluginOneCss, 'print.css', 'print styles')

**WordPress Theme**

The following WordPress file header in file **style.css** 
identified as a WordPress theme::

  Theme Name: the theme name
  Version: 3.1.0

Search and Archive
------------------

Search the test folder to find certain string patterns.
The method **os.system** will not return the result.
So we are uing the subprocess module.

  >>> import subprocess
  >>> import zipfile
  >>> # search only one level deep in the testFolder
  >>> plugins = subprocess.check_output("grep -l 'Plugin Name: ' " + 
  ...     testFolder + "/*/*.php", 
  ...     # shell need to be True **
  ...     shell=True)
  >>> for plugin in plugins.splitlines():
  ...     fileName = os.path.basename(plugin)
  ...     print """File Name: %s""" % fileName
  ...     pluginDir = os.path.dirname(plugin)
  ...     # print """Plugin Dir: %s""" % pluginDir
  ...     pluginName = os.path.basename(pluginDir)
  ...     print """Plugin Name: %s""" % pluginName
  ...     # extract the version number from the plugin file.
  ...     # try to using sed or grep
  ...     version = subprocess.check_output("grep -oE 'Version: .*' " 
  ...                                       + plugin, shell=True)
  ...     version = version.strip().split(":")
  ...     version = version[1].strip()
  ...     print """Version: %s""" % version
  ...     # get ready the archive name.
  ...     archiveName = """%s.%s.zip""" % (pluginName, version)
  ...     print """Archive Name: %s""" % archiveName
  ...     # archive the plugin.
  ...     # check file exist o not.
  ...     archivePath = os.path.join(testFolder, archiveName)
  ...     os.path.exists(archivePath)
  ...     # zip the plugin dir
  ...     zip = zipfile.ZipFile(archivePath, "w", 
  ...        compression=zipfile.ZIP_DEFLATED)
  ...     os.chdir(testFolder)
  ...     for dirpath, dirnames, filenames in os.walk('./' + 
  ...                                                 pluginName):
  ...         for name in filenames:
  ...             path = os.path.normpath(os.path.join(dirpath, name))
  ...             if os.path.isfile(path):
  ...                 zip.write(path, path)
  ...     zip.close()
  ...     os.path.exists(archivePath)
  ...     files = zip.namelist()
  ...     len(files)
  ...     'pluginone/pfileone.php' in files
  ...     'pluginone/pfile2.php' in files
  ...     'pluginone/pfile3.php' in files
  ...     'pluginone/css/styles.css' in files
  File Name: pfileone.php
  Plugin Name: pluginone
  Version: 1.0.1
  Archive Name: pluginone.1.0.1.zip
  False
  True
  5
  True
  True
  True
  True

The ... seems not working here, might need set up one of the 
option flag::

  Plugin Dir: /home/.../testfolder/pluginone

Remove Testing Folder
---------------------

remove the whole testing folder.

  >>> import shutil
  >>> shutil.rmtree(testFolder)
  >>> os.path.isdir(testFolder)
  False
