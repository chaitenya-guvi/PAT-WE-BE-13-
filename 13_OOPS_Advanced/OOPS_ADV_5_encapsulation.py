"""
Python Encapsulation - principal of OOP , Inheritance , Polymorphism ,Encapsulation
Encapsulation is one of the key features of object-oriented programming.
Encapsulation refers to the bundling of attributes and methods inside a single class.

It prevents outer classes from accessing and
changing attributes and methods of a class.
This also helps to achieve data hiding.

In Python, we denote private attributes using underscore
as the prefix i.e single _ or double __.

"""

class Computer:

    def __init__(self):
        self.__maxprice = 900 # private attribute
        self.cost = 800  # public attribute

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price

computer1 = Computer()
computer1.sell()

# change the price
computer1.__maxprice = 1000
computer1.sell()

print(computer1.cost)
computer1.cost= 500
print(computer1.cost)

# using setter function
computer1.setMaxPrice(1200)
computer1.sell()