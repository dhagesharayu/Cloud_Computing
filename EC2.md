# EC2 (Elastic Compute Cloud)
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
#### [More info on EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
## Guide to launch EC2 Instance (AWS)
1. Login into your AWS console, Search for ```EC2``` in your services search bar and select EC2.
![image](https://user-images.githubusercontent.com/63589909/80907204-750eb200-8d32-11ea-873b-3f292dc04e52.png)
2. You will see your EC2 dashboard, scroll down and you will see launch instance click on it.
![image](https://user-images.githubusercontent.com/63589909/80907227-f2d2bd80-8d32-11ea-9c6b-c9fdb68d4b14.png)
3. Now select the AMI i.e OS you want for your EC2, I am selecting Linux.Click on select.
![image](https://user-images.githubusercontent.com/63589909/80907240-139b1300-8d33-11ea-8cac-7691ef7ffc76.png)
* You can select windows, ubuntu etc.
4. Here you can select instance type i.e core(CPU's), Memory(Ram), I am selecting T2.micro and click on Configure details.
![image](https://user-images.githubusercontent.com/63589909/80907333-e69b3000-8d33-11ea-9939-0b353215ecac.png)
* For more details on instance type click below:
* [AWS instance type](https://aws.amazon.com/ec2/instance-types/)
5. Keep everthing default on configure instance details and directorly click on add storage.
![image](https://user-images.githubusercontent.com/63589909/80907409-9d97ab80-8d34-11ea-9ac0-59aa1a13b679.png)
6. Here you can select the size and type of storage or also add another volume by clicking on add volume. 
![image](https://user-images.githubusercontent.com/63589909/80907445-e0598380-8d34-11ea-9d15-784089216738.png)
* Once done click on add Tag.
7. Tag acts like Identity?name for your EC2 to be easily identify. you can add multiple tags but 1 is more
than enough.
![image](https://user-images.githubusercontent.com/63589909/80907523-9e7d0d00-8d35-11ea-8a6b-5fa35a41e6e1.png)
9. After adding tag click on Configure security group.
![image](https://user-images.githubusercontent.com/63589909/80907608-14817400-8d36-11ea-9344-d0f02300f33f.png)
* here you can create a security group give it any name and description, but if you already have and existing group you can use it.
* Details such as type of connection, protocol, source etc are given.
* Since we are going to connect through SSH, port 22 and TCP has been automatically selected. Source can be custom(i.e specific IP),
My IP(i.e Only you can connect) or anywhere(i.e)anyone can connect to your ec2 if its running.
* If you are using existing security group just make sure above details have been configure in Inbound rules in security group.
10. Click on review and launch, you can make any change you want in review and then launch it.
11. You will get this window, select create a new key and give a name and download the key, it will be a .pem extension
![image](https://user-images.githubusercontent.com/63589909/80908001-83ac9780-8d39-11ea-80e2-b9644e8147ce.png)
* The key is a RSA encryted key you cannot use your ec2 without it so keep it safety in a folder, as you will require it everytime you use this instance.
* Now click on launch
12. Once launch go to your ec2 dashboard, it will show 1 running instance, click on it.
![image](https://user-images.githubusercontent.com/63589909/80907811-8b6b3c80-8d37-11ea-8430-cbbe7093c588.png)
13. You will see your ec2
![image](https://user-images.githubusercontent.com/63589909/80907827-a5a51a80-8d37-11ea-9678-0df35f76e135.png)
14. Since my local os is Windows, i will need a third party app to comunicate with my EC2 instance, i am using the one mentioned below:
* [Mobaxterm](https://mobaxterm.mobatek.net/download-home-edition.html)
* I downloaded the portable edition
15. Once you install this application and run it click on session on top left corner.
![image](https://user-images.githubusercontent.com/63589909/80908282-41d12080-8d3c-11ea-81d5-eb596101eba6.png)
16. you will get this.
![image](https://user-images.githubusercontent.com/63589909/80908309-6f1dce80-8d3c-11ea-8d59-139bde42b672.png)
* Click on specify username and fill the details such as user:```ec2-user```.
* Click on advanced SSH setting, check the use key box and browse and slect the key(.pem file) you downloaded earlier.
* Enter Public Ip from instance details shown below in the Remote host box mentioned in above image.
![image](https://user-images.githubusercontent.com/63589909/80908433-624daa80-8d3d-11ea-8a03-6a50faae5f09.png)
* Click on ok on ssh connection box.
17. Your connection has been established, now you can communicate with your ec2.
![image](https://user-images.githubusercontent.com/63589909/80908517-1fd89d80-8d3e-11ea-8fe8-779c35eeac63.png)
18. Once done you can start, stop or terminate your insatance as shown below.
![image](https://user-images.githubusercontent.com/63589909/80908557-662dfc80-8d3e-11ea-8f35-1a48a4345f5c.png)
19. You can also change any of its configuration as shown below, just stop the instance make the changes and start it.
![image](https://user-images.githubusercontent.com/63589909/80908562-71812800-8d3e-11ea-8c57-d3856787d6cd.png)

### [If you have trouble connecting to your linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)




