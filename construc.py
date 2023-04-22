# argument constructor
class person:
    def __init__(self,n,a,w):
        person.name=n
        person.age=a
        person.work=w
        print(f"name is:{self.name},\nwork is:{self.work},\nage is:{self.age}")
a=person("sonu",24,"programmer")
print("\n")
b=person("lalit",25,"HR")
print(b.name)

# default constructor
class show:
    def __init__(self):
        print("i am here")
a=show()