
try:
    def sonu(a,b):
        c=(float(a)+float(b))
        print("The addition is: ",c)
    a=float(input("enter 1 value: "))
    b=float(input("enter 2 value: "))
    sonu(a,b)
except:
    print("Error: The value is invalid")
finally:
    print("go")
print("\n")
sonu(78,98)