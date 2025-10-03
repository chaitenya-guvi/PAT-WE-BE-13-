"""
Sets are like formal mathematical sets.
Sets do not have duplicate values
Elements in sets aren't ordered.
You cannot access items in a set by index.
Sets can be useful if you need to keep track
of a collection of elements, but don't care about ordering, keys or values and duplicates

"""
# Creating a set
#mutable set with mixed data types
my_set = {1, 2, 3, 4, 5}
print("My Set:", my_set)



# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}
print(f"the st has no duplicates : ", s)

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

print(4 in s)
# True

print(8 in s)
# False
