# What is an iterable object in Python?
# An iterable is any Python object capable of returning its members one at a time, allowing it to be looped over (iterated).
# Common iterable objects include lists, tuples, strings, dictionaries, and sets.
# You can use a for loop to go through each item in an iterable.

# Example: List (iterable)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example: String (iterable)
text = "Python"
for char in text:
    print(char)

# Example: Tuple (iterable)
numbers = (1, 2, 3)
for number in numbers:
    print(number)

# in python 3, many built-in data types are iterable.
# Examples include lists, tuples, strings, dictionaries, and sets.
# non iterable example
# number like int , float, complex are not iterable
# NoneType is not iterable
# boolean are not iterable


# You can check if an object is iterable using the iter() function:
print(iter(fruits))  # This returns an iterator object

# If an object is not iterable, calling iter() will raise a TypeError.
# Iterables are useful for looping, comprehensions, and many built-in Python functions.

