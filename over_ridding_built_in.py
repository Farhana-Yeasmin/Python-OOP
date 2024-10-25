"""
Change built in function using magic method/ dunder method

Magic methods in Python, also known as dunder methods, start and end with double underscores
Example: __len__, __str__, __add__
"""

class Cart:
    def __init__(self,basket1,basket2,basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.other=basket3
    
    '''
    __len__ method is a magic method that override the built in len() function
    '''
    def __len__(self):
        print("Total number of items in carts")
        # Calculate total items by adding lengths of each basket
        total = len(self.clothes)+len(self.electronics)+len(self.other)
        return total
    
farhana = Cart(['pant','shirt','t-shirt'],['earphone','mobile'],['chair'])
# Call len() on the Cart instance, which uses the overridden __len__ method
print(len(farhana))