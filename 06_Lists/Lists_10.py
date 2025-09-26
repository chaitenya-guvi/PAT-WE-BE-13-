# The append() method for lists in Python
# --------------------------------------
# The append() method adds a single element to the end of a list.
# It is commonly used to grow a list one item at a time.

# Basic Example: Add a value to a list
numbers = [1, 2, 3]
numbers.append(4)
print("After append:", numbers)  # Output: [1, 2, 3, 4]

# Intermediate Example: Append values in a loop
fruits = []
for fruit in ["apple", "banana", "cherry"]:
    fruits.append(fruit)
print("Fruits list:", fruits)  # Output: ['apple', 'banana', 'cherry']

# You can append any data type, including another list (which creates a nested list)
fruits.append(["date", "elderberry"])
print("After appending a list:", fruits)

fruits.append("string1")
print("After appending a list:", fruits)  # Output: ['apple', 'banana', 'cherry', ['date', 'elderberry']]

# Summary:
# - append() adds a single item to the end of a list.
# - It does not return a new list; it modifies the original list in place.
# - You can use append() in loops or to build lists dynamically.

