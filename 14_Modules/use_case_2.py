"""
selective importing from a module

when doing g selective importing we can import
specific objects like functions, classes or variables from a module
"""
from add_module import add_numbers# imports specific objects from module
# from add_module import *   # imports everything from module


print(add_numbers(4, 5))
# print(multiply_number(5, 5))