# List Comprehension vs Looping in Python
# --------------------------------------
# List comprehension provides a concise way to create lists, while traditional looping uses a for loop and appends items one by one.
# List comprehensions are often shorter, more readable, and faster for simple transformations and filtering.

# Example 1: Create a list of squares from 1 to 5
# Using a for loop
squares_loop = []
for num in range(1, 6):
    squares_loop.append(num**2)
print("Squares with loop:", squares_loop)  # Output: [1, 4, 9, 16, 25]

# Using list comprehension
squares_comp = [num**2 for num in range(1, 6)]
print("Squares with comprehension:", squares_comp)  # Output: [1, 4, 9, 16, 25]

# Example 2: Filter even numbers from 1 to 10
# Using a for loop
evens_loop = []
for number in range(1, 11):
    if number % 2 == 0:
        evens_loop.append(number)
    else:
        print(f"{number} is not even.")
print("Evens with loop:", evens_loop)  # Output: [2, 4, 6, 8, 10]

# Using list comprehension
evens_comp = [x for x in range(1, 11) if x % 2 == 0]
print("Evens with comprehension:", evens_comp)  # Output: [2, 4, 6, 8, 10]

# Summary:
# - List comprehensions are more compact and readable for simple list creation and filtering.
# - Traditional loops are more flexible for complex logic but require more lines of code.
# - Both approaches produce the same result for these examples.

