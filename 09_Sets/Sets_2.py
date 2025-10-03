"""
# Summary:
# - Sets are unordered collections of unique elements.
# - They support standard set operations like union, intersection, and difference.
# - Sets are useful for membership testing and eliminating duplicates from a collection.
# - You can create sets using curly braces {} or the set() constructor.
# - Sets are mutable, allowing you to add or remove elements.

"""
my_set = {1, 2, 3, 4, 5}

# Creating a set from a list (duplicates will be removed)
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set_from_list = set(my_list)
print("Set from List (duplicates removed):", my_set_from_list)

# Adding elements to a set
my_set.add(6)
print("Set after adding 6:", my_set)
my_set.add(3)  # Adding a duplicate (will have no effect)
print("Set after trying to add duplicate 3:", my_set)

# Removing elements from a set
my_set.remove(2)  # Raises KeyError if 2 is not found
print("Set after removing 2:", my_set)
my_set.discard(10)  # Does nothing if 10 is not found
print("Set after trying to discard non-existent 10:", my_set)


# Checking membership
print("Is 3 in my_set?", 3 in my_set)  # Output: True
print("Is 10 in my_set?", 10 in my_set)  # Output: False
# Length of a set
print("Length of my_set:", len(my_set))  # Output: Length of the set
my_set = {1, 2, 3, 4, 5}
print("My Set:", my_set)
