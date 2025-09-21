# Loops_04.py
"""Demonstrating the range() function in for loops
The range() function generates a sequence of numbers, which is commonly used in for loops to specify the number of iterations.
Syntax: range(start, stop, step)
- start: The starting number of the sequence (inclusive). Default is 0.
- stop: The ending number of the sequence (exclusive).
- step: The difference between each number in the sequence. Default is 1.

range converts an integer into an iterable object
"""

print("\n--- Range Function Examples ---\n")

# Basic usage: range(stop)
print("Basic range(stop):")
for num in range(5):
    print(num, end=" ")  # Output: 0 1 2 3 4
print("\n")

# Range with start and stop: range(start, stop)
print("Range(start, stop):")
for num in range(2, 7):
    print(num, end=" ")  # Output: 2 3 4 5 6
print("\n")

# Range with start, stop, and step: range(start, stop, step)
print("Range(start, stop, step):")
for num in range(1, 10, 2):
    print(num, end=" ")  # Output: 1 3 5 7 9
print("\n")


string1 = "Chaitenya"
len_of_string1 = len(string1) #this returns the length of the string in integer
print("Length of string1:", len_of_string1)

for character in range(len_of_string1):
    print(string1[character], end=" ") # Output: C h a i t e n y a