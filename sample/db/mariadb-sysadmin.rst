`Database Build and Config <README.rst>`_ >
MariaDB System Admin in A Nutshell

MariaDB System Information
--------------------------

The following commands will help you get system information about
MariaDB database server::

  MariaDB > SHOW VARIABLES LIKE '%version%';
  MariaDB > SELECT version();

How to check the size of a MariaDB database?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MariaDB has a system database called **information_schema**,
which have all details information for 
any database on a MariaDB server.
The following SQL will show the database size in MB::

  MariaDB > use infomation_schema;
  MariaDB > select table_schema "DB Name", 
         -> Round(Sum(data_length + index_length) / 1024 / 1024, 1) 
         -> "DB Size in MB" from tables where table_schema = 'xampp';

We could use **Group by table_schema** to get the size for 
each database.
