# Checking if a Value is in a List in Python
# ------------------------------------------
# You can check if a value exists in a list using the 'in' keyword.
# This is useful for searching, validation, and decision making.

# Example 1: Basic usage
fruits = ["apple", "banana", "cherry", "date"]
if "banana" in fruits:
    print("'banana' is in the list.")
else:
    print("'banana' is not in the list.")

# Example 2: Value not present
if "mango" in fruits:
    print("'mango' is in the list.")
else:
    print("'mango' is not in the list.")

# Example 3: Using 'in' with numbers
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("3 is in the list.")

# Example 4: Using 'in' in a loop for validation
user_input = "cherry"
if user_input in fruits:
    print(f"{user_input} is available!")
else:
    print(f"{user_input} is not available.")

# Summary:
# - Use 'in' to check if a value exists in a list.
# - Returns True if the value is found, False otherwise.
# - Works with lists containing any data type.

