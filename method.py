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