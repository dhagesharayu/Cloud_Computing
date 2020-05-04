#  IAM (Identity Access Managemet)
* Gives you an unique identity which you can attach to any service, It allows Communiaction between two services inside AWS.
* Basically its a Role which has policies which you can attached to any resource/services for authorized access.
![image](https://user-images.githubusercontent.com/63589909/80944079-511ca080-8e06-11ea-94a1-663d481e1627.png)
* Policies are rules(Permissions) such as read only or full access to either a bucket or RDS and so on.
![image](https://user-images.githubusercontent.com/63589909/80944138-71e4f600-8e06-11ea-958e-46351679543f.png)
* Policies regarding an resource or service is attached to an IAM Role and this role is then attached to instance of another service.\
![image](https://user-images.githubusercontent.com/63589909/80944201-98a32c80-8e06-11ea-9362-7278c2a2533d.png)

## Steps to create an IAM role for accessing S3 service (i.e buckets) and Attaching it to instance of EC2.
1. [EC2 creation, launch and SSH](https://github.com/dhagesharayu/Cloud_Computing/blob/Services/EC2.md)
2. [Bucket creation and how to store data](https://github.com/dhagesharayu/Cloud_Computing/blob/Services/S3.md)
### IAM Role Creation:
1. Login into AWS console and search for IAM in service search bar at the top.
![image](https://user-images.githubusercontent.com/63589909/80945030-832f0200-8e08-11ea-86ba-2d60ccde8460.png)
2. Next will be able to see IAM dashboard, click on Roles on left corner.
![image](https://user-images.githubusercontent.com/63589909/80945151-cdb07e80-8e08-11ea-9e38-8c329941b236.png)
3. You will see all existing roles, you can either select an existing one or create new.
![image](https://user-images.githubusercontent.com/63589909/80945355-4283b880-8e09-11ea-8d98-bf7a77203636.png)
* Click on create role.
4. Select AWS service, choose EC2 in use case and click on Next:permission.
![image](https://user-images.githubusercontent.com/63589909/80945421-6810c200-8e09-11ea-99b0-8748b6a2535b.png)
5. Next click on attach policies.\
![image](https://user-images.githubusercontent.com/63589909/80946621-1158b780-8e0c-11ea-8821-6750b9192533.png)
6. You will see this, search S3 in filter policy.\
![image](https://user-images.githubusercontent.com/63589909/80946703-3cdba200-8e0c-11ea-9106-57cc09602078.png)
* You can select either S3 readonly or full access.
* Click on drop down besides the policy you selected and again click on JSON.
![image](https://user-images.githubusercontent.com/63589909/80946805-7ad8c600-8e0c-11ea-861a-8bcb149ea5b2.png)
* You will see policy is written in json format.
* Here you can specify a specific bucket_name in action i.e "Action":"S3:bucket_name", then only permission for this bucket will be given.
7. Click on Next:tags in the as seen in step 6.
8. Adding tags is optional, directly click on Next:Review.
![image](https://user-images.githubusercontent.com/63589909/80947039-f33f8700-8e0c-11ea-9382-f908db1fa81d.png)
9. Give Name and descriptional to your IAM Role and click on create role.
![image](https://user-images.githubusercontent.com/63589909/80947136-241fbc00-8e0d-11ea-9fab-7fae15737bf6.png)
10. Congrats! Your IAM Role has been created.\
![image](https://user-images.githubusercontent.com/63589909/80947307-824c9f00-8e0d-11ea-97ed-24b7cc47c37e.png)
11. Now login into your EC2 dashboard and click on runing instance.
![image](https://user-images.githubusercontent.com/63589909/80947974-db690280-8e0e-11ea-8062-5db229b0f4af.png)
* If its stopped, then select your instance, select action and start as shown above.
12. Now to attach youe Role to this instance, select the instance, go to action, instance setting and select Attach/Replace IAM Role.\
![image](https://user-images.githubusercontent.com/63589909/80948143-271bac00-8e0f-11ea-8617-e256545dfc73.png)
* You will see this screen.\
![image](https://user-images.githubusercontent.com/63589909/80948342-824d9e80-8e0f-11ea-9a74-9e0a0446f3b4.png)
13. Instance Id is automatically filled in, its Id of the instance you are attaching the role to.
14. Click on the drop down besides IAM Role and select the Role you created, i.e MyIamRole and click on Apply.
15. You are almost done.\
![image](https://user-images.githubusercontent.com/63589909/80948588-0c960280-8e10-11ea-9245-4f23ca278a24.png)
16. Now in the EC2 linux terminal you will be ale to access all buckets in your account. 
![image](https://user-images.githubusercontent.com/63589909/80948813-7a422e80-8e10-11ea-847d-d6b58827e9f6.png)
* ```aws s3 ls``` command list all the buckets in your account.
* Now you can manipulate all buckets using your EC2.

### [For more info on IMA](https://aws.amazon.com/iam/)
### [IAM Troubleshooting](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot.html)
