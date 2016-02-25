Cloud Administration
====================

Administration tips on Cloud!

AWS Certificate Manager
-----------------------

AWS Certificate Manager is the comprehensive solution fo SSL/TLS
certificates management, 
including purchasing, uploading, and renewing.

Here are some memos:

- SSL/TLS certificates provisioned through AWS Certificate Manager 
  are free. You pay only for the AWS resources you create to 
  run your application.

Steps to set up SSL/TLS certificates:

- request a certificate from ACM console, you will be
  able to type your domain name here.
- validate domain ownership. a validation email will be send to the
  domain name owner's email.

**AWS CLI**

We need use **AWS CLI** to request a SSL certificate for a subdomain.
Such as **test.example.com**.

- install the AWS CLI client, Python egg.
- create the buildout config file to generate the script.

AWS CLI Basic
-------------

mainly we only need know the following commands:

- aws help
- aws configure
