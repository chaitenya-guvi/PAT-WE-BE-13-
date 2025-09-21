"""
The 'continue' statement in for loops
-------------------------------------
'continue' is used to skip the rest of the code
inside the loop for the current iteration and move
to the next iteration.
It is useful when you want to ignore certain values or conditions while looping.
"""
# Basic Example: Skip even numbers in a range
for number in range(1, 6):
    if number % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {number}")
# Output: Odd number: 1, 3, 5

# Real World Scenario: Print non-empty items from a shopping list
shopping_list = ["Milk", "", "Eggs", "", "Bread", "Butter", ""]
for item in shopping_list:
    if item == "":
        continue  # Skip empty items
    print(f"Buy: {item}")
# Output:
# Buy: Milk
# Buy: Eggs
# Buy: Bread
# Buy: Butter

# Summary:
# - 'continue' is used to skip certain iterations in a loop based on a condition.
# - It helps filter out unwanted values or perform actions only for specific cases.
# - Works in both for and while loops.

