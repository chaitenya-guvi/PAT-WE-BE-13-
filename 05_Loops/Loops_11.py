# Print a smiley face pattern using both for loop and while loop

# Using for loop to print a 5x5 grid of smiley faces
print("Pattern using for loop:")
for row in range(5):
    for col in range(5):
        print("\U0001f600", end=" ")
    print()  # Newline after each row

# Using while loop to print a 5x5 grid of smiley faces
print("\nPattern using while loop:")
row = 0
while row < 5:
    col = 0
    while col < 5:
        print("\U0001f600", end=" ")
        col += 1
    print()  # Newline after each row
    row += 1


