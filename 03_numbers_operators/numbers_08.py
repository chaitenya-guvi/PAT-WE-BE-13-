# Assignment Operators with Strings in Python
# Assignment operators can be used with strings for concatenation and updating values.

# Basic assignment (=)
greeting = "Hello"
print("= operator:", greeting)  # Output: Hello

# Add and assign (+=) - Concatenates strings
greeting += " World"
print("+= operator:", greeting)  # Output: Hello World

# You cannot use -=, *=, /=, etc. directly with strings, as they are not defined for string objects.
# Only += is commonly used for string concatenation.

# Example with multiple concatenations:
message = "Python"
message += " is"
message += " awesome!"
print("Concatenated message:", message)  # Output: Python is awesome!

# Assignment operators are useful for building strings step by step.

