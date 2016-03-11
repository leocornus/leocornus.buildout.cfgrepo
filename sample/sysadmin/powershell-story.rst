PowerShell Story
================

Batch Rename Multiple Files
---------------------------

Using powershell to rename multiple files.

Copy all files in one folder

Replace abc to c-d-e::

  PS c:\afolder > Dir | Rename-Item -NewName {$_.name -replace "abc","c-d-e"}

Run Command Shell As Administrator
----------------------------------

Here are the steps to run command shell as administrator.

- got to the run box, type **cmd**
- Use **CTRL+SHIFT+ENTER** 

The combined 3 keys make the trick.

Routing Management
------------------

The **route** command need run as administrator.

Here are some examples::

  c:\> route add 0.0.0.0 mask 0.0.0.0 192.168.0.1 metric 10
  c:\> tracert www.google.com

More details document could find on this page: `https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/route.mspx?mfr=true`_
