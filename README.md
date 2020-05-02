# Python on linux
## How to execute python program on linux terminal using 
### Steps to follow:
1. Login into your linux terminal.
2. Check whether python interpreter is available is your terminal, linux by default provides python interpreter.
* You can do this excuting of either of this command: ```pthon``` or ```python --version```   
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


