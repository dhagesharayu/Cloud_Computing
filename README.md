# Python on linux
## How to execute python program on linux terminal using 
### Steps to follow:
1. Login into your linux terminal.
2. Check whether python interpreter is available is your terminal, linux by default provides python interpreter.
* You can do this excuting of either of this command: ```pthon``` or ```python --version```
![image](https://user-images.githubusercontent.com/63589909/80866152-e4d95a00-8caa-11ea-95d7-45abd4625d3a.png)
* What you see in the above screenshot is similar to python IDLE,so you nrrd to exit it. Syntax: ```exit()```

```
def minion_game(string):
    # your code goes here
    vowels="AEIOU"
    ks=ss=0
    for i in range(len(string)):
        if string[i] in vowels:
            ks+=(len(string)-i)
        else:
            ss+=(len(string)-i)
    if ks>ss:
        print "Kevin",ks
    elif ss>ks:
        print "Stuart",ss
    else:
        print "Draw"
if __name__ == '__main__':
    s = raw_input()
    minion_game(s)

```


