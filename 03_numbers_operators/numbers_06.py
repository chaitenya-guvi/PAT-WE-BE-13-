# Logical Operators in Python
# Logical operators are used to combine conditional statements and work with numbers, strings, and booleans.

# 1. and - Returns True if both statements are True
num1 = 10
num2 = 5
print(num1 > 0 and num2 > 0)  # True (both numbers are positive)

# 2. or - Returns True if at least one statement is True
print(num1 > 0 or num2 < 0)  # True (num1 is positive)

# 3. not - Reverses the result, returns False if the result is True
is_valid = True
print(not is_valid)  # False

# Logical operators with strings
str1 = "hello"
str2 = "" # empty string
print(bool(str1) and bool(str2))  # False (str2 is empty)
print(bool(str1) or bool(str2))   # True (str1 is non-empty)
print(not bool(str2))             # True (str2 is empty)

# Logical operators with booleans
flag1 = True
flag2 = False
print(flag1 and flag2)  # False
print(flag1 or flag2)   # True
print(not flag2)        # True

# Logical operators are commonly used in if statements and loops for decision making.

