"""
sorted
"""
# sorted (works on anything that is iterable)

more_numbers = [6,1,8,2]
print(sorted(more_numbers))
print(more_numbers) # [6, 1, 8, 2]
"""
reversed
Return a reverse iterator.
"""


more_numbers = [6, 1, 8, 2]
reversed(more_numbers) # <list_reverseiterator at 0x1049f7da0>
print(list(reversed(more_numbers))) # [2, 8, 1, 6]
