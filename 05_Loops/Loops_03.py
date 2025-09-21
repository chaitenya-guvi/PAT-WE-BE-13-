# Basic Syntax of For Loops in Python
# A for loop is used to iterate over a sequence (such as a list, tuple, string, or range).
# Syntax:
# for variable in sequence:
#     # code block to execute for each item

# Example 1: Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    print(f"fruit = {fruit.upper()} , capitailsed = {fruit.capitalize()} first index is {fruit[0]}")

# Example 2: Looping through a string
text = "Python"
for character in text:
    print(character)

# Example 3: Using range()
for number in range(5):
    print(number)
# Output: 0 1 2 3 4

# The indented code block inside the for loop runs once for each item in the sequence.
# The loop variable takes the value of each item, one by one.

