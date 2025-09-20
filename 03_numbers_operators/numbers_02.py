# Arithmetic Operators in Python
# Python supports several arithmetic operators for mathematical calculations:

# 1. Addition (+)
a = 10
b = 3
print("Addition:", a + b)  # Output: 13

# 2. Subtraction (-)
print("Subtraction:", a - b)  # Output: 7

# 3. Multiplication (*)
print("Multiplication:", a * b)  # Output: 30

# 4. Division (/) - can return a float
print("Division:", a / b)  # Output: 3.333...
print("Division can return a float also : ", a / b, "the type of a/b is: ", type(10/3))  #

# 5. Floor Division (//) - returns the integer part of the division
print("Floor Division:", a // b)  # Output: 3
print("Floor Division:", a // b , "type of a / b is : ", type(a/b) )  # Output: 3
print("Floor Division:", a // b , "type of a // b is : ", type(a//b) )  # Output: 3

# 6. Modulus (%) - returns the remainder
print("Modulus:", a % b)  # Output: 1

number = 11
print(number % 2) # Output: 1 (11 is odd, remainder when divided by 2 is 1)
number = 10
print(number % 2) # Output: 0 (10 is even, remainder when divided by 2 is 0)


# 7. Exponentiation (**)
print("Exponentiation:", a ** b)  # Output: 1000
a = 2
b = 4
c = 6

print("Exponentiation:", a ** b)  # Output: 2^4 = 16
print("Exponentiation:", a ** c)  # Output: 2^6 = 64

# These operators work with integers, floats, and can be used in expressions.

