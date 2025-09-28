# The values() method in Python dictionaries
# -----------------------------------------
# keys , values , items
# The values() method returns a view object containing all the values in the dictionary.
# You can use it to access, loop through, or convert all values to a list.

# Example 1: Basic usage
student = {"name": "Alice", "age": 20, "grade": "A"}
print("All values:", student.values())  # Output: dict_values(['Alice', 20, 'A'])

# Example 2: Looping through all values
for value in student.values():
    print("Value:", value)

# Example 3: Convert values to a list
values_list = list(student.values())
print("Values as list:", values_list)  # Output: ['Alice', 20, 'A']

# Example 4: Using values() with conditional logic
person = {"name": "Bob", "age": 25, "city": "London"}
if "London" in person.values():
    print("Person lives in London.")

# Summary:
# - values() returns a view object of all values in the dictionary.
# - Useful for looping, searching, or converting values to a list.
# - The view updates if the dictionary changes.

