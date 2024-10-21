"""
Create Class & Object
"""
# class Email:
#     pass

# e1=Email()

# print(type(e1))

"""
Constructor: Parameterize, Non Parameterize, Default
"""

class Employee:
    ''' This class miantain the employee information '''
    def __init__(self,sal,ag):
        self.salary = sal
        self.age = ag

    def display(self):
        print(f"salary is {self.salary} and age is {self.age}")


e1=Employee(24000,22)
e2=Employee(2555,12)
# To see the content on object
# print(e1.__dict__)

# accesing attribute outside the class
# print(e1.salary)
# updating attribute
e1.salary = 660000
# print(e1.salary)

""" Built in Class Attributes """
# print(getattr(e1, "age"))
# print(Employee.__doc__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)

