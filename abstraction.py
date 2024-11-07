"""
Abstraction: Data and Functions are defined in such a way that only essential details can be seen and unnecessary implementations are hidden is called Data Abstraction
- Python have no built in module to achieve abstraction in python
- By using "abc" module: "ABC" class abstracted method
"""
 
from abc import ABC,abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass

    def color(self):
        print("white")

class Maruti(Car):
    def mileage(self):
        print("Milage  is 100kmph")
