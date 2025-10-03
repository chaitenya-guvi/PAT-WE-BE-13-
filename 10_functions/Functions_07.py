"""
SCOPE
"""

# instructor = 'Chaitenya'
#
# def say_hello():
#     return f'Hello {instructor}'
#
#
# print(say_hello())  #'Hello Chaitenya'



"""

"""
instructor = 'Dinesh'  # global scope
def say_hello():
    instructor = 'Chaitenya'   # the variable is inside the function , # local scope
    return f'Hello {instructor}'


print(instructor) # NameError
print(say_hello())

"""
Unbound Local Error
"""
global_instructor = "Dinesh"  # global scope
def say_hello_updating_global_variable():

    global_instructor += ' Chaitenya'
    return f'Hello {global_instructor}'

say_hello_updating_global_variable()

"""
Global Keyword
"""

global_instructor = "Dinesh"  # global scope
def say_hello_updating_global_variable():
    global global_instructor
    global_instructor += ' Chaitenya'
    return f'Hello {global_instructor}'

print(say_hello_updating_global_variable())
print(global_instructor)  # Dinesh Chaitenya
