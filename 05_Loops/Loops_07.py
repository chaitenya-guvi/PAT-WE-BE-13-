# Advanced Example: Generating a Multiplication Table using for loop and range
# This program prints a formatted multiplication table for numbers 1 to 10

print("Multiplication Table (1 to 10):\n")

# Print header row
for col in range(1, 11):
    print(f"{col:4}", end="")
print()
print("-" * 44)

# Print table rows
for row in range(1, 11):
    for col in range(1, 11):
        print(f"{row * col:4}", end="")
    print()  # Newline after each row

# This program demonstrates nested for loops and range to create a formatted multiplication table.
# You can change the range to generate larger or smaller tables as needed.

