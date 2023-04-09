
# def multiply(a,b):
#     print("The multiplication is",a*b)
# a=34
# b=67
# multiply(a,b)


# a=67
# b=65
# multiply(a,b)


# def avg(*number):
#     sum=0
#     for i in number:
#         sum=sum+i
#         print("avg is",sum/len(number))
# avg(7,5)

# Function
def cp(p,r,t):
    # c=p+r+t
    amount = p*((1+(r/100))**t)
    ci=amount-p
    si=(p*r*t)/100
    print("The amount is: ",amount)
    print("The compound intreast is: ",ci)
    print("The simple intreast is: ",si)
cp(10000,10,2)
cp(10000,10,2)