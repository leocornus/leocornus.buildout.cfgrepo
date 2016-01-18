PowerShell Story
================

Batch Rename Multiple Files
---------------------------

Using powershell to rename multiple files.

Copy all files in one folder

Replace abc to c-d-e::

  PS c:\afolder > Dir | Rename-Item -NewName {$_.name -replace "abc","c-d-e"}
