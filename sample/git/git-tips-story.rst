`Git Stories <README.rst>`_ >
Git Tips

How to set proxy
----------------

Here are the config options::

  $ git config --global http.proxy http://my.proxy.com:3128
  $ git config --global https.proxy http://my.proxy.com:3128

Here are the commands to unset::

  $ git config --global --unset http.proxy
  $ git config --global --unset https.proxy

Normally the proxy server will now allow **git** protocol to
go through the server.
The easy way to walk around is tell git to replace the protocol.
Here is are example::

  $ git config --global url.http://.insteadOf git://
  $ git config --global url.https://.insteadOf git://

How to create a new repo from a subfolder
-----------------------------------------

The page `splitting a subfolder out into a new repository`_ has
a very good instruction.
The following is my experience for split out 
**leocornus.py.sandbox** to a new repository.
The first step is to create a new empty (no init commit) repository.
Then execute the following from command line::

  $ git clone git@github.com:leocornus/leocornus.buildout.cfgrepo.git cfgrepo-split
  $ cd cfgrepo-split
  $ git filter-branch --prune-empty --subdirectory-filter sample/python/src/leocornus.py.sandbox master
  Rewrite 94a5f2d827530e13e30b6f786c7c1db24b4b53a7 (23/23)
  Ref 'refs/heads/master' was rewritten
  $ git remote set-url origin git@github.com:leocornus/leocornus.py.sandbox.git
  $ git config user.name 'Sean Chen'
  $ git config user.email 'sean.chen@email.com'
  $ git push -u origin master
  $ git remote -v show origin
  $ cd ..
  $ mv cfgrepo-split leocornus.py.sandbox

Now we have the new repository with all history from folder
**sample/python/src/leocornus.py.sandbox** 

.. _splitting a subfolder out into a new repository: https://help.github.com/articles/splitting-a-subfolder-out-into-a-new-repository/
