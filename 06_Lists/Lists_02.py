# Mutability in Python: Lists vs Strings/Integers
# -----------------------------------------------
# Lists are mutable — they can be changed after creation.
# Strings and integers are immutable — they cannot be changed after creation.

# Example 1: Lists are mutable
numbers = [1, 2, 3]
numbers[0] = 10  # Change the first element
numbers.append(4)  # Add a new element
print("Modified list:", numbers)  # Output: [10, 2, 3, 4]

# Example 2: Strings are immutable
text = "hello"
# text[0] = "H"  # This will raise an error
new_text = "H" + text[1:]  # Create a new string
print("Original string:", text)      # Output: hello
print("Modified string:", new_text)  # Output: Hello

# Example 3: Integers are immutable
num = 5
print("Original integer id :",id(num))
# num[0] = 10  # This will raise an error
num = num + 1  # Creates a new integer object
print("Modified integer id :", id(num))
print("Original integer:", 5)
print("Modified integer:", num)  # Output: 6


# Summary:
# - Lists can be changed in-place (mutable).
# - Strings and integers cannot be changed in-place (immutable); any modification creates a new object.

