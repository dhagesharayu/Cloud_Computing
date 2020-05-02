# Merge the tools program
* Python Code:
```
def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    for i in range(int(n/k)):
        a=''
        for b in string[i*k:(i+1)*k]:
            if b in a:
                continue
            a+=b
        print(a)
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
```
* Output after excuting on linux terminal:\

