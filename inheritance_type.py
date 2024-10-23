"""
Single Inheritance: One Parent and one child class
Multi-level Inharitance: Parent class & child class further inherited into new class forming multiple levels.
"""

'''
                Multi Level Inheritance Example
'''
class Human_being(object):
    def __init__(self):
        print("Human being constructor called")
        self.name = input("Enter your name:")

class Employee(Human_being):
    def __init__(self):
        print("Employee constructor called")
        self.salary = float(input("Enter your salary:"))

class Managers(Employee):
    def __init__(self):
        print("Mangers constructor called")
        self.bonus = float(input("Enter your bonus:"))

m1= Managers()


"""
Hierarchical Inheritance: One Parent & multiple child classes
"""
class Person:
    def __init__(self, nm, ag):
        self.name = nm
        self.age=ag

    def display(self):
        print("This is person display method")

class Employee(Person):
    def __init__(self, nm,ag,sal):
        super.__init__(nm,ag)
        self.salary = sal
        

class Student(Person):
    def __init__(self,nm,ag,m):
        super.__init__(nm,ag)
        self.marks = m

s1 = Student('Jay',21,90)
e1= Employee('farhan',23,20000)

"""
Multiple Inheritance: Class is derived from multiple case classes
"""
