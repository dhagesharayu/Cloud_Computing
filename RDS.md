# RDS(Relational DataBase)
* Its a Saas, i.e it provides database as a service.
* It is used to set up, manage and scale a relational database instance in the cloud.
* You create, configure, manage and delete an RDS instance, which is a cloud database environment, along with the compute and storage resources it uses.
* It is Cost-effective,pay as you go and whatever the usage and resources you used, you are charged accordingly.
* It just takes a few minutes to scale your infrastructure up or down.
* There are six database engines which RDS provides, and they are:
1. Amazon Aurora 
2. PostgreSQL 
3. MySQL 
4. MariaDB 
5. Oracle Database 
6. Microsoft SQL Server
* Once the database is created and the status is changed to Available you need to connect it with your local MySQL shell and can perform operations.
### How to create and access the database.
1. Login into your aws console and search for RDS in service search bar.
![image](https://user-images.githubusercontent.com/63589909/80910837-ee68cd80-8d4f-11ea-9637-c4f85ad8f8c3.png)
2. You wiil see your RDS dashboard, click on create Database.
![image](https://user-images.githubusercontent.com/63589909/80910859-0c363280-8d50-11ea-8572-9739aafb6a97.png)
3. Choose standard creation.\
![image](https://user-images.githubusercontent.com/63589909/80910876-2b34c480-8d50-11ea-8d94-01dfe6579fef.png)
4. Select MYSQL in Engine Option, you can choose another if you want.
![image](https://user-images.githubusercontent.com/63589909/80910890-40115800-8d50-11ea-95bf-8d5124e67476.png)
5. Choose the default mysql version or choose the one compatible with yor mysql server or workbench.
![image](https://user-images.githubusercontent.com/63589909/80910924-7b138b80-8d50-11ea-926e-050663880083.png)
6. Select the free tier template.\
![image](https://user-images.githubusercontent.com/63589909/80910934-91b9e280-8d50-11ea-9a1f-2dd5cd27e7e4.png)
7. Write the name what your database to be called in identifier.
![image](https://user-images.githubusercontent.com/63589909/80910947-ac8c5700-8d50-11ea-8a65-7ffef27c3fc8.png)
* In credentials write username and password, but remember it as you will require it everytime you want to connect to this database.
8. Leave rest details default.\
![image](https://user-images.githubusercontent.com/63589909/80911617-fe36e080-8d54-11ea-9ccc-66e7d84e5032.png)
9. Only in additional connectivity configuration under connectivity.
![image](https://user-images.githubusercontent.com/63589909/80911640-27f00780-8d55-11ea-8e37-2293c133ca90.png)
* Select yes for publicly accesible.
10. Leave rest configuration default(as it is) and click on create database.
![image](https://user-images.githubusercontent.com/63589909/80911693-9b921480-8d55-11ea-9198-ca87e6b48316.png)
11. Now you can see the database you created on dashboard.
![image](https://user-images.githubusercontent.com/63589909/80911731-d1cf9400-8d55-11ea-8e1d-62ada9439aa1.png)
12. But it takes some time for creation and backup.\
![image](https://user-images.githubusercontent.com/63589909/80911736-da27cf00-8d55-11ea-803a-e61d39dcaef1.png)
![image](https://user-images.githubusercontent.com/63589909/80911737-e01db000-8d55-11ea-9304-9f42e998c994.png)
13. Your Database is now Available for use.
![image](https://user-images.githubusercontent.com/63589909/80911739-e6ac2780-8d55-11ea-85c5-ade5937e18cb.png)
14. Click on your database name.\
![image](https://user-images.githubusercontent.com/63589909/80911741-eca20880-8d55-11ea-945b-cbd7ca16ec60.png)
15. You will see details related to your database.
![image](https://user-images.githubusercontent.com/63589909/80911748-fd527e80-8d55-11ea-85e0-ca29527537d3.png)
16. click on security group and you will see this:\
![image](https://user-images.githubusercontent.com/63589909/80911752-04798c80-8d56-11ea-9ada-592c438c78c8.png)
17. select the security group and click on its names and select inbound rules.
![image](https://user-images.githubusercontent.com/63589909/80911756-0b080400-8d56-11ea-91c2-a3a7eee499a2.png)
18. There is no connection on port no 3306 which you require for your database to connect, so click on add rule. 
![image](https://user-images.githubusercontent.com/63589909/80911757-0fccb800-8d56-11ea-9aa9-3c30663d07ff.png)
19. Configure the rule as below and compare with step 15, i.e port no and connection type.
![image](https://user-images.githubusercontent.com/63589909/80911760-15c29900-8d56-11ea-9ba4-1479f0915991.png)
18. click on save rules.\
![image](https://user-images.githubusercontent.com/63589909/80911762-1a874d00-8d56-11ea-864a-0fcde06a7566.png)
19. You will see your rule has been added.\
![image](https://user-images.githubusercontent.com/63589909/80911765-207d2e00-8d56-11ea-9472-d630484a9dfe.png)
20. Login into your mysql workbench.\
![image](https://user-images.githubusercontent.com/63589909/80911795-3f7bc000-8d56-11ea-9e9d-c4728689c4ee.png)
* click on the **+** besides the Mysql Connections.
21. You will get this pop up window.\
![image](https://user-images.githubusercontent.com/63589909/80911803-486c9180-8d56-11ea-9db0-a96da37baa74.png)
22. Configure it as belows:\
![image](https://user-images.githubusercontent.com/63589909/80911806-4d314580-8d56-11ea-8902-53846e35d9c4.png)
* Enter endpoint from aws datase detail i.e the URL from Step 15 and copy it into host name.
* Enter the name and password which you used during database creation in step 7.
![image](https://user-images.githubusercontent.com/63589909/80911808-54585380-8d56-11ea-8ef1-fc594468cde8.png)
23. Click on ok. you will get this.\
![image](https://user-images.githubusercontent.com/63589909/80911809-5a4e3480-8d56-11ea-89bf-b35e86954097.png)
24. Now you are connected to your database and can use it, i.e create a schema timepass. 
![image](https://user-images.githubusercontent.com/63589909/80911816-5fab7f00-8d56-11ea-815a-31d0bafecafb.png)
* Created a table in it and so on, you can perform any relational operation on it.
![image](https://user-images.githubusercontent.com/63589909/80911826-689c5080-8d56-11ea-88d8-824824323ca4.png)
![image](https://user-images.githubusercontent.com/63589909/80911830-6c2fd780-8d56-11ea-9f96-86351f1c2b00.png)
![image](https://user-images.githubusercontent.com/63589909/80911838-74881280-8d56-11ea-9e64-f8bdfd3c0c90.png)
![image](https://user-images.githubusercontent.com/63589909/80911850-79e55d00-8d56-11ea-8b79-11c33266f236.png)
25. Once done you can simply select your database and go to action and stop or if not required terminate it.
![image](https://user-images.githubusercontent.com/63589909/80911858-7eaa1100-8d56-11ea-9970-77b18d54ded7.png)
* Or you could also change some of its configuration and restart it.
### [For more information on AWS RDS](https://docs.aws.amazon.com/rds/index.html?nc2=h_ql_doc_rds) 
