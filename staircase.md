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
