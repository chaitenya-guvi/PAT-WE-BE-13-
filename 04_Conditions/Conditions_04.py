# Multiple if statements in Python
# You can use more than one if statement in your code to check different conditions independently.
# Each if statement is evaluated separately, and all True conditions will execute their blocks.

# Example 1: Checking multiple independent conditions
age = 25
if age > 18:
    print("You are an adult.")
if age > 60:
    print("You are a senior citizen.")
# Output: You are an adult.
# (Second if does not run because age is not greater than 60)

# Example 2: Multiple if statements with different variables
score = 85
if score >= 50:
    print("You passed the exam.")
if score >= 90:
    print("Excellent score!")
# Output: You passed the exam.
# (Second if does not run because score is not >= 90)

# Example 3: All if statements can run if all conditions are True
temperature = 35
if temperature > 30:
    print("It's a hot day.")
if temperature > 20:
    print("It's warm outside.")
# Output:
# It's a hot day.
# It's warm outside.

# Multiple if statements are useful when you want to check several independent conditions
# , not just one chain of decisions.

