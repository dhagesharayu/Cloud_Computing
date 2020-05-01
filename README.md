# **Cloud Computing**
It means computing resources as rent, wherein\
compute means using, rent means pay as you go i.e on demand and resources can be anything but generally accounts for 
different types of clouds such as:
1. **Public Cloud:** 
  - *Anyone can use it i.e company, school, individual but you have to pay for it.*
  - *for example the cloud that we are using from AWS.*
  - *here vendors gives a ready to cloud to user.*
2. **Private Cloud:** 
  - *owned by and organization, i.e only people authorized by the organization can use it*
  - *for example if vita had a private cloud than only the employees and person authorized by vita would have access*
3. **Hybrid Cloud:**
  - *Combination of Private and Public cloud.*
  - *for example if Vita had an hybrid cloud than the private part would be for the employees and the public part would be                     for students.*\
All the above mentioned clouds have to be payed for.
---
## Advantages
1. Lower cost:
  - *as rent is pay as you go and not on contract*
  - *It is calculate on per hour basis and also what resources you are using and for how much time*
2. Scale up and down on demand i.e resources etc.
3. Provides faster processing and download speed, free internet, electricity as long as you are using it(running).
4. Faster development and deployment.
5. Outsource management, administration(backend) handled by provider of cloud computing services.
---
## Services
Various computing, storage, ML etc. services are provided.


## EC2 (Elastic Compute Cloud)
* Its a IAAS, i.e it provides infrastructure (raw computing resources) as a service.
* Its basically you get a laptop or desktop but not physically, it will be present at your respective datacentre.
* It also has all resources that are present in your laptop such as processor, RAM, OS, volume(SSD).
* All this resources are scalable i.e can be changed.
* Its instance is created and in becomes available very quickly as compared to your physical PC.
* It has a security group which is similar to firewall in your windows operarting system which has Inbound and outbound rules\
  responsible for network traffic control.
* **Inbound Rule:** used to control the incoming traffic by enabling/disabling port/s and source.
* **Outbound Rule:** used to control the outgoing traffic by enabling/disabling port/s and source.
* You (Local) can remotely login into your EC2(Datacentre can be anywhere) through SSH.
* Costing:  
1. If is instance is running then you are charged on the basis of resources being used per hour.
2. If the instance is stopped then you are charged only for the volume per hour as it cannot be given to other, unless you terminate the EC2.

## S3 (Simple Storage Service)
* Its a scalable storage engine.
* It also gives backup
* Any type of data can be stored as an object, but it cannot be stored directly.
* A **Bucket** needs to be created, its name should be unique across entire Cloud(Globally).
* Once a bucket has been created, inside it you can upload and download from any file or create another bucket.
* Only the root bucket needs to be unique.
* You can store unlimited data into it.
* You can also do **Web Hosting** in it.

## RDS(Relational DataBase)
* Its a Saas, i.e it provides database as a service. 

