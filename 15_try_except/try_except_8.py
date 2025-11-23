"""
finally block exmaple :

The finally block is used when you have some code that must run no matter what, such as:

closing files

releasing resources

closing database connections

printing clean-up messages

"""
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error occurred.")
finally:
    print("This will always run.")
