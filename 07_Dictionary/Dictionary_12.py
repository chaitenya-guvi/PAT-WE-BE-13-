# The pop() method in Python dictionaries
# --------------------------------------
# The pop() method removes the specified key and returns its value.
# If the key is not found, it raises a KeyError unless a default value is provided.

# Basic Example 1: Pop an existing key
person = {"name": "Alice", "age": 30, "city": "New York"}
age = person.pop("age")
print("After pop 'age':", person)  # Output: {'name': 'Alice', 'city': 'New York'}
print("Popped value:", age)         # Output: 30

# Basic Example 2: Pop another key
city = person.pop("city")
print("After pop 'city':", person)  # Output: {'name': 'Alice'}
print("Popped value:", city)        # Output: New York

# Basic Example 3: Pop a key with a default value (key not present)
country = person.pop("country", "Unknown")
print("After pop 'country':", person)  # Output: {'name': 'Alice'}
print("Popped value:", country)        # Output: Unknown


# print("execute pop without argument" , person.pop())

# If you try to pop a key that does not exist and do not provide a default, a KeyError is raised.
# Example:
print(person.pop("email", "unknown "))

# Summary:
# - pop(key) removes the key and returns its value.
# - If the key is not found, a KeyError is raised unless a default is provided.
# - pop() is useful for removing and retrieving values in one step.

