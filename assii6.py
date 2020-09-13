#assisgnment 6.1
class Bank_account:
    def __init__(self):
        self.balance = 0
        print('HELLO!!!! Welcome To The Deposit & Withdrawal Machine')

    def Deposit(self):
        amount = float(input("Enter amount to be deposited:"))
        self.balance += amount
        print("\n Amount Deposited: ",amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn:"))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You withdrew: ",amount)
        else:
            print("\n Insufficient Balance ")
    def display(self):
        print("\n Net Available Balance = ",self.balance)
s = Bank_account()
s.Deposit()
s.withdraw()
s.display()

"""
OUTPUT

HELLO!!!! Welcome To The Deposit & Withdrawal Machine
Enter amount to be deposited:5000

 Amount Deposited:  5000.0
Enter amount to be Withdrawn:1000

 You withdrew:  1000.0

 Net Available Balance =  4000.0
 
 """

#assisgnment 6.2

import math
pi = math.pi
def volume (radius,height):
    return (1/3)*pi*radius*radius*height
def surfacearea (radius,slantheight):
    return pi*radius*slantheight+pi*radius*radius
radius = float(5)
height = float(12)
slantheight = float(10)
print("volume of cone :" ,volume(radius,height))
print("surface area of cone : " ,surfacearea(radius,slantheight))

"""
output

volume of cone : 314.15926535897927
surface area of cone :  235.61944901923448
"""














