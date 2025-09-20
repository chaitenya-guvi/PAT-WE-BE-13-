# Example of string escape characters:
# 1. Newline (\n)
print("Hello\nWorld")  # Output: Hello (newline) World

# 2. Tab (\t)
print("Hello\tWorld")  # Output: Hello    World

# 3. Backslash (\\)
print("C:\\Users\\LENOVO")  # Output: C:\Users\LENOVO

# 4. Single quote (\') and double quote (\")
print('It\'s Python!')  # Output: It's Python!
print("She said, \"Hello!\"")  # Output: She said, "Hello!"

# Examples of string methods:
# 1. upper() - Converts all characters to uppercase
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.upper())  # Output: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 2. lower() - Converts all characters to lowercase
name = "Python Programming"
print(name.lower())  # Output: 'python programming'

# 3. strip() - Removes leading and trailing whitespace
raw_text = "   Hello World!   "
print(raw_text)
print(raw_text.strip())  # Output: 'Hello World!'