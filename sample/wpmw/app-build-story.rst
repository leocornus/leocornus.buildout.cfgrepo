Build Story for Applications
============================

Here are list applications:

- WordPress
- WordPress plugins
- WordPress themes
- MediaWiki
- MediaWiki Extensions
- MediaWiki Skins

.. contents:: Table of Contents
   :depth: 5

TODO:

Composer for PHP packages, including themes, plugins, extensions,
and skins.

- How to manage a list of plugins?
- How to manage a list of extensions?
- how to manage themes?
- how to manage skins?

Configuration check list
------------------------

- Nginx config
- WordPress config
- MediaWiki config

buildout structure
------------------

Thinking about the structure for buildout configuration::

  buildout-apps.cfg
  buildout-apps-wordpress.cfg
  buildout-apps-mediawiki.cfg


Steps for initial setup
-----------------------

WordPress Initial Setup
'''''''''''''''''''''''

- download source code for WordPress and MediaWiki
- setup database (database user, databases)

- Nginx configruation, WordPress rewrite rules
- WordPress configuration, wp-config.php
- Execute WordPress installation script.
- Set network for WordPress, update configruation.
  The option **WP-ALLOW-MULTISITE** will turn on or off
  the **Tools -> Network Setup** dashboard page.

MediaWiki Initial Setup
'''''''''''''''''''''''

- Nginx configuarion for MediaWiki
- MediaWiki installation script.
- deploy and config WPMW extensions

Configuration Tricks
--------------------

How to set default options for a theme
''''''''''''''''''''''''''''''''''''''

there are some choices for making default options for a theme:

- add_option, sidebars_widgets
- if !dynamic_sidebar() add manual widgets, dynamic_sidebar
  return true or false
- function the_widget could be used to load default widgets.

about WordPress index.php
'''''''''''''''''''''''''

How to remove the index.php in URL.

- after install wordpress at first time, site url is stored in
  table **wp_options** in option_name **siteurl** and **home**.
- if index.php presents on those 2 options, we could remove it 
  from the database manually.
- manually change the installation URL should avoid this problem.
  http://dev.vault.leocorn.com/wp-admin/install.php
