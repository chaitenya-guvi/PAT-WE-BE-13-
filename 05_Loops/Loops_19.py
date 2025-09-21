# For loop using enumerate in Python
# ----------------------------------
# The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# It is useful for getting both the index and the value when looping through a sequence.

# Example 1: Enumerate a list of fruits
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Example 2: Enumerate a string
text = "cat"
for index, char in enumerate(text):
    print(f"Index: {index}, Character: {char}")

# Example 3: Enumerate a list with a custom start index
colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):
    print(f"Color {index}: {color}")

# Example 4: Enumerate a tuple of numbers
numbers = (10, 20, 30, 40)
for idx, num in enumerate(numbers):
    print(f"Position: {idx}, Value: {num}")

# Summary:
# - enumerate() is useful for getting both index and value in a for loop.
# - You can specify a custom start index with enumerate(iterable, start=n).
# - Works with lists, strings, tuples, and other iterables.
