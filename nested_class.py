"""
The class which is declared inside another class
NOTE: It is required when one class object cannot exist without another class object
The concept of inner classes can be particularly useful in scenarios where you want to group related functionality together

"""

class Outer:
    def __init__(self):
        print("Outer class constructor called")
    
    def display(self):
        print("This is display method")
    class Inner:
        def __init__(self):
            print("Inner constructor called")
        
        def show(self):
            print("This is show method")

obj= Outer()
in1=obj.Inner()
# in1.show()

# Example 1
class Student:
    def __init__(self,name,roll,dd,mm,yy):
        self.name=name 
        self.roll = roll
        self.dob=self.DOB(dd,mm,yy)

    def display(self):
        print(f"name is {self.name} and roll is {self.roll}")
        self.dob.display()
    
    # INNNER CLASS
    class DOB:
        def __init__(self,dd,mm,yy):
            self.date=dd
            self.month=mm
            self.year=yy
        
        def display(self):
            print(f"Date of birth is:{self.date}/{self.month}/{self.year}")

s1=Student('Farhana',101,26,3,1997)
s1.display()

# Example 2:
class Car:
    def __init__(self, make, model, year, horsepower):
        self.make = make
        self.model = model
        self.year = year
        self.engine = self.Engine(horsepower)  # Create an instance of the inner class

    def display(self):
        print(f"Car: {self.year} {self.make} {self.model}")
        self.engine.display()  # Call the display method of the inner class

    # INNER CLASS
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower
        
        def display(self):
            print(f"Engine Horsepower: {self.horsepower} HP")

# Creating an instance of Car
my_car = Car('Toyota', 'Camry', 2022, 203)
my_car.display()
