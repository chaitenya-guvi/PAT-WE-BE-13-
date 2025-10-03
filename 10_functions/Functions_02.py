"""
we can try to print,
but what if we want to store
the result of a function in a variable?
"""
#
# def say_hi():
#     print('Hello!')
#
#
# result = say_hi()
# print(result)
#
# print(result) # None


"""
 return keyword
 once you return something from a function,
 the function exits
"""
#
def say_hi():
    print('hello!')
    print('hello!')
    return 'Hi!'
    print("never gets executed") # since it is after return statement

say_hi()

print("after the function is saved in a variable ")
greeting  = say_hi()

print(greeting)  # 'Hi!'
