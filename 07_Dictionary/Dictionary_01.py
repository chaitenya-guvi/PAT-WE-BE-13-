# Limitations of Lists and Use Cases for Dictionaries in Python
# ------------------------------------------------------------
# Lists are useful for storing ordered collections of items, but they have limitations:
# 1. Searching for a value in a list can be slow for large lists (linear search).
# 2. Lists do not provide a way to associate a value with a unique key.
# 3. Lists are not ideal for representing data with unique identifiers or fast lookups.

# Dictionaries solve these problems by allowing you to store key-value pairs.
# Dictionaries provide fast lookups, easy updates, and are ideal for mapping relationships.

name = "chaitenya"
pi = 3.14
list1 = [1,2,3,4]
marks =  [12,50,60]
marks_dict = {"science": 12 ,"english" : 50, "maths" : 60 }
# Example 1: Student marks (using dictionary for fast lookup by name)
student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
print("Bob's marks:", student_marks["Bob"])  # Output: 92

# Example 2: Phone book (mapping names to phone numbers)
phone_book = {"John": "123-4567", "Jane": "987-6543", "Tom": "555-1212"}
print("Jane's phone number:", phone_book["Jane"])  # Output: 987-6543


# Summary:
# - Lists are good for ordered data, but slow for searching and lack key-value mapping.
# - Dictionaries are ideal for fast lookups, mapping relationships, and counting/grouping data.
# - Use dictionaries when you need to associate values with unique keys or need fast access.

