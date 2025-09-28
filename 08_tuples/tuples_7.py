# tuples_7.py
# list vs tuple
# Lists are mutable, meaning their elements can be changed, added, or removed.
# Tuples are immutable, meaning once they are created, their elements cannot be changed, added, or removed.

# Lists are defined using square brackets [].
# Tuples are defined using parentheses ().

# Lists are generally used when you need a collection of items that may change during the program's execution.
# Tuples are used when you need a collection of items that should remain constant and not be modified.

# Example of a list
my_list = [1, 2, 3, "hello", True]
print("My List:", my_list)

# Modifying a list
my_list[0] = 10
my_list.append(4)

print("Modified List:", my_list)

# Example of a tuple
my_tuple = (1, 2, 3, "hello", True)
print("My Tuple:", my_tuple)

#when to use list vs tuple
"""
| **Use a List when...**                 | **Use a Tuple when...**                   |
| -------------------------------------- | ----------------------------------------- |
| You need to modify data                | You want to protect data from changes     |
| Order matters and you need flexibility | Order matters but data should be constant |
| You're doing lots of insert/delete     | You're storing fixed config/data          |

"""