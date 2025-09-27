# List Comprehension with Condition in Python
# ------------------------------------------
# Syntax: [expression for item in iterable if condition]
# This allows you to filter items from an iterable based on a condition while creating a new list.

# Example 1: Get even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# Example 2: Get words longer than 3 characters
words = ["cat", "elephant", "dog", "lion", "ant"]
long_words = [word for word in words if len(word) > 3]
print("Long words:", long_words)  # Output: ['elephant', 'lion']

# Example 3: Get positive numbers from a list
numbers = [-5, 3, 0, -2, 8, 7]
positive_numbers = [n for n in numbers if n > 0]
negative_numbers = [n for n in numbers if n < 0]
print("Positive numbers:", positive_numbers)  # Output: [3, 8, 7]
print("Negative numbers:", negative_numbers)


# Example 4: Get vowels from a string
text = "Python Programming"
vowels = [char for char in text if char.lower() in "aeiou"]
print("Vowels:", vowels)  # Output: ['o', 'o', 'a', 'i']

# Summary:
# - List comprehension with condition lets you filter and transform data in a single line.
# - The condition comes after 'for item in iterable' and before the closing bracket.
# - This technique is concise, readable, and efficient for creating filtered lists.

