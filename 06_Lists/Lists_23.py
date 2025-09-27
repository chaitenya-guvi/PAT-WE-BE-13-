# Deep Copy in Lists in Python
# ---------------------------
# A deep copy creates a new list and recursively copies all nested objects inside it.
# This means changes to nested objects in the copy do NOT affect the original list, and vice versa.
# Use the copy module's deepcopy() function for a deep copy.

import copy

# Example 1: Shallow copy (for comparison)
nested_list = [[1, 2], [3, 4]]
shallow_copy = nested_list[:]
shallow_copy[0][0] = 99
print("After shallow copy modification:")
print("Original:", nested_list)        # Output: [[99, 2], [3, 4]]
print("Shallow copy:", shallow_copy)   # Output: [[99, 2], [3, 4]]

print("----")
print("Examle2")
print("-----")

# Example 2: Deep copy
nested_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested_list)
print("Before deep copy modification:", deep_copy)  # Output: [[1, 2], [3, 4]]
deep_copy[0][0] = 88
print("\nAfter deep copy modification:")
print("Original:", nested_list)        # Output: [[1, 2], [3, 4]]
print("Deep copy:", deep_copy)         # Output: [[88, 2], [3, 4]]

# Summary:
# - Shallow copy only copies the outer list; nested objects are shared.
# - Deep copy copies all nested objects, so changes in the copy do not affect the original.
# - Use copy.deepcopy() for a true independent copy of lists with nested mutable objects.

