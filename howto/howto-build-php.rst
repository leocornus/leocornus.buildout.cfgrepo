
Some sample buildouts to build PHP.

PHP with krb5 Extension
=======================

php-krb5 is an extenstion to make PHP interface with Krb 5 libs.

.. code-block:: ini
    [buildout]
    extends = 
        cfgrepo/config/php-build-with-krb5.cfg

    parts = 
        php-krb5
        enable-krb5
        php-build

    # tweak the php-build options here.
    [php-build]
    php-build-libdir-options =
    # options for 64 bit hardware, comment out 
    # them for a 32 bit hardware
        --libdir=${buildout:directory}/parts/php-build/lib64
        --with-libdir=lib64
