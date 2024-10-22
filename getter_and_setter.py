class Employee:
    def setName(self,nm):
        self.name = nm
    def getName(self):
        print("The name is :",self.name)

e1=Employee()
e2=Employee()

e1.setName(input("Enter the name:"))
e2.setName(input("Enter the name:"))

print("e1 object is",e1.__dict__)
e1.getName()
e2.getName()