"""
a,b -- parameters
parameters are in the function definition
arguments are in the function call
"""

def add(a, b):
    """
    Sum of numbers
    :param a: the number 1
    :param b: the number 2
    :return: the sum of the numbers
    """
    print(a)
    print(b)
    return a + b

#functiuon calls with arguments - positional arguments
print(add(5, 3))
print(add(4, 5))

# function calls with arguments - keyword arguments
print(add(b=3, a=5))
print(add(a=4, b=5))

"""
Parameters

Variables that are passed to a function - 
think of them as placeholders that get assigned when you call the function.
"""


def multiply(first, second):
    return first * second

# multiply function with positional arguments
print("output of multiply with positional :  ", multiply(5, 3))

# multiply function with keyword arguments
print("output of multiply with keyword : ", multiply(second=3, first=5))