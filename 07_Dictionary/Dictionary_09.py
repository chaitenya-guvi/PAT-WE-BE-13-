# The copy() method in Python dictionaries
# ---------------------------------------
# The copy() method creates a shallow copy of a dictionary.
# This means it returns a new dictionary with the same key-value pairs as the original.
# Changes to the new dictionary do not affect the original, and vice versa (for top-level keys/values).

d1 = {"a": 1, "b": 2}
d2 = d1
d2["a"] = 99
print(d1)  # Output: {'a': 99, 'b': 2}
print(d2)  # Output: {'a': 99, 'b': 2}
# Here, modifying d2 also modified d1 because both variables reference the same dictionary object.

# Example 1: Basic usage
original = {"a": 1, "b": 2, "c": 3}
copy_dict = original.copy()
print("Original:", original)      # Output: {'a': 1, 'b': 2, 'c': 3}
print("Copy:", copy_dict)         # Output: {'a': 1, 'b': 2, 'c': 3}

# Modifying the copy does not affect the original
del copy_dict["b"]
print("After deleting 'b' from copy:", copy_dict)  # Output: {'a': 1, 'c': 3}
print("Original remains:", original)              # Output: {'a': 1, 'b': 2, 'c': 3}

# Example 2: Shallow copy and nested dictionaries
nested = {"x": 1, "y": {"z": 2}}
shallow_copy = nested.copy()
shallow_copy["y"]["z"] = 99
print("Nested after change in copy:", nested)      # Output: {'x': 1, 'y': {'z': 99}}
print("Shallow copy:", shallow_copy)               # Output: {'x': 1, 'y': {'z': 99}}

# Note: copy() only copies the top-level dictionary. If the values are mutable objects (like lists or other dicts), changes to those objects will affect both the original and the copy.

# Summary:
# - copy() creates a shallow copy of a dictionary.
# - Top-level changes to the copy do not affect the original.
# - Changes to nested mutable objects affect both.
# - Use copy() to duplicate a dictionary when you want to modify it without changing the original.

