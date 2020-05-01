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
