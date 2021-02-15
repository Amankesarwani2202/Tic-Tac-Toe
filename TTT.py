import os
l=['_','_','_','_','_','_','_','_','_']
ne=0
def win_condition(l):
    if(l[0]=='0' and l[1]=='0' and l[2]=='0' or l[0]=='X'and l[1]=='X'and l[2]=='X'):
        if(l[0]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    elif(l[3]=='0' and l[4]=='0' and l[5]=='0' or l[3]=='X'and l[4]=='X'and l[5]=='X'):
        if(l[3]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    elif(l[6]=='0' and l[7]=='0' and l[8]=='0' or l[6]=='X'and l[7]=='X'and l[8]=='X'):
        if(l[6]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    elif(l[0]=='0' and l[3]=='0' and l[6]=='0' or l[0]=='X'and l[3]=='X'and l[6]=='X'):
        if(l[0]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    elif(l[1]=='0' and l[4]=='0' and l[7]=='0' or l[1]=='X'and l[4]=='X'and l[7]=='X'):
        if(l[1]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    elif(l[2]=='0' and l[8]=='0' and l[5]=='0' or l[2]=='X'and l[8]=='X'and l[5]=='X'):
        if(l[2]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    elif(l[0]=='0' and l[4]=='0' and l[8]=='0' or l[0]=='X'and l[4]=='X'and l[8]=='X'):
        if(l[0]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    elif(l[2]=='0' and l[4]=='0' and l[6]=='0' or l[2]=='X'and l[4]=='X'and l[6]=='X'):
        if(l[2]=='0'):
            print("WINNER IS FIRST PLAYER")
        else:
            print("WINNER IS SECOND PLAYER")
        return 1
    else:
         return 0
def display(l):
    print(" %s| %s | %s"%(l[0],l[1],l[2]))
    print("__|___|___")
    print(" %s| %s | %s"%(l[3],l[4],l[5]))
    print("__|___|___")
    print(" %s| %s | %s"%(l[6],l[7],l[8]))
    print("  |   |   ")

def insert_value(l):
    ne=0
    while(ne<=9):
        display(l)
        b=win_condition(l)
        if(b==0):
            p=int(input("ENTER POSITION"))
            if(l[p]=='_'):
                if(ne%2==0):
                    l[p]='0'
                    ne=ne+1
                else:
                    l[p]='X'
                    ne=ne+1
            else:
                print("CHOOSE ANOTHER POSITION")
        else:
            break

insert_value(l)  
