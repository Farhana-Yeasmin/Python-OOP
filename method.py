"""
Stattic Method: This method perform operations on external data
"""

class Bank:
    bank_name="BOI"
    rate_of_interest=12.25

    @staticmethod
    def simple_interest(p,n):
        si = (p*n*Bank.rate_of_interest)/100
        print(si)


# prin=float(input("Enter principle amount:"))
# n=int(input("Enter number of years:"))
# Bank.simple_interest(prin,n)

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