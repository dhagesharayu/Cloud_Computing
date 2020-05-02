# List Comprehension
* Python Code:
```
if __name__ == '__main__':
    x = int(raw_input("Enter value of x:"))
    y = int(raw_input("Enter value of y:"))
    z = int(raw_input("Enter value of z:"))
    n = int(raw_input("Enter value of n:"))
    a=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if((i+j+k)!=n):
                    b=[i,j,k]
                    a.append(b)
    print(a)
```
* Output after running on linux terminal:\
![image](https://user-images.githubusercontent.com/63589909/80864660-bf941e00-8ca1-11ea-8385-3817a8137875.png)
