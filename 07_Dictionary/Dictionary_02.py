# Introduction to Dictionary in Python
# -----------------------------------
# A dictionary is a built-in data type in Python that stores data as key-value pairs.
# Each key in a dictionary is unique, and values can be of any data type.
# Dictionaries are useful for fast lookups, mapping relationships, and storing structured data.

# Basic dictionary example with different data types
person = {
    "name": "Alice",           # String
    "age": 30,                  # Integer
    "height": 5.5,              # Float
    "is_student": False,        # Boolean
    "skills": ["Python", "SQL"], # List
    "address": {                # Nested dictionary
        "city": "New York",
        "zip": "10001"
    }
}

print("Person dictionary:", person)

# You can access values using their keys:
print("Name:", person["name"])
print("Skills:", person["skills"])
print("City:", person["address"]["city"])
print("Skills", person["skills"][0])  # Accessing first skill using list indexing

# Summary:
# - Dictionaries use curly braces {} and key-value pairs separated by colons.
# - Keys must be unique and immutable (e.g., strings, numbers, tuples).
# - Values can be any data type, including lists and other dictionaries.
# - Dictionaries are ideal for storing related data and fast lookups by key.

