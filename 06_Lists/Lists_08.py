# Accessing all values in a list using for loop and while loop
# -----------------------------------------------------------
# Example 1: Using for loop (basic)
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(fruit)

# Example 2: Using for loop with index
numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    print(numbers[i])

#example 2 different way: Using for loop (direct iteration)
numbers = [10, 20, 30, 40]
for inum in numbers:
    print(inum)

# Example 3: Using while loop (basic)
colors = ["red", "green", "blue", "yellow"]
index = 0
while index < len(colors):
    print(colors[index])
    index += 1

# Example 4: Using while loop with modification (print values in reverse)
animals = ["cat", "dog", "bird", "fish"]
index = len(animals) - 1
while index >= 0:
    print(animals[index])
    index -= 1

# These examples show how to access all values in a list using both for and while loops, with direct iteration and index-based access.

