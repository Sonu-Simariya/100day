ques= ["what is the age of amitabh bacchan? ",
       "What is the color of sky in afternoon? ",
       "who is the PM of india? "]
price=[10000,20000,40000]
ans=[67,98,"blue","Narendra Modi"]
a=int(input("Show question: "))
if a==1:
    print(ques[0])
    print("1.67\n 2.45\n 3.89\n 4.45")
    x=int(input("Say answer: "))
    if x==1:
        print("Correct answer.\nyou won",price[0])
    else:
        print("Ghar ja ","\n the correct answer is: ",ans[1],ans[0])
elif a==2:
    print(ques[1])
    print("1.black\n 2.blue\n 3.violet\n 4. green")
    x=int(input("Say answer: "))
    if x==2:
        print("Correct answer you won: ",price[1])
    else:
        print("Go home\n","Correct answer is: ", ans[2])
elif a==3:
    print(ques[2])
    print("1.Amit Shah\n 2.Joe Bidan\n 3.Narendra Modi\n 4.B. Jayshankar")
    x=int(input("Say answer: "))
    if x==3:
        print("Correct answer you won: ",price[2])
    else:
        print("Go home\n","Correct answer is: ", ans[3])        
else:
    print("Error")