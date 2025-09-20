# Nested if conditions in Python
# A nested if is an if statement inside another if statement.
# This allows you to check multiple related conditions in a hierarchical way.

# Example 1: Basic nested if
age = 20
if age > 10:
    print("Age is greater than 10.")
    if age < 25:
        print("Age is less than 25.")
# Output:
# Age is greater than 10.
# Age is less than 25.

# Example 2: Real-world scenario
score = 85
if score >= 50:
    print("You passed the exam.")
    if score >= 80:
        print("You got a distinction!")
    else:
        print("Good job, but no distinction.")
else:
    print("You did not pass the exam.")
# Output:
# You passed the exam.
# You got a distinction!

# Nested if statements are useful when you want to check a condition only if another condition is already True.
# Indentation is important to show which statements are inside the nested if block.

