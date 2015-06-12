Sys Admin for PostgreSQL Database
=================================

start server
::

  $ bin/postgres -D /data/dir/full/path
  $ bin/pg_ctl start -D /data/dir/full/path -l /path/to/logfile

create database
::

  $ bin/createdb DB_NAME

access database.
::

  $ bin/psql DB_NAME
