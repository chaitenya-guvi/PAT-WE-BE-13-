"""
*args - Arbitrary Argument
A special operator we can pass to functions

Gathers remaining arguments as a tuple
when to use : when you have variable length of arguments

This is just a parameter - you can call it whatever you want!
you can also use other names like *values, *items, *numbers, etc.
you can access the values using indexing like a tuple

you can access multiple arguments as a parameter
"""

def my_function(*kids):
  print(type(kids))
  print("The youngest student  is " + kids[3])
#
my_function("Robin", "Tobias", "Star","Aravind","Suba")
my_function("Robin", "Tobias")

"""
Example 2
"""

def sum_all_values(*args):
    total = 0
    for val in args:
        total += val

    return total


print(sum_all_values(1, 2, 3))
print(sum_all_values(1, 2, 3, 7, 8, 8, 9))
#
print(sum_all_values(1, 2, 3, 4, 5))