`Sysadmin Samples <README.rst>`_
AHA Story
=========

aha_ is a cli simple tool to convert a linux terminal's output into
HTML format. 
It will also carry all those colors in the output.

some options
------------

Like all linux command line tools, aha_ has detail man manual.
You find all available options in man manual.
Here are some options I have used.

:-b:             generate the HTML with black background.
:--no-header: do NOT generate the HTML header.

Memos
-----

The simplest way to add line number for a text file or stream::

  $ cat -n afile.txt > afile-lines.txt

.. _aha: https://github.com/theZiz/aha
