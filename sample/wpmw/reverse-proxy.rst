Using reverse proxy for WordPress 
=================================

Some ideas about using reverse proxy to use show blog in 
WordPress single site.

Sample on Apache HTTPD
----------------------

This sample is trying to provide a separate frontend for
WordPress backend.
Here are what it try to archive:

- a frontend **front.example.com** to present the site for
  all users including anonymous users.
- the backend **contrib.example.com** for conbributers.

This setup including two parts: HTTPD config and WordPress config.

HTTPD config is using VirtualHost::

  <VirtualHost front.example.com:80>
    ServerAdmin postmaster@example.com
    ServerName front.example.com
    DocumentRoot "/projects/xampp/www/frontend/public"
    <IfModule mod_proxy.c>
    #
    # Reverse Proxy
    #
    ProxyRequests On
    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>
    ProxyVia On
  
    ProxyPass /wp-content/ http://contrib.example.com/wp-content/
    ProxyPassReverse /wp-content/ http://contrib.example.com/wp-content/
  
    ProxyPass /wordpress/ http://contrib.example.com/wordpress/
    ProxyPassReverse /wordpress/ http://contrib.example.com/wordpress/
  
    ProxyPass /wp-json/ http://contrib.example.com/wp-json/
    ProxyPassReverse /wp-json/ http://contrib.example.com/wp-json/
  
    ProxyPass /api/nonce http://contrib.example.com/api/nonce
    ProxyPassReverse /api/nonce http://contrib.example.com/api/nonce
    ProxyPreserveHost Off
    </IfModule>
  </VirtualHost>
  
  <VirtualHost contrib.example.com:80>
    ServerAdmin postmaster@example.com
    DocumentRoot "/projects/xampp/www/contrib"
    ServerName contrib.example.com
  </VirtualHost>

Backend WordPress config need set up the pathes to match the
frontend URL::

  // set paths
  define('WP_CONTENT_URL', 'http://front.example.com/wp-content');
  define('WP_SITEURL', 'http://front.example.com/wordpress');
  define('WP_HOME', 'http://front.example.com/');
  define('WP_CONTENT_DIR', sprintf("%s/%s", __DIR__, 'wp-content'));
  define('UPLOADS', sprintf("%s/%s", __DIR__, 'uploads'));

Here the foler structure for **www/contrib**, the WordPress backend::

  uploads/
  vendor/
  wordpress/
  wp-content/
  index.php
  wp-config.php

The file **index.php** has to be copied to the **www/contrib** folder.
It will have the following content::

  <?php
  
  define('WP_USE_THEMES', true);
  
  /** Loads the WordPress Environment and Template */
  require( dirname( __FILE__ ) . '/wordpress/wp-blog-header.php' );
