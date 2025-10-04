"""
lambdas in python

- no name functions
- used when we need a small function for a short period of time
- used as an argument to higher order functions (functions that accept other functions as arguments)
- syntax : lambda parameters : expression
- can have any number of parameters but only one expression
- cannot contain commands or multiple expressions
- cannot be used for complex operations
"""
# syntax
# lambda parameters : expression
# example
add = lambda x, y: x + y
print(add(3, 5))  # 8

# example 2
multiply = lambda a, b: a * b
print(multiply(4, 6))  # 24


# example 3
def apply_operation(func, x, y):
    return func(x, y)

result = apply_operation(lambda x, y: x - y, 10, 4)
print(result)  # 6
