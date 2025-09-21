# The 'break' statement in Python loops
# -------------------------------------
# 'break' is used to exit a loop immediately, even if the loop condition is still True.
# It is useful when you want to stop looping based on a specific condition.

# Basic Example: Stop loop when a number equals 3
for number in range(1, 6):
    if number == 3:
        break  # Exit the loop when number is 3
    print(f"Number: {number}")
# Output: 1, 2

# Intermediate Example: Find the first even number in a list
numbers = [7, 9, 13, 16, 21, 24]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break  # Stop after finding the first even number
# Output: First even number found: 16

# Real World Use Case: Searching for a password in a list
passwords = ["abc123", "letmein", "python123", "secure!", "guest"]
correct_password = "python123"
for pwd in passwords:
    if pwd == correct_password:
        print("Password found! Access granted.")
        break  # Stop searching once the password is found
else:
    print("Password not found. Access denied.")
# Output: Password found! Access granted.

# Summary:
# - 'break' is used to exit a loop early when a condition is met.
# - It works in both for and while loops.
# - Useful for searching, stopping on errors, or ending a process early.

