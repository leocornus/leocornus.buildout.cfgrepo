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

Create instance from dashboard
------------------------------

- using lunch instance button
- go through the wizard.
- pick or setup security group, set the firewall,
  allow or disallow network traffic, for example traffic for
  port 22, 80, 443, etc.
- enable public ip
- boot device and storage device, how to add storage device:
  attach, mkfs and mount.
- nees set up the key-pair when launch the instance.
  there is only one change to download the 
  private key. Store it properly!

Once the instance is running, we could using the private key 
to access the instance::

  $ ssh -i my-key.pem 23.12.34.56

**Storage Device**

- need attach the ebs volume to an instance.
- how to mount the storage device?

The page `Making a Volume Available for Use <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html>`_
has details instruction.

Here is a brief summary::

  $ lsblk ; help find the device name
  $ file -s /dev/xvdb ; help check the device has file system or not
  $ mkfs -t ext4 /dev/xvdb ; help to make a file system 
  $ mkdir /mount/point
  $ mount /dev/xvdb /mount/point

To auto mount on system reboot, need add the new device to file
**/etc/fstab**.

- make backup first
- add new line for the new device, need pay attention on the mount
  options. **nofail** and **nobootwait** must be used for Ubuntu.
- using command **mount -a** to test to make sure.

here is example for Ubuntu::

  /dev/xvdb /usr/opt defaults,nofail,nobootwait 0 2

**Cost!**

- $0.10 per GB-month of provisioned storage for type (gp2)

For example, 100GB will cost $10 / month

**Using Strategy**

- start from small, for example 30GB.
- organize the volume properly: boot volume, data, system (including logs)
- start from all in one, as it grow create different volumes
  to mount on different folders.
- we could attach new volume
- we could extend an existing volume

**Expanding a Volume**

basically, follow the following setps.

- stop the instance, make sure not terminame the storage volume.
- create a snapshot of your existing volume
- create new volume from the snapshot
- detach the old volume
- attach the new volume with the same device name.
- restart instance
- extending the Linux file system.
- verify the new volume to make sure everything is ok.
- delete the old volume

More details on page `Expanding a Vlume <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-expand-volume.html>`_
