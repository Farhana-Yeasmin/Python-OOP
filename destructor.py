"""
Destructor: A special method which destroy objects and release resources tied to objects
- Destructor is called automatically then object is distroyed

Two scenarios destructor is called:
- Reference counting reaches to 0
- when variable goes out of scope

Disadvantage: Circular referencing

"""


class Employee:
    def __init__(self,nm,sal):
        self.name=nm
        self.salary = sal

    def display(self):
        print(f"name is {self.name}\n salary is {self.salary}")

    #defining destructor
    def __del__(self):
        print("Destructor is called")

e1=Employee("Farhana",200000)
e1.display()

del e1