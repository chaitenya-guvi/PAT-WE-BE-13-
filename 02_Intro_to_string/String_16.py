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
