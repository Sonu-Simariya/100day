x=int(input("enter signal: "))
match x:
    case 1:
        if x==1:
            print("Green Signal")
        else:
            print("stop")
    case 2:
        if x==2:
            print("Ready to go")
        else:
            print("stop")
    case 3:
        if x==3:
            print("Stop")
        else:
            print("stop")
    case _:
        print("error")