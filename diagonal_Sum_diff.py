import math
import os
import random
import re
import sys



def diagonalDifference(arr):
   
    d1=d2=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if i==j:
                d1+=arr[i][j]
            if i+j==(n-1):
                d2+=arr[i][j]
    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()




