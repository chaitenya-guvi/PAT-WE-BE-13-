# Accessing Values in a List in Python
# ------------------------------------
# You can access individual elements in a list using their index (position).
# Indexing starts at 0 for the first element.

# Example 1: Accessing by index
fruits = ["apple", "banana", "cherry", "date"]
print("First fruit:", fruits[0])    # Output: apple
print("Second fruit:", fruits[1])   # Output: banana
print("Last fruit:", fruits[3])     # Output: date

# Example 2: Negative indexing (from the end)
print("Last fruit (negative index):", fruits[-1])  # Output: date
print("Second last fruit:", fruits[-2])            # Output: cherry

# Example 3: Accessing values in a loop
for fruit in fruits:
    print("Fruit:", fruit)

# Example 4: Accessing values with enumerate (index and value)
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Summary:
# - Use list[index] to access a specific value.
# - Indexing starts at 0; negative indices count from the end.
# - You can loop through a list to access all values.
# - Use enumerate() to get both index and value while looping.

