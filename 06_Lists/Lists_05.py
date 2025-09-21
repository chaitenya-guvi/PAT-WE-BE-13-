# Length of Lists in Python
# ------------------------
# The length of a list is the number of elements it contains.
# You can find the length of a list using the built-in len() function.

# Example 1: Basic usage
fruits = ["apple", "banana", "cherry", "date"]
print("Number of fruits:", len(fruits))  # Output: 4

# Example 2: Empty list
empty_list = []
print("Length of empty list:", len(empty_list))  # Output: 0

# Example 3: List with mixed data types
mixed_list = [1, "hello", 3.14, True]
print("Length of mixed list:", len(mixed_list))  # Output: 4

# Example 4: List within a list (nested list)
nested_list = [[1, 2, 3], ["a", "b"], [True, False, None]]
print("Nested list:", nested_list)  # Output: [[1, 2, 3], ['a', 'b'], [True, False, None]]
print("Length of nested list:", len(nested_list))  # Output: 3
print("Length of first inner list:", len(nested_list[0]))  # Output: 3
print("Length of second inner list:", len(nested_list[1]))  # Output: 2

# The len() function returns the number of top-level elements in the list.
# To get the length of an inner list, use len() on that element (e.g., len(nested_list[0])).

# The len() function works for any list, regardless of the types of elements inside.
# You can use len() to check the size of a list before looping, adding, or removing elements.
