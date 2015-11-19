`Sysadmin Samples <README.rst>`_
> Some tips for Vim.

color schemes
-------------

Switch color schemes::

  :colorscheme desert
  :help :colorscheme

auto indent and past mode
-------------------------

Tell vim to auto indent and using white spaces for tab::

  :set autoindent expandtab
  :set paste

search and replace
------------------

search and replace is under command **substitute**
::

  :%s/foo/bar/g
  :help substitue

record and play
---------------

record something to register a.
valid registers are **[0-9a-zA-Z]**
::

  :qa
  :help record

execute the contents of a register.
::

  :@a
  :@@

.vimrc
------

An sample for file **.vimrc**::

  colorscheme desert      " colorscheme desert
  colors desert
