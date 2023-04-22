#stone paper sizzer game. 
import random as r
while True:
    try:
        print("enter 1 for stone.")
        print("enter 2 for paper.")
        print("enter 3 for sizzer.")
        a=int(input("enter your choice: "))
        b=r.randint(1,3)
        if a==b:
            print("match draw",a)
            print("the computer is: ",b)
        elif (a,b)==(1,2):
            print("you lose.",a)
            print("the computer is: ",b)
        elif (a,b)==(1,3):
            print("you win",a)
            print("the computer is: ",b)
        elif (a,b)==(2,1):
            print("you win",a)
            print("the computer is: ",b)
        elif (a,b)==(2,3):
            print("you lose",a)
            print("the computer is: ",b)
        elif (a,b)==(3,1):
            print("you lose",a)
            print("the computer is: ",b)
        elif (a,b)==(3,2):
            print("you win")
            print("the computer is: ",b)
        else:
            print("invalid syntax.")
    except:
        print("\n")
        z=input("enter y to continue.")
        if z=="y":
            print("\n")
            continue
        else:
            break