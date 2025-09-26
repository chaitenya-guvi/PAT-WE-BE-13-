# The extend() method for lists in Python
# --------------------------------------
# The extend() method adds all elements from an iterable (like another list) to the end of the current list.
# It is useful for combining lists or adding multiple items at once.

# Basic Example 1: Extend with another list
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print("After extend:", numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Basic Example 2: Extend with a tuple
fruits = ["apple", "banana"]
fruits.extend(("cherry", "date"))
print("Fruits list:", fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

# Intermediate Example: Extend with a string (adds each character)
letters = ["a", "b"]
letters.extend("cd")
print("Letters list:", letters)  # Output: ['a', 'b', 'c', 'd']

# Real World Use Case: Merging two shopping lists
shopping_list_1 = ["milk", "eggs"]
shopping_list_2 = ["bread", "butter", "cheese"]
shopping_list_1.extend(shopping_list_2)
print("Combined shopping list:", shopping_list_1)  # Output: ['milk', 'eggs', 'bread', 'butter', 'cheese']

# Summary:
# - extend() adds all elements from an iterable to the end of a list.
# - It modifies the original list in place and does not return a new list.
# - Useful for combining lists, adding multiple items, or merging data from different sources.

