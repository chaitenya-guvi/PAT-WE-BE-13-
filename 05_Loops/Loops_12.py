# Different patterns with smiley faces

# 1. Right triangle pattern (for loop)
print("\nRight triangle pattern (for loop):")
for row in range(1, 6):
    for col in range(row):
        print("\U0001f600", end=" ")
    print()

# 2. Left triangle pattern (while loop)
print("\nLeft triangle pattern (while loop):")
row = 1
while row <= 5:
    col = 0
    while col < row:
        print("\U0001f600", end=" ")
        col += 1
    print()
    row += 1
