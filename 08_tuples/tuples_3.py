# tuples_3.py

# Tuples can contain nested structures
nested_tuple = (1, 2, (3, 4), [5, 6] ,{'a':8, 'b':9})
print("Nested Tuple:", nested_tuple)

# Accessing elements in nested tuples
print("First element of nested tuple:", nested_tuple[2][0])  # Output: 3
print("Second element of nested list:", nested_tuple[3][1])  # Output:


# Note :  Mutable elements inside a tuple can be changed
nested_tuple[3][0] = 50
print("Modified Nested Tuple:", nested_tuple)  # Output: (1, 2, (3, 4), [50, 6])

# ? modify dictionary inside nested tuple
nested_tuple[4].update(c=10)
print(f"tuple after updating mutable dictionary inside it: {nested_tuple}")

del nested_tuple[4]
# Note: You cannot change the tuple itself, but you can modify mutable elements inside it.
