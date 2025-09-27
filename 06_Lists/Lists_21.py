# Nested Lists in Python
# ---------------------
# A nested list is a list that contains other lists as its elements.
# You can access elements in a nested list using multiple indices.

"""
# Example 1: Basic nested list and accessing an inner list
# tic tac toe board o x x
                    o o o
                    x x x
"""
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("First inner list:", nested[0])  # Output: [1, 2, 3]

# Example 2: Accessing an element inside an inner list
print("Element at row 2, column 3:", nested[1][2])  # Output: 6

# Example 3: Looping through all inner lists
for inner_list in nested:
    print("Inner list:", inner_list)

# Example 4: Looping through all elements in a nested list (row by row)
for row in nested:
    for value in row:
        print(value, end=" ")
    print()  # Newline after each row

# Summary:
# - Nested lists are lists containing other lists.
# - Access an inner list with one index (e.g., nested[0]).
# - Access an element inside an inner list with two indices (e.g., nested[1][2]).
# - You can loop through inner lists or all elements using nested loops.

