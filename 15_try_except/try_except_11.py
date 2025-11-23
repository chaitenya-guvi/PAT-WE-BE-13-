"""assert in Python is a debugging tool used to check if a condition is true.
If the condition is true, the program continues normally.
If the condition is false, Python raises an AssertionError.

It is mainly used during development and testing to catch logical mistakes early.

Basic Syntax:
assert condition, "optional error message"

If condition is True → nothing happens.
If condition is False → program stops and shows an error.
"""

# Example 1: Simple Assertion
x = 10
assert x > 5
print("Assertion passed.")



# Example 2: Assertion Failure
x = 3
assert x > 5, f"{x} should be greater than 5"
print("This line will not run.")
