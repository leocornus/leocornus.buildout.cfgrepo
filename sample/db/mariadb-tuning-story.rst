`Database Build and Configuration <README.rst>`_ > 
MariaDB Tuning Story

Basic Commands
--------------

Here are some basic MariaDB system admin commands::

  MariaDB > SHOW GLOBAL STATUS;
  MariaDB > SET GLOBAL thread_cache_size = 16;
  MariaDB > SHOW GLOBAL STATUS LIKE 'threads%';
  MariaDB > SHOW VARIABLES LIKE 'query%';
  MariaDB > SHOW Warnings;

Some numbers:

  4GB 4294967295
  1GB 1073741823

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
