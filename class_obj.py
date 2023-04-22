class subject:
    name="physics"
    id=1
    person="sonu"
    def info(self):
        print(f"the subject is: {self.name}\nid is: {self.id}\npersonis: {self.person}")
a=subject()
a.info()
b=subject()
print("\n")
b.name="maths"
b.id=(2)
b.person="lalit"
b.info()