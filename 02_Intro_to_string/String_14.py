# 7. find() - Finds the first occurrence of a substring
text = "hello world"
print(text.find("world"))  # Output: 6
print(text.find("Python"))  # Output: -1 (not found)

# 8. count() - Counts occurrences of a substring
print(text.count("l"))  # Output: 3
print(text.count("ll"))  # Output: 1

# 9. startswith() - Checks if string starts with a substring
print(text.startswith("hello"))  # Output: True

# 10. endswith() - Checks if string ends with a substring
print(text.endswith("world"))  # Output: True

# 11. capitalize() - Capitalizes the first character
print(text.capitalize())  # Output: 'Hello world'

# 12. title() - Capitalizes the first letter of each word
print(text.title())  # Output: 'Hello World'