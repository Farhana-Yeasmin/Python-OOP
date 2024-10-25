"""
Step 1: check data type of left operator  #int
Step 2: go in that class
Step3: call __add__() function
"""
n1= 10
n2=20
# boths are print same res
# print(n1+n2)
# print(n1.__add__(n2))
# print(int.__add__(n1,n2))

class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages

    def __add__(self,other):  #(b1,b2)
        total = self.pages+other.pages
        # return total
        return Book("All books",total)
    
    def __str__(self):
        return str(self.pages)

b1= Book("b1",200)
b2=Book("B2",300)
b3=Book("b3",500)
#Call varibale using Object reference
# print('Totall number of pages',b1.pages+b2.pages) #500

# call variable without using object reference
# print('total number of pages:',b1+b2)   # b1.__add__(b2) --> Book,__add__(b,b2)

# print('total number of pages:',b1+b2+b3) 

