# SNS
1. Login into your aws console and search for SNS in your service search bar.

![image](https://user-images.githubusercontent.com/63589909/81083064-bc06ce00-8f11-11ea-887e-f4e8d47aec53.png)

2. Enter the topic name on right corner create topic window and click on next step.

![image](https://user-images.githubusercontent.com/63589909/81083182-e062aa80-8f11-11ea-8140-102554e65c11.png)

3. You will be able to see this on your screen, enter display name and scroll down.

![image](https://user-images.githubusercontent.com/63589909/81083239-f40e1100-8f11-11ea-9d2b-5e9daefd8444.png)

 
4.Encryption is optional, if you feel your data, i.e the message is critical than encrypt it.

![image](https://user-images.githubusercontent.com/63589909/81083412-2f104480-8f12-11ea-9e38-79e84e8f917f.png)

5.Choose Everyone for who can publish this message as we plan for s3 to publisher.

![image](https://user-images.githubusercontent.com/63589909/81083476-44856e80-8f12-11ea-84e8-7f9250e50898.png)

6.Choose Everyone for who can subscribe as we want user to receive an email.

![image](https://user-images.githubusercontent.com/63589909/81083566-5f57e300-8f12-11ea-9e35-bd7ef214edf1.png)

7. Delivery retry policy and tags are optional as we are sending an email.

![image](https://user-images.githubusercontent.com/63589909/81083660-7bf41b00-8f12-11ea-847f-5f205c123112.png)

8.  Click on dropdown besides delivery status logging and scroll down, you will see this.

 
*Choose create new service role and click on create new roles.
9. You will go on a new web tab as shown below, you can view policy details and click on allow. 
 
10 .Your IAM roles will be created.	
11. Now as soon in Step 8 click on use an existing role, it will ask for IAM role details.
 
*To get this IAM Role ARN, login into your IAM dashboard , select roles and left corner and search for SNS in search bar, as that is what you named your created role.
10. You wiil see this, click on the role.

 

12. Copy the Role ARN as it is and paste it, as shown in step 10.
 
13.Copy this also as shown in step ten. 
 
14.Scroll down and click on create topic.
 
15. Now click on topic in top left corner, you will see your created topic.
 
16.Scroll down and click on create Subscription.














6.Choose Everyone for who can subscribe as we want user to receive an email.
 
7. Delivery retry policy and tags are optional as we are sending an email.
 





8.  Click on dropdown besides delivery status logging and scroll down, you will see this.

 
*Choose create new service role and click on create new roles.
9. You will go on a new web tab as shown below, you can view policy details and click on allow. 
 
10 .Your IAM roles will be created.	
11. Now as soon in Step 8 click on use an existing role, it will ask for IAM role details.
 
*To get this IAM Role ARN, login into your IAM dashboard , select roles and left corner and search for SNS in search bar, as that is what you named your created role.
10. You wiil see this, click on the role.

 

12. Copy the Role ARN as it is and paste it, as shown in step 10.
 
13.Copy this also as shown in step ten. 
 
14.Scroll down and click on create topic.
 
15. Now click on topic in top left corner, you will see your created topic.
 
16.Scroll down and click on create Subscription.
