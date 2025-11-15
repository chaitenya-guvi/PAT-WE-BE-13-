"""
what is a module ?
A module is a file containing Python definitions and statements.
The file name is the module name with the suffix .py added.
Modules are used to organize code
into manageable sections, promote code reuse, and improve maintainability.


# User Defined Modules
Modules can define functions, classes, and variables that can be reused in other Python programs.
This allows for better organization and modularity in code development.
example : add_module.py (contains add_numbers and multiply_number functions)

#Built-in Modules
Python comes with a standard library of built-in modules that provide various functionalities,
such as file I/O, mathematical operations, and data manipulation.
example : os, sys, math, datetime etc.

# Third Party Modules
In addition to built-in modules,
there are many third-party modules available through package managers like pip
that extend Python's capabilities in areas like web development, data analysis, and machine learning.
example : numpy, pandas, requests, flask etc.

"""

def add_numbers(a,b) :
    return a + b

def multiply_number(a,b) :
    return a * b


name = "chaitenya"

# print(f"Hello, {name}. The sum of 2 and 3 is {add_numbers(2,3)}")
# print(f"Hello, {name}. The multiplication of 2 and 3 is {multiply_number(2,3)}")