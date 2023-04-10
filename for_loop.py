a=int(input("enter number to show mulltiplication: "))
print("Enter 1 for using(for loop): ")
print("Enter 2 for using(while loop): ")
x=int(input("enter your choice"))
if x==1:
    for i in range (11):
        print(a*i)
elif x==2:
    i=0
    while i<=10:
        print(a*i)
        i+=1
else:
    print("Error")