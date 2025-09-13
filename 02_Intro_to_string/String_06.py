# String Concatenation in Python
# String concatenation means joining two or more strings together to form a single string.
# The most common way is using the + operator.
# You can also use the join() method or f-strings for more advanced concatenation.

# Using + operator
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print("Using + operator:", result)

reult_f_string = f"{str1} {str2}"
print("Using f-string:", reult_f_string)



# Using f-strings (for formatting and concatenation)
name = "Alice"
greeting = f"Hello, {name}!"
print("Using f-string:", greeting)
#
# Note: When concatenating non-string types, convert them to string first
age = 25
info = "Age: " + str(age)
print("Concatenating string and int:", info)
#
# # Attempting to concatenate string with non-string type directly will cause an error
# # For example: "Age: " + age  # This will raise a TypeError

age = 25
info = f"Age: {age}"
print("Using f-string with int:", info)


