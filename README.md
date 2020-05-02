# Python on linux
## How to execute python program on linux terminal using 
### Steps to follow:
1. Login into your linux terminal.
2. Check whether python interpreter is available is your terminal, linux by default provides python interpreter.
* You can do this excuting of either of this command: ```pthon``` or ```python --version```
![image](https://user-images.githubusercontent.com/63589909/80866152-e4d95a00-8caa-11ea-95d7-45abd4625d3a.png)
* What you see in the above screenshot is similar to python IDLE,so you nrrd to exit it. Syntax: ```exit()```
![image](https://user-images.githubusercontent.com/63589909/80866310-8d87b980-8cab-11ea-91ce-2fdcad88016c.png)
3. Make an directory to store program you want to execute. ```mkdir python``` This make a directory in your ssd called python.
4. Enter into the python folder where you plan to store your code with ```cd python``` command.
![image](https://user-images.githubusercontent.com/63589909/80866775-3cc59000-8cae-11ea-81d1-94ce28fc8760.png)
5. Once in can create a python script with ``` vi miniongame.py``` command.
* Here your enter into the file on pressing ```i```, you enter insert mode.
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
* Type the command given above:
* Press ```Esc``` key to escape insert mode and type ```:wq``` to write your code into the file come out of the file.
![image](https://user-images.githubusercontent.com/63589909/80866823-857d4900-8cae-11ea-901e-891fe01aab44.png)
6. Now simply execute the filw with the command ```python miniongame.py``` i.e ```python path+file_name```

### You can also run local python file by simply uploading or copying them in the python directory.





