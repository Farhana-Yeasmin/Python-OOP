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


"""
            Super Function
- Using super() function, we can access parent class properties
- Here both parent & child have constructor so child constructor will be the priority and execute
But I need the parent class constructor also execute. So I will use super()
"""
class Computer(object):
    def __init__(self,ram,storage):
        # self.ram = '8gb'
        # self.storage='512gb'
        self.ram = ram
        self.storage = storage
        print('Computer class constructor called')

class Mobile(Computer):
    def __init__(self,ram,storage):
        # Here Parent class constructor will execute first
        super().__init__(ram,storage)
        self.model ='iphone X'
        print("Mobile class constructor called")

Apple = Mobile('8gb','512gb')
print(Apple.__dict__)