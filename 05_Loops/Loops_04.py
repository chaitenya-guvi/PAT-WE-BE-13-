# Loops_04.py


print('This is Loops_04.py')
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

