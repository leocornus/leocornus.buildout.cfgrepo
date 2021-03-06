Deploy SSL Cert on Web Servers
==========================

deploy ssl cert for all Web servers.

mainly the following steps:

- generate key and CSR
- send CSR to get the SSL certificates.  
  Since we have more than one servers, 
  we will need 3 files for the certificates: 
  chain cert, root cert, and server cert
- deploy the certs on each server.

Create CSR
----------

we need OPENSSL for this work. generate the private key

create CSR from the private key::

  $ openssl genrsa -des3 -out example.com.key 2048
  $ openssl req -new -sha1 -key example.com.key -out example.com-sha1.csr
  # remove the passphase.
  $ cp example.com.key example.com.key.org
  $ openssl rsa -in example.com.key.org -out example.com.key

Request Certificate using the CSR
---------------------------------

send the CSR to Certificate provider

Deploy Private Key and Certificate
----------------------------------

We need the Private Key and the Certificates file for Web Server to provide SSL connection

Sample of Nginx configuration
-----------------------------

Just need add this 2 lines::

  ssl_certificate /etc/pki/tls/certs/example.com-ServerCert.crt;
  ssl_certificate_key /etc/pki/tls/private/example.com.key;

Generate Seal
-------------

Here are the seals::

  <script language="javascript" src="https://seal.entrust.net/seal.js?domain=example.com&img=17"></script>
  <a href="http://www.entrust.net">SSL</a>
  <script language="javascript" type="text/javascript">goEntrust();</script>


