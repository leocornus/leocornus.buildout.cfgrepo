Buildout Story for taiga-back
==========================================================

taiga-back is maily a Django application.
Buildout is a very efficient tool to manage a Django application.

Benifit
-------

- automated development process the most.
- buildout is born for Python app,
- 

proposal
--------

- create **buildout** folder.
- phase by phase roll out features.

Basic features
--------------

- install dependence eggs
- generate taiga-back script as Django manage script
- install and setup PostgreSQL database.
- load testing data.
- generate various scripts: test, 
- install and config circus

Frontend development
--------------------

Possibly automate the frontend development.

- FRONTEND: install and config Nginx
- FRONTEND: install and config Node.js and npm
- 

First Cut
---------

As to now, supervisor doesn't support Python 3.
So we have to use circus to manage processes.

As cut, we will only have the following on board:

- install PostgreSQL database
- setup PostgreSQL database for taiga-back: create database and 
  user
- create easier Django manage scripts.
