# """
# Single Inheritance: One Parent and one child class
# Multi-level Inharitance: Parent class & child class further inherited into new class forming multiple levels.
# """

# '''
#                 Multi Level Inheritance Example
# '''
# class Human_being(object):
#     def __init__(self):
#         print("Human being constructor called")
#         self.name = input("Enter your name:")

# class Employee(Human_being):
#     def __init__(self):
#         print("Employee constructor called")
#         self.salary = float(input("Enter your salary:"))

# class Managers(Employee):
#     def __init__(self):
#         print("Mangers constructor called")
#         self.bonus = float(input("Enter your bonus:"))

# m1= Managers()


# """
# Hierarchical Inheritance: One Parent & multiple child classes
# """
# class Person:
#     def __init__(self, nm, ag):
#         self.name = nm
#         self.age=ag

#     def display(self):
#         print("This is person display method")

# class Employee(Person):
#     def __init__(self, nm,ag,sal):
#         super.__init__(nm,ag)
#         self.salary = sal
        

# class Student(Person):
#     def __init__(self,nm,ag,m):
#         super.__init__(nm,ag)
#         self.marks = m

# s1 = Student('Jay',21,90)
# e1= Employee('farhan',23,20000)

"""
Multiple Inheritance: Class is derived from multiple base case classes
"""

class Country:
    def __init__(self):
        print("Country class constructor")
        self.office = "Dhaka"  

class State(Country):  # State now inherits from Country to properly use super()
    def __init__(self):
        super().__init__()  # Calls Country's __init__
        print("State class constructor")
        self.office = "Dinajpur" 

class District(State, Country):  # Multiple inheritance: State and Country
    def __init__(self):
        super().__init__()  # First go from State, then Country based on MRO.
        print("District class constructor")
        self.office = "Rangpur"

d = District()
# print(d.__dict__)

"""
Hybrid Inheritance: It contains multiple type of inheritance
MRO: Method Resolution Order
MRO represent how properties are searched in inheritance
    - Rule 1: Python first search in child class and then goes to parent class. Priority is to child class
    - Rule 2: MRO follows 'Depth First Left to Right' Approach
    - 
"""
