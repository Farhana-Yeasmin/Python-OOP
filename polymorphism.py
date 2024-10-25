"""
Polymorphism in python is an ability of python object to tkae many forms.
- DIfferent behavior according to situation
"""

# +:- python object
print(10+20) #30
print("hello"+"world") # helloworld

"""
Polymorphism with Inheritance
"""

"""
According to the situation max_speed() func is changing so it is polymorphism
NOTE: Polymorphism allows methods in different classes to have the same name but behave differently

"""
class Veh:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price
    
    def get_details(self):
        print("name is:",self.name)
        print("color is:",self.color)
        print("price is:",self.price)
    
    def max_speed(self):
        print("maximum speed limit is 100")
    
    def gear(self):
        print("gear change is 6")

class Car(Veh):
    
    def max_speed(self):
        print("maximum speed limit is 140")
    
    def gear(self):
        print("gear change is 8")

v1=Veh("Truck",'red',2000000)
c1=Car("Car","white",500000)

'''
Method Overriding: In Car, the max_speed() and gear() methods override the same methods in Veh.
'''

# v1.max_speed()
# c1.max_speed()

# Example of Polymorphism with a loop
vehicles = [Veh("Truck", "red", 200000), Car("Car", "white", 500000)]

for v in vehicles:
    v.max_speed()  # Calls max_speed for each object in the list
    v.gear()       # Calls gear for each object in the list
