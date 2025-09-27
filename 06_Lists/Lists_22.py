# Copying Lists in Python
# ----------------------
# There are several ways to copy a list in Python. The simplest is a normal (shallow) copy.
# A normal copy creates a new list with the same elements as the original.
# Changes to the new list do not affect the original (for top-level elements).

# Example 1: Using slicing to copy a list
original = [1, 2, 3, 4]
print("Original:", original)
copy1 = original  # this syntax just points to the address of original
copy1.append(5)
print("Original:", original)  # Output: [1, 2, 3, 4]
print("Copy1:", copy1)        # Output: [1, 2, 3, 4, 5]


print("----")
print("Examle2")
print("-----")
# Example 2: Using the list() constructor
# here a new object is created
copy2 = list(original)  #creates a shallow copy
print("Copy2 before modification:", copy2)  # Output: [1, 2, 3, 4, 5]
copy2.remove(2)
print("Original:", original)  # Output: [1, 2, 3, 4]
print("Copy2:", copy2)        # Output: [1, 3, 4]



# Example 3: Using the copy() method
# creating a shallow copy
print("----")
print("Examle3")
print("-----")
copy3 = original.copy()  # creates a shallow copy
print("Copy3 before modification:", copy3)  # Output: [1, 2, 3, 4, 5]
copy3[0] = 99
print("Original:", original)  # Output: [1, 2, 3, 4]
print("Copy3:", copy3)        # Output: [99, 2, 3, 4]

# Note: All these methods create a shallow copy. If the list contains mutable objects
# (like other lists), changes to those objects will affect both lists.

# Example 4: Shallow copy with nested lists
print("----")
print("Examle4")
print("-----")
nested = [[1, 2], [3, 4]]
shallow_copy = nested
shallow_copy[0][0] = 99
print("Nested:", nested)           # Output: [[99, 2], [3, 4]]
print("Shallow copy:", shallow_copy) # Output: [[99, 2], [3, 4]]

print("----")
print("Examle5")
print("-----")
nested = [[1, 2], [3, 4]]
shallow_copy_with_list = list(nested)
shallow_copy_with_list[0][0] = 88
print("Nested:", nested)                 # Output: [[88, 2], [3, 4]]
print("Shallow copy with list():", shallow_copy_with_list) # Output: [[88, 2], [3, 4]]
# Summary:
# - Normal copy (shallow copy) creates a new list with the same top-level elements.
# - Use slicing [:], list(), or copy() to make a shallow copy.
# - For nested lists, use the copy module's deepcopy() for a true independent copy.

