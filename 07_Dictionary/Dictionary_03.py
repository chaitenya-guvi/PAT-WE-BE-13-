# Ways to Create a Dictionary in Python
# -------------------------------------
# Dictionaries can be created in several ways. Here are the most common methods:

# 1. Using curly braces with key-value pairs
student = {"name": "Alice", "age": 20, "grade": "A"}
print("Curly braces:", student)

# 2. Using the dict() constructor with keyword arguments
person = dict(name="Bob", age=25, city="London")
print("dict() with keywords:", person)

# 3. Using the dict() constructor with a list of tuples
marks = dict([("Math", 90), ("Science", 85), ("English", 88)])
print("dict() with list of tuples:", marks)

# 4. Using dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Dictionary comprehension:", squares)

# 5. Creating an empty dictionary and adding items
data = {}
data["id"] = 101
data["status"] = "active"
print("Empty dict and add:", data)
data["status"] = "inactive"  # Update value
print("Updated dict:", data)

# Summary:
# - Curly braces {} with key-value pairs
# - dict() constructor with keywords or list of tuples
# - Dictionary comprehension
# - Start with empty dict and add items
# - All methods create a dictionary for fast key-value lookups

