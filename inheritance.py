"""
- Code reusability
"""

class Employee:
    # class variable   
    bonus=2000

    # Instance method
    def display(self):
        print("This is employee class method")

class Manager(Employee):
    bonus1=3000
    def show(self):
        print("This is manager class method")

e1 = Employee()
m1 = Manager()

# print(m1.bonus)

"""
                    Inheritance with constructor overriding
- if Parent class has a constructor & child class not then Parent class constructor will execute
- But If child has the constructor & Parent class also have constructor then "Child class constructor will get the priority"
"""

class Father:
    def __init__(self):
        print("Father constructor called")
        self.vehicle="scooter"


class Son(Father):
    def __init__(self):
        print("Son constructor called")
        self.vehicle="BMW"
s= Son()
# print(s.__dict__)