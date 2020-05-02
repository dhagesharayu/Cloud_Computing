# Staircase
* Python Code:
```
import math
import os
import random
import re
import sys
def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-i)+"#"*i)
if __name__ == '__main__':
    n = int(raw_input())
    staircase(n)
```
* Output after executing code on linux terminal:\
![image](https://user-images.githubusercontent.com/63589909/80864782-7395a900-8ca2-11ea-9e00-03fa4210dbb2.png)
