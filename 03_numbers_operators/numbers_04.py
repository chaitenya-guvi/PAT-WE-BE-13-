# Logical AND Operator in Python
# The 'and' operator returns True only if both conditions are True.

"""
Empty values are considered False in Python.
Non-empty values are considered True.
0 is considered False, while any non-zero number is True.
None is considered False.
"""

bool("")
# False
bool(0)
# False
bool(None)
# False


# Example 1: Numbers
num_a = 8
num_b = 12


print(num_a > 5 and num_b < 15)  # True (both conditions are True)
print(num_a > 10 and num_b < 15) # False (first condition is False)

true_number = 1
false_number = 0
print(true_number * true_number)
print(true_number * false_number)
print(false_number * true_number)
print(false_number * false_number)


# Example 2: Strings
str_a = "Python"
str_b = ""
print(bool(str_a) and bool(str_b))  # False (str_b is empty)
print(bool(str_a) and len(str_a) > 3)  # True (str_a is non-empty and length > 3)

# Example 3: Booleans
flag_a = True
flag_b = False
print(flag_a and flag_b)  # False (one is False)
print(flag_a and not flag_b)  # True (flag_a is True and flag_b is not True)

# Example 4: Combined types
age = 20
name = "Alice"
print(age > 18 and name == "Alice")  # True (both conditions are True)
print(age > 18 and name == "Bob")    # False (second condition is False)

# The 'and' operator is commonly used in if statements for decision making.
if num_a > 5 and str_a == "Python":
    print("Both conditions are True!")

