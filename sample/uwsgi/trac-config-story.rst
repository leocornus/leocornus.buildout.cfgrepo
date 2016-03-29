Trac Configuration Story
========================

How to customize template for notification email
------------------------------------------------

`TracNotification <https://trac.edgewall.org/wiki/TracNotification>`_
has most of the detials.

content template location::

  trac/[PROJECT-NAME]/templates/

Have to restart trac after update the template.

Here is a sample to add more links to the content template::

  ${_('Project Homepage: \
    <http://example.com/projects/?project=%(project)s>', \
    project=ticket.project)}
  ${_('All Projects: <http://example.com/projects/>')}

The back-ward slash (\) is needed for multiple lines.
