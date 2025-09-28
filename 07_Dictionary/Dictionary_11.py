# Accessing Values in a Dictionary in Python
# -----------------------------------------
# You can access values in a dictionary using their keys directly or with the get() method.
# dict[key] raises a KeyError if the key is not found.
# dict.get(key) returns None (or a default value) if the key is not found.

# Basic Example 1: Accessing value with key
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Name:", person["name"])  # Output: Alice
print("Name (get):", person.get("name"))  # Output: Alice

# Basic Example 2: Accessing a missing key
# print(person["country"])  # Raises KeyError
print("Country (get):", person.get("country"))  # Output: None

# Basic Example 3: Using get() with a default value
print("Country (get, default):", person.get("country", "Unknown"))  # Output: Unknown

# Intermediate Example 1: Accessing nested dictionary values
student = {
    "name": "Bob",
    "marks": {"Math": 90, "Science": 85}
}
print("Math marks:", student["marks"]["Math"])  # Output: 90
print("Math marks (get):", student.get("marks", {}).get("Math"))  # Output: 90

# Intermediate Example 2: Safe access in a loop with get()
users = [
    {"username": "john", "email": "john@example.com"},
    {"username": "jane"},  # No email key
    {"username": "bob", "email": "bob@example.com"}
]
for user in users:
    print(f"Email for {user["username"]}:", user.get("email", "No email provided"))

# Summary:
# - Use dict[key] for direct access (raises KeyError if key is missing).
# - Use dict.get(key) for safe access (returns None or a default value if key is missing).
# - get() is especially useful for missing keys, nested dictionaries, and safe access in loops.

