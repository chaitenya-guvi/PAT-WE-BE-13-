# 3. Pyramid pattern (for loop)
print("\nPyramid pattern (for loop):")
rows = 5
for row in range(1, rows + 1):
    print(" " * (rows - row) * 2, end="")
    for col in range(2 * row - 1):
        print("\U0001f600", end=" ")
    print()

# 4. Diamond pattern (for loop)
print("\nDiamond pattern (for loop):")
rows = 5
# Top half
for row in range(1, rows + 1):
    print(" " * (rows - row) * 2, end="")
    for col in range(2 * row - 1):
        print("\U0001f600", end=" ")
    print()
# Bottom half
for row in range(rows - 1, 0, -1):
    print(" " * (rows - row) * 2, end="")
    for col in range(2 * row - 1):
        print("\U0001f600", end=" ")
    print()

# 5. Hollow square pattern (for loop)
print("\nHollow square pattern (for loop):")
size = 5
for row in range(size):
    for col in range(size):
        if row == 0 or row == size - 1 or col == 0 or col == size - 1:
            print("\U0001f600", end=" ")
        else:
            print("  ", end=" ")
    print()
