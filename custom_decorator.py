"""
Decorator: A decorator is a design pattern in python that allows you to modify or eenchance the behavior of func or methods.
This is custom made decorator

Decorator:  Two types decorator
- Function Decorator
- Class Decorator
"""

'''
Function Decorator: A function decorator is a higher-order function that takes another function as an argument
- It wraps the original function in another function
'''


# Example 1: Function Decorator

def Decorator_func(func):
    def wrapper(a,b):
        result = func(a,b) #call the original function
        return result ** 2
    return wrapper


@Decorator_func
def add(a,b):
    return a + b

# print(add(1,2))



'''
Decorator class: The decorator class takes a function (func) as an argument in its __init__ method
it stores the function in self.function
- The __call__ method allows instances of the class to be called as functions.
- @Decorator means when you call the add(), it actually invoked Decorator.__call__
'''
# Example 2: Class Decorator
class Decorator:
    def __init__(self,func):
        self.function=func

    def __call__(self, a, b):
        # original functionality
        # square

        result = self.function(a,b)
        return result**2

"""
INstead of create object we can use the Decorator word
"""
@Decorator
def add(a,b):
    return a+b
print(add(2,3))

add=Decorator(add)
print(add(1,2))


# Example 3: Class Decorator


class Decorator():
    def __init__(self,func):
        self.function = func
        

    def __call__(self, *args):
        
        try:
            for i in args:
                if isinstance(i,str):
                    raise TypeError("Cannot pass string as arguments")
                else:
                    return self.function(*args)
        except Exception as obj:
            print(obj)            

@Decorator   
def add(*args):
    total=0
    for i in args:
        total=total+i
    return total

print(add(10,12,11))
print(add(11,'12',23))

# add= Decorator(add)
# add(10,'20',23)  # add.__call__()

