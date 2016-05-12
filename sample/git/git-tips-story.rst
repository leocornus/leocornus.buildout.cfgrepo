`Git Stories <README.rst>`_ >
Git Tips from my day to day work

.. contents:: Table of Contents
   :depth: 5

Git Switch Remote
-----------------

switch remote is as simple as::

  git remote set-url origin /local/path/to/git/repo.git
  git remote -v

Migration Actions
-----------------

- git clone --bare REMOTE_URL

.. _Git on the Server: http://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols

Mirrowing / Duplicating a repository
------------------------------------

It is very simple to `duplicating a Git repository`_:
bare clone and mirror push.

.. _duplicating a Git repository: https://help.github.com/articles/duplicating-a-repository/

rev-list for total number
-------------------------

you my ask more than one path from git:: 

  $ cd themes
  $ git rev-list HEAD --count themeone themetwo
  $ git rev-list HEAD --count /full/path/to/themeone /full/path/two

Git Achive
----------

It is very easy to generate archive files (zip or tar) from 
git repository.
The following example will generate the archive file
**mytheme-8bb9d5a.zip** on **themes** folder at commit **8bb9d5a**
for **mytheme**.
::

  $ cd themes
  $ git archive --format=zip -o mytheme-8bb9d5a.zip 8bb9d5a mytheme

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

How to apply patch to files
---------------------------

here are some memo to generate patch file and apply the patch.::

  $ git diff --patch . >> thePatch.diff
  $ git apply thePatch.diff

How to move files (folders) from repo A to repo B
-------------------------------------------------

This should preserve all commit history for the files.
The post `Moving files between git repos`_ has details steps.

Here is the idea:

- clone everyting to local.
- remove the origin remote, then the current folder will be the
  temporary remote for this merge.
- filter branch by subdirectory
- create new folder for the subdirectory. the directory name
  should NOT change!
- add move all files to the new folder, then
  git add, and git commit.
- go to the target git repository
- add the remote to the filtered directory.
- git pull everything from the new remote.
- git remove the filtered dir.
- git commit.

question:

- how to keep the folder name.

Git log option follow
---------------------

The git log option **--follow** will keep all commit history,
including folder name change.

Git stash
---------

Mainly for the following actions.

Stash a local change on working folder:

  $ git stash create:b ser

.. _Moving files between git repos: http://gbayer.com/development/moving-files-from-one-git-repository-to-another-preserving-history/
.. _splitting a subfolder out into a new repository: https://help.github.com/articles/splitting-a-subfolder-out-into-a-new-repository/
