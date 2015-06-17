Taiga Story
===========

Try to set up development environment for Taiga,
both backend and frontend.

Dependences
-----------

Taiga depends on the following softwares:

- Python >= 3.4
- PostgreSQL >= 9.3
- Django > 1.7
- Circus or Supervisord, circus is better as Supervisord 
  is not working on Python 3 until version 4.0

Setup Steps for backend
-----------------------

#. clone **taiga-back** to src folder.
#. create buildout config file by extending `buildout-taiga.cfg
   <buildout-taiga.cfg>`_
#. update users, ports, hosts 
#. install part **init-postgresql** to create database.
#. install part **create-taiga-db** to create database with 
   owner taiga
#. import basic data by running migrate, loaddata, compilemessages,
   and collectstatic. Reference 

Taiga Agile Concept
-------------------

Taiga has the following basic concepts:

- blocks: sprint, user story, task, issue
- members
- roles: UX, Front, Back, Design, Stakholder, Tester, etc
- views: project backlog, sprint taskboard
- Points:

Operation highlight

- Project is built up with stories and issues
- Backlog will be a parking lot for all pending stories.
- Ability to turn an issue to a story
- Sprint is used to group stories into a 2-week period.
- Tasks are used to break down a story to small pieces of work
- Team member could be assigned to task or story
- Allow tasks without a story (Unassigned Tasks)
- Ability to customize status, priorities, severities
- Ability to create custom fields for story, task and issue
- Ability to customize team member roles for a Project. Default roles   include Design, Front, Back, UX, Stakeholder, External user, Design,
  Production Owner.
- Ability to assign points for different roles on a story.
- Points for a story is the total number of points from different
  roles.
- Ability to add member to a project.
- Ability to manage permissions for different roles on different
  blocks: Sprint, User story, task, issue

UX highlight

- Sprint Taskboard is very intuitive: very nice view and 
  drag and drop tasks between stories and across status.
- Backlog view has full list of parking stories and a list of 
  running sprint.
- Backlog view has the ability to drag and drop stories to sprints

Development fiendly features

- Comprehensive REST APIs
- Ability to integrate with Github, Gitlab, Bitbucket

We need the following thing to get understand how Taiga Agile works?

- Story lifecycle
- Task lifecycle
- Sprint lifecycle
- Project lifecycle

Questions
---------

**How to change the binding IP for taiga backend?**

using the Django command line options, for example::

  $ ../bin/taiga-back runserver 10.160.192.20:8000


