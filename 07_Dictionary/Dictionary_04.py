# Accessing Values in a Dictionary in Python
# -----------------------------------------
# You can access values in a dictionary using their keys.
# The most common way is with square brackets: dict[key]
# You can also use the get() method for safer access.

# Example 1: Accessing values with square brackets
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Name:", person["name"])      # Output: Alice
print("Age:", person["age"])        # Output: 30
print("City:", person["city"])      # Output: New York

# Example 2: Accessing values with get() method
print("Name (get):", person.get("name"))      # Output: Alice
print("Country (get):", person.get("country")) # Output: None (key not found)

# Example 3: Accessing nested dictionary values
student = {
    "name": "Bob",
    "marks": {"Math": 90, "Science": 85}
}
print("Math marks:", student["marks"]["Math"])  # Output: 90

# print(student["age"]) # This will raise a KeyError since "age" key does not exist
print(student.get("age")) # This will return None since "age" key does not exist

# Summary:
# - Use dict[key] to access a value by key (raises KeyError if key not found).
# - Use dict.get(key) for safer access (returns None or a default value if key not found).
# - You can access nested values with multiple keys.
# - Use dict.items() to loop through all key-value pairs.

