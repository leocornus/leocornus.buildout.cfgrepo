Search and Archive Story
========================

.. contents:: Table of Contents
   :depth: 5

Purpose
-------

- Search a folder to identify certain patterns of string, such as 
  plugin name, version, extension name, etc.
- Archive the folder based on name and version, the archive name
  will have pattern name-version.zip

Here are list of supported archive types:

- WordPress plugin
- WordPress Theme

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

createFile
~~~~~~~~~~

utility function to create a file in a folder.
There parameters: folder path, filename, and content for the file.
There is no return value for this function.

  >>> def createFile(folder, filename, content):
  ...     fullName = os.path.join(folder, filename)
  ...     os.system("touch " + fullName)
  ...     f = open(fullName, 'r+')
  ...     f.write(content)
  ...     f.close()

archiveFolder
~~~~~~~~~~~~~

utility function to archive a folder.
There parameters:

:archivePath: the full path the the archive file.
:rootFolder: the parent folder in full path of the source folder
:folderName: the name of the folder in the rootFolder.

Return value: the archive file as a object

  >>> def archiveFolder(archivePath, rootFolder, folderName):
  ...     # zip the plugin dir
  ...     zip = zipfile.ZipFile(archivePath, "w", 
  ...        compression=zipfile.ZIP_DEFLATED)
  ...     os.chdir(rootFolder)
  ...     for dirpath, dirnames, filenames in os.walk('./' + 
  ...                                                 folderName):
  ...         for name in filenames:
  ...             path = os.path.normpath(os.path.join(dirpath, name))
  ...             if os.path.isfile(path):
  ...                 zip.write(path, path)
  ...     zip.close()
  ...     return zip

extractInfo
~~~~~~~~~~~

utility function to extract a set of information from 
the given file full path.

Parameters:

:fullFilePath: the full path to the file.

Return a dict with the following fields:

:fileName: the file name, without path.
:dirName: the full path of the directory.
:folderName: the name of the directory without path.
:version: Version from the file.
:archiveName: the full path to the archive file.

  >>> def extractInfo(fullFilePath):
  ...     fileName = os.path.basename(fullFilePath)
  ...     #print """File Name: %s""" % fileName
  ...     dirName = os.path.dirname(fullFilePath)
  ...     #print """Dir Name: %s""" % dirName 
  ...     folderName = os.path.basename(dirName)
  ...     #print """Folder Name: %s""" % folderName
  ...     # extract the version number from the plugin file.
  ...     # try to using sed or grep
  ...     grepPattern = "grep -oE 'Version: .*' " + fullFilePath
  ...     version = subprocess.check_output(grepPattern, shell=True)
  ...     version = version.strip().split(":")
  ...     version = version[1].strip()
  ...     #print """Version: %s""" % version
  ...     # get ready the archive name.
  ...     archiveName = """%s.%s.zip""" % (folderName, version)
  ...     #print """Archive Name: %s""" % archiveName
  ...     info = {
  ...       'fileName' : fileName,
  ...       'dirName' : dirName,
  ...       'folderName' : folderName,
  ...       'version' : version,
  ...       'archiveName' : archiveName,
  ...     }
  ...     return info

Preparing Testing Files
-----------------------

WordPress Plugin
~~~~~~~~~~~~~~~~

The following WordPress file header identified as 
a WordPress Plugin::

  Plugin Name: name of plugin
  Version:  2.1.1

Here we will get ready some files for testing...

  >>> pluginOne = os.path.join(testFolder, 'pluginone')
  >>> os.mkdir(pluginOne)
  >>> data = """/**
  ...  * Plugin Name: Plugin One
  ...  * Version:  1.0.1
  ...  */
  ...  # *comments**
  ... <?php
  ... phpinfo()"""
  >>> createFile(pluginOne, 'pfileone.php', data)

Add more files here for testing.
Here are files in pluginOne folder.

  >>> createFile(pluginOne, 'pfile2.php', 'some testing code')
  >>> createFile(pluginOne, 'pfile3.php', 'some testing code 3')

Add subfolder css and add some styles.
 
  >>> pluginOneCss = os.path.join(pluginOne, 'css')
  >>> os.mkdir(pluginOneCss)
  >>> createFile(pluginOneCss, 'styles.css', 'styles')
  >>> createFile(pluginOneCss, 'print.css', 'print styles')

WordPress Theme
~~~~~~~~~~~~~~~

The following WordPress file header in file **style.css** 
identified as a WordPress theme::

  Theme Name: the theme name
  Version: 3.1.0

Create testing folders and files for WordPress theme.

  >>> themeOne = os.path.join(testFolder, 'themeone')
  >>> os.mkdir(themeOne)
  >>> os.path.isdir(themeOne)
  True

Create the theme style.css, which tells this is a WordPress theme.

  >>> data = """/**
  ...  * Theme Name: theme one
  ...  * Theme URI: http://www.themeone.com
  ...  * Version: 2.3
  ...  */
  ... some other infomation **"""
  >>> createFile(themeOne, 'style.css', data)

More files for theme one.

  >>> createFile(themeOne, 'tfileone.php', 'file one php')
  >>> createFile(themeOne, 'tfiletwo.php', 'file two php')
  >>> themeOneImage = os.path.join(themeOne, 'image')
  >>> os.mkdir(themeOneImage)
  >>> createFile(themeOneImage, 'imgone.jpg', 'image one')
  >>> createFile(themeOneImage, 'imgtwo.jpg', 'image two')

Search and Archive
------------------

Search the test folder to find certain string patterns.
The method **os.system** will not return the result.
So we are uing the subprocess module.

  >>> import subprocess
  >>> import zipfile

Grep the testing folder to find eather plugins or themes.
Here are the grep patterns for WordPress plugin and theme::

  $ grep -l 'Plugin Name: ' /full/path/plugins/*/*.php
  $ grep -l 'Theme Name: ' /full/path/themes/*/style.css

We only search one level deep in the testing folder.

  >>> pG = "grep -l 'Plugin Name: ' " + testFolder + "/*/*.php" #**
  >>> plugins = subprocess.check_output(pG, shell=True)
  >>> """Plugin: %s""" % plugins.strip() # doctest: +ELLIPSIS
  'Plugin:...pfileone.php'
  >>> tG = "grep -l 'Theme Name: ' " + testFolder + "/*/style.css"#**
  >>> themes = subprocess.check_output(tG, shell=True)
  >>> print(themes.strip()) # doctest: +ELLIPSIS
  /home/.../themeone/style.css
  >>> allPkgs = plugins + themes
  >>> print allPkgs.strip() # doctest: +ELLIPSIS
  /home/.../pfileone.php
  /home/.../style.css

Archive Plugin
~~~~~~~~~~~~~~

  >>> for plugin in plugins.strip().splitlines():
  ...     # the plugin already has full path, as we grep the 
  ...     # full path pattern.
  ...     info = extractInfo(plugin)
  ...     print("""File Name: %s""" % info['fileName'])
  File Name: pfileone.php

  ...     print("""Plugin Dir: %s""" % info['dirName']) 
  Plugin Dir: /.../pluginone

  ...     print("""Plugin Name: %s""" % info['folderName'])
  Plugin Name: pluginone

  ...     print("""Version: %s""" % info['version'])
  Version: 1.0.1

  ...     print("""Archive Name: %s""" % info['archiveName'])
  Archive Name: pluginone.1.0.1.zip

  ...     # archive the plugin.
  ...     # check file exist o not.
  ...     archivePath = os.path.join(testFolder, info['archiveName'])
  ...     os.path.exists(archivePath)
  False

  ...     # zip the plugin dir
  ...     zip = archiveFolder(archivePath, testFolder, 
  ...                         info['folderName'])
  ...     os.path.exists(archivePath)
  True

  ...     files = zip.namelist()
  ...     len(files)
  5

  ...     'pluginone/pfileone.php' in files
  True

  ...     'pluginone/pfile2.php' in files
  True

  ...     'pluginone/pfile3.php' in files
  True

  ...     'pluginone/css/styles.css' in files
  True

Archive Theme
~~~~~~~~~~~~~

  >>> for theme in themes.strip().splitlines():
  ...     info = extractInfo(theme)
  ...     print("""File Name: %s""" % info['fileName'])
  File Name: style.css

  ...     print("""Theme Dir: %s""" % info['dirName'])
  Theme Dir: /.../themeone

  ...     print("""Theme Name: %s""" % info['folderName'])
  Theme Name: themeone

  ...     print("""Version: %s""" % info['version'])
  Version: 2.3

  ...     print("""Archive Name: %s""" % info['archiveName'])
  Archive Name: themeone.2.3.zip

  ...     # archive the Theme.
  ...     archivePath = os.path.join(testFolder, info['archiveName'])
  ...     os.path.exists(archivePath)
  False

  ...     # zip the plugin dir
  ...     zip = archiveFolder(archivePath, testFolder, 
  ...                         info['folderName'])
  ...     os.path.exists(archivePath)
  True

  ...     files = zip.namelist()
  ...     len(files)
  5

  ...     'themeone/style.css' in files
  True

  ...     'themeone/tfileone.php' in files
  True

  ...     'themeone/tfiletwo.php' in files
  True

  ...     'themeone/image/imgone.jpg' in files
  True

Questions TODOs
---------------

The ... seems not working here, might need set up one of the 
option flag::

  Plugin Dir: /home/.../testfolder/pluginone

The **...** works only if you using **print** to show the result and
the testing result is right after the print.

Adding the doctest comment for ELLIPSIS will make sure **...**
work properly.

Remove Testing Folder
---------------------

remove the whole testing folder.

  >>> import shutil
  >>> shutil.rmtree(testFolder)

now verify testFolder is removed.

  >>> os.path.isdir(testFolder)
  False
  >>> os.path.isfile(testFolder)
  False

Doctest Directives
------------------

Here are some interesting doctest directives, more could be found
in post `Basic Python Doctest`_

+ELLIPSIS
  This output will use Ellipsis **...**

+SKIP
  Skip a test.

.. _Basic Python Doctest: https://www.packtpub.com/books/content/basic-doctest-python
