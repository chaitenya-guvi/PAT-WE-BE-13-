# Loops in Python
# Loops are used to repeat a block of code multiple times. They help automate repetitive tasks and make code more efficient.

# Example without a loop (manual repetition):
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
# This is repetitive and not efficient if you want to print "Hello" 100 times.

# Example with a for loop:
for count in range(5):
    print("Hello")
# The for loop repeats the print statement 5 times.

# Real world use case: Printing all items in a shopping list
shopping_list = ["Milk", "Eggs", "Bread", "Butter"]
for item in shopping_list:
    print("Buy:", item)
# Output:
# Buy: Milk
# Buy: Eggs
# Buy: Bread
# Buy: Butter

# Loops are useful for:
# - Processing items in a list
# - Automating repetitive tasks
# - Performing calculations multiple times
# - Collecting user input repeatedly
# - Many other tasks where repetition is needed

