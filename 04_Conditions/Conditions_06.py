# Logical Operators to Add Multiple 04_Conditions in Python
# Logical operators allow you to combine multiple conditions in a single statement.
# The main logical operators are: and, or, and not.

# 'and' operator: All conditions must be True
age = 25
has_ticket = True
if age > 18 and has_ticket:
    print("Allowed entry: Age is above 18 and has a ticket.")

# 'or' operator: At least one condition must be True
is_member = False
if age > 18 or is_member:
    print("Allowed entry: Either age is above 18 or is a member.")

# 'not' operator: Reverses the condition
is_banned = False
if not is_banned:
    print("Allowed entry: Not banned.")

# Combining multiple conditions
temperature = 30
weather = "sunny"
if temperature > 25 and weather == "sunny" and not is_banned:
    print("Go outside: Warm, sunny, and not banned.")

# Logical operators are useful for checking several conditions at once in if, elif, and while statements.
# You can combine as many conditions as needed using these operators.

