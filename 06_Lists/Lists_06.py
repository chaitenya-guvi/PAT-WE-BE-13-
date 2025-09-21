# Another Way to Make a List in Python
# -----------------------------------
# You can create a list using the built-in list() function.
# This is especially useful when converting other data types (like ranges, tuples, or strings) into lists.

# Example: Creating a list from a range
# The range() function generates a sequence of numbers, but it's not a list by default.
tasks = list(range(1, 4))
print("Tasks list:", tasks)  # Output: [1, 2, 3]

# You can use list() to convert other data types to lists as well:

# Convert a tuple to a list
tuple_data = (10, 20, 30)
list_from_tuple = list(tuple_data)
print("List from tuple:", list_from_tuple)  # Output: [10, 20, 30]

# Convert a string to a list of characters
string_data = "abc"
list_from_string = list(string_data)
print("List from string:", list_from_string)  # Output: ['a', 'b', 'c']

#convert list back to string
joined_string = ''.join(list_from_string)
print("Joined string:", joined_string)  # Output: abc

# Summary:
# - The list() function is a flexible way to create lists from ranges, tuples, strings, and other iterables.
# - We'll use this technique more later with several other data types!

