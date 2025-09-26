# The index() method for lists in Python
# -------------------------------------
# The index() method returns the first index of a specified value in a list.
# If the value is not found, it raises a ValueError.

# Basic Example 1: Find the index of a value
numbers = [10, 20, 30, 40, 50]
idx = numbers.index(30)
print("Index of 30:", idx)  # Output: 2

# Basic Example 2: Find the index of a string
fruits = ["apple", "banana", "cherry", "banana"]
idx = fruits.index("banana")
print("Index of 'banana':", idx)  # Output: 1 (first occurrence)

# Intermediate Example: Find the index of a value starting from a specific position
colors = ["red", "green", "blue", "green", "yellow"]
idx = colors.index("green", 2)  # Start searching from index 2
print("Index of 'green' after index 2:", idx)  # Output: 3

# Real World Use Case: Find the position of a task in a to-do list
tasks = ["Email", "Meeting", "Code Review", "Lunch"]
task_to_find = "Code Review"
if task_to_find in tasks:
    position = tasks.index(task_to_find)
    print(f"'{task_to_find}' is at position {position} in the to-do list.")
else:
    print(f"'{task_to_find}' is not in the to-do list.")

# Summary:
# - index() returns the first index of a value in a list.
# - You can specify a start (and optional end) position for searching.
# - Raises ValueError if the value is not found.
# - Useful for locating items, checking positions, or validating data.

