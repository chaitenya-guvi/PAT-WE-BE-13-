# tuples_1.py
"""
A tuple is a built-in Python data type used to store multiple items in a single variable.
It is ordered and immutable, meaning:

Ordered → The items have a defined order, and that order will not change.

Immutable → Once a tuple is created, you cannot change, add, or remove its items.
"""

# Creating a tuple
my_tuple = (1, 2, 3, "hello", True)
print("My Tuple:", my_tuple)

tuple2 = (['a', 'b', 'c'], (4,5), None, 3.14, {"key": "value"},{1,2,3})

# immutable tuple with mixed data types
mixed_tuple = (1, "two", 3.0)
print("Mixed Tuple:", mixed_tuple)
print(mixed_tuple[0])
mixed_tuple[0] = 99  # This will raise an error because tuples are immutable

# NOTE : tuple with a single element needs a trailing comma
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)
print(type(single_element_tuple))  # Output: <class 'tuple'>

not_a_tuple = (42)
print("Not a Tuple:", not_a_tuple)
print(type(not_a_tuple))  # Output: <class 'int'>



#  real world example
coordinates = (10.5, 20.3)
print("X:", coordinates[0])
print("Y:", coordinates[1])


# Tuples are immutable
# The following line would raise an error if uncommented
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# However, you can concatenate tuples to create a new one
new_tuple = my_tuple + (4, 5)
print("New Tuple after concatenation:", new_tuple)
# You can also repeat tuples
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)


