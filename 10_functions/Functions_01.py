"""
- A process for executing a task
- It can accept input and return an output
- Useful for executing similar procedures over and over

Stay DRY - Don't Repeat Yourself!
Clean up and prevent code duplication
"Abstract away" code for other users
Imagine if you had to rewrite the "print()" function for every program you wrote


Syntax : 
def name_of_function():
    # block of runnable code
"""

#definihg a function
def say_hi(): # function header
    print('Hi!') # function body
    print('Hi!')

#calling a function
say_hi()
say_hi()
print("outside the function")

# builtin functions
print(len("chaitenya"))  # 9
print(type(3))
print(int("3"))

#user defined functions
say_hi()

# note - please do not create user defined functions with th same name as builtin functions
# for example - print(), len(), type() etc