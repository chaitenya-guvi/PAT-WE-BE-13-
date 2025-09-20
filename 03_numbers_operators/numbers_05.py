# Logical OR Operator in Python
# The 'or' operator returns True if at least one condition is True.

# Example 1: Numbers
num_x = 4
num_y = 15
print(num_x < 5 or num_y > 20)  # True (first condition is True)
print(num_x > 10 or num_y < 10) # False (both conditions are False)

# Example 2: Strings
str_x = ""
str_y = "World"
print(bool(str_x) or bool(str_y))  # True (str_y is non-empty)
print(bool(str_x) or len(str_x) > 0)  # False (both are False)

# Example 3: Booleans
flag_x = False
flag_y = True
print(flag_x or flag_y)  # True (flag_y is True)
print(flag_x or not flag_y)  # False (both are False)

# Example 4: Combined types
age = 16
name = "Bob"
print(age > 18 or name == "Bob")  # True (second condition is True)
print(age > 18 or name == "Alice") # False (both are False)

# The 'or' operator is commonly used in if statements for decision-making.
if num_x < 5 or str_y == "World":
    print("At least one condition is True!")
