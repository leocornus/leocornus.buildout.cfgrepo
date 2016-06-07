AWS IAM
=======

AWS Certificate Manager
-----------------------

AWS Certificate Manager is the comprehensive solution fo SSL/TLS
certificates management, 
including purchasing, uploading, and renewing.

Here are some memos:

- SSL/TLS certificates provisioned through AWS Certificate Manager 
  are free. You pay only for the AWS resources 
  (for example, EC2 instances) you create to run your application.

Steps to set up SSL/TLS certificates:

- request a certificate from ACM console, you will be
  able to type your domain name here.
- validate domain ownership. a validation email will be send to the
  domain name owner's email.

**ERROR: The AWS Access Key Id needs a subscription for the service**

This error message is normally because of the Amazon account is 
not activated properly!
The common reasons are email not confirmed, or credit card not 
authorized.

**AWS CLI**

We need use **AWS CLI** to request a SSL certificate for a subdomain.
Such as **test.example.com**.

- install the AWS CLI client, Python egg.
- create the buildout config file to generate the script.

Force SSL balancer way
----------------------

AWS provides free SSL certificate service.
But the free SSL cert only works on Elastic Load Balancer and
AWS CloudFront.
That tells the SSL certificate is deployed on the balancer 
instead of your EC2 instances.
So you could not set your Web server to listen to port 443.
You only can set up your balancer to direct HTTPS traffic to 
instance port 80.
Here is the simple strategy to force SSL for your balancer:

- balancer port 80 to instance port 8443
- balancer port 443 to instance port 80
- config vitual host on instance port 8443 to redirect all request
  to balancer port 443.
