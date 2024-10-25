"""
Wrapping up data and methods working on data together in a single unit is called as excapsulation
"""
class Finance:
    def __init__(self):
        self.__revenue=100000 #private data
        self.__number_of_sales=111

    def display(self):
        print(f"revenue is: {self.__revenue} and number of sales{self.__number_of_sales}")

f1=Finance()
f1.display()
'''
In side the memory private variable is stored as: _classname__variablename
NOTE: In python Encapsulation concept is not properly implemented coz it can be bypass like as below
'''
# Outside the class we can acces the private data
print(f1._Finance__revenue)


