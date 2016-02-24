Build Story for Applications
============================

Here are list applications:

- WordPress
- WordPress plugins
- WordPress themes
- MediaWiki
- MediaWiki Extensions
- MediaWiki Skins

TODO:

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

How to set default options for a theme
--------------------------------------

there are some choices for making default options for a theme:

- add_option, sidebars_widgets
- if !dynamic_sidebar() add manual widgets, dynamic_sidebar
  return true or false
- function the_widget could be used to load default widgets.
