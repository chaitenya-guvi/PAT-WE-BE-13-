# The 'pass' statement in Python
# ------------------------------
# 'pass' is a null statement. It does nothing when executed.
# It is used as a placeholder in code blocks where a statement is required syntactically, but you don't want any action to be taken.

# Example 1: Empty function definition

def do_nothing():
    pass  # Function does nothing

# Example 2: Empty class definition

class EmptyClass:
    pass  # Class has no attributes or methods

# Example 3: Placeholder in if statement

x = 10
if x > 5:
    pass  # No action for now, but code is syntactically correct
else:
    print("x is not greater than 5")

# Example 4: Placeholder in a loop

for number in range(3):
    pass  # Loop does nothing

# Example 5: Placeholder in exception handling

try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Ignore the error for now

# Summary:
# - 'pass' is useful when you are planning to add code later, or want to leave a block intentionally empty.
# - It helps avoid syntax errors when a statement is required but no action is needed yet.

