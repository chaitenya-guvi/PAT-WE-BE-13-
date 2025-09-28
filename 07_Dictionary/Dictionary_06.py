# The keys() method in Python dictionaries
# ---------------------------------------
# The keys() method returns a  object containing all the keys in the dictionary.
# You can use it to access, loop through, or convert all keys to a list.

# Example 1: Basic usage
student = {"name": "Alice", "age": 20, "grade": "A"}
print("All keys:", student.keys())  # Output: dict_keys(['name', 'age', 'grade'])

# Example 2: Looping through all keys
for key in student.keys():
    print("Key:", key)

# Example 3: Convert keys to a list
keys_list = list(student.keys())
print("Keys as list:", keys_list)  # Output: ['name', 'age', 'grade']

# Example 4: Using keys() with conditional logic
person = {"name": "Bob", "age": 25, "city": "London"}
if "city" in person.keys():
    print("Person has a city key.")

#  default python checks keys in a dictionary with "in" operator
if "city" in person:
    print("Person has a city key.")


# Summary:
# - keys() returns a  object of all keys in the dictionary.
# - Useful for looping, searching, or converting keys to a list.
# - The view updates if the dictionary changes.

