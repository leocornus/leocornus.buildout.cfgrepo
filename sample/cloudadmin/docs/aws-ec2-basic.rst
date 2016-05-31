EC2 in Basic
============

Basic usage for aws ec2 command.

list all instances
------------------

The command **describe-instances** will list all instances in
JSON format. Here is an example to list all instances id.::

  $ aws ec2 describe-instances
  $ aws ec2 describe-instances | grep InstanceId

All fields are following the capitalized convention. 
Here are some important fields:

- InstanceId

Crate an instance
-----------------

Using command **create-instance**

minimium requirement and options:

- stack-id, 
- layer-ids
- instanc-type
