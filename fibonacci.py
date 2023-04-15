n=int(input("enter nth term: "))
a,b=0,1
count=0
if n<=0:
    print("enter positive number.")
elif n==1:
    print("enter greater than 1 value.")
else:
    print("fibonacci sequence: ")
    while count<n:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
