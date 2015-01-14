`Database Build and Configuration <README.rst>`_ > 
MariaDB Tuning Story

Basic Commands
--------------

Here are some basic MariaDB system admin commands::

  MariaDB > SHOW GLOBAL STATUS;
  MariaDB > SET GLOBAL thread_cache_size = 16;
  MariaDB > SHOW GLOBAL STATUS LIKE 'threads%';
  MariaDB > SHOW GLOBAL STATUS LIKE 'innodb_buffer%';
  MariaDB > SHOW VARIABLES LIKE 'query%';
  MariaDB > SHOW Warnings;

Some numbers::

  4GB 4294967295
  1GB 1073741823

Production Parameters
---------------------

There are 2 main categories of parameters we can tweak the 
database performance: general params and innodb params.

General Params::

  #key_buffer_size = 16K
  key_buffer_size = 128M
  #max_allowed_packet = 1M
  max_allowed_packet = 64M
  #table_open_cache = 4
  table_open_cache = 4
  sort_buffer_size = 64K
  read_buffer_size = 256K
  read_rnd_buffer_size = 256K
  net_buffer_length = 2K
  thread_stack = 128M
  thread_cache_size = 16
  query_cache_size = 1024M
  join_buffer_size = 128M
  
  myisam_sort_buffer_size = 512M
  # default value for max connection is 150
  max_connections = 20000
  max_heap_table_size = 128M
  tmp_table_size = 128M
  table_cache = 75000

innodb params::

  # You can set .._buffer_pool_size up to 50 - 80 %
  # of RAM but beware of setting memory usage too high
  #innodb_buffer_pool_size = 16M
  innodb_buffer_pool_size = 1024M
  #innodb_additional_mem_pool_size = 2M
  # Set .._log_file_size to 25 % of buffer pool size
  #innodb_log_file_size = 5M
  innodb_log_buffer_size = 16M
  #innodb_flush_log_at_trx_commit = 1
  #innodb_lock_wait_timeout = 50
  innodb_read_io_threads = 8
  innodb_write_io_threads = 8

This post `INNODB VARIABLES AND STATUS EXPLAINED 
<http://www.fromdual.com/innodb-variables-and-status-explained>`_
has a good calculation for the innodb_buffer_pool_size.

MySQL Tunner Output
-------------------

On January 13, 2015::

  -------- Performance Metrics -------------------------------------------------
  [--] Up for: 6d 0h 50m 43s (76M q [147.544 qps], 1M conn, TX: 6160B, RX: 21B)
  [--] Reads / Writes: 95% / 5%
  [--] Total buffers: 1.2G global + 832.0K per thread (20000 max threads)
  [!!] Maximum possible memory usage: 17.0G (212% of installed RAM)
  [OK] Slow queries: 0% (1K/76M)
  [OK] Highest usage of available connections: 1% (381/20000)
  [OK] Key buffer size / total MyISAM indexes: 128.0M/2.0G
  [OK] Key buffer hit rate: 99.9% (1B cached / 1M reads)
  [!!] Query cache is disabled
  [OK] Sorts requiring temporary tables: 5% (299K temp sorts / 5M sorts)
  [!!] Joins performed without indexes: 7882
  [!!] Temporary tables created on disk: 34% (2M on disk / 6M total)
  [!!] Thread cache is disabled
  [OK] Table cache hit rate: 38% (43K open / 112K opened)
  [OK] Open file limit used: 64% (42K/65K)
  [OK] Table locks acquired immediately: 99% (81M immediate / 81M locks)
  
  -------- Recommendations -----------------------------------------------------
  General recommendations:
      Reduce your overall MySQL memory footprint for system stability
      Enable the slow query log to troubleshoot bad queries
      Adjust your join queries to always utilize indexes
      When making adjustments, make tmp_table_size/max_heap_table_size equal
      Reduce your SELECT DISTINCT queries without LIMIT clauses
      Set thread_cache_size to 4 as a starting value
  Variables to adjust:
    *** MySQL's maximum memory usage is dangerously high ***
    *** Add RAM before increasing MySQL buffer variables ***
      query_cache_size (>= 8M)
      join_buffer_size (> 128.0K, or always use indexes with joins)
      tmp_table_size (> 16M)
      max_heap_table_size (> 128M)
      thread_cache_size (start at 4)
