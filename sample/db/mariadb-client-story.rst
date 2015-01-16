`Database Build and Config <README.rst>`_ >
Story about Building MariaDB Client

wget settings
-------------

In some case, we want skip the certificate check when
we try to download the source code. 
The **~/.wgetrc** is the best choice::

  # (find-es "wget" "--no-check-certificate")
  # (find-wgetnode "HTTPS (SSL/TLS) Options" "`--no-check-certificate'")
  # (find-wgetnode "Wgetrc Commands" "check_certificate = on/off")
  check_certificate = off

cmake options
-------------

The cmake options **-DWITHOUT_SERVER=1** will make sure only
MariaDB client is built.
