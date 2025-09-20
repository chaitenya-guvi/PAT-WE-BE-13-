# Comparison Operators in Python
# Comparison operators are used to compare values and return True or False.

x = 10
y = 5

# 1. Equal to (==)
print("x == y:", x == y)  # False
print(10 == 10)  # True
print(10 == 9)   # False

# 2. Not equal to (!=)
print("x != y:", x != y)  # True
print(10 != 10)  # False
print(10 != 9)   # True

# 3. Greater than (>)
print("x > y:", x > y)  # True

# 4. Less than (<)
print("x < y:", x < y)  # False

# 5. Greater than or equal to (>=)
print("x >= y:", x >= y)  # True

# 6. Less than or equal to (<=)
print("x <= y:", x <= y)  # False

# These operators work with numbers, strings, and other data types.

# Comparison operators also work with strings
str1 = "apple"
str2 = "banana"
str3 = "apple"

# 1. Equal to (==)
print("str1 == str2:", str1 == str2)  # False
print("str1 == str3:", str1 == str3)  # True

# 2. Not equal to (!=)
print("str1 != str2:", str1 != str2)  # True
print("str1 != str3:", str1 != str3)  # False

# 3. Greater than (>)
print("str1 > str2:", str1 > str2)  # False
print("str2 > str1:", str2 > str1)  # True

# 4. Less than (<)
print("str1 < str2:", str1 < str2)  # True
print("str2 < str1:", str2 < str1)  # False

# 5. Greater than or equal to (>=)
print("str1 >= str3:", str1 >= str3)  # True
print("str1 >= str2:", str1 >= str2)  # False

# 6. Less than or equal to (<=)
print("str1 <= str3:", str1 <= str3)  # True
print("str1 <= str2:", str1 <= str2)  # True


