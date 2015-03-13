`Git Stories <README.rst>`_ >
Git Tips

How to set proxy
----------------

Here are the config options::

  $ git config --global url.http://.insteadOf git://
  $ git config --global http.proxy http://my.proxy.com:3128
  $ git config --global https.proxy http://my.proxy.com:3128

Here are the commands to unset.

  $ git config --global --unset http.proxy
  $ git config --global --unset https.proxy
