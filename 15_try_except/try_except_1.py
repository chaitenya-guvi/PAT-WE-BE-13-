"""
Exception Handling
In Python, the try block is used to write code that may produce an error.
If an error occurs inside the try block, Python immediately jumps to the except block.
If no error occurs, then the else block is executed.

So the flow works like this:

Python executes the statements inside try.

If an exception occurs, the except block runs.

If no exception occurs in the try block, the else block runs.

The else block is optional.
"""

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
