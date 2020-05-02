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
