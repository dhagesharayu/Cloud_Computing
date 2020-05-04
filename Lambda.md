# LAMBDA
* Its a serverless service.
* You are only charged for code execution and not for its storage.
* You are charged only on the basis of CPU, RAM etc i.e the resources required during the execution duration of code.
* Its major advantage is Scalability and Parallelization.
* **Scalability:** As you change or update the code and execute it AWS automatically configures the resources required.
* **Parallelization:** There is no need for your program to be multithreaded. Lambda function does it automatically.
## Lambda function(python) creation and testing.
<details>
<summary>Steps</summary>
<br>

1. Login into your AWS console and search for lambda in service search bar.
![image](https://user-images.githubusercontent.com/63589909/80984559-a29b4e80-8e4b-11ea-94c8-daf9afc3fa07.png)
2. You will see dashboard, click on create function.
![image](https://user-images.githubusercontent.com/63589909/80984681-c9f21b80-8e4b-11ea-90f0-53b16e751fff.png)
3. You get this on your screen.\
![image](https://user-images.githubusercontent.com/63589909/80984773-f0b05200-8e4b-11ea-93ff-4f2849dd376d.png)
* Choose use a Blueprint.\
![image](https://user-images.githubusercontent.com/63589909/80984900-19384c00-8e4c-11ea-8814-78de144d03cd.png)
4. Search for Hello in blueprint and hit enter.\
![image](https://user-images.githubusercontent.com/63589909/80985172-7a601f80-8e4c-11ea-9c72-1b97576b9d36.png)
5. Select python and click on configure.\
![image](https://user-images.githubusercontent.com/63589909/80985313-ad0a1800-8e4c-11ea-83fb-44ca2bffdc95.png)
6. You will be able to see this on your screen.\
![image](https://user-images.githubusercontent.com/63589909/80985393-cad77d00-8e4c-11ea-9402-1bed38705a32.png)
* Write Function name, select use existing role and select the default provided by AWS in drop down. i.e robomaker_student.\
![image](https://user-images.githubusercontent.com/63589909/80985691-2c97e700-8e4d-11ea-924d-f905b11351d1.png)
7. Scroll down and click on create function.
![image](https://user-images.githubusercontent.com/63589909/80985719-3588b880-8e4d-11ea-90b0-a48aa71600e7.png)
8. You will be able to see your code on dashboard in configure on scrolling down.
![image](https://user-images.githubusercontent.com/63589909/80986298-032b8b00-8e4e-11ea-9229-b03b5f1ddd48.png)
9. You can make changes in your code here and then click on save.
![image](https://user-images.githubusercontent.com/63589909/80986406-25bda400-8e4e-11ea-8569-b2edbaf8d6c4.png)
10. To run, i.e test your lambda function, you need to create an event. 
11. Select your function, goto action and select test.
![image](https://user-images.githubusercontent.com/63589909/80986618-71704d80-8e4e-11ea-8b5a-63e86c1afe54.png)
12. A popup window will appear./
![image](https://user-images.githubusercontent.com/63589909/80986715-9664c080-8e4e-11ea-948a-03b41e04368e.png)
13. Choose create new test event, let the template be hello-world and name the event.
![image](https://user-images.githubusercontent.com/63589909/80986875-ce6c0380-8e4e-11ea-8b65-a6da11a8673f.png)
* Console input is given through event, i.e enter your key parameter values in place of values opposite keys.
14. Click on create.\
![image](https://user-images.githubusercontent.com/63589909/80987104-30c50400-8e4f-11ea-97a7-165c4a8c1335.png)
15. Now select the created function, go to action and click on test.
![image](https://user-images.githubusercontent.com/63589909/80987131-3a4e6c00-8e4f-11ea-8eef-533f13cb82a2.png)
16. Your created event "Myevent" should appear besides action, select it and click on test.
![image](https://user-images.githubusercontent.com/63589909/80987325-85687f00-8e4f-11ea-8222-322ab075003e.png)
17. Congrats! Your function has been executed.\
![image](https://user-images.githubusercontent.com/63589909/80987502-c2cd0c80-8e4f-11ea-9f25-a3603678625d.png)
18. Click on details for more information such as return value, output console, execution duration and so on.
![image](https://user-images.githubusercontent.com/63589909/80987736-193a4b00-8e50-11ea-8b6e-b886fca1a7ba.png)
![image](https://user-images.githubusercontent.com/63589909/80987750-1e979580-8e50-11ea-8708-3ad0c83ad01c.png)
</details>

## Lambda function(nodejs) creation and testing.
<details>
<summary>Steps</summary>
<br>

1. Login into your AWS console and search for lambda in service search bar.
![image](https://user-images.githubusercontent.com/63589909/80984559-a29b4e80-8e4b-11ea-94c8-daf9afc3fa07.png)
2. You will see dashboard, click on create function.
![image](https://user-images.githubusercontent.com/63589909/80984681-c9f21b80-8e4b-11ea-90f0-53b16e751fff.png)
3. You get this on your screen.\
![image](https://user-images.githubusercontent.com/63589909/80984773-f0b05200-8e4b-11ea-93ff-4f2849dd376d.png)
* Choose use a Blueprint.\
![image](https://user-images.githubusercontent.com/63589909/80984900-19384c00-8e4c-11ea-8814-78de144d03cd.png)
4. Search for Hello in blueprint and hit enter.\
![image](https://user-images.githubusercontent.com/63589909/80985172-7a601f80-8e4c-11ea-9c72-1b97576b9d36.png)
5. Select nodejs and click on configure.\
![image](https://user-images.githubusercontent.com/63589909/80989768-04ab8200-8e53-11ea-8ea8-4652577457bb.png)
6. You will be able to see this on your screen.\
![image](https://user-images.githubusercontent.com/63589909/80985393-cad77d00-8e4c-11ea-9402-1bed38705a32.png)
* Write Function name, select use existing role and select the default provided by AWS in drop down. i.e robomaker_student.\
![image](https://user-images.githubusercontent.com/63589909/80989881-299ff500-8e53-11ea-930d-b80e178eed89.png)
7. Scroll down and click on create function.
![image](https://user-images.githubusercontent.com/63589909/80989984-4a684a80-8e53-11ea-912d-f4647f2a524b.png)
8. You will be able to see your code on dashboard in configure on scrolling down, you can make changes in your code here and then click on save.\
![image](https://user-images.githubusercontent.com/63589909/80990286-bcd92a80-8e53-11ea-8ada-b3f63ea769e2.png)
9. To run, i.e test your lambda function, you need to create an event. 
10. select your function, goto action and select test.
![image](https://user-images.githubusercontent.com/63589909/80986618-71704d80-8e4e-11ea-8b5a-63e86c1afe54.png)
11. A popup window will appear./
![image](https://user-images.githubusercontent.com/63589909/80990542-16d9f000-8e54-11ea-9907-88b8eeae9a64.png)
12 Choose create new test event, let the template be hello-world and name the event.
![image](https://user-images.githubusercontent.com/63589909/80990801-9bc50980-8e54-11ea-98b8-1f91b07a2198.png)
* Console input is given through event, i.e enter your key parameter values in place of values opposite keys.
* Since i have change the "key3" to change in step 8, i also have to make the changes in the event.  
13. Click on create.\
![image](https://user-images.githubusercontent.com/63589909/80990829-a8496200-8e54-11ea-8660-1a936fe818ac.png)
14. Now select the created function, go to action and click on test.
![image](https://user-images.githubusercontent.com/63589909/80991207-49d0b380-8e55-11ea-95c2-e9a386d24537.png)
15. Your created event "Myevent" should appear besides action, select it and click on test.
![image](https://user-images.githubusercontent.com/63589909/80987325-85687f00-8e4f-11ea-8222-322ab075003e.png)
16. Congrats! Your function has been executed.\
![image](https://user-images.githubusercontent.com/63589909/80990939-e050a500-8e54-11ea-87cb-44023004e6f4.png)
17. Click on details for more information such as return value, output console, execution duration and so on.
![image](https://user-images.githubusercontent.com/63589909/80990944-e34b9580-8e54-11ea-918e-12dca1e04df9.png)
![image](https://user-images.githubusercontent.com/63589909/80990969-ee062a80-8e54-11ea-8107-881f005ba3cb.png)

</details>
### [For more info on Lambda](https://aws.amazon.com/lambda/)
