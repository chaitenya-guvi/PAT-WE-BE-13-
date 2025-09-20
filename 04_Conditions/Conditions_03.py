# The if, elif, and else statements in Python are used for multi-way decision making.
# 'if' checks the first condition. If it is False, 'elif' (else if) checks another condition.
# 'else' runs if none of the previous conditions are True.

# Example 1: Basic if-elif-else
number = 5
if number > 10:
    print("The number is greater than 10.")
elif number > 7:
    print("The number is greater than 7 but not greater than 10.")
elif number > 3:
    print("The number is greater than 3 but not greater than 7.")
else:
    print("The number is 3 or less.")
# Output: The number is greater than 3 but not greater than 7.

# Example 2: Using strings
name = "Charlie"
if name == "Alice":
    print("Hello, Alice!")
elif name == "Bob":
    print("Hello, Bob!")
else:
    print("Hello, stranger!")
# Output: Hello, stranger!

# Real world example: Checking ticket price based on age
age = 14
if age < 5:
    print("Ticket is free.")
elif age < 18:
    print("Child ticket price applies.")
elif age < 60:
    print("Adult ticket price applies.")
else:
    print("Senior citizen ticket price applies.")
# Output: Child ticket price applies.

# This example shows how if, elif, and else can be used to select different actions based on real-world conditions (age groups for ticket pricing).
# Only the first True condition's block runs, and the rest are skipped.

# You can use as many elif blocks as needed to check multiple conditions.
