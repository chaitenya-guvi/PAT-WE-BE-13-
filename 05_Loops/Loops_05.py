# Range with negative step (counting backwards)
print("Range with negative step:")
for num in range(10, 5, -1):
    print(num, end=" ")  # Output: 10 9 8 7 6
print("\n")

# Range with step greater than 1
print("Range with step 3:")
for num in range(0, 15, 3):
    print(num, end=" ")  # Output: 0 3 6 9 12
print("\n")

# Using range to iterate over indices of a list
print("Range for list indices:")
items = ["apple", "banana", "cherry", "date"]
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")
print()

# Using range to create a list (with list())
print("Create a list from range:")
numbers = list(range(5, 10))
print(numbers)  # Output: [5, 6, 7, 8, 9]

# Using range with reversed()
print("Reversed range:")
for num in reversed(range(3, 8)):
    print(num, end=" ")  # Output: 7 6 5 4 3
print()

# Using range with for loop for summing numbers
print("Sum numbers from 1 to 5:")
total = 0
for num in range(1, 6):
    total += num
print(total)  # Output: 15
