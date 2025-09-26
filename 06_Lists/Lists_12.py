# The insert() method for lists in Python
# --------------------------------------
# The insert() method adds an element at a specific position in a list.
# Syntax: list.insert(index, value)
# Existing elements from that index onward are shifted right.

# Basic Example 1: Insert at the beginning
numbers = [2, 3, 4]
numbers.insert(0, 1)
print("After insert at beginning:", numbers)  # Output: [1, 2, 3, 4]

# Basic Example 2: Insert in the middle
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")
print("After insert in middle:", fruits)  # Output: ['apple', 'banana', 'cherry']

# Intermediate Example: Insert at the end (using len())
colors = ["red", "green"]
colors.insert(len(colors), "blue")
print("After insert at end:", colors)  # Output: ['red', 'green', 'blue']

# Example: Insert using negative indexing
# Negative indices count from the end (-1 is the last position, -2 is second last, etc.)
letters = ["a", "b", "d"]
letters.insert(-1, "c")  # Inserts 'c' before the last element
print("After insert with negative index:", letters)  # Output: ['a', 'b', 'c', 'd']

# You can also use -2, -3, etc. to insert at other positions from the end.

# Real World Use Case: Insert a new task at a specific priority in a to-do list
# Suppose tasks are ordered by priority, and you want to add a new urgent task at the top
tasks = ["Email", "Meeting", "Code Review"]
tasks.insert(0, "Urgent Bug Fix")
print("Updated tasks:", tasks)  # Output: ['Urgent Bug Fix', 'Email', 'Meeting', 'Code Review']

# Summary:
# - insert() adds an item at a specific index in the list.
# - Existing items from that index onward are shifted right.
# - Useful for adding items at a specific position, such as priority or order.
