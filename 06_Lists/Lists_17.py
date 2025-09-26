# The count() and reverse() methods for lists in Python
# ----------------------------------------------------
# count() returns the number of times a value appears in a list.
# reverse() reverses the order of elements in a list in place.

# Example 1: Using count() method
numbers = [1, 2, 2, 3, 2, 4, 2]
count_of_2 = numbers.count(2)
print("Count of 2:", count_of_2)  # Output: 4

fruits = ["apple", "banana", "apple", "cherry", "apple"]
count_apple = fruits.count("apple")
print("Count of 'apple':", count_apple)  # Output: 3

for idx , value in enumerate(fruits):
    if value == "apple":
        print(f"Found 'apple' at index: {idx}")

# Example 2: Using reverse() method
colors = ["red", "green", "blue"]
colors.reverse()
print("Reversed colors:", colors)  # Output: ['blue', 'green', 'red']

numbers.reverse()
print("Reversed numbers:", numbers)  # Output: [2, 4, 2, 3, 2, 2, 1]

# Example 3: Using sort() method
# The sort() method arranges the elements of a list in ascending order (by default).
# It modifies the original list in place and does not return a new list.


numbers_to_sort = [5, 2, 9, 1, 7]
numbers_to_sort.sort()
print("Sorted numbers:", numbers_to_sort)  # Output: [1, 2, 5, 7, 9]

fruits_to_sort = ["banana", "apple", "cherry", "date"]
fruits_to_sort.sort()
print("Sorted fruits:", fruits_to_sort)  # Output: ['apple', 'banana', 'cherry', 'date']

# You can also sort in descending order using the reverse=True argument:
numbers_to_sort.sort(reverse=True)
print("Numbers sorted in descending order:", numbers_to_sort)  # Output: [9, 7, 5, 2, 1]

# Summary (updated):
# - count(value) returns the number of times value appears in the list.
# - reverse() reverses the list in place (does not return a new list).
# - sort() arranges the list in ascending order by default, or descending with reverse=True.
# - All three methods are useful for analyzing and manipulating lists.
