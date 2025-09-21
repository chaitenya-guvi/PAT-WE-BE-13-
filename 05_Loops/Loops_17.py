# The 'continue' statement in while loops
# ---------------------------------------
# 'continue' is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.
# It is useful when you want to ignore certain values or conditions while looping.

# Basic Example: Skip even numbers while counting from 1 to 6
number = 1
while number <= 6:
    if number % 2 == 0:
        number += 1
        continue  # Skip even numbers
    print(f"Odd number: {number}")
    number += 1
# Output: Odd number: 1, 3, 5

# Real World Scenario: Skip invalid user inputs (simulate with a list)
user_inputs = ["John", "", "Alice", "Bob", "", "Eve"]
index = 0
while index < len(user_inputs):
    name = user_inputs[index]
    index += 1
    if name == "":
        continue  # Skip empty (invalid) inputs
    print(f"Valid name entered: {name}")
# Output:
# Valid name entered: John
# Valid name entered: Alice
# Valid name entered: Bob
# Valid name entered: Eve

# Summary:
# - 'continue' is used to skip certain iterations in a loop based on a condition.
# - It helps filter out unwanted values or perform actions only for specific cases.
# - Works in both for and while loops.

