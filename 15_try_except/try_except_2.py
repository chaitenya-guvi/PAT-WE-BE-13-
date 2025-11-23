"""
# This code demonstrates the use of try-except-else for handling exceptions in Python.
# In this example, we attempt to divide 10 by 0, which raises a ZeroDivisionError.
# The except block catches this specific exception and prints an error message.
# If the division were successful, the else block would print the result.
"""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: division by zero.")
else:
    print("Result:", result)
