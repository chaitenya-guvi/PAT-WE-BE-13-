# The clear() method for lists in Python
# -------------------------------------
# The clear() method removes all items from a list, making it empty.
# It is useful when you want to reuse a list or reset its contents.

# Basic Example 1: Clear a list of numbers
numbers = [1, 2, 3, 4]
numbers.clear()
print("After clear:", numbers)  # Output: []

# Basic Example 2: Clear a list of strings
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print("After clear:", fruits)  # Output: []

# Intermediate Example: Clear a list after processing its items
tasks = ["task1", "task2", "task3"]
for task in tasks:
    print(f"Processing: {task}")
tasks.clear()
print("Tasks after processing:", tasks)  # Output: []

# Real World Use Case: Resetting a shopping cart after checkout
shopping_cart = ["milk", "eggs", "bread"]
# Simulate checkout
print("Checking out items:", shopping_cart)
shopping_cart.clear()  # Empty the cart after purchase
print("Shopping cart after checkout:", shopping_cart)  # Output: []

# Summary:
# - clear() removes all elements from a list, leaving it empty.
# - It modifies the original list in place and does not return a new list.
# - Useful for resetting lists in programs, such as after processing or checkout.

