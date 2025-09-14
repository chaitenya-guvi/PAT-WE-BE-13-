# Using format() method (for formatting and concatenation)
# The format() method allows you to insert values into a string using curly braces {}
# It supports positional and named arguments, and works with different data types.

# Basic usage with positional arguments
formatted1 = "Hello, {}!".format("Bob")
print("Using format() with positional argument:", formatted1)

# Multiple positional arguments
formatted2 = "{} scored {} out of {}.".format("Alice", 95, 100)
print("Using format() with multiple positional arguments:", formatted2)


# Using named arguments
formatted3 = "{name} is {age} years old.".format(name="Charlie", age=30)
print("Using format() with named arguments:" , formatted3)


name="Charlie"
age=30
formatted3 = "{name} is {age} years old.".format(name = name, age = age)
print(formatted3)


# Mixing types
pi = 3.14159
formatted4 = "Value of pi: {:.2f}".format(pi)
formatted5 = "Value of pi: {}".format(pi)
print("Using format() with float formatting:", formatted4)
print("Using format() with no decimal float formatting:", formatted5)

# Note: f-strings (Python 3.6+) are more concise, but format() is useful for older versions or advanced formatting.
