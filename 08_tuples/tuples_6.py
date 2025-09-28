# tuples_6.py

# Tuple methods

my_tuple = (1, 2, 3, "hello", True, 2)
print("Original Tuple:", my_tuple)

print("Index of 'hello':", my_tuple.index("hello"))  # Output: 3
print("Index of 2:", my_tuple.index(2))  # Output: 1



print("Count of 2 in tuple:", my_tuple.count(2))  # Output: 1
print("Count of 4 in tuple:", my_tuple.count(4))  # Output: 0

print("Count of 'hello' in tuple:", my_tuple.count("hello"))  # Output: 1
print("Count of 'world' in tuple:", my_tuple.count("world"))  # Output: 0
