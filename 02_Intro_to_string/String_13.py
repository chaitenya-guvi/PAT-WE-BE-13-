# 4. replace() - Replaces a substring with another substring
sentence = "I like apples"
print(sentence.replace("apples", "bananas"))  # Output: 'I like bananas'

# 5. split() - Splits a string into a list
csv = "red,green,blue"
print(csv.split(","))  # Output: ['red', 'green', 'blue']

# More examples of split() with default and other characters

# Default split (splits by whitespace)
text = "Python is awesome"
print(text.split())  # Output: ['Python', 'is', 'awesome']

name = "John Doe Smith"
firstname, middlename, lastname = name.split()
print(firstname)  # Output: 'John'
print(middlename) # Output: 'Doe'
print(lastname)   # Output: 'Smith'

address_example = "123 Main St, Springfield, IL"
street, city, state = address_example.split(", ")
print(street)  # Output: '123 Main St'
print(city)    # Output: 'Springfield'
print(state)   # Output: 'IL'

# Split by a specific character (comma)

data = "apple,banana,grape"
print(data.split(","))  # Output: ['apple', 'banana', 'grape']

# Split by another character (dash)
info = "2025-09-20"
print(info.split("-"))  # Output: ['2025', '09', '20']

# Split by multiple spaces
sentence = "Hello    world   Python"
print(sentence.split())  # Output: ['Hello', 'world', 'Python']


# 6. join() - Joins elements of a list into a string
colors = ["red", "green", "blue"]
print("-".join(colors))  # Output: 'red-green-blue'

# Easier examples of join() method

# Join a list of words with a space
words = ["Python", "is", "fun"]
print("%%".join(["Python", "is", "fun"]))  # Output: 'Python is fun'

# Join single characters to form a word
letters = ["C", "o", "d", "e"]
print("".join(letters))  # Output: 'Code'

# Join numbers converted to strings
numbers = ["1", "2", "3"]
print("-".join(numbers))  # Output: '1-2-3'

# Join with a custom separator
fruits = ["apple", "banana", "cherry"]
print(" | ".join(fruits))  # Output: 'apple | banana | cherry'
