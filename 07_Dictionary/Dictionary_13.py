# The popitem() method in Python dictionaries
# ------------------------------------------
# The popitem() method removes and returns the last inserted key-value pair as a tuple.
# In Python 3.7+, dictionaries preserve insertion order, so popitem() removes the last item.
# If the dictionary is empty, popitem() raises a KeyError.

# Basic Example 1: Pop the last item from a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
item = person.popitem()
print("After popitem:", person)  # Output: {'name': 'Alice', 'age': 30}
print("Popped item:", item)      # Output: ('city', 'New York')

# Basic Example 2: Pop another item (now the new last item)
item2 = person.popitem()
print("After popitem again:", person)  # Output: {'name': 'Alice'}
print("Popped item:", item2)           # Output: ('age', 30)

# Basic Example 3: Pop the last remaining item
item3 = person.popitem()
print("After final popitem:", person)  # Output: {}
print("Popped item:", item3)           # Output: ('name', 'Alice')

# If you try to popitem() from an empty dictionary, a KeyError is raised.
# Example:
person.popitem()  # Raises KeyError


# Summary:
# - popitem() removes and returns the last inserted key-value pair as a tuple.
# - Raises KeyError if the dictionary is empty.
# - Useful for destructively iterating or emptying a dictionary.

