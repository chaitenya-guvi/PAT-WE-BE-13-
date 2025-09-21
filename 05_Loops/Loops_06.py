# Loop through numbers 1 to 20 and print messages based on conditions
# For 4 and 13, print "x is unlucky"
# For even numbers, print "x is even"
# For odd numbers, print "x is odd"

for number in range(1, 21):
    # Check for unlucky numbers first
    if number == 4 or number == 13:
        print(f"{number} is unlucky")
    # Check for even numbers
    elif number % 2 == 0:
        print(f"{number} is even")
    # Otherwise, it's odd
    else:
        print(f"{number} is odd")

# Explanation:
# - We use a for loop to iterate through numbers 1 to 20 (inclusive).
# - The variable 'number' represents the current number in the loop.
# - The first condition checks if the number is 4 or 13 and prints a special message.
# - The second condition checks if the number is even using 'number % 2 == 0'.
# - If neither condition is met, the number is odd and prints the corresponding message.
# - The order of conditions is important so that 4 and 13 are not classified as even or odd, but as unlucky.

