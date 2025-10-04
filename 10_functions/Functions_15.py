# Normal functions have names

def first_function():
    return 'Hello!'

first_function() # 'Hello!'

first_function.__name__ # first_function'

# Lambda Functions are nameless functions

first_lambda = lambda x: x + 5

first_lambda(10) # 15

first_lambda.__name__ # '<lambda>'

"""
Syntax : 
lambda arguments: expression


# Lambdas are used when you need a nameless function for a short period of time
# They are often used with functions like map(), filter(), and sorted()
# They are also used when you need to pass a simple function as an argument to another function

"""

# Example 1
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5