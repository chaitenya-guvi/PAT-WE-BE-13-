# The 'break' statement in while loops
# ------------------------------------
# 'break' is used to exit a while loop immediately, even if the loop condition is still True.
# It is useful when you want to stop looping based on a specific condition inside the loop.

# Basic Example: Stop loop when number equals 5
number = 1
while number <= 10:
    if number == 5:
        break  # Exit the loop when number is 5
    print(f"Number: {number}")
    number += 1
# Output: 1, 2, 3, 4

# Real World Use Case: User login attempts
max_attempts = 3
attempts = 0
correct_password = "python123"
while attempts < max_attempts:
    # Simulate user input (replace with input() in real use)
    entered_password = ["abc", "letmein", "python123"][attempts]
    print(f"Attempt {attempts + 1}: Entered password: {entered_password}")
    if entered_password == correct_password:
        print("Access granted!")
        break  # Exit loop if password is correct
    attempts += 1
else:
    print("Access denied. Too many attempts.")
# Output:
# Attempt 1: Entered password: abc
# Attempt 2: Entered password: letmein
# Attempt 3: Entered password: python123
# Access granted!

# Summary:
# - 'break' is used to exit a while loop early when a condition is met.
# - Useful for stopping loops on success, error, or a specific event.
# - Works in both for and while loops.

