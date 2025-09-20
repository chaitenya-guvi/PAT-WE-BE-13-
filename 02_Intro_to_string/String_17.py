# Assignment Operators with Strings in Python
# Assignment operators are used to assign and update string values.

# Basic assignment (=)
greeting = "Hello"
print(greeting)  # Output: Hello

# Add and assign (+=) - Concatenates strings
greeting += " World"
print(greeting)  # Output: Hello World

# You cannot use -=, *=, /=, etc. directly with strings, as they are not defined for string objects.
# Only += is commonly used for string concatenation.

# Example: Building a string step by step
message = "Python"
message += " is"
message += " awesome!"
print(message)  # Output: Python is awesome!

# Assignment operators are useful for updating and building strings efficiently.
line = "***___"
print(line)

line *= '4'
print(line)
