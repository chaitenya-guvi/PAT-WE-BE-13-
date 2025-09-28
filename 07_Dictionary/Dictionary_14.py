# The update() method in Python dictionaries
# -----------------------------------------
# The update() method updates a dictionary with key-value pairs from another dictionary or from an iterable of key-value pairs.
# Existing keys are overwritten; new keys are added.

# Basic Example 1: Update with another dictionary
person = {"name": "Alice", "age": 30}
person["new_key"] = "new_value"
print(person)
update_data = {"city": "New York", "age": 31}
person.update(update_data)
print("After update:", person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Basic Example 2: Update with keyword arguments
person.update(country="USA", email="alice@example.com")
print("After update with kwargs:", person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA', 'email': 'alice@example.com'}

# Basic Example 3: Update with a list of tuples
person.update([("phone", "123-4567"), ("age", 32)])
print("After update with list of tuples:", person)  # Output: {'name': 'Alice', 'age': 32, 'city': 'New York', 'country': 'USA', 'email': 'alice@example.com', 'phone': '123-4567'}

# Intermediate Example 1: Update with another dictionary containing overlapping and new keys
profile = {"username": "alice123", "email": "alice@oldmail.com"}
update_profile = {"email": "alice@newmail.com", "phone": "555-1234"}
profile.update(update_profile)
print("After profile update:", profile)  # Output: {'username': 'alice123', 'email': 'alice@newmail.com', 'phone': '555-1234'}



# Summary:
# - update() can take another dictionary, keyword arguments, or an iterable of key-value pairs.
# - Existing keys are overwritten; new keys are added.
# - Useful for merging, extending, or modifying dictionaries efficiently.
