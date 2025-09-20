# The if statement in Python is used to make decisions based on conditions.
# If the condition is True, the indented block of code runs.
# Indentation is very important in Python. It defines which statements belong to the if block.
# Indented code (usually 4 spaces) after if is executed only if the condition is True.

# Basic example:
number = 7
if number > 5:
    print("The number is greater than 5.")  # This line runs because 7 > 5
    print("This line is also indented and runs if the condition is True.")
# The above two print statements are inside the if block due to indentation.

# If the condition is False, the code inside the if block does not run.
number = 3
if number > 5:
    print("This will not be printed because 3 is not greater than 5.")
    print("Indented lines are skipped if the condition is False.")

# Code that is not indented is outside the if block and always runs.
print("This line runs regardless of the if condition.")

