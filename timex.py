import time as t
c= t.strftime('%H:%M:%S')
print(c)
a= int(t.strftime('%H'))
if 0<=a<=12:
    print("good morning")
else:
    print("good evening")