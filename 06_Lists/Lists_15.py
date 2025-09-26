# The remove() method for lists in Python
# --------------------------------------
# The remove() method deletes the first occurrence of a specified value from a list.
# If the value is not found, it raises a ValueError.

# Basic Example 1: Remove a value from a list
numbers = [1, 2, 3, 4]
numbers.remove(3)
print("After remove 3:", numbers)  # Output: [1, 2, 4]

# Basic Example 2: Remove a string from a list
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print("After remove 'banana':", fruits)  # Output: ['apple', 'cherry', 'banana']
# Only the first occurrence is removed

# Intermediate Example: Remove items in a loop
colors = ["red", "green", "blue", "green"]
while "green" in colors:
    colors.remove("green")
print("After removing all 'green':", colors)  # Output: ['red', 'blue']

# Real World Use Case: Remove a completed task from a to-do list
tasks = ["Email", "Meeting", "Code Review", "Meeting"]
tasks.remove("Meeting")
print("Tasks after removing completed 'Meeting':", tasks)  # Output: ['Email', 'Code Review', 'Meeting']

numbers.remove(10) #valuerror if the value is not found

# Summary:
# - remove() deletes the first occurrence of a value from a list.
# - If the value is not found, a ValueError is raised.
# - Useful for deleting specific items, but be careful with duplicates and missing values.

