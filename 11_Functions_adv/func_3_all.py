"""
Return True if all elements of the iterable are truthy (or if the iterable is empty)
"""

print(all([ 0,1, 2, 3]))

lidt1 = [char for char in 'chaitenya' if char in 'aeiou']

print(all(lidt1))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


# by default in python everything is truthy except 0, None, False, empty collections (like '', (), [], {})

bool('a')
all(['a', 'b', 'c',0,False])