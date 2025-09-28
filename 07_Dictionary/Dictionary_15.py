# Dictionary Comprehension in Python
# ---------------------------------
# Dictionary comprehension provides a concise way to create dictionaries from iterables.
# Syntax: {key_expression: value_expression for item in iterable}
# You can also add an optional condition: {key: value for item in iterable if condition}

# Example 1: Create a dictionary of squares from 1 to 5
squares = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: Create a dictionary from two lists (zip)
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print("Combined dictionary:", combined)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Example 3: Filter items with a condition (only even numbers)
numbers = range(1, 7)
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print("Even squares dictionary:", even_squares)  # Output: {2: 4, 4: 16, 6: 36}

# Summary:
# - Dictionary comprehension is a compact way to create dictionaries from iterables.
# - You can use expressions and conditions to transform and filter data.
# - It makes code shorter, more readable, and often faster than using loops.

