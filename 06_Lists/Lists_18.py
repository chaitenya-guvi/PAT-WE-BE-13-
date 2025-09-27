# List Comprehension in Python
# ---------------------------
# List comprehension provides a concise way to create lists.
# Syntax: [expression for item in iterable]
# You can also add an optional condition: [expression for item in iterable if condition]

# Example 1: Create a list of squares from 1 to 5
squares = [num**2 for num in range(1, 6)]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# Example 2: Create a list of even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)  # Output: [2, 4, 6, 8, 10]

# Example 3: Convert a list of strings to uppercase
words = ["python", "list", "comprehension"]
upper_words = [word.upper() for word in words]
print("Uppercase words:", upper_words)  # Output: ['PYTHON', 'LIST', 'COMPREHENSION']

words = ["python", "list", "comprehension"]
upper_words = [word.upper() for word in words if word[0] == 'p']
print("Uppercase words:", upper_words)  # Output: ['PYTHON', 'LIST', 'COMPREHENSION']

# Example 4: Extract digits from a string
text = "a1b2c3d4"
digits = [char for char in text if char.isdigit()]
print("Digits:", digits)  # Output: ['1', '2', '3', '4']

# Example 5: Create a list of tuples (number, square)
tuple_list = [(x, x**2) for x in range(1, 6)]
print("Tuples:", tuple_list)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Example 6: Filter out negative numbers from a list
numbers = [3, -1, 5, -2, 7, 0]
positive_numbers = [n for n in numbers if n >= 0]
print("Positive numbers:", positive_numbers)  # Output: [3, 5, 7, 0]

# Summary:
# - List comprehension is a compact way to create lists from iterables.
# - You can use expressions and conditions to transform and filter data.
# - It makes code shorter, more readable, and often faster than using loops.

