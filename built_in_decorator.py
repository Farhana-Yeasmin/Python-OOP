"""
Three type of built-in decorator: 
- @staticmethod
- @classmethod
- @property
"""

'''
@staticmethod allows you to define a method that does not need access to instance or class-specific data.
'''
#Example 1:

class Calculator:
    def __init__(self, name: str, version: int):
        self.name= name
        self.version = version

    def get_calculator_info(self):
        return f'{self.name} V.{self.version}'
    
    @staticmethod
    def add_all(*numbers: int):
        return sum(numbers)

calc = Calculator(name='Farhana\'s Calculator', version=1)
# print(calc.get_calculator_info())
# print(calc.add_all(1,2,3,4))

'''
@classmethod is a type of method in Python that belongs to the class itself, not any specific instance. It is typically used when you want to work with class-level data or create instances with specific configurations.
'''

class Calculators:
    def __init__(self, name: str, version: int):
        self.name = name
        self.version = version

    @classmethod
    def add_and_create(cls, *numbers:int):
        total = sum (numbers)
        # Creates a new Calculator instance with the result as part of the name or version

        return cls(name=f"Total: {total}", version=1)

# Example usage:
calc = Calculators.add_and_create(1, 2, 3, 4)
# print(calc.name)        # Output: "Total: 10"
# print(calc.version)

'''
@property: 
'''
class Employee:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
        # self.email = first + last +"@gmail.com"
    
    @property
    def email(self):
        return f'{self.firstname}{self.lastname}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split()
        self.firstname = first
        self.lastname = last

    
    
e = Employee("Farhana", "Yeasmin")
e1 = Employee("Bulbul","Ahmed")


print(e.fullname)
e.fullname = "Farjana Bobi"
print("After setting full name: ")
print(e.fullname)