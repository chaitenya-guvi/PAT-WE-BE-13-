# The pop() method for lists in Python
# ------------------------------------
# The pop() method removes and returns an element from a list.
# By default, it removes the last item, but you can specify an index to remove a specific item.

# Basic Example 1: Pop the last item from a list
numbers = [1, 2, 3, 4]
removed = numbers.pop()
print("After pop:", numbers)  # Output: [1, 2, 3]
print("Removed item:", removed)  # Output: 4

# Basic Example 2: Pop an item at a specific index
fruits = ["apple", "banana", "cherry", "date"]
removed_fruit = fruits.pop(1)  # Removes 'banana' (index 1)
print("After pop at index 1:", fruits)  # Output: ['apple', 'cherry', 'date']
print("Removed fruit:", removed_fruit)  # Output: banana

# Intermediate Example: Pop items in a loop until the list is empty
colors = ["red", "green", "blue"]
while colors:
    color = colors.pop()
    print(f"Processing color: {color}")
print("Colors after popping all:", colors)  # Output: []

# Real World Use Case: Undo last action in a to-do list app
# Each action is stored in a list; pop() is used to remove the last action (undo)
actions = ["add task", "edit task", "delete task"]
last_action = actions.pop()
print("Actions after undo:", actions)  # Output: ['add task', 'edit task']
print("Undone action:", last_action)  # Output: delete task

# Summary:
# - pop() removes and returns an item from a list (last by default, or at a given index).
# - It modifies the original list in place.
# - Useful for removing items, processing lists, or implementing undo features.

