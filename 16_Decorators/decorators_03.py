"""
Decorators with Arguments

"""

def my_decorator(func):
    def wrapper(a, b):
        print("Before")
        print( func(a, b))
        print("After")
    return wrapper

@my_decorator
def add(x, y):
    return x + y

add(5, 10)
