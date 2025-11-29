"""
A decorator is just a function that adds
extra features to another function without changing its code.

Higher Order Functions:
A function that takes another function as an argument
or returns a function as a result.
"""

def my_decorator(func):
    def wrapper():
        print("Something before function runs")
        func()
        print("Something after function runs")
    return wrapper


def greet():
    print("Hello!")


# greet()
#
decorated = my_decorator(greet)
decorated()
