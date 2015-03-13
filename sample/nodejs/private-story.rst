`Node.js Samples <README.rst>`_
Private Registry Story

This story is all about how to set up private registry and
how to use the private registry.
It will cover both npm_ and bower_ registries.

Sinopia as Private npm Registry
-------------------------------

Sinopia_ is a comprehensive solution for a private npm registry.
It will save public npm packages locally once the package is asked 
once. It works like a proxy server to the public npm registry.

Sinopia_ supports multiuser to registry private package.

Installation and setup is very easy and simple::

  $ npm install -g sinopia
  $ sinopia

  # set npm to use sinopia, 4873 is the default port.
  $ npm set registry http://server.domain.com:4873/

Private Bower
-------------

set up bower to use different registry, in file **.bowerrc**::


  {
    "registry": "http://10.0.0.1:5678",
    "proxy": "http://10.0.0.2:3128",
    "https-proxy": "http://10.0.0.2:3128",
    "directory": "app/bower_components",
    "interactive": false
  }

private-bower using **5678** as the default port.
private-bower will by pass public packages to public bower registry.
It will NOT cache any public packages locally.
So you have to set up proxy if you behind a firewall.

.. _npm: https://www.npmjs.org/
.. _bower: http://bower.io
.. _Sinopia: https://github.com/rlidwka/sinopia
