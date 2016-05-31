SQL tips for WordPress
======================

Some interesting SQLs::

  select concat('prefix', path) from wp_blogs 
  where path not in 
  (select concat('/', user_login, '/') from wp_users) 
  order by path 
  into outfile '/home/sean/blog.list';

The **into outfile** will have the query result into a file.
