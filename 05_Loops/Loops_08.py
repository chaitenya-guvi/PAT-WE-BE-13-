# When to use a while loop instead of a for loop in Python
# --------------------------------------------------------
# A while loop is used when you want to repeat a block of code as long as a condition is True.
# Use a while loop when you do not know in advance how many times you need to repeat the code.
# For loops are best when you know the exact number of iterations (e.g., iterating over a list or range).

# Example 1: Basic while loop (counting)
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1
# Output: Count is: 1, 2, 3, 4, 5

# Example 2: User input loop (unknown number of iterations)
# This loop keeps asking for input until the user types 'exit'
# Uncomment to run

# user_input = ""
# while user_input != "exit":
#     user_input = input("Type 'exit' to stop: ")
#     print(f"You typed: {user_input}")



# Example 3: Waiting for a condition to change
temperature = 30
while temperature > 25:
    print(f"Temperature is {temperature}, too hot!")
    temperature -= 2
# Output: Temperature is 30, 28, 26

# Summary:
# - Use while loops for indefinite repetition, when the number of iterations is not known in advance.
# - Use for loops for definite repetition, when you know how many times to repeat.

