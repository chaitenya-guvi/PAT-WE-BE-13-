# The items() method in Python dictionaries
# ----------------------------------------
# The items() method returns a view object containing all key-value pairs as tuples.
# You can use it to loop through, access, or convert all key-value pairs in the dictionary.

# Example 1: Basic usage
student = {"name": "Alice", "age": 20, "grade": "A"}
print("All items:", student.items())  # Output: dict_items([('name', 'Alice'), ('age', 20), ('grade', 'A')])

for index,value in enumerate(['a','b','c']):
    print(f"{index} :  {value}")

# Example 2: Looping through all key-value pairs
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

# Example 3: Convert items to a list of tuples
items_list = list(student.items())
print("Items as list:", items_list)  # Output: [('name', 'Alice'), ('age', 20), ('grade', 'A')]

# Example 4: Using items() for conditional logic
person = {"name": "Bob", "age": 25, "city": "London"}
for key, value in person.items():
    if key == "city" and value == "London":
        print("Person lives in London.")

# Summary:
# - items() returns a view object of all key-value pairs as tuples.
# - Useful for looping, searching, or converting items to a list.
# - The view updates if the dictionary changes.

