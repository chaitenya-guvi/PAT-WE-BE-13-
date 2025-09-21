# While loops require more careful setup than for loops,
# since you have to specify the termination conditions manually.
# If you forget to update the condition or set it incorrectly, you may create an infinite loop.

# Example 1: Correctly set up while loop (counting from 1 to 5)
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Termination condition is updated each iteration
# Output: 1, 2, 3, 4, 5

# Example 2: Incorrectly set up while loop (infinite loop)
# Uncomment the lines below to see the effect
# counter = 1
# while counter <= 5:
#     print(f"Counter is: {counter}")
#     # Missing counter += 1, so the loop never ends
# Output: Will keep printing 'Counter is: 1' forever

# Explanation:
# - In a for loop, the termination is handled automatically by the range or sequence.
# - In a while loop, you must manually update the condition variable and ensure the loop will eventually stop.
# - If you forget to update the variable or set the condition incorrectly, you may create an infinite loop.
# - Always check that your while loop has a clear and reachable termination condition.
